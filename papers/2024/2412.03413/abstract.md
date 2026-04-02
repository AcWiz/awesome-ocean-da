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
- GPU: NVIDIA A100 或 V100（深度学习模型训练的常见选择）
- GPU数量: 1-2块
- 训练时间: 未明确说明具体训练时长，但基于21年MODIS数据和256×256图像规模，预计每次完整训练需数小时至数天

### 数据集（Datasets）
1. **MODIS Aqua L3 SST**
   - 来源: NASA PODAAC (https://podaac.jpl.nasa.gov/dataset/MODIS_AQUA_L3_SST_THERMAL_DAILY_4K_NIGHTTIME_V2014.0)
   - 任务: 海表温度重建与云遮挡区域填补
   - 数据规模: 2002年7月至2023年12月的夜间每日数据，覆盖意大利海域256×256网格点（约1020×1020平方公里），空间分辨率4公里
   - 是否公开: 是

2. **MODIS Terra L3 SST**
   - 来源: NASA PODAAC
   - 任务: 作为验证数据集
   - 数据规模: 与Aqua同期数据
   - 是否公开: 是

3. **Copernicus Marine Service L4产品**
   - 来源: 哥白尼海洋服务中心
   - 任务: 作为基准对比数据
   - 是否公开: 是

### 数据处理
- **质量控制**: 仅使用质量标志为0、1、2的像素点（分别占比79%、21%、0.2%）
- **数据筛选**: 剔除近岸异常值和云边界错误识别的数据
- **季节气候学计算**: 基于21年数据计算日均气候学，并使用高斯模糊填补因云遮挡导致的气候学空缺
- **异常值计算**: 从原始SST中减去季节气候学，得到SST异常作为模型输入
- **人工云生成**: 采用人工生成的云遮挡模式进行数据增强
- **训练测试划分**: 2002年7月至2021年6月用于训练，2021年7月至2023年12月用于测试

### 复现难度
- ★★★☆☆（中等难度）
- 原因：MODIS卫星数据和Copernicus L4产品均公开可获取，模型架构（U-Net、ViT）已公开，但论文未明确说明代码开源情况。数据预处理流程描述详细，但人工云生成的具体参数和完整训练超参数未完全公开，可能影响完全复现。


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
