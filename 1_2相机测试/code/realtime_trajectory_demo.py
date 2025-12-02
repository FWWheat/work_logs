"""
实时白色物体轨迹跟踪演示程序
使用ALVIUM相机实时采集图像，检测白色物体并绘制运行轨迹
"""

import sys
import cv2
import numpy as np
import time
from typing import Optional

try:
    from vmbpy import VmbSystem
except ImportError:
    print("警告: 无法导入vmbpy模块")
    print("将使用模拟摄像头模式")
    VmbSystem = None

from camera_controller import CameraController
from trajectory_tracker import EnhancedImageProcessor


class RealtimeTrajectoryDemo:
    """实时轨迹跟踪演示类"""
    
    def __init__(self, use_camera: bool = True):
        """
        初始化演示程序
        
        Args:
            use_camera: 是否使用真实相机（False则使用电脑摄像头）
        """
        self.use_camera = use_camera and VmbSystem is not None
        self.camera_controller: Optional[CameraController] = None
        self.webcam: Optional[cv2.VideoCapture] = None
        
        # 图像处理器
        self.processor = EnhancedImageProcessor(max_trajectory_length=100)
        
        # 最新的图像帧
        self.latest_frame: Optional[np.ndarray] = None
        self.frame_lock = False
        
        # 统计信息
        self.frame_count = 0
        self.start_time = time.time()
        self.fps = 0.0
        
        # 显示选项
        self.show_coordinate = True
        self.show_detection = True
        self.show_trajectory = True
        
    def frame_callback(self, frame: np.ndarray) -> None:
        """相机帧回调函数"""
        if not self.frame_lock:
            self.latest_frame = frame.copy()
            self.frame_count += 1
    
    def setup_camera(self) -> bool:
        """设置相机"""
        if self.use_camera:
            print("正在连接ALVIUM相机...")
            try:
                self.camera_controller = CameraController(frame_callback=self.frame_callback)
                self.camera_controller.__enter__()
                
                if not self.camera_controller.connect_camera():
                    print("无法连接相机，切换到摄像头模式")
                    self.use_camera = False
                    return self.setup_webcam()
                
                if not self.camera_controller.configure_camera():
                    print("无法配置相机")
                    return False
                
                if not self.camera_controller.start_acquisition():
                    print("无法启动采集")
                    return False
                
                print("相机设置完成")
                return True
                
            except Exception as e:
                print(f"相机设置出错: {e}")
                print("切换到摄像头模式")
                self.use_camera = False
                return self.setup_webcam()
        else:
            return self.setup_webcam()
    
    def setup_webcam(self) -> bool:
        """设置电脑摄像头"""
        print("正在打开电脑摄像头...")
        self.webcam = cv2.VideoCapture(0)
        
        if not self.webcam.isOpened():
            print("无法打开摄像头")
            return False
        
        # 设置分辨率
        self.webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        print("摄像头设置完成")
        return True
    
    def get_frame(self) -> Optional[np.ndarray]:
        """获取一帧图像"""
        if self.use_camera:
            # 从相机获取
            if self.latest_frame is not None:
                self.frame_lock = True
                frame = self.latest_frame.copy()
                self.frame_lock = False
                return frame
        else:
            # 从摄像头获取
            ret, frame = self.webcam.read()
            if ret:
                self.frame_count += 1
                return frame
        
        return None
    
    def calculate_fps(self) -> float:
        """计算FPS"""
        elapsed = time.time() - self.start_time
        if elapsed > 0:
            return self.frame_count / elapsed
        return 0.0
    
    def draw_info_panel(self, image: np.ndarray) -> np.ndarray:
        """绘制信息面板"""
        img = image.copy()
        
        # 计算FPS
        self.fps = self.calculate_fps()
        
        # 准备信息文本
        info_lines = [
            f"FPS: {self.fps:.1f}",
            f"Frames: {self.frame_count}",
            f"Objects: {self.processor.get_trajectory_count()}",
            f"Source: {'ALVIUM Camera' if self.use_camera else 'Webcam'}",
            "",
            "Controls:",
            "Q - Quit",
            "C - Clear trajectories",
            "1 - Toggle coordinate",
            "2 - Toggle detection",
            "3 - Toggle trajectory",
            "SPACE - Pause",
        ]
        
        # 绘制半透明背景
        overlay = img.copy()
        cv2.rectangle(overlay, (10, 10), (250, 300), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.7, img, 0.3, 0, img)
        
        # 绘制文本
        y_offset = 30
        for line in info_lines:
            color = (0, 255, 0) if line and not line.startswith("Controls") else (255, 255, 255)
            cv2.putText(
                img, line, (20, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1
            )
            y_offset += 20
        
        # 绘制状态指示器
        status_y = img.shape[0] - 30
        status_items = [
            ("Coordinate", self.show_coordinate, (0, 0, 255)),
            ("Detection", self.show_detection, (0, 255, 0)),
            ("Trajectory", self.show_trajectory, (255, 0, 0)),
        ]
        
        x_offset = 20
        for name, enabled, color in status_items:
            text = f"{name}: {'ON' if enabled else 'OFF'}"
            text_color = color if enabled else (100, 100, 100)
            cv2.putText(
                img, text, (x_offset, status_y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1
            )
            x_offset += 150
        
        return img
    
    def run(self) -> None:
        """运行演示程序"""
        print("=" * 70)
        print(" " * 15 + "实时白色物体轨迹跟踪演示")
        print("=" * 70)
        print()
        
        # 设置相机或摄像头
        if not self.setup_camera():
            print("无法初始化图像采集设备")
            return
        
        print("\n开始实时跟踪...")
        print("=" * 70)
        print()
        
        # 主循环
        paused = False
        window_name = "Real-time Trajectory Tracking"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, 1280, 720)
        
        try:
            while True:
                # 获取图像帧
                if not paused:
                    frame = self.get_frame()
                    
                    if frame is None:
                        print("无法获取图像帧")
                        time.sleep(0.1)
                        continue
                    
                    # 处理图像并绘制轨迹
                    processed_frame, centers = self.processor.process_frame_with_trajectory(
                        frame,
                        draw_coordinate=self.show_coordinate,
                        draw_detection=self.show_detection,
                        draw_trajectory=self.show_trajectory
                    )
                    
                    # 绘制信息面板
                    display_frame = self.draw_info_panel(processed_frame)
                    
                    # 显示图像
                    cv2.imshow(window_name, display_frame)
                
                # 处理按键
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord('q'):
                    print("\n正在退出...")
                    break
                elif key == ord('c'):
                    self.processor.clear_trajectories()
                    print("轨迹已清空")
                elif key == ord('1'):
                    self.show_coordinate = not self.show_coordinate
                    print(f"坐标系显示: {'开' if self.show_coordinate else '关'}")
                elif key == ord('2'):
                    self.show_detection = not self.show_detection
                    print(f"检测结果显示: {'开' if self.show_detection else '关'}")
                elif key == ord('3'):
                    self.show_trajectory = not self.show_trajectory
                    print(f"轨迹显示: {'开' if self.show_trajectory else '关'}")
                elif key == ord(' '):
                    paused = not paused
                    print(f"{'已暂停' if paused else '继续运行'}")
        
        except KeyboardInterrupt:
            print("\n程序被用户中断")
        
        finally:
            # 清理资源
            cv2.destroyAllWindows()
            
            if self.use_camera and self.camera_controller:
                self.camera_controller.stop_acquisition()
                self.camera_controller.__exit__(None, None, None)
            
            if self.webcam:
                self.webcam.release()
            
            # 打印统计信息
            print()
            print("=" * 70)
            print("统计信息:")
            print(f"  总帧数: {self.frame_count}")
            print(f"  运行时间: {time.time() - self.start_time:.2f} 秒")
            print(f"  平均FPS: {self.fps:.1f}")
            print(f"  跟踪对象数: {self.processor.get_trajectory_count()}")
            print("=" * 70)


def main():
    """主函数"""
    # 检查命令行参数
    use_camera = True
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--webcam':
            use_camera = False
            print("使用摄像头模式")
        elif sys.argv[1] == '--help':
            print("使用方法:")
            print("  python realtime_trajectory_demo.py         # 使用ALVIUM相机")
            print("  python realtime_trajectory_demo.py --webcam  # 使用电脑摄像头")
            return
    
    # 创建并运行演示程序
    if use_camera and VmbSystem is None:
        print("vmbpy模块未安装，将使用摄像头模式")
        use_camera = False
    
    demo = RealtimeTrajectoryDemo(use_camera=use_camera)
    demo.run()


if __name__ == "__main__":
    main()

