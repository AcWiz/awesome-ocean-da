---
title: "SamudrACE: Fast and Accurate Coupled Climate Modeling with 3D Ocean and Atmosphere Emulators"
arXiv: "2509.12490"
authors: ["James P. C. Duncan", "Elynn Wu", "Surya Dheeshjith", "Adam Subel", "Troy Arcomano", "Spencer K. Clark", "Brian Henn", "Anna Kwa", "Jeremy McGibbon", "W. Andre Perkins", "William Gregory", "Carlos Fernandez-Granda", "Julius Busecke", "Oliver Watt-Meyer", "William J. Hurlin", "Alistair Adcroft", "Laure Zanna", "Christopher Bretherton"]
year: 2025
source: "arXiv"
venue: "arXiv"
method_tags: ["Climate Modeling", "Ocean Emulator", "Atmosphere Emulator", "Coupled Modeling", "Machine Learning"]
application_tags: ["Climate Modeling", "ENSO", "Ocean-Atmosphere Coupling", "Weather Prediction"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# SamudrACE: Fast and Accurate Coupled Climate Modeling with 3D Ocean and Atmosphere Emulators

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2509.12490
- **作者**: James P. C. Duncan et al.
- **开源代码**: None

## 2. 一句话总结（TL;DR）
本文提出 SamudrACE，一个耦合全球气候模型 emulator，能够以 1 度水平分辨率、6 小时间隔大气和 5 天间隔海洋产生长达数百年的模拟。

## 3. 研究问题（Problem Definition）
**核心问题**：传统数值全球气候模型需要通过单独的模拟器交换边界条件来模拟完整地球系统，计算成本高昂。

**研究背景**：
- 传统方法将大气、海洋、海冰、陆面等作为独立模拟器
- 通过 coupler 在各领域之间进行空间/时间对齐和通量交换
- 机器学习 emulator 提供了加速可能

**关键挑战**：
1. 如何将机器学习 emulator 适配到耦合建模框架
2. 保证长期模拟的稳定性
3. 保持与完整数值模型相当的精度

## 4. 核心贡献（Contributions）
1. **SamudrACE 系统**：耦合全球气候模型 emulator
2. **高分辨率长周期模拟**：百年尺度模拟，1 度水平分辨率
3. **多变量输出**：145 个 2D 场，8 个大气层和 19 个海洋层
4. **气候可靠性**：低气候偏差，ENSO 等耦合气候现象的真实变率

## 5. 方法详解（Methodology）

### 5.1 耦合建模框架
- 遵循传统数值模型的耦合范式
- 针对机器学习 emulator 进行了适配
- 保留 coupler 处理领域间转换的功能

### 5.2 分辨率规格
- **水平分辨率**: 1 度
- **大气时间分辨率**: 6 小时间隔
- **海洋时间分辨率**: 5 天间隔

### 5.3 输出变量
- 145 个 2D 场
- 8 个大气垂直层
- 19 个海洋垂直层
- 海冰、表面和大气顶变量

## 6. 实验分析（Experiments）

**稳定性**：
- 高度稳定的长周期模拟
- 可运行数百年

**精度**：
- 气候偏差低
- 与边界强迫下的组件模型相当

**变率**：
- ENSO 等耦合气候现象的真实变率
- 在非耦合模式下无法实现的模拟能力
