---
title: "Reduced-Order Surrogates for Forced Flexible Mesh Coastal-Ocean Models"
arXiv: "2602.05416v1"
authors: ["Freja Høgholm Petersen", "Jesper Sandvig Mariegaard", "Rocco Palmitessa", "Allan P. Engsig-Karup"]
year: 2026
source: "arXiv"
venue: "arXiv"
method_tags: ["Koopman Autoencoder", "Reduced-Order Modeling", "Proper Orthogonal Decomposition", "Temporal Unrolling", "Neural Network Surrogates"]
application_tags: ["Coastal-Ocean Modeling", "Hydrodynamics", "Sea Surface Elevation Prediction", "Current Velocity Prediction", "Climate Simulation"]
difficulty: "★★★★☆"
importance: "★★★★☆"
read_status: "skim"
---

# Reduced-Order Surrogates for Forced Flexible Mesh Coastal-Ocean Models

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2602.05416
- **作者机构**: Technical University of Denmark (DTU)
- **开源代码**: None (文中未提及代码开源)

## 2. 一句话总结（TL;DR）
本文提出了一种结合气象强迫和边界条件的灵活Koopman自编码器框架，并与基于POD的代理模型进行系统比较。该方法在三个真实水动力学测试案例上实现了300-1400倍的推理加速，预测误差相对均方根误差达0.01-0.13，R²值达0.65-0.996，能够支持长达一年的海岸-海洋预测。

## 3. 研究问题（Problem Definition）
**核心问题**: 物理基础海洋模型虽然精度高，但计算成本高昂，限制了其在长期气候模拟和大ensemble预报中的应用。如何在保持预测精度的同时大幅提升计算效率？

**研究背景**:
- 海平面上升和极端天气事件使海岸区域面临日益严峻的威胁
- 传统物理模型（如ADCIRC、Delft3D、MIKE 21）需要精细空间分辨率和小时间步长
- 长时域稳定性和对真实大气强迫的鲁棒性是关键挑战

**关键挑战**:
1. 大规模操作模型的计算瓶颈
2. 长期预测的时域稳定性
3. 真实气象强迫和边界条件下的鲁棒性
4. 可解释性和可控的稳定性

## 4. 核心贡献（Contributions）
1. **灵活的Koopman自编码器框架**: 首次将气象强迫和边界条件纳入Koopman自编码器架构，实现了端到端的降阶代理建模
2. **系统性对比研究**: 对Koopman自编码器与POD基代理模型进行了全面评估，包括特征值正则化和时域展开技术的效果
3. **长期稳定预测**: 通过时域展开技术实现了长达一年的稳定预测（30分钟时间分辨率），相对RMSE为0.01-0.13
4. **实际应用验证**: 与现场观测数据对比，水面高程预测误差变化为-0.65%至12%（对应厘米级误差），满足实际应用需求

## 5. 方法详解（Methodology）

### 5.1 整体框架
本研究开发了两类降阶代理模型：

**A. POD基代理模型**
- 使用截断的POD基将高维状态压缩到低维潜在空间
- 神经网络用于传播降阶状态
- 空间分量与时间分量显式分离

**B. Koopman自编码器（CKAEs）**
- **编码器**: 将高维物理场映射到潜在空间
- **解码器**: 从潜在空间重建物理场
- **Koopman算子学习**: 在潜在空间学习线性时域算子
- **特征值正则化**: 促进时域稳定性
- **时域展开**: 用于长期预测的迭代展开技术

### 5.2 关键设计
- **气象强迫集成**: 将气象强迫作为外部输入纳入网络
- **边界条件处理**: 灵活处理开放边界和陆地边界
- **稳定性约束**: 通过特征值正则化和时域展开确保长期预测稳定性

## 6. 数学与物理建模（Math & Physics）

### 6.1 Koopman算子理论
Koopman算子理论提供了一种将非线性动力系统线性化的框架：
- 原始系统：$\frac{d\mathbf{x}}{dt} = \mathbf{f}(\mathbf{x})$
- Koopman观测：$\mathbf{z} = \mathbf{g}(\mathbf{x})$
- 线性演化：$\mathbf{z}(t+\Delta t) = \mathbf{K} \mathbf{z}(t)$

其中 $\mathbf{K}$ 是Koopman算子在离散化后的矩阵表示。

### 6.2 自编码器架构
- **编码器**: $\mathbf{z} = \phi(\mathbf{x}; \theta_e)$
- **解码器**: $\hat{\mathbf{x}} = \psi(\mathbf{z}; \theta_d)$
- **潜在动态**: $\mathbf{z}_{t+1} = \mathbf{K} \mathbf{z}_t + \mathbf{B} \mathbf{u}_t$

其中 $\mathbf{u}_t$ 表示外部强迫输入。

### 6.3 损失函数
综合损失函数包括：
- 重构损失：$\mathcal{L}_{recon} = \|\mathbf{x} - \hat{\mathbf{x}}\|^2$
- 预测损失：$\mathcal{L}_{pred} = \|\mathbf{z}_{t+1} - \mathbf{K}\mathbf{z}_t\|^2$
- 特征值正则化：$\mathcal{L}_{eig} = \sum_i \max(0, |\lambda_i| - 1)$

## 7. 实验分析（Experiments）

**数据集**: 
- 三个真实水动力学测试案例，覆盖不同动力机制
- 预测时间跨度：长达一年
- 时间分辨率：30分钟

**评估指标**:
- 相对均方根误差（Relative RMSE）
- 决定系数（R²）
- 预测误差变化百分比
- 推理加速比

**对比方法**:
1. POD基代理模型（截断基）
2. POD + 神经网络时域推进
3. Koopman自编码器（无时域展开）
4. Koopman自编码器（有时域展开）

**核心结果**:
| 指标 | 数值范围 |
|------|----------|
| 相对RMSE | 0.01–0.13 |
| R²值 | 0.65–0.996 |
| 推理加速 | 300–1400x |
| 水面高程误差变化 | -0.65%至12% |

**关键发现**:
- Koopman自编码器 + 时域展开在所有案例中表现最佳
- 流速预测误差最大，水面高程预测误差最小
- 与物理模型相比，代理模型产生厘米级误差，可满足实际应用需求

## 8. 优缺点分析（Critical Review）

**优点**:
- 实现了显著的推理加速（300-1400倍），支持实时应用
- 长时间尺度预测（长达一年）表现出良好的稳定性
- 结合气象强迫和边界条件，贴近实际应用场景
- 与现场观测对比验证了方法的实用性
- 系统性地比较了多种降阶方法，提供了全面的基准

**缺点**:
- 训练成本相对较高，需要大量模拟数据进行训练
- 对不同动力机制需要重新训练或调整
- 未开源代码，复现性受限
- 长期预测精度随时间累积可能下降
- 对极端事件（如风暴潮）的预测能力未充分验证

## 9. 对我的启发（For My Research）

1. **数据同化集成**: Koopman自编码器的潜在空间表示为数据同化提供了新的状态初始化方式，可考虑将观测数据直接映射到潜在空间

2. **混合建模策略**: 结合物理约束的代理模型训练方法，可为数据同化中的模型偏差校正提供思路

3. **在线更新框架**: 时域展开技术的稳定性保证机制值得借鉴，可用于同化预报的在线模型更新

4. **不确定性量化**: 该方法的高效推理特性使其适合与集合数据同化方法结合，进行不确定性传播分析

5. **多尺度建模**: 编码器-解码器架构的降维思路可应用于多尺度海洋数据同化系统的构建

## 10. Idea 扩展与下一步（Next Steps）

1. **融入数据同化框架**: 将Koopman自编码器与集合卡尔曼滤波或变分同化方法结合，构建混合数据同化系统，利用代理模型加速背景场更新

2. **时变强迫适应**: 研究如何使Koopman自编码器适应非平稳气象强迫，实现自适应在线学习

3. **多物理场耦合**: 扩展到波浪-潮流-生态耦合模型，提高对海岸生态系统的预测能力

4. **极端事件预测**: 针对风暴潮和海啸等极端事件进行专项训练和评估，提高代理模型在极端条件下的可靠性

5. **实时同化应用**: 部署到高性能计算平台，实现近实时的海洋状态估计和预报

## 11. 引用格式（BibTex）
```bibtex
@article{Petersen2026ReducedOrder,
  title={Reduced-Order Surrogates for Forced Flexible Mesh Coastal-Ocean Models},
  author={Petersen, Freja Høgholm and Mariegaard, Jesper Sandvig and Palmitessa, Rocco and Engsig-Karup, Allan P.},
  journal={arXiv preprint arXiv:2602.05416},
  year={2026},
  eprint={2602.05416},
  archivePrefix={arXiv},
  primaryClass={physics.flu-dyn}
}