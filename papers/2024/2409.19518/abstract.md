---
title: KODA: A Data-Driven Recursive Model for Time Series Forecasting and data assimilation using koopman operators
arXiv: 2409.19518
authors:
- Ashutosh Singh
- Ashish Singh
- Tales Imbiriba
- Deniz Erdogmus
- Ricardo Borsoi
year: 2024
source: arXiv
venue: NeurIPS
difficulty: ★★★★★
importance: ★★★★☆
read_status: deep_read
method_tags:
- Koopman_operator
- data_assimilation
- Kalman_filter
- Fourier_filtering
- disentangled_learning
application_tags:
- time_series_forecasting
- nonstationary_dynamics
- state_estimation
- long_term_forecast
- LTSF
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# EnKode: Active Learning of Unknown Flows with Koopman Operators

## TL;DR
EnKode combines Koopman operators with ensemble methods for active sampling of unknown flows, providing comparable or better estimates than Gaussian Process Regression.

## Research Question
How can active sampling strategies based on Koopman operator theory effectively model unknown fluid flows with sparse data?

## Main Contributions
1. Proposes EnKode active sampling approach using Koopman Operator theory and ensemble methods for flow modeling
2. Develops novel measure of flow model uncertainty for active learning strategy
3. Demonstrates comparable or better flow estimates than Gaussian Process Regression with hyperparameter optimization

## Method
EnKode combines Koopman operator theory with ensemble methods to model unknown nonlinear ODEs. Flow measurements are encoded via lifting functions into space where dynamics are linear, propagated by estimated Koopman operator, and reconstructed to produce flow estimate and uncertainty map. Active sensing identifies next sampling location with greatest epistemic uncertainty. Evaluated on Bickley Jet, Lid-Driven Cavity flow, and real NOAA ocean currents.

## Datasets
- Bickley Jet (synthetic)
- Lid-Driven Cavity flow with obstacle (synthetic)
- Real ocean currents from NOAA

## Core Results
- Comparable or better flow estimates than GP regression with hyperparameter optimization
- Active sensing provides more accurate flow estimates than uniform sampling
- Effective uncertainty quantification for flow modeling

## Limitations
- Performance depends on quality of initial sampling
- Koopman eigenvalues may require careful selection
- Real ocean application limited by measurement accessibility

## Research Gaps
- Application to underwater robotic sampling
- Extension to 3D flows
- Integration with autonomous ocean monitoring systems