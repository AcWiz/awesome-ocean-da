---
title: Towards fully differentiable neural ocean model with Veros
arXiv: 2511.17427
authors:
- Etienne Meunier
- Said Ouala
- Hugo Frezat
- Julien Le Sommer
- Ronan Fablet
year: 2025
source: arXiv
venue: Nature
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- differentiable_programming
- JAX
- automatic_differentiation
- ocean_model
- parameter_calibration
application_tags:
- ocean_circulation
- ACC
- initial_state_estimation
- model_calibration
- mesoscale_eddy
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Towards Fully Differentiable Neural Ocean Model with Veros

## TL;DR
Veros ocean model modified for full JAX autodifferentiation enables gradient-based state reconstruction and parameter calibration with accurate computed gradients.

## Research Question
How can ocean model calibration and data assimilation be enhanced through differentiable programming with automatic differentiation through the dynamical core?

## Main Contributions
1. Proposes modifications to Veros ocean model enabling full JAX autodifferentiation compatibility
2. Demonstrates gradient-based initial state reconstruction achieving near-zero loss after 4-step optimization
3. Shows gradient-based parameter calibration successfully recovers reference lateral viscosity and bottom friction coefficients

## Method
Modified Veros wrapper ensuring functional purity (no in-place operations). Custom gradient definitions for singular-gradient functions (e.g., sqrt with regularization). Selective differentiation wrapper for parameter subset optimization. Forward-mode differentiation for sensitivity analysis. Gradient descent for initial state correction and parameter calibration. Validation via finite-difference approximation (errors ~10^-7). ACC idealized configuration at 1/4 degree resolution with 15 vertical levels.

## Datasets
- ACC (Antarctic Circumpolar Current) idealized configuration
- Eddy-permitting resolution 1/4 degree
- Zonally re-entiant channel connected to Atlantic basin
- 40S to 40N latitude, 0-60E longitude
- Barotropic streamfunction as calibration target (SSH proxy)
- Reference parameter values: lateral viscosity Ah, bottom friction rbot

## Core Results
- Relative error ~10^-10 for forward simulation consistency after modifications
- Gradient validation errors ~10^-7 over single-step evaluations
- Successful initial temperature field reconstruction from perturbed state
- Calibration recovers reference Ah and rbot values from mis-specified starting points
- Calibrated model reproduces reference ACC transport and mesoscale eddy patterns

## Limitations
- Tested on idealized configurations only
- Long-horizon gradient accuracy not fully validated
- Memory and computational performance for long rollouts not characterized
- Implicit differentiation schemes for vertical mixing not yet implemented

## Research Gaps
- Extension to real-ocean configurations
- Implicit differentiation for vertical mixing schemes
- Hybrid AD/adjoint methods for long-horizon problems
- Integration with ensemble DA methods
- Parameter estimation with real observational data
