---
title: "STREAMLINING OCEAN DYNAMICS MODELING WITH FOURIER NEURAL OPERATORS: A MULTIOBJECTIVE HYPERPARAMETER AND ARCHITECTURE OPTIMIZATION APPROACH"
arXiv: "2404.05768"
authors: ['Yixuan Sun', 'Argonne National Laboratory', 'Ololade Sowunmi', 'Florida State University', 'Romain Egele', 'Université Paris-Saclay', 'Sri Hari Krishna Narayanan', 'Argonne National Laboratory', 'Luke Van Roekel', 'Los Alamos National Laboratory', 'Prasanna Balaprakash', 'Oak Ridge National Laboratory']
year: 2024
source: "arXiv"
venue: "arXiv preprint"
method_tags: ['neural_operator', 'fno', 'hyperparameter_optimization', 'deephyper', 'bayesian_optimization']
application_tags: ['ocean_modeling', 'baroclinic_wind_driven_ocean', 'sea_surface_temperature', 'forecasting']
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "read"
---

# 📑 STREAMLINING OCEAN DYNAMICS MODELING WITH FOURIER NEURAL OPERATORS

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2404.05768
- **作者机构**: Yixuan Sun (Argonne National Laboratory), Ololade Sowunmi (Florida State University), Romain Egele (Université Paris-Saclay), Sri Hari Krishna Narayanan (Argonne), Luke Van Roekel (Los Alamos), Prasanna Balaprakash (Oak Ridge)
- **开源代码**: None

## 🧠 2. 一句话总结（TL;DR）
本文利用DeepHyper中的多目标超参数优化算法，对傅里叶神经算子（FNO）进行自动化调参，解决海洋动力学建模中的超参数选择难题。创新性地将异常相关系数（ACC）引入损失函数，结合MSE组成复合损失，在理想化斜压风驱动海洋模型上实现了单步预测和30天自回归滚动预测的显著提升。

## 🎯 3. 研究问题（Problem Definition）
深度学习海洋建模面临两大挑战：（1）超参数选择困难，手动调参耗时耗力且搜索空间庞大；（2）传统MSE损失函数倾向于产生模糊的均值场预测，忽略了局地变化和涡旋等精细结构。本文针对理想化斜压风驱动海洋模型，目标是预测四个诊断变量（盐度、温度、纬向速度、经向速度）的单步和长期时空演化。

## 🚀 4. 核心贡献（Contributions）
1. **自动化超参数优化流程**：首次将DeepHyper与FNO结合，构建完整的自动化建模流程，涵盖数据预处理、神经网络架构和训练策略的联合优化。
2. **复合损失函数设计**：提出MSE+负ACC的复合损失函数，利用气候研究中常用的ACC指标改善深度学习模型的预测质量。
3. **多目标优化**：同时优化验证集MSE和ACC两个目标，探索两者之间的权衡关系。
4. **大规模并行搜索**：在20个计算节点（每节点4块A100 GPU）上执行贝叶斯优化，实现高效的超参数搜索。

## 🏗️ 5. 方法详解（Methodology）

### 5.1 傅里叶神经算子（FNO）
FNO通过在傅里叶域中执行卷积核积分来逼近偏微分方程的解算子。主要包含三个组件：
- **Lifting层**：将输入函数变换到高维空间
- **FNO块**：快速傅里叶变换（FFT）→频域卷积→高频滤波→逆FFT
- **投影层**：将数据映射回原始维度

### 5.2 超参数搜索空间
搜索空间分为三类：
- **数据预处理**：padding开关、padding类型（constant/reflect/replicate/circular）、坐标特征开关
- **网络架构**：lifting激活函数、FNO块数量、隐通道数、傅里叶模式数、投影层数和大小、投影激活函数
- **训练策略**：损失函数权重α、优化器（Adadelta/Adagrad/Adam/AdamW/RMSprop/SGD）、学习率、权重衰减、批大小

### 5.3 多目标贝叶斯优化
采用DeepHyper中的集中式贝叶斯优化，使用随机森林作为代理模型，qUCB获取函数实现多点多目标并行采集。通过随机标量化将多目标问题转化为单目标问题进行求解。

## 📐 6. 数学与物理建模（Math & Physics）

### 6.1 问题形式化
理想化斜压风驱动海洋模型可表述为初值问题：
$$x(t+1) = x(t) + \int_t^{t+1} f(x(\tau, \kappa)) d\tau$$

FNO近似的离散形式为：
$$x_{t+1} = N_\theta(x_t, \kappa)$$

### 6.2 复合损失函数
$$L(\theta, D) = \alpha \cdot L_{MSE} + (1-\alpha) \cdot L_{NegACC}$$

其中：
$$L_{MSE} = \frac{1}{N}\sum_{i=1}^{N} \|x_{t+1}^{(i)} - N_\theta(x_t^{(i)}, \kappa^{(i)})\|_2^2$$

$$L_{NegACC} = -\frac{\sum_{i=1}^{N}(N_\theta(x_t^{(i)}, \kappa^{(i)})-\bar{x}_{t+1})(x_{t+1}^{(i)}-\bar{x}_{t+1})}{\sqrt{\sum_{i=1}^{N}(N_\theta(x_t^{(i)}, \kappa^{(i)})-\bar{x}_{t+1})^2}\sqrt{\sum_{i=1}^{N}(x_{t+1}^{(i)}-\bar{x}_{t+1})^2}}$$

### 6.3 ACC的物理意义
异常相关系数（ACC）衡量预测值与真实值相对于时间均值场的偏差相关性，在气候模型评估中广泛使用。ACC越高，表明模型越能准确捕捉相对于平均态的偏离模式，这对于海洋涡旋、中尺度变率等关键过程的预测至关重要。

## 📊 7. 实验分析（Experiments）

### 7.1 数据集
使用SOMA测试案例生成的理想化斜压风驱动海洋模型数据：
- 100个独立模拟，每个模拟改变Gent-McWilliams参数化中的bolus扩散率κGM
- 变量：盐度、温度、纬向速度、经向速度
- 分辨率：100×100网格点
- 时间：30个时间步（天）
- 数据划分：训练60%、验证20%、测试20%

### 7.2 复合损失函数验证
在默认超参数下，复合损失函数（MSE+NegACC）相比纯MSE损失：
- 盐度：log(RSE) -2.202→-2.498, log(1-ACC) -2.503→-2.800
- 温度：log(RSE) -3.696→-3.061, log(1-ACC) -4.015→-3.363
- 经向速度：log(RSE) -1.958→-2.067, log(1-ACC) -2.258→-2.842
- 纬向速度：log(RSE) -2.248→-2.303, log(1-ACC) -2.549→-2.808

### 7.3 最优配置性能
最优配置相比基线配置：
- 所有四个变量的ACC均有提升
- 自回归滚动30天预测误差积累显著降低
- 10天滚动预测的经向速度剖面对比显示最优配置预测更加准确

### 7.4 超参数敏感性分析
- **数据相关**：padding类型和坐标特征对验证MSE影响不明显（圆形流域边界条件所致）
- **训练相关**：较小batch size更优；AdamW优化器表现最佳；α在中间值时性能次优
- **架构相关**：隐通道数2-10、较少FNO块、较多傅里叶模式数、较少投影层数效果更好；Leaky ReLU和PReLU优于ReLU

## 🔍 8. 优缺点分析（Critical Review）

### 优点
1. **自动化程度高**：首次实现FNO全流程自动化调参，减少人工干预
2. **多目标优化框架**：同时考虑精度和异常相关性的权衡，设计合理
3. **复合损失函数创新**：将气候评估指标引入深度学习损失函数，具有较强的物理意义
4. **大规模并行效率**：在20节点A100集群上完成搜索，具有实际应用价值
5. **无权衡关系**：实验证明MSE和ACC之间不存在明显权衡，可同时优化

### 缺点
1. **仅测试理想化模型**：未在真实海洋观测数据或高分辨率环流模型上验证
2. **滚动预测仅30天**：对于气候尺度预测仍较短
3. **搜索空间可能不完备**：部分重要超参数（如学习率调度策略）未纳入搜索
4. **缺乏与其他架构对比**：仅与默认FNO配置对比，未与Transformer、U-Net等架构比较

## 💡 9. 对我的启发（For My Research）

1. **超参数优化范式**：DeepHyper的多目标HPO流程可移植到我的数据同化研究中，自动搜索EnKF的协方差膨胀因子、观测误差阈值等关键参数。
2. **复合损失函数设计**：将物理约束或评估指标（如相关系数、谱误差）引入损失函数，可能改善海洋数据同化中模型预测的精细结构。
3. **自回归滚动测试**：对FNO等算子学习模型进行长期滚动预测测试，是验证模型稳定性的关键。
4. **并行计算策略**：早停机制（constant predictor和单epoch时间约束）可显著加速HPO搜索。

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **FNO+数据同化**：将超参数优化后的FNO与集合卡尔曼滤波（EnKF）结合，用于海洋状态估计和预报。
2. **真实海洋数据验证**：在ORAS5、ORAP等再分析数据或卫星观测数据上验证FNO性能。
3. **更长尺度预测**：扩展到季节至年际尺度的海洋可预报性研究。
4. **多物理过程耦合**：加入海冰、波浪、大气通量等耦合过程。
5. **神经架构搜索**：将FNO与可学习激活函数、动态卷积核等结合，实现联合架构和超参数优化。

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{sun2024streamlining,
  title={STREAMLINING OCEAN DYNAMICS MODELING WITH FOURIER NEURAL OPERATORS: A MULTIOBJECTIVE HYPERPARAMETER AND ARCHITECTURE OPTIMIZATION APPROACH},
  author={Sun, Yixuan and Sowunmi, Ololade and Egele, Romain and Narayanan, Sri Hari Krishna and Van Roekel, Luke and Balaprakash, Prasanna},
  year={2024},
  eprint={2404.05768},
  eprinttype={arxiv},
  eprintclass={cs.LG},
}
```
