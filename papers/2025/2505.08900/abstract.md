---
title: "Generalizable neural-network parameterization of mesoscale eddies in idealized and global ocean models"
arXiv: "2505.08900"
authors: ['Pavel Perezhogin', 'Alistair Adcroft', 'Laure Zanna']
year: 2025
source: "arXiv"
venue: "arXiv"
method_tags: []
application_tags: []
---

# Generalizable neural-network parameterization of mesoscale eddies in idealized and global ocean models

## 基本信息
- **论文链接**: https://arxiv.org/abs/2505.08900
- **作者**: Pavel Perezhogin, Alistair Adcroft, Laure Zanna

## 摘要
driven methods have become popular to parameterize the effects of mesoscale eddies in ocean models. However, they perform poorly in generalization tasks and may require retuning if the grid resolution or ocean configuration changes. We address the generalization problem by enforcing physics constraints on a neural network parameterization of mesoscale eddy fluxes. We found that the local scaling of input and output features helps to generalize to unseen grid resolutions and depths offline in the global ocean. The scaling is based on dimensional analysis and incorporates grid spacing as a length scale. We formulate our findings as a general algorithm that can be used to enforce data-driven parameterizations with dimensional scaling. The new parameterization improves the representation of kinetic and potential energy in online simulations with idealized and global ocean models. Comparison to baseline parameterizations and impact on global ocean biases are discussed.
