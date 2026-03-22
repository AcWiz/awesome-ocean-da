---
title: Spatio-temporal modeling and forecasting with Fourier neural operators
arXiv: 2601.01813
authors:
- Pratik Nag
- Andrew Zammit-Mangion
- Sumeetpal Singh
- Noel Cressie
year: 2026
source: arXiv
venue: Science
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- FNO
- neural_operator
- dynamical_system
- spatio_temporal
- uncertainty_quantification
application_tags:
- SST
- precipitation
- ocean_modeling
- atmospheric_modeling
- forecasting
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Principled Operator Learning in Ocean Dynamics: The Role of Temporal Structure

## TL;DR
FNOtD with temporal Fourier modes improves long-term prediction stability and captures multiscale wave propagation through dispersion relation learning.

## Research Question
How can temporal structure be incorporated into Fourier neural operators to improve physical fidelity in ocean dynamics?

## Main Contributions
1. Modifies FNO to internalize dispersion relation while learning solution operator for ocean PDEs
2. Entangling space and time in integral kernel training enables capture of multiscale wave propagation
3. FNOtD substantially improves long-term prediction stability compared to standard FNO

## Method
FNOtD parameterizes integral kernels jointly over space and time, rather than mapping current state to next timestep at fixed interval. This allows operator to internalize dispersion relations crucial for ocean wave physics. Architecture enables principled zero-shot super-resolution and effective training on limited datasets. Compared against standard FNO and state-of-the-art numerical ocean model.

## Datasets
- Regional ocean model simulations
- Shallow water equations for sea level prediction

## Core Results
- Improved long-term prediction stability over standard FNO
- Better consistency with underlying physical dynamics
- Competitive predictive skill with numerical ocean model
- Lower computational cost than numerical simulation

## Limitations
- Validated on regional scale; generalizability to global ocean unclear
- Requires careful tuning of temporal frequency truncation
- Performance depends on training data coverage

## Research Gaps
- Extension to global ocean modeling
- Integration with data assimilation
- Application to climate-scale predictions