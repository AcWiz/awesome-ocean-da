# Scripts 目录

论文搜集和管理工具集。

## 目录结构

```
scripts/
├── README.md                    # 本文档
├── run_tests.py                 # 测试套件
├── search_strategy.py            # 搜索策略配置
├── requirements.txt              # Python 依赖
├── utils/                       # 共享工具模块
│   ├── __init__.py
│   ├── normalizers.py           # normalize_arxiv, normalize_tag, normalize_venue
│   ├── tag_config.py           # TAG_CATEGORIES, TAG_ALIASES, get_canonical_tag
│   └── paper_schema.py         # PaperMetadata dataclass
├── collection/                  # 论文采集
├── site_generation/            # 静态网站生成
├── validation/                  # 数据质量检查
├── repair/                      # 修复工具
├── one_time/                    # 一次性迁移脚本
└── ai_generation/              # LLM 生成工具
```

## 模块说明

### utils/ - 共享工具模块

```python
from scripts.utils.normalizers import normalize_arxiv, normalize_tag, normalize_venue
from scripts.utils.tag_config import TAG_CATEGORIES, TAG_ALIASES, get_canonical_tag
from scripts.utils.paper_schema import PaperMetadata, extract_tags_from_text
```

| 文件 | 内容 |
|------|------|
| `normalizers.py` | `normalize_arxiv()`, `normalize_tag()`, `normalize_venue()` |
| `tag_config.py` | `TAG_CATEGORIES`, `TAG_ALIASES`, `get_canonical_tag()` |
| `paper_schema.py` | `PaperMetadata` dataclass, `extract_tags_from_text()` |

---

### collection/ - 论文采集

| 脚本 | 说明 |
|------|------|
| `collect_papers.py` | 从 arXiv 搜集 AI+海洋数据同化相关论文 |
| `fetch_arxiv_metadata.py` | 从 arXiv 获取论文元数据并更新 abstract.md |
| `fetch_venue_from_doi.py` | 从 DOI 获取正式 venue 信息并更新论文元数据 |

**使用示例:**
```bash
# 采集论文（默认最多5篇）
python scripts/collection/collect_papers.py

# 采集论文（指定数量）
python scripts/collection/collect_papers.py --max-results 10 --dry-run

# 获取 venue 信息
python scripts/collection/fetch_venue_from_doi.py --dry-run
python scripts/collection/fetch_venue_from_doi.py --loop --limit 20
```

---

### site_generation/ - 静态网站生成

| 脚本 | 说明 |
|------|------|
| `update_index.py` | 更新 Jekyll 索引文件 `_data/papers.json` |
| `generate_tag_pages_from_json.py` | 从 papers.json 生成标签分类页面 |
| `generate_year_pages.py` | 为每个年份生成索引页面 |
| `regenerate_main_readme.py` | 从 papers.json 生成主页 README |

**使用示例:**
```bash
# 推荐执行顺序：采集 → 更新索引 → 生成页面

# 1. 更新索引
python scripts/site_generation/update_index.py

# 2. 生成标签页
python scripts/site_generation/generate_tag_pages_from_json.py

# 3. 生成年份页
python scripts/site_generation/generate_year_pages.py

# 4. 重新生成主页 README
python scripts/site_generation/regenerate_main_readme.py
```

---

### validation/ - 数据质量检查

| 脚本 | 说明 |
|------|------|
| `validate_arxiv_links.py` | 验证 arXiv 链接的有效性 |
| `validate_local_links.py` | 验证本地链接的有效性 |
| `validate_venue_data.py` | 验证 Venue 数据质量并生成报告 |
| `comprehensive_audit.py` | 全面审核论文库的所有信息正确性 |

**使用示例:**
```bash
# 验证 arXiv 链接
python scripts/validation/validate_arxiv_links.py

# 验证本地链接
python scripts/validation/validate_local_links.py

# 验证 Venue 数据
python scripts/validation/validate_venue_data.py
python scripts/validation/validate_venue_data.py --check-consistency

# 全面审核
python scripts/validation/comprehensive_audit.py
```

---

### repair/ - 修复工具

| 脚本 | 说明 |
|------|------|
| `fix_arxiv_links.py` | 修复所有文件中的 arXiv 链接格式 |
| `fix_abstract_frontmatter.py` | 修复 abstract.md 中的 frontmatter 格式问题 |
| `fix_bibtex_venue.py` | 修复 BibTeX 中错误的 journal 字段 |

**使用示例:**
```bash
# 修复 arXiv 链接格式
python scripts/repair/fix_arxiv_links.py

# 修复 frontmatter 格式
python scripts/repair/fix_abstract_frontmatter.py --dry-run

# 修复 BibTeX venue
python scripts/repair/fix_bibtex_venue.py --dry-run --verbose
```

---

### one_time/ - 一次性迁移脚本

| 脚本 | 说明 |
|------|------|
| `fill_arxiv_ids.py` | 生成缺失 arXiv ID 的报告，用于手动补充 |
| `translate_tags.py` | 将 README 中的标签从英文翻译为中文 |

**使用示例:**
```bash
# 生成缺失 arXiv ID 报告
python scripts/one_time/fill_arxiv_ids.py

# 翻译标签（预览）
python scripts/one_time/translate_tags.py --dry-run --verbose

# 翻译标签（执行）
python scripts/one_time/translate_tags.py --verbose
```

---

### ai_generation/ - LLM 生成工具（需 API Key）

| 脚本 | 说明 |
|------|------|
| `generate_chinese_summary.py` | 使用 Claude API 生成中文 summary.md |
| `regenerate_abstracts.py` | 使用 MiniMax API 生成新模板内容 |

**使用示例:**
```bash
# 生成中文 summary（需设置 ANTHROPIC_API_KEY）
export ANTHROPIC_API_KEY=sk-ant-...
python scripts/ai_generation/generate_chinese_summary.py --dry-run
python scripts/ai_generation/generate_chinese_summary.py --limit 5

# 重新生成摘要（需设置 MINIMAX_API_KEY）
export MINIMAX_API_KEY=...
python scripts/ai_generation/regenerate_abstracts.py --dry-run
python scripts/ai_generation/regenerate_abstracts.py --apply --limit 10
```

---

## 测试

运行测试套件:
```bash
# 运行所有测试
python scripts/run_tests.py

# 详细输出
python scripts/run_tests.py --verbose

# 只运行特定测试
python scripts/run_tests.py -t T1
```

测试列表:
- T1: arXiv ID 格式验证
- T2: papers.json 完整性验证
- T3: arXiv 链接有效性验证
- T4: 标签页格式验证
- T5: 标签页论文完整性验证
- T6: 年份页面有效性验证
- T7: README 有效性验证
- T8: 本地链接完整性验证

---

## 推荐的脚本执行顺序

### 日常维护（采集新论文）

```
1. python scripts/collection/collect_papers.py --max-results 5
2. python scripts/site_generation/update_index.py
3. python scripts/site_generation/generate_tag_pages_from_json.py
4. python scripts/site_generation/generate_year_pages.py
5. python scripts/site_generation/regenerate_main_readme.py
```

### 获取正式 Venue

```
1. python scripts/collection/fetch_venue_from_doi.py --loop --limit 20
2. python scripts/site_generation/update_index.py
3. python scripts/site_generation/regenerate_main_readme.py
```

### 定期审核

```
1. python scripts/validation/validate_arxiv_links.py
2. python scripts/validation/validate_local_links.py
3. python scripts/validation/validate_venue_data.py --check-consistency
4. python scripts/validation/comprehensive_audit.py
```

---

## 注意事项

- **API Key 依赖**: `generate_chinese_summary.py` 需要 `ANTHROPIC_API_KEY`，`regenerate_abstracts.py` 需要 `MINIMAX_API_KEY`
- **Jekyll 构建依赖**: `update_index.py` 和 `generate_tag_pages_from_json.py` 是 Jekyll 构建流程的一部分
- **修复工具**: 使用 `--dry-run` 参数预览更改，确认无误后再执行
- **Rate Limiting**: API 调用脚本内置延迟，避免超出限制
