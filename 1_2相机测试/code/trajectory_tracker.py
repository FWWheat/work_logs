"""
物体轨迹跟踪模块
实现白色物体的实时轨迹追踪和绘制
"""

import cv2
import numpy as np
from collections import deque
from typing import List, Tuple, Dict, Optional
from config import DetectionConfig, CoordinateConfig


class TrajectoryTracker:
    """轨迹跟踪器类"""
    
    def __init__(self, max_trajectory_length: int = 100, min_distance: float = 10.0):
        """
        初始化轨迹跟踪器
        
        Args:
            max_trajectory_length: 轨迹最大长度（保存多少个历史点）
            min_distance: 两点之间最小距离，小于此值视为同一位置（像素）
        """
        self.max_trajectory_length = max_trajectory_length
        self.min_distance = min_distance
        
        # 存储所有跟踪对象的轨迹 {object_id: deque([(x, y), ...])}
        self.trajectories: Dict[int, deque] = {}
        
        # 当前帧检测到的中心点
        self.current_centers: List[Tuple[int, int]] = []
        
        # 下一个可用的对象ID
        self.next_id = 0
        
        # 对象ID到颜色的映射（为每个对象分配不同颜色）
        self.colors: Dict[int, Tuple[int, int, int]] = {}
        
        # 预定义的颜色列表
        self.color_palette = [
            (255, 0, 0),    # 蓝色
            (0, 255, 0),    # 绿色
            (0, 0, 255),    # 红色
            (255, 255, 0),  # 青色
            (255, 0, 255),  # 品红色
            (0, 255, 255),  # 黄色
            (128, 0, 128),  # 紫色
            (255, 165, 0),  # 橙色
        ]
        
    def _distance(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
        """计算两点之间的欧氏距离"""
        return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def _get_color_for_id(self, object_id: int) -> Tuple[int, int, int]:
        """为对象ID分配颜色"""
        if object_id not in self.colors:
            # 循环使用颜色列表
            self.colors[object_id] = self.color_palette[object_id % len(self.color_palette)]
        return self.colors[object_id]
    
    def update(self, centers: List[Tuple[int, int]]) -> None:
        """
        更新轨迹跟踪器
        
        Args:
            centers: 当前帧检测到的中心点列表 [(x1, y1), (x2, y2), ...]
        """
        self.current_centers = centers
        
        if not centers:
            return
        
        # 如果是第一次检测或没有现有轨迹，创建新轨迹
        if not self.trajectories:
            for center in centers:
                self.trajectories[self.next_id] = deque([center], maxlen=self.max_trajectory_length)
                self.next_id += 1
            return
        
        # 匹配当前检测点与现有轨迹
        # 使用简单的最近邻匹配
        matched_ids = set()
        matched_centers = set()
        
        # 对每个现有轨迹，找到最近的新检测点
        for obj_id, trajectory in list(self.trajectories.items()):
            if not trajectory:
                continue
                
            last_point = trajectory[-1]
            min_dist = float('inf')
            closest_center = None
            closest_idx = -1
            
            for idx, center in enumerate(centers):
                if idx in matched_centers:
                    continue
                dist = self._distance(last_point, center)
                if dist < min_dist:
                    min_dist = dist
                    closest_center = center
                    closest_idx = idx
            
            # 如果找到足够近的点，更新轨迹
            if closest_center and min_dist < 100:  # 最大匹配距离100像素
                # 只有当新位置与上一个位置距离足够远时才添加
                if self._distance(last_point, closest_center) >= self.min_distance:
                    trajectory.append(closest_center)
                matched_ids.add(obj_id)
                matched_centers.add(closest_idx)
        
        # 为未匹配的检测点创建新轨迹
        for idx, center in enumerate(centers):
            if idx not in matched_centers:
                self.trajectories[self.next_id] = deque([center], maxlen=self.max_trajectory_length)
                self.next_id += 1
    
    def draw_trajectories(self, image: np.ndarray, 
                         draw_points: bool = True,
                         draw_lines: bool = True,
                         draw_current: bool = True) -> np.ndarray:
        """
        在图像上绘制轨迹
        
        Args:
            image: 输入图像 (BGR格式)
            draw_points: 是否绘制轨迹点
            draw_lines: 是否绘制轨迹线
            draw_current: 是否突出显示当前位置
            
        Returns:
            绘制了轨迹的图像
        """
        img = image.copy()
        
        for obj_id, trajectory in self.trajectories.items():
            if len(trajectory) < 2:
                continue
            
            color = self._get_color_for_id(obj_id)
            points = list(trajectory)
            
            # 绘制轨迹线
            if draw_lines:
                for i in range(len(points) - 1):
                    # 使用渐变透明度，越老的点越透明
                    alpha = (i + 1) / len(points)
                    thickness = max(1, int(3 * alpha))
                    cv2.line(img, points[i], points[i + 1], color, thickness)
            
            # 绘制轨迹点
            if draw_points:
                for i, point in enumerate(points):
                    # 使用渐变大小，越老的点越小
                    alpha = (i + 1) / len(points)
                    radius = max(1, int(4 * alpha))
                    cv2.circle(img, point, radius, color, -1)
            
            # 突出显示当前位置
            if draw_current and points:
                current_point = points[-1]
                # 绘制大圆圈
                cv2.circle(img, current_point, 8, color, 2)
                # 绘制实心中心点
                cv2.circle(img, current_point, 3, color, -1)
                
                # 显示对象ID和坐标
                coord_x = current_point[0] - CoordinateConfig.ORIGIN_X
                coord_y = current_point[1] - CoordinateConfig.ORIGIN_Y
                text = f"ID{obj_id}: ({coord_x},{coord_y})"
                
                # 文字位置
                text_x = current_point[0] + 15
                text_y = current_point[1] - 15
                
                # 绘制文字背景
                (text_width, text_height), _ = cv2.getTextSize(
                    text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1
                )
                cv2.rectangle(
                    img,
                    (text_x - 2, text_y - text_height - 2),
                    (text_x + text_width + 2, text_y + 2),
                    (0, 0, 0),
                    -1
                )
                
                # 绘制文字
                cv2.putText(
                    img, text, (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1
                )
        
        return img
    
    def get_trajectory_count(self) -> int:
        """获取当前跟踪的轨迹数量"""
        return len(self.trajectories)
    
    def get_trajectories(self) -> Dict[int, List[Tuple[int, int]]]:
        """获取所有轨迹数据"""
        return {obj_id: list(trajectory) for obj_id, trajectory in self.trajectories.items()}
    
    def clear_trajectories(self) -> None:
        """清空所有轨迹"""
        self.trajectories.clear()
        self.colors.clear()
        self.next_id = 0
        self.current_centers.clear()
    
    def remove_old_trajectories(self, max_frames_missing: int = 30) -> None:
        """
        移除长时间没有更新的轨迹
        
        Args:
            max_frames_missing: 最大允许缺失的帧数
        """
        # 这个功能需要配合帧计数器使用
        # 简化版本：移除空轨迹
        to_remove = [obj_id for obj_id, traj in self.trajectories.items() if not traj]
        for obj_id in to_remove:
            del self.trajectories[obj_id]
            if obj_id in self.colors:
                del self.colors[obj_id]


class EnhancedImageProcessor:
    """增强型图像处理器（包含轨迹跟踪功能）"""
    
    def __init__(self, max_trajectory_length: int = 100):
        """
        初始化增强型图像处理器
        
        Args:
            max_trajectory_length: 轨迹最大长度
        """
        # 导入基础图像处理器
        from image_processor import ImageProcessor
        self.base_processor = ImageProcessor()
        
        # 创建轨迹跟踪器
        self.tracker = TrajectoryTracker(max_trajectory_length=max_trajectory_length)
        
    def detect_white_objects(self, image: np.ndarray) -> List[Tuple[int, int]]:
        """检测白色物体"""
        return self.base_processor.detect_white_squares(image)
    
    def process_frame_with_trajectory(self, image: np.ndarray,
                                     draw_coordinate: bool = True,
                                     draw_detection: bool = True,
                                     draw_trajectory: bool = True) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
        """
        处理图像帧并绘制轨迹
        
        Args:
            image: 输入图像 (BGR格式)
            draw_coordinate: 是否绘制坐标系
            draw_detection: 是否绘制检测结果
            draw_trajectory: 是否绘制轨迹
            
        Returns:
            (处理后的图像, 检测到的中心点列表)
        """
        img = image.copy()
        
        # 1. 检测白色物体
        centers = self.detect_white_objects(img)
        
        # 2. 更新轨迹跟踪器
        if centers:
            self.tracker.update(centers)
        
        # 3. 绘制坐标系
        if draw_coordinate:
            img = self.base_processor.draw_coordinate_system(img)
        
        # 4. 绘制检测结果（轮廓）
        if draw_detection:
            img = self.base_processor.draw_detection_results(img)
        
        # 5. 绘制轨迹
        if draw_trajectory:
            img = self.tracker.draw_trajectories(img)
        
        return img, centers
    
    def clear_trajectories(self) -> None:
        """清空所有轨迹"""
        self.tracker.clear_trajectories()
    
    def get_trajectory_count(self) -> int:
        """获取当前跟踪的轨迹数量"""
        return self.tracker.get_trajectory_count()


# 测试代码
if __name__ == "__main__":
    """轨迹跟踪器测试程序"""
    import sys
    
    print("=" * 50)
    print("轨迹跟踪器测试程序")
    print("=" * 50)
    
    # 创建测试序列
    # 模拟一个物体从左上角移动到右下角
    def create_test_frame(step: int, total_steps: int = 50) -> np.ndarray:
        """创建测试帧"""
        img = np.ones((600, 800, 3), dtype=np.uint8) * 50  # 深灰色背景
        
        # 物体1：从左上到右下
        x1 = int(100 + (500 * step / total_steps))
        y1 = int(100 + (400 * step / total_steps))
        cv2.circle(img, (x1, y1), 20, (255, 255, 255), -1)
        
        # 物体2：从右上到左下
        x2 = int(700 - (500 * step / total_steps))
        y2 = int(100 + (400 * step / total_steps))
        cv2.circle(img, (x2, y2), 20, (255, 255, 255), -1)
        
        return img
    
    # 创建处理器
    processor = EnhancedImageProcessor(max_trajectory_length=50)
    
    print("\n正在生成测试序列并跟踪轨迹...")
    print("按 'q' 键退出，按 'c' 键清空轨迹")
    
    total_steps = 50
    step = 0
    paused = False
    
    while True:
        # 创建测试帧
        test_frame = create_test_frame(step, total_steps)
        
        # 处理帧
        result_frame, centers = processor.process_frame_with_trajectory(test_frame)
        
        # 显示信息
        info_text = f"Step: {step}/{total_steps} | Objects: {len(centers)} | Trajectories: {processor.get_trajectory_count()}"
        cv2.putText(
            result_frame, info_text, (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
        )
        
        cv2.putText(
            result_frame, "Press 'q' to quit, 'c' to clear, SPACE to pause", (10, 560),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1
        )
        
        # 显示结果
        cv2.imshow("Trajectory Tracking Test", result_frame)
        
        # 处理按键
        key = cv2.waitKey(50) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            processor.clear_trajectories()
            print("轨迹已清空")
        elif key == ord(' '):
            paused = not paused
            print("已暂停" if paused else "继续播放")
        
        # 更新步骤
        if not paused:
            step += 1
            if step >= total_steps:
                step = 0  # 循环播放
    
    cv2.destroyAllWindows()
    print("\n测试完成")

