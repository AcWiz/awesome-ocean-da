---
title: LanTu: Dynamics-Enhanced Deep Learning for Eddy-Resolving Ocean Forecasting
arXiv: 2505.10191
authors:
- Qingyu Zheng
- Qi Shao
- Guijun Han
- Wei Li
- Hong Li
- Xuan Wang
year: 2025
source: arXiv
venue: Nature
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- Vision_Transformer
- AFNO
- dynamics_enhancement
- multi_scale
- CNN
application_tags:
- ocean_forecasting
- mesoscale_eddy
- SST
- salinity
- ocean_circulation
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# LanTu: Dynamics-Enhanced Deep Learning for Eddy-Resolving Ocean Forecasting

## TL;DR
Vision Transformer with dynamics-enhanced multiscale constraint achieves superior eddy-resolving ocean forecasting, outperforming operational NOFS and AI-OFS by 2-4 weeks.

## Research Question
How can dynamics-enhanced deep learning overcome the smoothing/blurring effect in AI ocean forecasting to capture mesoscale eddy evolution?

## Main Contributions
1. Proposes LanTu, an AI-based regional eddy-resolving ocean forecasting system with Vision Transformer backbone
2. Designs dynamics-enhanced multiscale constraint combining static (MSE) and dynamic (forecast increment correlation) loss terms
3. Demonstrates superior 3D eddy structure capture and eddy splitting/merging prediction compared to XiHe global AI-OFS

## Method
Non-autoregressive Vision Transformer (AFNO-inspired) trained on GLORYS12 reanalysis and ERA5 atmospheric data. Input: 97 variables (4 surface atmospheric + 4 ocean variables x 23 depth levels) at 1/12 degree resolution. Dynamics-enhanced loss: static constraint (MSE) + dynamic constraint (Pearson correlation of forecast increments). Separate models trained for each forecast lead time (1-30 days). Northwestern Pacific regional domain (10N-50N, 115E-180E). Training: 1993-2020; evaluation: 2021-2023.

## Datasets
- GLORYS12 Copernicus ocean reanalysis (1993-2023, 1/12 degree, 50 vertical layers, 643m depth)
- ERA5 atmospheric reanalysis (SLP, T2m, U10, V10)
- IV-TT Class 4 validation framework (GODAE OceanView)
- DUACS satellite SLA observations

## Core Results
- 10-day SLA forecast: 46.78% lower RMSE than IV-TT for temperature, 20.08% for salinity
- 30-day forecasts comparable to or better than IV-TT 10-day forecasts
- Positive persistence skill score (PSS) for 10-30 day lead times
- ACC >0.6 for temperature, salinity, SLA at 30-day lead time
- Captures eddy splitting and merging better than XiHe
- 3D eddy structure prediction superior to XiHe at 5-day lead time

## Limitations
- Regional focus limits global applicability
- Relies on GLORYS reanalysis quality for training
- Dynamics constraint designed specifically for Northwestern Pacific
- No fine-tuning for autoregressive cumulative error mitigation

## Research Gaps
- Extension to global ocean forecasting
- Integration of richer physics constraints
- Adaptive boundary conditions for regional modeling
- Coupling with global AI-OFS or weather forecasting models
