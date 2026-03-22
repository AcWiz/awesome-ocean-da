---
title: Equation-Free Surrogate Modeling of Geophysical Flows at the Intersection of Machine Learning and Data Assimilation
arXiv: 2205.13410
authors:
- Suraj Pawar
- Omer San
year: 2022
source: arXiv
venue: N/A - Preprint
difficulty: ★★★★☆
importance: ★★★★☆
read_status: skim
method_tags:
- POD
- LSTM
- DEnKF
- Reduced Order Model
- NIROM
application_tags:
- SST
- Sea Surface Temperature
- Data Assimilation
- NOAA OI
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# CTP: A Hybrid CNN-Transformer-PINN Model for Ocean Front Forecasting

## TL;DR
CTP framework combines CNN, Transformer, and physics-informed neural networks for accurate multi-step ocean front prediction in South China Sea and Kuroshio regions.

## Research Question
How can ocean front prediction maintain spatial continuity and physical consistency over multi-step forecasts while achieving state-of-the-art accuracy?

## Main Contributions
1. Proposes CTP framework integrating CNN for spatial encoding, Transformer for temporal attention, and PINN for physics constraints
2. Achieves SOTA performance in both single-step and multi-step ocean front predictions
3. Demonstrates superior accuracy, F1 score, and temporal stability compared to LSTM, ConvLSTM, and AttentionConv baselines

## Method
CTP uses CNN encoder for spatial feature extraction, Transformer encoder for long-range temporal dependencies through multi-head attention, and PINN constraints enforcing Navier-Stokes physics for regularization. The model predicts frontal zones, eastward velocity (u), and northward velocity (v) from preceding week's data. Input dimensions are 7x3x300x300 representing one week of three variables at 300x300 spatial resolution.

## Datasets
- NOAA Coral Reef Watch daily global 5km SST satellite product v3.1
- Copernicus marine service global ocean physics reanalysis (9km resolution)
- South China Sea (SCS): 100-125 deg E, 0-25 deg N
- Kuroshio (KUR): 120-145 deg E, 20-45 deg N
- Temporal range: 1993-2020

## Core Results
- Significantly outperforms LSTM, ConvLSTM, CNN-LSTM-PINN (CLP), and AttentionConv in accuracy
- Achieves superior F1 score for front detection
- Maintains temporal stability in multi-step predictions

## Limitations
- Validated primarily in South China Sea and Kuroshio regions; generalizability to other ocean regions requires further testing
- Performance may degrade for extreme front events not well represented in training data

## Research Gaps
- Application to other ocean phenomena beyond fronts
- Integration with operational ocean forecasting systems
- Extension to subsurface ocean feature prediction