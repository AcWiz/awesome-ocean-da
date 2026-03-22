---
title: CAS-C ANGLONG: A SKILLFUL 3D TRANSFORMER MODEL FOR SUB-SEASONAL TO SEASONAL GLOBAL SEA SURFACE TEMPERATURE PREDICTION
arXiv: 2409.05369
authors:
- Longhao Wang
- Chinese Academy of Sciences
- Xuanze Zhang
- Chinese Academy of Sciences
- L. Ruby Leung
- Pacific Northwest National Laboratory
- Francis H.S. Chiew
- CSIRO Environment
- Amir AghaKouchak
- University of California
- Irvine
- Kairan Ying
- National Institute of Natural Hazards
- Yongqiang Zhang
- Chinese Academy of Sciences
year: 2024
source: arXiv
venue: Nature
difficulty: ★★★★☆
importance: ★★★★★
read_status: read
method_tags:
- transformer
- swin_transformer
- attention_mechanism
- 3d_cnn
- lstm
application_tags:
- sst_prediction
- s2s_forecasting
- enso
- ocean_modeling
- climate_prediction
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# CAS-Canglong: A Skillful 3D Transformer Model for Sub-Seasonal to Seasonal Global Sea Surface Temperature Prediction

## TL;DR
3D Swin-Transformer (CAS-Canglong) achieves 13.7-77.1% RMSE improvement over ECMWF S2S and NMME models for 1-3 month global SST prediction.

## Research Question
How can deep learning with self-attention mechanisms achieve skillful sub-seasonal to seasonal (S2S) global SST predictions that outperform physics-based numerical models?

## Main Contributions
1. Develops CAS-Canglong, first DL model specifically for S2S global SST prediction using 3D Swin-Transformer architecture
2. Achieves 13.7-77.1% RMSE improvement over state-of-the-art ECMWF S2S and NMME models across seven key ocean regions
3. Demonstrates superior ENSO prediction skill (R=0.91/0.89/0.57 for 1/2/3-month leads) with 85% hit rate for 3-month forecasts

## Method
3D Swin-Transformer with encoder-decoder architecture processing 16-month input sequences with 8 predictor variables. Self-attention via window-based MSA (W-MSA) and shifted MSA. Earth-specific positional bias strategy. Combined MSE and correlation-based loss function. Training: 1959-2009 (51 years); validation: 2009-2016; testing: 2016-2022. Ensemble predictions from multiple initializations.

## Datasets
- ERA5 monthly reanalysis (0.25 degree, 721x1440 grids)
- 8 predictor variables: SLP, U10, V10, Z850, Z500, latent heat flux, solar radiation, SST
- ECMWF S2S and NMME model outputs for comparison
- HadSST for validation

## Core Results
- RMSE improvement: 34.9% (Niño 3.4), 77.1% (AO), 28.5% (PDO), 39.6% (Warm Pool)
- 1-month lead: R>0.9 for Southern Ocean and Arctic regions
- 3-month lead: ACC>0.7 for Southern Ocean; R=0.57 for ENSO
- Outperforms 22 ECMWF S2S models at 0.25 degree resolution
- 1000x faster inference than physics-based models

## Limitations
- Performance degrades for longer lead times (beyond 3 months)
- Extratropical SST prediction remains challenging
- Model trained on reanalysis data; real-time forecasting depends on data availability
- Computational requirements for 3D Transformer (4 A100 GPUs)

## Research Gaps
- Extension to longer lead times (seasonal to annual)
- Integration with coupled ocean-atmosphere models
- Regional specialization and transfer learning
- Multi-variable prediction (salinity, currents, sea level)
