# ALVIUM相机实时采集与检测程序

基于Vimba X Python SDK开发的ALVIUM相机图像采集和白色方块检测程序。

> **注意**: 本程序支持 **Vimba X SDK** (vmbpy 1.2.0+)，不支持旧版Vimba SDK。

## 快速开始

### 1. 环境配置

```bash
# 创建conda环境
conda env create -f environment.yml

# 激活环境
conda activate alvium_camera

# 安装vmbpy（需要先安装Vimba SDK）
pip install vmbpy
```

### 2. 运行程序

```bash
# 确保相机已通过USB 3.0连接
python main.py
```

### 3. 操作说明

#### 基础采集模式（GUI）
1. 点击 **"开始采集"** 连接相机并开始采集
2. 观察实时图像和检测结果
3. 点击 **"停止采集"** 停止采集
4. 点击 **"退出程序"** 或关闭窗口退出

#### 轨迹跟踪模式（新功能）
```bash
# 方式1：使用批处理文件（推荐）
双击运行 "启动轨迹跟踪.bat"

# 方式2：命令行启动
python realtime_trajectory_demo.py           # 使用ALVIUM相机
python realtime_trajectory_demo.py --webcam   # 使用电脑摄像头
python trajectory_tracker.py                  # 测试模式（模拟动画）
```

**轨迹跟踪快捷键：**
- `Q` - 退出程序
- `C` - 清空所有轨迹
- `1` - 开/关坐标系显示
- `2` - 开/关检测结果显示
- `3` - 开/关轨迹显示
- `空格` - 暂停/继续

详细使用说明请参阅 `轨迹跟踪使用说明.md`

## 功能特性

- ✅ 软件触发模式连续采集（约30 FPS）
- ✅ 实时绘制X-Y坐标系
- ✅ 自动检测白色方块并标注中心坐标
- ✅ 图形化操作界面
- ✅ 实时显示FPS和检测统计
- ✅ **白色物体轨迹跟踪**（新功能）
  - 多目标实时跟踪
  - 运动轨迹可视化
  - 彩色轨迹区分不同对象
  - 支持ALVIUM相机和普通摄像头

## 参数配置

所有参数可在 `config.py` 文件中调整：

- **相机参数**: 曝光时间、增益、触发间隔
- **坐标系**: 原点位置、轴长度、刻度间隔
- **检测参数**: HSV阈值、面积范围
- **GUI配置**: 窗口尺寸、更新频率

## 文件结构

```
code/
├── main.py                      # 主程序入口
├── gui_app.py                  # GUI应用程序
├── camera_controller.py        # 相机控制模块
├── image_processor.py          # 图像处理模块
├── trajectory_tracker.py       # 轨迹跟踪模块（新）
├── realtime_trajectory_demo.py # 轨迹跟踪演示程序（新）
├── config.py                   # 配置参数
├── environment.yml             # Conda环境配置
├── requirements.txt            # pip依赖列表
├── 启动轨迹跟踪.bat           # 快速启动脚本（新）
├── 轨迹跟踪使用说明.md        # 轨迹跟踪详细文档（新）
└── README.md                   # 本文件
```

## 依赖要求

- Python 3.9+
- **Vimba X SDK**（必须先安装）
- vmbpy 1.2.0+
- opencv-python
- numpy
- Pillow

## 详细文档

请参阅项目根目录下的 `1_2_4软件触发采集程序使用说明.md` 获取完整文档。

## 常见问题

**Q: 无法检测到相机？**
- 确保使用USB 3.0接口
- 检查相机后部绿灯是否亮起
- 确认已安装Vimba X驱动

**Q: 检测不到白色方块？**
- 调整相机曝光和增益
- 修改config.py中的HSV阈值
- 确保光照充足

更多问题请查看完整使用说明文档。

---

**Version**: 1.1  
**Last Updated**: 2025-12-02  
**New in v1.1**: 白色物体实时轨迹跟踪功能

