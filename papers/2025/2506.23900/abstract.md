---
title: SeaCast: Accurate Mediterranean Sea Forecasting via Graph-Based Deep Learning
arXiv: 2506.23900
authors:
- Daniel Holmberg
- Emanuela Clementi
- Italo Epicoco
- Teemu Roos
year: 2025
source: arXiv
venue: Nature
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- GNN
- graph_neural_network
- hierarchical_mesh
- regional_ocean
- autoregressive
application_tags:
- Mediterranean_Sea
- ocean_forecasting
- SST
- SSH
- temperature
- salinity
- currents
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Accurate Mediterranean Sea Forecasting via Graph-based Deep Learning

## TL;DR
SeaCast outperforms operational MedFS model across all ocean variables using GNN-based forecasting, achieving 15-day predictions in 20 seconds on single GPU.

## Research Question
How can graph neural networks achieve superior regional ocean forecasting compared to operational numerical models while maintaining computational efficiency?

## Main Contributions
1. Proposes SeaCast, a hierarchical GNN achieving consistent improvement over MedFS operational system across all 73 predicted ocean fields
2. Demonstrates 15-day forecasting capability (vs 10-day operational standard) with comparable or better accuracy
3. Shows data-driven atmospheric forcing (AIFS) achieves better skill than numerical ENS forcing at extended lead times

## Method
Hierarchical graph neural network with encode-process-decode architecture on 3-level mesh (22,677/2,515/272 nodes). 17.7M parameters. Predicts tendency (delta) rather than next state directly. Atmospheric forcing: wind stress, 2m temperature, MSLP, with seasonal sine/cosine encoding. Lateral boundary forcing at Strait of Gibraltar and Dardanelles. Depth-weighted MSE loss. Training: 35 years reanalysis (1987-2021) + fine-tuning on 2 years analysis (2022-2023). 64 AMD MI250x GPUs, 24 hours total training.

## Datasets
- Mediterranean Sea Physics from CMEMS (Med-PHY operational + reanalysis)
- 1/24 degree resolution, 18 depth levels (surface to 200m)
- 7 variables: zonal/meridional velocity, salinity, temperature, SSH, mixed layer depth, bottom temperature
- 73 predicted fields, 79 input dimensions including static features
- ERA5 atmospheric forcing, AIFS and ENS for testing
- Test: July-December 2024 initialization period

## Core Results
- SeaCast outperforms MedFS across all variables and depths
- Improvements increase at longer lead times
- Wind stress is dominant atmospheric driver for currents and salinity
- 10-year training data sufficient for currents/temperature, 35-year needed for salinity/SLA
- Fine-tuning consistently improves performance
- AIFS forcing outperforms ENS at extended lead times
- 20 second inference on single GPU vs 70 minutes for MedFS on 89 CPU cores

## Limitations
- Limited to Mediterranean regional sea
- Epipelagic zone only (0-200m, 18 levels)
- Deterministic forecasts only (no uncertainty quantification)
- Fixed hierarchical graph structure
- Training on simulation data may not capture all real-world phenomena

## Research Gaps
- Extension to other regional seas and global ocean
- Probabilistic/ensemble forecasting
- Integration with coupled wave-biogeochemistry models
- Higher temporal resolution training data (6-hourly)
- Foundation models for ocean forecasting
- Real-time operational deployment validation
