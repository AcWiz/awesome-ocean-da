---
title: "Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage"
arXiv: "2602.12274"
authors: ["Xin Ju", "Jiachen Yao", "Anima Anandkumar", "Sally M. Benson", "Gege Wen"]
year: 2026
source: "arXiv"
venue: "arXiv"
method_tags: ["Diffusion Models", "Neural Operators", "Inverse Problems", "Data Assimilation", "Bayesian Inference"]
application_tags: ["Carbon Capture and Storage", "Subsurface Flow Modeling", "Geological Parameter Estimation", "CO2 Plume Migration"]
difficulty: "★★★★☆"
importance: "★★★★☆"
read_status: "skim"
---

# Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2602.12274
- **作者机构**: Xin Ju, Jiachen Yao (卡内基梅隆大学), Anima Anandkumar (卡内基梅隆大学/NVIDIA), Sally M. Benson (斯坦福大学), Gege Wen (卡内基梅隆大学)
- **开源代码**: 未在文中明确提供GitHub链接

## 2. 一句话总结（TL;DR）
本文提出Fun-DDPS框架，通过解耦扩散模型先验与物理约束，利用函数空间扩散模型学习地质参数分布，并结合局部神经算子（LNO）代理模型提供物理一致的梯度指导，在碳捕集与封存（CCS）场景下实现了鲁棒的正向建模和精确的逆问题求解，在仅25%观测数据条件下达到7.7%的相对误差，并首次通过拒绝采样验证了扩散逆求解器的渐近精确性。

## 3. 研究问题（Problem Definition）
**核心问题**: 碳捕集与存储（CCS）中的地下流动精确表征面临严峻挑战，特别是在稀疏观测条件下的不适定逆问题。

**问题重要性**: CCS是应对气候变化的关键技术，其安全性和有效性依赖于两个计算任务：1）正向建模预测CO2羽流迁移和压力累积；2）逆问题建模从稀疏监测数据表征地下地质非均匀性。

**关键挑战**:
- 地下参数是高维且非高斯的
- 多相流方程计算成本高昂
- 传统集合卡尔曼滤波（EnKF）等方法依赖高斯假设，无法捕捉离散岩相或通道化储层等复杂地质特征
- 严格贝叶斯采样方法（如MCMC）计算成本过高
- 现有联合状态架构的扩散模型学习统计相关性而非显式物理定律，导致物理不一致性

## 4. 核心贡献（Contributions）
1. **鲁棒正向建模**: 利用生成先验重构缺失数据，在仅25%数据覆盖条件下实现7.7%相对误差，相比标准代理模型的86.9%误差提升11倍
2. **物理一致的反演**: 通过物理基代理模型引导扩散过程，消除联合状态模型常见的高频伪影，即使在有限观测下也能产生地质真实的后验样本
3. **严格验证**: 首次对扩散逆求解器进行渐近精确拒绝采样后验的严格基准测试，达到JS散度<0.06的统计精度，计算成本降低4倍

## 5. 方法详解（Methodology）

### 5.1 整体框架
Fun-DDPS（Function-space Decoupled Diffusion Posterior Sampling）将地质先验学习与流动物理近似解耦：

```
┌─────────────────────────────────────────────────────┐
│                  Fun-DDPS Framework                 │
├─────────────────────────────────────────────────────┤
│  [地质参数先验 p(m)]  ←──  函数空间扩散模型          │
│         ↓                                          │
│  [局部神经算子 LNO]  ←──  物理约束代理模型           │
│         ↓                                          │
│  [交叉场条件化]      ←──  动态场梯度指导             │
│         ↓                                          │
│  [后验采样 p(m|s_obs)]                              │
└─────────────────────────────────────────────────────┘
```

### 5.2 核心组件

**1. 地质参数先验学习（单通道函数空间扩散模型）**
- 学习地质参数m的分布 p(m)
- 在函数空间中操作，而非像素空间
- 使用单通道扩散模型避免联合状态的高维问题

**2. 局部神经算子（LNO）代理模型**
- 近似正向物理过程：s = ℒ_φ(m)
- 提供可微分的梯度用于反向传播
- 提供跨场的条件化指导

**3. 推理过程**
- 利用可微神经代理将稀疏观测的梯度反向传播到扩散生成过程
- 实现数据同化，无需联合训练

### 5.3 解耦优势
- 扩散先验稳健恢复参数空间缺失信息
- 代理模型提供高效梯度指导
- 避免联合状态模型的物理不一致问题

## 6. 数学与物理建模（Math & Physics）

### 6.1 问题 formulation

**正向问题**: 给定地质参数m，预测动态状态s
$$s = \mathcal{L}(m)$$

**逆问题**: 给定稀疏观测s_obs，推断地质参数后验分布
$$p(m | s_{obs}) \propto p(s_{obs} | m) p(m)$$

### 6.2 函数空间扩散模型
- 在函数空间而非有限维向量空间定义分布
- 使用denoising score matching训练
- 前向过程逐渐添加高斯噪声
- 反向过程学习score function

### 6.3 条件化机制
通过LNO代理模型提供的物理梯度指导扩散过程：
$$\nabla_m \mathcal{L}_\phi(m) \cdot (s_{obs} - \hat{s})$$

### 6.4 评估指标
- **相对误差**: $\frac{||m - \hat{m}||_2}{||m||_2}$
- **Jensen-Shannon散度**: 验证后验样本与拒绝采样ground truth的分布一致性

## 7. 实验分析（Experiments）

**数据集**: 
- 合成CCS建模数据集
- 包含地质参数（渗透率、孔隙度等）与其对应的多相流动态状态

**评估指标**: 
- 相对误差（Relative Error）
- Jensen-Shannon散度（JS divergence）
- 计算效率（样本效率）

**对比方法**: 
- 标准神经网络代理模型（86.9%误差基线）
- 联合状态Fun-DPS基线
- 拒绝采样（RS）渐近精确后验

**核心结果**:
1. **正向建模**: 仅25%观测数据条件下，Fun-DDPS达到7.7%相对误差 vs 标准代理模型86.9%（11倍提升）
2. **逆问题求解**: Fun-DDPS和Fun-DPS均达到JS散度<0.06的统计精度
3. **样本质量**: Fun-DDPS产生物理一致的样本，无联合状态模型的高频伪影
4. **计算效率**: 相比拒绝采样实现4倍样本效率提升

## 8. 优缺点分析（Critical Review）

**优点**:
- 成功解耦先验学习与物理近似，避免联合训练的复杂性
- 在极端数据稀疏（25%）场景下表现出色，验证了生成先验的鲁棒性
- 首次提供扩散逆求解器的严格统计验证，具有重要方法论意义
- 物理一致的样本质量对实际地质应用至关重要

**缺点**:
- 仅在合成数据集验证，真实CCS场景的适用性待验证
- LNO代理模型的精度直接影响反演质量，需预先训练
- 对于超大规模3D地质模型的计算可扩展性未充分讨论
- 拒绝采样验证在低维可行，高维场景的计算可行性存疑

## 9. 对我的启发（For My Research）

**海洋数据同化的潜在应用**:
1. **替代传统EnKF**: 函数空间扩散先验可替代高斯假设，更好地捕捉海洋参数的复杂非高斯分布（如涡旋、锋面等）
2. **稀疏观测处理**: 海洋观测同样面临空间稀疏性问题，Fun-DDPS的鲁棒性为卫星高度计、Argo浮标等稀疏数据的利用提供新思路
3. **物理一致约束**: 将物理约束解耦为独立模块的思想可应用于海洋环流模型的逆问题，保持物理守恒性
4. **验证方法论**: 严格的JS散度验证框架为海洋数据同化方法的评估提供了新标准

## 10. Idea 扩展与下一步（Next Steps）

1. **真实海洋数据集验证**: 将Fun-DDPS应用于真实海洋温盐场重构，如ARMOR3D或EN4数据集，验证其在实际海洋条件下的性能
2. **高维3D扩展**: 研究函数空间扩散在三维海洋模型（如MITgcm输出）上的可扩展性，解决计算效率和内存约束
3. **多物理场耦合**: 扩展到海洋-大气耦合系统，将扩散先验扩展到多场联合推断，如海表温度与盐度的协同重构
4. **在线学习框架**: 结合海洋模型的时变特性，开发增量更新机制，使先验和代理模型能够适应时间演化的海洋状态
5. **可解释性增强**: 引入不确定性量化工具，为海洋参数估计提供可信区间，支持海洋科学决策

## 11. 引用格式（BibTex）
```bibtex
@article{Ju2026FunctionSpaceDecoupled,
  title={Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage},
  author={Ju, Xin and Yao, Jiachen and Anandkumar, Anima and Benson, Sally M. and Wen, Gege},
  year={2026},
  eprint={2602.12274},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  journal={arXiv preprint arXiv:2602.12274}
}