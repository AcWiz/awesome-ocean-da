---
title: "Optimizing AUV speed dynamics with a data-driven Koopman operator approach"
arXiv: "2503.09628"
authors: ["Zhiliang Liu", "Xin Zhao", "Peng Cai", "Bing Cong"]
year: 2025
source: "arXiv"
venue: "arXiv"
method_tags: ["Koopman Operator", "Model Predictive Control", "Dynamic Mode Decomposition", "Data-Driven Control"]
application_tags: ["AUV Speed Control", "Underwater Robotics", "Nonlinear Systems", "Constraint Handling"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# Optimizing AUV speed dynamics with a data-driven Koopman operator approach

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2503.09628
- **作者机构**: Zhiliang Liu, Xin Zhao, Peng Cai, Bing Cong（具体机构信息未在摘要中提供）
- **开源代码**: 未在内容样本中发现GitHub链接或代码仓库信息

## 2. 一句话总结（TL;DR）
本文提出了一种基于数据驱动Koopman算子理论与模型预测控制（MPC）相结合的AUV速度控制系统，该方法通过将非线性系统状态空间提升至高维空间实现线性化表示，在保证系统性能的同时有效处理状态约束、输入约束以及增量输入约束，并在ROS2和Gazebo平台上进行了仿真验证。

## 3. 研究问题（Problem Definition）
**核心问题**：AUV速度控制系统的设计与优化面临多重挑战：
1. **非线性动力学特性**：螺旋桨转速与航速之间存在高度非线性关系，传统线性化方法难以准确捕获系统动态特性
2. **多约束条件**：包括状态限制、输入约束以及增量输入约束，约束违反可能导致设备损坏
3. **建模困难**：精确的解析模型难以获得，限制了非线性控制方法在实际工程中的应用

**研究意义**：AUV在现代海洋探测中扮演关键角色，可执行水下测量、地形测绘、水文地质数据采集及军事应用等任务，其速度控制系统的性能直接影响任务执行效率与航行安全。

## 4. 核心贡献（Contributions）
1. **创新性方法融合**：提出将数据驱动的Koopman算子理论与MPC相结合的AUV速度控制系统，充分利用Koopman方法增强的建模精度和MPC的预测与约束处理能力
2. **完整约束处理框架**：系统性地考虑状态约束、输入约束以及增量输入约束，防止螺旋桨转速的快速变化对航行器造成潜在损害
3. **仿真验证平台**：开发了基于ROS2和Gazebo的仿真验证平台，为水下航行器的控制策略研究提供了新的测试环境

## 5. 方法详解（Methodology）

### 5.1 Koopman算子理论
Koopman算子理论提供了一种独特的非线性系统处理方法，其核心思想是将原始状态空间提升到更高维的空间，在该空间中实现线性表示：
- **核心原理**：通过定义观测函数，将非线性系统的演化过程映射到线性算子的作用
- **优势对比**：与传统的泰勒线性化方法不同，Koopman方法能够保持全局动力学特性

### 5.2 动态模态分解（DMD）
作为数据驱动的动力学系统分析方法，DMD系列方法用于近似Koopman算子：
- **原始DMD**：主要针对线性系统
- **扩展DMD（EDMD）**：通过引入非线性观测函数扩展到非线性系统
- **高阶DMD**：进一步增强对复杂动态的捕捉能力

### 5.3 模型预测控制（MPC）
MPC框架通过有限时域内的优化问题实现约束处理与预测控制：
- **滚动优化**：在每个控制时刻求解有限时域优化问题
- **约束处理**：自然地处理各种状态和输入约束
- **预测能力**：提前考虑未来状态变化并调整控制动作

### 5.4 系统架构
```
[AUV非线性系统] → [数据采集] → [EDMD/Koopman近似] → [线性化模型]
                                                              ↓
                                                    [MPC控制器设计]
                                                              ↓
                                                    [最优控制输入]
                                                              ↓
                                                    [AUV执行器控制]
```

## 6. 数学与物理建模（Math & Physics）

### 6.1 AUV六自由度运动方程
AUV的6-DOF运动方程可分解为三个相对独立的子系统：
- **速度控制子系统**：控制螺旋桨转速以调节航行器速度
- **纵向动力学子系统**：包含纵荡、垂荡和俯仰
- **侧向动力学子系统**：包含横荡、横滚和偏航

### 6.2 螺旋桨动力学建模
- **非线性关系**：螺旋桨转速与推力/速度之间存在非线性函数关系
- **环境因素**：考虑周围流速、水流角度等环境因素的影响
- **建模方法**：可采用最小二乘回归、实验数据拟合等方法进行参数优化

### 6.3 Koopman算子定义
对于离散动力学系统 $x_{k+1} = F(x_k)$，Koopman算子 $\mathcal{K}$ 作用于观测函数 $g$：
$$\mathcal{K}g(x) = g(F(x))$$

通过EDMD方法近似Koopman算子得到线性矩阵表示：
$$\hat{K} = \Phi^T \Phi^{-1} \Psi^T \Psi / N$$

其中 $\Phi$ 和 $\Psi$ 分别为当前状态和下一状态的特征矩阵。

### 6.4 MPC优化问题
$$\min_{u} \sum_{i=1}^{N_p} ||r(k+i|k) - y(k+i|k)||_Q^2 + \sum_{i=0}^{N_c-1} ||u(k+i|k)||_R^2$$

约束条件：
- $x_{min} \leq x \leq x_{max}$（状态约束）
- $u_{min} \leq u \leq u_{max}$（输入约束）
- $\Delta u_{min} \leq \Delta u \leq \Delta u_{max}$（增量输入约束）

## 7. 实验分析（Experiments）

**数据集**: 
- 基于仿真环境的AUV运动数据
- 螺旋桨推力特性实验数据（参考Yoerger et al., Healey et al.等研究）

**评估指标**:
- 速度跟踪精度
- 约束满足度
- 控制响应速度
- 鲁棒性

**对比方法**:
- 传统线性MPC控制
- 滑模控制
- PID控制
- 增益调度控制

**核心结果**:
根据摘要所述，所提出的Koopman-MPC方法在ROS2和Gazebo平台上验证了有效性，能够在复杂动态水下环境中实现良好的AUV控制性能，同时满足多约束条件。

## 8. 优缺点分析（Critical Review）

**优点**:
- **数据驱动建模**：无需精确的解析模型，通过数据驱动方式学习系统动态，降低了建模复杂度
- **全局线性化**：Koopman方法提供全局意义上的线性表示，避免了局部线性化的近似误差
- **约束处理能力强**：MPC框架天然支持多种约束的显式处理
- **增量约束保护**：考虑增量输入约束，有效防止控制输入的剧烈变化

**缺点**:
- **计算复杂度**：高维提升空间可能导致计算负担增加
- **观测函数选择**：EDMD的性能高度依赖观测函数的选择，需要领域知识或经验
- **仿真验证局限**：目前仅在仿真平台验证，真实水下环境的验证有待进行
- **泛化能力**：对训练数据范围外的工况适用性可能受限

## 9. 对我的启发（For My Research）

对于海洋数据同化研究，本文提供以下启示：

1. **Koopman算子在海洋模型中的应用潜力**：海洋系统同样具有强非线性特性，Koopman方法可能为海洋动力学的降维建模提供新思路

2. **数据驱动与物理约束的结合**：论文展示了如何将数据驱动方法与物理约束相结合，在海洋数据同化中也可以考虑类似的混合建模策略

3. **MPC在海洋预测控制中的应用**：MPC的预测能力和约束处理能力可应用于海洋环境预测、海洋灾害预警等场景

4. **ROS2/Gazebo仿真环境**：为海洋机器人系统的仿真测试提供了技术参考

## 10. Idea 扩展与下一步（Next Steps）

1. **扩展到海洋状态估计**：将Koopman算子方法与海洋数据同化技术（如EnKF、4DVAR）结合，发展海洋状态估计的新方法

2. **多AUV协同控制**：基于速度控制的研究成果，探索多AUV编队协同控制中的Koopman方法应用

3. **考虑洋流影响的建模**：在现有模型基础上引入时变洋流的影响，增强模型在真实海洋环境中的适应性

4. **硬件在环验证**：从仿真平台扩展到实际AUV硬件验证，评估方法在实际部署中的性能

5. **与其他深度学习方法结合**：探索将神经网络与Koopman算子结合，进一步提升非线性系统的建模精度

## 11. 引用格式（BibTex）
```bibtex
@article{liu2025optimizing,
  title={Optimizing AUV speed dynamics with a data-driven Koopman operator approach},
  author={Liu, Zhiliang and Zhao, Xin and Cai, Peng and Cong, Bing},
  year={2025},
  eprint={2503.09628},
  archiveprefix={arXiv},
  primaryclass={eess.SY},
  venue={arXiv preprint}
}
```