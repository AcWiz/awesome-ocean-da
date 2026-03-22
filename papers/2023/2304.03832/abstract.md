---
title: Deep Learning of Systematic Sea Ice Model Errors from Data Assimilation Increments
arXiv: 2304.03832
authors:
- William Gregory
- Mitchell Bushuk
- Alistair Adcroft
- Yongfei Zhang
- Laure Zanna
year: 2023
source: arXiv
venue: Journal of Advances in Modeling Earth Systems (JAMES)
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- CNN
- Data_Assimilation
- Sea_Ice
- Bias_Correction
- Model_Error_Learning
application_tags:
- Sea_Ice_Modeling
- Climate_Modeling
- SPEAR
- Bias_Prediction
- GFDL
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Deep Learning of Systematic Sea Ice Model Errors from Data Assimilation Increments

## TL;DR
CNN predicts sea ice data assimilation increments from model state variables, enabling potential bias correction parameterization in SPEAR climate model.

## Research Question
Can convolutional neural networks learn to predict state-dependent sea ice model errors from data assimilation increments to serve as a parameterization for reducing systematic biases?

## Main Contributions
1. Demonstrates sea ice DA increments closely reflect systematic bias patterns of global ice-ocean SPEAR model
2. Shows CNNs can make skillful predictions of sea ice concentration increments using only model state variables
3. Proposes CNN-based parameterization as tool to reduce sea ice biases in free-running climate simulations

## Method
CNN learns mapping from model state variables to analysis increments. SPEAR ice-ocean model assimilates satellite sea ice concentration every 5 days (1982-2017). CNN inputs: sea ice concentration, SST, ice velocities, ice thickness, net shortwave radiation, ice-surface skin temperature, sea-surface salinity, land-sea mask + tendencies. Prediction of sea ice concentration increments. Evaluation against climatological increment prediction baseline. Assessed across Arctic and Antarctic, all seasons.

## Datasets
- SPEAR (Seamless system for Prediction and EArth system Research) ice-ocean model at GFDL
- Sea ice concentration satellite observations assimilated every 5 days 1982-2017
- MOM6 ocean (75 vertical layers) + SIS2 sea ice model
- JRA55-do atmospheric forcing
- 1 degree nominal resolution

## Core Results
- CNN skillful predictions exceed climatological increment prediction baseline
- Skill consistent across Arctic and Antarctic and all seasons
- Sea ice DA increments closely reflect systematic SPEAR model bias patterns
- Temporal averaging of increments reveals clear seasonal and spatial bias structure
- Potential for online bias correction in free-running simulations

## Limitations
- Offline prediction evaluation only (not yet implemented as online parameterization)
- Single sea ice variable (concentration) - other variables not assessed
- Perfect model assumption may not fully capture real-world complexity
- Generalization to different model versions not tested

## Research Gaps
- Online implementation of CNN-based parameterization in SPEAR
- Extension to other sea ice variables (thickness, velocity) and ocean variables
- Uncertainty quantification for CNN predictions
- Application to operational sea ice forecasting
- Integration with coupled model bias correction frameworks
