---
title: Physics-Informed Neural Networks for Modeling Ocean Pollutant Transport
arXiv: 2507.08834
authors:
- Karishma Battina
- Prathamesh Dinesh Joshi
- Raj Abhijit Dandekar
- Rajat Dandekar
- Sreedath Panat
year: 2025
source: arXiv
venue: Nature
difficulty: ★★★☆☆
importance: ★★★★★
read_status: deep_read
method_tags:
- PINN
- advection_diffusion
- physics_informed
- neural_network
- Julia
application_tags:
- ocean_pollutant
- advection_diffusion_equation
- finite_difference
- environmental_monitoring
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Physics-Informed Neural Networks for Modeling Ocean Pollutant

## TL;DR
PINN framework with hybrid weighted loss function achieves approximately 8.25% relative L2 error for 2D advection-diffusion pollutant transport simulation.

## Research Question
How can physics-informed neural networks effectively simulate oceanic pollutant dispersion while handling noisy data and enforcing physical constraints?

## Main Contributions
1. Develops robust PINN framework in Julia for oceanic pollutant transport with hybrid weighted loss function
2. Systematically investigates neural network architecture (depth, width) and hyperparameters on solution accuracy
3. Achieves relative L2 error of approximately 8.25% against high-resolution finite difference method

## Method
The PINN approximates solution to 2D advection-diffusion equation governing pollutant transport. Training uses hybrid loss function combining PDE residuals, boundary/initial condition conformity, and weighted data fit term. The framework employs automatic differentiation for gradient computation and handles noisy synthetic data with varying noise levels. Boundary conditions enforce zero concentration at domain edges, simulating localized pollution events.

## Datasets
- Synthetic data generated via finite difference method (FDM)
- 2D advection-diffusion equation with velocity field vx=0.5, vy=0.5
- Diffusion coefficient D=0.01
- Noise-augmented boundary and initial conditions

## Core Results
- Relative L2 error of approximately 8.25% compared to high-resolution FDM
- Robust performance with noisy synthetic data
- Scalable and flexible alternative to traditional solvers

## Limitations
- 2D idealized domain; extension to 3D required for real applications
- Simplified velocity fields used; real ocean currents more complex
- Performance on real ocean pollutant data not demonstrated

## Research Gaps
- Extension to 3D domains with realistic ocean geometries
- Integration with real ocean current data
- Application to specific pollutant types (oil spills, microplastics)