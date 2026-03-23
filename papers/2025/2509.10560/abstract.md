---
title: "GTS_Forecaster: a novel deep learning based geodetic time series forecasting toolbox with python"
arXiv: "2509.10560"
authors: ["Xuechen Liang", "Xiaoxing He", "Shengdao Wang", "Jean-Philippe Montillet", "Zhengkai Huang", "Gaël Kermarrec", "Shunqiang Hu", "Yu Zhou", "Jiahui Huang"]
year: 2025
source: "arXiv"
venue: "arXiv"
method_tags: ["Deep Learning", "Graph Neural Networks", "Time Series Forecasting", "KAN", "GNN-GRU", "Reinforcement Learning", "Gap-filling"]
application_tags: ["Geodetic Time Series", "GNSS", "Sea Surface Height", "Tide Gauge", "Hazard Mitigation"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# GTS_Forecaster: a novel deep learning based geodetic time series forecasting toolbox with python

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2509.10560
- **作者机构**: 梁学辰 (Xuechen Liang), 何晓星 (Xiaoxing He), 王盛道 (Shengdao Wang), Jean-Philippe Montillet, 黄政凯 (Zhengkai Huang), Gaël Kermarrec, 胡顺强 (Shunqiang Hu), 周宇 (Yu Zhou), 黄嘉辉 (Jiahui Huang)
- **开源代码**: GitHub链接未在摘要中明确提供，但文中提到"open-source Python package"

## 2. 一句话总结（TL;DR）
GTS_Forecaster是一个面向大地测量时间序列预测的开源Python工具箱，集成了KAN、GNN-GRU、TimeGNN等先进深度学习模型，并提供了基于强化学习的KTIF缺失值填补算法和WQE评估指标，能够有效处理GNSS、卫星测高海表面高度和验潮仪记录等数据的非线性、非平稳时空依赖问题。

## 3. 研究问题（Problem Definition）
大地测量时间序列（如GNSS位置数据、卫星测高海表面高度SSH、验潮仪TG记录）在监测地表变形和海平面变化中至关重要。然而，这些时间序列具有非线性、非平稳和不完整的特性，受地球物理、气候和人为因素影响显著。传统统计模型（如ARIMA）和标准机器学习方法难以捕捉多尺度时空依赖，导致预测精度受限。现有深度学习在 geodesy 预测中的应用相对有限，缺乏针对地球科学需求的集成化工具箱。

## 4. 核心贡献（Contributions）
1. **开源工具箱**: 推出GTS-Forecaster Python包，提供完整的预处理、预测、可视化和评估功能
2. **先进模型集成**: 整合多种深度学习架构，包括KAN、GNN-GRU、TimeGNN、LSTM、GRU、TCN、BiLSTM、Transformer和Informer
3. **创新预处理模块**: 开发基于强化学习的KTIF缺失值填补算法和鲁棒的异常值检测工具
4. **评估指标**: 提出加权质量评估（WQE）指数用于定量评价预测精度
5. **多源数据支持**: 同时支持GNSS、SSH和TG数据集的预测，并可扩展到通用时间序列应用

## 5. 方法详解（Methodology）

### 5.1 核心模型架构
- **KAN (Kolmogorov-Arnold Networks)**: 利用Kolmogorov-Arnold表示定理，通过可学习激活函数替代传统固定激活函数，增强网络表达能力
- **GNN-GRU**: 将图神经网络与门控循环单元结合，用于建模空间拓扑关系和时间依赖
- **TimeGNN**: 时间感知图神经网络，同时考虑时间动态性和空间相关性

### 5.2 传统模型集成
工具箱还集成了经典深度学习模型用于对比和补充：
- LSTM (长短期记忆网络)
- GRU (门控循环单元)
- TCN (时序卷积网络)
- BiLSTM (双向LSTM)
- Transformer
- Informer

### 5.3 预处理模块
- **异常值检测**: 鲁棒的数据清洗工具
- **KTIF (Kalman-TransFusion Interpolation Framework)**: 基于强化学习的图信息自回归缺失值填补算法

### 5.4 评估模块
- **WQE (Weighted Quality Evaluation)**: 加权质量评估指数，用于定量评价模型预测精度

## 6. 数学与物理建模（Math & Physics）

### 6.1 问题形式化
给定历史观测序列 $X_{1:T} = \{x_1, x_2, ..., x_T\}$，预测未来 $H$ 步序列 $X_{T+1:T+H}$，其中：
- $x_t \in \mathbb{R}^D$ 为 $D$ 维特征向量
- $T$ 为历史窗口长度
- $H$ 为预测步长

### 6.2 KAN核心思想
基于Kolmogorov-Arnold表示定理，将多变量函数分解为单变量函数组合：
$$f(x_1, ..., x_n) = \sum_{q=1}^{2n+1} \Phi_q\left(\sum_{i=1}^{n} \phi_{q,i}(x_i)\right)$$
其中 $\phi_{q,i}$ 为可学习的单变量激活函数。

### 6.3 GNN-GRU时空建模
图神经网络捕获空间依赖：
$$h_i^{(l+1)} = \sigma\left(W^{(l)} \cdot \text{AGG}\left(\{h_j^{(l)} : j \in \mathcal{N}(i) \cup \{i\}\}\right)\right)$$
GRU捕获时间动态：
$$r_t = \sigma(W_r \cdot [h_{t-1}, x_t])$$
$$z_t = \sigma(W_z \cdot [h_{t-1}, x_t])$$
$$h_t = (1-z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$

### 6.4 KTIF缺失值填补
将缺失值填补问题建模为马尔可夫决策过程，利用强化学习策略优化填补序列。

## 7. 实验分析（Experiments）
**数据集**: 
- GNSS位置数据（全球导航卫星系统）
- SSH（卫星测高海表面高度）
- TG（验潮仪记录）

**评估指标**: 
- WQE (加权质量评估指数)
- 其他标准时间序列评估指标（RMSE、MAE等）

**对比方法**: 
- ARIMA（自回归差分移动平均模型）
- SVM（支持向量机）
- LSTM、GRU、TCN、BiLSTM
- Transformer、Informer

**核心结果**: 
论文通过实验验证了集成模型（特别是KAN、GNN-GRU、TimeGNN）在处理非线性、非平稳大地测量时间序列方面的优势，具体数值结果需查阅完整论文。

## 8. 优缺点分析（Critical Review）

**优点**:
- **模型丰富**: 集成了从传统RNN到最新KAN等多种架构，便于对比研究
- **领域定制**: 专门针对大地测量时间序列设计，预处理模块考虑了地球科学数据特点
- **开源易用**: Python实现，提供了完整的预处理-预测-评估工作流
- **创新填补**: KTIF算法将强化学习应用于缺失值填补，具有原创性

**缺点**:
- **实验细节有限**: 当前摘要中缺乏具体数值结果和消融实验分析
- **计算复杂度**: 多种模型集成可能导致计算资源需求较高
- **泛化性验证**: 需要更多不同地理区域和气候条件的实验验证
- **模型可解释性**: 深度学习模型在地球科学应用中的物理解释仍需加强

## 9. 对我的启发（For My Research）
1. **海洋数据同化扩展**: GTS-Forecaster的时空建模方法可借鉴到海洋Argo浮标、卫星海表温度等数据的预测
2. **KTIF算法迁移**: 基于强化学习的缺失值填补思路可应用于海洋观测数据的质量控制
3. **多源数据融合**: 图神经网络建模空间关系的思想可用于海洋-大气耦合系统的建模
4. **评估指标设计**: WQE指数的设计理念可启发海洋预测模型的综合评价体系

## 10. Idea 扩展与下一步（Next Steps）
1. 将GTS-Forecaster中的图神经网络方法扩展到海洋锋面、涡旋等中尺度现象的预测
2. 结合物理约束（如海洋动力学方程）开发Physics-informed深度学习模型
3. 探索Transformer架构在长时间海洋气候预测中的应用潜力
4. 开发海洋专属的预处理模块，包括潮汐滤波、季节性分解等

## 11. 引用格式（BibTex）
```bibtex
@article{Liang2025GTSForecaster,
  title={GTS\_Forecaster: a novel deep learning based geodetic time series forecasting toolbox with python},
  author={Liang, Xuechen and He, Xiaoxing and Wang, Shengdao and Montillet, Jean-Philippe and Huang, Zhengkai and Kermarrec, Gaël and Hu, Shunqiang and Zhou, Yu and Huang, Jiahui},
  journal={arXiv preprint arXiv:2509.10560},
  year={2025}
}