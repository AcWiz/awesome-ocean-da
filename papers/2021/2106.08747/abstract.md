---
title: Towards Optimally Weighted Physics-Informed Neural Networks in Ocean Modelling
arXiv: 2106.08747v1
authors: Taco de Wolff; Hugo Carrillo; Luis Martí; Nayat Sánchez-Pi
year: 2021
source: arXiv
venue: arXiv preprint
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: priority-read
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Towards Optimally Weighted Physics-Informed Neural Networks in Ocean Modelling

## TL;DR
PINN weight tuning experiments reveal that small datasets benefit more from added physics information; optimal weight depends on network architecture and activation functions.

## Research Question
How does the relative weight between data and physics components in PINN loss functions influence training results for ocean modeling PDEs?

## Main Contributions
1. Explores trade-offs of using data vs physical models in PINNs for solving ocean-related PDEs (Burgers, wave, advection-diffusion equations)
2. Demonstrates that small datasets benefit more from added physics information
3. Studies effects of network hyperparameters (depth, width, activation functions) on optimal weight selection

## Method
Physics-informed neural networks combine neural network data fitting with physics loss terms encoding PDE constraints. The relative weight between data loss and physics loss is systematically varied to study its influence on solution accuracy. Experiments compare different network architectures and activation functions to understand their interaction with optimal weight selection.

## Datasets
- Synthetic data generated from analytical solutions of Burgers equation
- Wave equation solutions for shallow-water modeling
- Advection-diffusion equation for temperature transport

## Core Results
- Small data sets benefit more from physics information in PINN training
- Optimal weight depends on network architecture and activation functions
- Provides guidelines for efficient parameter configuration based on data characteristics

## Limitations
- Studies limited to relatively simple 1D PDEs
- Optimal weight selection requires empirical tuning
- May not generalize to more complex ocean dynamics

## Research Gaps
- Extension to 3D ocean circulation models
- Automated weight selection methods
- Application to real oceanographic observations