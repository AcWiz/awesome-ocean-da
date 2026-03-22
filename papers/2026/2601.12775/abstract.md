---
title: Eddy-Resolving Global Ocean Forecasting with Multi-Scale Graph Neural Networks
arXiv: 2601.12775
authors:
- Yuta Hirabayashi
- Daisuke Matsuoka
- Konobu Kimura
year: 2026
source: arXiv
venue: ICML
difficulty: ★★★★★
importance: ★★★★★
read_status: deep_read
method_tags:
- GNN
- graph_neural_network
- multi_scale
- spherical_mesh
- eddy_resolving
application_tags:
- global_ocean
- eddy
- forecasting
- ocean_circulation
- ocean_state_prediction
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Eddy-Resolving Global Ocean Forecasting with Multi-Scale Graph Neural Networks

## TL;DR
Multi-scale GNN with two spherical meshes enables 10-day eddy-resolving global ocean forecasting at 1/12 degree, improving representation across wide spatial scales.

## Research Question
How can multi-scale graph neural networks effectively represent the broad range of spatial scales in eddy-resolving global ocean forecasting?

## Main Contributions
1. Proposes multi-scale GNN using two spherical meshes for 10-day eddy-resolving global ocean forecasts at 1/12 degree
2. Improves representation of multi-scale ocean dynamics and short-term variability through multi-resolution design
3. Incorporates surface atmospheric variables with ocean state variables to enhance short-term prediction accuracy

## Method
Encoder-processor-decoder architecture on two spherical meshes (finest and second-finest resolutions). Land nodes excluded from graph for computational efficiency and physical relevance. Message passing with MLPs and residual connections. 16 message passing iterations. Embedding dimension 192. Node features: ocean state variables (Xt-1, Xt), atmospheric forcing (At-1, At, At+1), static data (latitude, longitude, depth). Edge features from relative positions. Multi-scale design captures mesoscale eddies to basin-scale western boundary currents. Autoregressive 10-day forecasting (1-day steps). Surface kinetic energy spectra for scale evaluation.

## Datasets
- GLORYS12V1 global ocean reanalysis (ocean state variables)
- 23 vertical levels (0.49m to 643.57m depth)
- Atmospheric forcing at ocean surface
- 1/12 degree eddy-resolving resolution
- Comparison against Swin Transformer-based architecture (Wang et al. 2024)

## Core Results
- Accurate representation of broad range of spatial scales (mesoscale to basin-scale)
- Improved short-term prediction skill vs Swin Transformer baseline
- Higher skill at multiple spatial scales confirmed by kinetic energy spectra analysis
- Atmospheric forcing improves surface layer short-term forecasts
- Multi-scale design better captures ocean variability vs single-resolution approaches

## Limitations
- 10-day forecast horizon (not extended to climate timescales)
- Surface variables only for atmospheric forcing impact
- Single architecture comparison (vs Swin Transformer only)
- Land node exclusion may affect coastal dynamics
- Training on reanalysis may not capture all observational characteristics

## Research Gaps
- Extension to longer forecast horizons
- Integration with deep ocean variables
- Multi-scale temporal dependencies
- Coupling with atmospheric and wave models
- Real-time operational validation
- Ensemble forecasting approaches
