---
title: 'Sub-seasonal Forecasting with Deep Learning Weather Prediction'
arXiv: ''
authors:

year: 2021
source: other
venue: arXiv
domain_tags:
- Deep-Learning
ocean_vars: Global Ocean, Climate
spatiotemporal_res: Unknown
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: skim
---


# Sub-seasonal Forecasting with a Large Ensemble of Deep-Learning Weather Prediction Models

## 基本信息
- **arXiv**: [2102.05107](https://arxiv.org/abs/2102.05107)
- **作者**: Jonathan A. Weyn, Dale R. Durran, Rich Caruana, Nathaniel Cresswell-Clay
- **年份**: 2021

## 中文总结
**核心贡献**：构建了基于深度学习天气预测(DLWP)模型的大规模集合预报系统，实现了计算高效的次季节尺度预报。

**主要方法**：
- 使用卷积神经网络(CNN)在立方体球网格上进行全球天气预报
- 通过随机化CNN训练过程创建32个不同权重的模型组成集合
- 单GPU仅需3分钟即可生成320个成员的6周预报

**意义**：在次季节到季节(S2S)时间尺度的预报中表现出与ECMWF集合预报相当的性能，为海洋、大气等地球系统的中期预报提供了新的计算框架。

## 关键词
- 深度学习, 次季节预报, 集合预报, 卷积神经网络, 天气预报, S2S预报
