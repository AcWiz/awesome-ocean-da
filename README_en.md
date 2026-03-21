# AI + Ocean Data Assimilation Papers

[![Paper Count](https://img.shields.io/badge/Papers-92-blue)](./papers)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--03--21-green)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

[English](./README_en.md) | [简体中文](./README.md)

> This project is automatically maintained by GitHub Actions, collecting papers every 5 minutes

---

## About

A curated collection of academic papers on **AI/Deep Learning + Ocean Data Assimilation and Forecasting**, covering the latest research from arXiv, top conferences, and leading journals.

---

## Research Areas

- Ocean Data Assimilation
- Ocean Numerical Forecasting
- Sea Surface Temperature/Height Prediction (SST/SSH)
- Ocean Remote Sensing Data Assimilation
- Physics-Informed Neural Networks (PINNs) for Ocean
- Deep Learning for Ocean Modeling

---

## Publication Overview

| Category | Count | Percentage |
|----------|-------|------------|
| Top AI/ML Conferences (NeurIPS/ICML/ICLR/AAAI) | 8 | 9% |
| Top Ocean/Climate Journals (Nature Comm/JAMES/JCP/Ocean Modelling) | 12 | 13% |
| Other Peer-Reviewed (IEEE/EGU/TGRS) | 4 | 4% |
| arXiv Preprints | 68 | 74% |

---

## Yearly Trend

```
2026  ████████████████████                    19
2025  ████████████████████████████████████████ 37
2024  ████████████████████                    19
2023  ██████                                    6
2022  ██████                                    6
2021  ██                                        2
2015  █                                        1
2014  █                                        1
2012  █                                        1
```

---

## Top Conference & Journal Papers

| Paper | Venue | Year | Method |
|-------|-------|------|--------|
| Tensor-Var: Efficient 4D-Var | ICML 2025 | 2025 | 4D-Var, Neural-Operator |
| Semilinear Neural Operators | ICLR 2024 | 2024 | Neural-Operator |
| NeuralOM: Neural Ocean Model | AAAI 2026 (pending) | 2025 | Neural-Operator |
| Meta-Learning FNO for Hessian Inversion | NeurIPS 2025 (ML4PS) | 2025 | Neural-Operator, 4D-Var |
| Principled Operator Learning in Ocean Dynamics | NeurIPS 2025 (ML4PS) | 2025 | Neural-Operator |
| Advancing Ocean State Estimation | Nature Communications | 2025 | Hybrid |
| CGKN: Conditional Gaussian Koopman | J. Computational Physics | 2025 | Koopman, Neural-Operator |
| FuXi-DA: DL for satellite obs | npj Climate Atmos Sci | 2025 | Deep-Learning, Transformer |
| OceanCastNet Wave Forecasting | J. Advances Modeling Earth Sys | 2025 | Deep-Learning, GNN |
| Tropical Pacific Ocean DA | J. Advances Modeling Earth Sys | 2024 | EnKF |
| Deep Learning Enhanced DA | J. Computational Physics | 2023 | EnKF, Deep-Learning |
| 4D-SRDA | J. Advances Modeling Earth Sys | 2024 | 4D-Var |
| Validating DL Weather Forecast | AI for Earth Systems | 2025 | Deep-Learning |
| Discrete-Time Conditional Gaussian Koopman | CMAME | 2025 | Koopman, Neural-Operator |
| Observation-only learning neural mapping | IEEE TGRS | 2025 | 4D-Var |
| 4DVarNet-SSH | Geoscientific Model Dev | 2023 | 4D-Var |

---

## Methodology Distribution

| Method | Count |
|--------|-------|
| Deep-Learning | 24 |
| Hybrid | 20 |
| 4D-Var | 14 |
| PINN | 13 |
| Neural-Operator | 13 |
| EnKF | 11 |
| Koopman | 9 |
| GNN | 8 |
| Transformer | 6 |
| Surrogate | 4 |
| U-Net | 3 |
| Neural-Network | 2 |
| LSTM | 1 |
| Bayesian | 1 |
| ESN | 1 |

---

## Application Distribution

| Application | Count |
|-------------|-------|
| Ocean-DA (Ocean Data Assimilation) | 49 |
| Global-Forecast | 20 |
| Climate | 15 |
| Wave | 12 |
| Regional-Forecast | 12 |
| ENSO | 10 |
| SST (Sea Surface Temperature) | 10 |
| Submesoscale | 8 |
| Deep-Ocean | 7 |
| SSH (Sea Surface Height) | 5 |
| Carbon-Storage | 3 |
| Tidal | 2 |

---

## Features

- **Auto-Collection**: GitHub Actions collects papers from arXiv every 5 minutes
- **Multi-dimensional Tags**: Method types (PINN/Koopman/GNN) + Application scenarios (Global-Forecast/Regional-Forecast/ENSO)
- **Chinese Summaries**: Each paper includes Chinese summaries
- **Online Browse**: GitHub Pages with keyword search and tag filtering

---

## Quick Navigation

- [2026 Papers](./papers/2026/)
- [2025 Papers](./papers/2025/)
- [2024 Papers](./papers/2024/)
- [Browse by Method](#methodology-distribution)
- [Browse by Application](#application-distribution)

---

## Live Demo

GitHub Pages: https://AcWiz.github.io/ai-data-assimilation-papers

Features:
- Keyword search (title, author)
- Method type filtering (PINN, Koopman, GNN, etc.)
- Application filtering (Global-Forecast, Regional-Forecast, ENSO, etc.)
- Responsive design for mobile

---

## How to Contribute

Pull requests are welcome to add new papers!

### Submission Guidelines

1. **Scope**: AI/Deep Learning + Ocean Data Assimilation/Forecasting research
2. **Format**:
   - One directory per paper under the corresponding year
   - Must include `abstract.md` file
   - PDF is optional (gitignored)

### abstract.md Template

```markdown
---
title: "Paper Title"
arXiv: "2501.12345"
authors: ["Author1", "Author2"]
year: 2025
source: "arXiv"
method_tags: ["PINN", "Deep-Learning"]
application_tags: ["Global-Forecast", "Deep-Ocean"]
---

# Paper Title

## Basic Info

- **arXiv**: [2501.12345](https://arxiv.org/abs/2501.12345)
- **Authors**: Author1, Author2
- **Year**: 2025

## Summary

**Key Contribution**: Brief description of main contribution

**Method**: Main methods and techniques used

**Significance**: Impact and importance of the research

## Keywords

- Keyword1, Keyword2, ...
```

---

## Auto-Collection

This project uses GitHub Actions to automatically collect papers from arXiv every 5 minutes.

### Search Keywords

- data assimilation + neural network + ocean
- PINN + ocean
- Koopman + ocean
- neural operator + ocean
- graph neural network + ocean
- sea surface temperature/height + deep learning
- ENSO + deep learning

### Manual Trigger

Go to **Actions** -> **Collect Papers** -> **Run workflow** on the GitHub repository page.

---

## Project Structure

```
ai-data-assimilation-papers/
├── README.md              # This file (Chinese)
├── README_en.md           # English version
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE                # MIT License
│
├── _config.yml            # Jekyll config
├── index.md               # GitHub Pages home
├── _layouts/              # Jekyll templates
├── _includes/              # Reusable components
├── _data/                  # Paper index data
├── assets/                 # CSS, JS resources
│
├── scripts/                # Paper collection scripts
│   ├── collect_papers.py   # Main collection script
│   ├── search_strategy.py  # Search strategy config
│   ├── paper_schema.py     # Data model
│   ├── update_index.py     # Index update
│   └── requirements.txt    # Python dependencies
│
├── .github/
│   └── workflows/
│       └── collect.yml     # GitHub Actions workflow
│
└── papers/                 # Papers directory
    ├── 2022/
    ├── 2023/
    ├── 2024/
    ├── 2025/
    └── 2026/
        └── [paper-name]/
            ├── abstract.md    # Paper abstract with tags
            └── paper.pdf      # PDF file (optional)
```

---

## License

MIT License - See [LICENSE](LICENSE) file

---

*Last Updated: 2026-03-21*
