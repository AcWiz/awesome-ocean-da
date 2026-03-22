---
title: SST: Multi-Scale Hybrid Mamba-Transformer Experts for Time Series Forecasting
arXiv: 2404.14757
authors:
- Xiongxiao Xu
- Illinois Institute of Technology
- Canyu Chen
- Illinois Institute of Technology
- Yueqing Liang
- Illinois Institute of Technology
- Baixiang Huang
- Emory University
- Guangji Bai
- Emory University
- Liang Zhao
- Emory University
- Kai Shu
- Emory University
year: 2024
source: arXiv
venue: CIKM
difficulty: ★★★★☆
importance: ★★★★☆
read_status: read
method_tags:
- mamba
- transformer
- mixture_of_experts
- multi_scale
- state_space_model
- time_series
application_tags:
- time_series_forecasting
- weather_prediction
- traffic_prediction
- energy_forecasting
- sst_forecasting
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# SST: Multi-Scale Hybrid Mamba-Transformer Experts for Time Series Forecasting

## TL;DR
State Space Transformer combines Mamba for long-term patterns with Transformer for short-term variations, achieving SOTA with O(L) complexity.

## Research Question
How can hybrid Mamba-Transformer architectures effectively combine linear-complexity state space models with attention mechanisms for time series forecasting?

## Main Contributions
1. Identifies information interference problem when naively stacking Mamba and Transformer layers
2. Proposes time series decomposition separating long-range patterns (Mamba) from short-range variations (Transformer)
3. Achieves SOTA performance on 7 real-world datasets with linear O(L) complexity

## Method
Multi-scale hybrid architecture with three components: (1) Multi-scale Patcher adjusts resolution - low resolution (large patches) for long-range patterns, high resolution (small patches) for short-range variations. (2) Mamba expert processes coarse-grained long-range series for pattern extraction. (3) Local Window Transformer (LWT) captures fine-grained short-term variations with reduced O(w*S) complexity. (4) Long-short router adaptively fuses expert outputs. Multi-scale patching with patch length 48/stride 16 for long range, patch 16/stride 8 for short range.

## Datasets
- ETTh1&ETTh2, ETTm1&ETTm2 (electricity transformers)
- Weather (local weather)
- ECL (electricity consumption)
- Traffic (traffic flow)
- 7 variates to 862 variates across datasets

## Core Results
- Outperforms Mamba-based (TimeMachine, S-Mamba, SiMBA) and Transformer-based (iTransformer, PatchTST) methods
- ETTm1 F=720: MSE 0.429 vs S-Mamba 0.488, 13.75% improvement
- Linear complexity O(L) scales to 6k time steps vs Transformer O(L^2) limited to 336
- Memory efficient: SST 6480 steps vs PatchTST 3240 vs vanilla Transformer 336

## Limitations
- Performance depends on appropriate decomposition of patterns vs variations
- Fixed multi-scale resolution may not suit all time series types
- Validated primarily on univariate time series forecasting tasks

## Research Gaps
- Application to multivariate and spatio-temporal forecasting
- Extension to time series classification and anomaly detection
- Adaptive determination of pattern/variation decomposition
