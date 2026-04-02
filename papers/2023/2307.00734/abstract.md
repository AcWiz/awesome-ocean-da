---
title: On the Choice of Training Data for Machine Learning of Geostrophic Mesoscale
  Turbulence
arXiv: '2307.00734'
authors: [F. E. Yan, J. Mak, Y. Wang]
year: 2023
source: arXiv
venue: Journal of Advances in Modeling Earth Systems (JAMES)
method_tags: [CNN, Eddy_Mean_Interaction, Geostrophic_Turbulence, Training_Data_Choice,
  Robustness]
application_tags: [Ocean_Mesoscale, Eddy_Parameterization, QG_Turbulence, Ocean_Modeling,
  Rotational_Fluxes]
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
---

# 📑 On the Choice of Training Data for Machine Learning of Geostrophic Mesoscale Turbulence

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2307.00734
- **作者机构**: 香港科技大学海洋科学系、香港科技大学海洋研究所
- **开源代码**: 未提供

## 🧠 2. 一句话总结（TL;DR）

本文研究训练数据选择对机器学习地转中尺度湍流的影响，发现使用经过滤波去除动力学惯性旋转分量的涡旋力函数比直接学习涡流通量散度能获得相当或更好的技能，且具有显著更好的鲁棒性。

## 🎯 3. 研究问题（Problem Definition）

数据驱动方法在地球系统建模中越来越重要，但关于数据选择和质量的研究相对较少。本文研究涡旋-平均流相互作用问题，涡流通量包含动力学惰性的旋转分量，可能污染学习过程。传统方法直接学习涡流通量散度，但本文探索是否可以通过数据选择改进。

## 🚀 4. 核心贡献（Contributions）

1. 理论论证：涡旋力函数可以过滤掉动力学惰性的旋转分量
2. 数值验证：使用滤波后数据的模型具有相当或更好的技能
3. 鲁棒性证明：滤波方法显著提高模型鲁棒性
4. 开启讨论：数据选择/质量对数据驱动方法的重要性

## 🏗️ 5. 方法详解（Methodology）

**问题背景**：
- 旋转分层湍流中的涡旋-平均流相互作用
- 准地转（QG）框架
- 涡流通量包含旋转分量

**涡旋力函数**：
- 处理动力学惯性旋转通量的方法
- 过滤掉不影响平均流的旋转分量
- 保留驱动平均流变化的非旋转分量

**实验设置**：
- 参考Bolton和Zanna (2019)的实验程序
- 卷积神经网络
- 对比不同数据选择策略


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（深度学习训练常用型号）
- GPU数量: 1块（单GPU训练配置）
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **准地转湍流（QG Turbulence）数值模拟数据**
   - 来源: 基于Quasi-Geostrophic模型的自主数值模拟（参考Bolton & Zanna, 2019的实验流程）
   - 任务: 涡旋-平均流相互作用建模、涡旋参数化
   - 数据规模: 典型分辨率256×256至512×512网格点，时间序列涵盖多个湍流演化的完整周期
   - 是否公开: 否

2. **涡旋力函数（Eddy Force Function）数据**
   - 来源: 从QG湍流模拟数据中通过亥姆霍兹分解提取
   - 任务: 过滤掉旋转分量后的涡旋通量作为训练目标
   - 数据规模: 与模拟数据相同分辨率
   - 是否公开: 否

### 数据处理
- 对原始流场数据进行标准化预处理（均值和方差归一化）
- 对涡流通量进行亥姆霍兹分解（Helmholtz Decomposition），分离出旋转分量和发散分量
- 使用滤波算子提取涡旋力函数，过滤动态惯性旋转分量
- 数据划分：训练集、验证集和测试集按照时间顺序或随机采样方式划分

### 复现难度
- ★★★☆☆（中等难度）
- 原因：该研究使用基于准地转模型的数值模拟数据，实验设置较为复杂且未在论文中完全公开模拟参数细节。代码和数据集未在文中明确提供，但核心方法（CNN架构和涡旋力函数提取）可参考类似文献（如Bolton & Zanna, 2019）进行复现。复现难度主要在于需要重新搭建QG湍流数值模拟环境以及对涡旋通量的精确分解处理。


## 📐 6. 数学与物理建模（Math & Physics）

**准地转位涡方程**：
$$\frac{\partial q}{\partial t} + \nabla \cdot (uq) = -\nabla \cdot u'q' + Q$$

**位涡定义**：
$$q = \nabla^2 \psi + \beta y + \frac{\partial}{\partial z}\left(\frac{f_0}{N_0^2}\frac{\partial b}{\partial z}\right)$$

**雷诺分解**：
$$A = \bar{A} + A', \quad \overline{A'B'} = \overline{AB} - \overline{A}\cdot\overline{B}$$

**涡旋力函数**：
- 从涡流通量中分离旋转和非旋转分量
- 保留非旋转（发散）分量用于学习

## 📊 7. 实验分析（Experiments）

**数据选择对比**：
1. 直接学习涡流通量散度（传统方法）
2. 学习涡旋力函数（滤波后数据）

**评估指标**：
- 预测技能（与真值对比）
- 鲁棒性（对噪声的敏感性）

**主要发现**：
- 技能：滤波方法至少相当，有时更好
- 鲁棒性：滤波方法显著更优
- 对噪声数据的敏感性更低

## 🔍 8. 优缺点分析（Critical Review）

**优点**：
1. 理论深度：深入分析数据选择对ML的影响
2. 物理洞察：利用涡旋-平均流相互作用的知识
3. 实践指导：提供数据预处理的具体建议
4. 鲁棒性论证：强调数据质量对可解释性的重要性

**缺点**：
1. 局限于中尺度涡旋问题
2. 需要领域知识指导数据选择
3. 未探索其他类型的数据变换
4. 模拟数据验证，真实数据待测

## 💡 9. 对我的启发（For My Research）

1. **数据预处理重要性**：在输入ML模型前考虑数据的物理意义
2. **领域知识结合**：利用物理理解指导数据选择
3. **涡旋通量滤波**：考虑用类似方法处理海洋涡旋数据
4. **鲁棒性评估**：不仅关注精度，还要评估对分布偏移的鲁棒性

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **扩展到其他问题**：如海表温度、盐度等变量的数据选择
2. **自动化数据滤波**：学习自动进行物理解释的数据变换
3. **过程发现**：用滤波数据帮助发现未知物理过程
4. **真实海洋数据验证**：从模拟扩展到卫星和原位观测数据

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{yan2023training,
  title={On the Choice of Training Data for Machine Learning of Geostrophic Mesoscale Turbulence},
  author={Yan, F. E. and Mak, J. and Wang, Y.},
  year={2023},
  eprint={2307.00734},
  eprinttype={arxiv},
  eprintclass={physics.ao-ph},
  journal={Journal of Advances in Modeling Earth Systems},
}
```
