# 投稿指南

欢迎提交新的论文到本项目！

## 快速开始

### 1. Fork 本仓库

点击 GitHub 页面右上角的 **Fork** 按钮。

### 2. 克隆你的 Fork

```bash
git clone https://github.com/[你的用户名]/ai-data-assimilation-papers.git
cd ai-data-assimilation-papers
```

### 3. 创建论文目录

```bash
# 根据论文的 arXiv ID 确定年份
# 例如 arXiv ID 2503.19160 → 年份 2025
mkdir -p papers/2025/paper-short-name/
```

### 4. 填写 abstract.md

从模板复制并填写：[_templates/abstract_template.md](_templates/abstract_template.md)

### 5. 提交 PR

```bash
git checkout -b feat/add-paper-[arxiv-id]
git add papers/2025/paper-short-name/
git commit -m "feat: 添加 [论文简称] (arXiv: XXXX.XXXXX)"
git push origin feat/add-paper-[arxiv-id]
```

然后在 GitHub 上创建 Pull Request。

---

## 投稿要求

### 论文范围

- AI/深度学习与海洋数据同化、预报相关研究
- 优先收录：有开源代码、实验充分的论文

### 必需文件

每篇论文一个目录，放在对应年份下（如 `papers/2025/paper-name/`）：

```
papers/[年份]/[论文简称]/
├── abstract.md    # 必须：论文摘要和总结（中文）
└── summary.md    # 必须：与 abstract.md 内容一致
```

### arXiv ID 要求

> **重要**：`arXiv` 是 **必填字段**。如果论文尚未发布在 arXiv 上，请先搜索确认。

- 优先通过 [arXiv](https://arxiv.org) 检索论文
- 如果论文有正式期刊发表但未上 arXiv，请注明 DOI
- 确实无法获取 arXiv ID 的论文，需在 PR 中说明原因

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
- arXiv ID 格式必须正确（如 `2503.19160`）

---

## 常见问题

### Q: 如何确定论文的年份？

根据 arXiv ID 推断：`YYMM.XXXXX` → 年份。例如 `2503.19160` 表示 2025 年 3 月。

### Q: 论文暂时没有 arXiv ID 怎么办？

请先尝试在 arXiv 搜索论文。如果确实没有，可以提交但需要在 PR 中说明。后续需要补充有效的 arXiv ID。

### Q: method_tags 和 application_tags 如何选择？

请根据论文的**主要贡献**选择 1-3 个最相关的标签。具体标签含义请参见下文的标签说明。

### Q: 可以直接上传 PDF 吗？

PDF 文件已被 `.gitignore` 排除，不会上传到仓库。如果需要上传 PDF，请使用 [PDF上传工具](https://github.com/[your-repo]/paper-uploader)。

### Q: 如何更新已存在的论文？

请同样提交 PR，标注是 `fix` 类型，并说明修改原因。

### Q: 提交后发现内容有误怎么办？

在原 PR 中追加修改，或提交新的 PR 进行修正。

---

## 相关资源

- [论文模板下载](./_templates/abstract_template.md)
- [PR 模板](./.github/PULL_REQUEST_TEMPLATE.md)
- [问题反馈](https://github.com/[owner]/ai-data-assimilation-papers/issues/new/choose)
