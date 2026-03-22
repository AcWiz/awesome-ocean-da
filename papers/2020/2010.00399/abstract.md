---
title: Analyzing Koopman approaches to physics-informed machine learning for long-term sea-surface temperature forecasting
arXiv: 2010.00399v2
authors: Julian Rice; Wenwei Xu; Andrew August
year: 2020
source: arXiv
venue: arXiv preprint
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: priority-read
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Analyzing Koopman Approaches to Physics-informed Machine Learning for Long-term Sea-Surface Temperature Forecasting

## TL;DR
Koopman-based methods outperform baselines for Gulf of Mexico SST prediction up to 180 days using convolutional autoencoder and consistent Koopman approaches.

## Research Question
How can Koopman operator theory enable accurate sea-surface temperature forecasting weeks to months into the future?

## Main Contributions
1. Evaluates combination of basic Koopman method with convolutional autoencoder for long-range SST forecasting
2. Proposes and evaluates "consistent Koopman" method for improved SST predictions
3. Demonstrates accurate prediction up to 180 days in Gulf of Mexico using only present thermal image and 3 years historical data

## Method
Koopman operator theory provides linear embedding of nonlinear SST dynamics in infinite-dimensional space. The approach combines convolutional autoencoder for measurement functions with Koopman-based prediction. Models predict SST up to 180 days from a single present thermal image, trained on three years of historical data. Methods evaluated include basic Koopman and consistent Koopman variants.

## Datasets
- Gulf of Mexico sea surface temperature
- 3 years historical training data
- 180-day prediction horizon

## Core Results
- Koopman approach consistently outperforms baselines
- Accurate SST prediction up to 180 days demonstrated
- Loop Current and eddy shedding dynamics captured

## Limitations
- Validated primarily for Gulf of Mexico region
- Performance depends on quality and length of training data
- May struggle with extreme events not well represented in training

## Research Gaps
- Extension to other ocean basins and variables
- Integration with numerical weather prediction models
- Application to climate-scale predictions