---
title: Deep Learning for Sea Surface Temperature Reconstruction under Cloud Occlusion
arXiv: '2412.03413'
authors: [Andrea Aspertia, Ali Aydogdub, Angelo Grecoa, Fabio Merizzia, Pietro Miragliob,
  Beniamino Tartufolici, Alessandro Testaa, Nadia Pinardic, Paolo Oddob]
year: 2024
source: arXiv
venue: arXiv
method_tags: [U_Net, Vision_Transformer, DINCAE, CNN]
application_tags: [SST_reconstruction, cloud_filling, satellite_Ocean, MODIS, oceanography]
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
---

# 📑 Deep Learning for Sea Surface Temperature Reconstruction under Cloud Occlusion

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2412.03413
- **作者机构**: 博洛尼亚大学、CMCC Foundation
- **开源代码**: 未提供

## 🧠 2. 一句话总结（TL;DR）
本文利用U-Net和Vision Transformer等深度学习模型从卫星MODIS图像中重建被云遮挡的海表温度(SST)区域。与传统最优插值方法相比，提出的U-Net64模型在RMSE指标上降低了约50%，展现了深度学习方法在海洋卫星数据重建中的优势。

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 如何从有云遮挡的卫星SST图像中准确重建完整海表温度场
- **科学意义**: SST是重要的气候变量，云遮挡导致大量海洋数据缺失，影响海洋-大气耦合研究
- **研究挑战**:
  - 云遮挡区域的SST重建需要保持空间连续性
  - 需避免在无云区域引入平滑效应
  - 重建方法需优于传统统计方法（如OI、EOF）

## 🚀 4. 核心贡献（Contributions）
1. 系统比较了U-Net和Vision Transformer两种深度学习架构在SST重建中的表现
2. 验证了将模型分割为四个128×128区域训练优于单个256×256模型
3. 确定了4天时间窗口是最佳的历史数据输入长度
4. 开发的U-Net64模型比现有DINCAE方法RMSE降低约20%

## 🏗️ 5. 方法详解（Methodology）
- **U-Net架构**: 编码器-解码器结构，跳跃连接保留空间细节
  - 结构[64, 128, 256, 512]，3个下采样层
  - 残差块(RB)和转置卷积进行上/下采样
- **Vision Transformer**: 分块嵌入+自注意力建模全局依赖
- **人工云生成器**: 在训练时模拟云遮挡进行数据增强
- **训练策略**: AdamW优化器，学习率1e-4，early stopping patience=10


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（典型深度学习训练GPU）
- GPU数量: 未明确说明（推测为单GPU或少量GPU训练）
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **MODIS_AQUA_L3_SST_THERMAL_DAILY_4K_NIGHTTIME**
   - 来源: NASA PODAAC (https://podaac.jpl.nasa.gov/dataset/MODIS_AQUA_L3_SST_THERMAL_DAILY_4K_NIGHTTIME_V2014.0)
   - 任务: 海表温度（SST）重建与云填充
   - 数据规模: 2002-2023年夜间数据，区域覆盖256×256网格点（约1020×1020平方公里），意大利海域（纬度35.33°-46.0°N，经度7.92°-18.58°E）
   - 是否公开: 是

2. **MODIS_TERRA_L3_SST**
   - 来源: NASA PODAAC
   - 任务: 验证数据集（用于模型验证）
   - 数据规模: 与MODIS_AQUA相同时间范围
   - 是否公开: 是

3. **Copernicus Marine Service L4产品**
   - 来源: Copernicus Marine Service
   - 任务: 模型对比基准
   - 数据规模: 意大利海域L4 SST产品
   - 是否公开: 是

### 数据处理
- 质量控制：仅使用质量标志为0、1、2的像素点（分别占比79%、21%、0.2%）
- 季节气候学计算：基于21年数据计算每日气候学均值，使用高斯模糊填补云遮挡导致的缺失值
- 异常值处理：剔除低于5°C的极端低温值（ Mediterranean海区SST不低于5°C）
- 人工云层生成：使用随机生成算法模拟云遮挡区域用于训练
- 残差学习：模型学习SST观测值与气候学估计之间的残差
- 数据划分：训练集（2002-2021），测试集（2021-2023）

### 复现难度
- ★★★☆☆（中等）
- 原因：MODIS数据集公开可获取，区域明确；但论文未提供完整代码仓库、训练超参数细节及模型架构具体配置；部分实验细节（如梯度阈值设置、注意力模块具体实现）需进一步推断；arXiv论文通常在后续版本或GitHub仓库提供完整代码


## 📐 6. 数学与物理建模（Math & Physics）
- **数据预处理**: 减去气候学值获得距平
- **云遮挡建模**: 随机叠加历史云掩膜模拟真实遮挡
- **损失函数**: MSE for 回归任务
- **时间窗口**: 验证4天历史数据最优

## 📊 7. 实验分析（Experiments）
- **数据**: MODIS Aqua夜间L3 SST (2002-2023)，4km分辨率
- **研究区域**: 地中海（256×256网格）
- **评估指标**: RMSE
- **主要结果**:
  - U-Net64 128×128版本RMSE=0.30°C
  - 比DINCAE方法好约20%
  - 与Copernicus L4产品对比，U-Net64平均误差0.04°C vs L4的0.14°C

## 🔍 8. 优缺点分析（Critical Review）
**优点**:
- 深度学习方法显著优于传统OI/EOF方法
- 模块化设计便于调整区域和分辨率
- 与现有业务化L4产品直接对比

**缺点**:
- 依赖MODIS数据，可能不适用其他传感器
- 128×128分割策略增加了训练复杂度
- 扩散模型尚未取得满意效果

## 💡 9. 对我的启发（For My Research）
- U-Net等编码器-解码器架构可用于海洋数据插值和重构
- 多模型集成策略（U-Net + ViT）值得探索
- 人工遮挡生成是训练数据增强的有效方法
- 气候学去除+残差学习是处理周期性信号的有效范式

## 🔮 10. Idea 扩展与下一步（Next Steps）
1. 将类似方法应用于其他海洋变量（盐度、叶绿素）
2. 探索更长的历史时间窗口对重建质量的影响
3. 结合物理约束（如海表温度梯度守恒）增强结果一致性
4. 扩展到其他卫星传感器和海域

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{aspertia2024deep,
  title={Deep Learning for Sea Surface Temperature Reconstruction under Cloud Occlusion},
  author={Aspertia, Andrea and Aydogdub, Ali and Grecoa, Angelo and Merizzia, Fabio and Miragliob, Pietro and Tartufolici, Beniamino and Testaa, Alessandro and Pinardic, Nadia and Oddob, Paolo},
  year={2024},
  eprint={2412.03413},
  eprinttype={arxiv},
  eprintclass={cs.CV},
  journal={Elsevier},
}
```
