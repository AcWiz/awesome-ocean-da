---
title: FEM-PIKFNNs for Underwater Acoustic Propagation Induced by Structural Vibrations in Different Ocean Environments
arXiv: 2308.09956
authors:
- Qiang Xi
- Zhuojia Fu
- Wenzhi Xu
- Mi-An Xue
- Jinhai Zheng
year: 2023
source: arXiv
venue: arXiv
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- FEM
- PIKFNN
- Physics-Informed_Neural_Network
- Kernel_Function
- Finite_Element_Method
application_tags:
- Underwater_Acoustic_Propagation
- Structural_Vibration
- Ocean_Acoustics
- Unbounded_Ocean
- Deep_Ocean
- Shallow_Ocean
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Prediction of Sea Ice Velocity and Concentration in the Arctic Ocean using Physics-informed Neural Network

## TL;DR
PINN-based HIS-Unet architecture outperforms fully data-driven models for Arctic sea ice prediction, especially with limited training data and in melting/freezing seasons.

## Research Question
How can physics-informed neural networks overcome limitations of fully data-driven models for Arctic sea ice prediction under rapidly changing climate conditions?

## Main Contributions
1. Develops physics-informed neural network (PINN) strategy integrating physical knowledge into sea ice prediction
2. Modifies HIS-Unet architecture with physics loss function and activation functions for physically plausible outputs
3. Demonstrates improved sea ice concentration predictions in melting and early freezing seasons and near fast-moving ice regions

## Method
The PINN model is based on Hierarchical Information-sharing U-net (HIS-Unet) architecture with incorporated physics loss function and modified activation functions. Physics constraints enforce physically valid sea ice concentration values (0-100%) and momentum conservation. Training uses physics-informed loss combining data fidelity with physical law residuals, enabling improved predictions even with small training datasets.

## Datasets
- Arctic Ocean sea ice data for model training and validation
- Sea ice velocity (SIV) and sea ice concentration (SIC) observations

## Core Results
- Outperforms fully data-driven models in daily SIV and SIC predictions
- Better performance with limited training samples
- Improved SIC predictions during melting and early freezing seasons
- Better predictions near fast-moving ice regions

## Limitations
- Validated primarily for Arctic Ocean conditions
- Performance depends on accuracy of physics constraints imposed
- May need retraining as Arctic conditions continue to change

## Research Gaps
- Extension to Antarctic sea ice predictions
- Integration with operational sea ice forecasting systems
- Application to longer-term climate projections