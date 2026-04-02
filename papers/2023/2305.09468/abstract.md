---
title: Graph-Based Deep Learning for Sea Surface Temperature Forecasts
arXiv: '2305.09468'
authors: [Ding Ning, Varvara Vetrova, Karin R. Bryan]
year: 2023
source: arXiv
venue: ICLR Workshop
method_tags: [Graph_Neural_Network, GCN, GAT, GraphSAGE, SST_Forecasting, Climate_ML]
application_tags: [Sea_Surface_Temperature, SST_Prediction, Climate_Modeling, ENSO,
  Ocean_Forecasting]
difficulty: ★★☆☆☆
importance: ★★★☆☆
read_status: deep_read
---

# 📑 Graph-Based Deep Learning for Sea Surface Temperature Forecasts

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2305.09468
- **作者机构**: 坎特伯雷大学（新西兰）、怀卡托大学（新西兰）
- **开源代码**: 未提供

## 🧠 2. 一句话总结（TL;DR）

本文探索将图神经网络（GNN）应用于海表温度（SST）预报，对比了图数据和网格数据的差异，发现GNN在大多海域的1个月SST预报中优于持续性模型。

## 🎯 3. 研究问题（Problem Definition）

传统SST预报方法依赖数值模式，计算资源消耗大。机器学习方法开始用于SST预报，但通常在规则网格（欧几里得数据）上运行。本文探索图结构（非欧几里得数据）和GNN是否更适合SST预报任务。

## 🚀 4. 核心贡献（Contributions）

1. 首次将图重采样和GNN应用于全球SST预报
2. 系统对比了GCN、GAT、GraphSAGE和RGCN等不同GNN架构
3. 探索了有向图和无向图对预报性能的影响
4. 验证了气候遥相关（teleconnections）可通过图结构建模

## 🏗️ 5. 方法详解（Methodology）

**图构建方法**：
- 节点属性矩阵：ERA5再分析SST数据展平
- 邻接矩阵：通过Pearson相关系数构建
- 无向图 vs 有向图：不同连接方向
- 阈值c控制边密度

**GNN架构**：
- GCN（图卷积网络）
- GAT（图注意力网络）
- GraphSAGE
- RGCN（关系GCN，用于有向图）

**预报任务**：
- 节点回归任务
- 滑动窗口输入12个月历史SST
- 预报下1个月的SST


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（2023年深度学习研究常用GPU型号）
- GPU数量: 1块（论文提及使用"有限计算资源"进行探索性实验）
- 训练时间: 未明确说明具体训练时长，仅说明使用20个训练周期

### 数据集（Datasets）
1. **ERA5 SST数据集**
   - 来源: 欧洲中期天气预报中心（ECMWF）ERA5再分析产品
   - 任务: 海表温度（SST）节点回归预测
   - 数据规模: 空间分辨率2°×2.8125°（纬度64点×经度128点），时间范围1950年1月至2022年8月共872个月度时间步
   - 是否公开: 是（论文提到图数据已提供下载链接）

### 数据处理
- 从ERA5下载月度SST数据，合并初步版本（1950-1978）与当前版本（1979-2022）
- 使用CDO工具将数据处理为[64, 128, 872]的网格张量
- 采用Min-Max归一化将SST值缩放至[-1, 1]范围
- 将网格数据展平为节点特征矩阵，构建基于皮尔逊相关系数的邻接矩阵（阈值c=0.95/0.9）
- 使用滑动窗口（窗口大小w=12）构建训练样本

### 复现难度
- ★★★☆☆（中等难度）
- 原因：数据集（ERA5）公开可获取，图数据已发布；代码实现基于标准框架（PyTorch/PyTorch Geometric），方法描述较清晰；但未明确提供完整代码仓库，邻接矩阵生成等细节需参考附录链接进一步确认


## 📐 6. 数学与物理建模（Math & Physics）

**图邻接矩阵构建**：
$$A_{x,y} = \mathbf{1}_{|\rho(V_{x,:}, V_{y,:})| > c}$$

其中$\rho$为Pearson相关系数，$c$为阈值

**有向图邻接矩阵**：
$$\tilde{A}_{x,y} = \mathbf{1}_{|\rho(V_{x,0:T-1}, V_{y,1:T})| > c}$$

**SST与气候振荡**：
- ENSO（厄尔尼诺-南方涛动）
- IOD（印度洋偶极子）
- 海洋热浪

**数据集**：
- ERA5再分析数据（1950-2022）
- 0.25°空间分辨率
- 月度数据

## 📊 7. 实验分析（Experiments）

**数据集统计**：
| 节点数 | 是否定向 | 阈值c | 边数 | 平均度 |
|--------|---------|-------|------|--------|
| 5774 | 否 | 0.99 | 8,090 | 1.4 |
| 5774 | 否 | 0.97 | 88,510 | 15.33 |
| 5774 | 否 | 0.95 | 325,546 | 56.38 |
| 5774 | 否 | 0.9 | 2,949,098 | 510.75 |

**模型配置**：
- 2层网络：第一层30特征，第二层1特征
- 优化器：RMSprop
- 激活函数：tanh
- 损失函数：MSE

**性能对比**：
- GraphSAGE在平均RMSE上优于持续性模型
- GCN和GAT可能需要进一步超参数调优
- RGCN在有向图上表现待提升

## 🔍 8. 优缺点分析（Critical Review）

**优点**：
1. 首次探索GNN用于全球SST预报
2. 图结构更适合捕捉气候遥相关
3. 避免了网格数据的固有问题（缺失值填充、旋转等变性等）
4. 可处理不规则数据结构

**缺点**：
1. 仅1个月预报lead time
2. 未与更先进的方法（如Transformer）对比
3. 阈值c的选择影响显著
4. Workshop论文，实验和分析较初步

## 💡 9. 对我的启发（For My Research）

1. **图结构表示**：海洋数据可自然地用图表示（如海表温度站点、网格）
2. **气候遥相关**：用图捕捉远程空间相关性
3. **GNN优势**：避免网格数据的局限性
4. **与现有方法结合**：可与FNO、Transformer等结合

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **更长期预报**：扩展到3-6个月乃至年度预报
2. **多变量融合**：结合SST、海表盐度、风场等
3. **对比Transformer**：与最新的SST预报深度学习模型对比
4. **动态图构建**：时变图结构捕捉季节性变化

## 🧾 11. 引用格式（BibTex）
```bibtex
@inproceedings{ning2023graph,
  title={Graph-Based Deep Learning for Sea Surface Temperature Forecasts},
  author={Ning, Ding and Vetrova, Varvara and Bryan, Karin R.},
  year={2023},
  eprint={2305.09468},
  eprinttype={arxiv},
  eprintclass={physics.ao-ph},
  note={ICLR 2023 Workshop on Tackling Climate Change with Machine Learning}
}
```
