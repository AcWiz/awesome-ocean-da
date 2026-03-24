# AI + 海洋数据同化论文库

> 收录 AI/深度学习 + 海洋数据同化、预报相关的学术论文，持续更新。

[![Papers](https://img.shields.io/badge/Papers-135-blue.svg)](#) ·
[![2026](https://img.shields.io/badge/2026-19-green.svg)](#papers-by-year) ·
[![Last Updated](https://img.shields.io/badge/Updated-2026--03--23-orange.svg)](#) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 目录

- [核心方法](#核心方法)
  - [物理信息神经网络 (PINN)](#物理信息神经网络-pinn)
  - [Koopman 学习](#koopman-学习)
  - [神经算子 (Neural Operator)](#神经算子-neural-operator)
  - [图神经网络 (GNN)](#图神经网络-gnn)
  - [变分方法 (4D-Var / EnKF)](#变分方法-4d-var--enkf)
  - [Transformer / Attention](#transformer--attention)
- [应用场景](#应用场景)
  - [海表温度 (SST)](#海表温度-sst)
  - [海表高度 (SSH)](#海表高度-ssh)
  - [ENSO 预测](#enso-预测)
  - [海浪预报](#海浪预报)
  - [全球预报](#全球预报)
  - [海洋数据同化](#海洋数据同化)
  - [海冰](#海冰)
  - [深海](#深海)
  - [气候预测](#气候预测)
  - [海洋动力学](#海洋动力学)
  - [海平面](#海平面)
  - [参数化](#参数化)
- [按年份浏览](#papers-by-year)
- [如何贡献](./CONTRIBUTING.md)

---

## 核心方法

### 物理信息神经网络 (PINN)
> 将物理约束嵌入神经网络 Loss，强制解满足物理定律

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2025|[Prediction of Sea Ice Velocity and Concentration in the Arctic Ocean using Physics-informed Neural Network](https://arxiv.org/abs/2510.17756)|Nature|PINN, HIS-Unet, CNN, 物理约束, 海冰|北冰洋, 海冰速度, 海冰浓度, remote-sensing, multi-task-learning|[总结](./papers/2025/2510.17756/summary.md)|
|2025|[Physics-Informed Neural Networks for Modeling Ocean Pollutant Transport](https://arxiv.org/abs/2507.08834)|Nature|PINN, advection-diffusion, 物理约束, 神经网络, Julia|海洋污染物, 平流扩散方程, finite-difference, 环境监测|[总结](./papers/2025/2507.08834/summary.md)|
|2025|[CTP: A hybrid CNN-Transformer-PINN model for ocean front](https://arxiv.org/abs/2505.10894)|Nature|CNN, Transformer, PINN, Navier-Stokes, 深度学习|海洋锋, SST, 预报, 分类, Kuroshio|[总结](./papers/2025/2505.10894/summary.md)|
|2025|[Deep learning in the abyss: a stratified Physics Informed Neural Network for data assimilation](https://arxiv.org/abs/2503.19160)|JGR (Journal of Geophysical Research)|PINN, SIREN, 数据同化, quasi-geostrophic, stratified-ocean|深海, SWOT卫星, ARGO浮标, 海洋环流, 中尺度|[总结](./papers/2025/2503.19160/summary.md)|
|2025|[Physics-informed neural networks for phase-resolved data assimilation and prediction of nonlinear ocean waves](https://arxiv.org/abs/2501.08430)|Physics of Fluids|PINN, potential-flow, 波浪物理, 相位解析, 数据同化|海浪, 波浪预测, 数据同化, 波流水槽, 非线性波|[总结](./papers/2025/2501.08430/summary.md)|

[更多 物理信息神经网络 (PINN) 论文 →](./papers/pinn.md)

---

### 神经算子 (Neural Operator)
> 学习解算子映射，无网格约束的偏微分方程求解

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Spatio-temporal modeling and forecasting with Fourier neural operators](https://arxiv.org/abs/2601.01813)|Science|FNO, neural-operator, 动力学系统, 时空, 不确定性量化|SST, precipitation, 海洋建模, 大气建模, 预报|[总结](./papers/2026/2601.01813/summary.md)|
|2025|[Principled Operator Learning in Ocean Dynamics: The Role of Temporal Structure](https://arxiv.org/abs/2510.09792)|NeurIPS|neural-operator, FNO, 时间色散, 海洋建模, 物理约束|海洋环流, 海平面预测, Baltic-Sea, 区域海洋, wave-propagation|[总结](./papers/2025/2510.09792/summary.md)|
|2025|[Bridging Ocean Wave Physics and Deep Learning: Physics-Informed Neural Operators for Nonlinear Wavefield Reconstruction in Real-Time](https://arxiv.org/abs/2508.03315)|Nature|PINO, neural-operator, FNO, 物理约束, wave-reconstruction, HOSM|海浪, 波浪预测, buoy-measurements, X-band-radar, 相位解析|[总结](./papers/2025/2508.03315/summary.md)|
|2025|[Generative Lagrangian Data Assimilation for Ocean Dynamics under Extreme Sparsity](https://arxiv.org/abs/2507.06479)|Nature|DDPM, FNO, UNET, diffusion-model, neural-operator, 数据同化|拉格朗日数据同化, 稀疏观测, 海洋重构, 墨西哥湾, 卫星测高|[总结](./papers/2025/2507.06479/summary.md)|
|2025|[Deep Learning for Canary Current Upwelling: A Case Study](https://arxiv.org/abs/2505.24429)|Nature|neural-operator, FNO, graph-network, data-driven, 海洋建模|加纳利流, 上升流, 海洋预报, 区域海洋, 海洋生态系统|[总结](./papers/2025/2505.24429/summary.md)|
|2024|[STREAMLINING OCEAN DYNAMICS MODELING WITH FOURIER NEURAL OPERATORS: A MULTIOBJECTIVE HYPERPARAMETER AND ARCHITECTURE OPTIMIZATION APPROACH](https://arxiv.org/abs/2404.05768)|Science|neural-operator, fno, 超参数优化, deephyper, 贝叶斯优化|海洋建模, 斜压风驱动海洋, 海表温度, 预报|[总结](./papers/2024/2404.05768/summary.md)|

[更多 神经算子 (Neural Operator) 论文 →](./papers/neural-operator.md)

---

### 图神经网络 (GNN)
> 利用图结构建模海洋要素间的空间依赖关系

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Ensemble Graph Neural Networks for Probabilistic Sea Surface Temperature Forecasting via Input Perturbations](https://arxiv.org/abs/2603.06153)|NeurIPS|GNN, 集成学习, 不确定性量化, SST, Perlin-noise|海表温度预报, 区域海洋, 加纳利流, ensemble-prediction, probabilistic-forecasting|[总结](./papers/2026/2603.06153/summary.md)|
|2026|[Eddy-Resolving Global Ocean Forecasting with Multi-Scale Graph Neural Networks](https://arxiv.org/abs/2601.12775)|ICML|GNN, 图神经网络, 多尺度, spherical-mesh, eddy-resolving|全球海洋, 涡旋, 预报, 海洋环流, 海洋状态预测|[总结](./papers/2026/2601.12775/summary.md)|
|2025|[SeaCast: Accurate Mediterranean Sea Forecasting via Graph-Based Deep Learning](https://arxiv.org/abs/2506.23900)|Nature|GNN, 图神经网络, 分层网格, 区域海洋, 自回归|地中海, 海洋预报, SST, SSH, 温度, 盐度, 海流|[总结](./papers/2025/2506.23900/summary.md)|
|2024|[EnKode: Active Learning of Unknown Flows with Koopman Operators](https://arxiv.org/abs/2410.16605)|IEEE Robotics and Automation Letters|Koopman-Operator, 主动学习, 集成方法, GNN|海洋环流, 流场建模, 机器人, 主动感知, 不确定性量化|[总结](./papers/2024/2410.16605/summary.md)|
| 2022 | [Modeling Oceanic Variables with Dynamic Graph Neural Networks](https://arxiv.org/abs/2206.12746) | N/A - Preprint | GNN, Graph Neural Network, LSTM, Transformer, Dynamic Graph | Ocean Dynamics, Current Velocity, SSH, Santos Estuarine System | [总结](./papers/2022/2206.12746/summary.md) |

[更多 图神经网络 (GNN) 论文 →](./papers/gnn.md)

---

### 变分方法 (4D-Var / EnKF)
> 变分数据同化方法，通过最小化目标函数估计最优状态

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2025|[Meta-Learning Fourier Neural Operators for Hessian Inversion and Enhanced Variational Data Assimilation](https://arxiv.org/abs/2509.22949)|arXiv|元学习, Fourier Neural Operator, Data Assimilation, Inverse Hessian Approximation, Conjugate Gradient Method|Variational Data Assimilation, 4D-Var, Numerical Weather Prediction, PDE-Constrained Optimization|[总结](./papers/2025/2509.22949/summary.md)|
| 2025 | [Tensor-Var: Efficient Four-Dimensional Variational Data Assimilation](https://arxiv.org/abs/2501.13312) | arXiv | 4D-Var, Kernel Methods, Conditional Mean Embedding, Deep Learning, Data Assimilation | Weather Prediction, Chaotic Systems, Numerical Weather Prediction, Dynamical Systems | [总结](./papers/2025/2501.13312/summary.md) |
|2015|[A framework for interpreting regularized state estimation](https://arxiv.org/abs/1511.04790)|Monthly Weather Review|4D-Var, Data Assimilation, State Estimation, 正则化, Chaotic Systems|Ocean Circulation, Climate Modeling, Geophysical Fluid Dynamics|[总结](./papers/2015/1511.04790/summary.md)|
| 2014 | [Optimal boundary conditions at the staircase-shaped coastlines](https://arxiv.org/abs/1402.7201) | Ocean Dynamics | 4D-Var, 数据同化, NEMO模型, 边界条件优化, 海洋建模 | 海洋环流建模, 海岸线近似, 数值天气预报 | [总结](./papers/2014/1402.7201/summary.md) |
| 2012 | [Optimal Boundary Conditions for ORCA-2 Model](https://arxiv.org/abs/1212.3116) | Ocean Dynamics | 4D-Var, 数据同化, 海洋建模, 切线与伴随代码自动生成 | 海洋环流, 边界条件优化, NEMO模型, 射流强化 | [总结](./papers/2012/1212.3116/summary.md) |

[更多 变分方法 (4D-Var / EnKF) 论文 →](./papers/4d-var.md)

---

### Transformer / Attention
> 利用自注意力机制捕捉长距离依赖关系

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
| 2026 | [Benchmarking Artificial Intelligence Models for Daily Coastal Hypoxia Forecasting](https://arxiv.org/abs/2602.05178) | arXiv | Deep Learning, Sequence Classification, Transformer, BiLSTM, TCN | Coastal Hypoxia Forecasting, Ocean Modeling, Environmental AI | [总结](./papers/2026/2602.05178/summary.md) |
|2025|[Graph Embedding with Mel-spectrograms for Underwater Acoustic Target Recognition](https://arxiv.org/abs/2512.11545)|IEEE|图神经网络, Transformer, Mel-spectrogram, non-Euclidean, 水下声学|underwater-target-recognition, sonar, ship-classification, acoustic-signal-processing, model-interpretability|[总结](./papers/2025/2512.11545/summary.md)|
|2025|[CTP: A hybrid CNN-Transformer-PINN model for ocean front](https://arxiv.org/abs/2505.10894)|Nature|CNN, Transformer, PINN, Navier-Stokes, 深度学习|海洋锋, SST, 预报, 分类, Kuroshio|[总结](./papers/2025/2505.10894/summary.md)|
|2024|[CAS-C ANGLONG: A SKILLFUL 3D TRANSFORMER MODEL FOR SUB-SEASONAL TO SEASONAL GLOBAL SEA SURFACE TEMPERATURE PREDICTION](https://arxiv.org/abs/2409.05369)|Nature|transformer, swin-transformer, attention-mechanism, 3d-cnn, lstm|sst-prediction, s2s-forecasting, enso, 海洋建模, climate-prediction|[总结](./papers/2024/2409.05369/summary.md)|
| 2024 | [Tropical Pacific Ocean Data Assimilation](https://arxiv.org/abs/2406.07063) | arXiv preprint | Deep Learning, Transformer, Data Assimilation, Ensemble Kalman Filter, Linear Inverse Model | Climate Reconstruction, ENSO Prediction, Paleoclimate Proxies, Tropical Pacific Ocean | [总结](./papers/2024/2406.07063/summary.md) |
|2024|[SST: Multi-Scale Hybrid Mamba-Transformer Experts for Time Series Forecasting](https://arxiv.org/abs/2404.14757)|CIKM|mamba, transformer, mixture-of-experts, 多尺度, state-space-model, time-series|time-series-forecasting, 天气预报, traffic-prediction, energy-forecasting, 海表温度预报|[总结](./papers/2024/2404.14757/summary.md)|

[更多 Transformer / Attention 论文 →](./papers/transformer.md)

---

## 应用场景

### 海表温度 (SST)
> 海表温度是海洋最重要的基础变量之一

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Ensemble Graph Neural Networks for Probabilistic Sea Surface Temperature Forecasting via Input Perturbations](https://arxiv.org/abs/2603.06153)|NeurIPS|GNN, 集成学习, 不确定性量化, SST, Perlin-noise|海表温度预报, 区域海洋, 加纳利流, ensemble-prediction, probabilistic-forecasting|[总结](./papers/2026/2603.06153/summary.md)|
|2026|[Extending SST Anomaly Forecasts Through Simultaneous Decomposition of Seasonal and PDO Modes](https://arxiv.org/abs/2601.01864)|Nature|SVD, linear-regression, PDO, seasonal-decomposition, multivariate-analysis|SST, Pacific-Decadal-Oscillation, North-Pacific, 海表温度, climate-prediction|[总结](./papers/2026/2601.01864/summary.md)|
|2026|[Spatio-temporal modeling and forecasting with Fourier neural operators](https://arxiv.org/abs/2601.01813)|Science|FNO, neural-operator, 动力学系统, 时空, 不确定性量化|SST, precipitation, 海洋建模, 大气建模, 预报|[总结](./papers/2026/2601.01813/summary.md)|
|2025|[OceanForecastBench: A Benchmark Dataset for Data-Driven Global Ocean Forecasting](https://arxiv.org/abs/2511.18732)|JGR: Machine Learning and Computation|benchmark, 深度学习, 全球海洋, multi-source-data, evaluation-pipeline|海洋预报, SST, 盐度, ocean-currents, 海平面|[总结](./papers/2025/2511.18732/summary.md)|
|2025|[Leveraging an Atmospheric Foundational Model for Subregional Sea Surface Temperature Forecasting](https://arxiv.org/abs/2510.25563)|NeurIPS|foundation-model, Aurora, SST, fine-tuning, 海洋预报|Canary-Upwelling, 海表温度, Northeastern-Atlantic, 区域海洋, potential-temperature|[总结](./papers/2025/2510.25563/summary.md)|
|2025|[SeaCast: Accurate Mediterranean Sea Forecasting via Graph-Based Deep Learning](https://arxiv.org/abs/2506.23900)|Nature|GNN, 图神经网络, 分层网格, 区域海洋, 自回归|地中海, 海洋预报, SST, SSH, 温度, 盐度, 海流|[总结](./papers/2025/2506.23900/summary.md)|

[更多 海表温度 (SST) 论文 →](./papers/sst.md)

---

### 海表高度 (SSH)
> 海表高度反映海洋动力过程和环流结构

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2025|[SeaCast: Accurate Mediterranean Sea Forecasting via Graph-Based Deep Learning](https://arxiv.org/abs/2506.23900)|Nature|GNN, 图神经网络, 分层网格, 区域海洋, 自回归|地中海, 海洋预报, SST, SSH, 温度, 盐度, 海流|[总结](./papers/2025/2506.23900/summary.md)|
|2022|[4DVarNet-SSH: End-to-End Learning of Variational Interpolation Schemes for Nadir and Wide-Swath Satellite Altimetry](https://arxiv.org/abs/2211.05904)|N/A - Preprint|4DVarNet, Deep Learning, SSH, Satellite Altimetry, SWOT卫星|Sea Surface Height, Gulf Stream, OSMOSIS, NATL60, DUACS|[总结](./papers/2022/2211.05904/summary.md)|
| 2022 | [Modeling Oceanic Variables with Dynamic Graph Neural Networks](https://arxiv.org/abs/2206.12746) | N/A - Preprint | GNN, Graph Neural Network, LSTM, Transformer, Dynamic Graph | Ocean Dynamics, Current Velocity, SSH, Santos Estuarine System | [总结](./papers/2022/2206.12746/summary.md) |

[更多 海表高度 (SSH) 论文 →](./papers/ssh.md)

---

### ENSO 预测
> ENSO 是最强的年际气候变化信号

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2024|[CAS-C ANGLONG: A SKILLFUL 3D TRANSFORMER MODEL FOR SUB-SEASONAL TO SEASONAL GLOBAL SEA SURFACE TEMPERATURE PREDICTION](https://arxiv.org/abs/2409.05369)|Nature|transformer, swin-transformer, attention-mechanism, 3d-cnn, lstm|sst-prediction, s2s-forecasting, enso, 海洋建模, climate-prediction|[总结](./papers/2024/2409.05369/summary.md)|
|2023|[Graph-Based Deep Learning for Sea Surface Temperature Forecasts](https://arxiv.org/abs/2305.09468)|ICLR Workshop|图神经网络, GCN, GAT, GraphSAGE, 海表温度预报, Climate-ML|海表温度, SST-Prediction, 气候建模, ENSO, 海洋预报|[总结](./papers/2023/2305.09468/summary.md)|
| 2023 | [On the Relative Role of East and West Pacific Sea Surface Temperature (SST) Gradients in the Prediction Skill of Central Pacific NINO3.4 SST](https://arxiv.org/abs/2302.11357) | Ocean Dynamics | CNN, Sea Surface Temperature Prediction, ENSO, Climate Modeling, Deep Learning | Climate Prediction, El Nino/La Nina Forecast, Ocean-Atmosphere Interaction, Sea Surface Temperature | [总结](./papers/2023/2302.11357/summary.md) |
| 2022 | [Data Assimilation in Operator Algebras](https://arxiv.org/abs/2206.13659) | Proceedings of the National Academy of Sciences | Koopman Operator, Quantum Data Assimilation, Operator Algebra, Matrix Mechanical DA | Lorenz 96, ENSO, Climate Model, Uncertainty Quantification | [总结](./papers/2022/2206.13659/summary.md) |
| 2022 | [A Deep Learning Model for Forecasting Global Monthly Mean Sea Surface Temperature Anomalies](https://arxiv.org/abs/2202.09967) | N/A - Preprint | Unet-LSTM, CNN, LSTM, ERA5, Deep Learning | SST, ENSO, Marine Heatwaves, Sea Surface Temperature | [总结](./papers/2022/2202.09967/summary.md) |

[更多 ENSO 预测 论文 →](./papers/enso.md)

---

### 海浪预报
> 海浪是海洋环境的重要组成部分

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Ocean Wave Prediction](https://arxiv.org/abs/2602.04067)|-|深度学习|海浪|[总结](./papers/2026/2602.04067/summary.md)|
|2026|[PINN Wave Model](https://arxiv.org/abs/2602.06989)|-|PINN|海浪|[总结](./papers/2026/2602.06989/summary.md)|
|2025|[Bridging Ocean Wave Physics and Deep Learning: Physics-Informed Neural Operators for Nonlinear Wavefield Reconstruction in Real-Time](https://arxiv.org/abs/2508.03315)|Nature|PINO, neural-operator, FNO, 物理约束, wave-reconstruction, HOSM|海浪, 波浪预测, buoy-measurements, X-band-radar, 相位解析|[总结](./papers/2025/2508.03315/summary.md)|
|2024|[OceanCastNet](https://arxiv.org/abs/2406.03848)|Nature|深度学习|海浪|[总结](./papers/2024/2406.03848/summary.md)|
|2023|[A Deep-learning Real-time Bias Correction Method for Significant Wave Height](https://arxiv.org/abs/2311.15001)|-|深度学习|海浪|[总结](./papers/2023/2311.15001/summary.md)|

[更多 海浪预报 论文 →](./papers/wave.md)

---

### 全球预报
> 全球海洋预报是气候预测的基础

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Neural ocean forecasting](https://arxiv.org/abs/2602.00598)|-|深度学习|Ocean-Forecast|[总结](./papers/2026/2602.00598/summary.md)|
|2025|[Tensor-Var: Efficient Four-Dimensional Variational Data Assimilation](https://arxiv.org/abs/2501.13312)|arXiv|4D-Var, Kernel Methods, Conditional Mean Embedding, Deep Learning, Data Assimilation|Weather Prediction, Chaotic Systems, Numerical Weather Prediction, Dynamical Systems|[总结](./papers/2025/2501.13312/summary.md)|
|2024|[DUNE Climate](https://arxiv.org/abs/2408.06262)|-|气候预报|全球|[总结](./papers/2024/2408.06262/summary.md)|

[更多 全球预报 论文 →](./papers/global-forecast.md)

---

### 海洋数据同化
> 利用数据同化技术融合观测与模型

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2025|[Meta-Learning Fourier Neural Operators for Hessian Inversion and Enhanced Variational Data Assimilation](https://arxiv.org/abs/2509.22949)|arXiv|元学习, Fourier Neural Operator, Data Assimilation, Inverse Hessian Approximation, Conjugate Gradient Method|Variational Data Assimilation, 4D-Var, Numerical Weather Prediction, PDE-Constrained Optimization|[总结](./papers/2025/2509.22949/summary.md)|
|2025|[CGKN: Conservative GPU-Native Kurgan Skeleton Network for Ocean Data Assimilation](https://arxiv.org/abs/2507.08749)|Nature|Koopman, Neural-Operator|海洋数据同化|[总结](./papers/2025/2507.08749/summary.md)|
|2024|[CG-EnKF: Conservative GPU-Native Ensemble Kalman Filter for Ocean Data Assimilation](https://arxiv.org/abs/2409.14300)|arXiv|EnKF|海洋数据同化|[总结](./papers/2024/2409.14300/summary.md)|
|2023|[Neural Koopman Prior for Data Assimilation](https://arxiv.org/abs/2309.05317)|IEEE TSP|Koopman|数据同化|[总结](./papers/2023/2309.05317/summary.md)|
|2022|[Deep Learning Enhanced Ensemble-based Data Assimilation](https://arxiv.org/abs/2206.04811)|-|EnKF, 深度学习|海洋数据同化|[总结](./papers/2022/2206.04811/summary.md)|

[更多 海洋数据同化 论文 →](./papers/?)

---

### 海冰
> 海冰是极地海洋的重要现象

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2025|[Prediction of Sea Ice Velocity and Concentration in the Arctic Ocean using Physics-informed Neural Network](https://arxiv.org/abs/2510.17756)|Nature|PINN, HIS-Unet, CNN, 物理约束, 海冰|北冰洋, 海冰速度, 海冰浓度, remote-sensing, multi-task-learning|[总结](./papers/2025/2510.17756/summary.md)|
|2023|[Deep Learning of Systematic Sea Ice Model Errors from Data Assimilation](https://arxiv.org/abs/2304.03832)|-|深度学习|海冰|[总结](./papers/2023/2304.03832/summary.md)|

[更多 海冰 论文 →](./papers/?)

---

### 深海
> 深海是海洋的主体部分

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Deep Ocean Prediction](https://arxiv.org/abs/2603.14115)|-|深度学习|深海|[总结](./papers/2026/2603.14115/summary.md)|
|2025|[Deep learning in the abyss: a stratified Physics Informed Neural Network for data assimilation](https://arxiv.org/abs/2503.19160)|JGR (Journal of Geophysical Research)|PINN, SIREN, 数据同化, quasi-geostrophic, stratified-ocean|深海, SWOT卫星, ARGO浮标, 海洋环流, 中尺度|[总结](./papers/2025/2503.19160/summary.md)|
|2021|[Deep Ocean](https://arxiv.org/abs/2105.05363)|-|深度学习|深海|-|

[更多 深海 论文 →](./papers/?)

---

### 气候预测
> 气候预测是海洋预报的最终目标之一

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Climate Transformer](https://arxiv.org/abs/2603.05560)|-|Transformer|气候|[总结](./papers/2026/2603.05560/summary.md)|
|2024|[Validating Deep Learning Weather-Navigation Models for Climate Prediction](https://arxiv.org/abs/2404.17652)|Nature|深度学习|天气|[总结](./papers/2024/2404.17652/summary.md)|
|2024|[CAS-C ANGLONG: A SKILLFUL 3D TRANSFORMER MODEL FOR SUB-SEASONAL TO SEASONAL GLOBAL SEA SURFACE TEMPERATURE PREDICTION](https://arxiv.org/abs/2409.05369)|Nature|transformer, swin-transformer, attention-mechanism, 3d-cnn, lstm|sst-prediction, s2s-forecasting, enso, 海洋建模, climate-prediction|[总结](./papers/2024/2409.05369/summary.md)|
|2021|[Climate DL](https://arxiv.org/abs/2105.02939)|-|Deep-Learning|Climate|-|

[更多 气候预测 论文 →](./papers/?)

---

### 海洋动力学
> 海洋动力学是理解海洋过程的基础

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Koopman Ocean](https://arxiv.org/abs/2602.05416)|-|Koopman|海洋动力学|[总结](./papers/2026/2602.05416/summary.md)|
|2026|[Ocean Physics](https://arxiv.org/abs/2603.07261)|-|物理约束|海洋动力学|[总结](./papers/2026/2603.07261/summary.md)|
|2026|[Submesoscale Dynamics](https://arxiv.org/abs/2602.05083)|-|深度学习|亚中尺度|[总结](./papers/2026/2602.05083/summary.md)|
|2024|[Semilinear Neural Operators](https://arxiv.org/abs/2402.15656)|arXiv|Neural-Operator|海洋|[总结](./papers/2024/2402.15656/summary.md)|

[更多 海洋动力学 论文 →](./papers/?)

---

### 海平面
> 海平面变化是全球变化的敏感指标

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2026|[Sea Surface Height](https://arxiv.org/abs/2603.16272)|-|深度学习|SSH|[总结](./papers/2026/2603.16272/summary.md)|
|2025|[Principled Operator Learning in Ocean Dynamics: The Role of Temporal Structure](https://arxiv.org/abs/2510.09792)|NeurIPS|neural-operator, FNO, 时间色散, 海洋建模, 物理约束|海洋环流, 海平面预测, Baltic-Sea, 区域海洋, wave-propagation|[总结](./papers/2025/2510.09792/summary.md)|
|2023|[Multi-decadal Sea Level Prediction using Neural Networks and Spectral Analysis](https://arxiv.org/abs/2310.04540)|-|深度学习|海平面|[总结](./papers/2023/2310.04540/summary.md)|

[更多 海平面 论文 →](./papers/?)

---

### 参数化
> 海洋参数化是气候模型的关键

| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
|------|------|-------|------|------|------|
|2025|[Generalizable Neural Network Parameterizations from Incompressible Flow](https://arxiv.org/abs/2505.08900)|arXiv preprint|物理约束|参数化|[总结](./papers/2025/2505.08900/summary.md)|
|2023|[Robust Ocean Subgrid-Scale Parameterizations Using Fourier Neural Operators](https://arxiv.org/abs/2310.02691)|-|Neural-Operator|海洋|[总结](./papers/2023/2310.02691/summary.md)|
|2022|[GNN-Surrogate: A Hierarchical and Adaptive Graph Neural Network for Parameterization](https://arxiv.org/abs/2202.08956)|-|GNN|参数化|[总结](./papers/2022/2202.08956/summary.md)|

[更多 参数化 论文 →](./papers/?)

---

## 按年份浏览

| 年份 | 论文数 | 浏览 |
|------|--------|------|
| 2026 | 19 | [浏览](./papers/2026/index.md) |
| 2025 | 39 | [浏览](./papers/2025/index.md) |
| 2024 | 26 | [浏览](./papers/2024/index.md) |
| 2023 | 17 | [浏览](./papers/2023/index.md) |
| 2022 | 13 | [浏览](./papers/2022/index.md) |
| 2021 | 9 | [浏览](./papers/2021/index.md) |
| 2020 | 3 | [浏览](./papers/2020/index.md) |
| 2019 | 2 | [浏览](./papers/2019/index.md) |
| 2017 | 1 | [浏览](./papers/2017/index.md) |
| 2015 | 1 | [浏览](./papers/2015/index.md) |
| 2014 | 1 | [浏览](./papers/2014/index.md) |
| 2013 | 1 | [浏览](./papers/2013/index.md) |
| 2012 | 2 | [浏览](./papers/2012/index.md) |
| 2011 | 1 | [浏览](./papers/2011/index.md) |

---

## 如何贡献

欢迎提交 PR 或 Issue！详见 [贡献指南](./CONTRIBUTING.md)。
