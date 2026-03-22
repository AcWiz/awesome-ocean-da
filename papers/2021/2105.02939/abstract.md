---
title: PCE-PINNs: Physics-Informed Neural Networks for Uncertainty Propagation in Ocean Modeling
arXiv: 2105.02939v1
authors: Björn Lütjens; Catherine H. Crawford; Mark Veillette; Dava Newman
year: 2021
source: arXiv
venue: ICLR 2021 Workshop on AI for Modeling Oceans and Climate Change
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: priority-read
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# PCE-PINNs: Physics-Informed Neural Networks for Uncertainty Propagation in Ocean Modeling

## TL;DR
PCE-PINNs combine polynomial chaos expansion with physics-informed neural networks for fast uncertainty propagation of parameter uncertainties in ocean modeling.

## Research Question
How can physics-informed neural networks enable fast uncertainty quantification for climate model parameters when ensemble simulations are computationally prohibitive?

## Main Contributions
1. Proposes PCE-PINNs method combining polynomial chaos expansion with physics-informed neural networks for uncertainty propagation
2. Demonstrates effectiveness for uncertainty propagation in local advection-diffusion equation for ocean temperature modeling
3. Enables fast surrogate model computation for parameter distributions without expensive ensemble simulations

## Method
PCE-PINNs learn PCE coefficients directly from observations using neural networks. The method approximates stochastic functions via polynomial chaos expansion while leveraging neural networks to estimate PCE coefficients in high-dimensional spaces. The network is trained to approximate PCE coefficients using limited solution measurements as target data, enabling fast inference of uncertainty distributions.

## Datasets
- Local advection-diffusion equation for ocean temperature distribution
- Synthetic solutions from differential equation solver
- Stochastic diffusivity modeled as exponential Gaussian process

## Core Results
- Achieves fast surrogate model for uncertainty propagation
- Neural network enables PCE coefficient estimation in high-dimensional spaces
- Demonstrates application to stochastic ocean advection-diffusion modeling

## Limitations
- Validated primarily on local advection-diffusion equation
- Requires known parameter distributions for uncertainty propagation
- Performance depends on training data quality and quantity

## Research Gaps
- Application to full 3D ocean circulation models
- Integration with operational climate modeling systems
- Extension to more complex stochastic parameterizations