#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""迁移 abstract.md 到新的模板格式

用法:
    python scripts/migrate_abstract_format.py --dry-run  # 预览
    python scripts/migrate_abstract_format.py --apply    # 执行迁移
    python scripts/migrate_abstract_format.py --check     # 检查完整性
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml


# 默认值
DEFAULTS = {
    'venue': 'arXiv',
    'domain_tags': [],
    'ocean_vars': 'Unknown',
    'spatiotemporal_res': 'Unknown',
    'difficulty': '★★★☆☆',
    'importance': '★★★☆☆',
    'read_status': 'skim',
}


def parse_front_matter(content: str) -> Tuple[Optional[Dict], Optional[str]]:
    """解析 YAML front matter"""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return None, content
    yaml_str = match.group(1)
    try:
        data = yaml.safe_load(yaml_str)
        body = content[match.end():]
        return data, body
    except yaml.YAMLError:
        return None, content


def migrate_front_matter(old_data: Dict) -> Dict:
    """将旧格式映射到新格式"""
    new_data = {
        'title': old_data.get('title', 'Unknown'),
        'arXiv': old_data.get('arXiv', ''),
        'authors': old_data.get('authors', []),
        'year': old_data.get('year', 2024),
        'source': old_data.get('source', 'arXiv'),
        'venue': old_data.get('venue', DEFAULTS['venue']),
        'domain_tags': old_data.get('method_tags', DEFAULTS['domain_tags']),
        'ocean_vars': _map_application_tags(old_data.get('application_tags', [])),
        'spatiotemporal_res': DEFAULTS['spatiotemporal_res'],
        'difficulty': DEFAULTS['difficulty'],
        'importance': DEFAULTS['importance'],
        'read_status': DEFAULTS['read_status'],
    }
    return new_data


def _map_application_tags(app_tags: List[str]) -> str:
    """将 application_tags 映射为 ocean_vars 字符串"""
    if not app_tags:
        return 'Unknown'
    # 常见海洋变量映射
    var_mapping = {
        'SST': 'Sea Surface Temperature',
        'SSH': 'Sea Surface Height',
        'SSS': 'Sea Surface Salinity',
        'ocean': 'Ocean State',
        'Ocean-DA': 'Ocean State',
        'Ocean': 'Ocean State',
        'Global-Forecast': 'Global Ocean',
        'Regional-Forecast': 'Regional Ocean',
        'ENSO': 'ENSO',
        'Wave': 'Ocean Waves',
        'Sea-Ice': 'Sea Ice',
        'Marine': 'Marine Ecosystem',
        'Turbulence': 'Turbulence',
    }
    result = []
    for tag in app_tags:
        if tag in var_mapping:
            result.append(var_mapping[tag])
        elif tag not in result:
            result.append(tag)
    return ', '.join(result) if result else 'Unknown'


def format_front_matter(data: Dict) -> str:
    """格式化为 YAML front matter"""
    # 构建 authors 列表字符串
    authors_str = '\n'.join(f'- {a}' for a in data.get('authors', []))

    # domain_tags 列表字符串
    domain_tags = data.get('domain_tags', [])
    domain_tags_str = '\n'.join(f'- {t}' for t in domain_tags) if domain_tags else '- '

    lines = [
        '---',
        f"title: '{data.get('title', 'Unknown')}'",
        f"arXiv: '{data.get('arXiv', '')}'",
        'authors:',
        authors_str,
        f"year: {data.get('year', 2024)}",
        f"source: {data.get('source', 'arXiv')}",
        f"venue: {data.get('venue', 'arXiv')}",
        'domain_tags:',
        domain_tags_str,
        f"ocean_vars: {data.get('ocean_vars', 'Unknown')}",
        f"spatiotemporal_res: {data.get('spatiotemporal_res', 'Unknown')}",
        f"difficulty: {data.get('difficulty', '★★★☆☆')}",
        f"importance: {data.get('importance', '★★★☆☆')}",
        f"read_status: {data.get('read_status', 'skim')}",
        '---',
    ]
    return '\n'.join(lines)


def convert_body_to_new_format(body: str, old_data: Dict) -> str:
    """将旧格式 body 转换为新格式"""
    # 提取标题（从 body 第一行）
    title = old_data.get('title', '')
    lines = body.strip().split('\n')

    # 跳过旧的"基本信息"部分，找到中文总结
    new_body_parts = [f'# {title}\n']

    # 查找中文总结部分
    chinese_summary_start = -1
    for i, line in enumerate(lines):
        if '## 中文总结' in line or '## 摘要' in line:
            chinese_summary_start = i + 1
            break

    if chinese_summary_start > 0:
        # 提取中文总结内容
        summary_lines = []
        for line in lines[chinese_summary_start:]:
            if line.startswith('## ') or (line.startswith('# ') and not summary_lines):
                break
            if line.strip() and not line.startswith('**'):
                summary_lines.append(line)
            elif line.startswith('**'):
                summary_lines.append(line)

        if summary_lines:
            new_body_parts.append('\n## TL;DR\n')
            # 合并为一个段落作为 TL;DR
            summary_text = ' '.join(s.strip() for s in summary_lines if s.strip())
            new_body_parts.append(f'> {summary_text[:200]}...\n')

    # 添加占位符 sections
    new_body_parts.extend([
        '\n## 研究问题\n',
        '> 本文要解决什么问题？研究动机是什么？\n',
        '\n## 核心贡献\n',
        '> 3-5 个关键贡献点\n\n',
        '1. \n',
        '2. \n',
        '3. \n',
        '\n## 方法详解\n',
        '> 核心方法的详细描述\n',
        '\n## 数学/物理建模\n',
        '> 关键公式和物理意义\n',
        '\n## 实验分析\n',
        '> 实验设置、结果和发现\n',
        '\n## 优缺点\n',
        '**优点：**\n',
        '- \n',
        '\n**缺点：**\n',
        '- \n',
        '\n## 工程落地\n',
        '> 实际应用场景和可行性\n',
        '\n## Idea 扩展\n',
        '> 可以借鉴到其他研究的想法\n',
        '\n## BibTeX\n',
        '```bibtex\n',
        '@article{},\n',
        '  title={},\n',
        '  author={},\n',
        '  journal={},\n',
        '  year={}\n',
        '}\n',
        '```\n',
    ])

    return '\n'.join(new_body_parts)


def migrate_file(file_path: Path, dry_run: bool = True) -> Tuple[bool, str]:
    """迁移单个文件"""
    try:
        content = file_path.read_text(encoding='utf-8')
        old_data, body = parse_front_matter(content)

        if old_data is None:
            return False, f"无法解析 front matter: {file_path}"

        new_data = migrate_front_matter(old_data)
        new_front_matter = format_front_matter(new_data)

        # 保留原有 body（不转换，因为转换会丢失信息）
        # 只在 --apply 模式下写入
        if not dry_run:
            new_content = new_front_matter + '\n\n' + body
            file_path.write_text(new_content, encoding='utf-8')

        return True, f"OK: {file_path}"
    except Exception as e:
        return False, f"错误 {file_path}: {e}"


def find_abstract_files(base_dir: Path) -> List[Path]:
    """查找所有 abstract.md 文件"""
    return sorted((base_dir / 'papers').glob('*/*/abstract.md'))


def main():
    parser = argparse.ArgumentParser(description='迁移 abstract.md 到新格式')
    parser.add_argument('--dry-run', action='store_true', help='预览模式')
    parser.add_argument('--apply', action='store_true', help='执行迁移')
    parser.add_argument('--check', action='store_true', help='检查完整性')
    parser.add_argument('--base-dir', type=str,
                        default='/home/fenglonghan/projects/ai-data-assimilation-papers',
                        help='项目根目录')
    args = parser.parse_args()

    if not args.dry_run and not args.apply and not args.check:
        parser.print_help()
        sys.exit(1)

    base_dir = Path(args.base_dir)
    abstract_files = find_abstract_files(base_dir)

    print(f"找到 {len(abstract_files)} 个 abstract.md 文件\n")

    if args.check:
        # 检查模式：统计字段缺失情况
        missing_stats = {
            'venue': 0,
            'ocean_vars': 0,
            'spatiotemporal_res': 0,
            'difficulty': 0,
            'importance': 0,
            'read_status': 0,
        }
        empty_domain_tags = 0

        for f in abstract_files:
            content = f.read_text(encoding='utf-8')
            data, _ = parse_front_matter(content)
            if data:
                if data.get('venue') in [None, '', 'Unknown', 'arXiv']:
                    missing_stats['venue'] += 1
                if data.get('spatiotemporal_res', 'Unknown') == 'Unknown':
                    missing_stats['spatiotemporal_res'] += 1
                if data.get('difficulty', '★★★☆☆') == '★★★☆☆':
                    missing_stats['difficulty'] += 1
                if data.get('importance', '★★★☆☆') == '★★★☆☆':
                    missing_stats['importance'] += 1
                if data.get('read_status', 'skim') == 'skim':
                    missing_stats['read_status'] += 1
                if not data.get('domain_tags'):
                    empty_domain_tags += 1

        print("=== 字段完整性统计 ===")
        for field, count in missing_stats.items():
            print(f"  {field}: {count}/{len(abstract_files)}")
        print(f"  empty domain_tags: {empty_domain_tags}/{len(abstract_files)}")
        return

    # Dry-run 或 Apply 模式
    success_count = 0
    fail_count = 0

    for f in abstract_files:
        if args.dry_run:
            ok, msg = migrate_file(f, dry_run=True)
            print(msg)
            if ok:
                success_count += 1
            else:
                fail_count += 1
        elif args.apply:
            ok, msg = migrate_file(f, dry_run=False)
            if ok:
                success_count += 1
            else:
                print(f"失败: {msg}")
                fail_count += 1

    print(f"\n完成: 成功 {success_count}, 失败 {fail_count}")

    if args.apply:
        print("\n注意：原有中文总结内容已保留在正文中。")
        print("建议人工补充以下字段：ocean_vars, spatiotemporal_res, difficulty, importance")


if __name__ == '__main__':
    main()
