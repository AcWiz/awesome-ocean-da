---
title: "Long-Range Vision-Based UAV-assisted Localization for Unmanned Surface Vehicles"
arXiv: "2408.11429"
authors: ["Waseem Akram", "Siyuan Yang", "Hailiang Kuang", "Xiaoyu He", "Muhayy Ud Din", "Yihao Dong", "Defu Lin", "Lakmal Seneviratne", "Shaoming He", "Irfan Hussain"]
year: 2024
source: "arXiv"
venue: "arXiv"
method_tags: ["UAV辅助定位", "视觉定位", "三角测量", "扩展卡尔曼滤波", "深度学习目标检测"]
application_tags: ["水面无人艇导航", "GNSS拒止环境", "海洋无人系统", "多机器人协作"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# Long-Range Vision-Based UAV-assisted Localization for Unmanned Surface Vehicles

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2408.11429
- **作者机构**: [ Khalifa University, 武汉大学, 西北工业大学, University of Oxford, MBZIRC ]
- **开源代码**: None

## 2. 一句话总结（TL;DR）
本文提出了一种基于无人机（UAV）辅助水面无人艇（USV）在GNSS受限海洋环境中实现远程视觉定位的新方法。无人机沿海岸线飞行，通过深度学习检测无人艇并结合三角测量和扩展卡尔曼滤波（EKF）进行鲁棒的状态估计，该方法在MBZIRC-2024真实海洋环境中验证有效。

## 3. 研究问题（Problem Definition）
**核心问题**: 当GPS信号受干扰、阻塞或遭受恶意干扰时，水面无人艇在海洋环境中无法获得可靠的定位信息，如何实现精确的替代导航？

**研究背景**:
- GPS在海洋环境中易受信号遮挡、多径反射和人为干扰
- 传统传感器如DVL存在漂移问题，雷达在近距离和恶劣天气下性能较差
- 传统方法的长距离导航和目标跟踪受限于视野范围和地球曲率

**关键挑战**:
1. GNSS拒止环境下的精确定位
2. 远距离目标的持续跟踪与检测
3. 海洋动态干扰下的鲁棒状态估计
4. 异构机器人系统间的实时通信与协调

## 4. 核心贡献（Contributions）
1. 提出了一种新颖的UAV辅助USV定位方法，利用无人机从空中视角克服地球曲率限制，实现远程目标检测与跟踪
2. 设计了基于像素误差的动态相机角度调整机制，通过闭环控制持续优化目标在图像中心的偏离程度
3. 融合三角测量几何约束与扩展卡尔曼滤波（EKF），实现了视觉测量与遥测数据的鲁棒状态估计
4. 在MBZIRC-2024真实海洋竞赛环境中验证了方法的有效性，证明了其在复杂海况下的实用价值

## 5. 方法详解（Methodology）

### 5.1 系统架构
系统由异构机器人接口连接的UAV和USV组成：
- **无人机端**: 配备相机，沿海岸线以恒定高度飞行，执行目标检测与跟踪
- **无人艇端**: 携带机载传感器，负责状态测量与数据回传
- **通信接口**: 建立UAV与USV之间的数据传输链路

### 5.2 定位流程
1. **目标检测阶段**: UAV使用深度学习方法处理相机图像，连续检测和跟踪USV
2. **相机角度调整**: 根据USV与图像中心的像素误差，动态调整无人机相机角度
3. **三角测量定位**: 利用几何信息和无人机数据链距离估计USV相对位置
4. **状态融合**: 将视觉测量结果输入EKF进行鲁棒状态估计

### 5.3 关键技术细节
- **深度学习检测器**: 用于从相机图像中实时检测USV
- **像素误差反馈控制**: 目标与图像中心的像素偏移量作为控制信号调整相机俯仰角
- **EKF融合**: 结合视觉测量与遥测数据，消除单传感器误差影响

## 6. 数学与物理建模（Math & Physics）

### 6.1 三角测量模型
利用以下几何关系估计USV位置：
- 无人机飞行高度 $h$（恒定）
- 无人机位置 $(x_{uav}, y_{uav}, h)$
- 相机俯仰角 $\theta$
- 目标在图像中的像素位置 $(u, v)$
- 数据链距离 $d_{datalink}$

通过三角几何关系建立目标位置方程，实现从2D图像到3D空间的映射。

### 6.2 扩展卡尔曼滤波
状态向量:
$$\mathbf{x} = [x, y, \dot{x}, \dot{y}, \theta, \dot{\theta}]^T$$

预测步骤:
$$\hat{\mathbf{x}}_{k|k-1} = F\hat{\mathbf{x}}_{k-1|k-1} + B\mathbf{u}_{k-1}$$

更新步骤:
$$\hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + K(z - h(\hat{\mathbf{x}}_{k|k-1}))$$

其中 $z$ 为视觉测量融合的观测值。

### 6.3 像素误差控制
$$e_{pixel} = \sqrt{(u - u_{center})^2 + (v - v_{center})^2}$$

通过最小化 $e_{pixel}$ 调整相机角度，确保目标始终位于图像中心区域。

## 7. 实验分析（Experiments）

**数据集**: MBZIRC-2024真实海洋环境测试数据集

**评估指标**:
- 定位精度
- 跟踪成功率
- 状态估计收敛性

**对比方法**: 文中主要与纯GPS导航、DVL导航进行对比

**核心结果**:
- 成功在真实海洋环境中完成远程定位任务
- 包含噪声测量和海洋干扰的情况下仍保持稳定定位
- 验证了该方法可作为GPS导航的有效补充
- 异构机器人通信接口工作可靠

## 8. 优缺点分析（Critical Review）

**优点**:
- 创新性地利用无人机视角克服地球曲率和障碍物限制，实现远距离定位
- 结合深度学习与经典滤波方法，工程实用性强
- 像素误差反馈机制简单有效，提升了跟踪稳定性
- 在真实竞赛环境中验证，具有实际应用价值

**缺点**:
- 依赖无人机飞行高度和天气条件，适用范围有一定限制
- 深度学习检测器需要针对USV目标进行训练和优化
- 未公开代码和详细实验数据，定量评估有限
- 未考虑夜间或低能见度极端条件下的性能

## 9. 对我的启发（For My Research）

1. **多源融合思路**: 该工作将视觉测量与EKF融合的思想可应用于海洋数据同化中多源观测资料的融合
2. **无人机辅助观测**: 利用UAV扩展观测范围的思路可借鉴到海洋遥感数据的获取与验证
3. **GNSS拒止环境**: 对GNSS受限时海洋无人系统的鲁棒定位研究具有参考价值
4. **异构系统协作**: 无人机-无人艇协同框架为海空一体化海洋监测系统设计提供思路
5. **竞赛驱动研究**: MBZIRC等竞赛场景为算法验证提供了接近实战的测试平台

## 10. Idea 扩展与下一步（Next Steps）

1. **多无人机协同**: 扩展为多UAV编队协同定位，提高冗余度和覆盖范围
2. **夜间/低光增强**: 集成红外相机或激光雷达，应对夜间和低能见度场景
3. **端到端学习**: 将三角测量和EKF融合替换为端到端神经网络，直接回归位置估计
4. **仿真-真实迁移**: 构建Sim2Real框架，降低实际部署的调试成本
5. **与其他传感器集成**: 融合声学传感器、AIS等多源信息，进一步提升定位鲁棒性

## 11. 引用格式（BibTex）
```bibtex
@article{akram2024long,
  title={Long-Range Vision-Based UAV-assisted Localization for Unmanned Surface Vehicles},
  author={Akram, Waseem and Yang, Siyuan and Kuang, Hailiang and He, Xiaoyu and Din, Muhayy Ud and Dong, Yihao and Lin, Defu and Seneviratne, Lakmal and He, Shaoming and Hussain, Irfan},
  year={2024},
  eprint={2408.11429},
  archivePrefix={arXiv},
  primaryClass={cs.RO},
  institution={Khalifa University, Wuhan University, Northwestern Polytechnical University, University of Oxford, MBZIRC}
}