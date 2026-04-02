#!/usr/bin/env python3
"""
Batch fill Section 6 for all papers with placeholder content.

Processes all papers with "GPU: xxx" or similar placeholders in Section 6,
calling LLM for each to generate proper content.
"""

import argparse
import os
import re
import sys
import json
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

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


def find_papers_with_placeholders(papers_dir: Path) -> List[Path]:
    """Find all papers with Section 6 placeholder content."""
    # Multiple placeholder patterns to catch various incomplete Section 6 content
    placeholder_patterns = [
        re.compile(r'GPU: xxx'),
        re.compile(r'GPU数量: xxx'),
        re.compile(r'论文未明确提供'),
        re.compile(r'未明确说明'),
        re.compile(r'来源: xxx'),
        re.compile(r'任务: xxx'),
        re.compile(r'数据规模: xxx'),
        re.compile(r'是否公开: xxx'),
    ]
    papers = []

    for abstract_file in papers_dir.glob("*/**/abstract.md"):
        try:
            content = abstract_file.read_text(encoding='utf-8')
            # Check if Section 6 exists in this file
            if '## ⚙️ 6. 实验配置' not in content:
                continue
            # Check if it has placeholder content
            has_placeholder = any(p.search(content) for p in placeholder_patterns)
            if has_placeholder:
                papers.append(abstract_file)
        except Exception:
            continue

    return sorted(papers)


def fill_section6_for_paper(abstract_path: Path, api_key: str) -> Dict[str, Any]:
    """Fill Section 6 for a single paper."""

    content = abstract_path.read_text(encoding='utf-8')

    # Check if Section 6 has placeholder
    placeholder_patterns = [
        re.compile(r'GPU: xxx'),
        re.compile(r'GPU数量: xxx'),
        re.compile(r'论文未明确提供'),
        re.compile(r'未明确说明'),
        re.compile(r'来源: xxx'),
        re.compile(r'任务: xxx'),
        re.compile(r'数据规模: xxx'),
        re.compile(r'是否公开: xxx'),
    ]
    if not any(p.search(content) for p in placeholder_patterns):
        return {"success": False, "error": "No placeholder", "skipped": True}

    # Parse abstract.md
    info = parse_abstract_md(abstract_path)

    if not info.get('title'):
        return {"success": False, "error": "Could not parse paper title"}

    # Read arxiv_content.txt if available
    arxiv_content = read_arxiv_content(abstract_path)

    # Generate prompt
    prompt = generate_section6_prompt(info, arxiv_content)

    # Call API
    section6_content = call_claude_api(prompt, api_key)

    if not section6_content:
        return {"success": False, "error": "API call failed", "paper": info.get('title')}

    # Clean up - remove any markdown formatting
    section6_content = section6_content.strip()
    if section6_content.startswith("```"):
        section6_content = re.sub(r'^```[a-z]*\n?', '', section6_content)
    if section6_content.endswith("```"):
        section6_content = section6_content[:-3]
    section6_content = section6_content.strip()

    # Find and replace Section 6 placeholder
    # Pattern: from "## ⚙️ 6. 实验配置" to just before the next major section (## followed by space)
    # Key: The lookahead (?=\n## ) matches newline followed by "## " which is the start of a new section
    # The pattern \n## [^#] means newline + ## + any non-# character (which is the space after ##)
    pattern = r'(## ⚙️ 6\. 实验配置.*?)(?=\n## )'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return {"success": False, "error": "Could not find Section 6 location", "paper": info.get('title')}

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
    parser = argparse.ArgumentParser(description="Batch fill Section 6 using LLM inference")
    parser.add_argument("--api-key", type=str, default=None, help="Anthropic API key")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of papers to process")
    parser.add_argument("--rate-limit", type=float, default=5.0, help="Seconds between API calls (default: 5)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be processed")
    parser.add_argument("--base-dir", type=str, default=None, help="Base directory for papers")
    parser.add_argument("--log-file", type=str, default=None, help="Log file path")
    args = parser.parse_args()

    api_key = args.api_key if args.api_key else get_api_key()
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found")
        print("Set it with: export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    # Determine base directory
    if args.base_dir:
        papers_dir = Path(args.base_dir)
    else:
        papers_dir = PROJECT_ROOT / "papers"

    if not papers_dir.exists():
        print(f"Error: Papers directory not found: {papers_dir}")
        sys.exit(1)

    # Find papers with placeholders
    papers = find_papers_with_placeholders(papers_dir)

    print(f"Found {len(papers)} papers with Section 6 placeholders")
    print("=" * 60)

    if args.dry_run:
        print("\nPapers that would be processed:")
        for paper in papers[:20]:
            print(f"  {paper.parent.parent.name}/{paper.parent.name}")
        if len(papers) > 20:
            print(f"  ... and {len(papers) - 20} more")
        return

    if args.limit:
        papers = papers[:args.limit]

    results = []
    success = 0
    failed = 0
    skipped = 0

    log_file = None
    if args.log_file:
        log_file = open(args.log_file, 'w', encoding='utf-8')
        log_file.write(f"# Section 6 Fill Log - {datetime.now().isoformat()}\n")

    for i, paper in enumerate(papers):
        print(f"\n[{i+1}/{len(papers)}] ", end="", flush=True)

        result = fill_section6_for_paper(paper, api_key)
        results.append(result)

        if result.get("success"):
            print(f"[OK] {result.get('paper_title', paper.parent.name)[:50]}...")
            success += 1
            if log_file:
                log_file.write(f"[OK] {result.get('paper_title')} -> {result.get('file')}\n")
        elif result.get("skipped"):
            print(f"[SKIP] {result.get('error', 'placeholder not found')}")
            skipped += 1
            if log_file:
                log_file.write(f"[SKIP] {paper} -> {result.get('error')}\n")
        else:
            print(f"[FAILED] {result.get('error', 'unknown error')}")
            failed += 1
            if log_file:
                log_file.write(f"[FAILED] {paper} -> {result.get('error')}\n")

        # Rate limiting
        if i < len(papers) - 1 and not result.get("skipped"):
            time.sleep(args.rate_limit)

    if log_file:
        log_file.close()

    print("\n" + "=" * 60)
    print(f"Done: {success} succeeded, {failed} failed, {skipped} skipped")

    # Summary by year
    year_counts = {}
    for paper in papers:
        year = paper.parent.parent.name
        year_counts[year] = year_counts.get(year, 0) + 1

    print("\nBy year:")
    for year in sorted(year_counts.keys()):
        print(f"  {year}: {year_counts[year]} papers")

    # Save results JSON
    results_file = PROJECT_ROOT / "scripts" / "repair" / "section6_fill_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total": len(papers),
            "success": success,
            "failed": failed,
            "skipped": skipped,
            "rate_limit": args.rate_limit,
            "results": results
        }, f, ensure_ascii=False, indent=2)

    print(f"\nResults saved to: {results_file}")


if __name__ == "__main__":
    main()
