#!/usr/bin/env python3
"""
Unified Library System Facade for Multiplicity.
Orchestrates indexing, math correction, and AI curation.
"""

import argparse
import sys
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "library" / "scripts"

def run_script(script_name, *args):
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        print(f"[ERROR] Script not found: {script_path}")
        return False
    
    cmd = [sys.executable, str(script_path)] + list(args)
    print(f"[EXEC] {' '.join(cmd)}")
    
    # We use REPO_ROOT/library as CWD for build_index.py to maintain its path logic
    result = subprocess.run(cmd, cwd=REPO_ROOT / "library")
    return result.returncode == 0

def build_index():
    print("[INFO] Rebuilding Master Index...")
    # build_index.py expects to run in library/
    return run_script("build_index.py", "--minify")

def normalize_math():
    print("[INFO] Normalizing Math Expressions...")
    # math_corrector.py defaults to 'articles'
    return run_script("math_corrector.py", "--path", "articles")

def ai_curate():
    print("[INFO] AI Metadata Curation (Stub)...")
    # This would iterate over articles and call ai_assist.py
    # For now, we'll just show the intent
    print("[TODO] Implement bulk AI curation loop.")
    return True

def verify_rigor():
    print("[INFO] Verifying Formal Rigor (Stub)...")
    # This would link to lean4/ verification if available
    print("[TODO] Connect to lean4/ verification artifacts.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Multiplicity Library System")
    parser.add_argument("command", choices=["build-index", "normalize-math", "ai-curate", "verify-rigor"])
    
    args = parser.parse_args()
    
    success = False
    if args.command == "build-index":
        success = build_index()
    elif args.command == "normalize-math":
        success = normalize_math()
    elif args.command == "ai-curate":
        success = ai_curate()
    elif args.command == "verify-rigor":
        success = verify_rigor()
    
    if success:
        print(f"[SUCCESS] Command {args.command} finished.")
        sys.exit(0)
    else:
        print(f"[FAILURE] Command {args.command} failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
