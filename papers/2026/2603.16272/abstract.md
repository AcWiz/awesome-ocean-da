---
title: "Probabilistic reconstruction of global sea surface temperature using generative diffusion models"
arXiv: "2603.16272"
authors: ["Haijie Li", "Ya Wang", "Kai Yang", "Gang Huang", "Xiangao Xia", "Ziming Chen", "Weichen Tao", "Chenglin Lu", "Lin Chen", "Miao Zhang", "Kaiming Hu", "Hainan Gong", "Disong Fu", "Lin Wang"]
year: 2026
source: "arXiv"
venue: "arXiv"
method_tags: ["Diffusion Model", "Generative Model", "Uncertainty Quantification", "Data Assimilation", "Probabilistic Reconstruction"]
application_tags: ["Sea Surface Temperature", "Climate Prediction", "Ocean State Estimation", "El Niño Forecasting"]
difficulty: "★★★★☆"
importance: "★★★★★"
read_status: "skim"
---

# Probabilistic reconstruction of global sea surface temperature using generative diffusion models

## 1. 基本信息

- **论文链接**: https://arxiv.org/abs/2603.16272
- **作者机构**: 中国气象局、国家卫星气象中心、清华大学等（具体机构信息需从论文全文获取）
- **开源代码**: 未在提供内容中明确提及（建议查阅全文或补充材料确认）

## 2. 一句话总结（TL;DR）

本文提出了SAGE（Satellite and in situ Adaptive Guided Estimation）框架，这是首个基于扩散模型的全球海表温度（SST）概率重建方法。SAGE通过学习历史SST变化的物理一致先验，结合风云-3D卫星数据和现场观测数据进行后验采样，能够生成集合SST估计场，有效量化观测不确定性，并在10天预报和2023-2024年厄尔尼诺事件预测中展现出比现有业务产品更高的精度。

## 3. 研究问题（Problem Definition）

### 核心问题

全球海表温度（SST）是主导海气耦合和全球气候变率的关键变量，精确的SST重建对于气候监测和预测至关重要。

### 研究背景与挑战

1. **数据异构性**：现有SST重建产品主要依赖异构卫星数据和现场观测，这些数据源具有不同的时空分辨率和误差特性。

2. **不确定性表示缺失**：传统SST重建产品仅提供一个确定性场，无法有效表示观测不确定性和多尺度变异性。

3. **概率预测支持不足**：确定性重建无法支持概率预报和集合预测，限制了其在气候预测系统中的应用价值。

4. **极端事件捕捉困难**：稀疏的现场测量难以准确捕捉局部异常和极端SST事件。

## 4. 核心贡献（Contributions）

1. **创新性框架**：提出SAGE（Satellite and in situ Adaptive Guided Estimation），首个基于扩散模型的不确定性感知生成式SST重建框架，将数据同化技术与深度生成模型相结合。

2. **渐进式数据融合策略**：设计了两阶段数据融合机制，首先利用两颗风云-3D极轨卫星观测约束盆地尺度结构，然后使用稀疏现场测量细化局部异常和极端值。

3. **物理一致性先验学习**：SAGE学习历史SST变化的物理一致先验分布，确保生成的SST场符合海洋动力学约束。

4. **气候预测应用验证**：首次展示生成式SST重建在初始化预报系统中的实际价值，在10天SST预报和2023-2024年厄尔尼诺事件预测中均表现出附加价值。

## 5. 方法详解（Methodology）

### 整体架构

SAGE采用基于扩散概率模型（Diffusion Probabilistic Model）的生成式框架，核心思想是在潜在空间中进行迭代去噪，生成符合物理约束的SST场。

### 技术路线

1. **先验学习阶段**：
   - 利用大规模历史SST再分析数据训练扩散模型
   - 学习SST的时空变化模式和物理一致性特征
   - 建立多尺度SST变化的概率分布先验

2. **条件重建阶段**：
   - 输入多源异构观测数据（卫星SST、浮标、船舶观测等）
   - 通过引导机制（guidance mechanism）将观测约束融入扩散过程
   - 执行后验采样，生成集合SST估计

3. **渐进式数据融合**：
   - **第一阶段**：卫星数据约束大尺度结构
     - 利用风云-3D卫星的微波和红外SST产品
     - 捕捉盆地尺度的SST梯度和大尺度环流特征
   - **第二阶段**：现场测量细化局部特征
     - 融合浮标、Argo剖面等稀疏观测
     - 修正局部异常和极端值
     - 提高近岸和涡旋区精度

### 关键创新点

- **不确定性感知生成**：通过集合采样自然地量化观测和模式不确定性
- **多尺度保真度**：同时保持大尺度结构和局部细节的准确性
- **观测加权机制**：根据不同数据源的质量和覆盖度自适应调整融合权重

## 6. 数学与物理建模（Math & Physics）

### 扩散模型基础

SAGE基于去噪扩散概率模型（DDPM），包含前向扩散过程和逆向去噪过程：

**前向过程** $q(\mathbf{x}_t | \mathbf{x}_{t-1})$：
$$
q(\mathbf{x}_t | \mathbf{x}_{t-1}) = \mathcal{N}(\mathbf{x}_t; \sqrt{1-\beta_t}\mathbf{x}_{t-1}, \beta_t\mathbf{I})
$$

**逆向过程** $p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t)$：
$$
p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t) = \mathcal{N}(\mathbf{x}_{t-1}; \mu_\theta(\mathbf{x}_t, t), \Sigma_\theta(\mathbf{x}_t, t))
$$

### 条件生成机制

对于给定观测 $\mathbf{y}$，SAGE通过条件逆向过程进行采样：
$$
p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t, \mathbf{y}) = p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t) \cdot p(\mathbf{y} | \mathbf{x}_t)
$$

### 物理约束融合

SAGE引入海表温度的物理约束项，包括：
- **能量守恒约束**：确保SST场的面积平均变化符合热力学规律
- **时空连续性约束**：通过正则化项强制平滑
- **海气耦合约束**：与大气强迫场保持一致

## 7. 实验分析（Experiments）

**数据集**:
- 风云-3D（FY-3D）卫星SST产品
- 多源现场观测数据（浮标、Argo、船舶观测）
- 历史SST再分析数据（用于训练）
- 独立验证数据集

**评估指标**:
- 均方根误差（RMSE）
- 相关系数（Correlation）
- 不确定性校准度（Uncertainty Calibration）
- 集合离散度（Ensemble Spread）

**对比方法**:
- 现有业务化SST重建产品（如OISST、OSTIA等）
- 传统数据同化方法
- 其他生成式重建方法

**核心结果**:

1. **重建精度提升**：与独立现场观测验证显示，SAGE显著降低重建误差

2. **不确定性量化有效**：生成的集合SST场能够准确反映观测不确定性

3. **多尺度变异性保持**：成功捕捉从盆地尺度到局部尺度的SST变化

4. **预报性能改进**：
   - 10天SST预报误差明显低于业务分析场
   - 预报改进在热带太平洋等关键海区尤为显著

5. **厄尔尼诺事件预测**：2023-2024年厄尔尼诺事件的 onset 和强度演化预测表现优于传统方法

## 8. 优缺点分析（Critical Review）

**优点**:

- **创新性强**：首次将扩散模型应用于全球海洋状态估计，具有重要的方法论创新价值
- **不确定性量化**：解决了传统SST重建缺乏不确定性感知的根本问题
- **多源数据融合**：巧妙利用不同数据源的优势，实现优势互补
- **实际应用价值**：不仅限于重建，还成功应用于预报系统初始化
- **气候事件预测**：在厄尔尼诺预测中展现出附加价值，具有重要的科学意义

**缺点**:

- **计算成本**：扩散模型的迭代采样过程计算量大，实时应用可能受限
- **模型依赖性**：重建质量依赖于先验模型的准确性，可能在极端事件中表现不足
- **观测覆盖依赖**：在观测稀疏区域（如南大洋），重建质量可能下降
- **超参数敏感**：数据融合权重等超参数需要精细调整
- **验证范围**：作为新方法，长期气候重建性能需要进一步验证

## 9. 对我的启发（For My Research）

1. **生成式AI在海洋科学中的应用潜力**：扩散模型能够学习复杂的多尺度海洋变量分布，为海洋数据同化提供了新的思路。

2. **不确定性量化范式转变**：传统数据同化提供单点估计，而生成式方法自然地提供集合估计，这种范式可能成为未来海洋状态估计的主流。

3. **多源数据协同的重要性**：渐进式数据融合策略为如何有效利用异构观测数据提供了参考。

4. **重建与预报的一体化**：将重建作为预报系统初始化的前处理步骤，打通了观测到预测的价值链。

5. **物理约束与数据驱动的结合**：如何将物理规律融入神经网络是提高模型可解释性和准确性的关键。

## 10. Idea 扩展与下一步（Next Steps）

1. **多变量联合重建**：将SAGE框架扩展到海表盐度、叶绿素浓度等多海洋变量联合重建，实现三维海洋状态的概率重建。

2. **实时业务化部署**：优化推理效率，探索模型压缩和蒸馏技术，开发适合业务运行的轻量化版本。

3. **更长时间尺度预测**：将方法应用于年代际尺度气候预测，探索SST重建对长期气候预估的价值。

4. **区域精细化应用**：针对中国近海等特定区域进行精细化建模，结合区域海洋动力学特征优化模型。

5. **与其他AI模型结合**：探索与物理信息神经网络（PINN）、图神经网络（GNN）的结合，进一步提高物理一致性。

## 11. 引用格式（BibTex）

```bibtex
@article{Li2026SAGE,
  title={Probabilistic reconstruction of global sea surface temperature using generative diffusion models},
  author={Li, Haijie and Wang, Ya and Yang, Kai and Huang, Gang and Xia, Xiangao and Chen, Ziming and Tao, Weichen and Lu, Chenglin and Chen, Lin and Zhang, Miao and Hu, Kaiming and Gong, Hainan and Fu, Disong and Wang, Lin},
  journal={arXiv preprint},
  year={2026},
  eprint={2603.16272},
  archivePrefix={arXiv},
  primaryClass={physics.ao-ph}
}