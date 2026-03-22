---
title: "FEM-PIKFNNs for Underwater Acoustic Propagation Induced by Structural Vibrations in Different Ocean Environments"
arXiv: "2308.09956"
authors: ["Qiang Xi", "Zhuojia Fu", "Wenzhi Xu", "Mi-An Xue", "Jinhai Zheng"]
year: 2023
source: "arXiv"
venue: "arXiv"
method_tags: ["FEM", "PIKFNN", "Physics-Informed_Neural_Network", "Kernel_Function", "Finite_Element_Method"]
application_tags: ["Underwater_Acoustic_Propagation", "Structural_Vibration", "Ocean_Acoustics", "Unbounded_Ocean", "Deep_Ocean", "Shallow_Ocean"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "deep_read"
---

# 📑 FEM-PIKFNNs for Underwater Acoustic Propagation Induced by Structural Vibrations in Different Ocean Environments

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2308.09956
- **作者机构**: 河海大学（ Hohai University），南京，中国
- **开源代码**: None

## 🧠 2. 一句话总结（TL;DR）

本文提出了一种基于有限元方法（FEM）和物理信息核函数神经网络（PIKFNNs）的混合方法，用于预测无限深海、深海和浅海中由结构振动引起的水下声传播。

## 🎯 3. 研究问题（Problem Definition）

传统有限元方法在模拟无限域海洋声传播时面临计算瓶颈——计算成本随域大小迅速增加。本文探索如何结合FEM和物理信息核函数神经网络的优点，实现高效准确的水下声传播预测，同时满足Sommerfeld辐射条件和海洋环境中的反射边界条件。

## 🚀 4. 核心贡献（Contributions）

1. 提出FEM-PIKFNNs混合方法，结合有限元法和物理信息核函数神经网络
2. PIKFNNs用物理信息核函数（PIKFs）替代传统激活函数，将先验物理信息嵌入神经网络
3. 无需将控制方程显式嵌入损失函数，只需边界数据训练
4. 验证了在无限深海、深海和浅海三种海洋环境中的准确性和可行性

## 🏗️ 5. 方法详解（Methodology）

**混合方法框架**：
- FEM计算近场水下声压作为训练数据
- PIKFNNs学习从近场到远场的声传播映射

**物理信息核函数（PIKFs）**：
- 无限深海Green函数：$\Psi^{(1)} = \frac{e^{ikR_a}}{R_a}$
- 深海反射修正：$\Psi^{(2)} = \frac{e^{ikR_a}}{R_a} - \frac{e^{ikR_b}}{R_b}$
- 浅海多层反射：$\Psi^{(3)} = \sum_{i=1}^{\infty} \chi_i \frac{e^{ikR_i}}{R_i}$

**PIKFNNs结构**：
- 全连接神经网络：输入层、隐藏层、输出层
- PIKFs作为神经元函数替代传统激活函数
- Levenberg-Marquardt优化算法

## 📐 6. 数学与物理建模（Math & Physics）

**声压控制方程**：
$$\Delta p + k^2 p = 0$$

**结构振动方程**：
$$(K_a - \omega^2 M_a + i\omega C_a) u = F_a$$

**结构-声耦合矩阵**：
$$\begin{bmatrix} K_a - \omega^2 M_a + i\omega C_a & -K_{ac} \\ M_{bc} & K_b - \omega^2 M_b + i\omega C_b \end{bmatrix} \begin{bmatrix} u \\ p \end{bmatrix} = \begin{bmatrix} F_a \\ F_b \end{bmatrix}$$

**Sommerfeld辐射条件**：确保无限远处声波衰减到零

## 📊 7. 实验分析（Experiments）

**示例1 - 无限深海**：
- 球形结构振动，无限海洋环境
- 振动频率：1000-6000 Hz
- PIKF函数：$\Psi^{(1)}$
- 相对误差：$L_2 < 3.61 \times 10^{-5}$
- 结论：与解析解高度吻合

**示例2 - 深海**：
- 带肋圆柱壳振动
- 振动频率：50-1000 Hz
- PIKF函数：$\Psi^{(2)}$（考虑海面反射）
- 结果与COMSOL Multiphysics FEA软件一致

**示例3 - 浅海**：
- 胶囊壳振动
- 海洋深度：20m
- 沉积层声反射系数考虑
- 结果与COMSOL高度吻合

## 🔍 8. 优缺点分析（Critical Review）

**优点**：
1. PIKFs天然满足控制方程和辐射条件
2. 无需显式嵌入控制方程到损失函数
3. 只需边界/近场数据训练，大幅减少训练数据量
4. 单隐藏层网络即可达到高精度

**缺点**：
1. 依赖于Green函数的解析形式
2. 对于复杂几何形状，PIKFs构建困难
3. 训练数据来自FEM，存在固有误差
4. 未考虑非线性效应和多物理场耦合

## 💡 9. 对我的启发（For My Research）

1. **物理信息嵌入方式**：PIKFs将物理约束嵌入激活函数，而非损失函数，可能更适合我的数据同化研究
2. **Green函数方法**：利用Green函数满足辐射条件的特性
3. **耦合方法思路**：结合传统数值方法和神经网络的优势

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **推广到三维问题**：当前方法主要针对二维场景
2. **时变声传播**：从频域扩展到时域分析
3. **多物理场耦合**：考虑温度、盐度变化对声速的影响
4. **数据驱动PIKFs**：当解析Green函数不可用时，用神经网络学习核函数

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{xi2023fempikfnn,
  title={FEM-PIKFNNs for Underwater Acoustic Propagation Induced by Structural Vibrations in Different Ocean Environments},
  author={Xi, Qiang and Fu, Zhuojia and Xu, Wenzhi and Xue, Mi-An and Zheng, Jinhai},
  year={2023},
  eprint={2308.09956},
  eprinttype={arxiv},
  eprintclass={cs.LG},
}
```
