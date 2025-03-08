## 题目
- 阅读疑问：
    - **UWB惯性里程计**
        - UWB：ultra-wideband，超宽带
    - **B样条**
    - non-uniform(非均匀)
    - fewer anchors(较少锚点)
    - IMU：inertial measurement unit，惯性测量单元
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

## 1.介绍
- 位置信息的应用：机器人工作中，轨迹预测、物体追踪、自动拣选操作
- 室内用UWB替代GNSS，UWB优势：稳定性、低成本、大规模部署中的可扩展性
- 传统利用UWB的方法：multilateration(三角测量)，需要至少3个锚点来给确定移动目标的2D位置
    - 问题：在某些情况或场景中，只能获得一个或两个锚点，该方法不适用
        - 例如energy-constrained UWB(能量受限的UWB)、deployment scenarios with spatial limitations(部署场景空间受限):狭窄的走廊、隧道
- 加入IMU和里程计传感器，
    提供环境无关的即时响应速度(instantaneous response velocity)，
    可以在连续的(consecutive)UWB测距测量之间构建相对位置约束(the construction of relative position constraints)
- 传统的传感器融合(fusion)方法：extended kalman filter(EKF,扩展卡尔曼滤波)，particle filter(PF,粒子滤波)
    - 问题：
        - 依赖smoothness priors推测机器人动作状态
        - 但基于discrete-time(DT,离散时间)轨迹预测，无法足够地**represent smoothness**
            - 因为interpolation schemes(插值方案)，在推测离散状态之间的机器人动作是不准确的
- 异步问题：多模态传感器配置(multi-modal sensor setups)可能有异步测量，在估计过程中需要同一时间点数据融合
- **连续时间表示**：
    - 应用在多传感器标定(multi-sensors calibration)、动作规划、目标追踪
    - 生成光滑轨迹，具有连续数据流
#### B-spline：通过一组控制点定义时间多项式(temporal polynomials)，表示轨迹，可以查询任意时刻局部性姿势(pose with locality)
- 现有方法
    - 需要：
        - 控制节点间距均匀，控制节点预先确定
        - 速度恒定假设
    - 问题：
        - 速度变化时，控制节点间距较小时，导致过拟合
### 论文贡献
1. 提出CT-UIO定位系统
    - 融合时间不同步的UWB测距、IMU、里程计
        - 如何融合？对应下面第2点
    - 适应少锚点场景和非均匀控制节点
        - 如何解决？
2. 利用自适应估计的EKF，构建IMU/里程计融合模型
    - 自适应是什么，如何实现？
        - 好像是，根据速度动态调整节点数量
    - 模型结果是什么？短期动作先验是什么？
3. 完整轨迹定位，结合UWB测距和上述短期动作先验给出  
    - 少锚点如何处理？
        - 好像是，多个假设虚拟锚点


