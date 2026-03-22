---
title: Principled Operator Learning in Ocean Dynamics: The Role of Temporal Structure
arXiv: 2510.09792
authors:
- Vahidreza Jahanmard
- Ali Ramezani-Kebrya
- Robinson Hordoir
year: 2025
source: arXiv
venue: NeurIPS
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- neural_operator
- FNO
- temporal_dispersion
- ocean_modeling
- physics_informed
application_tags:
- ocean_circulation
- sea_level_prediction
- Baltic_Sea
- regional_ocean
- wave_propagation
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Spatio-temporal Modeling and Forecasting with Fourier Neural Operators

## TL;DR
FNO-based dynamic spatio-temporal statistical models enable accurate forecasting with valid uncertainty quantification for SST and precipitation data.

## Research Question
How can Fourier neural operators construct statistical dynamical spatio-temporal models that capture complex real-world dependencies?

## Main Contributions
1. Proposes FNO-based dynamic spatio-temporal (DST) statistical modeling framework
2. Demonstrates accurate forecasting with valid uncertainty quantification for SST and precipitation
3. FNO requires no explicit knowledge of underlying PDE

## Method
FNO approximates solution operator of possibly unknown linear or nonlinear PDEs from input-output samples. Dynamical spatio-temporal models use FNO framework to capture temporal evolution of spatial processes. FNO-DST forecasts compared against state-of-the-art statistical spatio-temporal methods. Validated on sea surface temperature (Atlantic Ocean) and precipitation (Europe) data.

## Datasets
- Atlantic Ocean sea surface temperature data
- European precipitation data
- Simulations from nonlinear PDE with known solution

## Core Results
- FNO-DST forecasts accurate with valid uncertainty quantification
- Outperforms state-of-the-art statistical spatio-temporal methods
- Computationally efficient alternative to traditional PDE solvers

## Limitations
- Performance depends on training data quality and representativeness
- May struggle with extreme events not well represented in training
- Uncertainty quantification may underestimate true uncertainty

## Research Gaps
- Extension to other ocean and climate variables
- Integration with data assimilation
- Application to longer-term climate predictions