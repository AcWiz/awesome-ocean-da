---
title: EnKode: Active Learning of Unknown Flows with Koopman Operators
arXiv: 2410.16605
authors:
- Alice K. Li
- Thales C. Silva
- M. Ani Hsieh
year: 2024
source: arXiv
venue: IEEE Robotics and Automation Letters
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- Koopman_Operator
- Active_Learning
- Ensemble_Methods
- GNN
application_tags:
- ocean_circulation
- flow_modeling
- robotics
- active_sensing
- uncertainty_quantification
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# A Lagrangian Conditional Gaussian Koopman Network for Data Assimilation and Prediction

## TL;DR
LaCGKN enables accurate Lagrangian data assimilation and prediction without ensemble methods or governing physical models using structure-preserving neural network architecture.

## Research Question
How can machine learning overcome the fundamental challenges of Lagrangian data assimilation where nonlinear tracer-flow coupling makes posterior inference computationally intractable?

## Main Contributions
1. Develops LaCGKN embedding Eulerian flow dynamics into low-dimensional latent space governed by nonlinear stochastic system with conditional Gaussian structures
2. Incorporates tracer homogenization for permutation equivariance, Fourier-based positional encoding, and SVD-inspired low-rank parameterization
3. Enables analytic posterior updates without ensemble forecasting for Lagrangian observations

## Method
LaCGKN uses Lagrangian conditional Gaussian Koopman network architecture. Tracer homogenization enforces permutation equivariance for generalization across varying tracer numbers. Fourier-based positional encoding captures spatial dependence and reconstructs local flow features. SVD-inspired low-rank parameterization reduces complexity while preserving expressive capacity. Application to two-layer quasi-geostrophic flow demonstrates accurate assimilation and prediction.

## Datasets
- Two-layer quasi-geostrophic flow with surface tracer observations
- Synthetic Lagrangian tracer trajectories

## Core Results
- Accurate and efficient Lagrangian data assimilation and prediction demonstrated
- No reliance on ensemble methods or governing physical model
- Unified computationally tractable alternative to traditional and data-driven methods

## Limitations
- Validated primarily on simplified quasi-geostrophic model
- Performance depends on tracer coverage and quality
- May require adaptation for real-world ocean conditions

## Research Gaps
- Application to real ocean Lagrangian observations (drifters, floats)
- Extension to three-dimensional flows
- Integration with operational ocean forecasting systems