---
title: 'OceanCastNet: Wave Forecasting Network'
arXiv: '2406.03848'
authors:

year: 2024
source: arXiv
venue: arXiv
domain_tags:
- Deep-Learning
- GNN
ocean_vars: Ocean Waves
spatiotemporal_res: Unknown
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: skim
---


# OceanCastNet: Ocean Wave Forecasting with Deep Learning

## 基本信息
- **arXiv**: [2406.03848](https://arxiv.org/abs/2406.03848)
- **作者**: Ziliang Zhang, Huaming Yu, Danqin Ren, Chenyu Zhang, Minghua Sun, Xin Qi
- **年份**: 2024

## 中文总结
**核心贡献**：提出 OceanCastNet (OCN)，基于机器学习的海浪预报模型，利用风场和浪场数据预测有效波高、平均波周期和平均波向。

**主要方法**：融合风场和浪场输入特征，与业务化 ECWAM 模型对比，在 NDBC 浮标和 Jason-3 卫星观测数据上验证。OCN 在 24 个站点优于 ECWAM（后者仅 10 个站点），在 228 小时预报上精度相当，成功捕捉台风 Goni 极端天气过程，预报误差通常在 ±0.5 米以内。

**意义**：为海浪预报提供深度学习替代方案，计算效率优于传统数值预报模式。

## 关键词
- 海浪预报, 深度学习, 有效波高, 风场浪场融合, ECWAM 对比, 台风预报, NDBC 浮标, 卫星观测, 计算效率
