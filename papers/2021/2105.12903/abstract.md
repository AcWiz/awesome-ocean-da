---
title: Neural Enhanced Belief Propagation for Cooperative Localization
arXiv: 2105.12903v1
authors:
- Mingchao Liang
- Florian Meyer
year: 2021
source: arXiv
venue: arXiv preprint
difficulty: ★★★★☆
importance: ★★★☆☆
read_status: skim
method_tags:
- Belief Propagation
- Graph Neural Network
- Neural Enhanced BP
- Particle Filtering
application_tags:
- Cooperative Localization
- Wireless Networks
- Agent Networks
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Neural Enhanced Belief Propagation for Cooperative Localization

## TL;DR
GNN-enhanced belief propagation combines model-based and data-driven inference for wireless agent network localization with consistent estimates.

## Research Question
How can graph neural networks enhance belief propagation to overcome overconfident estimates in cooperative localization for wireless agent networks?

## Main Contributions
1. Extends neural enhanced belief propagation (NEBP) to continuous random variables via particle-based representation
2. Combines BP with learned GNN messages to correct errors from graph cycles and model mismatch
3. Achieves consistent (well-calibrated) estimates without explicitly addressing overconfidence in loss function

## Method
Particle-based belief propagation for continuous states. GNN learns to complement BP messages via message passing neural network (MPNN). Node embeddings initialized from sample mean and covariance. GNN messages combined with BP messages via learned scalar and vector functions (gs, gv). MLP architectures with single hidden layer, Leaky ReLU activations. L1 loss on position estimates for training.

## Datasets
- Synthetic cooperative localization with 25 agents (training) and 100 mobile agents with 13 anchors (testing)
- 2D constant-velocity motion model with drag and Gaussian driving noise
- Range measurements with Gaussian noise (sigma=1)
- 50 time steps per trajectory, 100 realizations for training, 400 for testing
- Connectivity radius 20m for neighbor detection

## Core Results
- NEBP significantly reduces outage probability compared to BP
- At 95% confidence level, only 5% of NEBP estimates inconsistent vs 40% for BP
- Improved estimation accuracy with consistent (well-calibrated) belief estimates
- Generalizes to larger networks without retraining
- Computational complexity remains comparable to BP (constant factor overhead)

## Limitations
- Static anchor configuration (5 anchors in training, 13 in testing)
- Range-only measurements (no bearing information)
- Single motion model (constant-velocity with drag)
- Assumes Gaussian measurement noise
- Fixed connectivity threshold (20m)

## Research Gaps
- Extension to bearing-only measurements
- Adaptive mobility models
- Non-Gaussian noise scenarios
- Integration with practical ranging technologies (UWB, WiFi)
- Online learning for changing network topologies
