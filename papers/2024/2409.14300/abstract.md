---
title: 'Conditional Gaussian Ensemble Kalman Filtering'
arXiv: '2409.14300'
authors:

year: 2024
source: arXiv
venue: arXiv
domain_tags:
- EnKF
ocean_vars: Ocean State
spatiotemporal_res: Unknown
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: skim
---


# A competitive baseline for deep learning enhanced data assimilation using conditional Gaussian ensemble Kalman filtering

## 基本信息
- **arXiv**: [2409.14300](https://arxiv.org/abs/2409.14300)
- **作者**: Zachariah Malik, Romit Maulik
- **年份**: 2024

## 中文总结
**核心贡献**：提出条件高斯 EnKF（CG-EnKF）和正态得分 EnKF（NS-EnKF）方法，解决传统 EnKF 在非线性扰动下的不适用问题。

**主要方法**：通过条件高斯更新公式构建 Kalman 增益矩阵，替代传统线性假设。在 Lorenz-96 系统上与基于深度学习的 score filter 进行对比。

**意义**：证明 CG-EnKF 和 NS-EnKF 在高维多尺度数据同化任务中显著优于 score filter，并能处理高度非高斯加性噪声扰动。

## 关键词
- Ensemble Kalman Filter, Data Assimilation, Conditional Gaussian, Deep Learning, Lorenz-96, Nonlinear Perturbations, Particle Filter
