---
title: Regional Ocean Forecasting with Hierarchical Graph Neural Networks
arXiv: 2410.11807
authors:
- Daniel Holmberg
- University of Helsinki
- Emanuela Clementi
- CMCC Foundation
- Teemu Roos
- University of Helsinki
year: 2024
source: arXiv
venue: NeurIPS
difficulty: ★★★★☆
importance: ★★★★★
read_status: read
method_tags:
- graph_neural_network
- hierarchical_gnn
- regional_ocean_model
- neural_forecasting
- mediterranean_sea
application_tags:
- ocean_forecasting
- regional_ocean
- mediterranean_sea
- sst_forecasting
- marine_dynamics
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Regional Ocean Forecasting with Hierarchical Graph Neural Networks

## TL;DR
SeaCast uses hierarchical GNN with encode-process-decode architecture for Mediterranean Sea forecasting, matching operational Med-PHY accuracy at fraction of computational cost.

## Research Question
How can graph neural networks effectively handle complex irregular ocean grid geometries and atmospheric forcing for high-resolution regional ocean forecasting?

## Main Contributions
1. Proposes hierarchical GNN architecture (SeaCast) with 3 mesh levels and 4 processor layers for regional ocean forecasting
2. Adapts graph creation, training, and evaluation to accommodate irregular ocean grid geometry
3. Integrates relevant atmospheric forcing near sea surface with lateral boundary forcing for water inflow/outflow

## Method
Encode-process-decode GNN architecture operating on hierarchical mesh. 3 mesh levels (G0: 22,677 nodes, G1: 2,515 nodes, G2: 272 nodes). Interaction networks for edge updates. 5.6M trainable parameters. Predicts tendency (delta) rather than next state directly. Rollout masking for internal ocean grid only. Boundary forcing at Strait of Gibraltar. MSE loss with depth-dependent weighting. Training: 35 years reanalysis (1987-2021) + 2 years analysis (2022-2024), 200 epochs on 32 AMD MI250x GPUs.

## Datasets
- Mediterranean Sea Physics (Med-PHY) from Copernicus Marine Service
- 1/24 degree resolution (~4km), 18 vertical levels (surface to 200m)
- 7 physical variables: zonal/meridional velocity, salinity, temperature, SSH, mixed layer depth, bottom temperature
- 75 predicted fields total
- ERA5 atmospheric forcing (wind, temperature, pressure)
- Test period: July-August 2024

## Core Results
- SeaCast performs on par with operational Med-PHY for most variables
- ML models significantly outperform persistence baseline
- Analysis data initialization shows improved forecast skill
- Training took 2 days on 32 AMD MI250x GPUs
- Produces 15-day forecasts (extended from 10-day operational standard)
- SST forecasting shows favorable comparison with Med-PHY

## Limitations
- ML in ocean forecasting remains relatively nascent
- Limited to regional Mediterranean Sea application
- Only epipelagic zone (0-200m depth, 18 levels)
- Reanalysis lacks some operational model features (Dardanelles boundaries, tidal inputs, wave coupling)
- Fixed 3-level hierarchical graph may not optimal for all regions

## Research Gaps
- Extension to climate timescales (seasonal, decadal)
- Integration with coupled atmosphere-wave-biogeochemistry models
- Application to other regional seas and global ocean
- Probabilistic forecasting and ensemble methods
- Foundation models for ocean forecasting
