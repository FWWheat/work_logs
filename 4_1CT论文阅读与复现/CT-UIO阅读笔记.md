## 题目
- 阅读疑问：
    - **UWB惯性里程计**
        - UWB：ultra-wideband，超宽带
    - **B样条**
    - non-uniform(非均匀)
    - fewer anchors(较少锚点)
## 摘要
- 探讨问题：在锚点较少时，能源受限时，UWB定位技术
- 目前的研究：
    - 依赖：
        1. discrete-time representations(离散时间表示)
        2. **smoothness priors(光滑性先验)**推测机器人的运动状态
            - **smoothness priors(光滑性先验)**
    - 问题：无法确保多传感器数据同步
- 论文贡献：
    1. 提出一个**uwb惯性里程计定位系统**，利用**具有较少锚点的非均匀B样条框架**
    2. 引入一个**adaptive knot-span adjustment strategy(自适应节点跨度调整策略)**，用于非均匀连续时间轨迹表示
        - 一个方法表示轨迹
        - 方法实现：根据运动速度动态调整**控制节点**
            - 控制节点具体是什么，有什么作用?
    3. 提出**改进的扩展卡尔曼滤波(EKF)**，实现IMU和里程计数据的有效融合(efficient fusion)；基于创新的自适应评估(estimation)，给出短期精确运动先验
        - 多传感器数据融合，提供短期预计位置
    4. 提出基于多个假设(hypotheses)的Virtual Anchor(VA,虚拟锚点)生成方法，实现少锚点条件下的**完全可观测的**UWB定位系统
        - 给了一个虚拟锚点生成方法，但要满足很多假设
    5. 提出一个**基于自适应滑动窗口的CT-UIO因子图**，用于全局轨迹估计
        - 输入什么，输出轨迹坐标
    - 使用的数据集：corridor , exhibition hall
    
        
        
