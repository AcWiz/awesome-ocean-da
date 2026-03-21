# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **paper collection repository** for AI/Deep Learning + Ocean Data Assimilation and Forecasting research. It contains paper summaries (abstracts) organized by year, not source code.

## Repository Structure

```
papers/
├── [year]/                    # Year folders (2022, 2023, 2024, 2025)
│   └── [paper-name]/
│       └── abstract.md         # Required: paper summary in Chinese
└── README.md                   # Paper index organized by year
```

## Adding a New Paper

1. Create folder: `papers/[year]/[paper-short-name]/`
2. Add `abstract.md` with the following frontmatter:
   ```markdown
   # [Paper Title]

   ## 基本信息
   - **arXiv**: [link]
   - **作者**: author list
   - **年份**: year

   ## 中文总结
   **核心贡献**: brief description
   **主要方法**: main methods used
   **意义**: significance

   ## 关键词
   - keyword1, keyword2, ...
   ```
3. Update `papers/README.md` with the new paper entry
4. Update root `README.md` with the new paper entry

## Gitignore

PDF files are excluded from version control (`*.pdf` in `.gitignore`).

## Key Files

- `README.md` - Main paper list organized by year
- `papers/README.md` - Detailed paper index with keywords
- `CONTRIBUTING.md` - Contribution guidelines and abstract template
