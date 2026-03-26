# -*- coding: utf-8 -*-
"""论文数据模型"""

from dataclasses import dataclass, field, asdict
from typing import List, Optional
from datetime import datetime


@dataclass
class PaperMetadata:
    """论文元数据"""
    title: str
    arxiv_id: str
    authors: List[str]
    year: int
    source: str = "arXiv"
    venue: Optional[str] = None
    doi: Optional[str] = None
    abstract: str = ""
    method_tags: List[str] = field(default_factory=list)
    application_tags: List[str] = field(default_factory=list)
    date_collected: str = ""
    paper_url: str = ""
    pdf_url: str = ""

    def __post_init__(self):
        if not self.date_collected:
            self.date_collected = datetime.now().strftime("%Y-%m-%d")
        if self.arxiv_id and not self.paper_url:
            self.paper_url = f"https://arxiv.org/abs/{self.arxiv_id}"
        if self.arxiv_id and not self.pdf_url:
            self.pdf_url = f"https://arxiv.org/pdf/{self.arxiv_id}.pdf"

    def to_dict(self) -> dict:
        return asdict(self)

    @property
    def short_name(self) -> str:
        """生成短名称（URL-safe）"""
        # 移除特殊字符，只保留字母数字和连字符
        name = self.title.lower()
        # 移除常见前缀
        for prefix in ["a ", "an ", "the "]:
            if name.startswith(prefix):
                name = name[len(prefix):]
        # 只保留字母数字和空格
        import re
        name = re.sub(r'[^a-z0-9\s-]', '', name)
        # 替换空格为下划线，取前50字符
        name = '_'.join(name.split())[:50]
        return name

    def to_yaml_front_matter(self) -> str:
        """生成 YAML front matter"""
        import yaml
        data = {
            'title': self.title,
            'arXiv': self.arxiv_id,
            'authors': self.authors,
            'year': self.year,
            'source': self.source,
            'method_tags': self.method_tags,
            'application_tags': self.application_tags,
            'date_collected': self.date_collected,
        }
        if self.venue:
            data['venue'] = self.venue
        if self.doi:
            data['doi'] = self.doi

        yaml_str = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False)
        return f"---\n{yaml_str}---\n"

    def to_markdown(self, include_abstract: bool = True) -> str:
        """生成带 YAML front matter 的 Markdown 内容"""
        content = self.to_yaml_front_matter()
        content += f"# {self.title}\n\n"
        content += "## 基本信息\n\n"
        content += f"- **arXiv**: [{self.arxiv_id}]({self.paper_url})\n"
        if self.venue:
            content += f"- **发表**: {self.venue}\n"
        content += f"- **作者**: {', '.join(self.authors[:5])}"
        if len(self.authors) > 5:
            content += f" et al."
        content += "\n"
        content += f"- **年份**: {self.year}\n"
        content += f"- **来源**: {self.source}\n\n"

        if include_abstract and self.abstract:
            content += "## 摘要\n\n"
            content += self.abstract[:500]  # 截取前500字符
            if len(self.abstract) > 500:
                content += "..."
            content += "\n\n"

        if self.method_tags or self.application_tags:
            content += "## 标签\n\n"
            if self.method_tags:
                content += f"**方法**: {', '.join(self.method_tags)}\n"
            if self.application_tags:
                content += f"**应用**: {', '.join(self.application_tags)}\n"

        return content


def extract_tags_from_text(text: str, tag_dict: dict) -> List[str]:
    """从文本中提取标签"""
    text_lower = text.lower()
    found_tags = []

    for tag, keywords in tag_dict.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                found_tags.append(tag)
                break

    return found_tags
