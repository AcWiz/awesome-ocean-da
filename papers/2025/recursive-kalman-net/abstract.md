---
title: Recursive Kalman Net
authors: []
year: 2025
source: other
method_tags:
- EnKF
- Deep-Learning
application_tags:
- Ocean-DA
date_collected: '2026-03-21'
---

# Recursive KalmanNet: Deep Learning-Augmented Kalman Filtering for State Estimation with Consistent Uncertainty Quantification

## 基本信息
- **arXiv**: [2506.11639](https://arxiv.org/abs/2506.11639)
- **作者**: Hassan Mortada, Cyril Falcon, Yanis Kahil, Mathéo Clavaud, Jean-Philippe Michel
- **年份**: 2025

## 中文总结
**核心贡献**：提出Recursive KalmanNet，一种结合卡尔曼滤波器的循环神经网络，用于精确状态估计和一致的误差协方差量化。

**主要方法**：
- 使用递归Joseph公式传播误差协方差
- 优化高斯负对数似然
- 在非高斯测量白噪声环境下进行实验验证

**意义**：为海洋动力系统、气象预报等领域的状态估计提供新的深度学习增强方案，相比传统卡尔曼滤波器和现有深度学习方法表现更优。

## 关键词
- 深度学习, 卡尔曼滤波, 状态估计, 循环神经网络, 不确定性量化, 数据同化
