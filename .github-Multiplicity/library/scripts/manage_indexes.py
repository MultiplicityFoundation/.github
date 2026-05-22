#!/usr/bin/env python3
"""
CLI wrapper to validate and build indexes.

Usage:
  python3 scripts/manage_indexes.py validate
  python3 scripts/manage_indexes.py build
  python3 scripts/manage_indexes.py all
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd: list[str]) -> int:
    print('Running:', ' '.join(cmd))
    r = subprocess.run(cmd)
    return r.returncode


def cmd_validate(schema: str, path: str) -> int:
    return run_cmd([sys.executable, 'scripts/validate_frontmatter.py', '--schema', schema, '--path', path])


def cmd_build() -> int:
    return run_cmd([sys.executable, 'scripts/build_index.py'])


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd')
    root = Path(__file__).resolve().parents[1]
    p_val = sub.add_parser('validate')
    p_val.add_argument('--only', help='Comma-separated list of files to validate')
    p_val.add_argument('--paths-file', help='File listing files to validate, one per line')
    p_val.add_argument('--schema', default=str(root / 'schemas' / 'article-schema.json'))
    p_val.add_argument('--path', default=str(root / 'articles'))
    p_build = sub.add_parser('build')
    p_build.add_argument('--path', default=str(root / 'articles'))
    p_build.add_argument('--no-json', action='store_true')
    p_build.add_argument('--minify', action='store_true')
    p_all = sub.add_parser('all')
    p_all.add_argument('--schema', default=str(root / 'schemas' / 'article-schema.json'))
    p_all.add_argument('--path', default=str(root / 'articles'))
    p_all.add_argument('--no-json', action='store_true')
    p_all.add_argument('--minify', action='store_true')
    args = p.parse_args(argv)
    if not args.cmd:
        p.print_help()
        return 2

    schema = str(root / 'schemas' / 'article-schema.json')
    path = str(root / 'articles')

    if args.cmd == 'validate':
        schema = args.schema
        path = args.path
        additional = []
        if hasattr(args, 'only') and args.only:
            additional.extend(['--only', args.only])
        if hasattr(args, 'paths_file') and args.paths_file:
            additional.extend(['--paths-file', args.paths_file])
        return run_cmd([sys.executable, 'scripts/validate_frontmatter.py', '--schema', schema, '--path', path] + additional)
    if args.cmd == 'build':
        cmd = [sys.executable, 'scripts/build_index.py']
        if hasattr(args, 'no_json') and args.no_json:
            cmd.append('--no-json')
        if hasattr(args, 'minify') and args.minify:
            cmd.append('--minify')
        return run_cmd(cmd)
    if args.cmd == 'all':
        schema = args.schema
        path = args.path
        rc = cmd_validate(schema, path)
        if rc != 0:
            return rc
        cmd = [sys.executable, 'scripts/build_index.py']
        if hasattr(args, 'no_json') and args.no_json:
            cmd.append('--no-json')
        if hasattr(args, 'minify') and args.minify:
            cmd.append('--minify')
        return run_cmd(cmd)
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
