---
title: Application of Deep Learning to the Estimation of Normalization Coefficients in Diffusion-Based Covariance Models
arXiv: 2312.05068
authors:
- Folke Skrunes
- Mayeul Destouches
- Anthony T. Weaver
- Guillaume Coulaud
- Olivier Goux
- Corentin Lapeyre
year: 2023
source: arXiv
venue: arXiv
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- CNN
- Data_Assimilation
- Diffusion_Operator
- Normalization_Coefficients
- Covariance_Model
application_tags:
- Ocean_Data_Assimilation
- Variational_DA
- Correlation_Operators
- NEMOVAR
- Ocean_Modeling
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Application of Deep Learning to Estimation of Normalization Coefficients in Diffusion-Based Covariance Models

## TL;DR
CNN estimates normalization factors for ocean DA diffusion-based covariance operators 3x more accurately than Monte Carlo randomization with 10000 samples.

## Research Question
How can CNNs efficiently estimate normalization factors for diffusion-based correlation operators in ocean data assimilation systems?

## Main Contributions
1. Proposes CNN-based estimation of normalization factors for diffusion-based covariance operators
2. Demonstrates 3x lower mean absolute relative error vs randomization with 10^4 samples
3. Requires only 10 training samples (vs thousands of Monte Carlo samples) for effective training

## Method
ResNet architecture with 4 residual blocks, ~3x10^5 parameters. 4 input channels: scaled diffusivity fields (alpha1, alpha2), grid cell area (w), distance-to-coast. Translation-equivariant formulation preserves CNN compatibility. Preprocessing: re-scaling diffusivities to reduce 8 inputs to 3 while preserving equivariance. L1 loss masked over ocean points only.

## Datasets
- NEMO ORCA1 configuration (global ocean, ~1 degree resolution)
- 190 generated samples with spatially-correlated perturbations
- Training: 10 samples, Validation: 10 samples, Test: 170 samples
- 2D diffusion operator from NEMOVAR ocean DA system
- Brute-force ground truth for normalization factors

## Core Results
- CNN: epsilon=0.4% mean absolute relative error
- Randomization (10^4 samples): epsilon=1.15% mean absolute relative error
- CNN 4.3% vs randomization 5.91% mean maximum absolute relative error
- Distance-to-coast input channel reduces coastal errors by up to 10x
- Single forward pass inference vs thousands of diffusion operator applications

## Limitations
- Only 2D diffusion tested (3D extension discussed but not validated)
- Coarse 1 degree resolution (operational systems use 1/4 to 1/12 degree)
- Single ocean model configuration
- Training data generation via brute-force still expensive for high resolution
- Generalization to different boundary conditions not tested

## Research Gaps
- Extension to 3D diffusion and 2D x 1D separable formulation
- Transfer learning across ocean model configurations
- Adaptive correlation models in operational DA
- Integration with ensemble-variational (EnVar) schemes
- Uncertainty quantification for CNN estimates
