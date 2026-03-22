---
title: Generative Lagrangian Data Assimilation for Ocean Dynamics under Extreme Sparsity
arXiv: 2507.06479
authors:
- Niloofar Asefi
- Leonard Lupin-Jimenez
- Tianning Wu
- Ruoying He
- Ashesh Chattopadhyay
year: 2025
source: arXiv
venue: Nature
difficulty: ★★★★★
importance: ★★★★★
read_status: deep_read
method_tags:
- DDPM
- FNO
- UNET
- diffusion_model
- neural_operator
- data_assimilation
application_tags:
- Lagrangian_DA
- sparse_observations
- ocean_reconstruction
- Gulf_of_Mexico
- satellite_altimetry
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Generative Lagrangian data assimilation for ocean dynamics under extreme sparsity

## TL;DR
A deep learning framework combining neural operators with denoising diffusion models reconstructs high-resolution ocean states from 99-99.9% sparse Lagrangian observations.

## Research Question
How can we reconstruct high-resolution ocean dynamics from extremely sparse, irregular, and Lagrangian observational data, particularly in subsurface and remote regions where traditional data assimilation methods and deep learning models struggle to recover mesoscale turbulence?

## Main Contributions
1. Proposes a neural operator-conditioned generative diffusion model (FNO+DDPM/UNET+DDPM) for ocean state reconstruction from sparse Lagrangian observations
2. Achieves accurate reconstruction at 99% sparsity (synthetic data) and 99.9% sparsity (real satellite observations) without a background model
3. Preserves both large- and small-scale flow features through Fourier spectral analysis, addressing spectral bias in standard metrics

## Method
The framework combines Fourier Neural Operator (FNO) predictions with denoising diffusion probabilistic models (DDPMs). The FNO provides predictive capabilities while the conditional generative diffusion model enables reconstruction of high-resolution ocean states from sparse Lagrangian observations. Training uses L2/MSE loss, and the model is validated on synthetic and real satellite data.

## Datasets
- Synthetic Lagrangian tracers from 2D forced Kolmogorov flow on beta-plane (Re=10,000)
- GLORYS reanalysis dataset (1/12 degree resolution) for Gulf of Mexico surface ocean dynamics
- CNAPS high-resolution (1/25 degree) satellite altimetry observations over Gulf of Mexico

## Core Results
- RMSE significantly reduced compared to baseline ML methods under 99% sparsity
- Successfully captures small-scale, high-wavenumber dynamics typically missed by standard statistical metrics
- Robust performance on real satellite observations with 99.9% spatial sparsity

## Limitations
- Method validated primarily on Gulf of Mexico regional dynamics; generalizability to other ocean regions unclear
- Requires further validation with actual Lagrangian drifter data rather than synthetic tracers

## Research Gaps
- Extension to three-dimensional deep ocean flow reconstruction with combined surface and interior observations
- Integration with operational ocean forecasting systems for real-time applications