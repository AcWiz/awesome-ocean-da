# 投稿指南

欢迎提交新的论文到本项目！

## 投稿要求

1. **论文范围**：AI/深度学习与海洋数据同化、预报相关研究
2. **文件格式**：
   - 每篇论文一个目录，放在对应年份下（如 `papers/2025/paper-name/`）
   - 必须包含 `abstract.md` 文件
   - PDF 文件可选（已在 `.gitignore` 中排除）

## 目录结构

```
papers/[年份]/[论文简称]/
└── abstract.md    # 必须：论文摘要和总结
```

## abstract.md 模板

```markdown
---
title: "论文标题"
arXiv: "2501.12345"
authors: ["作者1", "作者2"]
year: 2025
source: "arXiv"
venue: "arXiv"
method_tags: ["PINN", "Deep-Learning"]
application_tags: ["SST", "Global-Forecast"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# 论文标题

## 基本信息

- **arXiv**: [2501.12345](https://arxiv.org/abs/2501.12345)
- **作者**: 作者1, 作者2
- **年份**: 2025

## TL;DR

> 一句话总结本文的核心贡献

## 研究问题

> 本文要解决什么问题？研究动机是什么？

## 核心贡献

> 3-5 个关键贡献点

## 方法详解

> 核心方法的详细描述

## 实验分析

> 实验设置、结果和发现

## 优缺点

**优点：**
-

**缺点：**
-
```

详细模板请参考 [_templates/abstract_template.md](_templates/abstract_template.md)

## 标签说明

### 方法标签 (method_tags)

- `PINN` - 物理信息神经网络
- `Koopman` - Koopman 学习
- `Neural-Operator` - 神经算子（包含 FNO）
- `GNN` - 图神经网络
- `4D-Var` - 变分方法
- `EnKF` - 集合卡尔曼滤波
- `Transformer` - Transformer/Attention
- `Deep-Learning` - 通用深度学习
- `Physics-Informed` - 物理约束

### 应用标签 (application_tags)

- `SST` - 海表温度
- `SSH` - 海表高度
- `ENSO` - ENSO 预测
- `Wave` - 海浪预报
- `Global-Forecast` - 全球预报
- `Regional-Forecast` - 区域预报
- `Ocean-DA` - 海洋数据同化
- `Deep-Ocean` - 深海
- `Climate` - 气候

## 更新索引

提交 PR 时，请同时更新：

1. `papers/README.md` - 添加到对应年份的论文列表
2. 根目录 `README.md` - 如果需要，按方法或应用分类添加链接

## 审核标准

- 论文必须与 AI/深度学习 + 海洋数据同化/预报相关
- `abstract.md` 必须包含中文总结
- 标签需要准确反映论文的方法和应用
