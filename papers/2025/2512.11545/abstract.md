---
title: Graph Embedding with Mel-spectrograms for Underwater Acoustic Target Recognition
arXiv: 2512.11545
authors:
- Sheng Feng
- Shuqing Ma
- Xiaoqian Zhu
year: 2025
source: arXiv
venue: IEEE
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- graph_neural_network
- Transformer
- Mel_spectrogram
- non_Euclidean
- underwater_acoustics
application_tags:
- underwater_target_recognition
- sonar
- ship_classification
- acoustic_signal_processing
- model_interpretability
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Graph Embedding with Mel-spectrograms for Underwater Acoustic Target Recognition

## TL;DR
UATR-GTransformer integrates Transformer with GNN for underwater acoustic target recognition, modeling Mel-spectrograms as graphs for non-Euclidean feature extraction.

## Research Question
How can graph neural networks combined with Transformer architectures effectively handle the non-Euclidean structure of underwater acoustic signals for target recognition?

## Main Contributions
1. Proposes UATR-GTransformer, first work to introduce graph structures into underwater acoustic target recognition (UATR)
2. Integrates Transformer Encoder with GNN to capture both global dependencies and local neighborhood relationships in Mel-spectrograms
3. Achieves competitive performance with state-of-the-art methods while providing interpretability through attention and graph visualization

## Method
Three-component architecture: Mel patchify block, GTransformer block, classification head. Mel patchify converts acoustic signals to Mel-spectrogram and partitions into overlapping patches. GTransformer block uses Transformer Encoder to capture mutual information between split patches, generating Mel-graph embeddings. Each embedding treated as graph node with edges defined by node relationships. GNN enhances embeddings by modeling local neighborhood structure. FFN performs final feature transformation. Non-Euclidean framework explicitly incorporates spatial information from acoustic features. Hinich test validates non-Gaussian and non-linear characteristics of underwater signals.

## Datasets
- ShipsEar dataset (underwater acoustic ship-radiated noise)
- 20-second samples at 52374 Hz sampling rate
- Segmented into 40 intervals of 0.5s each
- Two widely used benchmark datasets for UATR

## Core Results
- Competitive performance with state-of-the-art UATR methods
- Effective extraction of rich frequency-domain information
- Graph modeling captures topological characteristics of acoustic signals
- Interpretable predictions via attention visualization
- Outperforms methods assuming Euclidean data structure

## Limitations
- Performance validation limited to benchmark datasets
- Real-world deployment not tested
- Computational cost of graph construction not characterized
- Fixed patch size may not optimal for all target types

## Research Gaps
- Extension to real-ocean operational environments
- Adaptive graph construction strategies
- Multi-target recognition in complex acoustic scenes
- Integration with passive sonar systems
- Graph-based approaches for other underwater acoustic tasks
