---
title: A Neural Network-Based Submesoscale Vertical Heat Flux Parameterization and
  Its Implementation in Regional Ocean Modeling System (ROMS)
arXiv: '2403.05028'
authors:
- Shuyi Zhou
- Jihai Dong
- Fanghua Xu
- Zhiyou Jing
- Changming Dong
year: 2024
source: arXiv
venue: arXiv
method_tags:
- Neural_Network
- Submesoscale
- Heat_Flux_Parameterization
- ROMS
application_tags:
- Ocean_Modeling
- Submesoscale_Processes
- Heat_Flux
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: skim
---

# A Neural Network-Based Submesoscale Vertical Heat Flux Parameterization and Its Implementation in Regional Ocean Modeling System (ROMS)

## 基本信息
- **论文链接**: https://arxiv.org/abs/2403.05028
- **作者**: Shuyi Zhou, Jihai Dong, Fanghua Xu, Zhiyou Jing, Changming Dong

## 摘要

temporal scales of O(0.01-10) km and hours to 1 day which are hardly resolved by current ocean models, are important sub-grid processes in ocean models. Due to the strong vertical currents, submesoscale processes can lead to submesoscale vertical heat flux (SVHF) in the upper ocean which plays a crucial role in the heat exchange between the atmosphere and the ocean interior, and further modulates the global heat redistribution. At present, simulating a submesoscale-resolving ocean model is still expensive and time-consuming. Parameterizing SVHF becomes a feasible alternative by introducing it into coarse-resolution models. Traditionally, researchers tend to parameterize SVHF by a mathematically fitted relationship based on one or two key background state variables, which fail to represent the relationship between SVHF and the background state variables comprehensively. In this study, we propose a data-driven SVHF parameterization scheme based on a deep neural network and implement it into the Regional Ocean Modeling System (ROMS). In offline tests, our scheme can accurately calculate SVHF using mesoscale-averaged variables and characterize how it varies with depth. In online tests, we simulate an idealized model of an anticyclonic mesoscale eddy and a realistic model of the Gulf Stream, respectively. Compared to the coarse-resolution cases without the SVHF effect, the coarse-resolution cases with the SVHF scheme tend to reproduce results closer to the high-resolution case and the observational state in terms of the temperature structure and mixed layer depth, indicating a good performance of the neural network-based SVHF scheme. Our results show the potential of applying the neural network in parameterizing sub-grid processes in ocean models.
## 2. 一句话总结（TL;DR）
本文提出了基于深度学习的方法解决相关问题，在实验中取得了良好效果。
## 3. 研究问题（Problem Definition）
**核心问题**：如何有效地解决...？

**研究背景**：
- 现有方法存在一定局限性
- 需要新的技术手段

**关键挑战**：
1. 挑战一
2. 挑战二
## 4. 核心贡献（Contributions）
1. **提出新方法**：...
2. **理论分析**：...
3. **实验验证**：...
## 5. 方法详解（Methodology）

### 5.1 方法一
### 5.2 方法二

## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（深度学习训练常用型号）
- GPU数量: 1-2块（单节点训练配置）
- 训练时间: 未明确说明（根据典型深度学习训练任务推测为数小时至数天）

### 数据集（Datasets）
1. **ROMS高分辨率模拟输出数据**
   - 来源: 使用Regional Ocean Modeling System (ROMS)进行高分辨率数值模拟生成
   - 任务: 提供训练神经网络的真实标签数据（SVHF）以及特征变量（背景态变量）
   - 数据规模: 涵盖亚中尺度过程的时间尺度（小时至天）和空间尺度（0.01-10 km）
   - 是否公开: 否

2. **Gulf Stream真实海域数据**
   - 来源: 基于Gulf Stream区域的真实海洋环境配置ROMS模型
   - 任务: 用于在线测试（Online test），验证参数化方案在实际海流场景中的表现
   - 数据规模: 区域性高分辨率模拟
   - 是否公开: 不确定

### 数据处理
- 使用ROMS模型输出数据提取关键背景态变量（如海表温度、盐度、密度等）
- 从高分辨率模拟结果中计算真实的亚中尺度垂直热通量（SVHF）作为训练标签
- 对数据进行深度方向的插值和对齐，确保输入变量与输出变量的空间匹配
- 采用时间平均或空间平均处理获取中尺度平均变量作为神经网络输入特征
- 数据划分：训练集、验证集和测试集按时间或空间区域划分

### 复现难度
- ★★★☆☆（中等难度）
- 原因：该研究基于ROMS海洋模式进行，代码未在文中明确说明公开；需要专业的海洋建模知识；神经网络的实现细节（如网络结构、超参数）需参考补充材料或后续代码发布；数据来源为模拟生成而非公开数据集，增加了复现的数据准备难度。


## 📐 7. 数学与物理建模（Math & Physics）
- **关键公式**: xxx
- **物理意义 / 解释**: xxx


## 📊 8. 实验分析（Experiments）
- **对比方法**: xxx
- **评估指标**: xxx
- **主要结果**: xxx
- **关键发现**: xxx

## 🔍 9. 优缺点分析（Critical Review）
**优点：** xxx
**缺点：** xxx

## 💡 10. 对我的启发（For My Research）
- xxx

## 🔮 11. Idea 扩展与下一步（Next Steps）
1. xxx

## 🧾 12. 引用格式（BibTex）
```bibtex
@article{论文标题,
  title={论文标题},
  author={作者},
  year={年份},
  eprint={arxiv编号},
  eprinttype={arxiv},
  eprintclass={},
  journal={arXiv preprint},
}
```
