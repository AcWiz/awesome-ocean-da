---
title: "Sub-seasonal forecasting with a large ensemble of deep-learning weather prediction models"
arXiv: "2102.05107"
authors: ['Jonathan A. Weyn', 'Dale R. Durran', 'Rich Caruana', 'Nathaniel Cresswell-Clay']
year: 2021
source: "arXiv"
venue: "Journal of Advances in Modeling Earth Systems"
method_tags: []
application_tags: []
---

# Sub-seasonal forecasting with a large ensemble of deep-learning weather prediction models

## 基本信息
- **论文链接**: https://arxiv.org/abs/2102.05107
- **作者**: Jonathan A. Weyn, Dale R. Durran, Rich Caruana, Nathaniel Cresswell-Clay

## 摘要
hour time resolution. This model uses convolutional neural networks (CNNs) on a cubed sphere grid to produce global forecasts. The approach is computationally efficient, requiring just three minutes on a single GPU to produce a 320-member set of six-week forecasts at 1.4° resolution. Ensemble spread is primarily produced by randomizing the CNN training process to create a set of 32 DLWP models with slightly different learned weights. Although our DLWP model does not forecast precipitation, it does forecast total column water vapor, and it gives a reasonable 4.5-day deterministic forecast of Hurricane Irma. In addition to simulating mid-latitude weather systems, it spontaneously generates tropical cyclones in a one-year free-running simulation. Averaged globally and over a two-year test set, the ensemble mean RMSE retains skill relative to climatology beyond two-weeks, with anomaly correlation coefficients remaining above 0.6 through six days. Our primary application is to subseasonal-to-seasonal (S2S) forecasting at lead times from two to six weeks. Current forecast systems have low skill in predicting one- or 2-week-average weather patterns at S2S time scales. The continuous ranked probability score (CRPS) and the ranked probability skill score (RPSS) show that the DLWP ensemble is only modestly inferior in performance to the European Centre for Medium Range Weather Forecasts (ECMWF) S2S ensemble over land at lead times of 4 and 5-6 weeks. At shorter lead times, the ECMWF ensemble performs better than DLWP.
