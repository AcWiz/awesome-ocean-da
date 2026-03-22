---
title: A Deep Learning Model for Forecasting Global Monthly Mean Sea Surface Temperature Anomalies
arXiv: 2202.09967
authors:
- John Taylor
- Ming Feng
year: 2022
source: arXiv
venue: N/A - Preprint
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: skim
method_tags:
- Unet-LSTM
- CNN
- LSTM
- ERA5
- Deep Learning
application_tags:
- SST
- ENSO
- Marine Heatwaves
- Sea Surface Temperature
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# A Deep Learning Model for Forecasting Global Monthly Mean Sea Surface Temperature Anomalies

## TL;DR
Unet-LSTM model predicts global SST anomalies up to 24 months with RMSE below 0.75°C, capturing ENSO events and marine heatwaves.

## Research Question
How can deep learning models predict global sea surface temperature anomalies at long lead times for climate applications?

## Main Contributions
1. Develops Unet-LSTM architecture combining spatial (Unet) and temporal (LSTM) learning for SST prediction
2. Achieves accurate 24-month SST predictions with RMSE below 0.75°C for all predicted months
3. Demonstrates long-lead prediction skill for ENSO events and marine heatwaves including Blob

## Method
Unet-LSTM model trained on 70+ years (1950-2021) of ECMWF ERA5 monthly mean SST and 2m air temperature data. Unet captures spatial patterns while LSTM learns temporal evolution. Model learns underlying physics driving SST variability. Validated on ENSO indices (Niño3.4), marine heatwaves (Blob, Ningaloo Niño).

## Datasets
- ECMWF ERA5 monthly mean SST (1950-2021)
- 2-metre air temperature data
- Global coverage for SST anomaly prediction

## Core Results
- RMSE below 0.75°C for 24-month predictions
- Captures 2010-11 La Niña, 2009-10 El Niño, 2015-16 extreme El Niño
- Long-lead prediction skill for Blob marine heatwave
- Limited skill for Ningaloo Niño in southeast Indian Ocean

## Limitations
- Monthly mean predictions; sub-monthly variability not captured
- Limited skill for some regional marine heatwaves
- Performance depends on training data length and quality

## Research Gaps
- Extension to weekly/daily predictions
- Integration with coupled ocean-atmosphere models
- Application to other marine ecosystem variables