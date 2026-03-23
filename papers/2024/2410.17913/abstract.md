---
title: "Deep learning for model correction of dynamical systems with data scarcity"
arXiv: "2410.17913"
authors: ['Caroline Tatsuoka', 'Dongbin Xiu']
year: 2024
source: "arXiv"
venue: "arXiv"
method_tags: []
application_tags: []
---

# Deep learning for model correction of dynamical systems with data scarcity

## 基本信息
- **论文链接**: https://arxiv.org/abs/2410.17913
- **作者**: Caroline Tatsuoka, Dongbin Xiu

## 摘要
fidelity data set. In many practical situations, one has a low-fidelity model that can capture the dynamics reasonably well but lacks high resolution, due to the inherent limitation of the model and the complexity of the underlying physics. When high resolution data become available, it is natural to seek model correction to improve the resolution of the model predictions. We focus on the case when the amount of high-fidelity data is so small that most of the existing data driven modeling methods cannot be applied. In this paper, we address these challenges with a model-correction method which only requires a scarce high-fidelity data set. Our method first seeks a deep neural network (DNN) model to approximate the existing low-fidelity model. By using the scarce high-fidelity data, the method then corrects the DNN model via transfer learning (TL). After TL, an improved DNN model with high prediction accuracy to the underlying dynamics is obtained. One distinct feature of the propose method is that it does not assume a specific form of the model correction terms. Instead, it offers an inherent correction to the low-fidelity model via TL. A set of numerical examples are presented to demonstrate the effectiveness of the proposed method.
