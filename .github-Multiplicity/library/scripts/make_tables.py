#!/usr/bin/env python3
# Aggregate JSONL logs into CSV tables.

import argparse, os, glob, json, csv

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="indir", required=True)
    ap.add_argument("--out", dest="outdir", required=True)
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    logs = sorted(glob.glob(os.path.join(args.indir, "logs", "*.jsonl")))
    rows = []
    for log in logs:
        with open(log, "r", encoding="utf-8") as f:
            for line in f:
                rows.append(json.loads(line))

    if not rows:
        print("No logs found; nothing to write.")
        return

    out_csv = os.path.join(args.outdir, "all_results.csv")
    cols = ["config","experiment","n","tiers","R1","R2","R3","R","seed"]
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in cols})
    print("Wrote", out_csv)

if __name__ == "__main__":
    main()
