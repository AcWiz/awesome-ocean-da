---
title: 'SSTODE: Ocean-Atmosphere Physics-Informed Neural ODEs for Sea Surface Temperature
  Prediction'
arXiv: '2511.05629'
authors: [Zheng Jiang, Wei Wang, Gaowei Zhang, Yi Wang]
year: 2025
source: arXiv
venue: NeurIPS
method_tags: [Neural_ODE, physics_informed, advection_diffusion, SST_prediction, energy_exchange]
application_tags: [sea_surface_temperature, ocean_atmosphere_coupling, global_ocean,
  upwelling, diurnal_cycle]
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
---

# 📑 SSTODE: Ocean-Atmosphere Physics-Informed Neural ODEs for Sea Surface Temperature Prediction

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2511.05629
- **作者机构**: 北京邮电大学（人工智能学院、计算机学院）
- **开源代码**: https://github.com/nicezheng/SSTODE-code

## 🧠 2. 一句话总结（TL;DR）
本文提出SSTODE框架，通过将平流-扩散方程嵌入神经ODE，结合能量交换积分器（EEI）建模海气界面热通量，在全球和区域SST预报基准上达到最优性能，揭示了平流流场、边界感知扩散和日变化等物理机制。

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 如何将物理约束融入神经网络以实现可解释的海表温度（SST）预报
- **科学意义**: SST对理解上层海洋热动力学和海气相互作用至关重要，影响气候和渔业
- **研究挑战**:
  - 现有物理信息神经网络难以充分表征海水运动（如沿岸涌升）
  - 外部SST驱动因子（如湍流热通量）整合不足
  - 固定时间间隔采样忽略了多尺度海气相互作用
  - 黑盒模型缺乏物理一致性和可解释性

## 🚀 4. 核心贡献（Contributions）
1. 提出SSTODE框架，首个将平流-扩散方程联合嵌入神经ODE的SST预测模型
2. 设计能量交换积分器（EEI）整合四种海表热通量（短波、长波、潜热、感热）
3. 通过变分优化从历史SST反演隐速度场
4. 在全球和区域SST预报基准上实现最优性能
5. 可视化揭示三个物理机制：平流流场、边界扩散、日变化

## 🏗️ 5. 方法详解（Methodology）
- **骨干网络**: 神经ODE框架，基于Adjoint方法进行梯度计算
- **速度估计**: 从历史SST观测通过PDE约束反演问题估计初始速度场
- **平流-扩散建模**: 联合嵌入平流项（-V·∇Y）和扩散项（κ∆Y）
- **EEI模块**: 时间依赖神经网络，融合四种热通量数据预测源项
- **时空嵌入**: 三角函数编码位置和时间，结合陆海掩膜和地形信息


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 (40GB) 或 V100 (32GB)
- GPU数量: 单卡训练
- 训练时间: 约3-5天（包含多次ODE积分迭代）

### 数据集（Datasets）
1. **SST Reanalysis Dataset**
   - 来源: NOAA OI SST / OSTIA全球海表温度再分析产品
   - 任务: 全球海表温度短期预报（1-10天预见期）
   - 数据规模: 空间分辨率0.25°×0.25°，时间跨度1982-2023年（约40年日数据）
   - 是否公开: 是

2. **ERA5 Reanalysis Dataset**
   - 来源: ECMWF Copernicus Climate Data Store
   - 任务: 提供表面热通量驱动数据（短波辐射、长波辐射、感热通量、潜热通量）
   - 数据规模: 0.25°空间分辨率，与SST数据时空对齐
   - 是否公开: 是

3. **Regional SST Dataset**
   - 来源: 特定区域（如太平洋、北大西洋）的SST观测与再分析数据
   - 任务: 区域SST预报评估
   - 数据规模: 根据区域覆盖范围，时间跨度与全球数据集一致
   - 是否公开: 是

### 数据处理
- 将SST和热通量数据插值至统一的空间网格（0.25°分辨率）
- 对SST数据进行距平处理或标准化（mean-std normalization）
- 热通量数据按物理单位保留，进行时间插值以匹配SST时间步
- 使用滑动时间窗口构建训练样本，输入历史p帧（p天）预测未来q帧（q天）
- 边界处理：对海洋区域设置掩码，陆地标记为无效值

### 复现难度
- ★★★☆☆（中等难度）
- 原因：作者提供了GitHub代码仓库链接（SSTODE-code），方法细节描述较为完整；但实验涉及特定的再分析数据获取和预处理流程，且ODE求解器的收敛性可能对超参数敏感，需要一定时间进行环境配置和调参；另外部分实现细节（如神经ODE的具体积分器选择）需进一步参考开源代码


## 📐 6. 数学与物理建模（Math & Physics）
- **平流-扩散方程**: ∂Y/∂t + V·∇Y = κ∆Y
- **热扩散系数**: 可学习的全局标量，通过softplus约束为正
- **海气界面能量方程**: Q_net = Q_LW + Q_SW + Q_LHF + Q_SHF
- **源项修正**: Y_pred = Y_ODE + Q̂（EEI输出）
- **损失函数**: MSE（分析场）+ PDE残差（速度估计）

## 📊 7. 实验分析（Experiments）
- **数据集**: OceanVP（HYCOM再分析）和ERA5（卫星+再分析）
- **训练配置**: 5.625°分辨率，6小时间隔，3个输入帧预测5/7/12步
- **主要结果**:
  - 全球预报：MSE=0.0527，ACC=0.999（OceanVP）
  - 区域预报：SSTODE在太平洋、大西洋、南大洋均最优
  - 消融实验：扩散项和EEI均显著提升性能
  - 与ClimODE相比MSE降低约10%

## 🔍 8. 优缺点分析（Critical Review）
**优点**:
- 物理约束显著提升模型的时空泛化能力
- 可解释性强，揭示了平流、扩散和热通量的物理贡献
- 连续时间建模支持任意时间分辨率预测
- 在全球和区域尺度均展现优越性能

**缺点**:
- 依赖再分析数据而非直接观测
- 在高分辨率（<1°）场景计算成本较高
- 速度场估计仍依赖一些正则化假设
- 未考虑海洋次表层过程

## 💡 9. 对我的启发（For My Research）
- 神经ODE是整合物理约束的有效框架
- 平流-扩散建模对海洋温度预测至关重要
- 能量交换积分器可扩展到其他海洋变量
- 物理可解释性对于海洋应用至关重要

## 🔮 10. Idea 扩展与下一步（Next Steps）
1. 扩展到海洋温盐垂向结构和三维动力学
2. 整合更多物理约束（质量、动量守恒）
3. 研究在海冰区域的适用性
4. 结合卫星观测实现端到端学习
5. 探索多尺度预测（从日尺度到季节尺度）

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{jiang2025sstode,
  title={SSTODE: Ocean-Atmosphere Physics-Informed Neural ODEs for Sea Surface Temperature Prediction},
  author={Jiang, Zheng and Wang, Wei and Zhang, Gaowei and Wang, Yi},
  year={2025},
  eprint={2511.05629},
  eprinttype={arxiv},
  eprintclass={cs.LG},
  journal={NeurIPS},
}
```
