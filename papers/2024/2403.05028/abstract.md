---
title: "A Neural Network-Based Submesoscale Vertical Heat Flux Parameterization and Its Implementation in Regional Ocean Modeling System (ROMS)"
arXiv: "2403.05028"
authors: ['Shuyi Zhou', 'Jihai Dong', 'Fanghua Xu', 'Zhiyou Jing', 'Changming Dong']
year: 2024
source: "arXiv"
venue: "arXiv"
method_tags: ["Neural Network", "Submesoscale", "Heat Flux Parameterization", "ROMS"]
application_tags: ["Ocean Modeling", "Submesoscale Processes", "Heat Flux"]
difficulty: "★★★☆☆"
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