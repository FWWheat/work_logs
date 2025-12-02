"""
GUI应用程序
使用Tkinter创建图形用户界面，整合相机控制和图像处理
"""

import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk
import threading
import queue
import time
from typing import Optional

from config import GUIConfig
from camera_controller import CameraController
from image_processor import ImageProcessor

try:
    from vmbpy import VmbSystem
except ImportError:
    print("错误: 无法导入vmbpy模块")
    print("请确保已安装Vimba X SDK并正确安装了vmbpy包")


class CameraApp:
    """相机应用程序GUI类"""
    
    def __init__(self, root: tk.Tk):
        """
        初始化应用程序
        
        Args:
            root: Tkinter根窗口
        """
        self.root = root
        self.root.title(GUIConfig.WINDOW_TITLE)
        self.root.geometry(f"{GUIConfig.WINDOW_WIDTH}x{GUIConfig.WINDOW_HEIGHT}")
        
        # 相机和处理器
        self.vimba = None
        self.camera_controller: Optional[CameraController] = None
        self.image_processor = ImageProcessor()
        
        # 图像队列（线程安全）
        self.image_queue = queue.Queue(maxsize=10)
        
        # 状态变量
        self.is_running = False
        self.fps = 0.0
        self.frame_count = 0
        self.last_fps_time = time.time()
        self.last_fps_count = 0
        
        # 创建GUI组件
        self._create_widgets()
        
        # 绑定窗口关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # 启动图像更新循环
        self._update_image()
        self._update_status()
    
    def _create_widgets(self):
        """创建GUI组件"""
        # 顶部控制面板
        control_frame = tk.Frame(self.root, bg='lightgray', height=60)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # 开始按钮
        self.btn_start = tk.Button(
            control_frame,
            text="开始采集",
            command=self.start_acquisition,
            width=GUIConfig.BUTTON_WIDTH,
            height=GUIConfig.BUTTON_HEIGHT,
            bg='green',
            fg='white',
            font=('Arial', 10, 'bold')
        )
        self.btn_start.pack(side=tk.LEFT, padx=5, pady=5)
        
        # 停止按钮
        self.btn_stop = tk.Button(
            control_frame,
            text="停止采集",
            command=self.stop_acquisition,
            width=GUIConfig.BUTTON_WIDTH,
            height=GUIConfig.BUTTON_HEIGHT,
            bg='red',
            fg='white',
            font=('Arial', 10, 'bold'),
            state=tk.DISABLED
        )
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=5)
        
        # 退出按钮
        self.btn_exit = tk.Button(
            control_frame,
            text="退出程序",
            command=self.on_closing,
            width=GUIConfig.BUTTON_WIDTH,
            height=GUIConfig.BUTTON_HEIGHT,
            bg='gray',
            fg='white',
            font=('Arial', 10, 'bold')
        )
        self.btn_exit.pack(side=tk.RIGHT, padx=5, pady=5)
        
        # 中间图像显示区域
        canvas_frame = tk.Frame(self.root, bg='black')
        canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(
            canvas_frame,
            width=GUIConfig.CANVAS_WIDTH,
            height=GUIConfig.CANVAS_HEIGHT,
            bg='black'
        )
        self.canvas.pack()
        
        # 底部状态栏
        status_frame = tk.Frame(self.root, bg='lightgray', height=30)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        # 状态标签
        self.lbl_status = tk.Label(
            status_frame,
            text="状态: 未连接",
            font=GUIConfig.STATUS_FONT,
            bg='lightgray',
            anchor='w'
        )
        self.lbl_status.pack(side=tk.LEFT, padx=10)
        
        self.lbl_fps = tk.Label(
            status_frame,
            text="FPS: 0.0",
            font=GUIConfig.STATUS_FONT,
            bg='lightgray'
        )
        self.lbl_fps.pack(side=tk.LEFT, padx=10)
        
        self.lbl_detection = tk.Label(
            status_frame,
            text="检测: 0 个方块",
            font=GUIConfig.STATUS_FONT,
            bg='lightgray'
        )
        self.lbl_detection.pack(side=tk.LEFT, padx=10)
        
        self.lbl_frames = tk.Label(
            status_frame,
            text="总帧数: 0",
            font=GUIConfig.STATUS_FONT,
            bg='lightgray'
        )
        self.lbl_frames.pack(side=tk.RIGHT, padx=10)
    
    def _frame_callback(self, frame: np.ndarray):
        """
        相机帧回调函数
        
        Args:
            frame: OpenCV格式的图像帧
        """
        try:
            # 将帧放入队列（非阻塞）
            if not self.image_queue.full():
                self.image_queue.put(frame, block=False)
            
            self.frame_count += 1
            
        except queue.Full:
            pass  # 队列满时忽略
    
    def _update_image(self):
        """更新图像显示（在主线程中运行）"""
        try:
            # 从队列获取图像
            if not self.image_queue.empty():
                frame = self.image_queue.get(block=False)
                
                # 图像处理
                processed_frame, centers = self.image_processor.process_image(frame)
                
                # 调整图像大小以适应画布
                h, w = processed_frame.shape[:2]
                canvas_w = GUIConfig.CANVAS_WIDTH
                canvas_h = GUIConfig.CANVAS_HEIGHT
                
                # 计算缩放比例
                scale = min(canvas_w / w, canvas_h / h)
                new_w = int(w * scale)
                new_h = int(h * scale)
                
                resized = cv2.resize(processed_frame, (new_w, new_h))
                
                # 转换为Tkinter格式
                rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(rgb)
                tk_image = ImageTk.PhotoImage(image=pil_image)
                
                # 更新画布
                self.canvas.delete("all")
                x_offset = (canvas_w - new_w) // 2
                y_offset = (canvas_h - new_h) // 2
                self.canvas.create_image(x_offset, y_offset, anchor=tk.NW, image=tk_image)
                
                # 保持引用（防止被垃圾回收）
                self.canvas.image = tk_image
                
        except queue.Empty:
            pass
        except Exception as e:
            print(f"更新图像时出错: {e}")
        
        # 继续更新循环
        self.root.after(GUIConfig.UPDATE_INTERVAL, self._update_image)
    
    def _update_status(self):
        """更新状态栏信息"""
        try:
            # 计算FPS
            current_time = time.time()
            elapsed = current_time - self.last_fps_time
            
            if elapsed >= 1.0:  # 每秒更新一次FPS
                frame_diff = self.frame_count - self.last_fps_count
                self.fps = frame_diff / elapsed
                
                self.last_fps_time = current_time
                self.last_fps_count = self.frame_count
                
                # 更新FPS标签
                self.lbl_fps.config(text=f"FPS: {self.fps:.1f}")
            
            # 更新检测数量
            detection_count = self.image_processor.get_detected_count()
            self.lbl_detection.config(text=f"检测: {detection_count} 个方块")
            
            # 更新总帧数
            self.lbl_frames.config(text=f"总帧数: {self.frame_count}")
            
        except Exception as e:
            print(f"更新状态时出错: {e}")
        
        # 继续更新循环
        self.root.after(GUIConfig.STATUS_UPDATE_INTERVAL, self._update_status)
    
    def start_acquisition(self):
        """开始图像采集"""
        if self.is_running:
            messagebox.showwarning("警告", "相机已在采集中")
            return
        
        try:
            # 初始化Vimba X
            if not self.vimba:
                self.vimba = VmbSystem.get_instance()
                self.vimba.__enter__()
            
            # 创建相机控制器
            self.camera_controller = CameraController(frame_callback=self._frame_callback)
            self.camera_controller.__enter__()
            
            # 连接相机
            self.lbl_status.config(text="状态: 正在连接相机...")
            self.root.update()
            
            if not self.camera_controller.connect_camera():
                messagebox.showerror("错误", "无法连接相机，请检查相机是否已连接并安装Vimba驱动")
                self._cleanup_camera()
                return
            
            # 配置相机
            self.lbl_status.config(text="状态: 正在配置相机...")
            self.root.update()
            
            if not self.camera_controller.configure_camera():
                messagebox.showerror("错误", "无法配置相机")
                self._cleanup_camera()
                return
            
            # 开始采集
            self.lbl_status.config(text="状态: 正在启动采集...")
            self.root.update()
            
            if not self.camera_controller.start_acquisition():
                messagebox.showerror("错误", "无法启动采集")
                self._cleanup_camera()
                return
            
            # 更新状态
            self.is_running = True
            self.frame_count = 0
            self.last_fps_count = 0
            self.last_fps_time = time.time()
            
            self.btn_start.config(state=tk.DISABLED)
            self.btn_stop.config(state=tk.NORMAL)
            self.lbl_status.config(text="状态: 采集中")
            
            print("图像采集已启动")
            
        except Exception as e:
            messagebox.showerror("错误", f"启动采集时出错: {e}")
            self._cleanup_camera()
    
    def stop_acquisition(self):
        """停止图像采集"""
        if not self.is_running:
            return
        
        try:
            self.lbl_status.config(text="状态: 正在停止采集...")
            self.root.update()
            
            # 停止相机采集
            if self.camera_controller:
                self.camera_controller.stop_acquisition()
            
            # 清理资源
            self._cleanup_camera()
            
            # 更新状态
            self.is_running = False
            self.btn_start.config(state=tk.NORMAL)
            self.btn_stop.config(state=tk.DISABLED)
            self.lbl_status.config(text="状态: 已停止")
            
            print("图像采集已停止")
            
        except Exception as e:
            messagebox.showerror("错误", f"停止采集时出错: {e}")
    
    def _cleanup_camera(self):
        """清理相机资源"""
        try:
            if self.camera_controller:
                self.camera_controller.__exit__(None, None, None)
                self.camera_controller = None
            
            # 清空图像队列
            while not self.image_queue.empty():
                try:
                    self.image_queue.get(block=False)
                except queue.Empty:
                    break
                    
        except Exception as e:
            print(f"清理相机资源时出错: {e}")
    
    def on_closing(self):
        """窗口关闭事件处理"""
        if self.is_running:
            if messagebox.askokcancel("退出", "相机正在采集中，确定要退出吗？"):
                self.stop_acquisition()
                self._cleanup_vimba()
                self.root.destroy()
        else:
            self._cleanup_vimba()
            self.root.destroy()
    
    def _cleanup_vimba(self):
        """清理Vimba X资源"""
        try:
            if self.vimba:
                self.vimba.__exit__(None, None, None)
                self.vimba = None
        except Exception as e:
            print(f"清理Vimba X资源时出错: {e}")


def main():
    """主函数"""
    print("=" * 60)
    print("ALVIUM相机实时采集与检测程序")
    print("=" * 60)
    print("\n使用说明:")
    print("1. 点击'开始采集'按钮连接相机并开始采集")
    print("2. 程序会实时显示图像并检测白色方块")
    print("3. 检测到的方块会用绿色轮廓标注，中心点用红色标记")
    print("4. 坐标系: 原点在左上角，X向右(红色)，Y向下(蓝色)")
    print("5. 点击'停止采集'按钮停止采集")
    print("6. 点击'退出程序'或关闭窗口退出程序")
    print("\n" + "=" * 60 + "\n")
    
    # 创建Tkinter窗口
    root = tk.Tk()
    
    # 创建应用程序
    app = CameraApp(root)
    
    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    main()

