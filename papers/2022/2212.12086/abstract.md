---
title: "Eigenvalue Initialisation and Regularisation for Koopman Autoencoders"
arXiv: "2212.12086"
authors: ["Jack W. Miller", "Charles O'Neill", "Navid C. Constantinou", "Omri Azencot"]
year: 2022
source: "arXiv"
venue: "arXiv"
method_tags: ["Koopman Autoencoder", "Eigenvalue", "Initialisation", "Regularisation", "Deep Learning"]
application_tags: ["Dynamical Systems", "Ocean SST", "Cyclone", "Pendulum", "Cylinder Flow"]
difficulty: "★★★★☆"
importance: "★★★☆☆"
read_status: "skim"
---

# 📑 Eigenvalue Initialisation and Regularisation for Koopman Autoencoders

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2212.12086
- **作者机构**: Australian National University (Research School of Earth Sciences), Ben-Gurion University (Computer Science)
- **开源代码**: None

## 🧠 2. 一句话总结（TL;DR）
为 Koopman 自编码器提出特征初始化（eigeninit）和特征损失（eigenloss）正则化方案，通过控制 Koopman 算子特征值分布提升收敛速度和长期预测精度。

## 🎯 3. 研究问题（Problem Definition）
Koopman 自编码器用于物理相关动力系统，但大多数现有工作使用标准正则化实践。通用初始化和惩罚方案可能不适用于 Koopman 算子的特殊结构。

## 🚀 4. 核心贡献（Contributions）
- 提出 eigeninit：基于特征值分布采样初始化 Koopman 算子
- 提出 eigenloss：惩罚 Koopman 算子特征值偏离单位圆
- 收敛速度提升最高 5 倍
- 长期预测误差降低最高 3 倍
- spike-and-slab 分布自然匹配系统特性

## 🏗️ 5. 方法详解（Methodology）
1. **eigeninit**：
   - 采样 Koopman 矩阵 U₀
   - 特征分解：U₀ = VΛV⁻¹
   - 调整特征值模：r → r̃ ~ spikeAndSlab
   - 重构：Ũ = VΛ̃V⁻¹

2. **eigenloss**：
   - 惩罚项：L_λ = Σⱼ|| |λⱼ| - 1 ||²
   - 鼓励特征值接近单位圆

3. **spike-and-slab 分布**：
   - D = θ·U(0,1) + (1-θ)·δ(1)

## 📐 6. 数学与物理建模（Math & Physics）
- Koopman 算子：Kf(x) = f(φ(x))
- Koopman 自编码器：编码器 φ，Koopman 层 U，解码器 ψ
- 特征值意义：
  - |λ| < 1：耗散，渐近消失
  - |λ| > 1：爆炸
  - |λ| = 1：稳定

## 📊 7. 实验分析（Experiments）
- **数据集**：Pendulum, Cylinder Flow, Ocean SST, Cyclone Wind
- **评估**：验证损失、累积测试误差、收敛速度
- **结果**：
  - Ocean SST：累积误差降低 3 倍
  - Cyclone：收敛速度提升 5 倍
  - 所有数据集性能提升

## 🔍 8. 优缺点分析（Critical Review）
**优点**：
- 收敛速度显著提升
- 长期预测改善
- 物理可解释性强

**缺点**：
- 需要调参 θ
- 计算特征分解开销
- 主要在合成数据验证

## 💡 9. 对我的启发（For My Research）
- Koopman 方法用于海洋动力系统
- 特征值约束的物理意义
- 初始化策略对深度学习的重要性
- 结合物理先验的正则化

## 🔮 10. Idea 扩展与下一步（Next Steps）
- 更复杂动力系统
- 输入驱动系统扩展
- 自动 θ 选择
- 与其他 Koopman 方法结合

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{miller2022eigenvalue,
  title={Eigenvalue Initialisation and Regularisation for Koopman Autoencoders},
  author={Miller, Jack W. and O'Neill, Charles and Constantinou, Navid C. and Azencot, Omri},
  year={2022},
  eprint={2212.12086},
  archivePrefix={arXiv}
}
```
