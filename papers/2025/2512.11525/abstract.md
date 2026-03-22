---
title: NeuralOGCM: Differentiable Ocean Modeling with Learnable Physics
arXiv: 2512.11525
authors:
- Hao Wu
- Yuan Gao
- Fan Xu
- Fan Zhang
- Guangliang Liu
- Yuxuan Liang
- Xiaomeng Huang
year: 2025
source: arXiv
venue: NeurIPS
difficulty: ★★★★★
importance: ★★★★★
read_status: deep_read
method_tags:
- differentiable_physics
- hybrid_model
- neural_network_corrector
- ocean_GCM
- end_to_end_training
application_tags:
- global_ocean
- sea_temperature
- sea_salinity
- ocean_currents
- sea_surface_height
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# NeuralOGCM: Differentiable Ocean Modeling with Learnable Physics

## TL;DR
NeuralOGCM hybrid framework combines differentiable physics solver with neural corrector, achieving superior speed-accuracy trade-off over both numerical and pure AI models.

## Research Question
How can hybrid differentiable physics programming with deep learning bridge the trade-off between computational efficiency and physical fidelity in ocean modeling?

## Main Contributions
1. Proposes learnable physics paradigm where key physical parameters (diffusion coefficients) are optimized end-to-end via gradient descent
2. Designs NeuralOGCM, the first end-to-end differentiable hybrid ocean circulation model combining physics solver with neural corrector
3. Demonstrates significant advantages in speed, accuracy, and long-term stability over traditional numerical and pure AI baselines

## Method
Hybrid architecture: Differentiable Physics Core + Neural Corrector unified by ODE solver. Physics core implements advection, Coriolis force, and horizontal diffusion with learnable parameters (ν_momentum, ν_tracer) via softplus activation. Neural corrector uses encoder-decoder with spatio-temporal evolution (STE) module using multi-head self-attention. Single-step explicit Forward Euler integration. End-to-end training via backpropagation. Latitude-dependent spherical grid metrics. Periodic boundary in longitude.

## Datasets
- Benchmark ocean modeling dataset (likely OCCAM or similar global ocean)
- State variables: ocean internal variables y_t
- Atmospheric forcing: F_t at each timestep
- Subgrid-scale process learning from high-resolution reference

## Core Results
- Maintains long-term stability and physical consistency
- Significantly outperforms traditional numerical models in speed
- Significantly outperforms pure AI baselines in accuracy
- Learnable diffusion parameters converge to physically meaningful values
- Neural corrector captures subgrid-scale dynamics and discretization errors

## Limitations
- Single-step Forward Euler integration may limit long-term accuracy
- Hybrid approach may inherit biases from both physics and neural components
- Performance on eddying regimes not fully characterized
- Generalization to different ocean basins needs validation

## Research Gaps
- Extension to coupled ocean-atmosphere systems
- Higher-order ODE solvers for improved integration
- Adaptive physics-neural coupling strategies
- Application to climate-scale simulations
- Uncertainty quantification for hybrid predictions
