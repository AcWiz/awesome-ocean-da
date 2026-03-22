---
title: Ensemble Graph Neural Networks for Probabilistic Sea Surface Temperature Forecasting via Input Perturbations
arXiv: 2603.06153
authors:
- Alejandro J. González-Santana
- Giovanny A. Cuervo-Londoño
- Javier Sánchez
year: 2026
source: arXiv
venue: NeurIPS
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- GNN
- ensemble_learning
- uncertainty_quantification
- SST
- Perlin_noise
application_tags:
- SST_forecasting
- regional_ocean
- canary_current
- ensemble_prediction
- probabilistic_forecasting
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Ensemble Graph Neural Networks for Probabilistic Sea Surface Temperature Forecasting via Input Perturbations

## TL;DR
Spatially coherent Perlin noise perturbations for ensemble GNN achieve better calibration than Gaussian noise for probabilistic SST forecasting in Canary Islands region.

## Research Question
How can input perturbations during inference create diverse ensemble forecasts from a single trained GNN model for regional ocean prediction?

## Main Contributions
1. Proposes lightweight ensemble framework using inference-time input perturbations on hierarchical GNN
2. Demonstrates spatially coherent Perlin noise achieves better CRPS and calibration than unstructured Gaussian noise
3. Shows fractal Perlin noise refinement through octaves does not improve probabilistic forecasting

## Method
Adapted SeaCast GNN to Canary Islands region (North Atlantic). Homogeneous ensemble via input perturbation at inference: Gaussian noise, Perlin noise, and fractal Perlin noise with varying resolutions and intensities. 5 ensemble members. Aggregated via mean for final forecast. Evaluated with deterministic (RMSE, bias) and probabilistic (CRPS, spread-skill ratio) metrics over 15-day horizon.

## Datasets
- CMEMS North Atlantic SST L4 product (0.05 degree, 1982-2023)
- ERA5 atmospheric forcing (u10, v10 wind components)
- ETOPO bathymetry
- Training: 2003-2019; validation: 2020-2021; testing: 2022-2023

## Core Results
- Deterministic skill remains comparable to single model across all ensemble configurations
- Perlin noise (low resolution 2x3x3) achieves spread-skill ratio close to 1 at 15-day lead, indicating well-calibrated ensemble
- Gaussian noise (sigma=0.1) shows overdispersion initially but becomes underdispersed at longer leads
- Spatially coherent perturbations better capture geophysical correlation scales
- CRPS increases with lead time; structured noise maintains lower CRPS than random noise

## Limitations
- Single variable (SST) limits capturing complex coastal upwelling dynamics
- No autoregressive training (only 1-day training horizon)
- 10 ensemble members showed no significant improvement over 5
- Computational constraints limited training on single GPU

## Research Gaps
- Perturbation of atmospheric forcing variables
- Lagged prediction ensembles
- Training with autoregressive steps for better long-term predictions
- Parameter perturbation for ensemble diversity
