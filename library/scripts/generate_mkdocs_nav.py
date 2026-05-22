#!/usr/bin/env python3
"""
Generate a small mkdocs nav fragment from articles/*/index.md files.
Writes 'nav.generated.yml' which can be included into mkdocs.yml manually.
"""

from __future__ import annotations

import yaml
from pathlib import Path


def build_nav(root: Path) -> dict:
    docs_dir = root / 'articles'
    nav = []
    if not docs_dir.exists():
        return nav
    for sub in sorted(docs_dir.iterdir()):
        if sub.is_dir():
            idx = sub / 'index.md'
            if idx.exists():
                title = " ".join([s.capitalize() for s in sub.name.replace('-', ' ').split()])
                nav.append({title: str(idx.relative_to(root))})
    return nav


def main():
    root = Path(__file__).resolve().parents[1]
    nav = {
        'nav': [
            {'Home': 'README.md'},
            {'Master Index': 'articles/index.md'},
            {'Tags': 'tags/index.md'},
            {'Glossary': 'glossary/index.md'},
            {'Articles': build_nav(root)}
        ]
    }
    out = root / 'mkdocs.nav.generated.yml'
    with out.open('w', encoding='utf-8') as f:
        yaml.dump(nav, f, sort_keys=False)
    print('Wrote', out)


if __name__ == '__main__':
    main()
