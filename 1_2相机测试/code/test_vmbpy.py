"""
测试vmbpy模块是否正确安装
"""

print("=" * 60)
print("测试 vmbpy 模块安装")
print("=" * 60)

try:
    print("\n1. 测试导入 vmbpy...")
    import vmbpy
    print("   ✓ vmbpy 模块导入成功")
    print(f"   版本: {vmbpy.__version__}")
    
    print("\n2. 测试导入 VmbSystem...")
    from vmbpy import VmbSystem
    print("   ✓ VmbSystem 导入成功")
    
    print("\n3. 测试获取 VmbSystem 实例...")
    vmb = VmbSystem.get_instance()
    print("   ✓ VmbSystem 实例获取成功")
    
    print("\n4. 测试进入 VmbSystem 上下文...")
    with vmb:
        print("   ✓ VmbSystem 上下文进入成功")
        
        print("\n5. 检测相机...")
        cameras = vmb.get_all_cameras()
        
        if cameras:
            print(f"   ✓ 检测到 {len(cameras)} 个相机:")
            for i, cam in enumerate(cameras, 1):
                print(f"      相机 {i}: {cam.get_id()}")
                print(f"         型号: {cam.get_model()}")
        else:
            print("   ⚠ 未检测到相机")
            print("     请检查:")
            print("       - 相机是否通过USB 3.0连接")
            print("       - 相机指示灯是否亮起")
            print("       - 驱动程序是否已安装")
    
    print("\n" + "=" * 60)
    print("✓ 所有测试通过！可以运行主程序了。")
    print("=" * 60)
    
except ImportError as e:
    print(f"\n✗ 导入错误: {e}")
    print("\n可能的原因:")
    print("  1. vmbpy 未安装")
    print("  2. Vimba X SDK 未安装")
    print("  3. Python 环境不正确")
    print("\n解决方法:")
    print("  1. 确认已安装 Vimba X SDK")
    print("  2. 运行: pip install vmbpy")
    print("  3. 激活正确的 conda 环境")

except Exception as e:
    print(f"\n✗ 错误: {e}")
    print("\n请检查 Vimba X SDK 是否正确安装")
    import traceback
    traceback.print_exc()

