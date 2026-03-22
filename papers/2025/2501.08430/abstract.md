---
title: Physics-informed neural networks for phase-resolved data assimilation and prediction of nonlinear ocean waves
arXiv: 2501.08430
authors:
- Svenja Ehlers
- Norbert Hoffmann
- Tianning Tang
- Adrian H. Callaghan
- Rui Cao
- Enrique M. Padilla
- Yuxin Fang
- Merten Stender
year: 2025
source: arXiv
venue: Physics of Fluids
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- PINN
- potential_flow
- wave_physics
- phase_resolved
- data_assimilation
application_tags:
- ocean_waves
- wave_prediction
- data_assimilation
- wave_flume
- nonlinear_waves
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Physics-informed neural networks for phase-resolved data assimilation and prediction of nonlinear ocean waves

## TL;DR
PINNs parameterize potential flow theory solutions to achieve computationally efficient assimilation and prediction of irregular, nonlinear ocean waves from sparse surface measurements.

## Research Question
How can phase-resolved ocean wave prediction achieve real-time capability while accurately capturing strong wave nonlinearity without excessive computational cost?

## Main Contributions
1. Proposes a physics-informed neural network (PINN) framework that parameterizes potential flow theory solutions as neural networks
2. Demonstrates accurate capture and prediction of irregular, nonlinear, and dispersive wave surface dynamics validated against analytical solutions and laboratory data
3. Enables inference of fully nonlinear velocity potential throughout the fluid volume from surface elevation measurements alone

## Method
The PINN framework solves the inverse problem of wave data assimilation using physics-informed neural networks. The network parameterizes both the velocity potential and surface elevation fields, trained by enforcing Laplace equation and free surface boundary conditions via automatic differentiation. The loss function includes residuals of governing equations and data fidelity terms evaluated at collocation points without numerical grid requirements.

## Datasets
- Analytical linear potential flow theory solutions for validation
- MARATHON laboratory wave flume measurements (Imperial College London)
- JONSWAP-type random waves with varying steepness (0.05 to 0.11)

## Core Results
- Accurate reconstruction of irregular nonlinear wave surfaces from sparse buoy-like measurements
- PINN successfully infers velocity potential throughout the fluid domain from surface elevation data alone
- Achieves good agreement with both analytical solutions and experimental wave flume data

## Limitations
- Computational cost of PINN training may still be significant for real-time applications
- Performance validated primarily on laboratory data; real ocean conditions may introduce additional complexities

## Research Gaps
- Extension to three-dimensional wave dynamics and real ocean environments
- Integration with operational wave forecasting systems
- Development of faster training strategies for real-time assimilation applications