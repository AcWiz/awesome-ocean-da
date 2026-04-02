---
title: 'CAS-C ANGLONG: A SKILLFUL 3D TRANSFORMER MODEL FOR SUB-SEASONAL TO SEASONAL
  GLOBAL SEA SURFACE TEMPERATURE PREDICTION'
arXiv: '2409.05369'
authors: [Longhao Wang, Chinese Academy of Sciences, Xuanze Zhang, Chinese Academy
    of Sciences, L. Ruby Leung, Pacific Northwest National Laboratory, Francis H.S.
    Chiew, CSIRO Environment, Amir AghaKouchak, 'University of California, Irvine',
  Kairan Ying, National Institute of Natural Hazards, Yongqiang Zhang, Chinese Academy
    of Sciences]
year: 2024
source: arXiv
venue: arXiv
method_tags: [transformer, swin_transformer, attention_mechanism, 3d_cnn, lstm]
application_tags: [sst_prediction, s2s_forecasting, enso, ocean_modeling, climate_prediction]
difficulty: ★★★★☆
importance: ★★★★★
read_status: read
---

# 📑 CAS-C ANGLONG: A SKILLFUL 3D TRANSFORMER MODEL

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2409.05369
- **作者机构**: Longhao Wang, Xuanze Zhang, Yongqiang Zhang (中国科学院地理科学与资源研究所); L. Ruby Leung (太平洋西北国家实验室); Francis H.S. Chiew (CSIRO); Amir AghaKouchak (加州大学欧文分校); Kairan Ying (国家自然灾害研究院)
- **开源代码**: https://github.com/GISWLH/CAS-Canglong

## 🧠 2. 一句话总结（TL;DR）
本文提出了CAS-Canglong模型，一个基于Swin-Transformer架构的三维深度学习模型，用于次季节至季节（S2S）尺度的全球海表温度（SST）预测。该模型首次利用深度学习实现S2S全球SST预测，在七个关键海洋区域的1-3个月提前预测技能比物理数值模型提升13.7%至77.1%，并成功预测了2024年ENSO从El Niño向La Niña的转换。

## 🎯 3. 研究问题（Problem Definition）
S2S（2周至数月）时间尺度的全球SST准确预测对干旱洪水预报和灾害预警至关重要。传统物理数值模式面临计算效率低、海洋-大气初始条件保持能力有限、不确定性大等挑战。深度学习方法虽在天气预报和ENSO预测中取得进展，但尚无专门针对S2S全球SST预测的DL模型。本研究旨在开发一个能捕捉海洋-大气耦合非线性复杂系统、同时建模空间和时间维度的DL模型。

## 🚀 4. 核心贡献（Contributions）
1. **首个S2S全球SST深度学习预测模型**：首次利用深度学习实现S2S尺度的全球SST预测，分辨率达0.25°×0.25°。
2. **3D Transformer架构**：将时间维度作为第三维，采用encoder-decoder结构的Swin-Transformer，融合多变量气象和海洋要素。
3. **复合损失函数**：结合MSE损失（优化收敛）和相关性损失（保证长期预测可靠性），平衡短期精度和长期稳定性。
4. **卓越的预测性能**：在七个关键区域（Niño 3.4、AO、PDO、Warm Pool、SAO、SIO、SPO）的1-3个月SST预测技能提升13.7%-77.1%。
5. **实时预报验证**：成功预测2024年ENSO从El Niño向La Niña的转换，表现优于ECMWF S2S模式。

## 🏗️ 5. 方法详解（Methodology）

### 5.1 模型架构
- **输入格式**：$T_{in} \times C \times N_{lat} \times N_{lon} = 16 \times 8 \times 721 \times 1440$
  - 16个月连续序列作为输入
  - 8个特征变量：海平面气压、850hPa和500hPa纬向/经向风速、位势高度、地面潜热通量、净太阳辐射
  - 输出：$T_{out} \times 721 \times 1440$（可调，默认预测3个月）
- **核心结构**：Swin-Transformer encoder-decoder架构
- **关键模块**：
  - Patch embedding层（2×4×4）
  - 多头自注意力（MSA）和窗口多头自注意力（W-MSA）
  - 下采样提取特征→Swin-Transformer处理→上采样恢复

### 5.2 损失函数设计
1. **MSE损失**（快速收敛）：
$$L_{fmse} = \frac{1}{T_{out}}\sum_{t=1}^{T_{out}}(X_{t,l} - \hat{X}_{t,l})^2$$

2. **相关性损失**（保证长期预测可靠性）：
$$L_{corr} = \frac{1}{T_{out}}\sum_{l=2}^{T_{out}} \max\{0, 0.5 - \frac{\sum_{t=1}^{T}(X_{t,l}-\bar{X}_l)(\hat{X}_{t,l}-\bar{\hat{X}}_l)}{\sqrt{\sum_{t=1}^{T}(X_{t,l}-\bar{X}_l)^2}\sqrt{\sum_{t=1}^{T}(\hat{X}_{t,l}-\bar{\hat{X}}_l)^2}}\}$$


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100
- GPU数量: 未明确说明（推测为多GPU并行训练）
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **ERA5再分析数据**
   - 来源: 欧洲中期天气预报中心（ECMWF）
   - 任务: 作为模型训练和验证的真值（ground truth）
   - 数据规模: 51年（1959-2009）训练数据，验证期2009-2015，测试期2016-2022；包含8个关键海洋和大气变量
   - 是否公开: 是

2. **ECMWF S2S模式数据**
   - 来源: ECMWF S2S项目
   - 任务: 与物理数值模型进行对比评估
   - 数据规模: 2015-2020年重叠时段
   - 是否公开: 是

3. **NMME多模式集合数据**
   - 来源: 北美多模式集合（North American Multi-Model Ensemble）
   - 任务: 与物理数值模型进行对比评估
   - 数据规模: 22个先进数值天气预报模型集合
   - 是否公开: 是

4. **HadISST数据集**
   - 来源: 英国气象局哈德利中心
   - 任务: SST预测的独立验证对比
   - 数据规模: 2015-2020年重叠时段
   - 是否公开: 是

### 数据处理
- 数据归一化处理：采用标准化方法对SST及大气变量进行预处理
- 时空特征编码：将时间维度作为额外维度融入3D Transformer架构
- 空间重映射：将模型0.25°×0.25°分辨率重映射至1°×1°以匹配数值模型进行对比
- 训练策略：采用滑动时间窗口方式构建训练样本，支持1-24个月不同预见期的预测任务

### 复现难度
- ★★★★☆（较高）
- 原因：（1）论文未提供源代码公开；（2）虽使用公开数据集（ERA5等），但模型架构细节和训练超参数未完全披露；（3）需要高性能GPU资源（推荐A100）进行复现；（4）3D Swin-Transformer架构实现较为复杂；（5）作为2024年最新研究成果，部分技术细节可能需进一步联系作者获取


## 📐 6. 数学与物理建模（Math & Physics）

### 6.1 数据驱动方法
利用51年（1959-2009）ERA5再分析数据驱动模型学习海洋-大气系统的非线性时空关系。模型通过自注意力机制从历史观测数据中学习SST格局和物理关系。

### 6.2 关键物理变量
- 海表温度异常与气候变率的强遥相关
- ENSO事件的热带太平洋SST异常
- 南大洋海温与气候变率

### 6.3 评估指标
- **RMSE**（纬向加权）：
$$RMSE = \sqrt{\frac{\sum_{i=1}^{N_{lon}}\sum_{j=1}^{N_{lat}}W(i)(\hat{X}_{i,j,l}-X_{i,j,l})^2}{N_{lon} \times N_{lat}}}$$

- **相关系数R**

## 📊 7. 实验分析（Experiments）

### 7.1 数据划分
- 训练集：1959年1月至2009年8月
- 验证集：2009年9月至2016年4月
- 测试集：2016年5月至2022年12月
- 比例约8:1:1

### 7.2 主要结果
- **与22个NWP模式对比**：CAS-Canglong在7个区域的1-3个月SST预测均优于所有数值模式
- **RMSE降低**：Niño 3.4降低34.9%，AO降低77.1%，PDO降低28.5%，Warm Pool降低39.6%
- **ENSO预测**：三个月提前预测的总体命中率达85%
- **实时预报**：成功预测2024年El Niño向La Niña的转变

### 7.3 分区域性能
| 区域 | 1月相关系数 | 3月相关系数 |
|------|-------------|-------------|
| Niño 3.4 | 0.91 | 0.57 |
| AO | 0.9 | 0.6 |
| PDO | 高 | - |
| 南大洋(SIO/SPO/SAO) | >0.9 | >0.7 |

## 🔍 8. 优缺点分析（Critical Review）

### 优点
1. **开创性工作**：首次实现S2S全球SST的深度学习预测
2. **高分辨率**：0.25°×0.25°分辨率与最先进物理模式相当
3. **多区域适用**：在热带、温带和高纬度区域均表现出色
4. **计算高效**：推理速度远快于数值模式
5. **实时预报验证**：在2024年实时预测中得到验证

### 缺点
1. **依赖再分析数据**：未直接使用卫星观测或现场观测数据
2. **单一模态预测**：仅预测SST，未耦合其他海洋或大气变量
3. **转移学习有限**：预训练模型区域迁移能力待充分验证
4. **物理约束缺失**：未显式编码物理守恒定律或能量平衡

## 💡 9. 对我的启发（For My Research）

1. **Swin-Transformer用于海洋预测**：3D时空建模方法可移植到海洋数据同化和预报研究
2. **复合损失函数设计**：将MSE与相关性损失结合，可平衡预测精度和时空一致性
3. **区域自适应策略**：预训练+微调策略可用于特定海域的高分辨率预报
4. **集成预测**：多模型初始化的集成方法可提高预报可靠性
5. **S2S时间尺度的重要性**：该尺度是天气预报和气候预测之间的桥梁，对我的数据同化研究具有重要意义

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **耦合预报系统**：将SST预测与大气环流模型耦合，提升陆地区域S2S预报
2. **海洋次表层**：加入温跃层和次表层温度预测，增强ENSO预测能力
3. **海冰耦合**：引入海冰密集度和厚度变量，扩展到极地区域预报
4. **不确定性量化**：采用贝叶斯深度学习或集合方法量化预测不确定性
5. **物理约束神经网络**：将能量守恒、质量守恒等物理定律编码到模型中

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{wang2024cascanglong,
  title={CAS-C ANGLONG: A SKILLFUL 3D TRANSFORMER MODEL FOR SUB-SEASONAL TO SEASONAL GLOBAL SEA SURFACE TEMPERATURE PREDICTION},
  author={Wang, Longhao and Zhang, Xuanze and Leung, L. Ruby and Chiew, Francis H.S. and AghaKouchak, Amir and Ying, Kairan and Zhang, Yongqiang},
  year={2024},
  eprint={2409.05369},
  eprinttype={arxiv},
  eprintclass={physics.ao-ph},
}
```
