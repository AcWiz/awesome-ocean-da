## 投稿PR检查清单

在提交PR之前，请确认以下所有项目：

### 必需文件
- [ ] `papers/[年份]/[论文简称]/abstract.md` 存在
- [ ] `papers/[年份]/[论文简称]/summary.md` 存在（与abstract.md内容一致）
- [ ] 已更新 `papers/[年份]/index.md` 添加新论文

### Frontmatter 必填字段
- [ ] `title`: 论文标题（使用英文引号包围）
- [ ] `arXiv`: 有效的arXiv ID格式（如 `2503.19160`）
- [ ] `authors`: 作者列表（JSON数组格式）
- [ ] `year`: 论文年份（数字）
- [ ] `source`: 来源（如 `arXiv`）
- [ ] `venue`: 发表场所（如 `arXiv`、`Nature`、`Science`）
- [ ] `method_tags`: 方法标签（至少一个）
- [ ] `application_tags`: 应用标签（至少一个）
- [ ] `difficulty`: 难度等级（如 `★★★☆☆`）
- [ ] `importance`: 重要程度（如 `★★★★☆`）

### method_tags 自检清单（选择适用的）
请确认论文使用了以下方法之一，并在PR中说明：

- [ ] **PINN** - 物理信息神经网络（Physics-Informed Neural Networks）
- [ ] **Koopman** - Koopman学习/算子理论
- [ ] **Neural-Operator** - 神经算子（FNO、DeepONet等）
- [ ] **GNN** - 图神经网络
- [ ] **Transformer** - Transformer/Attention机制
- [ ] **4D-Var** - 四维变分同化
- [ ] **EnKF** - 集合卡尔曼滤波
- [ ] **Deep-Learning** - 通用深度学习方法
- [ ] **Physics-Informed** - 物理约束/物理先验
- [ ] **Other**: _______________

### application_tags 自检清单（选择适用的）
请确认论文涉及以下应用之一，并在PR中说明：

- [ ] **SST** - 海表温度（Sea Surface Temperature）
- [ ] **SSH** - 海表高度（Sea Surface Height）
- [ ] **ENSO** - ENSO预测
- [ ] **Wave** - 海浪预报
- [ ] **Global-Forecast** - 全球预报
- [ ] **Regional-Forecast** - 区域预报
- [ ] **Ocean-DA** - 海洋数据同化
- [ ] **Deep-Ocean** - 深海/次表层
- [ ] **Climate** - 气候研究
- [ ] **Other**: _______________

### 内容质量
- [ ] `abstract.md` 包含中文总结
- [ ] TL;DR 部分准确反映论文核心贡献
- [ ] 标签与论文实际方法/应用相符

### 提交信息格式
```
feat: 添加 [论文简称] (arXiv: XXXX.XXXXX)

- 方法: [主要方法标签]
- 应用: [主要应用标签]
- 年份: YYYY
```

---

**论文信息**

- 论文标题: _______________
- arXiv ID: _______________
- 主要方法: _______________
- 主要应用: _______________
- 投稿人: @___________
