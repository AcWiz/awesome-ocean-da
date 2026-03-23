---
title: "A Neural Network-Based Submesoscale Vertical Heat Flux Parameterization and Its Implementation in Regional Ocean Modeling System (ROMS)"
arXiv: "2403.05028"
authors: ['Shuyi Zhou', 'Jihai Dong', 'Fanghua Xu', 'Zhiyou Jing', 'Changming Dong']
year: 2024
source: "arXiv"
venue: "arXiv"
method_tags: []
application_tags: []
---

# A Neural Network-Based Submesoscale Vertical Heat Flux Parameterization and Its Implementation in Regional Ocean Modeling System (ROMS)

## 基本信息
- **论文链接**: https://arxiv.org/abs/2403.05028
- **作者**: Shuyi Zhou, Jihai Dong, Fanghua Xu, Zhiyou Jing, Changming Dong

## 摘要
temporal scales of O(0.01-10) km and hours to 1 day which are hardly resolved by current ocean models, are important sub-grid processes in ocean models. Due to the strong vertical currents, submesoscale processes can lead to submesoscale vertical heat flux (SVHF) in the upper ocean which plays a crucial role in the heat exchange between the atmosphere and the ocean interior, and further modulates the global heat redistribution. At present, simulating a submesoscale-resolving ocean model is still expensive and time-consuming. Parameterizing SVHF becomes a feasible alternative by introducing it into coarse-resolution models. Traditionally, researchers tend to parameterize SVHF by a mathematically fitted relationship based on one or two key background state variables, which fail to represent the relationship between SVHF and the background state variables comprehensively. In this study, we propose a data-driven SVHF parameterization scheme based on a deep neural network and implement it into the Regional Ocean Modeling System (ROMS). In offline tests, our scheme can accurately calculate SVHF using mesoscale-averaged variables and characterize how it varies with depth. In online tests, we simulate an idealized model of an anticyclonic mesoscale eddy and a realistic model of the Gulf Stream, respectively. Compared to the coarse-resolution cases without the SVHF effect, the coarse-resolution cases with the SVHF scheme tend to reproduce results closer to the high-resolution case and the observational state in terms of the temperature structure and mixed layer depth, indicating a good performance of the neural network-based SVHF scheme. Our results show the potential of applying the neural network in parameterizing sub-grid processes in ocean models.
