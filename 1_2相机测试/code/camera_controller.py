"""
ALVIUM相机控制模块
使用Vimba X Python SDK实现相机连接、配置和图像采集
支持Vimba X SDK (vmbpy 1.2.0+)
"""

import sys
import time
import threading
import queue
import numpy as np
from typing import Optional, Callable
from config import CameraConfig

try:
    from vmbpy import *
except ImportError:
    print("错误: 无法导入vmbpy模块")
    print("请确保已安装Vimba X SDK并正确安装了vmbpy包")
    print("安装命令: pip install vmbpy")
    sys.exit(1)


class CameraController:
    """ALVIUM相机控制器类（适配Vimba X SDK）"""
    
    def __init__(self, frame_callback: Optional[Callable] = None):
        """
        初始化相机控制器
        
        Args:
            frame_callback: 图像帧回调函数，接收numpy数组格式的图像
        """
        self.vmb = VmbSystem.get_instance()
        self.camera: Optional[Camera] = None
        self.frame_callback = frame_callback
        self.is_streaming = False
        self.frame_count = 0
        self.trigger_thread: Optional[threading.Thread] = None
        self.stop_trigger_event = threading.Event()
        self.frame_handler = None
        
    def __enter__(self):
        """上下文管理器入口"""
        self.vmb.__enter__()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出"""
        self.stop_acquisition()
        if self.camera:
            try:
                self.camera.__exit__(exc_type, exc_val, exc_tb)
            except:
                pass
        self.vmb.__exit__(exc_type, exc_val, exc_tb)
        
    def connect_camera(self, camera_id: Optional[str] = None) -> bool:
        """
        连接相机
        
        Args:
            camera_id: 相机ID，如果为None则连接第一个发现的相机
            
        Returns:
            bool: 连接成功返回True，否则返回False
        """
        try:
            # 获取所有可用相机
            cameras = self.vmb.get_all_cameras()
            
            if not cameras:
                print("错误: 未发现任何相机")
                return False
            
            # 选择相机
            if camera_id:
                # 根据ID查找相机
                for cam in cameras:
                    if cam.get_id() == camera_id:
                        self.camera = cam
                        break
                if not self.camera:
                    print(f"错误: 未找到ID为 {camera_id} 的相机")
                    return False
            else:
                # 使用第一个相机
                self.camera = cameras[0]
            
            # 打开相机（尝试完全访问，如果失败则尝试只读）
            try:
                self.camera.__enter__()
            except Exception as e:
                if "already in use" in str(e):
                    print("警告: 相机可能被其他程序占用（如Vimba X Viewer）")
                    print("正在尝试关闭其他程序...")
                    # 等待一下再重试
                    time.sleep(1)
                    try:
                        self.camera.__enter__()
                    except:
                        print("错误: 无法打开相机，请关闭Vimba X Viewer或其他使用相机的程序")
                        return False
                else:
                    raise
            
            print(f"成功连接相机: {self.camera.get_id()}")
            print(f"相机型号: {self.camera.get_model()}")
            
            return True
            
        except Exception as e:
            print(f"连接相机时出错: {e}")
            return False
    
    def configure_camera(self) -> bool:
        """
        配置相机参数（软件触发模式）
        Vimba X SDK使用get_feature_by_name()访问相机特性
        
        Returns:
            bool: 配置成功返回True，否则返回False
        """
        if not self.camera:
            print("错误: 相机未连接")
            return False
            
        try:
            # 设置触发选择器
            try:
                trigger_selector = self.camera.get_feature_by_name('TriggerSelector')
                trigger_selector.set(CameraConfig.TRIGGER_SELECTOR)
            except Exception as e:
                print(f"警告: 无法设置TriggerSelector: {e}")
            
            # 设置触发源
            try:
                trigger_source = self.camera.get_feature_by_name('TriggerSource')
                trigger_source.set(CameraConfig.TRIGGER_SOURCE)
            except Exception as e:
                print(f"警告: 无法设置TriggerSource: {e}")
            
            # 设置触发模式
            try:
                trigger_mode = self.camera.get_feature_by_name('TriggerMode')
                trigger_mode.set(CameraConfig.TRIGGER_MODE)
            except Exception as e:
                print(f"警告: 无法设置TriggerMode: {e}")
            
            # 设置采集模式
            try:
                acquisition_mode = self.camera.get_feature_by_name('AcquisitionMode')
                acquisition_mode.set(CameraConfig.ACQUISITION_MODE)
            except Exception as e:
                print(f"警告: 无法设置AcquisitionMode: {e}")
            
            # 设置曝光时间（如果支持）
            try:
                exposure_time = self.camera.get_feature_by_name('ExposureTime')
                exposure_time.set(CameraConfig.EXPOSURE_TIME)
                print(f"曝光时间设置为: {CameraConfig.EXPOSURE_TIME} 微秒")
            except Exception as e:
                print(f"警告: 无法设置ExposureTime: {e}")
            
            # 设置增益（如果支持）
            try:
                gain = self.camera.get_feature_by_name('Gain')
                gain.set(CameraConfig.GAIN)
                print(f"增益设置为: {CameraConfig.GAIN} dB")
            except Exception as e:
                print(f"警告: 无法设置Gain: {e}")
            
            # 尝试设置像素格式为BGR8（与OpenCV兼容）
            try:
                pixel_format = self.camera.get_feature_by_name('PixelFormat')
                # 尝试获取可用格式
                try:
                    available_formats = pixel_format.get_available_entries()
                    format_names = [fmt.get_name() for fmt in available_formats]
                    print(f"可用像素格式: {format_names}")
                    
                    # 优先选择BGR8，其次是RGB8
                    if 'BGR8' in format_names or 'Bgr8' in format_names:
                        pixel_format.set('BGR8' if 'BGR8' in format_names else 'Bgr8')
                        print("像素格式设置为: BGR8")
                    elif 'RGB8' in format_names or 'Rgb8' in format_names:
                        pixel_format.set('RGB8' if 'RGB8' in format_names else 'Rgb8')
                        print("像素格式设置为: RGB8（将自动转换为BGR）")
                    else:
                        current = pixel_format.get()
                        print(f"使用当前像素格式: {current}")
                except:
                    # 直接尝试设置
                    try:
                        pixel_format.set('BGR8')
                        print("像素格式设置为: BGR8")
                    except:
                        try:
                            pixel_format.set('RGB8')
                            print("像素格式设置为: RGB8（将自动转换为BGR）")
                        except:
                            pass
            except Exception as e:
                print(f"警告: 无法设置PixelFormat: {e}")
            
            print("相机配置完成（软件触发模式）")
            print(f"  触发源: {CameraConfig.TRIGGER_SOURCE}")
            print(f"  触发模式: {CameraConfig.TRIGGER_MODE}")
            print(f"  采集模式: {CameraConfig.ACQUISITION_MODE}")
            
            return True
            
        except Exception as e:
            print(f"配置相机时出错: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _create_frame_handler(self):
        """创建帧处理器"""
        controller = self
        
        class FrameProducer:
            def __init__(self):
                self.frame_count = 0
                
            def __call__(self, cam: Camera, stream: Stream, frame: Frame):
                """帧回调函数"""
                if frame.get_status() == FrameStatus.Complete:
                    try:
                        # 尝试使用as_opencv_image()转换
                        try:
                            frame_bgr = frame.as_opencv_image()
                        except Exception as e:
                            # 如果失败，手动转换
                            # 获取原始图像数据
                            frame_np = frame.as_numpy_ndarray()
                            
                            # 根据像素格式转换
                            pixel_format = frame.get_pixel_format()
                            
                            if 'Rgb' in str(pixel_format):
                                # RGB转BGR
                                import cv2
                                frame_bgr = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)
                            elif 'Bgr' in str(pixel_format):
                                # 已经是BGR
                                frame_bgr = frame_np
                            elif 'Mono' in str(pixel_format) or 'Bayer' in str(pixel_format):
                                # 灰度或Bayer格式，转为BGR
                                import cv2
                                if len(frame_np.shape) == 2:
                                    frame_bgr = cv2.cvtColor(frame_np, cv2.COLOR_GRAY2BGR)
                                else:
                                    frame_bgr = frame_np
                            else:
                                # 其他格式，直接使用
                                frame_bgr = frame_np
                        
                        self.frame_count += 1
                        controller.frame_count = self.frame_count
                        
                        # 调用用户提供的回调函数
                        if controller.frame_callback:
                            controller.frame_callback(frame_bgr)
                            
                    except Exception as e:
                        print(f"处理帧时出错: {e}")
                        import traceback
                        traceback.print_exc()
                
                # 将帧返回给相机
                cam.queue_frame(frame)
        
        return FrameProducer()
    
    def _software_trigger_loop(self):
        """软件触发循环（在独立线程中运行）"""
        print("软件触发线程启动")
        
        while not self.stop_trigger_event.is_set():
            try:
                if self.camera and self.is_streaming:
                    # 发送软件触发（Vimba X SDK使用get_feature_by_name）
                    trigger_software = self.camera.get_feature_by_name('TriggerSoftware')
                    trigger_software.run()
                    
                # 等待一段时间再次触发
                time.sleep(CameraConfig.TRIGGER_INTERVAL)
                
            except Exception as e:
                print(f"软件触发时出错: {e}")
                # 继续运行，不要中断
                time.sleep(CameraConfig.TRIGGER_INTERVAL)
        
        print("软件触发线程停止")
    
    def start_acquisition(self) -> bool:
        """
        开始图像采集
        
        Returns:
            bool: 启动成功返回True，否则返回False
        """
        if not self.camera:
            print("错误: 相机未连接")
            return False
            
        if self.is_streaming:
            print("警告: 相机已在采集中")
            return True
            
        try:
            # 创建帧处理器
            self.frame_handler = self._create_frame_handler()
            
            # 开始流式传输
            self.camera.start_streaming(handler=self.frame_handler, buffer_count=10)
            self.is_streaming = True
            self.frame_count = 0
            
            print("开始图像采集")
            
            # 启动软件触发线程
            self.stop_trigger_event.clear()
            self.trigger_thread = threading.Thread(
                target=self._software_trigger_loop,
                daemon=True
            )
            self.trigger_thread.start()
            
            return True
            
        except Exception as e:
            print(f"启动采集时出错: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def stop_acquisition(self):
        """停止图像采集"""
        if not self.is_streaming:
            return
            
        try:
            # 停止软件触发线程
            if self.trigger_thread and self.trigger_thread.is_alive():
                self.stop_trigger_event.set()
                self.trigger_thread.join(timeout=2.0)
            
            # 停止流式传输
            if self.camera:
                self.camera.stop_streaming()
            
            self.is_streaming = False
            print(f"停止图像采集 (共采集 {self.frame_count} 帧)")
            
        except Exception as e:
            print(f"停止采集时出错: {e}")
    
    def get_frame_count(self) -> int:
        """获取已采集的帧数"""
        return self.frame_count
    
    def is_connected(self) -> bool:
        """检查相机是否已连接"""
        return self.camera is not None
    
    def is_acquiring(self) -> bool:
        """检查相机是否正在采集"""
        return self.is_streaming


# 测试代码
if __name__ == "__main__":
    """相机控制器测试程序"""
    
    def test_frame_callback(frame):
        """测试回调函数"""
        print(f"收到图像帧: {frame.shape}, dtype: {frame.dtype}")
    
    print("=" * 50)
    print("ALVIUM相机控制器测试程序")
    print("=" * 50)
    
    with VmbSystem.get_instance():
        with CameraController(frame_callback=test_frame_callback) as controller:
            # 连接相机
            if not controller.connect_camera():
                print("无法连接相机，退出")
                sys.exit(1)
            
            # 配置相机
            if not controller.configure_camera():
                print("无法配置相机，退出")
                sys.exit(1)
            
            # 开始采集
            if not controller.start_acquisition():
                print("无法启动采集，退出")
                sys.exit(1)
            
            # 采集5秒
            print("\n采集中，持续5秒...")
            time.sleep(5)
            
            # 停止采集
            controller.stop_acquisition()
            
            print("\n测试完成")

