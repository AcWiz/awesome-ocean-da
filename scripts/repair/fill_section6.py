#!/usr/bin/env python3
"""
Fill Section 6 (实验配置) for a single paper using LLM inference.

Reads abstract.md, extracts available info, calls LLM to infer Section 6 content,
and replaces the placeholder Section 6 with generated content.
"""

import argparse
import os
import re
import sys
import json
from pathlib import Path
from typing import Optional, Dict, Any

try:
    from anthropic import Anthropic
except ImportError:
    print("Error: anthropic package not installed. Install with: pip install anthropic")
    sys.exit(1)


PROJECT_ROOT = Path(__file__).parent.parent.parent


def get_api_key() -> str:
    """Get API key from environment or common locations."""
    for env_var in ["ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"]:
        api_key = os.environ.get(env_var, "")
        if api_key:
            return api_key

    env_locations = [
        Path.home() / ".env",
        Path.home() / ".claude" / "projects" / ".env",
        Path.home() / ".claude" / ".env",
    ]

    for env_path in env_locations:
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    if line.startswith("ANTHROPIC_API_KEY=") or line.startswith("ANTHROPIC_AUTH_TOKEN="):
                        return line.split("=", 1)[1].strip()

    return ""


def read_arxiv_content(abstract_path: Path) -> str:
    """Read arxiv_content.txt from the same directory as abstract.md."""
    arxiv_content_path = abstract_path.parent / "arxiv_content.txt"
    if arxiv_content_path.exists():
        try:
            return arxiv_content_path.read_text(encoding='utf-8')[:15000]
        except Exception:
            return ""
    return ""


def parse_abstract_md(abstract_path: Path) -> Dict[str, Any]:
    """Parse abstract.md to extract structured information."""
    if not abstract_path.exists():
        return {}

    content = abstract_path.read_text(encoding='utf-8')

    info = {
        'title': '',
        'arxiv': '',
        'authors': [],
        'year': '',
        'venue': '',
        'method_tags': [],
        'application_tags': [],
        'sections': {},
        'raw_content': content
    }

    # Parse YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1]
            for line in yaml_content.split('\n'):
                if ':' in line and not line.strip().startswith('#'):
                    key, val = line.split(':', 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")

                    if key == 'title':
                        info['title'] = val
                    elif key == 'arXiv':
                        info['arxiv'] = val
                    elif key == 'year':
                        info['year'] = val
                    elif key == 'venue':
                        info['venue'] = val
                    elif key == 'method_tags':
                        info['method_tags'] = [t.strip().strip('"').strip("'") for t in re.findall(r'["\']([^"\']+)["\']', val)]
                        if not info['method_tags']:
                            info['method_tags'] = [t.strip() for t in val.strip('[]').split(',')]
                    elif key == 'application_tags':
                        info['application_tags'] = [t.strip().strip('"').strip("'") for t in re.findall(r'["\']([^"\']+)["\']', val)]
                        if not info['application_tags']:
                            info['application_tags'] = [t.strip() for t in val.strip('[]').split(',')]

            # Parse authors
            yaml_lines = yaml_content.split('\n')
            in_authors = False
            authors_list = []
            for line in yaml_lines:
                if line.strip().startswith('authors:'):
                    in_authors = True
                    continue
                if in_authors:
                    if line.startswith('- '):
                        authors_list.append(line[2:].strip().strip('"').strip("'"))
                    elif line.startswith(' ') or line.startswith('\t'):
                        continue
                    else:
                        break
            if authors_list:
                info['authors'] = authors_list

    # Parse markdown sections
    body = parts[2] if content.startswith('---') and len(parts) >= 3 else content
    current_section = None
    current_content = []

    for line in body.split('\n'):
        if line.startswith('## '):
            if current_section:
                info['sections'][current_section] = '\n'.join(current_content).strip()
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)

    if current_section:
        info['sections'][current_section] = '\n'.join(current_content).strip()

    return info


def extract_section_6_placeholder(content: str) -> Optional[tuple]:
    """Find Section 6 placeholder boundaries. Returns (start, end) positions or None."""
    # Pattern to match Section 6 header through Section 7 header
    pattern = r'(## ⚙️ 6\. 实验配置.*?)(?=\n## [^#])'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return (match.start(), match.end())
    return None


def generate_section6_prompt(info: Dict[str, Any], arxiv_content: str = "") -> str:
    """Generate prompt for LLM to fill Section 6."""

    title = info.get('title', 'Unknown')
    arxiv = info.get('arxiv', '')
    year = info.get('year', '')
    authors = info.get('authors', [])
    method_tags = info.get('method_tags', [])
    application_tags = info.get('application_tags', [])
    sections = info.get('sections', {})

    # Extract relevant sections for context
    method_section = sections.get('5. 方法详解（Methodology）', '') or sections.get('方法详解', '')
    exp_section = sections.get('8. 实验分析（Experiments）', '') or sections.get('实验分析', '')

    # Get Chinese summary sections
    summary_keys = [k for k in sections.keys() if '总结' in k or '摘要' in k]
    summary = '\n'.join(sections.get(k, '') for k in summary_keys if sections.get(k))

    arxiv_section = f"\n\n## Full Paper Content (first 15000 chars)\n{arxiv_content[:15000]}\n\n" if arxiv_content else "\n"

    prompt = f"""You are an academic paper analyzer. Based on the paper information below, infer and generate Section 6 (实验配置 / Experimental Setup) content.

## Paper Information
- Title: {title}
- arXiv: {arxiv}
- Year: {year}
- Authors: {', '.join(authors[:5]) if authors else 'Unknown'}{' et al.' if len(authors) > 5 else ''}
- Method Tags: {', '.join(method_tags) if method_tags else 'Unknown'}
- Application Tags: {', '.join(application_tags) if application_tags else 'Unknown'}

## Existing Method Section (5)
{method_section[:1000] if method_section else 'Not available'}

## Existing Experiment Section (8)
{exp_section[:1000] if exp_section else 'Not available'}

## Summary/Abstract Content
{summary[:1500] if summary else 'Not available'}{arxiv_section}## Your Task
Generate Section 6 (实验配置 / Experimental Setup) content in Chinese. The section should include:

1. **硬件配置 (Hardware)**: Infer GPU type and count commonly used for this type of research. Training time if mentioned.
2. **数据集 (Datasets)**: Infer dataset names, sources, scale based on the paper's focus area.
3. **数据处理 (Data Processing)**: Infer typical preprocessing for this type of data.
4. **复现难度 (Reproducibility)**: Assess difficulty level (★☆☆☆☆ to ★★★★★) based on whether code/data are typically available.

## Output Format
Return ONLY the filled Section 6 content in this exact format (no code blocks, no explanations):

## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: [inferred GPU型号]
- GPU数量: [inferred 数量]
- 训练时间: [inferred 时间或"未明确说明"]

### 数据集（Datasets）
1. **[数据集名称]**
   - 来源: [来源]
   - 任务: [任务类型]
   - 数据规模: [规模]
   - 是否公开: [是/否/不确定]

### 数据处理
- [处理方式]

### 复现难度
- [星级评分 + 原因]

IMPORTANT: Return ONLY the Section 6 content, no preamble or explanation. Base your inference on:
- The paper's method (e.g., deep learning weather prediction typically uses A100/V100 GPUs)
- The paper's application domain (e.g., ocean data assimilation uses specific ocean datasets)
- Typical research practices in the field
"""
    return prompt


def call_claude_api(prompt: str, api_key: str) -> Optional[str]:
    """Call Claude API to generate Section 6 content."""
    base_url = os.environ.get("ANTHROPIC_BASE_URL", "")
    model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")

    if base_url:
        client = Anthropic(api_key=api_key, base_url=base_url)
    else:
        client = Anthropic(api_key=api_key)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        for block in response.content:
            if hasattr(block, 'text') and block.text:
                return block.text

        return None

    except Exception as e:
        print(f"  [API ERROR] {e}")
        return None


def fill_section6(abstract_path: Path, api_key: str, dry_run: bool = False) -> Dict[str, Any]:
    """Fill Section 6 for a paper using LLM."""

    if not abstract_path.exists():
        return {"success": False, "error": f"File not found: {abstract_path}"}

    content = abstract_path.read_text(encoding='utf-8')

    # Check if Section 6 has placeholder
    placeholder_pattern = r'GPU: xxx|GPU数量: xxx'
    if not re.search(placeholder_pattern, content):
        return {"success": False, "error": "No placeholder found in Section 6", "skipped": True}

    # Parse abstract.md
    info = parse_abstract_md(abstract_path)

    if not info.get('title'):
        return {"success": False, "error": "Could not parse paper title"}

    print(f"  Processing: {info.get('title', abstract_path.parent.name)[:60]}...")

    # Read arxiv_content.txt if available
    arxiv_content = read_arxiv_content(abstract_path)
    if arxiv_content:
        print(f"  [Using full paper content: {len(arxiv_content)} chars]")
    else:
        print(f"  [No arxiv_content.txt found, using abstract only]")

    # Generate prompt
    prompt = generate_section6_prompt(info, arxiv_content)

    # Call API
    section6_content = call_claude_api(prompt, api_key)

    if not section6_content:
        return {"success": False, "error": "API call failed"}

    # Clean up - remove any markdown formatting
    section6_content = section6_content.strip()
    if section6_content.startswith("```"):
        section6_content = re.sub(r'^```[a-z]*\n?', '', section6_content)
    if section6_content.endswith("```"):
        section6_content = section6_content[:-3]
    section6_content = section6_content.strip()

    if dry_run:
        return {
            "success": True,
            "dry_run": True,
            "section6_content": section6_content,
            "paper_title": info.get('title', 'Unknown')
        }

    # Find and replace Section 6 placeholder
    # Pattern: from "## ⚙️ 6. 实验配置" to just before the next major section (## followed by space)
    # Key: The lookahead (?=\n## ) matches newline followed by "## " which is the start of a new section
    # The pattern \n## [^#] means newline + ## + any non-# character (which is the space after ##)
    pattern = r'(## ⚙️ 6\. 实验配置.*?)(?=\n## )'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return {"success": False, "error": "Could not find Section 6 location"}

    # Replace the placeholder section
    new_content = content[:match.start()] + section6_content + '\n\n' + content[match.end():]

    # Write back
    abstract_path.write_text(new_content, encoding='utf-8')

    return {
        "success": True,
        "paper_title": info.get('title', 'Unknown'),
        "file": str(abstract_path)
    }


def main():
    parser = argparse.ArgumentParser(description="Fill Section 6 using LLM inference")
    parser.add_argument("--paper", type=str, required=True, help="Path to abstract.md file")
    parser.add_argument("--api-key", type=str, default=None, help="Anthropic API key")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    args = parser.parse_args()

    api_key = args.api_key if args.api_key else get_api_key()
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found")
        print("Set it with: export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    abstract_path = Path(args.paper)
    if not abstract_path.is_absolute():
        abstract_path = PROJECT_ROOT / abstract_path

    result = fill_section6(abstract_path, api_key, dry_run=args.dry_run)

    if result.get("dry_run"):
        print(f"\n[DRY RUN] Section 6 for: {result.get('paper_title')}")
        print("\n--- Generated Section 6 ---")
        print(result.get('section6_content', 'FAILED'))
    elif result.get("success"):
        print(f"\n[OK] Updated: {result.get('paper_title')}")
    elif result.get("skipped"):
        print(f"\n[SKIP] {result.get('error')}")
    else:
        print(f"\n[FAILED] {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
