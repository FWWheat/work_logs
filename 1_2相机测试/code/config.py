"""
ALVIUM相机图像采集程序配置文件
包含相机参数、图像处理参数、GUI配置等
"""

# ==================== 相机参数配置 ====================
class CameraConfig:
    """相机相关参数配置"""
    # 曝光时间 (微秒)
    EXPOSURE_TIME = 20000  # 20ms
    
    # 增益值 (dB)
    GAIN = 0.0
    
    # 触发模式配置
    TRIGGER_SOURCE = "Software"  # 软件触发
    TRIGGER_MODE = "On"  # 触发模式开启
    TRIGGER_SELECTOR = "FrameStart"  # 帧开始触发
    ACQUISITION_MODE = "Continuous"  # 连续采集模式
    
    # 软件触发间隔 (秒) - 用于连续触发
    TRIGGER_INTERVAL = 0.03  # 约30fps


# ==================== 坐标系配置 ====================
class CoordinateConfig:
    """坐标系绘制参数配置"""
    # 原点位置 (像素坐标)
    ORIGIN_X = 50  # 原点X坐标
    ORIGIN_Y = 50  # 原点Y坐标
    
    # 坐标轴长度 (像素)
    AXIS_LENGTH_X = 600  # X轴长度
    AXIS_LENGTH_Y = 400  # Y轴长度
    
    # 坐标轴颜色 (BGR格式)
    X_AXIS_COLOR = (0, 0, 255)  # 红色
    Y_AXIS_COLOR = (255, 0, 0)  # 蓝色
    
    # 坐标轴线宽
    AXIS_THICKNESS = 2
    
    # 箭头参数
    ARROW_LENGTH = 10  # 箭头长度
    
    # 刻度配置
    TICK_INTERVAL = 100  # 刻度间隔 (像素)
    TICK_LENGTH = 10  # 刻度线长度
    TICK_THICKNESS = 1  # 刻度线宽度
    
    # 文字配置
    FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX
    FONT_SCALE = 0.5  # 字体大小
    FONT_THICKNESS = 1  # 字体粗细
    FONT_COLOR = (255, 255, 255)  # 白色
    
    # 轴标签
    X_AXIS_LABEL = "X"
    Y_AXIS_LABEL = "Y"


# ==================== 白色方块检测配置 ====================
class DetectionConfig:
    """白色方块检测参数配置"""
    # HSV颜色空间阈值范围 (用于白色检测)
    # 白色在HSV空间中: H值范围广, S值低, V值高
    HSV_LOWER = (0, 0, 200)  # 下界: H, S, V
    HSV_UPPER = (180, 30, 255)  # 上界: H, S, V
    
    # 面积过滤阈值 (像素)
    MIN_AREA = 100  # 最小面积
    MAX_AREA = 50000  # 最大面积
    
    # 形态学操作参数
    MORPH_KERNEL_SIZE = 5  # 形态学操作核大小
    
    # 检测结果绘制配置
    CONTOUR_COLOR = (0, 255, 0)  # 绿色轮廓
    CONTOUR_THICKNESS = 2  # 轮廓线宽
    
    CENTER_COLOR = (0, 0, 255)  # 红色中心点
    CENTER_RADIUS = 5  # 中心点半径
    CENTER_THICKNESS = -1  # 实心圆 (-1表示填充)
    
    # 坐标文字配置
    COORD_FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX
    COORD_FONT_SCALE = 0.6
    COORD_FONT_THICKNESS = 2
    COORD_FONT_COLOR = (0, 255, 255)  # 黄色
    COORD_TEXT_OFFSET = (10, -10)  # 文字相对中心点的偏移


# ==================== GUI配置 ====================
class GUIConfig:
    """GUI界面参数配置"""
    # 窗口标题
    WINDOW_TITLE = "ALVIUM相机实时采集与检测"
    
    # 窗口尺寸
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 900
    
    # 图像显示区域尺寸
    CANVAS_WIDTH = 1150
    CANVAS_HEIGHT = 750
    
    # 图像更新频率 (毫秒)
    UPDATE_INTERVAL = 30  # 约33fps
    
    # 状态栏更新间隔 (毫秒)
    STATUS_UPDATE_INTERVAL = 500  # 0.5秒更新一次
    
    # 按钮配置
    BUTTON_WIDTH = 15
    BUTTON_HEIGHT = 2
    
    # 状态栏字体
    STATUS_FONT = ("Arial", 10)


# ==================== 其他配置 ====================
class GeneralConfig:
    """通用配置"""
    # 图像队列大小
    IMAGE_QUEUE_SIZE = 10
    
    # 调试模式
    DEBUG_MODE = False
    
    # 日志级别
    LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR

