---
title: OceanForecastBench: A Benchmark Dataset for Data-Driven Global Ocean Forecasting
arXiv: 2511.18732
authors:
- Haoming Jia
- Yi Han
- Xiang Wang
- Huizan Wang
- Wei Wu
- Jianming Zheng
- Peikun Xiao
year: 2025
source: arXiv
venue: JGR: Machine Learning and Computation
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- benchmark
- deep_learning
- global_ocean
- multi_source_data
- evaluation_pipeline
application_tags:
- ocean_forecasting
- SST
- salinity
- ocean_currents
- sea_level
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# OceanForecastBench: A Benchmark Dataset for Data-Driven Global Ocean Forecasting

## TL;DR
OceanForecastBench provides standardized training data (28-year GLORYS/ERA5/OSTIA), evaluation dataset (100M+ observations), and evaluation pipeline for 5 baseline models.

## Research Question
How can a standardized benchmark facilitate fair comparison and reproducibility in data-driven global ocean forecasting research?

## Main Contributions
1. Provides 28-year high-quality global ocean reanalysis training data (GLORYS12, ERA5, OSTIA) at 1.4 degree resolution, 23 depth levels
2. Compiles 100 million evaluation observations from EN4, GDP drifters, and CMEMS satellite data
3. Develops standardized evaluation pipeline and benchmarks 5 models (PSY4, ResNet, SwinTransformer, ClimaX, FourCastNet)

## Method
Standardized data processing: regridding to 1.40625 degree, masking land, aggregating multi-source data. Training: 1993-2017; validation: 2018-2020; testing: 2022-2023. Evaluation pipeline aligns grid forecasts with discrete observations via interpolation, calculates RMSE, Bias, ACC, and CSS metrics. Task: predict SLA, SST, temperature, salinity, and currents (Uo, Vo) at 1-10 day lead times.

## Datasets
- GLORYS12 ocean reanalysis (1993-2021, 1/12 degree, 50 layers, SSH, temperature, salinity, currents)
- ERA5 atmospheric (0.25 degree, 6-hourly, 10m wind components)
- OSTIA SST (1/20 degree, daily)
- EN4 in-situ observations (Argo buoys, temperature and salinity profiles)
- GDP drifter observations (6-hourly SST, 15m currents)
- CMEMS L3 satellite SLA

## Core Results
- All models show increasing RMSE with lead time (1-10 days)
- PSY4 excels at short lead times (SST, SLA); deep learning models better for longer leads
- Currents velocity forecast ACC <0.6, indicating reliability concerns
- ResNet and SwinTransformer show highest RMSE for subsurface variables
- ClimaX performs best for temperature and salinity profiles
- Deep learning models outperform PSY4 for currents at longer lead times

## Limitations
- Spatial resolution (1.4 degree) may lose mesoscale information
- 23 vertical levels selected as trade-off between information and GPU memory
- Evaluation limited to 2022-2023 due to observation availability
- Subsurface ocean dynamics remain challenging for all models

## Research Gaps
- Higher spatial resolution benchmarks
- Extended lead times (beyond 10 days)
- Integration of additional observation types
- Regional specialization and domain adaptation
