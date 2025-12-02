"""
创建测试视频工具
生成包含移动白色物体的测试视频，用于测试轨迹跟踪功能
"""

import cv2
import numpy as np
import os


class TestVideoGenerator:
    """测试视频生成器"""
    
    def __init__(self, width=1280, height=720, fps=30):
        """
        初始化视频生成器
        
        Args:
            width: 视频宽度
            height: 视频高度
            fps: 帧率
        """
        self.width = width
        self.height = height
        self.fps = fps
        
    def create_circular_motion(self, duration_sec=10, output_file="test_circular.mp4"):
        """
        创建圆周运动测试视频
        
        Args:
            duration_sec: 视频时长（秒）
            output_file: 输出文件名
        """
        print(f"正在生成圆周运动测试视频...")
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, self.fps, (self.width, self.height))
        
        total_frames = duration_sec * self.fps
        center_x = self.width // 2
        center_y = self.height // 2
        radius = 200
        
        for frame_num in range(total_frames):
            # 创建背景
            frame = np.ones((self.height, self.width, 3), dtype=np.uint8) * 80
            
            # 添加网格
            for i in range(0, self.width, 50):
                cv2.line(frame, (i, 0), (i, self.height), (100, 100, 100), 1)
            for i in range(0, self.height, 50):
                cv2.line(frame, (0, i), (self.width, i), (100, 100, 100), 1)
            
            # 计算物体位置（圆周运动）
            angle = (frame_num / total_frames) * 2 * np.pi * 3  # 3圈
            x = int(center_x + radius * np.cos(angle))
            y = int(center_y + radius * np.sin(angle))
            
            # 绘制白色圆形物体
            cv2.circle(frame, (x, y), 25, (255, 255, 255), -1)
            
            # 添加信息文字
            cv2.putText(frame, f"Frame: {frame_num}/{total_frames}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, "Circular Motion Test", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            out.write(frame)
            
            if (frame_num + 1) % 30 == 0:
                print(f"  进度: {frame_num + 1}/{total_frames} 帧")
        
        out.release()
        print(f"✓ 圆周运动测试视频已保存: {output_file}")
    
    def create_multiple_objects(self, duration_sec=10, output_file="test_multiple.mp4"):
        """
        创建多物体运动测试视频
        
        Args:
            duration_sec: 视频时长（秒）
            output_file: 输出文件名
        """
        print(f"正在生成多物体运动测试视频...")
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, self.fps, (self.width, self.height))
        
        total_frames = duration_sec * self.fps
        
        for frame_num in range(total_frames):
            # 创建背景
            frame = np.ones((self.height, self.width, 3), dtype=np.uint8) * 60
            
            # 添加网格
            for i in range(0, self.width, 50):
                cv2.line(frame, (i, 0), (i, self.height), (80, 80, 80), 1)
            for i in range(0, self.height, 50):
                cv2.line(frame, (0, i), (self.width, i), (80, 80, 80), 1)
            
            t = frame_num / total_frames
            
            # 物体1：水平往返运动
            x1 = int(100 + (self.width - 200) * (0.5 + 0.5 * np.sin(t * 4 * np.pi)))
            y1 = 150
            cv2.circle(frame, (x1, y1), 20, (255, 255, 255), -1)
            
            # 物体2：垂直往返运动
            x2 = 300
            y2 = int(100 + (self.height - 200) * (0.5 + 0.5 * np.sin(t * 3 * np.pi)))
            cv2.circle(frame, (x2, y2), 20, (255, 255, 255), -1)
            
            # 物体3：对角线运动
            x3 = int(200 + (self.width - 400) * t)
            y3 = int(100 + (self.height - 200) * t)
            cv2.circle(frame, (x3, y3), 20, (255, 255, 255), -1)
            
            # 物体4：圆周运动
            angle = t * 4 * np.pi
            x4 = int(self.width - 250 + 150 * np.cos(angle))
            y4 = int(self.height - 250 + 150 * np.sin(angle))
            cv2.circle(frame, (x4, y4), 20, (255, 255, 255), -1)
            
            # 添加信息文字
            cv2.putText(frame, f"Frame: {frame_num}/{total_frames}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, "Multiple Objects Test", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            out.write(frame)
            
            if (frame_num + 1) % 30 == 0:
                print(f"  进度: {frame_num + 1}/{total_frames} 帧")
        
        out.release()
        print(f"✓ 多物体运动测试视频已保存: {output_file}")
    
    def create_random_motion(self, duration_sec=10, num_objects=5, output_file="test_random.mp4"):
        """
        创建随机运动测试视频
        
        Args:
            duration_sec: 视频时长（秒）
            num_objects: 物体数量
            output_file: 输出文件名
        """
        print(f"正在生成随机运动测试视频...")
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, self.fps, (self.width, self.height))
        
        total_frames = duration_sec * self.fps
        
        # 初始化物体位置和速度
        objects = []
        for _ in range(num_objects):
            x = np.random.randint(50, self.width - 50)
            y = np.random.randint(50, self.height - 50)
            vx = np.random.uniform(-5, 5)
            vy = np.random.uniform(-5, 5)
            objects.append({'x': x, 'y': y, 'vx': vx, 'vy': vy})
        
        for frame_num in range(total_frames):
            # 创建背景
            frame = np.ones((self.height, self.width, 3), dtype=np.uint8) * 50
            
            # 更新和绘制物体
            for obj in objects:
                # 更新位置
                obj['x'] += obj['vx']
                obj['y'] += obj['vy']
                
                # 边界碰撞检测
                if obj['x'] < 50 or obj['x'] > self.width - 50:
                    obj['vx'] = -obj['vx']
                    obj['x'] = max(50, min(self.width - 50, obj['x']))
                
                if obj['y'] < 50 or obj['y'] > self.height - 50:
                    obj['vy'] = -obj['vy']
                    obj['y'] = max(50, min(self.height - 50, obj['y']))
                
                # 绘制物体
                cv2.circle(frame, (int(obj['x']), int(obj['y'])), 20, (255, 255, 255), -1)
            
            # 添加信息文字
            cv2.putText(frame, f"Frame: {frame_num}/{total_frames}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"Random Motion Test ({num_objects} objects)", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            out.write(frame)
            
            if (frame_num + 1) % 30 == 0:
                print(f"  进度: {frame_num + 1}/{total_frames} 帧")
        
        out.release()
        print(f"✓ 随机运动测试视频已保存: {output_file}")


def main():
    """主函数"""
    print("=" * 70)
    print(" " * 20 + "测试视频生成工具")
    print("=" * 70)
    print()
    
    generator = TestVideoGenerator()
    
    print("请选择要生成的测试视频：")
    print("  1. 圆周运动（单个物体）")
    print("  2. 多物体运动（4个物体，不同运动模式）")
    print("  3. 随机运动（5个物体）")
    print("  4. 全部生成")
    print("  0. 退出")
    print()
    
    choice = input("请输入选项 (0-4): ").strip()
    
    if choice == '1':
        generator.create_circular_motion()
    elif choice == '2':
        generator.create_multiple_objects()
    elif choice == '3':
        generator.create_random_motion()
    elif choice == '4':
        print("\n生成所有测试视频...\n")
        generator.create_circular_motion()
        print()
        generator.create_multiple_objects()
        print()
        generator.create_random_motion()
    elif choice == '0':
        print("退出")
        return
    else:
        print("无效的选项")
        return
    
    print()
    print("=" * 70)
    print("生成完成！")
    print()
    print("使用方法：")
    print("  1. 使用视频播放器播放生成的视频文件")
    print("  2. 或者使用OBS等软件将视频设置为虚拟摄像头")
    print("  3. 然后运行轨迹跟踪程序进行测试")
    print("=" * 70)


if __name__ == "__main__":
    main()

