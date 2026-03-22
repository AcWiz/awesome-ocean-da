---
title: Multi-decadal Sea Level Prediction using Neural Networks and Spectral Clustering on Climate Model Large Ensembles and Satellite Altimeter Data
arXiv: 2310.04540
authors:
- Saumya Sinha
- John Fasullo
- R. Steven Nerem
- Claire Monteleoni
year: 2023
source: arXiv
venue: arXiv
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- Neural_Network
- Spectral_Clustering
- Sea_Level_Prediction
- Climate_Modeling
- FCNN
application_tags:
- Sea_Level_Rise
- Regional_Sea_Level
- Climate_Change
- Satellite_Altimetry
- Multi-decadal_Prediction
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Multi-Decadal Sea Level Prediction using Neural Networks and Spectral Clustering

## TL;DR
FCNN with spectral clustering achieves 30-year global sea level trend predictions, outperforming non-segmented approach with lower uncertainty.

## Research Question
How can machine learning leverage climate model projections to predict regional sea level trends 30 years ahead?

## Main Contributions
1. Develops FCNN framework mapping climate model trends to altimeter observations for 30-year sea level prediction
2. Demonstrates spectral clustering segmentation improves ML predictions over domain-specified partitioning
3. Provides uncertainty quantification via Monte Carlo dropout with neural networks

## Method
Fully connected neural networks trained on climate model large ensemble projections to predict altimeter sea level trends. Input: 6 climate model (CESM1, CESM2, GFDLESM2M, MPIGE, MPI-ESM1-2-HR, MPI-ESM1-2-LR) trend features. Output: altimeter trend predictions. Spatial segmentation via spectral clustering on SSH time series; separate FCNN per cluster. Weighted MSE loss with latitude-based weights. Monte Carlo dropout for uncertainty estimation.

## Datasets
- Satellite altimeter SSH (1993-2022, 1/4° resolution, 30-year trends)
- Six climate model large ensemble means (CESM1, CESM2, GFDLESM2M, MPIGE, MPI-ESM1-2-HR, MPI-ESM1-2-LR)
- 2° spatial resolution (180x90 grid), 8,001 ocean grid points
- Future predictions for 2023-2052

## Core Results
- Spectral clustering RMSE 0.51 mm/year vs Domain partition 0.40 vs No clustering 0.72
- Spectral clustering achieves variability (RMS 1.05 mm/year) close to altimeter observations (1.23 mm/year)
- Lower cumulative uncertainty with spectral clustering (0.19 mm/year RMS)
- SHAP analysis shows CESM1, CESM2, MPIGE contribute most to predictions

## Limitations
- Climate models don't include ice sheet melting effects
- 30-year prediction horizon limits ground truth validation
- Climate model projections become less certain over longer periods

## Research Gaps
- Inclusion of wind and temperature features
- Integration of ice sheet contributions
- Extension to higher spatial resolution
- Improved handling of model structural uncertainties
