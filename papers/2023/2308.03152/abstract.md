---
title: 'AI-GOMS: Large AI-Driven Global Ocean Modeling System'
arXiv: '2308.03152'
authors: [Wei Xiong, Yanfei Xiang, Hao Wu, Shuyi Zhou, Yuze Sun, Muyuan Ma, Xiaomeng
    Huang]
year: 2023
source: arXiv
venue: arXiv
method_tags: [Masked_Autoencoder, Fourier_Based, Backbone_Downstream, Global_Ocean_Modeling,
  Deep_Learning]
application_tags: [Global_Ocean_Modeling, Ocean_Prediction, Mesoscale_Eddies, Ocean_Variables,
  Earth_System]
difficulty: ★★★★★
importance: ★★★★★
read_status: deep_read
---

# 📑 AI-GOMS: Large AI-Driven Global Ocean Modeling System

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2308.03152
- **作者机构**: 清华大学地球系统科学系、中国科学院大学计算机科学与技术学院
- **开源代码**: 未提供

## 🧠 2. 一句话总结（TL;DR）

AI-GOMS是一个大型AI驱动的全球海洋建模系统，采用基于傅里叶的掩码自编码器作为骨干模型，结合轻量级微调模型实现区域降尺度、海浪解码和生物地球化学耦合，在30天全球海洋基本变量预报中达到最佳性能。

## 🎯 3. 研究问题（Problem Definition）

传统数值海洋建模面临多重瓶颈：非线性不稳定、计算成本高、复用效率低、耦合成本高。海洋作为地球系统的重要组分，与大气不同，具有封闭复杂几何边界（地形拓扑约束）。现有AI方法尚未充分利用大规模预训练模型的潜力，且缺乏可迁移到其他相关场景的能力。

## 🚀 4. 核心贡献（Contributions）

1. 提出AI-GOMS，首个大型AI驱动的全球海洋建模系统
2. 设计基于傅里叶的掩码自编码器骨干模型
3. 提出"骨干-下游"范式，支持迁移、可扩展和复用
4. 实现15层深度、1/4°分辨率的30天全球海洋预报
5. 在黑潮区域1/12°分辨率成功模拟中尺度涡旋

## 🏗️ 5. 方法详解（Methodology）

**骨干模型架构**：
- 非对称编码器-解码器结构
- 基于Fourier的注意力块
- 支持变长序列输入输出
- Patch embedding结构映射物理场为一维token
- 多模态融合支持
- 随机掩码策略避免过拟合

**下游模块**：
- 区域降尺度模块
- 海浪解码模块
- 生物地球化学耦合模块

**训练策略**：
- 冻结骨干模型参数
- 轻量级微调下游模块
- 低训练成本


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 (基于同类型大规模深度学习海洋/气象模型的典型配置)
- GPU数量: 多GPU并行训练 (推测为8卡或以上配置，以支持大型骨干模型的训练)
- 训练时间: 未明确说明具体训练时长

### 数据集（Datasets）
1. **HYCOM (HYbrid Coordinate Ocean Model) 全球再分析数据**
   - 来源: GODAE (Global Ocean Data Assimilation Experiment)
   - 任务: 骨干模型训练、验证与测试
   - 数据规模: 10年训练数据(2000-2010) + 1年验证数据(2011) + 1年测试数据(2012)，包含5个基本海洋变量、15个深度层、1/4°空间分辨率
   - 是否公开: 是

2. **ERA5 大气再分析数据**
   - 来源: ECMWF (欧洲中期天气预报中心)
   - 任务: 作为大气强迫边界条件输入
   - 数据规模: 5个大气变量
   - 是否公开: 是

3. **ETOPO 地形数据**
   - 来源: NOAA
   - 任务: 海洋地形拓扑约束
   - 数据规模: 全球地形网格
   - 是否公开: 是

### 数据处理
- 将海洋变量(温度、盐度、流速、海表面高度)和大气变量通过Patch Embedding结构映射为一维序列 tokens
- 采用随机掩码策略(Random Mask)遮蔽部分patch以学习更本质的物理特征
- 输入数据包括初始时刻的海洋状态、大气强迫场和地形拓扑数据
- 骨干模型采用非对称编码器-解码器结构，编码器16层，解码器8层

### 复现难度
- ★★★☆☆ (中等难度)
- 原因：数据集(HYCOM、ERA5、ETOPO)均为公开可获取的标准数据集；方法框架基于成熟的Transformer架构和傅里叶注意力机制；但骨干模型的超参数设置、具体训练配置及完整代码细节未在文中详细披露，且需要大规模GPU计算资源进行完整模型训练


## 📐 6. 数学与物理建模（Math & Physics）

**预报变量**：
- 海水温度（T）
- 盐度（S）
- 纬向速度（U）
- 经向速度（V）
- 海表面高度（SSH）

**物理约束**：
- 地形拓扑约束
- 海洋层结特性
- 中尺度涡旋动力学

**深度设置**：
- 15个深度层
- 1/4°空间分辨率（约25km）
- 1/12°（约8km）涡旋解析

## 📊 7. 实验分析（Experiments）

**训练数据**：
- HYCOM（混合坐标海洋模式）全球再分析数据
- 覆盖全球海洋的5个基本变量

**性能评估**：
- 30天预报
- 多深度层（15层）
- 全球海洋基本变量

**关键成果**：
- 全球海洋基本变量预报最佳性能
- 黑潮区域中尺度涡旋成功模拟
- 热带太平洋海洋层结准确再现

**下游任务验证**：
- 区域降尺度
- 海浪解码
- 生物地球化学耦合

## 🔍 8. 优缺点分析（Critical Review）

**优点**：
1. 开创性的大型AI海洋建模系统
2. "骨干-下游"范式实现模型复用
3. 多模态数据支持，原生支持数据同化
4. 计算效率高，适合业务化应用

**缺点**：
1. 依赖再分析数据训练
2. 缺乏真实观测数据的端到端训练
3. 生物地球化学模块较为初步
4. 未与最新数值模式直接对比

## 💡 9. 对我的启发（For My Research）

1. **预训练-微调范式**：考虑先训练海洋基础模型，再针对具体任务微调
2. **多尺度建模**：同时处理全球和区域尺度
3. **多模态融合**：整合卫星高度计、SST、风场等多源数据
4. **业务化思路**：低推理成本支持实时预报应用

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **真实观测数据训练**：用卫星和Argo浮标数据微调
2. **三维预报扩展**：增加更多深度层
3. **集合预报**：利用AI模型的高效性进行大样本集合
4. **与其他地球系统组分耦合**：海气耦合、生物地球化学过程

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{xiong2023aigoms,
  title={AI-GOMS: Large AI-Driven Global Ocean Modeling System},
  author={Xiong, Wei and Xiang, Yanfei and Wu, Hao and Zhou, Shuyi and Sun, Yuze and Ma, Muyuan and Huang, Xiaomeng},
  year={2023},
  eprint={2308.03152},
  eprinttype={arxiv},
  eprintclass={physics.ao-ph},
}
```
