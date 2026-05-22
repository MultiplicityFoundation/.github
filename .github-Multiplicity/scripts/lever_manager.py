#!/usr/bin/env python3
"""
Multiplicity Unified Lever Manager.
Governs branch lifecycle and task execution across the ecosystem.
"""

import argparse
import sys
import yaml
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone

# Resolve REPO_ROOT: handle being in scripts/ or nested further
def get_repo_root():
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / "state" / "lever_manifest.yaml").exists() or (current / ".git").exists():
            return current
        current = current.parent
    return Path(__file__).resolve().parents[1]

REPO_ROOT = get_repo_root()
MANIFEST_PATH = REPO_ROOT / "state" / "lever_manifest.yaml"

def load_manifest():
    if not MANIFEST_PATH.exists():
        # Create default if missing
        return {
            "active_branches": [],
            "max_concurrent": 3,
            "policy": "default",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "levers": []
        }
    with open(MANIFEST_PATH, 'r') as f:
        return yaml.safe_load(f) or {}

def save_manifest(manifest):
    manifest['updated_at'] = datetime.now(timezone.utc).isoformat()
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, 'w') as f:
        yaml.dump(manifest, f, sort_keys=False)

def list_levers(args):
    manifest = load_manifest()
    levers = manifest.get('levers', [])
    if not levers:
        print("[INFO] No task-based levers defined in manifest.")
    else:
        print(f"{'ID':<25} {'Role':<15} {'Name'}")
        print("-" * 60)
        for lever in levers:
            print(f"{lever['id']:<25} {lever.get('role', 'any'):<15} {lever['name']}")
    
    active = manifest.get('active_branches', [])
    if active:
        print("\nActive Lever Branches:")
        for b in active:
            print(f"  - {b}")

def execute_lever(args):
    manifest = load_manifest()
    lever = next((l for l in manifest.get('levers', []) if l['id'] == args.id), None)
    
    if not lever:
        print(f"[ERROR] Lever {args.id} not found.")
        sys.exit(1)
    
    print(f"[INFO] Executing Lever: {lever['name']} ({lever.get('role', 'any')})")
    print(f"[INFO] Command: {lever['command']}")
    
    try:
        # Use shell=True to support piping/complex commands if needed
        result = subprocess.run(lever['command'], cwd=REPO_ROOT, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"[STDERR] {result.stderr}", file=sys.stderr)
        
        if result.returncode == 0:
            print(f"[SUCCESS] Lever {args.id} completed.")
        else:
            print(f"[FAILURE] Lever {args.id} failed with exit code {result.returncode}.")
            sys.exit(result.returncode)
            
    except Exception as e:
        print(f"[ERROR] Execution failed: {e}")
        sys.exit(1)

def create_branch(args):
    manifest = load_manifest()
    max_c = manifest.get('max_concurrent', 3)
    active = manifest.get('active_branches', [])
    
    if len(active) >= max_c:
        print(f"[BLOCKED] Maximum concurrent lever branches ({max_c}) reached.")
        sys.exit(1)
        
    # Format: lever/<id>/<tension>/<date>
    date_str = datetime.now().strftime('%Y-%m-%d')
    branch_name = f"lever/{args.id}/{args.tension}/{date_str}"
    
    if branch_name in active:
        print(f"[INFO] Branch {branch_name} is already active.")
        return

    print(f"[INFO] Creating Lever Branch: {branch_name}")
    
    # Check if git is available and repo is a git repo
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=REPO_ROOT, check=True, capture_output=True)
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=REPO_ROOT, check=True)
        print(f"[SUCCESS] Switched to new branch: {branch_name}")
    except Exception as e:
        print(f"[WARNING] Git operation failed or not in a git repo: {e}")
        print("[INFO] Registering branch in manifest anyway for tracking.")

    active.append(branch_name)
    manifest['active_branches'] = active
    save_manifest(manifest)

def main():
    parser = argparse.ArgumentParser(description="Multiplicity Unified Lever Manager")
    subparsers = parser.add_subparsers(dest="command")
    
    # List
    subparsers.add_parser("list", help="List available levers and active branches")
    
    # Exec
    exec_parser = subparsers.add_parser("exec", help="Execute a task-based lever")
    exec_parser.add_argument("id", help="ID of the lever to execute")
    
    # Branch
    branch_parser = subparsers.add_parser("branch", help="Create a resolution branch for a lever")
    branch_parser.add_argument("id", help="ID of the tension/finding")
    branch_parser.add_argument("--tension", type=int, default=50, help="Initial dissonance tension (0-100)")
    
    args = parser.parse_args()
    
    if args.command == "list":
        list_levers(args)
    elif args.command == "exec":
        execute_lever(args)
    elif args.command == "branch":
        create_branch(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
