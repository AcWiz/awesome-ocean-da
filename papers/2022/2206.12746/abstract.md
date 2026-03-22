---
title: Modeling Oceanic Variables with Dynamic Graph Neural Networks
arXiv: 2206.12746
authors:
- Caio F. D. Netto
- Marcel R. de Barros
- Jefferson F. Coelho
- Lucas P. de Freitas
- Felipe M. Moreno
- Marlon S. Mathias
- Marcelo Dottori
- Fábio G. Cozman
- Anna H. R. Costa
- Edson S. Gomi
- Eduardo A. Tannuri
year: 2022
source: arXiv
venue: N/A - Preprint
difficulty: ★★★★☆
importance: ★★★☆☆
read_status: skim
method_tags:
- GNN
- Graph Neural Network
- LSTM
- Transformer
- Dynamic Graph
application_tags:
- Ocean Dynamics
- Current Velocity
- SSH
- Santos Estuarine System
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Modeling Oceanic Variables with Dynamic Graph Neural Networks

## TL;DR
Graph neural network with LSTM/Transformer encoders predicts ocean current and SSH in Santos Estuarine System, outperforming physics-based SOFS model.

## Research Question
How can graph neural networks combine spatial and temporal modeling to predict oceanic variables in complex coastal estuarine systems?

## Main Contributions
1. Proposes spatio-temporal GNN architecture combining sequence models (LSTM/Transformer) with graph neural networks for ocean prediction
2. Achieves 27% improvement in water current speed and 14% in direction over physics-based SOFS model
3. Demonstrates handling of significant missing data (50% overall) in real sensor observations

## Method
Dynamic Temporal Graph representation of ocean variables as nodes with type and location. Encoder-decoder framework: temporal encoder (LSTM or Transformer) processes variable-length time series; GNN with attention propagates information spatially between observation sites. Separate decoders for current velocity (fixed-size MLP) and SSH (dynamic MLP with future information). Trained on 974 days of data from 6 observation sites.

## Datasets
- Santos-Sao Vicente-Bertioga Estuarine System (SSVBES), Brazil
- Six observation sites with current, SSH, and wind sensors
- 30-minute aggregated data from Jan 2019 to Sep 2021
- Missing data: 24.3% (current), 42.1% (SSH), 84.1% (wind)

## Core Results
- LSTM encoder + GATv2: IoA 0.726 for current speed vs 0.599 for SOFS
- Transformer encoder achieves best performance: 27% speed improvement over SOFS
- Adding SSH nodes improves current prediction; current addition does not improve SSH
- Fully connected graph topology outperforms same-variable and disconnected graphs

## Limitations
- Validated on single estuarine system; generalizability unclear
- Homogeneous GNN may not capture distinct variable dynamics optimally
- Performance degrades when wind data added due to over-squashing

## Research Gaps
- Latent graph inference for larger spatial domains
- Heterogeneous GNNs for different node/edge types
- Integration with physics-based models (SOFS as input)
- Temporal Graph Networks for continuous-time modeling
