---
title: A Langevinized Ensemble Kalman Filter for Large-Scale Static and Dynamic Learning
arXiv: 2105.05363v1
authors: Peiyi Zhang; Qifan Song; Faming Liang
year: 2021
source: arXiv
venue: arXiv preprint (stat.ME)
difficulty: ★★★★☆
importance: ★★★★☆
read_status: priority-read
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Equation-Free Surrogate Modeling of Geophysical Flows at the Intersection of Machine Learning and Data Assimilation

## TL;DR
Non-intrusive reduced-order modeling (NIROM) with POD and LSTM networks integrated with ensemble Kalman filter achieves one-order-of-magnitude prediction improvement for sea surface temperature.

## Research Question
How can data-driven reduced-order models trained on high-resolution simulations or satellite observations reduce computational burden while maintaining accuracy for data assimilation in geophysical flows?

## Main Contributions
1. Proposes end-to-end NIROM framework combining modal decomposition, LSTM time series prediction, optimal sensor placement, and sequential data assimilation
2. Integrates POD-based reduced-order model with deterministic ensemble Kalman filter (DEnKF) for improved state estimation
3. Achieves one-order-of-magnitude improvement in prediction accuracy through DEnKF correction

## Method
The framework uses proper orthogonal decomposition (POD) for dimensionality reduction and dominant mode identification, followed by LSTM networks for modeling dynamics of POD modes. Optimal sensor locations are determined via QR pivoting. The NIROM is integrated within DEnKF for sequential data assimilation, where latent observation space links real-time measurements with reduced-order state representations.

## Datasets
- NOAA Optimum Interpolation Sea Surface Temperature (SST) V2 dataset
- High-resolution simulation or satellite observation data

## Core Results
- NIROM stable for long-term forecasting with reasonable accuracy
- DEnKF improves prediction accuracy by almost one order of magnitude
- Framework effectively fuses information from large-scale Earth system models and diverse observations

## Limitations
- Performance depends on quality and representativeness of training data
- Optimal sensor placement may vary for different dynamical regimes

## Research Gaps
- Application to other geophysical flows beyond SST
- Extension to real-time operational forecasting systems
- Integration with more complex ocean-atmosphere coupled models