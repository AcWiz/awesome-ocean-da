---
title: Significant Wave Height Prediction based on Wavelet Graph Neural Network
arXiv: 2107.09483v1
authors:
- Delong Chen
- Fan Liu
- Zheqi Zhang
- Xiaomin Lu
- Zewen Li
year: 2021
source: arXiv
venue: arXiv preprint
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: skim
method_tags:
- Wavelet Transform
- Graph Neural Network
- Deep Learning
- Spatial-Temporal Modeling
application_tags:
- Significant Wave Height
- Ocean Wave Prediction
- Coastal Engineering
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Significant Wave Height Prediction based on Wavelet Graph Neural Network

## TL;DR
Wavelet Graph Neural Network (WGNN) integrates wavelet decomposition with GNN for simultaneous short and long-term significant wave height prediction.

## Research Question
How can deep learning learn both short-term and long-term spatial-temporal dependencies for accurate significant wave height (SWH) prediction?

## Main Contributions
1. Proposes first GNN application to SWH prediction with wavelet transform integration
2. Decomposes SWH data via Db-wavelet transform into frequency bands learned separately by parallel GNNs
3. Achieves 16.4% MSE reduction over vanilla GNN through wavelet decomposition

## Method
Db-type mother wavelet decomposition (3 levels) separates SWH data into approximate and detail components (rA1-rA3, rD1-rD3). Four parallel GNNs independently learn components rD1, rD2, rD3, and rA3. Each GNN uses graph learning, graph convolution, and temporal convolution modules with mix-hop propagation and dilated inception layers. Final prediction reconstructed from individual GNN outputs.

## Datasets
- Buoy data from Chinese Fujian Wave Forecast Station (119.30 degreeE, 24.48 degreeN)
- Taiwan Strait: 13,076 records (July 2016 - December 2017), hourly resolution
- Input features: average wind speed, maximum wind speed, wind direction
- Train-validate-test split: 6:2:2

## Core Results
- WGNN achieves MSE=0.1187 and R2=0.9341, outperforming WW3 numerical model, SVM, ANN, RNN, LSTM, SAE-BP, LSTNet, and TPA-LSTM
- Vanilla GNN (R2=0.9135) outperforms all deep learning baselines except WGNN
- Wavelet decomposition yields 16.4% MSE reduction compared to vanilla GNN
- Effectively captures both normal and extreme wave conditions

## Limitations
- Single buoy location limits geographic generalizability
- Hourly resolution may miss fine-scale wave dynamics
- Wavelet decomposition parameters (decomposition level, mother wavelet choice) require domain expertise

## Research Gaps
- Multi-location SWH prediction with spatial dependencies
- Integration with numerical wave models (WW3, SWAN)
- Uncertainty quantification for wave forecasting
- Generalization to different ocean basins and seasonal conditions
