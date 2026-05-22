#!/usr/bin/env python3
"""
Assign PR reviewers according to a mapping file for changed file paths.
Mapping file is YAML with glob patterns as keys and arrays of reviewer usernames as values.

Example mapping (`.github/reviewer-mapping.yml`):
  articles/00-foundations/**:
    - alice
  articles/01-operators/**:
    - bob
  articles/**:
    - core-maintainer

This script expects `gh` CLI to be installed and authenticated with a token.
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Set

try:
    import yaml
except Exception:
    print('Missing dependency: pyyaml (install with pip install pyyaml)', file=sys.stderr)
    raise


def load_mapping(path: Path) -> Dict[str, List[str]]:
    if not path.exists():
        return {}
    with path.open(encoding='utf-8') as fh:
        data = yaml.safe_load(fh) or {}
        return {k: [str(i).strip().lstrip('@') for i in v] for k, v in data.items()}


def get_pr_files(pr_number: int) -> List[str]:
    # Use gh to list files for the PR
    cmd = ['gh', 'pr', 'view', str(pr_number), '--json', 'files']
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print('gh pr view failed:', proc.stderr, file=sys.stderr)
        sys.exit(2)
    # parse JSON
    import json
    resp = json.loads(proc.stdout)
    return [f['path'] for f in resp.get('files', [])]


def map_reviewers(files: List[str], mapping: Dict[str, List[str]]) -> Set[str]:
    user_reviewers: Set[str] = set()
    team_reviewers: Set[str] = set()
    for fp in files:
        for pattern, users in mapping.items():
            if fnmatch.fnmatch(fp, pattern):
                for u in users:
                    if not u:
                        continue
                    val = u.strip()
                    if '/' in val:
                        # treat as org/team
                        team_reviewers.add(val.lstrip('@'))
                    else:
                        user_reviewers.add(val.lstrip('@'))
    return user_reviewers, team_reviewers


def request_reviewers(pr_number: int, user_reviewers: Set[str], team_reviewers: Set[str], dry_run: bool = False) -> int:
    if not user_reviewers and not team_reviewers:
        print('No reviewers to add')
        return 0
    owner_repo = os.environ.get('GITHUB_REPOSITORY')
    if not owner_repo:
        print('Missing GITHUB_REPOSITORY environment variable', file=sys.stderr)
        return 2
    owner, repo = owner_repo.split('/')
    data_args = []
    import json
    if user_reviewers:
        data_args.extend(['-F', f"reviewers={json.dumps(list(user_reviewers))}"])
    if team_reviewers:
        data_args.extend(['-F', f"team_reviewers={json.dumps(list(team_reviewers))}"])
    cmd = ['gh', 'api', f'/repos/{owner}/{repo}/pulls/{pr_number}/requested_reviewers'] + data_args
    if dry_run:
        print('DRY RUN: would run:', ' '.join(cmd))
        print('Users:', user_reviewers)
        print('Teams:', team_reviewers)
        return 0
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print('Error requesting reviewers:', p.stderr, file=sys.stderr)
        return p.returncode
    combined = list(user_reviewers) + list(team_reviewers)
    print('Requested reviewers:', ','.join(combined))
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--mapping', default='.github/reviewer-mapping.yml', help='Path to mapping YAML file')
    p.add_argument('--pr', type=int, help='PR number to operate on (optional, infer from env)')
    p.add_argument('--dry-run', action='store_true', help='List reviewers without making API call')
    args = p.parse_args(argv)

    if 'GITHUB_EVENT_PATH' in os.environ:
        import json
        try:
            event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
            pr_num = int(event.get('pull_request', {}).get('number', 0)) if not args.pr else args.pr
        except Exception:
            pr_num = args.pr
    else:
        pr_num = args.pr

    if not pr_num:
        print('PR number not specified and could not be inferred', file=sys.stderr)
        return 2

    mapping = load_mapping(Path(args.mapping))
    if not mapping:
        print('No mapping rules found; skipping', file=sys.stderr)
        return 0

    files = get_pr_files(pr_num)
    if not files:
        print('No changed files for this PR')
        return 0

    user_reviewers, team_reviewers = map_reviewers(files, mapping)
    return request_reviewers(pr_num, user_reviewers, team_reviewers, dry_run=args.dry_run)


if __name__ == '__main__':
    raise SystemExit(main())
