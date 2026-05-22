#!/usr/bin/env python3
# Execute experiments defined in YAML configs.
# Minimal runner: generates lattice patterns from operator lists and logs resonance metrics.

import argparse, os, glob, json, math, sys
from typing import Any, Dict, List
import numpy as np

try:
    import yaml  # type: ignore
    HAVE_YAML = True
except Exception:
    HAVE_YAML = False

def naive_yaml_load(text: str) -> Dict[str, Any]:
    # Extremely small fallback: handles a tiny subset of YAML.
    data: Dict[str, Any] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line and not line.startswith("-"):
            key, val = line.split(":", 1)
            key, val = key.strip(), val.strip()
            if val.lower() in ("true","false"):
                data[key] = (val.lower()=="true")
            else:
                try:
                    data[key] = int(val)
                except ValueError:
                    try:
                        data[key] = float(val)
                    except ValueError:
                        data[key] = val.strip('"').strip("'")
    return data

def load_config(path: str) -> Dict[str, Any]:
    text = open(path, "r", encoding="utf-8").read()
    if HAVE_YAML:
        return yaml.safe_load(text)  # type: ignore
    return naive_yaml_load(text)

def divisibility_mask(n: int, d: int, offset: int = 0) -> np.ndarray:
    t = np.arange(n, dtype=int)
    return ((t - offset) % d) == 0

def apply_word_ops(n: int, ops: List[Dict[str, Any]]) -> np.ndarray:
    x = np.zeros(n, dtype=float)
    for op in ops or []:
        kind = op.get("kind")
        if kind == "A":
            d = int(op["d"]); a = float(op.get("alpha", 0.0))
            m = divisibility_mask(n, d)
            x[m] += a
        elif kind == "Aoff":
            d = int(op["d"]); a = float(op.get("alpha", 0.0)); off = int(op.get("offset", 0))
            m = divisibility_mask(n, d, off)
            x[m] += a
        elif kind == "W":
            p = int(op.get("p", 2)); perm = list(op.get("perm", [1,0]))
            if p == 2 and perm == [1,0]:
                y = x.copy()
                for b in range(0, n, 4):
                    if b+2 < n:
                        y[b+0], y[b+2] = x[b+2], x[b+0]
                x = y
        # S/R ignored in this minimal runner
    return x

def R1(x: np.ndarray, D: np.ndarray) -> float:
    n = len(x)
    w = 0.5 - 0.5 * np.cos(2*np.pi*np.arange(n)/n)
    xa = x * w; Da = D * w
    best = 0.0
    for tau in range(n):
        y = np.roll(Da, tau)
        num = float(np.dot(xa, y))
        den = float(np.linalg.norm(xa)*np.linalg.norm(y))
        if den == 0: continue
        best = max(best, (num/den)**2)
    return float(best)

def comb_energy(X2: np.ndarray, step: int) -> float:
    idx = np.arange(0, len(X2), step, dtype=int)
    if len(idx)==0: return 0.0
    num = float(np.sum(X2[idx]))
    den = float(np.sum(X2))
    return 0.0 if den==0 else num/den

def R2(x: np.ndarray, D: np.ndarray, tiers: List[int]) -> float:
    X = np.abs(np.fft.rfft(x))**2
    Y = np.abs(np.fft.rfft(D))**2
    n = len(x)
    s = 0.0
    S = sum(tiers) if tiers else 1
    etas = [d/S for d in tiers] if tiers else [1.0]
    for eta, d in zip(etas, tiers if tiers else [n]):
        step = n//d if d>0 else n
        s += eta * math.sqrt(comb_energy(X, step) * comb_energy(Y, step))
    return float(s)

def R3(x: np.ndarray, D: np.ndarray, tiers: List[int]) -> float:
    n = len(x)
    X = np.fft.rfft(x); Y = np.fft.rfft(D)
    s = 0.0
    S = sum(tiers) if tiers else 1
    etas = [d/S for d in tiers] if tiers else [1.0]
    for eta, d in zip(etas, tiers if tiers else [n]):
        step = n//d if d>0 else n
        idx = np.arange(step, len(X), step, dtype=int)
        if len(idx)==0: continue
        ph = np.exp(1j * (np.angle(X[idx]) - np.angle(Y[idx])))
        s += eta * float(np.abs(np.mean(ph)))
    return float(s)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--configs", required=True, help="directory of YAML configs")
    ap.add_argument("--out", required=True, help="outputs root directory")
    ap.add_argument("--threads", type=int, default=1)
    args = ap.parse_args()

    os.makedirs(os.path.join(args.out, "logs"), exist_ok=True)

    cfg_paths = sorted(glob.glob(os.path.join(args.configs, "*.yml")))
    cfg_paths = [p for p in cfg_paths if not os.path.basename(p).startswith("common")]
    if not cfg_paths:
        print("No configs found.", file=sys.stderr); sys.exit(1)

    for cfg_path in cfg_paths:
        cfg = load_config(cfg_path)
        exp = str(cfg.get("experiment", os.path.splitext(os.path.basename(cfg_path))[0]))
        lattice = cfg.get("lattice", {})
        ns = lattice.get("n") or lattice.get("n_candidates") or [108]
        if isinstance(ns, int): ns = [ns]
        word_ops = ((cfg.get("word", {}) or {}).get("ops") or [])

        base_tiers = [2,3,4,5,7,9,27]

        out_log = os.path.join(args.out, "logs", f"{exp}.jsonl")
        with open(out_log, "w", encoding="utf-8") as logf:
            for n in ns:
                tiers = [d for d in base_tiers if int(n) % d == 0] or [int(n)]
                x = apply_word_ops(int(n), word_ops)
                rng = np.random.default_rng(0)
                D = x + 0.01*rng.standard_normal(int(n))

                r1 = R1(x, D)
                r2 = R2(x, D, tiers)
                r3 = R3(x, D, tiers)
                R = 0.40*r1 + 0.35*r2 + 0.25*r3

                rec = {
                    "config": os.path.basename(cfg_path),
                    "experiment": exp,
                    "n": int(n),
                    "tiers": tiers,
                    "R1": round(r1,6),
                    "R2": round(r2,6),
                    "R3": round(r3,6),
                    "R": round(R,6),
                    "seed": 0,
                }
                logf.write(json.dumps(rec)+"\n")
        print(f"Wrote {out_log}")

if __name__ == "__main__":
    main()
