"""
ALVIUM相机实时采集与检测程序 - 主程序入口
"""

import sys
import os

# 添加当前目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)


def check_dependencies():
    """检查依赖包是否已安装"""
    missing_packages = []
    
    try:
        import cv2
    except ImportError:
        missing_packages.append("opencv-python")
    
    try:
        import numpy
    except ImportError:
        missing_packages.append("numpy")
    
    try:
        from PIL import Image
    except ImportError:
        missing_packages.append("Pillow")
    
    try:
        from vmbpy import VmbSystem
    except ImportError:
        missing_packages.append("vmbpy")
    
    if missing_packages:
        print("错误: 缺少以下依赖包:")
        for pkg in missing_packages:
            print(f"  - {pkg}")
        print("\n请运行以下命令安装依赖:")
        print("  pip install -r requirements.txt")
        print("\n注意: vmbpy 需要先安装 Vimba SDK 软件")
        return False
    
    return True


def check_vimba_installation():
    """检查Vimba X SDK是否已安装"""
    try:
        from vmbpy import VmbSystem
        
        # 尝试获取VmbSystem实例
        vmb = VmbSystem.get_instance()
        with vmb:
            cameras = vmb.get_all_cameras()
            if not cameras:
                print("警告: Vimba X SDK已安装，但未检测到相机")
                print("请确保:")
                print("  1. 相机已通过USB3.0连接到电脑")
                print("  2. 相机电源指示灯亮起（绿色）")
                print("  3. 已安装相机驱动程序")
                return True  # SDK已安装，只是没有相机
            else:
                print(f"检测到 {len(cameras)} 个相机:")
                for cam in cameras:
                    print(f"  - {cam.get_id()} ({cam.get_model()})")
                return True
                
    except Exception as e:
        print(f"错误: Vimba X SDK未正确安装或配置")
        print(f"详细信息: {e}")
        print("\n请按照以下步骤操作:")
        print("  1. 下载并安装 Vimba X SDK")
        print("     下载地址: https://www.alliedvision.com/cn/products/software/vimba-x-sdk/")
        print("  2. 安装 vmbpy 包:")
        print("     pip install vmbpy")
        return False
    
    return True


def main():
    """主函数"""
    print("=" * 70)
    print(" " * 15 + "ALVIUM相机实时采集与检测程序")
    print("=" * 70)
    print()
    
    # 检查依赖
    print("正在检查依赖包...")
    if not check_dependencies():
        sys.exit(1)
    print("✓ 依赖包检查通过")
    print()
    
    # 检查Vimba X安装
    print("正在检查Vimba X SDK...")
    if not check_vimba_installation():
        print("\n提示: 您可以继续运行程序，但需要先安装Vimba X SDK和相机驱动")
        response = input("是否继续? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    print("✓ Vimba X SDK检查通过")
    print()
    
    # 启动GUI应用
    print("正在启动GUI应用...")
    print("=" * 70)
    print()
    
    try:
        from gui_app import main as gui_main
        gui_main()
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"\n程序运行时出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("\n程序已退出")


if __name__ == "__main__":
    main()

