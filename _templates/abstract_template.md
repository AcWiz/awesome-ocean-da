---
title: '{{ title }}'
arXiv: '{{ arxiv_id }}'
authors:
{%- for author in authors %}
- {{ author }}
{%- endfor %}
year: {{ year }}
source: {{ source | default('arXiv') }}
venue: {{ venue | default('arXiv') }}
domain_tags:
{%- for tag in domain_tags %}
- {{ tag }}
{%- endfor %}
ocean_vars: {{ ocean_vars | default('Unknown') }}
spatiotemporal_res: {{ spatiotemporal_res | default('Unknown') }}
difficulty: {{ difficulty | default('★★★☆☆') }}
importance: {{ importance | default('★★★☆☆') }}
read_status: {{ read_status | default('skim') }}
---

# {{ title }}

## TL;DR

> 一句话总结本文的核心贡献（待补充）

## 研究问题

> 本文要解决什么问题？研究动机是什么？

## 核心贡献

> 3-5 个关键贡献点

1.
2.
3.

## 方法详解

> 核心方法的详细描述

## 数学/物理建模

> 关键公式和物理意义

## 实验分析

> 实验设置、结果和发现

## 优缺点

**优点：**
-

**缺点：**
-

## 工程落地

> 实际应用场景和可行性

## Idea 扩展

> 可以借鉴到其他研究的想法

## BibTeX

```bibtex
@article{},
  title={},
  author={},
  journal={},
  year={}
}
```
