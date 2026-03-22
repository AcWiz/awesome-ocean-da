---
title: A Lagrangian Conditional Gaussian Koopman Network for Data Assimilation and Prediction
arXiv: 2603.14115
authors:
- Zhongrui Wang
- Chuanqi Chen
- Jin-Long Wu
- Nan Chen
year: 2026
source: arXiv
venue: Nature
difficulty: ★★★★★
importance: ★★★★★
read_status: deep_read
method_tags:
- Koopman_Operator
- data_assimilation
- Lagrangian
- conditional_Gaussian
- neural_network
application_tags:
- Lagrangian_DA
- tracer_observations
- quasi_geostrophic
- flow_estimation
- ensemble_filter
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# KODA: A Data-Driven Recursive Model for Time Series Forecasting and Data Assimilation using Koopman Operators

## TL;DR
KODA integrates forecasting and data assimilation for nonlinear dynamical systems using Fourier domain filtering to disentangle physical and residual dynamics.

## Research Question
How can Koopman operator-based forecasting be combined with data assimilation to handle nonstationarity and enable long-term prediction with noisy measurements?

## Main Contributions
1. Proposes KODA integrating forecasting and data assimilation using Fourier domain filter to disentangle physical and residual dynamics
2. Uses Koopman operator for physical component dynamics and learnable recursive model for time-varying behavior
3. Introduces coarse correction strategy for data assimilation with new measurements at inference time

## Method
KODA uses Fourier domain filter to decompose data into physical component (captured by Koopman operator) and residual dynamics (captured by flexible learnable recursive model). Architecture ensures stable long-term forecasts through careful design. Coarse correction strategy performs data assimilation with noisy measurements at inference time. Completely data-driven and end-to-end learnable. Evaluated on electricity, temperature, weather, Lorenz 63, and Duffing oscillator benchmarks.

## Datasets
- Electricity time series
- Temperature data
- Weather data
- Lorenz 63 system
- Duffing oscillator

## Core Results
- Outperforms state-of-the-art methods on forecasting, data assimilation, and state prediction
- Stable long-term forecasts demonstrated
- Effective data assimilation with noisy measurements

## Limitations
- Performance may degrade for highly chaotic systems
- Requires sufficient training data for both components
- Fourier decomposition may not capture all dynamical features

## Research Gaps
- Application to ocean and climate dynamical systems
- Extension to partial observations
- Integration with operational forecasting systems