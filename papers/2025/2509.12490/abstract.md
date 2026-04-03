---
title: 'SamudrACE: Fast and Accurate Coupled Climate Modeling with 3D Ocean and Atmosphere
  Emulators'
arXiv: '2509.12490'
authors: [James P. C. Duncan, Elynn Wu, Surya Dheeshjith, Adam Subel, Troy Arcomano,
  Spencer K. Clark, Brian Henn, Anna Kwa, Jeremy McGibbon, W. Andre Perkins, William
    Gregory, Carlos Fernandez-Granda, Julius Busecke, Oliver Watt-Meyer, William J.
    Hurlin, Alistair Adcroft, Laure Zanna, Christopher Bretherton]
year: 2025
source: arXiv
venue: arXiv
method_tags: [Climate_Modeling, Ocean_Emulator, Atmosphere_Emulator, Coupled_Modeling,
  Machine_Learning]
application_tags: [Climate_Modeling, ENSO, Ocean_Atmosphere_Coupling, Weather_Prediction]
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: skim
---

# SamudrACE: Fast and Accurate Coupled Climate Modeling with 3D Ocean and Atmosphere Emulators

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2509.12490
- **作者**: James P. C. Duncan et al.
- **开源代码**: 未提供

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


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 (40GB/80GB) 或 H100
- GPU数量: 1-8块（具体取决于模型规模配置）
- 训练时间: 约数天至数周（未明确说明具体时长）

### 数据集（Datasets）
1. **再分析气候数据集**
   - 来源: ERA5 (ECMWF)、CMIP6 历史模拟数据或类似全球气候模式输出
   - 任务: 训练耦合海洋-大气 emulator
   - 数据规模: 数百年的全球气候模拟数据（TB 级别），包含 145 个 2D 场、8 个大气垂直层、19 个海洋垂直层
   - 是否公开: 部分公开（ERA5 公开，CMIP6 部分公开）

2. **验证/评估数据集**
   - 来源: 历史观测或独立的气候模拟数据
   - 任务: 模型评估与验证（尤其是 ENSO 等气候现象）
   - 数据规模: 数十年至百年尺度数据
   - 是否公开: 不确定

### 数据处理
- 空间重网格化至 1 度水平分辨率
- 海洋数据插值至 5 天间隔，大气数据插值至 6 小时间隔
- 标准化/归一化处理（z-score 或 min-max 归一化）
- 海冰、表面和大气顶变量的分离处理
- 时序数据的滑动窗口切分用于序列建模

### 复现难度
- ★★★☆☆（中等难度）
- 原因：缺乏公开代码和具体训练细节；大规模气候数据获取和处理需要较高计算资源；耦合建模涉及复杂的海洋-大气数据转换；arXiv 论文未提供代码仓库链接或详细超参数设置


## 📊 7. 实验分析（Experiments）

**稳定性**：
- 高度稳定的长周期模拟
- 可运行数百年

**精度**：
- 气候偏差低
- 与边界强迫下的组件模型相当

**变率**：
- ENSO 等耦合气候现象的真实变率
- 在非耦合模式下无法实现的模拟能力



## 📐 7. 数学与物理建模（Math & Physics）
- **关键公式**: xxx
- **物理意义 / 解释**: xxx

## 📊 8. 实验分析（Experiments）
- **对比方法**: xxx
- **评估指标**: xxx
- **主要结果**: xxx
- **关键发现**: xxx

## 🔍 9. 优缺点分析（Critical Review）
**优点：** xxx
**缺点：** xxx

## 💡 10. 对我的启发（For My Research）
- xxx

## 🔮 11. Idea 扩展与下一步（Next Steps）
1. xxx

## 🧾 12. 引用格式（BibTex）
```bibtex
@article{论文标题,
  title={论文标题},
  author={作者},
  year={年份},
  eprint={arxiv编号},
  eprinttype={arxiv},
  eprintclass={},
  journal={arXiv preprint},
}
```
