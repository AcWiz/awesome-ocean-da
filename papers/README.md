# 海洋数据同化、预报论文索引

按年份索引所有收录的 AI + 海洋数据同化、预报论文。

## 论文 Abstract 模板

每篇论文的 `abstract.md` 使用统一的 YAML front matter 格式：

```yaml
---
title: '论文标题'
arXiv: 'arXiv ID'
authors:
- 作者1
- 作者2
year: 2024
source: arXiv
venue: arXiv  # 或会议/期刊名称
domain_tags:
- Deep-Learning
- Transformer
ocean_vars: Sea Surface Temperature  # 海洋变量
spatiotemporal_res: Unknown          # 时空分辨率
difficulty: '★★★☆☆'                  # 难度
importance: '★★★☆☆'                  # 重要性
read_status: skim                    # skim/read/important
---
```

### 字段说明

| 字段 | 说明 | 默认值 |
|------|------|--------|
| `title` | 论文标题 | 必填 |
| `arXiv` | arXiv ID | 必填 |
| `authors` | 作者列表 | 必填 |
| `year` | 发表年份 | 必填 |
| `source` | 来源 (arXiv/Conference/Journal) | `arXiv` |
| `venue` | 发表场所 | `arXiv` |
| `domain_tags` | 方法标签 | `[]` |
| `ocean_vars` | 海洋变量 | `Unknown` |
| `spatiotemporal_res` | 时空分辨率 | `Unknown` |
| `difficulty` | 难度 (★~★★★★★) | `★★★☆☆` |
| `importance` | 重要性 (★~★★★★★) | `★★★☆☆` |
| `read_status` | 阅读状态 (skim/read/important) | `skim` |

### 迁移说明

- 2026-03-21: 完成从旧格式（`method_tags`, `application_tags`）到新格式的批量迁移
- 旧字段 `method_tags` → 新字段 `domain_tags`
- 旧字段 `application_tags` → 新字段 `ocean_vars`（字符串）
- 原有中文总结内容已保留在正文中

## 2025 年 (6 篇)

| 论文 | arXiv | 关键词 |
|------|-------|--------|
| [Tensor-Var](./2025/Tensor-Var/) | 2503.XXXXX | 4D-Var, Kernel CME |
| [Neural Ocean Forecasting](./2025/Neural_Ocean_Forecasting/) | 2502.XXXXX | 神经海洋预报 |
| [Subregional Ocean Forecasting](./2025/Subregional_Ocean_Forecasting/) | 2501.XXXXX | 区域海洋预报 |
| [Stratified PINN DA](./2025/Stratified_PINN_DA/) | 2501.XXXXX | PINN, 深海 |
| [AI GCS DA](./2025/AI_GCS_DA/) | 2501.XXXXX | 地质碳存储 |
| [Generalizable Neural-Network Parameterization](./2025/Generalizable_Neural_Network_Parameterization/) | 2505.08900 | 物理约束神经网络参数化 |
| [Deep Learning Subregional Ocean Forecasting](./2025/deep-learning-subregional-ocean-forecasting-canary-current/) | 2505.24429 | 图神经网络, 亚区域海洋预报, 加那利洋流 |
| [Stratified PINN Deep Ocean DA](./2025/stratified-physics-informed-neural-network-data-assimilation/) | 2503.19160 | PINN, 深海数据同化, 海洋流重建 |

## 2024 年 (14 篇)

| 论文 | arXiv | 关键词 |
|------|-------|--------|
| [CGKN](./2024/CGKN/) | 2406.XXXXX | Koopman, 数据同化 |
| [Continuous Data Assimilation](./2024/Continuous_Data_Assimilation_Turbulence_Models/) | 2405.XXXXX | 湍流模型 |
| [Deep Koopman Learning Noisy Data](./2024/Deep_Koopman_Learning_Noisy_Data/) | 2405.16649 | Koopman, 噪声数据 |
| [Deep Learning ENSO Forecast](./2024/Deep_Learning_ENSO_Forecast/) | 2406.XXXXX | ENSO, 深度学习 |
| [Deep Learning Model Correction](./2024/Deep_Learning_Model_Correction_Dynamical_Systems/) | 2404.XXXXX | 模型校正 |
| [DUNE Climate Forecasting](./2024/DUNE_Climate_Forecasting/) | 2403.XXXXX | 气候预报 |
| [FuXi-DA](./2024/FuXi-DA/) | 2401.XXXXX | 卫星观测 |
| [Koopman-based Deep Learning](./2024/koopman-based-deep-learning-nonlinear-system-estimation/) | 2405.00627 | Koopman, 非线性系统 |
| [LangYa Ocean Forecasting](./2024/LangYa_Cross_Spatiotemporal_Ocean_Forecasting/) | 2406.XXXXX | 海浪预报 |
| [Machine Learning Inverse Problems DA](./2024/Machine_Learning_Inverse_Problems_DA/) | 2402.XXXXX | 逆问题 |
| [OceanCastNet Wave Forecasting](./2024/OceanCastNet_Wave_Forecasting/) | 2406.03848 | 海浪预报深度学习 |
| [Semilinear Neural Operators](./2024/Semilinear_Neural_Operators/) | 2401.XXXXX | 神经算子 |
| [CG-EnKF Data Assimilation](./2024/conditional-gaussian-ensemble-kalman-filtering/) | 2409.14300 | 条件高斯 EnKF, 非线性数据同化 |
| [Tropical Pacific Ocean DA](./2024/Tropical_Pacific_Ocean_DA/) | 2402.XXXXX | 太平洋, 上层海洋 |
| [Validating DL Weather Forecast](./2024/validating-deep-learning-weather-forecast-models/) | 2404.17652 | 深度学习天气预报验证 |

## 2023 年 (2 篇)

| 论文 | arXiv | 关键词 |
|------|-------|--------|
| [Graph SST Forecast](./2023/Graph_SST_Forecast/) | 2309.XXXXX | 图神经网络, SST |
| [Echo-State DA](./2023/Echo_State_DA/) | 2305.XXXXX | 回声状态网络 |

## 2022 年 (3 篇)

| 论文 | arXiv | 关键词 |
|------|-------|--------|
| [Deep Learning EnKF](./2022/deep-learning-enhanced-ensemble-based-data-assimilation/) | 2206.04811 | 深度学习增强EnKF |
| [4D-SRDA](./2022/4D-SRDA/) | 2203.XXXXX | 时空超分辨率 |
| [Ocean Observations Expansion](./2022/Ocean_Observations_Expansion/) | 2201.XXXXX | 海洋观测扩展 |

---

*最后更新: 2026-03-21*
