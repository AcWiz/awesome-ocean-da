---
title: "Generalizable neural-network parameterization of mesoscale eddies in idealized and global ocean models"
arXiv: "2505.08900"
authors: ["Pavel Perezhogin", "Alistair Adcroft", "Laure Zanna"]
year: 2025
source: "arXiv"
venue: "arXiv"
method_tags: ["Neural Network Parameterization", "Mesoscale Eddies", "Ocean Modeling", "Dimensional Analysis"]
application_tags: ["Ocean Modeling", "Climate Modeling", "Eddy Parameterization", "Subgrid-scale Modeling"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# Generalizable neural-network parameterization of mesoscale eddies in idealized and global ocean models

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2505.08900
- **作者**: Pavel Perezhogin, Alistair Adcroft, Laure Zanna
- **开源代码**: None

## 2. 一句话总结（TL;DR）
本文通过在神经网络参数化中强制物理约束，解决中尺度涡旋参数化的泛化问题，实现了对未见过的网格分辨率和深度的迁移。

## 3. 研究问题（Problem Definition）
**核心问题**：数据驱动的中尺度涡旋参数化方法在泛化任务中表现不佳，且在网格分辨率或海洋配置变化时可能需要重新调优。

**研究背景**：
- 中尺度涡旋对海洋环流有重要影响
- 参数化是海洋模型的关键组成部分
- 传统参数化方法依赖经验假设

**关键挑战**：
1. 跨不同网格分辨率的泛化能力
2. 跨不同深度层的迁移
3. 无需重新调优的适应性

## 4. 核心贡献（Contributions）
1. **物理约束神经网络**：对中尺度涡旋通量进行带物理约束的神经网络参数化
2. **局部缩放机制**：通过输入输出特征的局部缩放帮助泛化
3. **量纲分析**：基于量纲分析纳入网格间距作为长度尺度
4. **通用算法**：将发现表述为可强制数据驱动参数化量纲缩放的通用算法

## 5. 方法详解（Methodology）

### 5.1 神经网络参数化
- 学习中尺度涡旋通量的表示
- 输入：海洋状态变量
- 输出：涡旋效应参数化

### 5.2 物理约束
- 局部缩放输入输出特征
- 基于量纲分析设计
- 纳入网格间距作为长度尺度

### 5.3 泛化机制
- 在未见过的网格分辨率上离线测试
- 在不同深度层上验证
- 与基线参数化方法对比

## 6. 实验分析（Experiments）

**数据集**：
- 理想化海洋模型
- 全球海洋模型

**评估指标**：
- 动能和势能的表示
- 在线模拟中的性能

**结果**：
- 新参数化改进了动能和势能在在线模拟中的表示
- 展示了跨分辨率和跨深度的泛化能力
