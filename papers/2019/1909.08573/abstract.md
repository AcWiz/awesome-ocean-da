---
title: Statistical and Machine Learning Ensemble Modelling to Forecast Sea Surface Temperature
arXiv: 1909.08573v2
authors:
- Stefan W ola
- Fearghal O'Donncha
- Bei Chen
year: 2019
source: arXiv
venue: Journal of Marine Systems
difficulty: ★★☆☆☆
importance: ★★★☆☆
read_status: skim
method_tags:
- Ensemble Learning
- Regression
- Decision Tree
- Deep Learning
- Feature Engineering
application_tags:
- SST Forecasting
- Ocean Modeling
- Sea Surface Temperature
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Statistical and Machine Learning Ensemble Modelling to Forecast Sea Surface Temperature

## TL;DR
Ensemble of GAM, Random Forest, XGBoost, MLP, and LSTM models achieves ECMWF-comparable SST forecasting accuracy at negligible computational cost.

## Research Question
How can machine learning models with automated feature engineering achieve transportable, computationally efficient SST predictions comparable to physics-based numerical models?

## Main Contributions
1. Develops autonomous feature-engineering module for SST prediction using autoregressive features, atmospheric variables, and temporal information
2. Demonstrates ensemble aggregation via inverse MAPE weighting improves robustness over individual models
3. Achieves comparable accuracy to ECMWF physics-based forecasts (MAE 0.68 vs 0.56C, MAPE 7.9% vs 12.3%) at fraction of computational cost

## Method
Five ML models trained on 16 years of MODIS Aqua SST data (2002-2018) at North Atlantic location, then transportability tested globally at 730 locations. Models: Generalized Additive Models (GAM), Random Forest (RF), XGBoost, Multi-Layer Perceptron (MLP), and Long Short-Term Memory (LSTM). Feature engineering selects optimal autoregressive lags (30 days for GAM/RF/XGBoost, 400 days for MLP/LSTM) and atmospheric variables via F-score correlation analysis. Ensemble weighted by inverse MAPE. Evaluation: 90%/10% train-test split.

## Datasets
- MODIS Aqua satellite SST (Level 3, 4km, daily, daytime, 2002-2018)
- Weather Company atmospheric data (18 variables: air temperature, solar radiation, cloud cover, wind, etc.)
- ECMWF ERA5 reanalysis for validation benchmark

## Core Results
- Ensemble average MAPE 1.88% at North Atlantic location
- Global transportability: MAE <1C and MAPE <10% at most of 730 locations
- Ensemble average: MAE 0.68C, MAPE 7.9% (vs ECMWF 0.56C, 12.3%)
- GAM captures seasonal patterns; XGBoost and MLP capture short-term variations
- LSTM fails to capture high-frequency variations due to long-memory interference

## Limitations
- Missing data (57% at some locations) requires linear interpolation
- LSTM underperforms despite RNN design for temporal data
- Computational cost of feature engineering at each new location
- Performance degrades at higher latitudes due to reduced satellite data availability

## Research Gaps
- Integration of convolutional neural networks for spatial neighboring effects
- Extension to spatial fields rather than point-based predictions
- Automated hyperparameter optimization for new locations
- Integration with physics-based models for hybrid predictions
