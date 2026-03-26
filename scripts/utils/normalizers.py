# -*- coding: utf-8 -*-
"""共享的规范化函数"""

import re
from typing import Optional


def normalize_arxiv(arxiv: str) -> Optional[str]:
    """规范化 arXiv ID，移除无效字符，返回清理后的ID或None"""
    if not arxiv or arxiv in ['待补充', 'XXXXX', 'Not available', '', 'Not Available']:
        return None
    arxiv = arxiv.replace('_', '.')
    arxiv_clean = re.sub(r'v\d+$', '', arxiv).strip('.')
    if re.match(r'^\d{2}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    if re.match(r'^\d{4}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    if re.match(r'^\d{2}\.\d{4,5}v\d+$', arxiv):
        return arxiv_clean
    if re.match(r'^\d{4}\.\d{4,5}v\d+$', arxiv):
        return arxiv_clean
    return None


def normalize_tag(tag: str) -> str:
    """规范化标签，移除下划线转为连字符，转小写用于匹配"""
    return tag.replace('_', '-').lower()


def normalize_venue(venue: str) -> str:
    """规范化发表平台/期刊名称"""
    if not venue or venue == '-':
        return ''
    return venue.strip()
