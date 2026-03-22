#!/usr/bin/env python3
"""
Generate Chinese summary.md files for ai-data-assimilation-papers project.

This script:
1. Scans for papers missing summary.md
2. Reads abstract.md and content files
3. Uses Claude API to generate summary.md in the correct Chinese format

Target format matches existing 76 summary.md files with:
- YAML frontmatter with authors as Python list
- 11 Chinese sections with emoji headers
"""

import argparse
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from anthropic import Anthropic
except ImportError:
    print("Error: anthropic package not installed. Install with: pip install anthropic")
    sys.exit(1)


def get_api_key() -> str:
    """Get API key from environment or arguments."""
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


def parse_abstract_md(abstract_path: Path) -> dict:
    """Parse abstract.md to extract structured information."""
    if not abstract_path.exists():
        return {}

    content = abstract_path.read_text(encoding='utf-8')

    info = {
        'title': '',
        'arxiv': '',
        'authors': [],
        'year': '',
        'source': 'arXiv',
        'venue': 'arXiv',
        'difficulty': '★★★☆☆',
        'importance': '★★★☆☆',
        'read_status': 'skim',
        'method_tags': [],
        'application_tags': [],
        'sections': {}
    }

    # Parse YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1]
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")

                    if key == 'title':
                        info['title'] = val
                    elif key == 'arXiv':
                        info['arxiv'] = val
                    elif key == 'year':
                        info['year'] = val
                    elif key == 'source':
                        info['source'] = val
                    elif key == 'venue':
                        info['venue'] = val
                    elif key == 'difficulty':
                        info['difficulty'] = val
                    elif key == 'importance':
                        info['importance'] = val
                    elif key == 'read_status':
                        info['read_status'] = val
                    elif key == 'method_tags':
                        # Parse list format
                        tag_content = val
                        if '[' in val:
                            tag_content = val
                        info['method_tags'] = [t.strip().strip('"').strip("'") for t in re.findall(r'["\']([^"\']+)["\']', val)]
                        if not info['method_tags']:
                            info['method_tags'] = [t.strip() for t in val.strip('[]').split(',')]
                    elif key == 'application_tags':
                        info['application_tags'] = [t.strip().strip('"').strip("'") for t in re.findall(r'["\']([^"\']+)["\']', val)]
                        if not info['application_tags']:
                            info['application_tags'] = [t.strip() for t in val.strip('[]').split(',')]

            # Parse authors section if separate
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
    current_section = None
    current_content = []
    sections = {}

    for line in content.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)

    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()

    info['sections'] = sections

    # Extract TL;DR
    if 'TL;DR' in sections:
        info['tldr'] = sections['TL;DR']

    # Extract Research Question
    if 'Research Question' in sections:
        info['research_question'] = sections['Research Question']

    # Extract Method
    if 'Method' in sections:
        info['method'] = sections['Method']

    # Extract Main Contributions
    if 'Main Contributions' in sections:
        contributions_text = sections['Main Contributions']
        info['contributions'] = re.findall(r'^\d+\.\s*(.+)$', contributions_text, re.MULTILINE)
        if not info['contributions']:
            info['contributions'] = [c.strip() for c in contributions_text.split('\n') if c.strip()]

    # Extract Datasets
    if 'Datasets' in sections:
        datasets_text = sections['Datasets']
        info['datasets'] = re.findall(r'^- (.+)$', datasets_text, re.MULTILINE)
        if not info['datasets']:
            info['datasets'] = [d.strip() for d in datasets_text.split('\n') if d.strip()]

    # Extract Core Results
    if 'Core Results' in sections:
        results_text = sections['Core Results']
        info['results'] = re.findall(r'^- (.+)$', results_text, re.MULTILINE)
        if not info['results']:
            info['results'] = [r.strip() for r in results_text.split('\n') if r.strip()]

    # Extract Limitations
    if 'Limitations' in sections:
        limitations_text = sections['Limitations']
        info['limitations'] = re.findall(r'^- (.+)$', limitations_text, re.MULTILINE)

    # Extract Research Gaps
    if 'Research Gaps' in sections:
        gaps_text = sections['Research Gaps']
        info['research_gaps'] = re.findall(r'^- (.+)$', gaps_text, re.MULTILINE)

    return info


def read_content_file(paper_dir: Path) -> str:
    """Read content from arxiv_content.txt or paper_content.txt."""
    for fname in ['arxiv_content.txt', 'paper_content.txt']:
        content_path = paper_dir / fname
        if content_path.exists():
            return content_path.read_text(encoding='utf-8', errors='ignore')
    return ""


def generate_summary_markdown(info: dict, paper_dir: Path) -> str:
    """Generate summary.md content using Claude API."""

    abstract_info = info.get('abstract_info', {})

    # Build context from existing abstract.md
    tldr = info.get('tldr', abstract_info.get('tldr', 'Not available'))
    research_question = info.get('research_question', abstract_info.get('research_question', 'Not available'))
    method = info.get('method', abstract_info.get('method', 'Not available'))
    contributions = info.get('contributions', abstract_info.get('contributions', []))
    results = info.get('results', abstract_info.get('results', []))
    datasets = info.get('datasets', abstract_info.get('datasets', []))
    limitations = info.get('limitations', abstract_info.get('limitations', []))
    research_gaps = info.get('research_gaps', abstract_info.get('research_gaps', []))

    # Get content for context
    content_sample = info.get('content_sample', '')
    if len(content_sample) > 6000:
        content_sample = content_sample[:6000]

    # Build method_tags string
    method_tags = info.get('method_tags', [])
    if isinstance(method_tags, list):
        method_tags_str = ', '.join(method_tags)
    else:
        method_tags_str = str(method_tags)

    # Build application_tags string
    app_tags = info.get('application_tags', [])
    if isinstance(app_tags, list):
        app_tags_str = ', '.join(app_tags)
    else:
        app_tags_str = str(app_tags)

    prompt = f"""You are generating a structured summary for an academic paper in Chinese. Generate a complete summary.md file with YAML front matter and detailed sections in Chinese.

## Paper Information
- Title: {info.get('title', 'Unknown')}
- arXiv ID: {info.get('arxiv', 'Unknown')}
- Year: {info.get('year', 'Unknown')}
- Authors: {', '.join(info.get('authors', ['Unknown'])) if isinstance(info.get('authors'), list) else info.get('authors', 'Unknown')}
- Venue: {info.get('venue', 'arXiv')}

## Existing Abstract Info (from abstract.md)
- TL;DR: {tldr}
- Research Question: {research_question}
- Method: {method[:500] if len(method) > 500 else method}
- Contributions: {'; '.join(str(c) for c in contributions[:5]) if contributions else 'Not specified'}
- Results: {'; '.join(str(r) for r in results[:5]) if results else 'Not specified'}
- Datasets: {'; '.join(str(d) for d in datasets[:5]) if datasets else 'Not specified'}
- Limitations: {'; '.join(str(l) for l in limitations[:3]) if limitations else 'Not specified'}
- Research Gaps: {'; '.join(str(g) for g in research_gaps[:3]) if research_gaps else 'Not specified'}

## Paper Content Sample (first 6000 chars)
{content_sample[:6000] if content_sample else 'No content available'}

## Required Output Format
Generate ONLY the summary.md content in Chinese, following this exact structure:

```markdown
---
title: "Paper Title Here"
arXiv: "XXXXX.XXXXXvN"
authors: ["Author1", "Author2", "Author3"]
year: YYYY
source: "arXiv"
venue: "Venue Name"
method_tags: ["Tag1", "Tag2", "Tag3"]
application_tags: ["AppTag1", "AppTag2"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# Paper Title Here

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/XXXXX.XXXXX
- **作者机构**: [Extract author affiliations if available, otherwise use first 2-3 authors + et al.]
- **开源代码**: [Check content for GitHub link or mention "None" if not found]

## 2. 一句话总结（TL;DR）
[2-3 sentence summary in Chinese]

## 3. 研究问题（Problem Definition）
[What is the core research problem? Why is it important? What are the key challenges?]

## 4. 核心贡献（Contributions）
1. [Contribution 1]
2. [Contribution 2]
3. [Contribution 3]

## 5. 方法详解（Methodology）
[Detailed description of the method, architecture, and approach]

## 6. 数学与物理建模（Math & Physics）
[Key equations, physical constraints, mathematical formulations if applicable]

## 7. 实验分析（Experiments）
**数据集**: [List datasets]
**评估指标**: [List metrics]
**对比方法**: [List baselines]
**核心结果**: [Key findings]

## 8. 优缺点分析（Critical Review）
**优点**:
- [Strength 1]
- [Strength 2]

**缺点**:
- [Weakness 1]
- [Weakness 2]

## 9. 对我的启发（For My Research）
[How can this paper inspire your research in ocean data assimilation?]

## 10. Idea 扩展与下一步（Next Steps）
1. [Extension direction 1]
2. [Extension direction 2]
3. [Extension direction 3]

## 11. 引用格式（BibTex）
```bibtex
[Generate proper BibTeX citation]
```
```

Generate ONLY the summary.md content, no additional explanation. Output in Chinese.
"""

    return prompt


def call_claude_api(prompt: str, api_key: str) -> Optional[str]:
    """Call Claude API to generate summary content."""
    base_url = os.environ.get("ANTHROPIC_BASE_URL", "")
    model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")

    if base_url:
        client = Anthropic(api_key=api_key, base_url=base_url)
    else:
        client = Anthropic(api_key=api_key)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=4096,
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


def process_paper(paper_dir: Path, year: str, api_key: str) -> bool:
    """Process a single paper and generate summary.md."""
    abstract_path = paper_dir / "abstract.md"

    if not abstract_path.exists():
        print(f"  [SKIP] No abstract.md: {paper_dir.name}")
        return False

    try:
        # Parse abstract.md
        abstract_info = parse_abstract_md(abstract_path)

        if not abstract_info.get('title'):
            abstract_info['title'] = paper_dir.name

        # Get content sample
        content_sample = read_content_file(paper_dir)
        abstract_info['content_sample'] = content_sample

        print(f"  Processing: {abstract_info.get('title', paper_dir.name)[:60]}...")

        # Generate prompt
        prompt = generate_summary_markdown(abstract_info, paper_dir)

        # Call API
        summary_content = call_claude_api(prompt, api_key)

        if not summary_content:
            print(f"  [FAILED] API call failed: {paper_dir.name}")
            return False

        # Clean up markdown code block markers
        cleaned_content = summary_content.strip()
        if cleaned_content.startswith("```markdown"):
            cleaned_content = cleaned_content[len("```markdown"):].strip()
        if cleaned_content.startswith("```"):
            cleaned_content = cleaned_content[3:].strip()
        if cleaned_content.endswith("```"):
            cleaned_content = cleaned_content[:-3].strip()

        # Write output
        output_path = paper_dir / "summary.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"  [OK] Generated: {paper_dir.name}")
        return True

    except Exception as e:
        print(f"  [ERROR] {paper_dir.name}: {e}")
        import traceback
        traceback.print_exc()
        return False


def find_papers_missing_summary(base_dir: Path) -> list:
    """Find all papers missing summary.md."""
    missing = []

    for year_dir in sorted(base_dir.iterdir()):
        if not year_dir.is_dir():
            continue
        if not year_dir.name.isdigit():
            continue
        year = year_dir.name

        for paper_dir in sorted(year_dir.iterdir()):
            if not paper_dir.is_dir():
                continue
            if not (paper_dir / "abstract.md").exists():
                continue
            if (paper_dir / "summary.md").exists():
                continue

            missing.append((paper_dir, year))

    return missing


def main():
    parser = argparse.ArgumentParser(description="Generate Chinese summary.md for ai-data-assimilation-papers")
    parser.add_argument("--api-key", type=str, default=None, help="Anthropic API key")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of papers to process")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be processed")
    parser.add_argument("--base-dir", type=str, default=None, help="Base directory for papers")
    args = parser.parse_args()

    # Get API key
    api_key = args.api_key if args.api_key else get_api_key()
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found")
        print("Set it with: export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    # Determine base directory
    if args.base_dir:
        base_dir = Path(args.base_dir)
    else:
        base_dir = Path(__file__).parent.parent / "papers"

    if not base_dir.exists():
        print(f"Error: Base directory not found: {base_dir}")
        sys.exit(1)

    # Find papers missing summary.md
    missing_papers = find_papers_missing_summary(base_dir)

    print(f"Found {len(missing_papers)} papers missing summary.md")
    print("=" * 60)

    if args.dry_run:
        print("\nPapers that would be processed:")
        for paper_dir, year in missing_papers[:20]:
            print(f"  {year}/{paper_dir.name}")
        if len(missing_papers) > 20:
            print(f"  ... and {len(missing_papers) - 20} more")
        return

    if args.limit:
        missing_papers = missing_papers[:args.limit]

    success = 0
    failed = 0

    for i, (paper_dir, year) in enumerate(missing_papers):
        print(f"\n[{i+1}/{len(missing_papers)}] ", end="", flush=True)

        result = process_paper(paper_dir, year, api_key)
        if result:
            success += 1
        else:
            failed += 1

        # Rate limiting
        if i < len(missing_papers) - 1:
            time.sleep(1.5)

    print("\n" + "=" * 60)
    print(f"Done: {success} succeeded, {failed} failed")


if __name__ == "__main__":
    main()
