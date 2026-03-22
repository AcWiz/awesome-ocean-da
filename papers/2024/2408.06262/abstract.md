---
title: DUNE: A MACHINE LEARNING DEEPUNET++BASED ENSEMBLE APPROACH TO MONTHLY, SEASONAL AND ANNUAL CLIMATE FORECASTING
arXiv: 2408.06262
authors:
- Pratik Shukla
- University of Maryland Baltimore County
- Milton Halem
- University of Maryland Baltimore County
year: 2024
source: arXiv
venue: ICML
difficulty: ★★★☆☆
importance: ★★★★★
read_status: read
method_tags:
- unet
- unetpp
- ensemble
- convolutional_neural_network
- residual_block
- moving_window
application_tags:
- sst_prediction
- t2m_prediction
- s2s_forecasting
- climate_forecasting
- seasonal_prediction
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# DUNE: A Machine Learning Deep UNet++ Based Ensemble Approach to Monthly, Seasonal and Annual Climate Forecasting

## TL;DR
Deep UNet++ ensemble (DUNE) trained on ERA5 monthly mean data outperforms persistence, climatology, and linear regression for monthly to annual temperature forecasts.

## Research Question
How can deep learning architectures trained on monthly mean reanalysis data achieve skillful subseasonal-to-seasonal (S2S) and annual climate predictions?

## Main Contributions
1. Proposes DUNE, a Deep UNet++-based ensemble architecture with multi-encoder-decoder structures and residual blocks for S2S forecasting
2. Achieves first AI-based global monthly, seasonal, and annual mean forecasts for 2m temperature (T2m) and sea surface temperature (SST)
3. Outperforms NOAA operational monthly forecasts at 0.25 degree resolution (100x faster) with comparable statistical accuracy

## Method
Deep UNet++ fully convolutional neural network trained on ERA5 monthly mean data (1980-2016). Model predicts temperature anomalies using 7 input channels (SST over oceans, T2m over land, land-sea mask, orography, soil type, vegetation cover, solar radiation). Four intermediate ensemble predictions averaged for final output. Moving window approach enables extended-range forecasts (1-12 months). Training: 444 months; validation: 24 months; testing: 60 months (2019-2023).

## Datasets
- ERA5 monthly mean reanalysis (1940-2024, 0.25 degree resolution)
- 2m temperature (T2m) over land, SST over oceans
- Constant fields: land-sea mask, orography, soil type, high/low vegetation cover
- Top of atmosphere incident solar radiation (TISR)

## Core Results
- Monthly forecast: RMSE 1.07, ACC 0.74 (global), outperforming all baselines
- Seasonal forecast: RMSE 0.87, ACC 0.77
- Annual forecast: RMSE 0.63, ACC 0.85
- Comparable to NOAA operational 12-month probabilistic forecasts, 1000x faster
- 12-month moving window: RMSE 1.27, ACC 0.61

## Limitations
- AI/ML climate forecasting depends on training data period selection
- Climatology period choice (1950-1979) may not capture recent warming trends optimally
- Performance varies with training period; 1980-2016 with 1950-1979 climatology found optimal

## Research Gaps
- Wavelet transforms for downsampling/upsampling not fully explored
- Regional forecasts require separate training
- Extension to additional climate variables (precipitation, wind)
- Integration with physics-based ensemble forecasting systems
