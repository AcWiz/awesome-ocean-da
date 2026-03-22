---
title: Watching Swarm Dynamics from Above: A Framework for Advanced Object Tracking in Drone Videos
arXiv: 2406.07680
authors:
- Duc Pham
- Technical University Berlin
- Matthew Hansen
- Leibniz Institute for Freshwater Ecology and Inland Fisheries
- Félicie Dhellemmes
- Univ. Grenoble Alpes
- Inria
- CNRS
- Grenoble INP
- LJK
- Jens Krause
- Leibniz Institute for Freshwater Ecology and Inland Fisheries
- Pia Bideau
- Univ. Grenoble Alpes
- Inria
- CNRS
- Grenoble INP
- LJK
year: 2024
source: arXiv
venue: Nature
difficulty: ★★★☆☆
importance: ★★★★★
read_status: read
method_tags:
- particle_filter
- semantic_segmentation
- deeplabv3
- kalman_filter
- visual_tracking
application_tags:
- animal_tracking
- collective_behavior
- fish_school
- drone_videos
- marine_ecology
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Accurate Mediterranean Sea Forecasting via Graph-Based Deep Learning

## TL;DR
SeaCast GNN model outperforms operational MedFS system for Mediterranean Sea forecasting, delivering 15-day forecasts in 20 seconds on single GPU.

## Research Question
How can graph neural networks achieve accurate high-resolution regional ocean forecasting that outperforms physics-based numerical models while maintaining computational efficiency?

## Main Contributions
1. Develops SeaCast, first DL-based regional ocean forecasting system for Mediterranean Sea outperforming operational MedFS
2. Achieves 15-day forecasts at 1/24 degree resolution across 18 depth levels, outputting 73 predicted fields
3. Demonstrates 210x computational speedup (20s vs 70 minutes) compared to MedFS with improved forecast skill

## Method
Hierarchical GNN with encode-process-decode architecture on custom Mediterranean mesh. Input: 2-day ocean state + atmospheric forcing (wind stress, 2m temperature, MSLP). Predicts tendency (residual update) rather than direct state. Dynamic boundary conditions at Gibraltar and Dardanelles. Trained on 35 years GLORYS reanalysis (1987-2021) with 2-year fine-tuning (2022-2023). Autoregressive inference.

## Datasets
- Mediterranean Sea physics reanalysis (1/24 degree, 141 vertical levels, 1987-2021)
- Copernicus MedFS analysis (2022-2023) for fine-tuning
- ERA5 atmospheric forcing and AIFS/ENS forecasts
- L3 satellite SST and along-track altimeter SLA for validation

## Core Results
- SeaCast outperforms MedFS across all variables (zonal/meridional currents, salinity, temperature, SST, SLA)
- Improvements increase with lead time; largest gains in Alboran Sea and Aegean Sea
- Wind stress identified as dominant atmospheric forcing for all ocean variables
- 10-year training sufficient for currents and temperature competitive with MedFS
- HSS for SST extreme detection: 0.45-0.65 (vs MedFS 0.50-0.60)

## Limitations
- Lateral boundary forcing relies on MedFS data
- 10-year training insufficient for salinity and SLA
- Single GPU training not feasible for this configuration (requires 64 GPUs)
- Performance degrades at deepest levels (192m)

## Research Gaps
- Coupling with global ocean and atmospheric forecasts for extended lead times
- Integration of biogeochemical and wave dynamics
- Probabilistic forecasting with ensemble methods
- Continuous-time neural ocean modeling
