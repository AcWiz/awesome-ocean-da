---
title: Prediction of Sea Ice Velocity and Concentration in the Arctic Ocean using Physics-informed Neural Network
arXiv: 2510.17756
authors:
- Younghyun Koo
- Maryam Rahnemoonfar
year: 2025
source: arXiv
venue: Nature
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- PINN
- HIS-Unet
- CNN
- physics_informed
- sea_ice
application_tags:
- Arctic_Ocean
- sea_ice_velocity
- sea_ice_concentration
- remote_sensing
- multi_task_learning
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# FEM-PIKFNNs for Underwater Acoustic Propagation Induced by Structural Vibrations in Different Ocean Environments

## TL;DR
Hybrid FEM-PIKFNNs method combines finite element method with physics-informed kernel function neural networks for accurate underwater acoustic propagation prediction.

## Research Question
How can neural networks be integrated with traditional numerical methods to efficiently predict underwater acoustic propagation in infinite domain ocean environments?

## Main Contributions
1. Proposes hybrid FEM-PIKFNNs method combining finite element method with physics-informed kernel function neural networks
2. PIKFNNs use physics-informed kernel functions replacing activation functions, integrating prior physical information
3. Green's functions as PIKFs inherently capture Sommerfeld radiation condition at infinity

## Method
PIKFNNs are shallow physics-informed neural networks using physics-informed kernel functions (PIKFs) as neuron functions. The method uses Green's functions as PIKFs and structural-acoustic coupling response from FEM as boundary training data. This architecture eliminates the need to embed governing equations into loss functions, requiring only boundary data training. The hybrid approach combines FEM accuracy with PIKFNN efficiency for infinite domain problems.

## Datasets
- Finite element solutions for validation
- Structural-acoustic coupling response data
- Unbounded ocean, deep ocean, and shallow ocean environments

## Core Results
- Accuracy demonstrated in comparison with true solutions and finite element results
- Feasibility and efficacy validated for different ocean environments
- Efficient training requiring only boundary data

## Limitations
- Validated on synthetic and simulated data
- Requires accurate FEM solutions for coupling
- Performance depends on kernel function selection

## Research Gaps
- Application to real ocean acoustic measurements
- Extension to 3D ocean environments
- Integration with operational underwater acoustic modeling systems