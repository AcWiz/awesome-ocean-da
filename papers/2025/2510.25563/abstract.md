---
title: Leveraging an Atmospheric Foundational Model for Subregional Sea Surface Temperature Forecasting
arXiv: 2510.25563
authors:
- Víctor Medina
- Giovanny A. Cuervo-Londoño
- Javier Sánchez
year: 2025
source: arXiv
venue: NeurIPS
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- foundation_model
- Aurora
- SST
- fine_tuning
- ocean_forecasting
application_tags:
- Canary_Upwelling
- sea_surface_temperature
- Northeastern_Atlantic
- regional_ocean
- potential_temperature
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Leveraging an Atmospheric Foundational Model for Subregional Sea Surface Temperature Forecasting

## TL;DR
Aurora foundation model fine-tuned for Canary Upwelling System achieves RMSE 0.119K and ACC 0.997, demonstrating cross-domain adaptability from atmosphere to ocean.

## Research Question
How can a foundational model pre-trained on atmospheric data be adapted for oceanographic SST prediction in regional upwelling systems?

## Main Contributions
1. Demonstrates first successful adaptation of atmospheric foundation model (Aurora) to oceanographic prediction via two-stage fine-tuning
2. Achieves RMSE 0.119K and ACC 0.997 for Canary Upwelling System SST prediction
3. Establishes methodology for cross-domain transfer learning between atmospheric and oceanic forecasting

## Method
Aurora Medium model (660M parameters) with 3D Swin-Transformer processor. Two-stage fine-tuning: (1) decoder-only training with lr=1e-4, (2) full model fine-tuning with lr=1e-5. Data converted to Kelvin with zero-mean unit-variance normalization. Staged training with partial layer freezing preserves pre-trained representations. Autoregressive prediction up to 10 days. MAE loss with latitude-weighted metrics.

## Datasets
- GLORYS12V1 ocean reanalysis (1/12 degree, 50 vertical levels, 2014-2021)
- Canary Upwelling System region (19.55N-34.53N, 20.97W-5.98E)
- Training: 2014-2018; validation: 2019; testing: 2020
- Variables: potential temperature, salinity, sea level, currents, mixed layer depth

## Core Results
- Best RMSE: 0.119K with full fine-tuning strategy
- ACC consistently 0.997 across all configurations
- 10-day autoregressive forecast reaches RMSE 0.9K in summer
- Successfully captures large-scale SST patterns; coastal regions show higher error
- Decoder fine-tuning alone achieves RMSE 0.135K

## Limitations
- Regional focus limits global applicability
- Computational requirements (batch size constraints) limit resolution
- Reanalysis data inherits biases from underlying numerical models
- Coastal zones with complex topography show degraded performance
- Single variable (potential temperature) limits understanding of coupled dynamics

## Research Gaps
- Extension to multivariable ocean prediction (salinity, currents)
- Global ocean forecasting capability
- Physics-informed neural networks for dynamical consistency
- Higher spatial resolution through progressive training or domain decomposition
- Integration of in-situ and satellite observations for improved validation
