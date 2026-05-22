#!/usr/bin/env python3
# Emit per-run seeds and basic stats from JSONL logs.

import argparse, os, glob, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    logs = sorted(glob.glob(os.path.join(args.logs, "*.jsonl")))
    lines = []
    for lg in logs:
        with open(lg, "r", encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                lines.append(f"{rec.get('experiment')} n={rec.get('n')} seed={rec.get('seed')} R={rec.get('R')}")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as out:
        out.write("# Seed and run report\n")
        for ln in lines:
            out.write(ln + "\n")
    print("Wrote", args.out)

if __name__ == "__main__":
    main()
