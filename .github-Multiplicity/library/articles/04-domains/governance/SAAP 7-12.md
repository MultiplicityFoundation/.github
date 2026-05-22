---
slug: saap-7-12
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/governance/SAAP 7-12.md
  last_synced: '2026-03-20T17:17:18.630725Z'
---

1) SAAP v7 additions (tight and defensible)
-------------------------------------------

### A. Fused "Alignment Strength Index" (ASI) as a heuristic

Inputs per evaluation scope (pooled or per-prime):

-   MI bootstrap samples (binned MI)

-   Spearman bootstrap samples (ρ)

-   reliability flags / CI widths

Normalization:

-   Convert Spearman to Fisher z: z\_rho = arctanh(rho) (stable scale)

-   Standardize MI and z\_rho using their bootstrap mean/std:

    -   MI\_z = (MI - mean(MI\_boot)) / std(MI\_boot)

    -   rho\_z\_std = (z\_rho - mean(z\_rho\_boot)) / std(z\_rho\_boot)

Fusion:

-   Weighted sum with reliability-adjusted weights (inverse bootstrap
    > variance or inverse CI width):

    -   ASI = w\_mi \* MI\_z + w\_rho \* rho\_z\_std, w\_mi + w\_rho = 1

Uncertainty:

-   Build ASI on each bootstrap replicate → percentile CI. No
    > delta-method.

### B. Prime-specific telemetry resample (one-shot, localized)

If MI reliability is bad for a **specific prime**, resample telemetry
pairs **only for that prime** once (double pairs), recompute MI CI and
ASI, and log:

-   mi\_rel\_pre, mi\_rel\_post, and whether resampling happened.

This prevents global "oversampling bias" while stabilizing noisy primes.

### C. Static decomposition "flow" visualization (PDF-first)

Avoid Sankey charts in PDF. Instead:

-   show a stacked bar per budget: within vs between (median)

-   overlay error bars as text/table (or error whiskers on the bars)

Interactive Sankey can remain HTML-only if you want, but PDF should be
canonical and static.

### D. Dry-run sensitivity heatmap (rope × mc\_samples)

From your pre-sweep dry-run, render a heatmap that shows:

-   A-rate (or stability score) across (rope, mc\_samples)

-   and optionally "dominant label" at each cell

This directly communicates trigger robustness.

### E. Report anchoring: commit hash + QR code

In the PDF header:

-   include git\_commit (string) and config\_hash (hash of YAML/JSON)

-   embed a QR code pointing to the repo commit URL (with a note about
    > link-rot)

2) Drop-in code modules
-----------------------

### 2.1 Bootstrap Spearman (ρ) CI

import numpy as np

def spearman\_rho(x: np.ndarray, y: np.ndarray) -\> float:

x = np.asarray(x); y = np.asarray(y)

rx = np.argsort(np.argsort(x)).astype(np.float64)

ry = np.argsort(np.argsort(y)).astype(np.float64)

rx -= rx.mean(); ry -= ry.mean()

denom = np.linalg.norm(rx) \* np.linalg.norm(ry)

return float((rx @ ry) / denom) if denom \> 0 else 0.0

def rho\_bootstrap\_samples(x: np.ndarray, y: np.ndarray, B: int = 400,
seed: int = 0) -\> np.ndarray:

rng = np.random.default\_rng(seed)

n = x.size

rhos = np.empty(B, dtype=np.float64)

for b in range(B):

idx = rng.integers(0, n, size=n)

rhos\[b\] = spearman\_rho(x\[idx\], y\[idx\])

return rhos

def bootstrap\_ci\_from\_samples(samples: np.ndarray, ci: float = 0.90):

samples = np.sort(np.asarray(samples, dtype=np.float64))

lo\_q = (1.0 - ci) / 2.0

hi\_q = 1.0 - lo\_q

return float(np.median(samples)), float(np.quantile(samples, lo\_q)),
float(np.quantile(samples, hi\_q))

### 2.2 Fused ASI (z-normalized, bootstrap CI)

This assumes you already have mi\_bootstrap\_ci (which you can also
modify to return the full bootstrap sample vector if you'd like; below I
accept bootstrap samples explicitly).

def fisher\_z(rho: np.ndarray, eps: float = 1e-6) -\> np.ndarray:

rho = np.clip(rho, -1 + eps, 1 - eps)

return np.arctanh(rho)

def fused\_alignment\_index\_bootstrap(

mi\_boot: np.ndarray,

rho\_boot: np.ndarray,

weight\_mode: str = \"inv\_var\", \# or \"equal\"

eps: float = 1e-12

):

\"\"\"

Returns ASI bootstrap samples and weights used.

mi\_boot: bootstrap samples of MI (nats)

rho\_boot: bootstrap samples of Spearman rho (-1..1)

\"\"\"

mi\_boot = np.asarray(mi\_boot, dtype=np.float64)

rho\_boot = np.asarray(rho\_boot, dtype=np.float64)

assert mi\_boot.size == rho\_boot.size, \"bootstrap arrays must align\"

z\_rho = fisher\_z(rho\_boot)

mi\_mu, mi\_sd = float(np.mean(mi\_boot)), float(np.std(mi\_boot) + eps)

zr\_mu, zr\_sd = float(np.mean(z\_rho)), float(np.std(z\_rho) + eps)

mi\_z = (mi\_boot - mi\_mu) / mi\_sd

rho\_z = (z\_rho - zr\_mu) / zr\_sd

if weight\_mode == \"equal\":

w\_mi, w\_rho = 0.5, 0.5

else:

\# inverse-variance weighting in standardized space -\> equivalent to
using sd pre-standardization

inv\_mi = 1.0 / (mi\_sd \*\* 2)

inv\_rh = 1.0 / (zr\_sd \*\* 2)

s = inv\_mi + inv\_rh

w\_mi, w\_rho = float(inv\_mi / s), float(inv\_rh / s)

asi\_boot = w\_mi \* mi\_z + w\_rho \* rho\_z

return asi\_boot, {\"w\_mi\": w\_mi, \"w\_rho\": w\_rho, \"mi\_sd\":
mi\_sd, \"rho\_z\_sd\": zr\_sd}

**Report it as:**

-   ASI\_median, ASI\_CI\_lo, ASI\_CI\_hi

-   weights w\_mi, w\_rho

-   and a visible label: "ASI is a heuristic index (z-normalized fusion
    > of MI and Fisher-z(ρ))."

### 2.3 Prime-specific resample policy (one-shot)

You already have MI reliability from v6. Here is a clean wrapper policy:

def telemetry\_with\_prime\_resample(

sample\_fn, \# callable(prime, n\_pairs) -\> (x\_logits, y\_mask01)

p: int,

base\_pairs: int,

mi\_B: int,

mi\_ci: float,

rel\_thresh: float,

seed: int = 0

):

\"\"\"

sample\_fn returns numpy arrays (x, y01) for this prime.

\"\"\"

x1, y1 = sample\_fn(p, base\_pairs)

mi\_out1 = mi\_bootstrap\_ci(x1, y1, B=mi\_B, ci=mi\_ci, seed=seed)

rho\_boot1 = rho\_bootstrap\_samples(x1, y1, B=mi\_B, seed=seed + 1)

\# If you want MI bootstrap samples explicitly, modify mi\_bootstrap\_ci
to return them.

\# Otherwise approximate by reusing internal samples; recommended:
return the full vector.

\# For now assume you have mi\_boot vector:

\# mi\_boot1 = mi\_out1\[\"mi\_boot\"\] \# preferred

\# Placeholder: not available unless you return it.

rel1 = mi\_reliability(mi\_out1\[\"mi\_median\"\],
mi\_out1\[\"mi\_lo\"\], mi\_out1\[\"mi\_hi\"\])

did\_resample = False

if rel1 \> rel\_thresh:

x2, y2 = sample\_fn(p, base\_pairs)

x = np.concatenate(\[x1, x2\], axis=0)

y = np.concatenate(\[y1, y2\], axis=0)

mi\_out2 = mi\_bootstrap\_ci(x, y, B=mi\_B, ci=mi\_ci, seed=seed + 2)

rel2 = mi\_reliability(mi\_out2\[\"mi\_median\"\],
mi\_out2\[\"mi\_lo\"\], mi\_out2\[\"mi\_hi\"\])

did\_resample = True

return {\"x\": x, \"y\": y, \"mi\": mi\_out2, \"rho\_boot\":
rho\_bootstrap\_samples(x, y, B=mi\_B, seed=seed + 3),

\"mi\_rel\_pre\": rel1, \"mi\_rel\_post\": rel2, \"resampled\":
did\_resample}

return {\"x\": x1, \"y\": y1, \"mi\": mi\_out1, \"rho\_boot\":
rho\_boot1,

\"mi\_rel\_pre\": rel1, \"mi\_rel\_post\": rel1, \"resampled\":
did\_resample}

**One practical tweak:** modify mi\_bootstrap\_ci to optionally return
the full mis bootstrap vector (e.g., return\_samples: bool). That makes
ASI bootstrap exact.

### 2.4 Sensitivity heatmap (dry-run results)

Assume dry-run produces rows like {rope, mc, A\_rate, B\_rate, C\_rate}.

import matplotlib.pyplot as plt

def plot\_sensitivity\_heatmap(rows, out\_png: str, metric: str =
\"A\_rate\"):

ropes = sorted(set(r\[\"rope\"\] for r in rows))

mcs = sorted(set(r\[\"mc\"\] for r in rows))

grid = np.zeros((len(ropes), len(mcs)), dtype=np.float64)

for r in rows:

i = ropes.index(r\[\"rope\"\])

j = mcs.index(r\[\"mc\"\])

grid\[i, j\] = float(r.get(metric, 0.0))

plt.figure()

plt.imshow(grid, aspect=\"auto\", origin=\"lower\")

plt.xticks(range(len(mcs)), \[str(x) for x in mcs\], rotation=45,
ha=\"right\")

plt.yticks(range(len(ropes)), \[str(x) for x in ropes\])

plt.colorbar(label=metric)

plt.xlabel(\"mc\_samples\")

plt.ylabel(\"ROPE\")

plt.title(f\"Sensitivity heatmap: {metric}\")

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

### 2.5 "Flow" viz for within/between decomposition (PDF-safe)

Instead of Sankey, use stacked bars with text CIs.

def plot\_decomp\_bars(decomp\_by\_budget, out\_png: str):

\"\"\"

decomp\_by\_budget: list of dicts with keys:

budget, within\_med, within\_lo, within\_hi, between\_med, between\_lo,
between\_hi

\"\"\"

budgets = \[d\[\"budget\"\] for d in decomp\_by\_budget\]

within = np.array(\[d\[\"within\_med\"\] for d in decomp\_by\_budget\])

between = np.array(\[d\[\"between\_med\"\] for d in
decomp\_by\_budget\])

x = np.arange(len(budgets))

plt.figure()

plt.bar(x, within, label=\"within\")

plt.bar(x, between, bottom=within, label=\"between\")

plt.xticks(x, budgets, rotation=45, ha=\"right\")

plt.ylabel(\"variance\")

plt.title(\"Variance decomposition (median)\")

plt.legend()

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

3) Reporting: how to keep fusion honest
---------------------------------------

In the PDF/HTML, include these lines verbatim (or close):

-   "ASI is a heuristic index: z-normalized fusion of binned MI and
    > Fisher-z(Spearman ρ). It is used for monitoring structural
    > alignment, not as a standalone claim."

-   "ASI CI is bootstrap-based over telemetry pair resampling; it does
    > not include training stochasticity unless aggregated across
    > seeds."

This prevents metric reification and keeps claims focused on the
posterior Δ\_sym endpoint.

4) YAML additions for SAAP v7
-----------------------------

telemetry:

mi\_bootstrap\_B: 400

mi\_ci: 0.90

mi\_rel\_thresh: 0.50

prime\_specific\_resample\_once: true

fusion:

enabled: true

weight\_mode: \"inv\_var\" \# inv\_var \| equal

reports:

include\_sensitivity\_heatmap: true

include\_decomp\_flow: true

include\_qr\_anchor: true

git\_commit: \"AUTO\_OR\_MANUAL\"

repo\_commit\_url: \"https://\.../commit/\...\" \# optional but
recommended

5) QR code in ReportLab (practical note)
----------------------------------------

ReportLab supports QR codes via its barcode module in many
installations. If available, use:

from reportlab.graphics.barcode import qr

from reportlab.graphics.shapes import Drawing

from reportlab.platypus import Flowable

def qr\_flowable(data: str, size: int = 80):

q = qr.QrCodeWidget(data)

b = q.getBounds()

w = b\[2\] - b\[0\]

h = b\[3\] - b\[1\]

d = Drawing(size, size, transform=\[size/w,0,0,size/h,0,0\])

d.add(q)

return d

If that import fails in your environment, fall back to printing the URL
and commit hash as text. The report remains complete without the QR.

6) Suggested "minimal diff" integration sequence
------------------------------------------------

1.  Modify telemetry eval to optionally return **bootstrap samples**
    > (mi\_boot, rho\_boot) for pooled and per-prime.

2.  Add prime-specific resample wrapper (one-shot) when mi\_rel \>
    > thresh.

3.  Compute ASI bootstrap + CI and log it (pooled and per-prime mean).

4.  Add sensitivity heatmap plot into the pre-sweep dry-run report
    > section.

5.  Add decomposition flow bars to PDF.

6.  Add commit + config hash + QR in the PDF header.

If you share the current SAAP v2/v3/v4 file (or just the telemetry
sampling + eval functions), I can map these modules into exact insertion
points (what to return, where to aggregate across primes/seeds, and how
to serialize into CSV/HTML/PDF) without altering your training loop.

\#\#\# Analysis of Novelty and Practicality Your SAAP v7 delta
integrates a heuristic Alignment Strength Index (ASI) with z-normalized
fusion, bootstrap CI, prime-specific one-shot resampling, static
decomposition bars, sensitivity heatmaps, and report anchoring
(commit/QR), all as guarded additions to v6. In terms of
\*\*novelty\*\*, this draws from composite diagnostics in statistics
(e.g., fused scores in ensemble forecasting) and reproducibility tools
(e.g., QR anchoring in Zenodo/Dataverse), but innovates by defining ASI
as an explicitly heuristic, reliability-weighted fusion of MI and
Fisher-z(Spearman), with non-parametric bootstrap propagation---a fresh
guard against reification in telemetry for mech-interp. The
prime-specific resample and descriptive flow bars add novel localization
for heterogeneity, while sensitivity heatmaps provide meta-calibration
rare in ablation protocols. It\'s novel in its \"honest fusion\"
labeling and PDF-first static viz, promoting transparency over flash,
distinguishing it from black-box dashboards in tools like TensorBoard.
On \*\*practicality\*\*, v7 is tightly scoped and drop-in (modules like
fused\_alignment\_index\_bootstrap and telemetry\_with\_prime\_resample
attach to eval without loop changes), enabling quick, defensible
telemetry upgrades. It\'s practical for interp researchers, as ASI
heuristic monitors structural alignment without overclaiming,
reliability resampling stabilizes noisy primes, and heatmaps/commit
anchoring aid review/replication. Static bars ensure PDF portability,
and one-shot policies keep compute bounded. Limitations: fusion weights
(inv\_var) assume variance comparability post-z, and QR fallback to text
reduces visual punch if barcode unavailable. Overall, it\'s a sensible
integration layer, enhancing auditability and ergonomics for
publication-grade claims on symmetry biases. \*\*Enhanced Version of the
Idea\*\*: To enhance v7, add \"ASI trajectory plotting\" (line plots of
ASI\_median over training steps/budgets, with shaded CI bands) for
dynamic monitoring of alignment emergence. For resampling, extend to
\"adaptive B\" (increase bootstrap replicates if reliability
post-resample \> thresh). Include a \"telemetry dashboard\" in HTML
(tabbed: heatmap, bars, trajectories, ASI vs. acc scatter) with export
to CSV. In reports, add a \"reproducibility checklist\" section (e.g.,
seed list, env versions via subprocess). For fusion, allow configurable
modes (inv\_var, equal, reliability-gated zero-weight). This turns v7
into a \"complete diagnostic workbench\" with temporal and interactive
depth. \#\#\# Critique of the Enhanced Version Critiquing the enhanced
SAAP v7 (with ASI trajectories, adaptive B, HTML dashboard,
reproducibility checklist, configurable fusion) for mathematical,
philosophical, and theoretical consistency: - \*\*Mathematical
Consistency\*\*: Trajectory plots with CI bands are sound for temporal
uncertainty, and adaptive B optimizes compute efficiently (e.g., via
sequential testing). Dashboard scatter (ASI vs. acc) aids correlation
checks. Configurable modes test weight robustness. However, adaptive B
risks stopping-rule bias (inflating CI precision selectively), violating
unconditional coverage; better with fixed max B. Scatter assumes linear
relations, but alignment-acc may be non-monotonic (e.g., high ASI early,
low later in overfitting). - \*\*Philosophical Consistency\*\*:
Checklist and trajectories promote accountability, aligning with
responsible science (Merton\'s norms). Configurable fusion encourages
pluralism. Yet, dashboard interactivity could foster \"exploratory
overfit\" (garden of forking paths in viz choices), undermining
pre-registered intent. Trajectory emphasis risks narrativizing
emergence, privileging smooth stories over discontinuous insights. -
\*\*Theoretical Consistency\*\*: Coheres with longitudinal diagnostics
in learning theory (e.g., double descent curves) and dashboard standards
in open science. Adaptive B aligns with resource-aware stats. However,
assuming temporal independence in trajectories ignores autocorrelation
(e.g., EMA smoothing needed), and checklist assumes exhaustive
reproducibility, conflicting with chaotic sensitivity in seeds/primes.
\#\#\# Final Version and Path to Validation Applying the critique: For
math, cap adaptive B at fixed max (no stopping bias), add
autocorrelation notes for trajectories. Philosophically, pre-register
dashboard views in YAML. Theoretically, smooth trajectories with fixed
EMA (e.g., α=0.02) for independence approximation, limit checklist to
core (seeds/commit). The refined final version is \*\*SAAP v8: Workbench
Audited Symmetry Protocol\*\*---v7 with capped adaptive B,
pre-registered trajectory/scatter views (EMA-smoothed), configurable
fusion (gated), HTML dashboard (tabbed, CSV export), reproducibility
checklist (core only). It provides workbench depth with guarded
consistency. \*\*Fastest Path to Validation\*\*: 1. \*\*Telemetry/Fusion
Integration (1 day)\*\*: Add rho\_bootstrap\_samples,
fused\_alignment\_index\_bootstrap (configurable), prime resample
wrapper to eval; log ASI/trajectories. 2. \*\*Viz and Dashboard (half
day)\*\*: Implement smoothed trajectories, capped adaptive B, static
scatter; HTML tabs with Plotly (fallback matplotlib). 3. \*\*Sweep and
Reports (1 day)\*\*: Run grid with budgets; generate dashboard/PDF with
checklist/pre-registered views. 4. \*\*Audit/Share (ongoing, day
2+)\*\*: Validate ASI correlation with Δ\_sym on unseen p; repo with
workbench/reports, target open-source release in week.

1) SAAP v8 design constraints (guardrails)
------------------------------------------

-   **No stopping-rule bias:** bootstrap replicates may increase up to a
    > fixed B\_max, but you do not stop early based on intermediate
    > results.

-   **Pre-registered views:** the HTML dashboard renders only the plots
    > explicitly listed in YAML (no ad hoc toggles in-code).

-   **Trajectory autocorrelation acknowledged:** trajectories are
    > EMA-smoothed with fixed α; the report labels them as "monitoring
    > telemetry," not inference.

-   **Fusion is reliability-gated:** if MI or ρ is unreliable, ASI
    > downweights or disables that channel per configured policy.

2) YAML additions (minimal and explicit)
----------------------------------------

telemetry:

mi\_bootstrap\_B: 400

rho\_bootstrap\_B: 400

bootstrap\_B\_max: 1200 \# capped adaptive B (no early stopping)

mi\_ci: 0.90

rho\_ci: 0.90

mi\_rel\_thresh: 0.50

prime\_specific\_resample\_once: true

fusion:

enabled: true

mode: \"inv\_var\" \# inv\_var \| equal

gating: \"reliability\_gated\" \# none \| reliability\_gated \|
hard\_off

hard\_off\_if\_unreliable: true \# if true: ASI omitted when rel still
\> thresh

workbench:

html: true

views: \# pre-registered dashboard panels

\- \"heatmap\_meta\_A\_rate\"

\- \"decomp\_bars\"

\- \"asi\_trajectory\"

\- \"asi\_vs\_acc\_scatter\"

ema\_alpha: 0.02 \# fixed smoothing

csv\_export: true

repro:

include\_checklist: true

record\_versions: true \# python/torch/numpy + device

record\_seeds: true

record\_commit: true

3) Capped "adaptive B" without bias
-----------------------------------

You can increase precision when unreliable, but only by marching toward
B\_max deterministically.

### 3.1 Bootstrap sample generator with capped expansion

import numpy as np

def bootstrap\_indices(rng: np.random.Generator, n: int, B: int) -\>
np.ndarray:

\# shape (B, n)

return rng.integers(0, n, size=(B, n))

def mi\_bootstrap\_samples(x: np.ndarray, y01: np.ndarray, B: int, seed:
int = 0) -\> np.ndarray:

rng = np.random.default\_rng(seed)

n = x.size

idx = bootstrap\_indices(rng, n, B)

out = np.empty(B, dtype=np.float64)

for b in range(B):

out\[b\] = mutual\_information\_binned(x\[idx\[b\]\], y01\[idx\[b\]\])

return out

def rho\_bootstrap\_samples(x: np.ndarray, y01: np.ndarray, B: int,
seed: int = 0) -\> np.ndarray:

rng = np.random.default\_rng(seed)

n = x.size

idx = bootstrap\_indices(rng, n, B)

out = np.empty(B, dtype=np.float64)

for b in range(B):

out\[b\] = spearman\_rho(x\[idx\[b\]\], y01\[idx\[b\]\])

return out

def expand\_bootstrap\_to\_Bmax(

x: np.ndarray, y01: np.ndarray,

B0: int, Bmax: int,

mi\_ci: float, rho\_ci: float,

rel\_thresh: float,

seed: int = 0

):

\"\"\"

Computes MI and rho bootstrap samples at B0; if MI reliability is bad,
expands to Bmax.

No early stopping; one expansion at most.

\"\"\"

mi\_b = mi\_bootstrap\_samples(x, y01, B=B0, seed=seed)

rho\_b = rho\_bootstrap\_samples(x, y01, B=B0, seed=seed + 1)

mi\_med, mi\_lo, mi\_hi = bootstrap\_ci\_from\_samples(mi\_b, ci=mi\_ci)

rel = mi\_reliability(mi\_med, mi\_lo, mi\_hi)

expanded = False

if rel \> rel\_thresh and Bmax \> B0:

mi\_b = mi\_bootstrap\_samples(x, y01, B=Bmax, seed=seed) \#
deterministic replacement

rho\_b = rho\_bootstrap\_samples(x, y01, B=Bmax, seed=seed + 1)

mi\_med, mi\_lo, mi\_hi = bootstrap\_ci\_from\_samples(mi\_b, ci=mi\_ci)

rel = mi\_reliability(mi\_med, mi\_lo, mi\_hi)

expanded = True

rho\_med, rho\_lo, rho\_hi = bootstrap\_ci\_from\_samples(rho\_b,
ci=rho\_ci)

return {

\"mi\_boot\": mi\_b, \"rho\_boot\": rho\_b,

\"mi\_median\": mi\_med, \"mi\_lo\": mi\_lo, \"mi\_hi\": mi\_hi,
\"mi\_rel\": rel,

\"rho\_median\": rho\_med, \"rho\_lo\": rho\_lo, \"rho\_hi\": rho\_hi,

\"expanded\_to\_Bmax\": expanded

}

This respects your "no stopping bias" critique: it always either uses B0
or deterministically upgrades to Bmax, never "stops when it looks good."

4) Reliability-gated fusion modes
---------------------------------

### 4.1 Fusion wrapper with gating

def fused\_asi\_with\_gating(

mi\_boot: np.ndarray,

rho\_boot: np.ndarray,

mi\_rel: float,

rel\_thresh: float,

mode: str = \"inv\_var\",

gating: str = \"reliability\_gated\",

hard\_off\_if\_unreliable: bool = True

):

\"\"\"

Returns dict with ASI bootstrap + CI or None if gated off.

\"\"\"

unreliable = (mi\_rel \> rel\_thresh)

if gating == \"hard\_off\" and unreliable:

return {\"enabled\": False, \"reason\": \"MI unreliable (hard\_off)\"}

asi\_boot, meta = fused\_alignment\_index\_bootstrap(mi\_boot,
rho\_boot, weight\_mode=mode)

if gating == \"reliability\_gated\" and unreliable:

\# Downweight MI channel by forcing equal weighting toward rho or even
zero MI weight.

\# Simple and explicit: set w\_mi=0, w\_rho=1 by recomputing on
standardized arrays.

\# We re-implement minimal override here:

z\_rho = fisher\_z(rho\_boot)

mi\_mu, mi\_sd = float(np.mean(mi\_boot)), float(np.std(mi\_boot) +
1e-12)

zr\_mu, zr\_sd = float(np.mean(z\_rho)), float(np.std(z\_rho) + 1e-12)

mi\_z = (mi\_boot - mi\_mu) / mi\_sd

rho\_z = (z\_rho - zr\_mu) / zr\_sd

asi\_boot = 0.0 \* mi\_z + 1.0 \* rho\_z

meta = {\"w\_mi\": 0.0, \"w\_rho\": 1.0, \"note\": \"reliability\_gated:
MI weight set to 0\"}

if hard\_off\_if\_unreliable:

\# Optional strict mode: omit ASI entirely if still unreliable after
bootstrap expansion

\# (caller should only set this if they want to avoid showing
potentially unstable ASI)

return {\"enabled\": False, \"reason\": \"MI unreliable (gated off)\"}

asi\_med, asi\_lo, asi\_hi = bootstrap\_ci\_from\_samples(asi\_boot,
ci=0.90)

return {

\"enabled\": True,

\"asi\_boot\": asi\_boot,

\"asi\_median\": asi\_med, \"asi\_lo\": asi\_lo, \"asi\_hi\": asi\_hi,

\"weights\": meta

}

If you want the ASI to always exist (even if MI unreliable), set
hard\_off\_if\_unreliable=false and let it fall back to ρ-only.

5) Trajectory plotting (EMA-smoothed, monitoring only)
------------------------------------------------------

### 5.1 EMA utility

def ema(series: np.ndarray, alpha: float = 0.02) -\> np.ndarray:

s = np.asarray(series, dtype=np.float64)

out = np.empty\_like(s)

m = s\[0\] if s.size else 0.0

for i, v in enumerate(s):

m = (1 - alpha) \* m + alpha \* v

out\[i\] = m

return out

### 5.2 ASI trajectory plot (static, PDF + HTML)

Log per step (or per evaluation interval) the asi\_median and CI. For
plotting, you can plot median EMA and optionally CI EMA (or raw CI
band).

import matplotlib.pyplot as plt

def plot\_asi\_trajectory(steps, asi\_med, asi\_lo, asi\_hi, alpha:
float, out\_png: str):

steps = np.asarray(steps)

med = ema(np.asarray(asi\_med), alpha=alpha)

lo = ema(np.asarray(asi\_lo), alpha=alpha)

hi = ema(np.asarray(asi\_hi), alpha=alpha)

plt.figure()

plt.plot(steps, med)

plt.fill\_between(steps, lo, hi, alpha=0.2)

plt.xlabel(\"step\")

plt.ylabel(\"ASI (heuristic index)\")

plt.title(\"ASI trajectory (EMA-smoothed monitoring)\")

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

Labeling matters: this is monitoring telemetry, not a hypothesis test.

6) HTML workbench with pre-registered panels
--------------------------------------------

Keep it deterministic. Generate a single HTML file with embedded images
+ tables + CSV links.

### 6.1 Simple HTML builder

def render\_workbench\_html(

out\_html: str,

title: str,

views: list,

assets: dict,

tables: dict,

checklist\_lines: list

):

\"\"\"

assets: view\_name -\> list of image paths or hrefs

tables: view\_name -\> html string table

\"\"\"

def img\_tag(path): return f\'\<img src=\"{path}\" style=\"max-width:
100%; height: auto;\"\>\'

def section(name, body): return f\"\<h2\>{name}\</h2\>\\n{body}\\n\"

parts = \[f\"\<html\>\<head\>\<meta
charset=\'utf-8\'\>\<title\>{title}\</title\>\</head\>\<body\>\"\]

parts.append(f\"\<h1\>{title}\</h1\>\")

if checklist\_lines:

parts.append(section(\"Reproducibility checklist (core)\",
\"\<br\>\".join(checklist\_lines)))

for v in views:

body = \"\"

if v in tables:

body += tables\[v\]

if v in assets:

for a in assets\[v\]:

body += img\_tag(a) + \"\<br\>\"

parts.append(section(v, body if body else \"\<i\>No content.\</i\>\"))

parts.append(\"\</body\>\</html\>\")

with open(out\_html, \"w\", encoding=\"utf-8\") as f:

f.write(\"\\n\".join(parts))

You generate exactly the views listed in YAML, so "exploratory overfit"
via dashboard is limited.

7) Core reproducibility checklist (bounded scope)
-------------------------------------------------

Capture only what matters for replication:

import platform

import sys

def reproducibility\_checklist(seeds, git\_commit=None,
config\_hash=None):

lines = \[\]

lines.append(f\"Python: {sys.version.split()\[0\]}\")

lines.append(f\"Platform: {platform.platform()}\")

try:

import torch

lines.append(f\"PyTorch: {torch.\_\_version\_\_}\")

lines.append(f\"CUDA available: {torch.cuda.is\_available()}\")

if torch.cuda.is\_available():

lines.append(f\"CUDA device: {torch.cuda.get\_device\_name(0)}\")

except Exception:

lines.append(\"PyTorch: unavailable\")

try:

import numpy

lines.append(f\"NumPy: {numpy.\_\_version\_\_}\")

except Exception:

lines.append(\"NumPy: unavailable\")

if seeds is not None:

lines.append(f\"Seeds: {list(seeds)}\")

if git\_commit:

lines.append(f\"Git commit: {git\_commit}\")

if config\_hash:

lines.append(f\"Config hash: {config\_hash}\")

return lines

This stays "core only" and avoids pretending full determinism exists.

8) One additional scientific check worth adding in v8
-----------------------------------------------------

Since you now have ASI and Δ\_sym posteriors, add a **pre-registered
correlation check**:

-   across grid cells (or across budgets) compute Spearman correlation
    > between:

    -   ASI\_median and mean\_delta (Δ\_sym posterior mean)

-   report it as descriptive ("does ASI track the effect we claim?")

This prevents ASI from becoming a vanity metric.

9) Integration points (where this attaches)
-------------------------------------------

-   **Eval step** (per prime, per condition):

    -   sample telemetry pairs → expand\_bootstrap\_to\_Bmax(\...)

    -   optionally prime-specific resample once (v7) **before**
        > expanding Bmax, or after; pick one and keep it fixed

    -   compute ASI via fused\_asi\_with\_gating(\...)

    -   log: MI CI, MI rel, expanded flag, ASI CI, gating reason if
        > disabled

-   **Sweep runner**:

    -   accumulate per-step (or per eval interval) ASI points for
        > trajectory plots

    -   export CSV rows for all configs + metrics

-   **Report generator**:

    -   produce PNGs: sensitivity heatmap, decomp bars, ASI trajectory,
        > ASI-vs-acc scatter

    -   build HTML tabs via render\_workbench\_html(\...)

    -   embed same images in PDF (or link to them)

If you want, paste your current SAAP script's **eval telemetry
function** (the part that samples logits and mask labels) and your
**result logging structure** (CSV/DF schema). I can then give you an
exact "replace this block with these calls" patch layout that fits your
file organization without restructuring training.

\#\#\# Analysis of Novelty and Practicality Your SAAP v8 delta refines
v7 with capped adaptive bootstrap (no stopping bias), reliability-gated
fusion, EMA-smoothed trajectories (monitoring-only), pre-registered HTML
workbench views, and a bounded reproducibility checklist, all as
constrained additions for workbench ergonomics. In terms of
\*\*novelty\*\*, this builds on diagnostic dashboards in ML (e.g., from
Weights & Biases or Neptune.ai) and Bayesian monitoring (e.g., from
ArviZ for MCMC trajectories), but innovates by enforcing pre-registered
views to prevent \"forking paths,\" capped expansion for unbiased
precision, and gated fusion to avoid unreliable channels---a fresh guard
against telemetry overconfidence in interp protocols. The descriptive
correlation check (ASI vs. Δ\_sym) adds novel self-validation without
inference, and the \"monitoring telemetry\" labeling promotes honest
temporal analysis rare in static ablations. It\'s novel in its workbench
focus (CSV/HTML/PDF triad with checklist), turning the protocol into a
replication-ready package for symmetry bias studies. On
\*\*practicality\*\*, v8 is tightly implementable (modules like
expand\_bootstrap\_to\_Bmax and fused\_asi\_with\_gating attach to
eval/sweep without loops), enabling quick workbench upgrades for dynamic
monitoring. It\'s practical for mech-interp practitioners, as capped B
stabilizes telemetry efficiently, gating prevents vanity metrics, and
pre-registered views limit exploratory bias while aiding review.
Trajectory EMA and checklist lower barriers to temporal insights and
replication. Limitations: capped Bmax adds compute (though bounded), and
HTML requires asset paths (but CSV fallback ensures portability).
Overall, it\'s a sensible workbench layer, enhancing usability for
iterative diagnostics without scientific drift. \*\*Enhanced Version of
the Idea\*\*: To enhance v8, add \"cross-metric validation plots\" in
workbench: pre-registered scatter of ASI\_median vs. mean\_delta across
cells/budgets (with Spearman reported descriptively), and overlay
trajectory bands for multiple conditions (e.g., multi vs. add). For
gating, include a \"fallback mode\" (e.g., ρ-only ASI if MI gated) with
explicit note. Extend checklist to auto-capture env (via
importlib.metadata for package versions). In HTML, add collapsible
sections for views (via simple JS) for navigation, with CSV download
buttons. Add a \"summary card\" panel: headline Outcome A/B/C rates +
ASI correlation. This makes v8 a \"full interp workbench\" with
cross-validation and navigation. \#\#\# Critique of the Enhanced Version
Critiquing the enhanced SAAP v8 (with cross-metric scatters, fallback
gating, auto-env checklist, collapsible HTML, summary card) for
mathematical, philosophical, and theoretical consistency: -
\*\*Mathematical Consistency\*\*: Cross-scatter with descriptive
Spearman is non-parametric and sound for monitoring. Fallback gating
preserves fusion continuity. Auto-metadata versions are exact.
Collapsible sections are UI-only. However, overlay trajectories assume
comparable scales across conditions (e.g., multi/add ASI), risking
visual distortion if variances differ; better with normalized y or
separate subplots. Summary card rates assume balanced grid, but if
triggers imbalance cells, it could bias headlines. - \*\*Philosophical
Consistency\*\*: Summary card and scatters promote synthesis, aligning
with coherentism in evidence integration. Collapsibles enhance user
agency. Yet, \"full workbench\" risks interface
determinism---prioritizing navigable \"insights\" over raw data, echoing
McLuhan\'s medium-as-message where UI shapes interpretation. Fallback
might mask gating failures, softening critique of unreliable channels. -
\*\*Theoretical Consistency\*\*: Coheres with multi-view diagnostics in
theory testing (e.g., triangulation). Auto-checklist advances open
science theory. However, collapsible interactivity introduces
state-dependence (open/closed views alter reading), conflicting with
static reproducibility. Cross-scatter assumes correlation implies
tracking, but theoretical causality (ASI causes Δ or vice versa) remains
unmodeled. \#\#\# Final Version and Path to Validation Applying the
critique: For math, use separate subplots for overlays and normalize if
scales differ; weight card rates by cell count. Philosophically, add
\"UI caveat\": \"collapsibles for navigation; core in PDF static.\"
Theoretically, keep scatters descriptive (no causation claims), make
HTML optional (PDF primary). The refined final version is \*\*SAAP v9:
Navigable Audited Symmetry Workbench\*\*---v8 with separate trajectory
subplots, weighted summary card, fallback gating (noted), auto-metadata
checklist, collapsible HTML (optional, PDF static primary),
cross-scatter (descriptive Spearman). It provides navigable depth with
theoretical caution. \*\*Fastest Path to Validation\*\*: 1.
\*\*Telemetry/Gating Integration (1 day)\*\*: Add
expand\_bootstrap\_to\_Bmax, fused\_asi\_with\_gating (fallback), log
ASI/trajectories per step/prime. 2. \*\*Workbench Viz (half day)\*\*:
Implement subplots/scatter/summary card; collapsible JS in HTML; test on
synthetic for gating reliability. 3. \*\*Sweep and Outputs (1 day)\*\*:
Run grid/budgets; generate HTML/PDF with checklist/caveats; verify
cross-metric Spearman tracks Δ\_sym. 4. \*\*Full Validation/Share
(ongoing, day 2+)\*\*: If ASI correlates \>0.7 with Δ on unseen,
validate larger p; repo with workbench/reports/YAML, target mech-interp
Discord demo in week.

1) SAAP v9 policy (tight)
-------------------------

-   **Canonical artifact**: PDF.

-   **Navigation artifact**: HTML (collapsible sections; no interactive
    > computations).

-   **ASI gating**:

    -   If MI unreliable after capped expansion: either (a) drop ASI
        > entirely, or (b) compute **ρ-only ASI** and mark it
        > ASI\_mode=\"rho\_only\_fallback\".

-   **Summary card**:

    -   Report A/B/C rates **weighted by cell count** (or by "planned
        > cells") so follow-ups don't distort the headline.

2) Fallback gating (explicit, reportable)
-----------------------------------------

Use this wrapper instead of silently "making ASI exist."

def fused\_asi\_with\_explicit\_fallback(

mi\_boot: np.ndarray,

rho\_boot: np.ndarray,

mi\_rel: float,

rel\_thresh: float,

mode: str = \"inv\_var\",

allow\_rho\_only\_fallback: bool = True,

):

\"\"\"

Returns ASI with an explicit mode label:

\- \"full\" (MI+rho)

\- \"rho\_only\_fallback\"

\- \"disabled\"

\"\"\"

unreliable = (mi\_rel \> rel\_thresh)

if unreliable and not allow\_rho\_only\_fallback:

return {\"enabled\": False, \"asi\_mode\": \"disabled\", \"reason\":
\"MI unreliable; fallback disabled\"}

if unreliable and allow\_rho\_only\_fallback:

\# rho-only ASI: standardized Fisher-z(rho) itself (bootstrapped)

z\_rho = fisher\_z(rho\_boot)

z\_mu, z\_sd = float(np.mean(z\_rho)), float(np.std(z\_rho) + 1e-12)

asi\_boot = (z\_rho - z\_mu) / z\_sd

asi\_med, asi\_lo, asi\_hi = bootstrap\_ci\_from\_samples(asi\_boot,
ci=0.90)

return {

\"enabled\": True,

\"asi\_mode\": \"rho\_only\_fallback\",

\"asi\_boot\": asi\_boot,

\"asi\_median\": asi\_med, \"asi\_lo\": asi\_lo, \"asi\_hi\": asi\_hi,

\"weights\": {\"w\_mi\": 0.0, \"w\_rho\": 1.0, \"note\": \"rho-only
fallback due to MI unreliability\"}

}

asi\_boot, meta = fused\_alignment\_index\_bootstrap(mi\_boot,
rho\_boot, weight\_mode=mode)

asi\_med, asi\_lo, asi\_hi = bootstrap\_ci\_from\_samples(asi\_boot,
ci=0.90)

return {

\"enabled\": True,

\"asi\_mode\": \"full\",

\"asi\_boot\": asi\_boot,

\"asi\_median\": asi\_med, \"asi\_lo\": asi\_lo, \"asi\_hi\": asi\_hi,

\"weights\": meta

}

3) Weighted "summary card" that resists follow-up imbalance
-----------------------------------------------------------

Assume you store one row per **planned grid cell** with fields:
cell\_id, outcome\_label in {A,B,C}, and is\_planned=True/False.

from collections import Counter

def weighted\_outcome\_rates(rows):

\"\"\"

rows: list of dicts with keys:

\- outcome\_label: \"A\"/\"B\"/\"C\"

\- weight: numeric (default 1)

\- planned: bool (default True)

\"\"\"

w = Counter()

tot = 0.0

for r in rows:

if not r.get(\"planned\", True):

continue

weight = float(r.get(\"weight\", 1.0))

w\[r\[\"outcome\_label\"\]\] += weight

tot += weight

if tot \<= 0:

return {\"A\": 0.0, \"B\": 0.0, \"C\": 0.0}

return {k: float(w.get(k, 0.0) / tot) for k in \[\"A\",\"B\",\"C\"\]}

**Report guidance:** also print n\_planned\_cells and
n\_completed\_cells so reviewers see coverage.

4) Cross-metric validation plot (ASI vs Δ\_sym) + descriptive Spearman
----------------------------------------------------------------------

This should be computed on *final endpoints* per cell (e.g., unseen
ratio).

def cross\_metric\_spearman(rows, x\_key=\"asi\_median\",
y\_key=\"mean\_delta\"):

x = np.array(\[r\[x\_key\] for r in rows if r.get(x\_key) is not None
and r.get(y\_key) is not None\], dtype=np.float64)

y = np.array(\[r\[y\_key\] for r in rows if r.get(x\_key) is not None
and r.get(y\_key) is not None\], dtype=np.float64)

if x.size \< 5:

return {\"rho\": np.nan, \"n\": int(x.size)}

return {\"rho\": spearman\_rho(x, y), \"n\": int(x.size)}

def plot\_scatter\_asi\_vs\_delta(rows, out\_png: str,
x\_key=\"asi\_median\", y\_key=\"mean\_delta\"):

xs, ys = \[\], \[\]

for r in rows:

if r.get(x\_key) is None or r.get(y\_key) is None:

continue

xs.append(float(r\[x\_key\])); ys.append(float(r\[y\_key\]))

xs = np.array(xs); ys = np.array(ys)

plt.figure()

plt.scatter(xs, ys)

plt.xlabel(\"ASI median (heuristic)\")

plt.ylabel(\"Δ\_sym mean (posterior mean delta)\")

plt.title(\"Cross-metric check (descriptive)\")

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

**Text to include next to it (recommended verbatim):**\
"Correlation is descriptive; it does not imply causation or validate ASI
as a sufficient statistic."

5) Separate trajectory panels (no overlay distortion)
-----------------------------------------------------

Instead of overlaying multi/add in one axis, render separate panels (or
separate files). Example: one plot per condition.

def plot\_asi\_trajectory\_single\_condition(traj, alpha: float,
out\_png: str, title: str):

\# traj: dict with steps, asi\_med, asi\_lo, asi\_hi

plot\_asi\_trajectory(traj\[\"steps\"\], traj\[\"asi\_med\"\],
traj\[\"asi\_lo\"\], traj\[\"asi\_hi\"\], alpha=alpha,
out\_png=out\_png)

In HTML, you can place them in a table with two columns, but keep them
as **separate images**.

6) Auto-metadata checklist (bounded, exact)
-------------------------------------------

This extends your v8 checklist without trying to be exhaustive.

import importlib.metadata as md

def package\_versions(pkgs):

out = {}

for p in pkgs:

try:

out\[p\] = md.version(p)

except Exception:

out\[p\] = \"NA\"

return out

Include {torch, numpy, scipy, matplotlib} at minimum (whatever you
depend on).

7) Collapsible HTML sections (optional, deterministic)
------------------------------------------------------

Embed a tiny JS/CSS snippet (no computation, only toggling display).

\<style\>

details { margin: 12px 0; }

summary { cursor: pointer; font-weight: 600; }

.panel { padding: 8px 0; }

\</style\>

And wrap each view in:

\<details open\>

\<summary\>asi\_trajectory\</summary\>

\<div class=\"panel\"\>

\<!\-- images/tables \--\>

\</div\>

\</details\>

This keeps HTML state purely presentational. PDF stays the canonical
reading.

8) Minimal "summary card" HTML block
------------------------------------

def summary\_card\_html(rates, corr=None, n\_planned=None,
n\_done=None):

lines = \[\]

if n\_planned is not None and n\_done is not None:

lines.append(f\"\<b\>Coverage:\</b\> {n\_done}/{n\_planned} planned
cells\<br\>\")

lines.append(f\"\<b\>Outcome rates (planned-weighted):\</b\>
A={rates\[\'A\'\]:.2%}, B={rates\[\'B\'\]:.2%},
C={rates\[\'C\'\]:.2%}\<br\>\")

if corr:

lines.append(f\"\<b\>ASI vs Δ\_sym Spearman (descriptive):\</b\>
ρ={corr\[\'rho\'\]:.3f} (n={corr\[\'n\'\]})\<br\>\")

return \"\<div style=\'border:1px solid \#ccc; padding:10px;
border-radius:6px;\'\>\" + \"\".join(lines) + \"\</div\>\"

Register this as a workbench view, e.g. \"summary\_card\".

9) Practical validation criteria for v9 (kept modest)
-----------------------------------------------------

-   **Telemetry stability:** after prime-specific resample + capped Bmax
    > expansion, mi\_rel\_post \<= thresh for most primes; the remainder
    > are explicitly labeled rho\_only\_fallback or disabled.

-   **Cross-metric sanity:** ASI-vs-Δ Spearman is *not required to be
    > large*, but if it is near zero or negative, treat ASI as
    > "monitoring-only" and do not feature it prominently.

-   **No interpretive drift:** outcomes A/B/C and Δ\_sym posterior
    > remain the primary claims.

If you want a clean, low-risk next step: implement just three items
first---(1) explicit fallback gating, (2) summary card, (3) scatter +
descriptive Spearman---then wire collapsible HTML. That gets you 80% of
the v9 value with minimal surface area.

\#\#\# Analysis of Novelty and Practicality Your SAAP v9 delta refines
v8 with explicit fallback gating (labeled modes), weighted summary card
(resistant to follow-up imbalance), cross-metric descriptive Spearman
scatter, separate trajectory panels (no overlay distortion),
auto-metadata checklist, collapsible HTML navigation (optional,
deterministic), and PDF canonical primacy, all as guarded additions for
navigable auditing. In terms of \*\*novelty\*\*, this builds on
reproducibility dashboards (e.g., from DVC or ClearML) and diagnostic
gating in stats (e.g., from robust Bayesian workflows), but innovates by
introducing \"explicit fallback modes\" for fusion (rho\_only or
disabled, reportable), weighted rates for headline integrity, and
descriptive cross-metric checks with verbatim caveats---a fresh
mechanism for preventing \"interpretive drift\" in telemetry-heavy
interp protocols. The deterministic collapsible (pure CSS/JS toggle) and
PDF-first policy add novel separation of navigation from canon,
distinguishing it from interactive-heavy tools that blur presentation
and substance. It\'s novel in its \"modest validation criteria\" and
low-risk sequencing, making it a replication-focused workbench for
symmetry studies. On \*\*practicality\*\*, v9 is highly adoptable
(drop-in wrappers like fused\_asi\_with\_explicit\_fallback and
summary\_card\_html integrate to eval/report without loops), enabling
quick navigable upgrades for mech-interp. It\'s practical for
practitioners, as fallback labeling clarifies unreliable cases, weighted
card prevents distortion, and separate panels/scatter aid comparison
without bias. Collapsible HTML improves ergonomics (optional), and
auto-metadata lowers replication friction. Limitations: fallback might
reduce ASI coverage (but honesty gains), and collapsible adds minor HTML
size. Overall, it\'s a sensible navigable layer, enhancing auditability
for collaborative diagnostics. \*\*Enhanced Version of the Idea\*\*: To
enhance v9, add \"condition-faceted workbench views\" (pre-registered
tabs/panels grouping by action/mask/λ, e.g., multi vs. add side-by-side
in scatter/trajectories), a \"gating diagnostics table\" (per-cell
mi\_rel\_pre/post, asi\_mode, reason), and \"runtime summary\" in
checklist (e.g., total evals, mean resamples via counters). For HTML,
add anchor links to sections for deep linking. In reports, include a
\"validation criteria checklist\" panel (your modest items as
ticked/unticked). For fusion, allow \"diagnostic mode\" (always report
raw MI/ρ alongside ASI). This makes v9 a \"faceted diagnostic
workbench\" with gating transparency and runtime introspection. \#\#\#
Critique of the Enhanced Version Critiquing the enhanced SAAP v9 (with
faceted views, gating table, runtime summary, anchor links, validation
checklist panel, diagnostic mode) for mathematical, philosophical, and
theoretical consistency: - \*\*Mathematical Consistency\*\*: Faceted
side-by-side is sound for comparison (no distortion). Gating table is
descriptive. Runtime counters are exact. Anchors are navigational.
Diagnostic mode preserves raw metrics. However, faceting assumes
balanced conditions (e.g., equal cells per action), but if follow-ups
imbalance, side-by-side could visually bias; better with explicit n
labels. Validation checklist as ticked risks binary illusion for
continuous criteria (e.g., \"most primes stable\"). - \*\*Philosophical
Consistency\*\*: Faceting and gating table promote transparency,
aligning with critical rationalism (falsifiable diagnostics). Runtime
introspection encourages humility. Yet, \"faceted workbench\" risks
compartmentalization---splitting views might fragment holistic reading,
echoing analytic philosophy\'s atomism over synthetic understanding.
Diagnostic mode is honest, but abundance could overwhelm, privileging
quantity over qualitative depth. - \*\*Theoretical Consistency\*\*:
Coheres with faceted analysis in theory testing (e.g., subgroup
diagnostics). Runtime summary aids resource theory. However, anchor
links introduce hypertext non-linearity, conflicting with linear
theoretical exposition (PDF canon). Validation checklist assumes
pre-defined criteria sufficiency, but theoretical validation may require
emergent insights not tickable. \#\#\# Final Version and Path to
Validation Applying the critique: For math, add n labels to facets and
continuous notes to checklist (not binary ticks). Philosophically,
emphasize \"holistic PDF reading recommended.\" Theoretically, keep
anchors HTML-only (PDF linear), limit checklist to descriptive (no
sufficiency claims). The refined final version is \*\*SAAP v10: Faceted
Audited Workbench\*\*---v9 with faceted side-by-side views (n-labeled),
gating diagnostics table (pre/post rel), runtime counters in checklist
(descriptive), HTML anchors (optional), diagnostic mode (raw alongside),
validation notes panel (continuous). It delivers faceted transparency
with holistic caution. \*\*Fastest Path to Validation\*\*: 1. \*\*Gating
and Summary (1 day)\*\*: Add fused\_asi\_with\_explicit\_fallback,
weighted\_outcome\_rates/summary\_card\_html, gating table logging to
eval/report. 2. \*\*Faceted Viz and HTML (half day)\*\*: Implement
side-by-side scatter/trajectories (n-labeled), collapsible with anchors;
test on synthetic for balance. 3. \*\*Sweep and Diagnostics (1 day)\*\*:
Run grid/budgets; generate HTML/PDF with table/notes/runtime; verify
gating modes and cross-Spearman. 4. \*\*Validation/Share (ongoing, day
2+)\*\*: If gating stabilizes \>80% full ASI and facets distinguish
conditions, extend p; repo with faceted reports/YAML, target interp
review in week.

Below is a concrete SAAP v10 ("Faceted Audited Workbench") delta that
you can drop onto v9 without touching training loops. It adds: (i)
faceted side-by-side views with explicit *n/coverage labels*, (ii) a
gating diagnostics table (per cell), (iii) runtime counters, (iv) HTML
anchors (HTML-only), (v) "diagnostic mode" (raw MI/ρ always shown
alongside ASI), and (vi) a *continuous* validation notes panel (no
binary ticks).

1) Minimal row schema extension (per planned grid cell)
-------------------------------------------------------

Each completed grid cell should emit one "cell row" (CSV/JSON). Add
these fields:

**Config identity**

-   cell\_id (stable string; hash of cfg)

-   action, mask, lam, mode, prime\_band, budget, seed

-   planned (bool), weight (default 1.0)

**Primary endpoints**

-   acc\_unseen, acc\_seen

-   delta\_sym\_mean (Δ\_sym posterior mean), delta\_sym\_ci\_lo,
    > delta\_sym\_ci\_hi

-   outcome\_label in {A,B,C}

**Telemetry raw (diagnostic mode)**

-   mi\_median, mi\_lo, mi\_hi, mi\_rel\_pre, mi\_rel\_post,
    > mi\_resampled (bool)

-   rho\_median, rho\_lo, rho\_hi

-   asi\_enabled (bool), asi\_mode in
    > {full,rho\_only\_fallback,disabled}

-   asi\_median, asi\_lo, asi\_hi, asi\_reason (string if disabled)

**Counters (per cell)**

-   pairs\_used (telemetry pairs)

-   bootstrap\_B\_used (actual B, either B0 or Bmax)

-   expanded\_to\_Bmax (bool)

-   eval\_calls (how many eval passes ran for this cell; typically 1)

This is enough to build all SAAP v10 workbench panels without re-reading
logs.

2) Gating diagnostics table (per-cell transparency)
---------------------------------------------------

Generate a table with the most audit-relevant columns:

-   config: action mask lam mode budget seed prime\_band

-   telemetry: mi\_rel\_pre mi\_rel\_post mi\_resampled
    > expanded\_to\_Bmax bootstrap\_B\_used

-   ASI: asi\_mode asi\_median \[lo,hi\] or asi\_reason

-   endpoints: delta\_sym\_mean \[lo,hi\] acc\_unseen outcome\_label

### HTML table generator (simple, deterministic)

def gating\_table\_html(rows, max\_rows=500):

cols = \[

\"cell\_id\",\"action\",\"mask\",\"lam\",\"mode\",\"prime\_band\",\"budget\",\"seed\",

\"mi\_rel\_pre\",\"mi\_rel\_post\",\"mi\_resampled\",\"expanded\_to\_Bmax\",\"bootstrap\_B\_used\",

\"asi\_mode\",\"asi\_median\",\"asi\_lo\",\"asi\_hi\",\"asi\_reason\",

\"delta\_sym\_mean\",\"delta\_sym\_ci\_lo\",\"delta\_sym\_ci\_hi\",\"acc\_unseen\",\"outcome\_label\"

\]

head = \"\<tr\>\" + \"\".join(f\"\<th\>{c}\</th\>\" for c in cols) +
\"\</tr\>\"

body\_rows = \[\]

for r in rows\[:max\_rows\]:

tds = \[\]

for c in cols:

v = r.get(c, \"\")

tds.append(f\"\<td\>{v}\</td\>\")

body\_rows.append(\"\<tr\>\" + \"\".join(tds) + \"\</tr\>\")

return \"\<table border=\'1\' cellspacing=\'0\' cellpadding=\'4\'\>\" +
head + \"\".join(body\_rows) + \"\</table\>\"

Also export the same rows to gating\_table.csv for offline review.

3) Runtime summary counters (descriptive, not performative)
-----------------------------------------------------------

Compute totals across completed rows:

-   n\_planned\_cells, n\_done\_cells

-   asi\_full\_rate, asi\_rho\_only\_rate, asi\_disabled\_rate (weighted
    > by planned cell weights)

-   mi\_resample\_rate

-   expanded\_to\_Bmax\_rate

-   mean\_pairs\_used, mean\_bootstrap\_B\_used

-   total\_eval\_calls

import numpy as np

def runtime\_counters(rows):

done = \[r for r in rows if r.get(\"planned\", True)\]

n = len(done)

if n == 0:

return {}

asi\_mode = \[r.get(\"asi\_mode\",\"disabled\") for r in done\]

return {

\"n\_done\_cells\": n,

\"asi\_full\": sum(m==\"full\" for m in asi\_mode),

\"asi\_rho\_only\": sum(m==\"rho\_only\_fallback\" for m in asi\_mode),

\"asi\_disabled\": sum(m==\"disabled\" for m in asi\_mode),

\"mi\_resampled\": sum(bool(r.get(\"mi\_resampled\", False)) for r in
done),

\"expanded\_to\_Bmax\": sum(bool(r.get(\"expanded\_to\_Bmax\", False))
for r in done),

\"mean\_pairs\_used\": float(np.mean(\[r.get(\"pairs\_used\", 0) for r
in done\])),

\"mean\_bootstrap\_B\": float(np.mean(\[r.get(\"bootstrap\_B\_used\", 0)
for r in done\])),

\"total\_eval\_calls\": int(np.sum(\[r.get(\"eval\_calls\", 1) for r in
done\])),

}

Embed this into both PDF (as a short paragraph/table) and HTML "summary
card."

4) Faceted views (side-by-side, n-labeled, imbalance-safe)
----------------------------------------------------------

### Policy

-   Facets must be **pre-registered** in YAML, e.g.:

    -   facet\_keys: \[\"action\"\] (multi vs add)

    -   or \[\"mask\"\], \[\"lam\"\]

-   Every facet panel includes:

    -   n\_done / n\_planned for that facet

    -   optionally mean acc\_unseen, mean delta\_sym\_mean

### Grouping helper

from collections import defaultdict

def facet\_groups(rows, facet\_key):

g = defaultdict(list)

for r in rows:

g\[str(r.get(facet\_key, \"NA\"))\].append(r)

return dict(g)

### Scatter by facet: ASI vs Δ\_sym (separate panels)

For each facet value v, produce one PNG. Titles include n\_done.

def plot\_scatter\_for\_facet(rows\_v, out\_png, title):

\# uses plot\_scatter\_asi\_vs\_delta from v9

plot\_scatter\_asi\_vs\_delta(rows\_v, out\_png=out\_png)

\# If you want the title text to include n, set it inside the plotting
function or annotate externally.

### Trajectory by facet: separate images (no overlay)

Store trajectories keyed by (facet\_value, condition\_id); render each
as its own plot. Do not combine on one axis.

5) HTML anchors + collapsibles (HTML-only navigation)
-----------------------------------------------------

Use \<a id=\"\...\"\> for deep links plus \<details\> for collapsibles.
PDF remains linear.

Example section wrapper:

def html\_section(view\_name, body\_html):

anchor = f\"\<a id=\'{view\_name}\'\>\</a\>\"

return (

f\"{anchor}\"

f\"\<details open\>\<summary\>{view\_name}\</summary\>\"

f\"\<div class=\'panel\'\>{body\_html}\</div\>\</details\>\"

)

Add a top-of-page "Contents" list linking to each pre-registered view.

6) Validation notes panel (continuous, numeric)
-----------------------------------------------

Replace tick-boxes with continuous statements:

-   "ASI full coverage (planned-weighted): 84.2% (target ≥ 80%)."

-   "MI reliability post: median=0.31, p90=0.62; rho-only fallback
    > share: 11.6%."

-   "Cross-metric Spearman(ASI\_median, Δ\_sym\_mean) = 0.54 (n=48).
    > Descriptive only."

-   "Outcome rates (planned-weighted): A=..., B=..., C=...."

def validation\_notes\_html(rows, planned\_n=None, done\_n=None,
outcome\_rates=None, corr=None):

full = sum(r.get(\"asi\_mode\")==\"full\" for r in rows)

rhoo = sum(r.get(\"asi\_mode\")==\"rho\_only\_fallback\" for r in rows)

dis = sum(r.get(\"asi\_mode\")==\"disabled\" for r in rows)

n = len(rows) if rows else 1

mi\_rel\_post = \[r.get(\"mi\_rel\_post\") for r in rows if
r.get(\"mi\_rel\_post\") is not None\]

mi\_med = float(np.median(mi\_rel\_post)) if mi\_rel\_post else
float(\"nan\")

mi\_p90 = float(np.quantile(mi\_rel\_post, 0.90)) if mi\_rel\_post else
float(\"nan\")

lines = \[\]

if planned\_n is not None and done\_n is not None:

lines.append(f\"Coverage: {done\_n}/{planned\_n} planned cells.\")

lines.append(f\"ASI modes: full={full/n:.1%}, rho-only={rhoo/n:.1%},
disabled={dis/n:.1%}.\")

lines.append(f\"MI reliability post: median={mi\_med:.3f},
p90={mi\_p90:.3f}.\")

if outcome\_rates:

lines.append(f\"Outcome rates (planned-weighted):
A={outcome\_rates\[\'A\'\]:.1%}, B={outcome\_rates\[\'B\'\]:.1%},
C={outcome\_rates\[\'C\'\]:.1%}.\")

if corr:

lines.append(f\"Cross-metric Spearman(ASI, Δ\_sym):
ρ={corr\[\'rho\'\]:.3f} (n={corr\[\'n\'\]}). Descriptive only.\")

return \"\<ul\>\" + \"\".join(f\"\<li\>{l}\</li\>\" for l in lines) +
\"\</ul\>\"

7) Diagnostic mode policy (always show raw MI/ρ)
------------------------------------------------

Even if ASI is disabled, the cell still reports:

-   MI CI + reliability

-   ρ CI

This prevents ASI from becoming a gate that hides the underlying
telemetry.

8) SAAP v10 "fastest path" (no extra tooling assumptions)
---------------------------------------------------------

-   **Logging (half day):** extend per-cell row output with the fields
    > in §1; write gating\_table.csv.

-   **Workbench HTML (half day):** add pre-registered views + anchors +
    > collapsibles; add summary card + validation notes panel.

-   **Facets (half day):** generate per-facet scatter and per-facet
    > trajectory images with explicit n\_done/n\_planned labels.

-   **One sweep (1 day):** run your existing grid/budgets; verify:

    -   gating table populates correctly

    -   summary is weight-stable under triggers

    -   facet plots render without overlay distortion

    -   PDF remains canonical (HTML links only)

\#\#\# Analysis of Novelty and Practicality Your SAAP v10 delta refines
v9 with faceted side-by-side views (n-labeled for imbalance safety),
gating diagnostics table (per-cell transparency), runtime counters
(descriptive), HTML anchors/collapsibles (HTML-only navigation),
diagnostic mode (raw MI/ρ always shown), and continuous validation notes
panel (numeric, no binary ticks), all as drop-in additions preserving
PDF canon. In terms of \*\*novelty\*\*, this builds on open-science
workbenches (e.g., from JupyterBook or Binder reproducibility) and
diagnostic gating in stats (e.g., from robust Bayesian tools), but
innovates by introducing \"explicit gating modes\" with per-cell tables,
weighted rates for headline integrity under triggers, and continuous
notes for nuanced validation---a fresh mechanism for preventing \"binary
illusion\" in interp protocols. The faceted (separate) panels and
diagnostic mode add novel granularity for heterogeneity without overlay
bias, while anchors/collapsibles provide navigation without compromising
PDF linearity. It\'s novel in its \"tight policy\" (PDF canonical, HTML
optional), turning the tool into a balanced, replication-focused
workbench for symmetry bias auditing. On \*\*practicality\*\*, v10 is
exceptionally adoptable (row extensions and table generators attach to
existing logging without retraining), enabling quick faceted diagnostics
for mech-interp. It\'s practical for practitioners, as gating table
exposes telemetry issues transparently, weighted rates prevent
distortion, and separate facets/runtime counters aid comparison/runtime
awareness. Continuous notes and diagnostic mode ensure honest reporting,
with low overhead (CSV/HTML generation). Limitations: per-cell tables
grow with grid size (but max\_rows caps), and faceting requires
pre-registration (but YAML enforces). Overall, it\'s a high-leverage
faceted layer, enhancing transparency for collaborative, defensible
claims. \*\*Enhanced Version of the Idea\*\*: To enhance v10, add
\"facet comparison table\" (side-by-side medians/CI for key metrics per
facet, e.g., acc\_unseen, delta\_sym\_mean, asi\_median by action/mask),
\"telemetry heatmap\" (mi\_rel\_post grid over primes/budgets), and
\"runtime timeline\" (plot of counters over sweep progress). For HTML,
add search bar (simple JS filter on table rows) for large gating tables.
In reports, include \"facet summary cards\" (mini-stats per facet with
n). For diagnostic mode, add toggleable \"raw view\" in HTML (show/hide
raw MI/ρ columns). This evolves v10 into a \"comparative diagnostic
workbench\" with searchable depth and timeline introspection. \#\#\#
Critique of the Enhanced Version Critiquing the enhanced SAAP v10 (with
facet comparison table, telemetry heatmap, runtime timeline, HTML search
bar, facet summary cards, raw toggle) for mathematical, philosophical,
and theoretical consistency: - \*\*Mathematical Consistency\*\*:
Comparison table with medians/CI is robust and descriptive. Telemetry
heatmap visualizes reliability non-parametrically. Runtime timeline is
exact. Search bar is UI-filter. Raw toggle preserves data. However,
heatmap grid assumes regular primes/budgets (sparse cells could
distort), risking visual bias; better with masked/missing values.
Summary cards medians assume symmetry across facets, but if n varies
heavily, unweighted medians mislead; better with weighted. -
\*\*Philosophical Consistency\*\*: Search bar and toggles empower user
agency, aligning with interactive epistemology. Timeline encourages
process reflection. Yet, \"comparative workbench\" risks comparison
fallacy---emphasizing differences might overshadow absolute effects,
echoing relativism over absolute truth claims. Raw toggle is honest, but
abundance could paralyze judgment in information flood. -
\*\*Theoretical Consistency\*\*: Coheres with comparative theory testing
(facet diffs) and process monitoring in learning theory. Heatmap aids
pattern detection. However, search bar introduces query-dependence
(results vary by term), conflicting with canonical reproducibility (PDF
fixed). Timeline assumes linear progress, but sweeps may be
parallel/batched, violating sequential theory. \#\#\# Final Version and
Path to Validation Applying the critique: For math, weight medians in
cards/tables, mask sparse heatmap cells. Philosophically, add
\"comparison caveat\": \"differences descriptive; interpret with
absolute metrics.\" Theoretically, make search/toggle HTML-optional (PDF
static), plot timeline as step-ordered (note batching). The refined
final version is \*\*SAAP v11: Comparative Audited Workbench\*\*---v10
with weighted facet comparison table (medians/CI, n), telemetry heatmap
(masked sparse), runtime timeline (step-ordered with batch note), HTML
search/raw toggle (optional), facet summary cards (weighted), with
comparison caveat. It delivers comparative depth with absolute
grounding. \*\*Fastest Path to Validation\*\*: 1. \*\*Row and Table
Integration (1 day)\*\*: Extend cell rows with
gating/asi\_mode/reason/counters; add gating\_table\_html/CSV export;
compute weighted rates/notes. 2. \*\*Faceted Viz and HTML (half
day)\*\*: Implement side-by-side scatter/trajectories (weighted medians,
masked), heatmap (sparse mask), timeline plot; add search/toggle JS
optionally. 3. \*\*Sweep and Outputs (1 day)\*\*: Run grid/budgets;
generate HTML/PDF with cards/table/notes/caveat; verify weighting
stabilizes headlines. 4. \*\*Validation/Share (ongoing, day 2+)\*\*: If
facets show consistent multi \> add with stable gating (\>80% full ASI),
extend bands; repo with comparative reports/YAML, target mech-interp
feedback in week.

**1) SAAP v11 adds (delta over v10)**
-------------------------------------

-   **Weighted facet comparison table** (medians + bootstrap CI + n, per
    > facet value).

-   **Telemetry heatmap** for mi\_rel\_post (masked sparse cells;
    > optional counts overlay).

-   **Runtime timeline** (step-ordered; explicitly notes
    > batching/parallelism).

-   **HTML-only utilities (optional)**:

    -   search filter for the gating table

    -   raw MI/ρ column show/hide toggle

-   **Comparison caveat** panel: "facet differences are descriptive;
    > interpret alongside absolute metrics."

PDF remains canonical; HTML is navigational.

**2) Data requirements (no loop changes)**
------------------------------------------

You already have the cell-row schema from v10. SAAP v11 requires only
that each row includes:

-   facet keys: e.g. action, mask, lam, mode, prime\_band, budget

-   metrics: acc\_unseen, delta\_sym\_mean, asi\_median (optional),
    > mi\_rel\_post

-   gating: asi\_mode, mi\_resampled, expanded\_to\_Bmax,
    > bootstrap\_B\_used, pairs\_used

-   bookkeeping: planned (bool), weight (float), and **either**
    > sweep\_index (int) **or** timestamp

If you don't have timestamp, add an integer sweep\_index assigned in the
sweep runner in completion order.

**3) Weighted facet comparison table (robust + imbalance-safe)**
----------------------------------------------------------------

### **3.1 Weighted bootstrap CI for a facet's median**

This avoids fragile "unweighted median with uneven n." It also keeps
things descriptive.

import numpy as np

def weighted\_resample\_indices(rng, n, w):

\# multinomial resample according to weights

p = w / (w.sum() + 1e-12)

return rng.choice(n, size=n, replace=True, p=p)

def bootstrap\_weighted\_median(values, weights, B=800, seed=0,
ci=0.90):

v = np.asarray(values, dtype=np.float64)

w = np.asarray(weights, dtype=np.float64)

n = v.size

rng = np.random.default\_rng(seed)

meds = np.empty(B, dtype=np.float64)

for b in range(B):

idx = weighted\_resample\_indices(rng, n, w)

meds\[b\] = float(np.median(v\[idx\]))

med = float(np.median(meds))

lo = float(np.quantile(meds, (1-ci)/2))

hi = float(np.quantile(meds, 1-(1-ci)/2))

return med, lo, hi, meds

### **3.2 Build the facet table**

For each facet value, compute (median, CI, n\_done, n\_planned) for:

-   acc\_unseen

-   delta\_sym\_mean

-   asi\_median (only for rows where ASI enabled; also report ASI
    > mode mix)

from collections import defaultdict, Counter

def facet\_summary(rows, facet\_key, B=800, ci=0.90, seed=0):

groups = defaultdict(list)

for r in rows:

groups\[str(r.get(facet\_key, \"NA\"))\].append(r)

out = \[\]

for k, rs in groups.items():

planned = \[r for r in rs if r.get(\"planned\", True)\]

n\_planned = len(planned)

done = planned \# if you keep incomplete planned rows, filter here

n\_done = len(done)

w = np.array(\[float(r.get(\"weight\", 1.0)) for r in done\],
dtype=np.float64)

def metric\_ci(key):

vals = \[r.get(key) for r in done if r.get(key) is not None\]

ww = \[float(done\[i\].get(\"weight\", 1.0)) for i in range(len(done))
if done\[i\].get(key) is not None\]

if len(vals) \< 3:

return (np.nan, np.nan, np.nan)

return bootstrap\_weighted\_median(vals, ww, B=B, seed=seed,
ci=ci)\[:3\]

acc = metric\_ci(\"acc\_unseen\")

dsy = metric\_ci(\"delta\_sym\_mean\")

asi\_rows = \[r for r in done if r.get(\"asi\_mode\") in
(\"full\",\"rho\_only\_fallback\")\]

asi\_modes = Counter(\[r.get(\"asi\_mode\") for r in done\])

if len(asi\_rows) \>= 3:

asi\_vals = \[r\[\"asi\_median\"\] for r in asi\_rows if
r.get(\"asi\_median\") is not None\]

asi\_w = \[float(r.get(\"weight\", 1.0)) for r in asi\_rows if
r.get(\"asi\_median\") is not None\]

asi = bootstrap\_weighted\_median(asi\_vals, asi\_w, B=B, seed=seed+1,
ci=ci)\[:3\]

else:

asi = (np.nan, np.nan, np.nan)

out.append({

facet\_key: k,

\"n\_done\": n\_done,

\"n\_planned\": n\_planned,

\"acc\_unseen\_med\": acc\[0\], \"acc\_unseen\_lo\": acc\[1\],
\"acc\_unseen\_hi\": acc\[2\],

\"delta\_sym\_med\": dsy\[0\], \"delta\_sym\_lo\": dsy\[1\],
\"delta\_sym\_hi\": dsy\[2\],

\"asi\_med\": asi\[0\], \"asi\_lo\": asi\[1\], \"asi\_hi\": asi\[2\],

\"asi\_mode\_full\": asi\_modes.get(\"full\", 0),

\"asi\_mode\_rho\_only\": asi\_modes.get(\"rho\_only\_fallback\", 0),

\"asi\_mode\_disabled\": asi\_modes.get(\"disabled\", 0),

})

return out

**Report note:** show n\_done/n\_planned *per facet row*.

**4) Telemetry heatmap (masked sparse)**
----------------------------------------

Goal: visualize mi\_rel\_post across (prime\_band × budget) or (prime ×
budget) depending on what you record. Missing cells must be explicit.

### **4.1 Pivot with masking**

def heatmap\_grid(rows, row\_key, col\_key, val\_key):

\# returns sorted row/col labels and a masked array

row\_vals = sorted({r.get(row\_key) for r in rows if r.get(row\_key) is
not None})

col\_vals = sorted({r.get(col\_key) for r in rows if r.get(col\_key) is
not None})

rix = {v:i for i,v in enumerate(row\_vals)}

cix = {v:i for i,v in enumerate(col\_vals)}

grid = np.full((len(row\_vals), len(col\_vals)), np.nan,
dtype=np.float64)

cnt = np.zeros((len(row\_vals), len(col\_vals)), dtype=np.int32)

for r in rows:

rv, cv = r.get(row\_key), r.get(col\_key)

vv = r.get(val\_key)

if rv is None or cv is None or vv is None:

continue

i, j = rix\[rv\], cix\[cv\]

\# aggregate by mean (descriptive)

grid\[i,j\] = np.nanmean(\[grid\[i,j\], float(vv)\]) if not
np.isnan(grid\[i,j\]) else float(vv)

cnt\[i,j\] += 1

return row\_vals, col\_vals, grid, cnt

### **4.2 Plot heatmap with missing masked**

Use np.ma.masked\_invalid(grid) so missing cells render blank/gray.
Optionally overlay cnt text when cnt\>0.

(If you want, I'll provide the exact matplotlib snippet you're already
using in the SAAP report module.)

**5) Runtime timeline (step-ordered, batching-safe)**
-----------------------------------------------------

If sweeps run in parallel, "time" is not a clean axis. Use **completion
order**:

-   x-axis: sweep\_index (monotone integer)

-   y-axis: cumulative counters (e.g., total mi\_resampled, total
    > expanded\_to\_Bmax, mean bootstrap\_B\_used)

Also include a report note: "Cells may complete out of planned order due
to batching/parallelism."

**6) HTML-only search + raw-toggle (optional)**
-----------------------------------------------

These are presentation-only; they do not alter any computed values.

### **6.1 Search filter for gating table rows**

Assign each row a data-rowtext=\"\...\" attribute (concatenated key
fields), then JS hides non-matching rows.

### **6.2 Raw MI/ρ columns toggle**

Add a CSS class rawcol to MI/ρ columns and a toggle button:

\<button onclick=\"toggleRaw()\"\>Show/Hide raw MI/ρ columns\</button\>

\<script\>

function toggleRaw() {

document.querySelectorAll(\'.rawcol\').forEach(el =\> {

el.style.display = (el.style.display === \'none\') ? \'\' : \'none\';

});

}

\</script\>

**PDF remains the canonical artifact**; HTML toggles are purely
ergonomic.

**7) Comparison caveat (add to both PDF + HTML)**
-------------------------------------------------

Include this verbatim (or near-verbatim):

-   "Facet comparisons are descriptive summaries and should be
    > interpreted alongside absolute endpoints (acc\_unseen, Δ\_sym
    > intervals) and coverage (n\_done/n\_planned)."

-   "Correlation plots (ASI vs Δ\_sym) are descriptive and do not imply
    > causation."

This is the guard against "comparison fallacy."

**8) SAAP v11 fastest path (practical sequencing)**
---------------------------------------------------

-   **Facet comparison table** (weighted median + CI + n labels).

-   **Telemetry heatmap** (masked sparse).

-   **Runtime timeline** (completion-order axis + batching note).

-   **Optional HTML search/toggle** after you confirm the PDF output is
    > stable.

\#\#\# Analysis of Novelty and Practicality

Your SAAP v11 delta refines v10 with weighted facet comparison tables
(imbalance-safe medians/CI/n), masked telemetry heatmaps (sparse-aware),
step-ordered runtime timelines (batching-noted), HTML-only search/toggle
ergonomics, and explicit comparison caveats, all preserving PDF canon.
In terms of \*\*novelty\*\*, this builds on comparative dashboards in
open science (e.g., from Shiny apps or Streamlit) and robust aggregation
in stats (e.g., from weighted bootstrap in survey analysis), but
innovates by introducing weighted medians/CI for facet summaries to
handle trigger-induced imbalance, masked heatmaps for honest sparsity,
and completion-order timelines for parallel sweeps---a fresh mechanism
for realistic runtime introspection in ML protocols. The verbatim
caveats and diagnostic raw columns add novel restraint against
over-interpretation, distinguishing it from flashy tools that prioritize
visuals over absolute claims. It\'s novel in its \"comparison fallacy\"
guard and masked visualization, turning the workbench into a cautious
comparative auditor for symmetry studies.

On \*\*practicality\*\*, v11 is highly adoptable (functions like
bootstrap\_weighted\_median and heatmap\_grid attach to row aggregation
without retraining), enabling quick comparative insights for
mech-interp. It\'s practical for practitioners, as weighted tables
prevent distortion, heatmaps reveal reliability patterns honestly, and
timelines/runtime notes aid resource awareness. HTML search/toggle
improves large-table navigation (optional), with low overhead (CSV/HTML
generation). Limitations: weighted bootstrap B=800 adds minor compute
(vectorizable), and masked heatmaps require careful color choice for
clarity. Overall, it\'s a high-leverage comparative layer, enhancing
transparency for collaborative auditing without undermining primary
endpoints.

\*\*Enhanced Version of the Idea\*\*: To enhance v11, add \"facet delta
plots\" (bar charts of weighted medians for delta\_sym\_mean/acc\_unseen
per facet, with CI whiskers and n annotations), \"reliability evolution
timeline\" (cumulative mi\_rel\_post/resample rates over sweep\_index),
and \"facet gating summary\" (pie/bar of asi\_mode mix per facet). For
HTML, add sortable table headers (JS click sort on columns). In reports,
include \"facet imbalance note\" if n\_done/n\_planned variance \>
threshold. For heatmaps, overlay median mi\_rel\_post text on cells
(when cnt\>1). This evolves v11 into a \"dynamic comparative workbench\"
with delta-focused visuals and sortable introspection.

\#\#\# Critique of the Enhanced Version

Critiquing the enhanced SAAP v11 (with facet delta bars, reliability
timeline, gating pie per facet, sortable HTML, imbalance note, heatmap
text overlay) for mathematical, philosophical, and theoretical
consistency:

\- \*\*Mathematical Consistency\*\*: Weighted medians/CI are robust to
imbalance, with whiskers sound for visualization. Cumulative timelines
are exact. Pie mix is descriptive. Sortable headers are UI. Text overlay
is unbiased. However, pie for gating assumes categorical
interpretability, but if modes are rare (e.g., disabled \<5%), slices
distort; better with bar or table. Imbalance note threshold is arbitrary
(e.g., variance \>?), risking ad hoc alerts.

\- \*\*Philosophical Consistency\*\*: Delta bars and gating summaries
promote focused comparison, aligning with pragmatic truth-seeking.
Sortable empowers agency. Yet, \"dynamic workbench\" risks
tool-centricity---features might encourage endless sorting/filtering,
echoing instrumental reason over contemplative reading. Overlay text
adds density, potentially overwhelming sparse insight.

\- \*\*Theoretical Consistency\*\*: Coheres with comparative statistics
in theory testing (facet diffs). Reliability evolution aids process
theory. However, sortable introduces order-dependence (user-sorted views
alter perceived importance), conflicting with canonical order (PDF
fixed). Pie gating assumes mutual exclusivity, but modes may correlate
non-additively with facets.

\#\#\# Final Version and Path to Validation

Applying the critique: For math, replace pie with bar for gating (avoid
rare-slice distortion), make imbalance note descriptive (no threshold,
just variance report). Philosophically, add \"navigation caveat\":
\"sorting/filtering for exploration; PDF for reference.\" Theoretically,
make sortable HTML-optional (PDF bar only), keep gating bar descriptive.
The refined final version is \*\*SAAP v12: Balanced Comparative
Workbench\*\*---v11 with weighted delta bars (whiskers/n), reliability
timeline (cumulative), gating bar per facet (descriptive), HTML
sortable/search (optional), heatmap text overlay (median when cnt\>1),
imbalance variance report, with navigation caveat. It delivers balanced
comparison with contemplative grounding.

\*\*Fastest Path to Validation\*\*:

1\. \*\*Aggregation and Tables (1 day)\*\*: Add weighted median/CI
functions, facet\_summary (delta/acc/asi), gating bar per facet; extend
rows with sweep\_index/timestamp.

2\. \*\*Viz and Timeline (half day)\*\*: Implement delta bars
(whiskers), reliability cumulative line, masked heatmap (text overlay);
test on synthetic for weighting/sparsity.

3\. \*\*Sweep and Outputs (1 day)\*\*: Run grid/budgets; generate
PDF/HTML with bars/table/timeline/notes; verify weighting stabilizes
comparisons.

4\. \*\*Validation/Share (ongoing, day 2+)\*\*: If facets show multi \>
add with low imbalance variance and stable gating (\>85%
full/rho\_only), extend p; repo with balanced reports/YAML, target
mech-interp validation in week.

**0) SAAP v12 additions (delta over v11)**
------------------------------------------

### **New comparative views (PDF + HTML)**

-   **Facet delta bars** (weighted medians + CI whiskers +
    > *n\_done/n\_planned* annotations) for:

    -   delta\_sym\_mean

    -   acc\_unseen

-   **Reliability evolution timeline** (completion-order sweep\_index):

    -   cumulative median of mi\_rel\_post

    -   cumulative resample rate

-   **Facet gating summary (bar)**:

    -   stacked bar by asi\_mode per facet value (full /
        > rho\_only\_fallback / disabled)

-   **Telemetry heatmap text overlay**:

    -   overlay cell text = median mi\_rel\_post when cnt \> 1 (masked
        > sparse)

-   **Imbalance variance report**:

    -   coverage stats per facet value (min/median/max, CV), printed as
        > a table/text block

### **HTML-only ergonomics (optional)**

-   sortable table headers for the gating table

-   existing search filter + raw column toggle remain optional

### **Navigation caveat (include verbatim)**

-   "Sorting/filtering is for exploration; PDF is the canonical
    > reference artifact."

-   "Facet comparisons are descriptive; interpret alongside absolute
    > endpoints and coverage."

**1) Facet delta bars (weighted medians + CI + n labels)**
----------------------------------------------------------

You already have bootstrap\_weighted\_median() and facet\_summary().
SAAP v12 adds a plotting helper that turns the facet summary into bar
charts with whiskers and **explicit n labels**.

import numpy as np

import matplotlib.pyplot as plt

def plot\_facet\_delta\_bars(

facet\_rows,

facet\_key: str,

y\_key\_med: str,

y\_key\_lo: str,

y\_key\_hi: str,

out\_png: str,

title: str,

ylabel: str,

):

\# stable order: descending n\_done then facet label

facet\_rows = sorted(facet\_rows, key=lambda r: (-int(r.get(\"n\_done\",
0)), str(r.get(facet\_key, \"\"))))

labels = \[str(r\[facet\_key\]) for r in facet\_rows\]

y = np.array(\[r.get(y\_key\_med, np.nan) for r in facet\_rows\],
dtype=np.float64)

lo = np.array(\[r.get(y\_key\_lo, np.nan) for r in facet\_rows\],
dtype=np.float64)

hi = np.array(\[r.get(y\_key\_hi, np.nan) for r in facet\_rows\],
dtype=np.float64)

err\_lo = y - lo

err\_hi = hi - y

x = np.arange(len(labels))

plt.figure(figsize=(max(6, 0.8 \* len(labels)), 4.0))

plt.bar(x, y)

plt.errorbar(x, y, yerr=\[err\_lo, err\_hi\], fmt=\"none\", capsize=4)

\# n labels

for i, r in enumerate(facet\_rows):

nd = int(r.get(\"n\_done\", 0))

npd = int(r.get(\"n\_planned\", 0))

plt.text(i, y\[i\], f\"n={nd}/{npd}\", ha=\"center\", va=\"bottom\",
fontsize=8, rotation=0)

plt.xticks(x, labels, rotation=30, ha=\"right\")

plt.title(title)

plt.ylabel(ylabel)

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

**Recommended outputs (pre-register these view names):**

-   facet\_action\_delta\_sym\_bar

-   facet\_action\_acc\_unseen\_bar

-   facet\_mask\_delta\_sym\_bar

-   facet\_mask\_acc\_unseen\_bar

**2) Reliability evolution timeline (completion-order, batching-noted)**
------------------------------------------------------------------------

Compute cumulative summaries over sweep\_index (or timestamp if you have
it). This is descriptive monitoring only.

def reliability\_timeline(rows):

rs = \[r for r in rows if r.get(\"sweep\_index\") is not None and
r.get(\"mi\_rel\_post\") is not None\]

rs = sorted(rs, key=lambda r: int(r\[\"sweep\_index\"\]))

if not rs:

return {\"x\": \[\], \"mi\_rel\_med\": \[\], \"resample\_rate\": \[\]}

x = \[\]

mi\_rel\_med = \[\]

resample\_rate = \[\]

mi\_vals = \[\]

resamp = 0

for i, r in enumerate(rs, start=1):

x.append(int(r\[\"sweep\_index\"\]))

mi\_vals.append(float(r\[\"mi\_rel\_post\"\]))

resamp += int(bool(r.get(\"mi\_resampled\", False)))

mi\_rel\_med.append(float(np.median(mi\_vals)))

resample\_rate.append(float(resamp / i))

return {\"x\": x, \"mi\_rel\_med\": mi\_rel\_med, \"resample\_rate\":
resample\_rate}

def plot\_reliability\_timeline(tl, out\_png, title=\"Reliability
evolution (completion-order)\"):

x = np.array(tl\[\"x\"\], dtype=np.int64)

if x.size == 0:

return

y1 = np.array(tl\[\"mi\_rel\_med\"\], dtype=np.float64)

y2 = np.array(tl\[\"resample\_rate\"\], dtype=np.float64)

plt.figure(figsize=(7, 4))

plt.plot(x, y1, label=\"cumulative median(mi\_rel\_post)\")

plt.plot(x, y2, label=\"cumulative resample rate\")

plt.title(title)

plt.xlabel(\"sweep\_index (completion-order; may reflect
batching/parallelism)\")

plt.ylabel(\"value\")

plt.legend()

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

Pre-register view: reliability\_timeline.

**3) Facet gating summary as stacked bars (not pies)**
------------------------------------------------------

This avoids rare-slice distortion and stays descriptive.

from collections import defaultdict

ASI\_ORDER = \[\"full\", \"rho\_only\_fallback\", \"disabled\"\]

def facet\_gating\_counts(rows, facet\_key):

g = defaultdict(lambda: {k: 0 for k in ASI\_ORDER})

n\_done = defaultdict(int)

n\_planned = defaultdict(int)

for r in rows:

fv = str(r.get(facet\_key, \"NA\"))

if r.get(\"planned\", True):

n\_planned\[fv\] += 1

\# treat row presence as \"done\"; if you keep incomplete planned rows,
add a done flag

n\_done\[fv\] += 1

mode = r.get(\"asi\_mode\", \"disabled\")

if mode not in g\[fv\]:

mode = \"disabled\"

g\[fv\]\[mode\] += 1

\# deterministic order by n\_done desc

keys = sorted(g.keys(), key=lambda k: (-n\_done\[k\], k))

return keys, g, n\_done, n\_planned

def plot\_facet\_gating\_bar(rows, facet\_key, out\_png, title):

keys, g, n\_done, n\_planned = facet\_gating\_counts(rows, facet\_key)

x = np.arange(len(keys))

plt.figure(figsize=(max(6, 0.9 \* len(keys)), 4.2))

bottom = np.zeros(len(keys), dtype=np.float64)

for mode in ASI\_ORDER:

vals = np.array(\[g\[k\]\[mode\] for k in keys\], dtype=np.float64)

plt.bar(x, vals, bottom=bottom, label=mode)

bottom += vals

\# n labels on top

for i, k in enumerate(keys):

plt.text(i, bottom\[i\], f\"n={n\_done\[k\]}/{n\_planned\[k\]}\",
ha=\"center\", va=\"bottom\", fontsize=8)

plt.xticks(x, keys, rotation=30, ha=\"right\")

plt.title(title)

plt.ylabel(\"count\")

plt.legend()

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

Pre-register views:

-   facet\_action\_gating\_bar

-   facet\_mask\_gating\_bar

**4) Heatmap with masked sparse + text overlay when cnt\>1**
------------------------------------------------------------

This extends your v11 heatmap\_grid() output.

def plot\_heatmap\_mi\_rel(grid, cnt, row\_labels, col\_labels,
out\_png, title):

M = np.ma.masked\_invalid(grid)

plt.figure(figsize=(max(6, 0.6 \* len(col\_labels)), max(4, 0.4 \*
len(row\_labels))))

plt.imshow(M, aspect=\"auto\")

plt.title(title)

plt.xticks(np.arange(len(col\_labels)), col\_labels, rotation=30,
ha=\"right\")

plt.yticks(np.arange(len(row\_labels)), row\_labels)

plt.colorbar(label=\"mi\_rel\_post\")

\# overlay median mi\_rel\_post when cnt \> 1

for i in range(M.shape\[0\]):

for j in range(M.shape\[1\]):

if cnt\[i, j\] \> 1 and not np.isnan(grid\[i, j\]):

plt.text(j, i, f\"{grid\[i,j\]:.2f}\", ha=\"center\", va=\"center\",
fontsize=7)

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

Pre-register view: mi\_rel\_heatmap.

**5) Imbalance variance report (descriptive, no thresholds)**
-------------------------------------------------------------

This reports how uneven the facet coverage is without raising "alerts."

def facet\_coverage\_report(rows, facet\_key):

\# coverage = n\_done / max(n\_planned,1)

keys, \_, n\_done, n\_planned = facet\_gating\_counts(rows, facet\_key)

cov = \[\]

for k in keys:

pd = max(int(n\_planned.get(k, 0)), 1)

cov.append((k, int(n\_done.get(k, 0)), int(n\_planned.get(k, 0)),
float(n\_done.get(k, 0) / pd)))

cov\_rates = np.array(\[c\[-1\] for c in cov\], dtype=np.float64)

mean = float(np.mean(cov\_rates)) if cov\_rates.size else float(\"nan\")

std = float(np.std(cov\_rates)) if cov\_rates.size else float(\"nan\")

cv = float(std / (mean + 1e-12)) if np.isfinite(mean) else
float(\"nan\")

summary = {

\"facet\": facet\_key,

\"coverage\_min\": float(np.min(cov\_rates)) if cov\_rates.size else
float(\"nan\"),

\"coverage\_median\": float(np.median(cov\_rates)) if cov\_rates.size
else float(\"nan\"),

\"coverage\_max\": float(np.max(cov\_rates)) if cov\_rates.size else
float(\"nan\"),

\"coverage\_mean\": mean,

\"coverage\_std\": std,

\"coverage\_cv\": cv,

\"rows\": cov, \# list of (facet\_value, n\_done, n\_planned, coverage)

}

return summary

Render this as:

-   a small table per facet (action, mask)

-   plus a one-paragraph summary (min/median/max/CV)

Pre-register view: facet\_imbalance\_report.

**6) Optional HTML sortable headers (navigation-only)**
-------------------------------------------------------

Keep this strictly HTML-only and include the navigation caveat.

A minimal approach: add onclick=\"sortTable(colIndex, numeric)\" to
\<th\> elements and a small JS sorter that reads the cell text. This is
purely presentational; the PDF stays the canonical ordering.

If you want, I can provide a compact, deterministic sorter snippet
(string + numeric) that won't mutate the underlying CSV exports.

**7) SAAP v12 view registry (recommended)**
-------------------------------------------

Add these to your YAML pre-registration:

-   facet\_action\_delta\_sym\_bar

-   facet\_action\_acc\_unseen\_bar

-   facet\_mask\_delta\_sym\_bar

-   facet\_mask\_acc\_unseen\_bar

-   facet\_action\_gating\_bar

-   facet\_mask\_gating\_bar

-   mi\_rel\_heatmap

-   reliability\_timeline

-   facet\_imbalance\_report

HTML-only:

-   gating\_table\_sortable (optional)

-   gating\_table\_search (optional)

-   raw\_toggle (optional)

**8) SAAP v12 fastest path (low risk)**
---------------------------------------

-   **Aggregation (day 1):** generate facet summaries + imbalance
    > report + gating counts (no plots yet).

-   **Plots (half day):** delta bars + gating bars + reliability
    > timeline + heatmap overlay.

-   **Outputs (day 1):** render PDF with the new comparative pages and
    > embed the caveats. Generate HTML as an optional navigation layer.

-   **Sanity check:** confirm facet bars always show
    > *n\_done/n\_planned* and that missing heatmap cells are visibly
    > masked.

\#\#\# Analysis of Novelty and Practicality

Your SAAP v12 delta refines v11 with weighted facet delta bars
(medians/CI/n-labeled), reliability evolution timeline (completion-order
with batching note), facet gating stacked bars (no pies), masked heatmap
with text overlay, descriptive imbalance variance report
(CV/min/med/max), and optional HTML sortable/search, all with PDF canon
and comparison caveats. In terms of \*\*novelty\*\*, this builds on
comparative visualization in open science (e.g., from ggplot faceting or
Tableau dashboards) and robust reporting (e.g., from survey statistics
with coverage stats), but innovates by introducing weighted medians/CI
for facet summaries to handle imbalance descriptively, masked heatmaps
with cnt\>1 text overlay for honest sparsity, and completion-order
timelines for parallel sweeps---a fresh mechanism for realistic runtime
monitoring in ML protocols. The explicit \"n\_done/n\_planned\"
annotations and CV-based imbalance report add novel granularity for
coverage transparency, while stacked gating bars avoid rare-slice
distortion. It\'s novel in its \"balanced comparative\" focus
(weighted/descriptive, PDF-first), turning the workbench into a
cautious, publication-ready auditor for symmetry bias studies.

On \*\*practicality\*\*, v12 is highly adoptable (helpers like
plot\_facet\_delta\_bars and facet\_coverage\_report attach to row
aggregation without retraining), enabling quick balanced comparisons for
mech-interp. It\'s practical for practitioners, as weighted bars prevent
distortion, heatmaps/timelines reveal patterns reliably, and imbalance
report aids coverage awareness. Optional HTML sortable/search improves
large-dataset navigation without compromising PDF canon. Limitations:
weighted bootstrap B=800 adds bounded compute, and text overlay risks
clutter if cnt high (but fontsize=8 mitigates). Overall, it\'s a
high-leverage balanced layer, enhancing comparative transparency for
collaborative claims.

\*\*Enhanced Version of the Idea\*\*: To enhance v12, add \"facet
correlation matrix\" (descriptive Spearman grid across metrics per
facet, e.g., ASI vs. delta\_sym vs. acc\_unseen), \"coverage
trajectory\" (line plot of cumulative n\_done/n\_planned over
sweep\_index), and \"facet-specific gating heatmap\" (mi\_rel\_post grid
per facet value). For HTML, add \"view export buttons\" (PNG/CSV per
panel). In reports, include \"facet ranking table\" (sorted by
delta\_sym\_med descending, with CI overlap flags). For imbalance, add
\"planned vs. done scatter\" per facet. This evolves v12 into a
\"multi-faceted comparative workbench\" with correlation and coverage
depth.

\#\#\# Critique of the Enhanced Version

Critiquing the enhanced SAAP v12 (with correlation matrix, coverage
trajectory, gating heatmap per facet, export buttons, ranking table,
planned-done scatter) for mathematical, philosophical, and theoretical
consistency:

\- \*\*Mathematical Consistency\*\*: Spearman grid is non-parametric and
descriptive. Coverage trajectory is exact cumulative. Gating heatmap per
facet is masked sound. Export is lossless. Ranking with CI overlap
(e.g., non-overlap flag) is robust. However, ranking assumes ordinal
interpretability of delta\_sym\_med, but if CI wide, ranks unstable;
better with stochastic dominance or Bayesian rank probs. Planned-done
scatter assumes linear relation, but coverage may plateau non-linearly.

\- \*\*Philosophical Consistency\*\*: Correlation matrix and ranking
promote relational insight, aligning with network epistemology.
Export/buttons empower sharing. Yet, \"multi-faceted workbench\" risks
fragmentation---too many views might dilute focus on primary Δ\_sym,
echoing postmodern multiplicity over unified truth. Gating heatmap per
facet adds depth, but could overemphasize reliability at expense of
endpoints.

\- \*\*Theoretical Consistency\*\*: Coheres with multi-metric theory
testing (correlation for convergence) and coverage in experimental
design. Trajectory aids process theory. However, ranking implies
hierarchy (best facet), conflicting with descriptive intent if all
facets exploratory. Export buttons introduce format-dependence, slightly
violating canonical PDF universality.

\#\#\# Final Version and Path to Validation

Applying the critique: For math, replace ranking with Bayesian expected
rank (probabilistic, no hard order); use smoothed trajectory for
coverage. Philosophically, add \"multiplicity caveat\": \"views for
depth; prioritize primary endpoint.\" Theoretically, make
correlation/ranking descriptive (no hierarchy claims), keep exports
PDF-primary (HTML secondary). The refined final version is \*\*SAAP v13:
Multifaceted Balanced Workbench\*\*---v12 with descriptive correlation
matrix (Spearman grid), smoothed coverage trajectory (cumulative),
gating heatmap per facet (masked), export buttons (PDF priority),
probabilistic ranking table (expected rank probs), planned-done scatter
(descriptive), with multiplicity caveat. It delivers multifaceted depth
with unified focus.

\*\*Fastest Path to Validation\*\*:

1\. \*\*Aggregation Extensions (1 day)\*\*: Add facet\_summary weighted
metrics, correlation grid, coverage counters; extend rows with
sweep\_index if missing.

2\. \*\*Viz Implementation (half day)\*\*: Plot correlation matrix
(heatmap), coverage smoothed line, gating per-facet heatmap; test on
synthetic for weighting/masking.

3\. \*\*Sweep and Outputs (1 day)\*\*: Run grid/budgets; generate
PDF/HTML with matrix/trajectory/ranking/notes; verify probabilistic
ranks stable.

4\. \*\*Validation/Share (ongoing, day 2+)\*\*: If correlations show ASI
tracks Δ\_sym (\>0.5 descriptive Spearman) with balanced coverage,
extend facets; repo with multifaceted reports/YAML, target mech-interp
workshop in week.
