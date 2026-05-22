#!/usr/bin/env python3
"""
Validate YAML front matter of markdown files against a JSON Schema.

Usage:
  python3 scripts/validate_frontmatter.py --schema schemas/article-schema.json --path articles

Exits with non-zero code on validation failure.
"""

from __future__ import annotations

import argparse
import json
try:
    import yaml
except Exception:
    yaml = None
import re
import sys
from pathlib import Path
from typing import Any, Dict

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import ValidationError
except ImportError:
    print("Missing dependency: jsonschema. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(1)

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def extract_front_matter(text: str) -> Dict[str, Any]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    # YAML is allowed here but to reduce deps we expect it to parse as JSON-ish
    if yaml:
        try:
            data = yaml.safe_load(raw) or {}
            if isinstance(data, dict):
                return data
        except Exception:
            pass
    try:
        # Try to parse with JSON if it's pure JSON
        return json.loads(raw)
    except Exception:
        # Fall back to using a crude key: value parser to extract common fields
        data: Dict[str, Any] = {}
        for line in raw.splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                k = k.strip()
                v = v.strip()
                if v.startswith('[') and v.endswith(']'):
                    try:
                        data[k] = json.loads(v.replace("'", '"'))
                    except Exception:
                        data[k] = [i.strip().strip('"').strip("'") for i in v.strip('[]').split(',') if i.strip()]
                else:
                    data[k] = v.strip('"').strip("'")
        return data


def load_schema(schema_path: Path):
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate(md_path: Path, schema: Dict[str, Any]) -> bool:
    text = md_path.read_text(encoding='utf-8', errors='ignore')
    fm = extract_front_matter(text)
    if not fm:
        print(f"[ERROR] {md_path}: no front matter found")
        return False

    validator = Draft202012Validator(schema)
    errors = list(validator.iter_errors(fm))
    if errors:
        print(f"[ERROR] Validation failed for {md_path}")
        for e in errors:
            print(f" - {e.message}")
        return False
    return True


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--schema', required=True, help='Path to JSON schema')
    # Accept multiple paths or files
    p.add_argument('--path', default=['articles'], nargs='+', help='Path(s) to scan for markdown files')
    p.add_argument('--only', help='Comma-separated list of files to validate (overrides --path)')
    p.add_argument('--paths-file', help='Path to file with newline-separated list of files to validate')
    p.add_argument('--lenient', action='store_true', help='Treat validation failures as warnings; exit 0')
    p.add_argument('--skip-existing', action='store_true', help='Skip files that already exist on the base branch (only validate new files)')
    args = p.parse_args(argv)

    schema_path = Path(args.schema)
    if not schema_path.exists():
        print(f"Schema not found: {schema_path}", file=sys.stderr)
        return 2

    schema = load_schema(schema_path)
    base_paths = [Path(p) for p in args.path]
    # Load --only and --paths-file
    only_files = []
    if args.only:
        only_files.extend([Path(f.strip()) for f in args.only.split(',') if f.strip()])
    if args.paths_file:
        pf = Path(args.paths_file)
        if pf.exists():
            for line in pf.read_text(encoding='utf-8').splitlines():
                if line.strip():
                    only_files.append(Path(line.strip()))
    valid_bases = [p for p in base_paths if p.exists() or '*' in str(p)]
    if not valid_bases:
        print(f"Path not found: {base_paths}", file=sys.stderr)
        return 2

    failures = 0
    md_files = []
    if only_files:
        for f in only_files:
            p = Path(f)
            if p.is_file():
                md_files.append(p)
            else:
                # allow glob patterns
                from glob import glob
                for r in glob(str(p)):
                    md_files.append(Path(r))
    else:
        # compute from base paths
        for base in base_paths:
            if base.is_file():
                md_files.append(base)
            elif base.is_dir():
                md_files.extend(sorted(base.rglob('*.md')))
            else:
                # allow glob-style expressions
                from glob import glob
                for f in glob(str(base)):
                    p = Path(f)
                    if p.is_file():
                        md_files.append(p)

    for md in md_files:
        # Skip autogenerated index files
        if md.name == 'index.md' and (md.parent.name == 'tags' or any(md.parent == bp for bp in base_paths)):
            continue
        # Optionally skip files that exist on the base branch
        if args.skip_existing:
            base_branch = os.environ.get('GITHUB_BASE_REF') or 'main'
            try:
                # If the file exists on the base branch, skip
                import subprocess
                cp = subprocess.run(['git', 'cat-file', '-e', f'origin/{base_branch}:{md.as_posix()}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if cp.returncode == 0:
                    print(f"Skipping pre-existing file: {md}")
                    continue
            except Exception:
                # If git command fails, fall back to validating file
                pass

        ok = validate(md, schema)
        if not ok:
            failures += 1

    if failures:
        print(f"Validation failures: {failures}")
        return 0 if args.lenient else 3
    print("All files validated successfully.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
