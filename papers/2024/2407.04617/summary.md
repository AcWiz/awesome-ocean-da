---
title: "Randomized Physics-Informed Neural Networks for Bayesian Data Assimilation"
arXiv: "2407.04617"
authors: ['Yifei Zong', 'David Barajas-Solano', 'Alexandre M. Tartakovsky']
year: 2024
source: "arXiv"
venue: "arXiv"
method_tags: ["Bayesian Data Assimilation", "Physics-Informed Neural Networks", "Uncertainty Quantification"]
application_tags: ["Inverse Problems", "PDE"]
difficulty: "★★★☆☆"
---

# Randomized Physics-Informed Neural Networks for Bayesian Data Assimilation

## 基本信息
- **论文链接**: https://arxiv.org/abs/2407.04617
- **作者**: Yifei Zong, David Barajas-Solano, Alexandre M. Tartakovsky

## 摘要

informed neural network (PINN) or rPINN method for uncertainty quantification in inverse partial differential equation (PDE) problems with noisy data. This method is used to quantify uncertainty in the inverse PDE PINN solutions. Recently, the Bayesian PINN (BPINN) method was proposed, where the posterior distribution of the PINN parameters was formulated using the Bayes&#39; theorem and sampled using approximate inference methods such as the Hamiltonian Monte Carlo (HMC) and variational inference (VI) methods. In this work, we demonstrate that HMC fails to converge for non-linear inverse PDE problems. As an alternative to HMC, we sample the distribution by solving the stochastic optimization problem obtained by randomizing the PINN loss function. The effectiveness of the rPINN method is tested for linear and non-linear Poisson equations, and the diffusion equation with a high-dimensional space-dependent diffusion coefficient. The rPINN method provides informative distributions for all considered problems. For the linear Poisson equation, HMC and rPINN produce similar distributions, but rPINN is on average 27 times faster than HMC. For the non-linear Poison and diffusion equations, the HMC method fails to converge because a single HMC chain cannot sample multiple modes of the posterior distribution of the PINN parameters in a reasonable amount of time.
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