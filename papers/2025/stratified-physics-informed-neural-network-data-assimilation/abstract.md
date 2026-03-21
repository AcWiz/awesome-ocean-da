---
title: 'Stratified Physics-Informed Neural Network Data Assimilation'
arXiv: '2503.19160'
authors:

year: 2025
source: arXiv
venue: arXiv
domain_tags:
- PINN
ocean_vars: Deep-Ocean, Ocean State
spatiotemporal_res: Unknown
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: skim
---


# Deep learning in the abyss: a stratified Physics Informed Neural Network for data assimilation

## 基本信息
- **arXiv**: [2503.19160](https://arxiv.org/abs/2503.19160)
- **作者**: Vadim Limousin, Nelly Pustelnik, Bruno Deremble, Antoine Venaille
- **年份**: 2025

## 中文总结
**核心贡献**：提出 StrAssPINN（分层 assimilation PINNs）方法，用于深海海洋流重建，解决海洋内部数据稀缺导致的传统数据同化难题。

**主要方法**：采用物理信息神经网络（PINN），为海洋模型的每一层分配独立网络，通过 SIREN 架构（正弦激活函数的多层感知机）结合观测数据和动力学先验进行训练。

**意义**：证明了 PINN 可作为深海海洋流重建的有效替代方案，成功重建了涡旋环、东向射流和 Rossby 波等中尺度特征，为将 StrAssPINN 应用于真实观测数据奠定基础。

## 关键词
- Physics Informed Neural Network, Deep Ocean Reconstruction, Data Assimilation, Stratified Ocean Model, SIREN, Sea Surface Height, SWOT, ARGO Floats
