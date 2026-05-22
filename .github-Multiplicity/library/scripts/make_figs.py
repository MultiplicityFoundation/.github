#!/usr/bin/env python3
# Build publication figures from outputs or generate canonical placeholders.
# Rules: matplotlib only, each chart its own figure, no explicit colors.

import argparse, os
import numpy as np
import matplotlib.pyplot as plt

def fig_operator_diagrams(path: str):
    plt.figure()
    plt.title("Operator diagrams: S, A, R, W, Q̂")
    xs = np.arange(5)
    ys = np.array([0,1,0,1,0])
    plt.plot(xs, ys, marker='o')
    plt.xlabel("operator index")
    plt.ylabel("schematic output")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def fig_crt_tilings(path: str, n: int = 108):
    plt.figure()
    t = np.arange(n)
    x = t % 4
    y = t % 27
    plt.scatter(x, y, s=10)
    plt.title("CRT tilings for n=108 (mod 4 vs mod 27)")
    plt.xlabel("t mod 4")
    plt.ylabel("t mod 27")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def fig_resonance_spectra(path: str, n: int = 108):
    plt.figure()
    x = np.zeros(n)
    for t in range(n):
        if t % 27 == 0: x[t] += 1.0
        elif t % 9 == 0: x[t] += 0.7
        elif t % 3 == 0: x[t] += 0.5
        elif t % 4 == 0: x[t] += 0.3
        elif t % 2 == 0: x[t] += 0.2
    X = np.abs(np.fft.rfft(x))
    plt.plot(X)
    plt.title("Resonance spectra (|rFFT| of scaffold)")
    plt.xlabel("harmonic index")
    plt.ylabel("magnitude")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def fig_cadence_map_108(path: str, n: int = 108):
    plt.figure()
    w = np.zeros(n)
    for t in range(n):
        if t % 27 == 0: w[t] = 5
        elif t % 9 == 0: w[t] = 4
        elif t % 3 == 0: w[t] = 3
        elif t % 4 == 0: w[t] = 2
        elif t % 2 == 0: w[t] = 1
        else: w[t] = 0
    plt.stem(np.arange(n), w, use_line_collection=True)
    plt.title("108 cadence map (tick classes C0–C4)")
    plt.xlabel("tick")
    plt.ylabel("class weight")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="indir", required=False, default=".")
    ap.add_argument("--out", dest="outdir", required=True)
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    fig_operator_diagrams(os.path.join(args.outdir, "operator_diagrams.pdf"))
    fig_crt_tilings(os.path.join(args.outdir, "crt_tilings.pdf"))
    fig_resonance_spectra(os.path.join(args.outdir, "resonance_spectra.pdf"))
    fig_cadence_map_108(os.path.join(args.outdir, "cadence_map_108.pdf"))
    print("Figures written to", args.outdir)

if __name__ == "__main__":
    main()
