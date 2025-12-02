"""
图像处理模块
实现坐标系绘制、白色方块检测和结果标注
"""

import cv2
import numpy as np
from typing import List, Tuple, Optional
from config import CoordinateConfig, DetectionConfig


class ImageProcessor:
    """图像处理器类"""
    
    def __init__(self):
        """初始化图像处理器"""
        self.detected_squares = []  # 存储检测到的方块信息
        
    def draw_coordinate_system(self, image: np.ndarray) -> np.ndarray:
        """
        在图像上绘制坐标系
        
        Args:
            image: 输入图像 (BGR格式)
            
        Returns:
            绘制了坐标系的图像
        """
        img = image.copy()
        
        # 获取配置参数
        origin_x = CoordinateConfig.ORIGIN_X
        origin_y = CoordinateConfig.ORIGIN_Y
        axis_len_x = CoordinateConfig.AXIS_LENGTH_X
        axis_len_y = CoordinateConfig.AXIS_LENGTH_Y
        
        # 计算坐标轴终点
        x_end = origin_x + axis_len_x
        y_end = origin_y + axis_len_y
        
        # 确保不超出图像边界
        x_end = min(x_end, image.shape[1] - 20)
        y_end = min(y_end, image.shape[0] - 20)
        
        # 绘制X轴（红色，向右）
        cv2.arrowedLine(
            img,
            (origin_x, origin_y),
            (x_end, origin_y),
            CoordinateConfig.X_AXIS_COLOR,
            CoordinateConfig.AXIS_THICKNESS,
            tipLength=0.02
        )
        
        # 绘制Y轴（蓝色，向下）
        cv2.arrowedLine(
            img,
            (origin_x, origin_y),
            (origin_x, y_end),
            CoordinateConfig.Y_AXIS_COLOR,
            CoordinateConfig.AXIS_THICKNESS,
            tipLength=0.02
        )
        
        # 绘制X轴刻度
        tick_interval = CoordinateConfig.TICK_INTERVAL
        for i in range(0, axis_len_x + 1, tick_interval):
            x = origin_x + i
            if x > x_end:
                break
            # 刻度线
            cv2.line(
                img,
                (x, origin_y - CoordinateConfig.TICK_LENGTH // 2),
                (x, origin_y + CoordinateConfig.TICK_LENGTH // 2),
                CoordinateConfig.X_AXIS_COLOR,
                CoordinateConfig.TICK_THICKNESS
            )
            # 刻度值
            if i > 0:  # 不在原点显示0
                cv2.putText(
                    img,
                    str(i),
                    (x - 10, origin_y - 15),
                    CoordinateConfig.FONT,
                    CoordinateConfig.FONT_SCALE,
                    CoordinateConfig.FONT_COLOR,
                    CoordinateConfig.FONT_THICKNESS
                )
        
        # 绘制Y轴刻度
        for i in range(0, axis_len_y + 1, tick_interval):
            y = origin_y + i
            if y > y_end:
                break
            # 刻度线
            cv2.line(
                img,
                (origin_x - CoordinateConfig.TICK_LENGTH // 2, y),
                (origin_x + CoordinateConfig.TICK_LENGTH // 2, y),
                CoordinateConfig.Y_AXIS_COLOR,
                CoordinateConfig.TICK_THICKNESS
            )
            # 刻度值
            if i > 0:  # 不在原点显示0
                cv2.putText(
                    img,
                    str(i),
                    (origin_x - 35, y + 5),
                    CoordinateConfig.FONT,
                    CoordinateConfig.FONT_SCALE,
                    CoordinateConfig.FONT_COLOR,
                    CoordinateConfig.FONT_THICKNESS
                )
        
        # 绘制原点标记
        cv2.circle(img, (origin_x, origin_y), 3, (255, 255, 255), -1)
        cv2.putText(
            img,
            "O(0,0)",
            (origin_x + 5, origin_y - 5),
            CoordinateConfig.FONT,
            CoordinateConfig.FONT_SCALE,
            CoordinateConfig.FONT_COLOR,
            CoordinateConfig.FONT_THICKNESS
        )
        
        # 绘制轴标签
        cv2.putText(
            img,
            CoordinateConfig.X_AXIS_LABEL,
            (x_end + 10, origin_y + 5),
            CoordinateConfig.FONT,
            CoordinateConfig.FONT_SCALE + 0.2,
            CoordinateConfig.X_AXIS_COLOR,
            CoordinateConfig.FONT_THICKNESS + 1
        )
        
        cv2.putText(
            img,
            CoordinateConfig.Y_AXIS_LABEL,
            (origin_x - 5, y_end + 20),
            CoordinateConfig.FONT,
            CoordinateConfig.FONT_SCALE + 0.2,
            CoordinateConfig.Y_AXIS_COLOR,
            CoordinateConfig.FONT_THICKNESS + 1
        )
        
        return img
    
    def detect_white_squares(self, image: np.ndarray) -> List[Tuple[int, int]]:
        """
        检测图像中的白色方块
        
        Args:
            image: 输入图像 (BGR格式)
            
        Returns:
            检测到的方块中心坐标列表 [(x1, y1), (x2, y2), ...]
        """
        # 转换到HSV色彩空间
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # 创建白色掩码
        lower = np.array(DetectionConfig.HSV_LOWER)
        upper = np.array(DetectionConfig.HSV_UPPER)
        mask = cv2.inRange(hsv, lower, upper)
        
        # 形态学操作去除噪点
        kernel = np.ones(
            (DetectionConfig.MORPH_KERNEL_SIZE, DetectionConfig.MORPH_KERNEL_SIZE),
            np.uint8
        )
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        # 查找轮廓
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )
        
        # 过滤并计算中心点
        centers = []
        self.detected_squares = []  # 清空之前的检测结果
        
        for contour in contours:
            area = cv2.contourArea(contour)
            
            # 面积过滤
            if DetectionConfig.MIN_AREA <= area <= DetectionConfig.MAX_AREA:
                # 计算轮廓矩
                M = cv2.moments(contour)
                
                if M["m00"] != 0:
                    # 计算中心坐标
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    
                    centers.append((cx, cy))
                    
                    # 存储完整信息（包含轮廓）
                    self.detected_squares.append({
                        'center': (cx, cy),
                        'contour': contour,
                        'area': area
                    })
        
        return centers
    
    def pixel_to_coordinate(self, pixel_x: int, pixel_y: int) -> Tuple[int, int]:
        """
        将像素坐标转换为坐标系坐标
        
        Args:
            pixel_x: 像素X坐标
            pixel_y: 像素Y坐标
            
        Returns:
            坐标系坐标 (coord_x, coord_y)
        """
        coord_x = pixel_x - CoordinateConfig.ORIGIN_X
        coord_y = pixel_y - CoordinateConfig.ORIGIN_Y
        return (coord_x, coord_y)
    
    def draw_detection_results(self, image: np.ndarray) -> np.ndarray:
        """
        在图像上绘制检测结果
        
        Args:
            image: 输入图像 (BGR格式)
            
        Returns:
            标注了检测结果的图像
        """
        img = image.copy()
        
        for square in self.detected_squares:
            center = square['center']
            contour = square['contour']
            
            # 绘制轮廓
            cv2.drawContours(
                img,
                [contour],
                -1,
                DetectionConfig.CONTOUR_COLOR,
                DetectionConfig.CONTOUR_THICKNESS
            )
            
            # 绘制中心点
            cv2.circle(
                img,
                center,
                DetectionConfig.CENTER_RADIUS,
                DetectionConfig.CENTER_COLOR,
                DetectionConfig.CENTER_THICKNESS
            )
            
            # 转换为坐标系坐标
            coord_x, coord_y = self.pixel_to_coordinate(center[0], center[1])
            
            # 绘制坐标文字
            text = f"({coord_x}, {coord_y})"
            text_x = center[0] + DetectionConfig.COORD_TEXT_OFFSET[0]
            text_y = center[1] + DetectionConfig.COORD_TEXT_OFFSET[1]
            
            # 绘制文字背景（提高可读性）
            (text_width, text_height), _ = cv2.getTextSize(
                text,
                DetectionConfig.COORD_FONT,
                DetectionConfig.COORD_FONT_SCALE,
                DetectionConfig.COORD_FONT_THICKNESS
            )
            
            cv2.rectangle(
                img,
                (text_x - 2, text_y - text_height - 2),
                (text_x + text_width + 2, text_y + 2),
                (0, 0, 0),
                -1
            )
            
            # 绘制坐标文字
            cv2.putText(
                img,
                text,
                (text_x, text_y),
                DetectionConfig.COORD_FONT,
                DetectionConfig.COORD_FONT_SCALE,
                DetectionConfig.COORD_FONT_COLOR,
                DetectionConfig.COORD_FONT_THICKNESS
            )
        
        return img
    
    def process_image(self, image: np.ndarray) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
        """
        完整的图像处理流程
        
        Args:
            image: 输入图像 (BGR格式)
            
        Returns:
            (处理后的图像, 检测到的方块中心坐标列表)
        """
        # 1. 检测白色方块
        centers = self.detect_white_squares(image)
        
        # 2. 绘制坐标系
        img = self.draw_coordinate_system(image)
        
        # 3. 绘制检测结果
        img = self.draw_detection_results(img)
        
        return img, centers
    
    def get_detected_count(self) -> int:
        """获取检测到的方块数量"""
        return len(self.detected_squares)


# 测试代码
if __name__ == "__main__":
    """图像处理器测试程序"""
    import sys
    
    print("=" * 50)
    print("图像处理器测试程序")
    print("=" * 50)
    
    # 创建测试图像
    test_img = np.ones((600, 800, 3), dtype=np.uint8) * 128  # 灰色背景
    
    # 添加几个白色方块
    cv2.rectangle(test_img, (200, 150), (280, 230), (255, 255, 255), -1)
    cv2.rectangle(test_img, (400, 300), (480, 380), (255, 255, 255), -1)
    cv2.rectangle(test_img, (600, 200), (650, 250), (255, 255, 255), -1)
    
    # 创建处理器
    processor = ImageProcessor()
    
    # 处理图像
    result_img, centers = processor.process_image(test_img)
    
    print(f"\n检测到 {processor.get_detected_count()} 个白色方块")
    print("中心坐标（相对于坐标系）:")
    for i, center in enumerate(centers, 1):
        coord = processor.pixel_to_coordinate(center[0], center[1])
        print(f"  方块 {i}: 像素坐标{center} -> 坐标系坐标{coord}")
    
    # 显示结果
    cv2.imshow("Original", test_img)
    cv2.imshow("Result", result_img)
    print("\n按任意键退出...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print("\n测试完成")

