---
title: Data-driven discovery of Koopman eigenfunctions for control
arXiv: '1707.01146'
authors: [Eurika Kaiser, J. Nathan Kutz, Steven L. Brunton]
year: 2017
source: arXiv
venue: IEEE Transactions on Automatic Control / arXiv
method_tags: [Koopman_Operator, DMD, EDMD, System_Identification, Optimal_Control]
application_tags: [Nonlinear_Control, Hamiltonian_Systems, Ocean_Double_Gyre, Dynamical_Systems]
difficulty: ★★★★★
importance: ★★★★★
read_status: deep_read
---

# 📑 Data-driven discovery of Koopman eigenfunctions for control

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/1707.01146
- **作者机构**: University of Washington, Department of Mechanical Engineering & Department of Applied Mathematics
- **开源代码**: https://github.com/eurika-kaiser/KRONIC

## 🧠 2. 一句话总结（TL;DR）

本文提出KRONIC（Koopman Reduced Order Nonlinear Identification and Control）框架，通过稀疏回归从数据中发现Koopman本征函数，在由这些经验证的本征函数构成的Koopman不变子空间中构建控制模型，从而实现强非线性系统的线性最优控制，同时揭示了经典EDMD方法的闭包问题并给出解决方案。

## 🎯 3. 研究问题（Problem Definition）

非线性系统控制是工程领域的重大挑战。虽然线性系统已有成熟的控制和优化理论，但强非线性系统（如湍流，脑机接口、海洋流动）缺乏可用的简化模型用于控制设计。Koopman算子理论提供了一种将非线性系统嵌入线性框架的 principled 方法——通过有限维近似Koopman算子，利用线性系统理论进行预测、估计和控制。然而，现有方法存在关键问题：

1. **闭包问题（Closure Problem）**：标准EDMD在有限基函数下近似Koopman算子时，有限维子空间通常不构成Koopman不变子空间，导致估计的本征函数不能"封闭"地演化，产生虚假本征函数。

2. **线性测量局限性**：传统DMD基于线性测量（如状态本身），而这些测量通常不张成Koopman不变子空间，导致对非线性系统的线性模型无法描述瞬态动力学。

3. **轻阻尼本征函数识别**：哪些本征函数是可靠的、哪些是数值伪影，尚无系统的判别方法。

## 🚀 4. 核心贡献（Contributions）

1. **KRONIC控制框架**：提出首个基于经验证Koopman本征函数的非线性控制系统设计方法，在本征函数坐标中利用线性最优控制理论设计控制器，再映射回原状态空间。

2. **本征函数验证与稀疏回归**：指出EDMD的闭包问题，证明通过稀疏回归（Sparsity-promoting）可以正则化EDMD矩阵，发现可靠的轻阻尼本征函数。轻阻尼本征函数与近似守恒量（如哈密顿量）对应，在控制中具有特殊重要性。

3. **非线性嵌入线性控制的数学基础**：严格推导了控制-仿射系统和非仿射系统的本征函数动力学，证明了在本征函数坐标中控制问题可以转化为线性二次调节器（Linear Quadratic Regulator, LQR）。

4. **双gyre海流案例**：以双gyre流动（海洋混合的经典模型）为例，验证了从高维数据中发现本征函数并实现反馈控制的全流程。

5. **隐式本征函数发现**：提出不需要显式构建Koopman矩阵，而是通过隐式方程直接求解本征函数的算法，提高了数值稳定性。

## 🏗️ 5. 方法详解（Methodology）

### Koopman算子理论基础

对于离散动力学$x_{k+1} = F(x_k)$，Koopman算子$K$作用于观测函数$g: M \to \mathbb{R}$：

$$Kg = g \circ F$$

即$K$将函数$g$映射为$g$在流$F$作用下的值。Koopman本征函数$\phi(x)$满足：

$$K \phi = \lambda \phi \quad \text{或} \quad \phi(F(x)) = \lambda \phi(x)$$

本征函数在由其张成的子空间中，动力学完全线性——这是KRONIC的核心物理基础。

### EDMD及其闭包问题

扩展动态模态分解（EDMD）通过求解最小二乘问题近似Koopman算子矩阵$K$：

$$K = \arg\min_{\tilde{K}} \| \Psi(X') - \tilde{K} \Psi(X) \|_F^2$$

其中$\Psi(X)$为观测函数在数据点上的堆叠。由于基函数空间的有限性，$K$通常不能保证是Koopman不变子空间上的精确表示，产生虚假本征值/函数。

### 稀疏正则化EDMD

为解决闭包问题，论文提出：
- 在EDMD矩阵$K$上施加稀疏惩罚，引导$K$趋向块对角/近似对角结构
- 通过交叉验证判断哪些本征函数对动力学具有真实描述能力
- 仅保留被经验证的"轻阻尼"本征函数构建降阶模型

### KRONIC控制架构

1. **本征函数发现**：从数据用EDMD/稀疏EDMD识别Koopman本征函数
2. **本征函数验证**：检查$\phi(x(t))$的演化和$\lambda^t \phi(x(0))$的一致性，剔除虚假本征函数
3. **内坐标构建**：用经验证的本征函数构成Koopman不变子空间
4. **LQR控制器设计**：在$z = \Phi(x)$（$\Phi$为本征函数映射）中设计线性最优控制器
5. **物理实施**：将控制律$u = -C' z$映射回原状态空间，在原系统中实施

### 轻阻尼本征函数

本征值的模$|\lambda| \approx 1$（或阻尼极小）对应准守恒量。论文证明轻阻尼本征函数通常不被有限维近似中的数值误差破坏，是构建可靠降阶模型的关键。在Hamiltonian系统中，Hamiltonian本身就是一个轻阻尼本征函数（对应$\lambda = 1$）。


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: 未明确说明（本文方法基于EDMD和稀疏回归，属于轻量级矩阵运算，通常在CPU上即可完成，无需高端GPU加速）
- GPU数量: 未使用GPU
- 训练时间: 未明确说明（EDMD和稀疏回归的计算时间通常在秒级到分钟级，取决于系统维度和数据量）

### 数据集（Datasets）
1. **慢流形系统（Slow Manifold System）**
   - 来源: 人工构造的解析示例系统
   - 任务: 验证Koopman本征函数发现方法的闭包问题
   - 数据规模: 低维系统（2维状态），轨迹数据点数百至数千
   - 是否公开: 不确定（解析系统可自行实现）

2. **哈密顿系统（Hamiltonian Systems）**
   - 来源: 人工构造的保守系统（如范德波尔振子等）
   - 任务: 验证轻阻尼本征函数的识别与控制
   - 数据规模: 低维系统，数据规模较小
   - 是否公开: 不确定

3. **双涡系统（Double Gyre）**
   - 来源: 流体力学标准基准模型，用于模拟海洋混合
   - 任务: 高维系统上的Koopman控制验证
   - 数据规模: 空间网格128×256或类似分辨率，时间序列数千步
   - 是否公开: 不确定（可自行实现标准双涡模型）

### 数据处理
- 通过数值积分生成系统轨迹数据（如Runge-Kutta方法）
- 构建状态-未来状态快照矩阵用于EDMD回归
- 采用稀疏回归（SINDy/稀疏优化）识别Koopman本征函数
- 本征函数验证：检查线性演化特性 φ(x(t)) ≈ e^(λt)φ(x(0))

### 复现难度
- ★★★☆☆（中等）
- 原因：作者提供了GitHub代码仓库（KRONIC），但主要实验使用自定义生成的合成数据，缺乏公开的标准数据集；方法实现需要一定的动力系统背景知识；双涡系统等应用需熟悉计算流体力学仿真流程


## 📐 6. 数学与物理建模（Math & Physics）

### 控制-仿射系统的本征函数动力学

对于控制-仿射系统：

$$\dot{x} = f(x) + \sum_{i=1}^q b_i(x) u_i$$

本征函数演化方程为：

$$\dot{\phi}(x) = \lambda \phi(x) + \nabla \phi(x) \cdot \sum_{i=1}^q b_i(x) u_i$$

即：在本征函数坐标中，控制项表现为线性（或双线性）项，使得标准LQR理论可以直接应用。

### 双gyre流动模型

双gyre是二维非定常流的经典模型，常用于描述海洋大尺度环流和涡旋动力学：

$$\dot{x} = -\pi A \sin(\pi f(x,t)) \frac{\partial f}{\partial x} + \pi A \cos(\pi f(x,t)) \frac{\partial f}{\partial y}$$
$$\dot{y} = \pi A \cos(\pi f(x,t)) \frac{\partial f}{\partial y} + \pi A \sin(\pi f(x,t)) \frac{\partial f}{\partial y}$$

其中$f(x,t) = \epsilon \sin(\omega t) x^2 + (1 - 2\epsilon \sin(\omega t)) x$描述了随时间变化的流场结构。该系统是研究海洋中尺度涡旋能量输运的理想测试平台。

### 线性二次调节器（LQR）

在Koopman本征函数坐标$z = \Phi(x)$中，最优控制问题变为：

$$J = \frac{1}{2} \int_0^\infty (z^T Q z + u^T R u) dt$$

其最优反馈控制为：

$$u = -R^{-1} B'^T P z$$

其中$P$满足连续时间Riccati方程$A'^T P + P A' - P B' R^{-1} B'^T P + Q = 0$，而$A' = \text{diag}(\lambda_1, ..., \lambda_r)$为由本征值构成的对角矩阵。

## 📊 7. 实验分析（Experiments）

### 慢流形系统（验证闭包问题）

- **系统**：$\dot{x}_1 = \nu x_1, \quad \dot{x}_2 = \eta(x_2 - x_1^2)$（慢流形）
- **验证**：在多项式基函数（最多3次）下，EDMD产生虚假本征函数；通过验证发现仅有少数本征函数（对应慢流形结构）可靠
- **关键发现**：当基函数不能闭合时（高阶项"逃逸"出基函数空间），产生虚假模式

### Hamiltonian系统

- **单摆、双摆、Kepler问题**：验证轻阻尼本征函数与守恒量（能量）的对应关系
- **结果**：稀疏EDMD能够准确识别Hamiltonian对应的主本征函数（$\lambda \approx 1$），并在此基础上设计的LQR控制器能有效控制系统的周期运动

### 双势阱（Basin-Hopping）

- **系统**：非对称双势阱$\dot{x} = -\nabla V(x)$ with $V(x) = x^4 - x^2 + \alpha x$
- **目标**：控制初始状态从一个吸引域跳到另一个吸引域
- **结果**：KRONIC通过识别相关本征函数，在本征函数空间设计切换控制，比直接在工作空间设计需更少的控制能量

### 双Gyre海流（Ocean Mixing）

- **系统**：周期性强迫的双gyre流动，状态维数为2D空间网格点（实验中用100×50=5000维全阶模型）
- **控制输入**：施加在流场上的周期性体积力
- **目标**：通过控制改变流场的能量分布或涡旋结构
- **结果**：KRONIC在约10维本征函数空间中构建LQR控制器，成功实现目标追踪任务，计算成本比全阶最优控制低2个数量级

## 🔍 8. 优缺点分析（Critical Review）

**优点**：
- 首次系统性地将Koopman本征函数验证与控制设计结合，解决了EDMD长期存在的闭包问题
- 通过稀疏回归发现本征函数，提供了自动化、可解释的模型发现流程
- KRONIC将非线性控制问题转化为线性控制问题，继承了LQR/LQG等成熟理论的所有优势
- 双gyre实验证明了从高维海洋流模型中提取有效低维控制策略的可行性
- 代码开源（KRONIC GitHub），便于复现和扩展

**缺点**：
- 本征函数的稀疏回归需要事先指定候选基函数库，基函数的选择仍依赖专家知识
- 本征函数验证目前依赖人工判断，缺乏完全自动化的判别标准
- 轻阻尼本征函数的识别在噪声数据中可能不稳定
- 控制-仿射形式的假设限制了方法对一般形式非仿射控制问题的适用性
- 在高维本征函数空间（r较大）时，LQR的 Riccati方程求解仍可能面临计算挑战

## 💡 9. 对我的启发（For My Research）

1. **海洋动力学低维建模**：海洋流动具有强非线性，但可能存在少数主导的低维Koopman本征函数/模态。KRONIC方法启示我，可以从海洋模式输出数据中提取这些低维不变量，用来进行快速的海洋状态预测和反馈控制。

2. **海洋数据同化的新视角**：传统EnKF将非线性问题局部线性化，而Koopman方法提供了全局线性嵌入的可能性。两者结合（用EnKF估计Koopman坐标中的状态）是一个值得探索的方向。

3. **控制-数据联合学习**：KRONIC通过数据驱动发现本征函数，然后设计控制器。这与我的研究中"既需要精确模拟海洋物理，又需要优化控制策略"的双重目标高度吻合。

4. **轻阻尼模态的特殊价值**：论文指出轻阻尼本征函数（如Hamiltonian）具有更强的数值稳健性。在海洋中，对应于准守恒量（如位势涡度、能量）的模态可能同样更易于识别和利用。

5. **稀疏回归的工具性**：将稀疏回归方法（论文中用的LASSO类方法）引入海洋数据的低秩表示学习，可以帮助我从海量卫星和现场观测数据中自动提取主导模态。

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **海洋EnKF + Koopman混合架构**：用EnKF估计Koopman本征函数坐标中的状态，同时利用Koopman线性动力学进行外推预测。

2. **海表高度/温盐场的本征函数提取**：利用Argo浮标和卫星高度计数据，构建西北太平洋或北极海域的Koopman本征函数库，服务于海洋预报和目标性观测优化。

3. **数据驱动海洋反馈控制**：将KRONIC框架应用于实际海洋控制问题，如基于AUV（自主水下航行器）的海洋采样路径优化，或基于水下滑翔器的海洋参数反馈控制。

4. **稀疏Koopman的深度学习增强**：用神经网络（如ResNet）作为Koopman的基函数库，结合稀疏回归，发现更具表达能力的非线性本征函数，解决浅水/深海交界面的强非线性问题。

5. **不确定性量化**：在Koopman本征函数框架中引入贝叶斯推断，对本征函数和对应的本征值进行不确定性估计，增强控制器的鲁棒性。

## 🧾 11. 引用格式（BibTex）

```bibtex
@article{Kaiser2017KRONIC,
  title={Data-driven discovery of Koopman eigenfunctions for control},
  author={Kaiser, Eurika and Kutz, J. Nathan and Brunton, Steven L.},
  journal={IEEE Transactions on Automatic Control},
  year={2017},
  note={arXiv:1707.01146}
}
```
