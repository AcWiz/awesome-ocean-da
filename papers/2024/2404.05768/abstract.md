---
title: STREAMLINING OCEAN DYNAMICS MODELING WITH FOURIER NEURAL OPERATORS: A MULTIOBJECTIVE HYPERPARAMETER AND ARCHITECTURE OPTIMIZATION APPROACH
arXiv: 2404.05768
authors:
- Yixuan Sun
- Argonne National Laboratory
- Ololade Sowunmi
- Florida State University
- Romain Egele
- Université Paris-Saclay
- Sri Hari Krishna Narayanan
- Argonne National Laboratory
- Luke Van Roekel
- Los Alamos National Laboratory
- Prasanna Balaprakash
- Oak Ridge National Laboratory
year: 2024
source: arXiv
venue: Science
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: read
method_tags:
- neural_operator
- fno
- hyperparameter_optimization
- deephyper
- bayesian_optimization
application_tags:
- ocean_modeling
- baroclinic_wind_driven_ocean
- sea_surface_temperature
- forecasting
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Streamlining Ocean Dynamics Modeling with Fourier Neural Operators: A Multiobjective Hyperparameter and Architecture Optimization Approach

## TL;DR
Multiobjective hyperparameter optimization using DeepHyper improves FNO performance for ocean dynamics, with negative anomaly correlation as additional loss term.

## Research Question
How can automated hyperparameter optimization improve Fourier neural operator performance for ocean dynamics forecasting?

## Main Contributions
1. Leverages DeepHyper for multiobjective optimization of FNO hyperparameters
2. Proposes negative anomaly correlation coefficient (ACC) as additional loss term alongside MSE
3. Optimal hyperparameters greatly exceed baseline in autoregressive rollout up to 30 days

## Method
DeepHyper used for automated hyperparameter and architecture optimization of FNOs. Search space includes data preprocessing, architecture, and training hyperparameters. Loss function combines MSE with negative ACC for improved model performance. Optimized for single timestepping and long-horizon autoregressive forecasting. Applied to idealized baroclinic wind-driven ocean system with four prognostic variables.

## Datasets
- Idealized baroclinic wind-driven ocean system
- Four prognostic variables for prediction

## Core Results
- Optimal hyperparameters enhance single timestepping forecast performance
- Greatly improved autoregressive performance for 30-day rollout
- MSE+ACC loss combination outperforms pure MSE

## Limitations
- Validated on idealized ocean model
- Hyperparameter optimization computationally intensive
- May not directly transfer to realistic ocean conditions

## Research Gaps
- Application to real ocean observations
- Integration with data assimilation
- Extension to climate-scale predictions