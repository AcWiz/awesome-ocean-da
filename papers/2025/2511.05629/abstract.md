---
title: SSTODE: Ocean-Atmosphere Physics-Informed Neural ODEs for Sea Surface Temperature Prediction
arXiv: 2511.05629
authors:
- Zheng Jiang
- Wei Wang
- Gaowei Zhang
- Yi Wang
year: 2025
source: arXiv
venue: NeurIPS
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- Neural_ODE
- physics_informed
- advection_diffusion
- SST_prediction
- energy_exchange
application_tags:
- sea_surface_temperature
- ocean_atmosphere_coupling
- global_ocean
- upwelling
- diurnal_cycle
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Eigenvalue Initialisation and Regularisation for Koopman Autoencoders

## TL;DR
Eigeninit and eigenloss schemes improve Koopman autoencoder convergence by up to 5x and reduce long-term prediction error by up to 3x for ocean and fluid dynamics.

## Research Question
How can spectral properties of Koopman operators be exploited to improve regularisation and performance of physics-aware neural networks?

## Main Contributions
1. Proposes eigeninit scheme that samples initial Koopman operators from specific eigenvalue distributions
2. Suggests eigenloss penalty scheme that penalises eigenvalues during training
3. Demonstrates up to 5x faster convergence and 3x reduction in cumulative long-term prediction error

## Method
The eigeninit scheme initialises Koopman operator weights by sampling from eigenvalue distributions matched to stable dynamical systems (eigenvalues within unit circle). The eigenloss penalty modifies eigenvalues during training to enforce stability. The Koopman autoencoder architecture consists of encoder, Koopman operator layer, and decoder. Methods are applicable to any Koopman-based approach.

## Datasets
- Driven pendulum (synthetic)
- Flow past a cylinder (synthetic)
- Ocean surface temperatures (real-world)
- Cyclone wind fields (real-world)

## Core Results
- Improves convergence rate by up to a factor of 5
- Reduces cumulative long-term prediction error by up to a factor of 3
- Point utility of spectral schemes for physics-related deep learning

## Limitations
- Requires tuning of penalty weights
- Validated primarily on relatively low-dimensional systems
- Performance depends on eigenvalue distribution selection

## Research Gaps
- Application to higher-dimensional ocean and climate systems
- Extension to other physics-related deep learning architectures
- Automated eigenvalue distribution selection