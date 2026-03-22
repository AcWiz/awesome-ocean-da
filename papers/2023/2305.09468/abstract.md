---
title: Graph-Based Deep Learning for Sea Surface Temperature Forecasts
arXiv: 2305.09468
authors:
- Ding Ning
- Varvara Vetrova
- Karin R. Bryan
year: 2023
source: arXiv
venue: ICLR Workshop
difficulty: ★★☆☆☆
importance: ★★★☆☆
read_status: deep_read
method_tags:
- Graph_Neural_Network
- GCN
- GAT
- GraphSAGE
- SST_Forecasting
- Climate_ML
application_tags:
- Sea_Surface_Temperature
- SST_Prediction
- Climate_Modeling
- ENSO
- Ocean_Forecasting
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Graph-based Deep Learning for Sea Surface Temperature Forecasts

## TL;DR
GraphSAGE model using correlation-based graph construction outperforms persistence model for one-month ahead global SST prediction.

## Research Question
How can graph neural networks and graph-based data structures improve global sea surface temperature forecasting compared to traditional grid-based deep learning approaches?

## Main Contributions
1. Proposes graph-based deep learning framework for global SST forecasting using GNNs instead of grid-based CNNs
2. Demonstrates GraphSAGE outperforms persistence model (RMSE 0.0346 vs 0.0621 normalized) at most global locations
3. Explores correlation-based graph construction methods for SST data with varying thresholds

## Method
Graph neural networks (GCN, GAT, GraphSAGE, RGCN) applied to ERA5 monthly SST data (1950-2022). Graph constructed via Pearson correlation between SST time series at 5774 nodes with threshold c=0.95. Window size of 12 months used for input. Two-layer GNN architecture with 30 features. Training: 760 time steps; testing: remaining 112 time steps.

## Datasets
- ERA5 monthly mean reanalysis SST (0.25 degree, 1940-2022)
- Global SST grid (64 latitude x 128 longitude nodes, 872 months)
- Correlation threshold graphs (c=0.9-0.99)

## Core Results
- GraphSAGE achieves lowest RMSE (0.0346 normalized, 0.6338K) among all GNN models
- GraphSAGE outperforms persistence model (RMSE 0.0621) at most global locations
- Best performance in temperate zones and near continents; poorest in tropics and Antarctica
- Training time significantly faster than other GNN architectures

## Limitations
- Only one-month ahead forecast validated; longer lead times require autoregressive approach
- GCN and GAT underperform persistence model; may need hyperparameter tuning
- RGCN performance poor on directed graphs
- Edge attributes (oceanic/atmospheric variables) not included in current graph construction

## Research Gaps
- Graph U-Nets for SST forecasting
- Inclusion of relational variables for edge attributes
- Non-parametric correlation measures and seasonality removal
- Long lead forecasts (3 months to 2 years) via autoregressive approach
- SST anomaly and marine heatwave prediction
