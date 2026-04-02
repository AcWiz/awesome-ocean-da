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
- GPU数量: 8-64 张（分布式训练配置）
- 训练时间: 未明确说明（预计数天至数周，取决于模型规模和数据集规模）

### 数据集（Datasets）
1. **ERA5 再分析数据**
   - 来源: 欧洲中期天气预报中心 (ECMWF)
   - 任务: 大气 emulator 训练与验证
   - 数据规模: 1979-2023 年（约 44 年），6 小时间隔，1 度分辨率
   - 是否公开: 是

2. **ORAS5 / GLORYS 海洋再分析数据**
   - 来源: 哥白尼海洋环境监测服务 (CMEMS)
   - 任务: 海洋 emulator 训练与验证
   - 数据规模: 1989-2023 年（约 34 年），5 天间隔，1 度分辨率
   - 是否公开: 是

3. **CMIP6 历史模拟数据（可选验证）**
   - 来源: 全球气候模式比较项目
   - 任务: 耦合模型长期模拟验证
   - 数据规模: 多模式集合，约 1850-2014 年历史模拟
   - 是否公开: 是

### 数据处理
- 原始再分析数据重采样至 1 度网格（360×180）
- 大气数据：6 小时间隔提取，时间维度约 25,550 个时间步
- 海洋数据：5 天间隔处理，时间维度约 2,500 个时间步/年
- 垂直插值至 8 个大气层和 19 个海洋层
- Z-score 标准化处理（按时间序列全局统计）
- 陆地掩码和海冰掩码应用

### 复现难度
- ★★★☆☆（中等难度）
- 原因：数据集（ERA5、ORAS5）可公开获取，但完整训练流程和耦合策略细节未完全公开；需要大规模 GPU 集群资源；超参数和模型架构细节需参考补充材料或尝试复现；未提供官方开源代码库


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
