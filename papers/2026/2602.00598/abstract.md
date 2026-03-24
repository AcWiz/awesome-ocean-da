---
title: "HybridOM: Hybrid Physics-Based and Data-Driven Global Ocean Modeling with Efficient Spatial Downscaling"
arXiv: "2602.00598"
authors: ["Ruiqi Shu", "Xiaohui Zhong", "Qiusheng Huang", "Ruijian Gou", "Tianrun Gao", "Hao Li", "Xiaomeng Huang"]
year: 2026
source: "arXiv"
venue: "arXiv"
method_tags: ["Hybrid Model", "Physics-Informed Neural Network", "Differentiable Solver", "Ocean Modeling", "Neural Operator"]
application_tags: ["Climate Modeling", "Ocean Forecasting", "Subseasonal-to-Seasonal Prediction", "Downscaling", "Digital Twin"]
difficulty: "★★★★☆"
importance: "★★★★★"
read_status: "skim"
---

# HybridOM: Hybrid Physics-Based and Data-Driven Global Ocean Modeling with Efficient Spatial Downscaling

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2602.00598
- **作者机构**: Ruiqi Shu, Xiaohui Zhong, Qiusheng Huang, Ruijian Gou, Tianrun Gao, Hao Li, Xiaomeng Huang
- **开源代码**: https://github.com/ChiyodaMomo01/HybridOM

## 2. 一句话总结（TL;DR）
HybridOM提出了一种混合物理与数据驱动的全球海洋建模框架，通过将轻量级可微分数值求解器作为物理骨架与神经网络作为次网格尺度动力学校正器相结合，在保持物理一致性的同时实现了高效的推理性能，并引入了基于通量门控的物理信息区域降尺度机制，在GLORYS12V1和OceanBench数据集上验证了其在次季节到季节长期模拟和与FuXi-2.0耦合的运营预报中的卓越表现。

## 3. 研究问题（Problem Definition）
全球海洋模拟是气候科学和海洋生态系统管理的基础，但面临双重挑战：混沌多尺度动力学和昂贵的计算成本。传统数值求解器虽然准确但计算开销巨大，而纯深度学习方法虽然快速但缺乏物理一致性且长期展开时不稳定。特别是在区域降尺度模拟中，从粗分辨率全局模型生成高分辨率边界条件在计算上极其耗时且对边界不一致敏感。如何在保持物理一致性和长期稳定性的同时实现高效的全球海洋建模和区域高分辨率模拟，是本研究的核心问题。

## 4. 核心贡献（Contributions）
1. **全局可微分混合架构**：提出HybridOM框架，将可微分物理核心与多尺度神经网络相结合，通过将深度神经网络直接嵌入数值求解器的时间步进过程中，融合严格的物理定律与深度学习的表达能力，实现了高精度、稳健且物理一致的全球海洋模拟器。
2. **物理信息区域降尺度机制**：引入了基于通量门控的物理信息区域降尺度机制，实现高效的高分辨率建模，在保证物理一致性的前提下进行动态海洋降尺度模拟。
3. **SOTA运营预报系统**：通过将HybridOM与FuXi-2.0天气模型耦合，构建了逼真的全球海洋预报系统，在标准运营协议下验证了其性能，展示了在短期运营预报方面的卓越能力。

## 5. 方法详解（Methodology）
HybridOM的核心架构包含三个关键组件：

**5.1 可微分物理骨架**
- 采用轻量级可微分数值求解器作为基础
- 强制执行物理定律（质量守恒、动量守恒等）
- 提供长期数值稳定性和物理解释性

**5.2 神经网络肌肉校正器**
- 多尺度神经网络用于修正次网格尺度动力学
- 端到端可训练，与物理求解器联合优化
- 学习被简化和参数化的物理过程

**5.3 通量门控区域降尺度**
- 基于通量门控机制的区域高分辨率建模
- 保持边界处的物理一致性
- 实现从粗分辨率到高分辨率的高效转换

整体设计实现了AI方法的推理效率与物理模型的准确性和鲁棒性的统一。

## 6. 数学与物理建模（Math & Physics）
**核心物理约束**：
- 海洋动力学基本方程：Navier-Stokes方程在旋转地球框架下的简化（Primitive Equations）
- 质量守恒：连续性方程
- 动量守恒：水平动量方程
- 能量守恒：热力学方程

**混合建模框架**：
- 物理求解器提供主要动力学演化：∂U/∂t = F_physical(U)
- 神经网络提供次网格修正：U_corrected = U + ΔU_NN
- 端到端可微分设计允许梯度反向传播

**通量门控机制**：
- 在区域边界实施物理约束
- 控制进出区域的通量以保持一致性
- 支持高分辨率局部模拟

## 7. 实验分析（Experiments）
**数据集**: 
- GLORYS12V1（全球海洋再分析数据）
- OceanBench数据集

**评估指标**:
- 均方根误差（RMSE）
- 物理一致性指标
- 长期稳定性
- 预报技能评分

**对比方法**:
- 传统数值模型（如NEMO、MITgcm）
- 纯数据驱动模型（如Pangu-Weather海洋模块、GraphCast海洋模块）
- 简单混合方法

**核心结果**:
- 在次季节到季节（S2S）长期模拟中显著优于基线方法
- 严格保持物理一致性，无质量或动量守恒违反
- 在与FuXi-2.0耦合的运营预报中展现出色的短期预测能力
- 实现了AI推理效率与物理模型准确性的统一
- 为下一代海洋数字孪生提供了稳健解决方案

## 8. 优缺点分析（Critical Review）
**优点**:
- 成功融合物理约束与深度学习的表达能力的混合建模方法
- 可微分设计允许端到端优化，保证物理一致性
- 通量门控机制解决了区域降尺度中的边界不一致问题
- 在长期稳定性和短期预报精度之间取得良好平衡
- 开源代码发布，促进研究复现和进一步发展

**缺点**:
- 论文仅提供部分实现细节，完整的技术细节需要参考补充材料
- 对于极端海洋事件（如台风、厄尔尼诺）的表现未详细评估
- 计算复杂度和训练成本的具体数据未给出
- 在不同海洋区域（如深海与浅海、极地与热带）的泛化能力需进一步验证

## 9. 对我的启发（For My Research）
HybridOM的工作为海洋数据同化研究提供了重要启示：
1. **混合建模范式**：将物理模型与神经网络相结合的思路可直接应用于数据同化框架，如在EnKF、4DVar等经典方法中嵌入学习型修正项
2. **可微分架构**：端到端可微分设计为梯度基数据同化方法提供了新的可能性，可用于优化初始条件和边界条件
3. **通量守恒约束**：基于通量门控的物理一致性保持机制对同化过程中保持物理平衡具有重要参考价值
4. **降尺度同化**：区域高分辨率同化可借鉴其通量门控机制处理粗细分辨率边界条件
5. **多尺度耦合**：多尺度神经网络修正次网格动力学的思想可用于改进对流尺度和涡旋尺度过程的同化

## 10. Idea 扩展与下一步（Next Steps）
1. **数据同化集成**：将HybridOM与集合卡尔曼滤波（EnKF）或四维变分同化（4DVar）框架结合，构建混合数据同化系统，利用神经网络的表达能力修正模型误差同时保持物理约束
2. **多圈层耦合**：扩展框架到海-气-冰耦合系统，借鉴HybridOM的混合建模策略处理界面通量和耦合反馈
3. **在线学习更新**：开发自适应在线学习机制，使模型能够利用实时观测数据持续修正次网格参数化，降低模型偏差
4. **极端事件预测**：针对海洋极端事件（海洋热浪、台风浪、El Niño等）进行专项优化，增强模型在非平稳条件下的预测能力
5. **可解释性增强**：深入分析神经网络学习到的次网格修正物理意义，建立与已知海洋过程的对应关系，提高模型可解释性

## 11. 引用格式（BibTex）
```bibtex
@article{HybridOM2026,
  title={HybridOM: Hybrid Physics-Based and Data-Driven Global Ocean Modeling with Efficient Spatial Downscaling},
  author={Shu, Ruiqi and Zhong, Xiaohui and Huang, Qiusheng and Gou, Ruijian and Gao, Tianrun and Li, Hao and Huang, Xiaomeng},
  year={2026},
  eprint={2602.00598},
  archivePrefix={arXiv},
  primaryClass={physics.flu-dyn},
  journal={arXiv preprint}
}