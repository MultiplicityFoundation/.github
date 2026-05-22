---
slug: qs-test-instructions
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/tyler-vanosdol/QS Test Instructions.md
  last_synced: '2026-03-20T17:17:14.611975Z'
---

Let's turn quantum-supremacy benchmarking into a repeatable test harness
you can run against **PIRTM** (and any other system) so comparisons are
apples-to-apples. I'll give you:

1.  a clear list of metrics to compute (precise formulas),

2.  an experiment protocol (how to generate/measure data), and

3.  runnable Python scaffolding (framework + functions) you can drop
    > into your repo to run real experiments and produce CSVs/figures.

I assume PIRTM can (a) emit sample bitstrings for circuits/tasks, (b)
report wall-clock times, and (c) export required metadata (circuit
description, prime-indexed provenance, Λₘ traces). If anything differs,
you can patch the run\_task() hook in the harness.

**1 --- Metrics we'll compute**
===============================

(precise, implementable)

1.  **Cross-Entropy Benchmarking (XEB)\
    > ** Standard XEB for a task with target ideal distribution
    > Pideal(x)P\_\\text{ideal}(x) and observed samples {xi}\\{x\_i\\}:\
    > XEB=2n⋅1N∑i=1NPideal(xi)−1\\text{XEB} = 2\^n \\cdot
    > \\frac{1}{N}\\sum\_{i=1}\^{N} P\_\\text{ideal}(x\_i) - 1\
    > where nn = number of qubits / logical degrees and NN = number of
    > samples.

2.  **Fidelity (estimated from XEB)\
    > ** For random circuit sampling: F≈XEBF \\approx \\text{XEB} (under
    > usual assumptions). Report 95% CI via bootstrap.

3.  **Task Time Ratio (Quantum vs Classical)\
    > ** For a task TT: measure tQt\_Q (quantum wall time including
    > compilation and readout) and estimate or measure tCt\_C
    > (best-known classical wall time). Report\
    > RT=tCtQR\_T = \\frac{t\_C}{t\_Q}\
    > If tCt\_C is simulated / extrapolated, include modeling
    > assumptions and error bars.

4.  **rQOPS (Reliable Quantum Ops Per Second) --- estimator\
    > ** Use a pragmatic estimator:\
    > rQOPS=QL×fL×(1−ϵL)\\text{rQOPS} = Q\_L \\times f\_L \\times (1 -
    > \\epsilon\_L)\
    > where QLQ\_L = logical qubits, fLf\_L = logical gate rate
    > (ops/sec), ϵL\\epsilon\_L = logical error rate (per op). If
    > logical values unknown, compute from physical values +
    > error-correction overhead estimate.

5.  **Mutual Information / Entropy Marginals\
    > ** Compute pairwise mutual information between qubit measurement
    > marginals to capture entanglement/spread:\
    > I(i;j)=H(i)+H(j)−H(i,j)I(i;j) = H(i) + H(j) - H(i,j)\
    > where HH is empirical Shannon entropy from measured marginals.

6.  **Λₘ Stability Trace (your project-specific)\
    > ** If PIRTM emits Λₘ per layer/step, compute variance and spectral
    > drift:

    -   layerwise mean μΛ(l)\\mu\_{\\Lambda}(l) and stddev
        > σΛ(l)\\sigma\_{\\Lambda}(l)

    -   drift slope via linear regression across layers

    -   alarm if ∣ΔμΛ∣\>kσ\|\\Delta \\mu\_{\\Lambda}\| \> k \\sigma

7.  **Sample Complexity / Confidence\
    > ** For fidelity/XEB, compute how many samples NN required to
    > distinguish fidelity FF vs null F0F\_0 with α=0.05, using
    > bootstrap or analytic variance.

8.  **Practicality Score** (composite)\
    > Weighted score combining fidelity, task time ratio, and rQOPS:\
    > S=wF⋅F\~+wT⋅tanh⁡(log⁡10RT)+wR⋅norm⁡(rQOPS)S = w\_F \\cdot
    > \\tilde{F} + w\_T \\cdot \\tanh(\\log\_{10} R\_T) + w\_R \\cdot
    > \\operatorname{norm}(\\text{rQOPS})\
    > (weights configurable; normalization documented)

**2 --- Experimental protocol (recommended)**
=============================================

1.  **Define tasks** (pick 3 classes)

    -   Random circuit sampling (canonical XEB test) --- varied depths
        > and qubit counts.

    -   Application problem used by D-Wave (e.g., Ising / material
        > simulation) --- map to PIRTM format.

    -   Gaussian boson sampling / or domain-specific PIRTM task that
        > demonstrates advantage.

2.  **For each task and parameter set (n qubits, depth d):\
    > **

    -   Generate M different random problem instances (M ≥ 10).

    -   For each instance:

        -   Run classical simulator to compute or approximate
            > Pideal(x)P\_\\text{ideal}(x). If exact is impossible, use
            > high-fidelity tensor contraction / approximate classical
            > algorithm and record approximation error.

        -   Run PIRTM to produce N measurements (e.g., N = 10k typical
            > for XEB tests; configurable).

        -   Record wall time: compile\_time, run\_time, readout\_time,
            > total\_time.

        -   Capture PIRTM metadata: Λₘ per layer, hardware counters,
            > physical/logical qubits, gate rates, raw measurement
            > bitstrings.

3.  **Repeatability\
    > **

    -   Repeat each run R times (R≥5) to measure variability.

    -   Run classical baseline on best available classical hardware (or
        > model using reliable scaling laws) and record
        > environment/config.

4.  **Analysis\
    > **

    -   Compute XEB per instance and mean±CI across instances.

    -   Compute fidelity, rQOPS, mutual information matrices, Λₘ drift.

    -   Compute Task Time Ratio with uncertainties.

    -   Produce summary CSV per run and dashboards/figures.

**3 --- Runnable Python scaffolding**
=====================================

Below is a modular test harness you can drop into pirtm/bench/. It's
pure Python and uses NumPy/Pandas. Replace placeholder hooks
(run\_task\_on\_pirtm, compute\_ideal\_probabilities) with your PIRTM
integrations or Qiskit/Cirq calls.

\# pirtm/bench/benchmarks.py

import time

import json

import numpy as np

import pandas as pd

from collections import Counter

from math import log2

from scipy.stats import sem

from sklearn.utils import resample

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Helper metric functions

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def xeb\_score(samples, p\_ideal):

\"\"\"

Compute linear XEB: 2\^n \* mean(p\_ideal(x\_i)) - 1

samples: iterable of bitstrings as strings

p\_ideal: dict bitstring-\>probability (can be approximate)

\"\"\"

n = len(next(iter(samples)))

N = len(samples)

vals = np.array(\[p\_ideal.get(s, 0.0) for s in samples\])

return (2\*\*n) \* vals.mean() - 1.0

def bootstrap\_ci\_stat(samples, p\_ideal, stat\_func, n\_boot=1000,
alpha=0.05):

stats = \[\]

for \_ in range(n\_boot):

bs = resample(samples, replace=True, n\_samples=len(samples))

stats.append(stat\_func(bs, p\_ideal))

lo = np.percentile(stats, 100\*alpha/2)

hi = np.percentile(stats, 100\*(1-alpha/2))

return np.mean(stats), (lo, hi)

def mutual\_information\_from\_counts(counts, total\_samples):

\# counts: dict mapping tuples (i\_bit, j\_bit) -\> count for a pair,

\# but here we implement simple pairwise MI from full bitstring samples.

pass \# implemented below in compute\_pairwise\_mutual\_info

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Analysis utilities

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def empirical\_probs(samples):

c = Counter(samples)

total = sum(c.values())

return {k: v/total for k, v in c.items()}

def compute\_pairwise\_mutual\_info(samples):

\"\"\"

samples: list of bitstring strings

returns pairwise MI matrix (n x n)

\"\"\"

N = len(samples)

n = len(samples\[0\])

arr = np.array(\[\[int(b) for b in s\] for s in samples\])

mi = np.zeros((n,n))

for i in range(n):

xi = arr\[:,i\]

Hi = entropy\_from\_binary(xi)

for j in range(i+1,n):

xj = arr\[:,j\]

Hij = entropy\_from\_binary\_joint(xi, xj)

Hj = entropy\_from\_binary(xj)

mi\[i,j\] = Hi + Hj - Hij

mi\[j,i\] = mi\[i,j\]

return mi

def entropy\_from\_binary(x):

p1 = x.mean()

p0 = 1-p1

h = 0.0

for p in (p0,p1):

if p\>0:

h -= p \* np.log2(p)

return h

def entropy\_from\_binary\_joint(x, y):

pairs = np.array(\[x, y\]).T

\# compute distribution over (0,0),(0,1),(1,0),(1,1)

counts = {}

for a,b in pairs:

counts\[(a,b)\] = counts.get((a,b), 0) + 1

H = 0.0

for v in counts.values():

p = v / len(pairs)

H -= p \* np.log2(p)

return H

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Replace these hooks

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def compute\_ideal\_probabilities(instance\_spec):

\"\"\"

Given an instance spec (circuit description), compute ideal
probabilities.

Replace with exact simulator, tensor-contraction, or stored ideal.

Return: dict bitstring-\>prob

\"\"\"

raise NotImplementedError(\"Replace compute\_ideal\_probabilities with
your simulator\")

def run\_task\_on\_pirtm(instance\_spec, n\_samples=10000):

\"\"\"

Replace with your PIRTM invocation.

Must return dict:

{

\'samples\': list of bitstrings,

\'metadata\': { \'compile\_time\':\..., \'run\_time\':\...,
\'readout\_time\':\..., \'Lambda\_trace\': \[\...\], \... }

}

\"\"\"

raise NotImplementedError(\"Replace run\_task\_on\_pirtm with PIRTM run
hook\")

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# High-level benchmark runner

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def run\_instance\_benchmark(instance\_spec, n\_samples=10000,
n\_repeats=3):

results = \[\]

p\_ideal = compute\_ideal\_probabilities(instance\_spec)

for r in range(n\_repeats):

start = time.time()

out = run\_task\_on\_pirtm(instance\_spec, n\_samples=n\_samples)

end = time.time()

samples = out\[\'samples\'\]

metadata = out.get(\'metadata\', {})

total\_time = end - start

emp\_probs = empirical\_probs(samples)

xeb = xeb\_score(samples, p\_ideal)

xeb\_mean, xeb\_ci = bootstrap\_ci\_stat(samples, p\_ideal, xeb\_score,
n\_boot=500)

mi = compute\_pairwise\_mutual\_info(samples)

mi\_summary = {\'mi\_mean\': np.mean(mi), \'mi\_max\': np.max(mi)}

lambda\_trace = metadata.get(\'Lambda\_trace\', \[\])

lambda\_stats = {}

if lambda\_trace:

arr = np.array(lambda\_trace)

lambda\_stats = {\'lambda\_mean\': arr.mean(axis=0).tolist() if
arr.ndim\>1 else float(arr.mean()),

\'lambda\_std\': arr.std(axis=0).tolist() if arr.ndim\>1 else
float(arr.std())}

results.append({

\'instance\_id\': instance\_spec.get(\'id\'),

\'repeat\': r,

\'n\_qubits\': instance\_spec\[\'n\_qubits\'\],

\'depth\': instance\_spec.get(\'depth\'),

\'xeb\': xeb,

\'xeb\_bootstrap\_mean\': xeb\_mean,

\'xeb\_bootstrap\_ci\_lo\': xeb\_ci\[0\],

\'xeb\_bootstrap\_ci\_hi\': xeb\_ci\[1\],

\'mi\_mean\': mi\_summary\[\'mi\_mean\'\],

\'mi\_max\': mi\_summary\[\'mi\_max\'\],

\'total\_time\': total\_time,

\'compile\_time\': metadata.get(\'compile\_time\'),

\'run\_time\': metadata.get(\'run\_time\'),

\'readout\_time\': metadata.get(\'readout\_time\'),

\'lambda\_stats\': json.dumps(lambda\_stats),

\'emp\_prob\_nonzero\': len(emp\_probs),

\'raw\_counts\_sample\':
json.dumps(dict(Counter(samples).most\_common(10)))

})

return results

def save\_results\_csv(results, filename):

df = pd.DataFrame(results)

df.to\_csv(filename, index=False)

return df

\# Example driver

if \_\_name\_\_ == \"\_\_main\_\_\":

\# build a few instance specs (user should replace)

instances = \[

{\'id\': \'rand-12-20\', \'n\_qubits\': 12, \'depth\': 20, \'seed\':
42},

{\'id\': \'rand-16-18\', \'n\_qubits\': 16, \'depth\': 18, \'seed\':
101}

\]

all\_results = \[\]

for inst in instances:

r = run\_instance\_benchmark(inst, n\_samples=5000, n\_repeats=3)

all\_results.extend(r)

df = save\_results\_csv(all\_results, \'pirtm\_benchmark\_results.csv\')

print(df.head())

**Notes on integration**

-   compute\_ideal\_probabilities can call a Qiskit/Cirq simulator, or
    > use an amplitude simulator you already have for prime-indexed
    > circuits.

-   run\_task\_on\_pirtm should return raw bitstrings exactly as
    > measured. Keep measurement formatting consistent.

**4 --- Classical baseline estimation**
=======================================

If you cannot run the classical job on an actual supercomputer, use an
extrapolation model:

-   Fit classical runtime for small n using exact simulator (dense state
    > vector) or tensor contraction with measured memory/time scaling.

-   Fit to tC(n)=a⋅bnt\_C(n) = a \\cdot b\^n (exponential) or to tensor
    > contraction models (depend on entanglement structure).

-   Always report model R² and prediction intervals.

Add a classical\_baseline.py that runs classical simulators up to the
feasible n, computes scaling parameters, and extrapolates with CI.

**5 --- Statistical significance and reproducibility**
======================================================

-   Use bootstrap to get CI for XEB and fidelity. Report p-value for the
    > null hypothesis that fidelity ≤ F0 (e.g., random guess baseline
    > F0=0F\_0 = 0).

-   Report environmental metadata: CPU type, classical simulator
    > version, PIRTM software version, firmware, temperature if relevant
    > --- this matters when claims are challenged.

**6 --- Output / reporting format**
===================================

Produce the following artifacts per experiment:

-   pirtm\_benchmark\_results.csv (one row per run)

-   summary\_report.json (aggregated means, cis, task ratios)

-   figures: XEB vs depth, XEB vs n\_qubits, rQOPS timeline, Λₘ traces
    > per layer (saved as PNG)

-   a Markdown experiment\_README.md capturing exact commands run and
    > environment.

**7 --- Extensions & advanced diagnostics**
===========================================

-   **Layerwise fidelity**: measure XEB for prefixes/truncated circuits
    > to see where fidelity drops.

-   **Error budget breakdown**: decompose via tomography or randomized
    > benchmarking per gate to estimate ϵ\\epsilon.

-   **Noise injection experiments**: inject synthetic noise and measure
    > robustness curve.

-   **Prime-indexed provenance checks**: correlate Λₘ drift with
    > fidelity drops to detect semantic drift.

**8 --- Quick checklist to start running (minimal)**
====================================================

1.  Implement run\_task\_on\_pirtm to return samples and metadata.

2.  Implement compute\_ideal\_probabilities (or provide precomputed
    > ideal files).

3.  Run the harness for a small grid: n\_qubits = \[8, 10, 12, 14\],
    > depths = \[10, 20, 30\], N=5000 samples.

4.  Produce CSV + figures, then compute task time ratio using local
    > classical simulator and/or extrapolated baseline.

If you want, I can:

-   generate a full classical\_baseline.py that fits scaling laws from
    > small-n simulator runs, or

-   adapt the harness to output a Jupyter notebook that visualizes
    > XEB/fidelity/rQOPS side-by-side, or

-   implement compute\_ideal\_probabilities using a simulator
    > (statevector/tensor contraction) for n up to e.g. 20 --- tell me
    > which one you prefer and I'll produce the code now.
