#!/usr/bin/env python3
"""
Math corrector: normalize and fix latex-like math expressions in markdown `articles/`.

This merge combines a simple line-based normalizer and a placeholder stub.
It supports:
  - --dry-run: don't write files
  - --only: comma-separated list of files to process (absolute or relative)
  - --path: root path to search for markdown files (default: articles)
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List


def fix_math_expr(expr: str) -> str:
    # Example normalizations:
    expr = expr.replace("−", "-")  # Unicode minus
    # Convert bare \frac to escaped latex if needed
    expr = expr.replace(r"\frac", r"\\frac")
    # Reduce multiple spaces to single
    expr = re.sub(r"\s+", " ", expr)
    # TODO: add more comprehensive corrections (LLM call or latex parser)
    return expr


def correct_math_in_text(text: str) -> (str, bool):
    changed = False

    def fix_inline(match):
        nonlocal changed
        expr = match.group(1)
        fixed = fix_math_expr(expr)
        if fixed != expr:
            changed = True
        return f"${fixed}$"

    text = re.sub(r"\$(.+?)\$", fix_inline, text)

    def fix_block(match):
        nonlocal changed
        expr = match.group(1)
        fixed = fix_math_expr(expr)
        if fixed != expr:
            changed = True
        # Preserve block formatting
        return f"$$\n{fixed}\n$$"

    text = re.sub(r"\$\$\s*([\s\S]*?)\s*\$\$", fix_block, text)
    return text, changed


def find_files(root: Path, only_files: List[Path] | None = None) -> List[Path]:
    if only_files:
        resolved = []
        for f in only_files:
            p = Path(f)
            if not p.is_absolute():
                p = root / p
            if p.exists():
                resolved.append(p.resolve())
        return resolved
    else:
        return list(root.rglob("*.md"))


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true", help="Do not write changes")
    p.add_argument("--only", help="Comma-separated list of files to process (overrides scanning)")
    p.add_argument("--path", default="articles", help="Path to scan for markdown files")
    args = p.parse_args(argv)

    root = Path(args.path)
    only = None
    if args.only:
        only = [Path(s.strip()) for s in args.only.split(",") if s.strip()]

    files = find_files(root, only)
    if not files:
        print(f"[INFO] No files found in {root}")
        return 0

    files_changed = 0
    for md in files:
        try:
            orig = md.read_text(encoding="utf-8")
        except Exception:
            continue
        fixed, changed = correct_math_in_text(orig)
        if changed:
            files_changed += 1
            if not args.dry_run:
                md.write_text(fixed, encoding="utf-8")
                print(f"[FIXED] {md}")
            else:
                print(f"[DRY] Would fix {md}")

    if files_changed == 0:
        print("[INFO] No changes made.")
    else:
        print(f"[INFO] {files_changed} file(s) changed.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
