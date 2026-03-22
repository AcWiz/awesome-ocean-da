---
title: Extending SST Anomaly Forecasts Through Simultaneous Decomposition of Seasonal and PDO Modes
arXiv: 2601.01864
authors:
- Rameshan Kallummal
year: 2026
source: arXiv
venue: Nature
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- SVD
- linear_regression
- PDO
- seasonal_decomposition
- multivariate_analysis
application_tags:
- SST
- Pacific_Decadal_Oscillation
- North_Pacific
- sea_surface_temperature
- climate_prediction
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Extending SST Anomaly Forecasts Through Simultaneous Decomposition of Seasonal and PDO Modes

## TL;DR
16-dimensional linear regression with amplitude-modulated seasonal cycles achieves 36+ month PDO prediction skill, outperforming operational and ML methods.

## Research Question
How can simultaneous decomposition of seasonal cycles and Pacific Decadal Oscillation improve long-lead SST predictions?

## Main Contributions
1. Extracts four amplitude-modulated seasonal cycles alongside PDO as fourth SVD mode without a priori assumptions
2. Achieves unprecedented 36+ month prediction skill for PDO and IaS indices (PCC > 0.5, RMSE < 0.4)
3. Predicts sustained negative PDO phase through late 2026 with implications for marine heatwaves

## Method
Multivariate linear regression on 16 predictors (4 SVD modes x 4 variables: SST, zonal wind, meridional wind, surface pressure). SVD applied to raw uncentered data to extract seasonal cycles and their interannual amplitude modulations. PDO naturally emerges as fourth SVD mode (S4). Regression coefficients estimated via least squares with 36 time lags. Training: 1948-2000 (53 years); verification: 2001-2023; out-of-sample: 2024-2027.

## Datasets
- NOAA Extended Reconstructed SST v5 (1948-2025)
- NCEP/NCAR Reanalysis (surface winds, surface pressure)
- North Pacific domain (20°N-60°N, 100°E-90°W)
- Four high-variance regional indices per variable

## Core Results
- All-season PCC > 0.5 and RMSE < 0.4 for 36+ month lead times
- Outperforms operational NCEP CFSv2 and ML/DL methods (Qin et al. 2022, 2023)
- Accurate 7-year spatio-temporal reconstruction (2017-2024)
- Negative PDO predicted through late 2026, reducing marine heatwave likelihood in eastern North Pacific

## Limitations
- Linear model may not capture nonlinear climate dynamics
- Performance varies with training period selection
- Single basin (North Pacific) focus limits global applicability

## Research Gaps
- Extension to global ocean SST prediction
- Integration with ENSO forecasting
- Nonlinear extensions (neural networks) for enhanced skill
- Regular monitoring program for identified high-variance regions
