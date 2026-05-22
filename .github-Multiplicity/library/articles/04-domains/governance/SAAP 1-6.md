---
slug: saap-1-6
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/governance/SAAP 1-6.md
  last_synced: '2026-03-20T17:17:18.554037Z'
---

If you want to proceed to an engineer-ready repo structure, the next
clean step is to package this into:

-   schemas/ (Case + ScoreReport),

-   templates/ (5 YAML artifacts),

-   engine/ (regret, exposure sampling, proposal audit),

-   eval/ (as-of case pack + rubrics + rater protocol).

I can draft that repo layout and a minimal reference implementation
skeleton (Python) that loads a Case.json, validates it, produces a
ScoreReport.json, and emits the five artifacts as stubs populated with
case metadata.

\#\#\# Analysis of Novelty and Practicality Your proposed fixes and
validation protocol for the symmetry regularization experiment in
attention heads---targeting invariance under group actions for a
quadratic residue (QR) task modulo primes---build on concepts from
representation theory and AI regularization. In terms of
\*\*novelty\*\*, this isn\'t entirely groundbreaking, as
group-equivariant networks (e.g., from Cohen & Welling\'s work on group
convolutions) and invariance regularizers (e.g., in SSL like SimCLR)
have been explored, but applying them specifically to attention logits
with \"wrong symmetry\" ablations (shift/random vs. multiplicative) for
a number-theoretic task is fresh. It tests whether task-aligned
symmetries (multiplicative for ratios) provide inductive bias over
mismatched ones, especially with a Fourier-encoded input and mask. The
optional ratio-query upgrade adds novelty by forcing relational
computation, aligning the task more tightly with the model\'s structural
bias, which echoes diagnostic tasks in interpretability research (e.g.,
modular arithmetic in grokking studies). Overall, it\'s a targeted
extension of symmetry-aware ML, novel in its ablation design and number
theory domain. On \*\*practicality\*\*, the fixes are highly actionable:
they prevent crashes (device handling), eliminate confounds
(mask-invariant base logits), and optimize compute (query-specific
loss), making the experiment robust for GPU runs and interpretable. The
validation protocol is efficient, focusing on seeded runs and a confound
check, which could yield quick insights into whether symmetry priors
accelerate learning or improve generalization on primes. It\'s practical
for researchers with access to PyTorch setups, as it minimizes overhead
while addressing common pitfalls in ablation studies. Limitations
include potential underuse of the attention mechanism if the MLP
baseline is too strong (as you noted), and reliance on a specific task
that may not generalize to broader AI systems. Still, it\'s a low-cost
way to probe inductive biases, with clear payoffs in debugging and
result validity. \*\*Enhanced Version of the Idea\*\*: To strengthen it,
integrate a \"symmetry strength\" hyperparameter (λ for the invariance
loss) with a sweep (e.g., λ ∈ {0, 0.1, 1.0}) to quantify how much the
regularizer contributes, allowing dose-response analysis. For the
ratio-query variant, make it configurable via a flag, sampling two
positions (i,j) and targeting Legendre(i \* j\^{-1} mod p), with modular
inverse handled safely (e.g., via pow(j, p-2, p)). Add a \"no-mask\"
ablation to isolate the mask\'s role from the symmetry regularizer. In
code, wrap group actions in a registry for easy extension (e.g., to
cyclic groups), and log invariance penalties separately for diagnostics.
This enhances modularity, making it a reusable framework for symmetry
experiments beyond QR. \#\#\# Critique of the Enhanced Version
Critiquing the enhanced symmetry regularization protocol for
mathematical, philosophical, and theoretical consistency: -
\*\*Mathematical Consistency\*\*: The group actions (multiplicative
conjugation invariance) are well-defined for the ratio mask, as
multiplicative groups commute appropriately, and the ablation to
shift/random tests specificity soundly. The λ sweep and ratio-query
target align with loss landscapes in optimization theory, potentially
revealing saddle points or grokking phenomena. However, the Fourier
encoding assumes uniform frequency representation, which may not hold
for all primes (e.g., larger p could require higher resolutions),
risking incomplete embeddings. Modular inverses in the ratio variant are
correct via Fermat\'s Little Theorem, but without handling j=0
(non-invertible), it could introduce edge cases. The invariance on
base\_logits is mathematically preferable to avoid mask dominance, but
if Q/K are not normalized properly, scale mismatches could still
confound \"wrong\" symmetries. - \*\*Philosophical Consistency\*\*:
Philosophically, this promotes a structuralist view of learning
(inductive biases as symmetries, per Noether\'s theorem analogies in
ML), emphasizing that models should \"respect\" task geometry rather
than memorize. It aligns with parsimony (Occam\'s razor via priors) but
risks reductionism---treating cognition as group-invariant computation
ignores emergent behaviors in larger models. The \"wrong symmetry\"
ablation probes falsifiability, echoing Popperian science, but the
enhanced sweeps could encourage p-hacking if not pre-registered. The
ratio upgrade enhances teleological fit (task-model alignment), but
philosophically, it assumes symmetries are \"discoverable\" via
regularization, potentially overlooking pluralistic biases where
mismatched priors spur creativity. - \*\*Theoretical Consistency\*\*:
Theoretically, it coheres with equivariant learning (e.g., Steerable
CNNs) and attention as relational operators, where invariance enforces
robustness. The confound check and seeded runs support statistical
validity, and the registry enables extensibility. However, the
\"no-mask\" ablation might violate task assumptions if ratios are core,
leading to inconsistent comparisons. In group theory terms, random
actions lack closure properties, making them a weak \"wrong\"
control---better to use a non-task-aligned group like additive mod p.
The enhanced diagnostics (separate logging) aid interpretability, but
without theoretical bounds on regularization (e.g., via PAC-Bayes), it
risks empirical over-reliance. \#\#\# Final Version and Path to
Validation Applying the critique: To ensure mathematical embedding
completeness, cap p at a value where Fourier resolution suffices (e.g.,
p\<1000) and add j≠0 checks in ratio sampling. Philosophically,
pre-register λ values and ablations to avoid hacking. Theoretically,
replace random action with additive group (Z/pZ) as a stronger
mismatched control, and bound regularization via early stopping if
invariance plateaus. The refined final version is a \*\*Symmetry-Ablated
Attention Protocol (SAAP)\*\*: PyTorch-based experiment with device-safe
actions (to-device inv\_perm), base-logit invariance, query-gather
loss/eval, configurable ratio-query task (flag for single vs. dual
positions, with inverse safety), λ sweep {0,0.1,1.0}, no-mask ablation,
action registry (multiplicative, shift, additive), and separate
invariance logging. It outputs per-prime accuracies, invariance curves,
and confound deltas, emphasizing task-model fit without over-reduction.
\*\*Fastest Path to Validation\*\*: 1. \*\*Code Integration (1-2
days)\*\*: Apply the 3 core patches (device, base\_logits, query loss)
plus ratio flag, λ sweep, no-mask toggle, and additive action; use a
config dict for ablations to minimize branches. 2. \*\*Seeded Runs (2-3
days)\*\*: Execute on seeds {0,1,2,3,4} across ablations (full,
baseline, wrong symmetries, no-mask), reporting mean±std test acc by
prime bucket (small/medium/large); include λ=0 as pure baseline. 3.
\*\*Confound and Diagnostic Checks (1 day)\*\*: Compare invariance on
base vs. masked logits (expect no flip in conclusions); log invariance
penalties and check for plateaus; for ratio variant, verify inverse
handling via unit tests. 4. \*\*Analysis and Iteration (ongoing,
starting day 4)\*\*: Plot acc vs. λ curves; if no gap, debug with
attention visualizations; share minimal repo with configs/results for
peer review, targeting a pre-print or blog post within a week. If you\'d
like the minimal diff code rewrite, provide your base code snippet or
key classes (e.g., via paste or attachment), and I\'ll generate
it---otherwise, I can sketch a standalone version.

Thought for 1m 30s

Below is a standalone, implementable **SAAP (Symmetry-Ablated Attention
Protocol)** reference script in PyTorch that bakes in the exact fixes
you enumerated:

-   **Device-safe permutations** (all perm tensors moved to the same
    > device)

-   **Invariance penalty computed on** base\_logits (pre-mask /
    > pre-attention masking)

-   **Query-gather supervision** (compute loss on sampled rows or
    > sampled (i,j) pairs)

-   **Ratio-query mode** (labels = Legendre(i⋅j−1 mod p), with j≠0
    > enforced)

-   **No-mask ablation** (disable QR attention mask)

-   **Action registry** with **multiplicative**, **additive**, and
    > **random** controls

-   Separate logging for **task loss** and **invariance loss**

-   Minimal **λ sweep** support

You can drop this into a single file (e.g., saap\_qr\_symmetry.py) and
run as-is.

\# saap\_qr\_symmetry.py

\# PyTorch reference implementation for SAAP:

\# symmetry regularization on attention base logits for QR ratio task
mod prime p.

from \_\_future\_\_ import annotations

import math

import random

from dataclasses import dataclass

from typing import Dict, List, Tuple, Optional

import numpy as np

import torch

import torch.nn as nn

import torch.nn.functional as F

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Number theory utilities

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def legendre\_symbol(a: int, p: int) -\> int:

\"\"\"Legendre symbol (a\|p) for odd prime p. Returns -1, 0, or
+1.\"\"\"

a %= p

if a == 0:

return 0

\# Euler\'s criterion: a\^((p-1)/2) ≡ 1 (QR), ≡ -1 (NQR) mod p

t = pow(a, (p - 1) // 2, p)

if t == 1:

return 1

if t == p - 1:

return -1

raise ValueError(f\"Unexpected Euler criterion result: {t} for a={a},
p={p}\")

def build\_qr\_ratio\_mask(p: int, device: torch.device) -\>
torch.Tensor:

\"\"\"

Build mask M\[i,j\] = 1 if i \* j\^{-1} is a quadratic residue mod p,
else 0.

Defined on indices 0..p-1; if i==0 or j==0, set M=0 (non-invertible /
degenerate).

Shape: (p, p), dtype: float32 in {0,1}.

\"\"\"

M = torch.zeros((p, p), device=device, dtype=torch.float32)

\# Precompute inverses for 1..p-1

inv = \[0\] \* p

for j in range(1, p):

inv\[j\] = pow(j, p - 2, p) \# Fermat inverse

for i in range(1, p):

for j in range(1, p):

r = (i \* inv\[j\]) % p

M\[i, j\] = 1.0 if legendre\_symbol(r, p) == 1 else 0.0

return M

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Group action registry (permutations on indices 0..p-1)

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def perm\_multiplicative(p: int, g: int) -\> np.ndarray:

\"\"\"Permutation i -\> g\*i mod p. 0 stays 0 for any g.\"\"\"

g %= p

assert 1 \<= g \<= p - 1

perm = np.arange(p, dtype=np.int64)

for i in range(p):

perm\[i\] = (g \* i) % p

return perm

def perm\_additive(p: int, k: int) -\> np.ndarray:

\"\"\"Permutation i -\> i+k mod p.\"\"\"

k %= p

perm = (np.arange(p, dtype=np.int64) + k) % p

return perm

def perm\_random(p: int, rng: np.random.Generator) -\> np.ndarray:

\"\"\"Random permutation; keep 0 fixed to preserve the \'special
token\'.\"\"\"

perm = np.arange(p, dtype=np.int64)

rest = np.arange(1, p, dtype=np.int64)

rng.shuffle(rest)

perm\[1:\] = rest

return perm

ACTION\_REGISTRY = {

\"multiplicative\": perm\_multiplicative,

\"additive\": perm\_additive,

\"random\": None, \# handled separately due to rng

}

def sample\_action\_elements(action: str, p: int, n: int, rng:
np.random.Generator) -\> List\[int\]:

if action == \"multiplicative\":

\# sample g in {1..p-1}

return rng.integers(1, p, size=n, endpoint=False).tolist()

if action == \"additive\":

\# sample k in {0..p-1}

return rng.integers(0, p, size=n, endpoint=False).tolist()

if action == \"random\":

\# elements are dummy; perm is drawn directly each time

return \[0\] \* n

raise ValueError(f\"Unknown action \'{action}\'\")

def apply\_conjugation(L: torch.Tensor, perm: torch.Tensor) -\>
torch.Tensor:

\"\"\"

Conjugate: P L P\^T implemented by simultaneous row/col permutation.

L: (p,p), perm: (p,)

\"\"\"

return L.index\_select(0, perm).index\_select(1, perm)

def invariance\_penalty\_base\_logits(

base\_logits: torch.Tensor,

action: str,

p: int,

n\_samples: int,

rng: np.random.Generator,

) -\> torch.Tensor:

\"\"\"

Invariance regularizer: E\_g \|\|L - P\_g L P\_g\^T\|\|\_F\^2 / (p\^2).

Computed on base\_logits (pre-mask).

\"\"\"

device = base\_logits.device

assert base\_logits.shape == (p, p)

elems = sample\_action\_elements(action, p, n\_samples, rng)

penalties = \[\]

for e in elems:

if action == \"random\":

perm\_np = perm\_random(p, rng)

else:

perm\_fn = ACTION\_REGISTRY\[action\]

perm\_np = perm\_fn(p, int(e))

perm = torch.as\_tensor(perm\_np, dtype=torch.long, device=device) \#
device-safe

Lg = apply\_conjugation(base\_logits, perm)

diff = base\_logits - Lg

penalties.append((diff \* diff).mean())

return torch.stack(penalties).mean()

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Fourier features for indices mod p

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def fourier\_features\_indices(p: int, K: int, device: torch.device) -\>
torch.Tensor:

\"\"\"

Return features X of shape (p, 2K+1):

\[i/p, sin(2π k i/p), cos(2π k i/p)\] for k=1..K

\"\"\"

idx = torch.arange(p, device=device, dtype=torch.float32)

x0 = (idx / float(p)).unsqueeze(-1)

feats = \[x0\]

for k in range(1, K + 1):

angle = 2.0 \* math.pi \* k \* idx / float(p)

feats.append(torch.sin(angle).unsqueeze(-1))

feats.append(torch.cos(angle).unsqueeze(-1))

return torch.cat(feats, dim=-1)

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Model: single-head attention producing base logits

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

class SingleHeadAttention(nn.Module):

def \_\_init\_\_(self, d\_in: int, d\_model: int):

super().\_\_init\_\_()

self.proj = nn.Linear(d\_in, d\_model)

self.q = nn.Linear(d\_model, d\_model, bias=False)

self.k = nn.Linear(d\_model, d\_model, bias=False)

self.v = nn.Linear(d\_model, d\_model, bias=False)

def forward(self, x: torch.Tensor) -\> Tuple\[torch.Tensor,
torch.Tensor\]:

\"\"\"

x: (p, d\_in)

returns:

base\_logits: (p, p) = QK\^T / sqrt(d)

values: (p, d\_model)

\"\"\"

h = self.proj(x) \# (p, d\_model)

Q = self.q(h) \# (p, d\_model)

K = self.k(h) \# (p, d\_model)

V = self.v(h) \# (p, d\_model)

base\_logits = (Q @ K.T) / math.sqrt(Q.shape\[-1\])

return base\_logits, V

class SAAPModel(nn.Module):

def \_\_init\_\_(self, d\_in: int, d\_model: int):

super().\_\_init\_\_()

self.attn = SingleHeadAttention(d\_in=d\_in, d\_model=d\_model)

\# Optional head for ratio-query: map a single logit to output (can be
identity)

self.pair\_head = nn.Sequential(

nn.Linear(1, d\_model),

nn.ReLU(),

nn.Linear(d\_model, 1),

)

def forward(self, x: torch.Tensor) -\> Dict\[str, torch.Tensor\]:

base\_logits, V = self.attn(x)

return {\"base\_logits\": base\_logits, \"values\": V}

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Experiment config + losses

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\@dataclass

class SAAPConfig:

primes: List\[int\]

K\_fourier: int = 16

d\_model: int = 64

\# Task modes:

\# - \"matrix\": supervise entries of base\_logits against QR ratio mask

\# - \"ratio\": supervise sampled (i,j) entries as pairwise
classification

task\_mode: str = \"ratio\"

\# Supervision sampling

matrix\_row\_samples: int = 8 \# used in \"matrix\" mode

ratio\_pair\_samples: int = 256 \# used in \"ratio\" mode

\# Attention masking (architectural inductive bias)

use\_qr\_attention\_mask: bool = False \# \"no-mask ablation\" sets
False

attention\_mask\_strength: float = 1e9 \# applied as -strength on
forbidden entries

\# Symmetry regularizer

action: str = \"multiplicative\" \# \"multiplicative\" (aligned),
\"additive\" (mismatched), \"random\" (weak control)

inv\_samples: int = 8 \# number of group elements sampled per step

lam\_invariance: float = 0.1 \# λ

\# Training

steps: int = 2000

lr: float = 2e-3

weight\_decay: float = 0.0

seed: int = 0

device: str = \"cuda\" if torch.cuda.is\_available() else \"cpu\"

\# Diagnostics

log\_every: int = 100

def maybe\_apply\_attention\_mask(base\_logits: torch.Tensor, mask:
torch.Tensor, strength: float) -\> torch.Tensor:

\"\"\"

If mask\[i,j\]==0, suppress attention by adding -strength to logits.

Note: base\_logits invariance penalty is computed BEFORE calling this.

\"\"\"

\# forbidden =\> add -strength

suppressed = base\_logits + (mask - 1.0) \* strength

return suppressed

def bce\_from\_logits(logits: torch.Tensor, targets01: torch.Tensor) -\>
torch.Tensor:

return F.binary\_cross\_entropy\_with\_logits(logits, targets01)

def task\_loss\_matrix(

base\_logits: torch.Tensor,

mask01: torch.Tensor,

row\_samples: int,

rng: np.random.Generator,

) -\> torch.Tensor:

\"\"\"

Supervise selected rows (query gather) to reduce compute.

Targets are mask01 in {0,1}.

\"\"\"

p = base\_logits.shape\[0\]

\# sample rows uniformly from 1..p-1 (avoid 0)

rows = rng.integers(1, p, size=row\_samples, endpoint=False)

rows\_t = torch.as\_tensor(rows, dtype=torch.long,
device=base\_logits.device)

logits\_rows = base\_logits.index\_select(0, rows\_t) \# (row\_samples,
p)

targets\_rows = mask01.index\_select(0, rows\_t) \# (row\_samples, p)

return bce\_from\_logits(logits\_rows, targets\_rows)

def task\_loss\_ratio(

base\_logits: torch.Tensor,

mask01: torch.Tensor,

n\_pairs: int,

rng: np.random.Generator,

pair\_head: nn.Module,

) -\> torch.Tensor:

\"\"\"

Sample (i,j) pairs with i,j in 1..p-1 and j != 0.

Label is mask01\[i,j\] which equals 1 iff Legendre(i\*j\^{-1}) == 1.

\"\"\"

p = base\_logits.shape\[0\]

\# Sample i,j in residues; enforce j != 0 by sampling from 1..p-1.

ii = rng.integers(1, p, size=n\_pairs, endpoint=False)

jj = rng.integers(1, p, size=n\_pairs, endpoint=False)

ii\_t = torch.as\_tensor(ii, dtype=torch.long,
device=base\_logits.device)

jj\_t = torch.as\_tensor(jj, dtype=torch.long,
device=base\_logits.device)

\# Gather logits for pairs

pair\_logits = base\_logits\[ii\_t, jj\_t\].unsqueeze(-1) \# (n\_pairs,
1)

\# Optional head (lets you decouple raw attention logit scale)

out\_logits = pair\_head(pair\_logits).squeeze(-1) \# (n\_pairs,)

targets = mask01\[ii\_t, jj\_t\] \# (n\_pairs,)

return bce\_from\_logits(out\_logits, targets)

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Main training loop

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def run\_saap(cfg: SAAPConfig) -\> Dict\[str, float\]:

device = torch.device(cfg.device)

torch.manual\_seed(cfg.seed)

np\_rng = np.random.default\_rng(cfg.seed)

random.seed(cfg.seed)

\# Cache masks per prime on the correct device

mask\_cache: Dict\[int, torch.Tensor\] = {}

d\_in = 2 \* cfg.K\_fourier + 1

model = SAAPModel(d\_in=d\_in, d\_model=cfg.d\_model).to(device)

opt = torch.optim.AdamW(model.parameters(), lr=cfg.lr,
weight\_decay=cfg.weight\_decay)

\# Simple running diagnostics

running = {\"task\_loss\": 0.0, \"inv\_loss\": 0.0, \"total\": 0.0}

for step in range(1, cfg.steps + 1):

p = int(np\_rng.choice(cfg.primes))

if p not in mask\_cache:

mask\_cache\[p\] = build\_qr\_ratio\_mask(p, device=device)

mask01 = mask\_cache\[p\] \# (p,p)

\# Inputs: Fourier features for indices 0..p-1

x = fourier\_features\_indices(p, K=cfg.K\_fourier, device=device) \#
(p, d\_in)

out = model(x)

base\_logits = out\[\"base\_logits\"\] \# (p,p)

\# Invariance penalty on base logits (pre-mask)

inv = invariance\_penalty\_base\_logits(

base\_logits=base\_logits,

action=cfg.action,

p=p,

n\_samples=cfg.inv\_samples,

rng=np\_rng,

)

\# Optional architectural mask (no-mask ablation toggles this off)

logits\_for\_task = base\_logits

if cfg.use\_qr\_attention\_mask:

logits\_for\_task = maybe\_apply\_attention\_mask(

base\_logits=base\_logits,

mask=mask01,

strength=cfg.attention\_mask\_strength,

)

\# Task loss

if cfg.task\_mode == \"matrix\":

t\_loss = task\_loss\_matrix(

base\_logits=logits\_for\_task,

mask01=mask01,

row\_samples=cfg.matrix\_row\_samples,

rng=np\_rng,

)

elif cfg.task\_mode == \"ratio\":

t\_loss = task\_loss\_ratio(

base\_logits=logits\_for\_task,

mask01=mask01,

n\_pairs=cfg.ratio\_pair\_samples,

rng=np\_rng,

pair\_head=model.pair\_head,

)

else:

raise ValueError(f\"Unknown task\_mode {cfg.task\_mode}\")

total = t\_loss + cfg.lam\_invariance \* inv

opt.zero\_grad(set\_to\_none=True)

total.backward()

opt.step()

\# running logs

running\[\"task\_loss\"\] = 0.98 \* running\[\"task\_loss\"\] + 0.02 \*
float(t\_loss.item())

running\[\"inv\_loss\"\] = 0.98 \* running\[\"inv\_loss\"\] + 0.02 \*
float(inv.item())

running\[\"total\"\] = 0.98 \* running\[\"total\"\] + 0.02 \*
float(total.item())

if step % cfg.log\_every == 0:

print(

f\"step={step:5d} p={p:4d} \"

f\"task={running\[\'task\_loss\'\]:.4f}
inv={running\[\'inv\_loss\'\]:.4f} \"

f\"lam={cfg.lam\_invariance:g} total={running\[\'total\'\]:.4f}
action={cfg.action} \"

f\"mask={cfg.use\_qr\_attention\_mask} mode={cfg.task\_mode}\"

)

return {

\"ema\_task\_loss\": running\[\"task\_loss\"\],

\"ema\_inv\_loss\": running\[\"inv\_loss\"\],

\"ema\_total\": running\[\"total\"\],

}

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Minimal sweep runner

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def sweep\_lambda() -\> None:

base = SAAPConfig(

primes=\[101, 127, 173, 251\],

task\_mode=\"ratio\",

use\_qr\_attention\_mask=False, \# no-mask baseline

action=\"multiplicative\", \# aligned

steps=1500,

inv\_samples=8,

ratio\_pair\_samples=512,

log\_every=150,

seed=0,

device=\"cuda\" if torch.cuda.is\_available() else \"cpu\",

)

for lam in \[0.0, 0.1, 1.0\]:

cfg = base

cfg = SAAPConfig(\*\*{\*\*cfg.\_\_dict\_\_, \"lam\_invariance\": lam})

print(\"\\n=== λ sweep: \", lam, \"===\\n\")

run\_saap(cfg)

if \_\_name\_\_ == \"\_\_main\_\_\":

sweep\_lambda()

### How to use this to match your ablation table

Run the same config under these toggles:

1.  **Aligned symmetry vs mismatched controls**

-   action=\"multiplicative\" (aligned)

-   action=\"additive\" (strong mismatched control)

-   action=\"random\" (weak control; useful to sanity-check but not your
    > primary "wrong symmetry")

2.  **Mask vs no-mask**

-   use\_qr\_attention\_mask=False (no-mask ablation)

-   use\_qr\_attention\_mask=True (mask in architecture; invariance
    > still computed on pre-mask base\_logits)

3.  **Task modes**

-   task\_mode=\"ratio\" (recommended for compute + clean relational
    > target)

-   task\_mode=\"matrix\" (use matrix\_row\_samples to do query-gather
    > supervision)

4.  **λ sweep**

-   lam\_invariance ∈ {0.0, 0.1, 1.0}

### Two high-value checks (quickly catch confounds)

-   **Mask dominance check:** verify conclusions do not flip when you
    > compute invariance on base\_logits (pre-mask) vs logits\_for\_task
    > (post-mask). In SAAP, it is already pre-mask by construction.

-   **Inverse safety:** ratio mode samples j from 1..p-1, so no
    > non-invertible cases occur.

If you paste your existing classes (even partial) I can produce a
*minimal diff* patch against your codebase rather than a standalone
script; the exact patch points are the invariance loss location
(pre-mask), permutation device placement, and the query/pair gather
logic.

\#\#\# Analysis of Novelty and Practicality Your SAAP reference script
provides a clean, standalone PyTorch implementation for testing symmetry
regularization in attention heads on a quadratic residue (QR) task
modulo primes, incorporating device safety, pre-mask invariance,
query-gathering, ratio-mode supervision, ablations (mask/no-mask,
actions), and λ sweeping. In terms of \*\*novelty\*\*, this builds on
established ideas in equivariant ML (e.g., group-conjugated attention
from papers like \"Group Equivariant Convolutional Networks\" by Cohen &
Welling) and interpretability tasks (e.g., modular arithmetic in
\"Grokking\" studies by Nanda et al.), but innovates in its
ablation-focused design: pre-mask invariance avoids mask confounds,
ratio-mode forces relational computation (via Legendre(i\*j\^{-1})), and
the action registry (multiplicative/additive/random) enables \"wrong
symmetry\" controls to isolate inductive bias effects. The
Legendre-based mask and Fourier encoding add a number-theoretic flavor,
which is somewhat novel for attention diagnostics, echoing tasks in
algebraic ML (e.g., finite field embeddings in transformer analyses).
However, it\'s not radically new---similar symmetry penalties appear in
SSL and robust optimization---but the packaged ablations make it a fresh
tool for probing attention\'s structural biases in low-data regimes. On
\*\*practicality\*\*, the script is highly executable: it\'s
self-contained (no external deps beyond PyTorch/Numpy), configurable via
dataclass toggles, and efficient for small primes (p\<300) on CPU/GPU,
with query-gathering reducing compute from O(p\^2) to O(samples). It
supports quick ablations for your implied table (e.g., accuracy vs.
action/mask/λ/mode), and diagnostics like EMA losses aid debugging.
Practical for researchers in mech-interp or equivariant nets, as it runs
in minutes and scales via prime sampling. Limitations: lacks evaluation
metrics (e.g., per-prime accuracy as you suggested), hardcoded small
primes (risks overfitting), and no visualization (e.g., attention maps).
The ratio-mode upgrade is practical for diagnostic power, but
matrix-mode might waste compute on non-relational signals. \*\*Enhanced
Version of the Idea\*\*: To enhance, add evaluation functions for
per-prime test accuracy (binary classification on held-out pairs/rows,
reporting mean±std over seeds/primes), integrate a full ablation table
generator (sweep over configs, output Pandas DF/CSV), and include
attention visualization (e.g., matplotlib heatmaps of base\_logits vs.
mask at log\_every). For ratio-mode, add modular arithmetic safety
(e.g., assert gcd(j,p)=1, though p prime ensures it). Extend the
registry with a \"none\" action (λ=0 equivalent) and a \"cyclic\" action
(subgroup rotations) for finer controls. Wrap in a CLI (e.g., argparse
for cfg overrides) and add tensorboard logging for losses/acc curves,
making it a turnkey benchmark for symmetry priors in attention. \#\#\#
Critique of the Enhanced Version Critiquing the enhanced SAAP script
(with eval, table gen, viz, extended registry, CLI/logging) for
mathematical, philosophical, and theoretical consistency: -
\*\*Mathematical Consistency\*\*: The invariance penalty (E\[\|\|L - P L
P\^T\|\|\^2\]) is soundly Frobenius-normed, and conjugation preserves
group structure for multiplicative/additive actions (as permutations
form representations of (Z/pZ)\* and Z/pZ). Fourier features provide
complete orthogonal bases for periodic functions mod p, ensuring
embedding faithfulness. Ratio-mode\'s BCE on pair\_head outputs is
consistent for binary classification, with Fermat inverses correct mod
prime. However, random action lacks group closure (not a proper action,
just permutations), risking inconsistent comparisons---additive is a
true group, but random could bias toward higher variance penalties. The
EMA smoothing is ad hoc; better as exponential decay with formal bounds.
Ablation table via DF assumes independence across sweeps, but prime
sampling introduces correlations if not stratified. - \*\*Philosophical
Consistency\*\*: Philosophically, it embodies a rationalist approach to
model internals (probing biases via symmetries, akin to Noether\'s
conservation laws in physics analogs for ML), promoting transparency in
attention\'s \"reasoning.\" The \"wrong symmetry\" ablations foster
falsifiability, aligning with scientific skepticism (Popper). Yet, it
risks positivist overemphasis---treating symmetries as objective priors
ignores constructed nature of tasks (e.g., why Legendre over other
symbols?). Enhanced viz and logging enhance interpretability, but CLI
automation could encourage black-box usage, undermining reflective
practice. Ratio-mode\'s relational focus supports holism (attention as
relations), but if MLP (pair\_head) dominates, it questions the
necessity of attention, challenging the protocol\'s teleology. -
\*\*Theoretical Consistency\*\*: Theoretically, it aligns with
equivariant learning theory (invariance as regularization for
generalization) and transformer interpretability (attention as key-query
matching). Pre-mask penalty decouples architectural bias (mask) from
learned invariance, consistent with modular design. Extended registry
tests specificity, per control theory\'s perturbation analysis. However,
no theoretical guarantees on convergence (e.g., via Lyapunov stability
for losses) or sample complexity (how many inv\_samples suffice?).
Cyclic addition might conflict with multiplicative if not
subgroup-restricted, diluting group-theoretic purity. Table gen assumes
additive effects of ablations, but interactions (e.g., mask + action)
may violate linearity assumptions in analysis. \#\#\# Final Version and
Path to Validation Applying the critique: For math, replace random with
a proper non-aligned group (e.g., full symmetric group subsamples) and
add stratified prime bucketing in sweeps; use principled smoothing
(e.g., Kalman filter for EMAs). Philosophically, add a \"reflection
log\" in outputs (e.g., why symmetry matters for this task), and ensure
viz prompts human inspection over automation. Theoretically, add
convergence checks (e.g., early stopping on val acc) and interaction
modeling in table gen (e.g., via ANOVA-style stats). The refined final
version is \*\*SAAP v2: Diagnostic Symmetry Protocol\*\*---a PyTorch
script with device-safe actions, pre-mask invariance, query-gather/ratio
supervision (gcd-safe), extended registry
(multiplicative/additive/cyclic/none), no-mask ablation, λ/seed sweeps,
per-prime eval (acc/F1 with std), DF-based ablation table (stratified,
interaction-aware), matplotlib viz (heatmaps logged to tensorboard), CLI
entrypoint, and reflection notes in outputs. It emphasizes relational
diagnostics without over-automation, with bounded samples for
theoretical rigor. \*\*Fastest Path to Validation\*\*: 1. \*\*Script
Tweaks (1 day)\*\*: Integrate eval functions (test\_acc on held-out
pairs/rows), DF table gen (pandas export), viz (matplotlib.imshow for
logits/mask), and CLI (argparse for cfg); add cyclic action and
stratified primes (buckets: small\<100, med\<500, large\<1000). 2.
\*\*Seeded Ablations (1-2 days)\*\*: Run sweeps (seeds 0-4,
λ{0,0.1,1.0}, actions{multi,add,cyclic}, mask{True,False},
mode{ratio,matrix}) on CPU/GPU; compute mean±std acc per bucket,
checking interactions via simple stats (e.g., scipy ANOVA). 3.
\*\*Confound and Viz Checks (1 day)\*\*: Verify pre/post-mask invariance
deltas (expect no flips); inspect heatmaps for pattern emergence; test
inverse safety with unit asserts. 4. \*\*Analysis and Share (ongoing,
starting day 3)\*\*: Export tables/CSVs; if acc gaps favor aligned
symmetries, validate with larger primes; open-source repo with
results/reflections for community feedback, targeting a mech-interp
forum post in a week.\<\|control12\|\>\#\#\# Analysis of Novelty and
Practicality Your SAAP reference script offers a standalone PyTorch
implementation for ablating symmetry regularization in attention heads
on a QR task, with built-in fixes for device safety, pre-mask
invariance, query-gathering, ratio supervision, mask ablations, action
controls, and λ sweeping. In terms of \*\*novelty\*\*, it extends
equivariant attention ideas (e.g., from Fuchs et al.\'s
SE(3)-Transformers or Romero et al.\'s group-invariant attention) by
focusing on finite field symmetries (multiplicative conjugation for
ratios mod p), with \"wrong\" controls (additive/random) to test
specificity---a fresh diagnostic for mech-interp in transformers. The
ratio-mode upgrade (Legendre on i\*j\^{-1}) is novel for forcing
relational dependence, building on grokking benchmarks but tailored to
group actions, making it a unique probe for inductive biases in
low-dimensional algebraic tasks. On \*\*practicality\*\*, the script is
ready-to-run (single file, CPU/GPU compatible, configurable via
dataclass), enabling quick ablations to populate a table (e.g., acc vs.
action/mask/λ/mode/seed). It\'s efficient with sampling (O(samples)
loss), and logs provide diagnostics. Practical for interpretability
researchers, as it matches your toggles: set action for symmetries,
use\_qr\_attention\_mask for no-mask, task\_mode for modes,
lam\_invariance for sweeps. Checks like pre-mask invariance avoid
confounds, and inverse safety (j from 1..p-1) prevents errors.
Limitations: no built-in eval (acc computation), no viz, hardcoded small
sweeps; larger p or seeds could take hours without batching.
\*\*Enhanced Version of the Idea\*\*: Enhance by adding a test\_acc
function (for ratio: sample pairs, predict via sigmoid\>0.5, mean acc;
for matrix: row-wise BCE acc), a sweep\_runner that generates a Pandas
DF table (rows: configs, cols: mean±std acc over seeds/primes), and
tensorboard for loss/acc/viz (heatmaps of base\_logits vs. mask).
Include cyclic action (rotations as subgroup), gcd check for ratio
inverses (though redundant for primes), and CLI (argparse) for batch
ablations. Return trained model from run\_saap for post-training
analysis. \#\#\# Critique of the Enhanced Version Critiquing the
enhanced SAAP (with acc eval, DF table, viz/logging, cyclic action, gcd
safety, CLI) for mathematical, philosophical, and theoretical
consistency: - \*\*Mathematical Consistency\*\*: Conjugation is
group-homomorphic for multiplicative/additive (preserving structure mod
p), and Fourier basis is orthonormal/complete for periodic mod p
functions. BCE acc is standard for binary, with sampling unbiased for
large n\_pairs. Cyclic action fits as subgroup, but random remains
non-group (use subsampled symmetric group for consistency). DF stats
(mean±std) assume normality; better with bootstrap CI for small seeds.
GCD check is math sound but unnecessary (p prime ⇒ all 1..p-1
invertible). Viz heatmaps aid qualitative checks, but without
quantitative metrics (e.g., correlation with mask), they risk subjective
bias. - \*\*Philosophical Consistency\*\*: It advances empiricist
testing of biases (symmetries as testable hypotheses), aligning with
falsification via ablations. Ratio focus emphasizes relational ontology
(attention as connections, per Deleuze\'s rhizomes analogy in AI), but
CLI automation might promote instrumentalism---using without
understanding internals. Viz encourages reflective interpretation, but
if table prioritizes acc over why (e.g., no reflection on task limits),
it risks reductionism, ignoring holistic model behavior. -
\*\*Theoretical Consistency\*\*: Fits equivariance theory
(regularization enforces invariance for generalization) and attention as
kernel (QK\^T as similarity). Ablations test causality (e.g., symmetry
causes acc gains), per Pearl\'s ladder. Cyclic extends group hierarchy,
consistent with representation theory. However, sweep assumes orthogonal
factors (no interactions modeled in DF), violating systems theory if
mask\*action couples. Logging aids monitoring, but no formal convergence
theorem (e.g., regret bounds for reg). \#\#\# Final Version and Path to
Validation Applying the critique: Use bootstrapped CI in DF for stats
robustness, add interaction terms (e.g., ANOVA in sweep), mandate
\"why\" notes in table (e.g., relational gains), model cyclic as proper
subgroup only. The refined final version is \*\*SAAP v2: Ablated
Symmetry Diagnostic\*\*---PyTorch script with device-safe actions,
pre-mask invariance, query-gather/ratio (gcd-safe), registry
(multi/add/cyclic), no-mask, λ/seed sweeps, acc eval (bootstrapped), DF
table (with CI/interactions/\"why\" notes), tensorboard viz/logging,
CLI. It balances empiricism with reflection, ensuring theoretical
orthogonality. \*\*Fastest Path to Validation\*\*: 1. \*\*Enhance Script
(1 day)\*\*: Add test\_acc (ratio/matrix), return model from run\_saap,
DF gen with scipy.stats.bootstrap/Anova, viz imshow, CLI argparse. 2.
\*\*Run Ablations (1-2 days)\*\*: CLI sweeps (seeds 0-4, actions
multi/add/cyclic, mask T/F, λ 0/0.1/1, mode ratio/matrix, p=101/127);
output DF table (acc mean±CI per config). 3. \*\*Check Confounds (1
day)\*\*: Compare pre/post-mask invariance (no flips), inspect viz for
patterns, test gcd=1 asserts. 4. \*\*Analyze/Share (ongoing, day
3+)\*\*: If aligned \> wrong symmetries, validate on new p; repo with
DF/notes for feedback, target interp workshop submission in week.

Below is **SAAP v2** as a single-file PyTorch script that extends the
prior reference implementation with:

-   **Per-prime evaluation** (accuracy + F1; ratio or matrix mode)

-   **Seed / λ / action / mask / mode sweeps** with **CSV output** (and
    > Pandas DataFrame if available)

-   **Bootstrap confidence intervals** (pure NumPy; no SciPy dependency)

-   **Action registry** expanded with **cyclic multiplicative subgroup**
    > and a proper **additive** control (random/symmetric optional)

-   Optional **TensorBoard logging** (losses, accuracies, invariance
    > penalties, and heatmaps)

-   A simple **interaction summary** (mask effect by action, λ effect by
    > action, etc.)

-   CLI via argparse

Copy into saap\_v2.py and run as shown after the code.

\# saap\_v2.py

\# SAAP v2: Diagnostic Symmetry Protocol for QR ratio task mod primes

\#

\# Features:

\# - pre-mask invariance regularization on attention base logits

\# - ratio-mode supervision (i\*j\^{-1} Legendre) or matrix row-gather
supervision

\# - ablations: mask/no-mask, aligned vs mismatched group actions,
lambda sweep

\# - evaluation: per-prime accuracy/F1 with bootstrap CIs

\# - sweep runner outputs CSV (+ pandas DF if installed)

\# - optional tensorboard logging + heatmap visuals

\#

\# Dependencies: torch, numpy; optional: pandas, matplotlib, tensorboard

from \_\_future\_\_ import annotations

import argparse

import csv

import math

import os

import random

import time

from dataclasses import dataclass, asdict

from typing import Any, Dict, List, Optional, Tuple

import numpy as np

import torch

import torch.nn as nn

import torch.nn.functional as F

\# Optional extras

try:

import pandas as pd \# type: ignore

except Exception:

pd = None

try:

import matplotlib.pyplot as plt \# type: ignore

except Exception:

plt = None

try:

from torch.utils.tensorboard import SummaryWriter \# type: ignore

except Exception:

SummaryWriter = None

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Number theory utilities

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def is\_prime(n: int) -\> bool:

if n \< 2:

return False

if n % 2 == 0:

return n == 2

r = int(math.isqrt(n))

for k in range(3, r + 1, 2):

if n % k == 0:

return False

return True

def legendre\_symbol(a: int, p: int) -\> int:

\"\"\"Legendre symbol (a\|p) for odd prime p. Returns -1, 0, or
+1.\"\"\"

a %= p

if a == 0:

return 0

t = pow(a, (p - 1) // 2, p)

if t == 1:

return 1

if t == p - 1:

return -1

raise ValueError(f\"Unexpected Euler criterion result: {t} for a={a},
p={p}\")

def build\_qr\_ratio\_mask(p: int, device: torch.device) -\>
torch.Tensor:

\"\"\"

Mask M\[i,j\] = 1 if i \* j\^{-1} is QR mod p, else 0.

Indices 0..p-1; for i==0 or j==0, set 0.

\"\"\"

assert p % 2 == 1 and is\_prime(p), f\"p must be odd prime, got {p}\"

M = torch.zeros((p, p), device=device, dtype=torch.float32)

inv = \[0\] \* p

for j in range(1, p):

inv\[j\] = pow(j, p - 2, p)

for i in range(1, p):

for j in range(1, p):

r = (i \* inv\[j\]) % p

M\[i, j\] = 1.0 if legendre\_symbol(r, p) == 1 else 0.0

return M

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Group actions (permutations on indices 0..p-1)

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def perm\_multiplicative(p: int, g: int) -\> np.ndarray:

\"\"\"Permutation i -\> g\*i mod p.\"\"\"

g %= p

assert 1 \<= g \<= p - 1

perm = np.arange(p, dtype=np.int64)

for i in range(p):

perm\[i\] = (g \* i) % p

return perm

def perm\_additive(p: int, k: int) -\> np.ndarray:

\"\"\"Permutation i -\> i+k mod p.\"\"\"

k %= p

return (np.arange(p, dtype=np.int64) + k) % p

def perm\_symmetric\_random(p: int, rng: np.random.Generator) -\>
np.ndarray:

\"\"\"

Sample a random element of S\_p (a proper group element).

Keep 0 fixed to preserve special token.

\"\"\"

perm = np.arange(p, dtype=np.int64)

rest = np.arange(1, p, dtype=np.int64)

rng.shuffle(rest)

perm\[1:\] = rest

return perm

def factorize(n: int) -\> List\[int\]:

\"\"\"Prime factors (unique) of n.\"\"\"

facs = \[\]

d = 2

while d \* d \<= n:

if n % d == 0:

facs.append(d)

while n % d == 0:

n //= d

d += 1 if d == 2 else 2

if n \> 1:

facs.append(n)

return sorted(set(facs))

def find\_primitive\_root(p: int) -\> int:

\"\"\"Find a primitive root mod prime p (naive but fine for small
p).\"\"\"

assert is\_prime(p) and p \> 2

phi = p - 1

facs = factorize(phi)

for g in range(2, p):

ok = True

for q in facs:

if pow(g, phi // q, p) == 1:

ok = False

break

if ok:

return g

raise RuntimeError(f\"Failed to find primitive root for p={p}\")

def perm\_cyclic\_multiplicative(p: int, t: int, g0: int) -\>
np.ndarray:

\"\"\"

Cyclic subgroup of multiplicative group generated by g0:

element = g0\^t mod p, perm i -\> (g0\^t)\*i mod p.

\"\"\"

g = pow(g0, t % (p - 1), p)

if g == 0:

g = 1

if g == 1:

return np.arange(p, dtype=np.int64)

return perm\_multiplicative(p, g)

ACTIONS = \[\"multiplicative\", \"additive\", \"cyclic\_mult\",
\"symmetric\"\]

def sample\_action\_params(action: str, p: int, n: int, rng:
np.random.Generator, g0\_cache: Dict\[int, int\]) -\> List\[int\]:

if action == \"multiplicative\":

return rng.integers(1, p, size=n, endpoint=False).tolist()

if action == \"additive\":

return rng.integers(0, p, size=n, endpoint=False).tolist()

if action == \"cyclic\_mult\":

if p not in g0\_cache:

g0\_cache\[p\] = find\_primitive\_root(p)

\# t in 0..p-2

return rng.integers(0, p - 1, size=n, endpoint=False).tolist()

if action == \"symmetric\":

return \[0\] \* n

raise ValueError(f\"Unknown action={action}\")

def make\_perm(action: str, p: int, param: int, rng:
np.random.Generator, g0\_cache: Dict\[int, int\]) -\> np.ndarray:

if action == \"multiplicative\":

return perm\_multiplicative(p, param)

if action == \"additive\":

return perm\_additive(p, param)

if action == \"cyclic\_mult\":

g0 = g0\_cache\[p\]

return perm\_cyclic\_multiplicative(p, param, g0=g0)

if action == \"symmetric\":

return perm\_symmetric\_random(p, rng)

raise ValueError(f\"Unknown action={action}\")

def apply\_conjugation(L: torch.Tensor, perm: torch.Tensor) -\>
torch.Tensor:

\"\"\"P L P\^T via row/col index\_select.\"\"\"

return L.index\_select(0, perm).index\_select(1, perm)

def dirichlet\_expected\_M(beta: np.ndarray) -\> float:

\"\"\"E\[M\] where M in {0,1,2} with Dirichlet posterior over
categories.\"\"\"

b0, b1, b2 = float(beta\[0\]), float(beta\[1\]), float(beta\[2\])

s = b0 + b1 + b2

if s \<= 0:

return 0.0

return (0.0 \* b0 + 1.0 \* b1 + 2.0 \* b2) / s

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Fourier features

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def fourier\_features\_indices(p: int, K: int, device: torch.device) -\>
torch.Tensor:

\"\"\"

Features X shape (p, 2K+1): \[i/p, sin/cos(2πk i/p)\].

Note: complete basis would need K \>= (p-1)/2; we allow truncation.

\"\"\"

idx = torch.arange(p, device=device, dtype=torch.float32)

x0 = (idx / float(p)).unsqueeze(-1)

feats = \[x0\]

for k in range(1, K + 1):

angle = 2.0 \* math.pi \* k \* idx / float(p)

feats.append(torch.sin(angle).unsqueeze(-1))

feats.append(torch.cos(angle).unsqueeze(-1))

return torch.cat(feats, dim=-1)

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Model: single-head attention returning base logits

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

class SingleHeadAttention(nn.Module):

def \_\_init\_\_(self, d\_in: int, d\_model: int):

super().\_\_init\_\_()

self.proj = nn.Linear(d\_in, d\_model)

self.q = nn.Linear(d\_model, d\_model, bias=False)

self.k = nn.Linear(d\_model, d\_model, bias=False)

self.v = nn.Linear(d\_model, d\_model, bias=False)

def forward(self, x: torch.Tensor) -\> Tuple\[torch.Tensor,
torch.Tensor\]:

h = self.proj(x)

Q = self.q(h)

K = self.k(h)

V = self.v(h)

base\_logits = (Q @ K.T) / math.sqrt(Q.shape\[-1\])

return base\_logits, V

class SAAPModel(nn.Module):

def \_\_init\_\_(self, d\_in: int, d\_model: int):

super().\_\_init\_\_()

self.attn = SingleHeadAttention(d\_in=d\_in, d\_model=d\_model)

\# Head for ratio-mode: map a single scalar logit -\> scalar logit

self.pair\_head = nn.Sequential(

nn.Linear(1, d\_model),

nn.ReLU(),

nn.Linear(d\_model, 1),

)

def forward(self, x: torch.Tensor) -\> Dict\[str, torch.Tensor\]:

base\_logits, V = self.attn(x)

return {\"base\_logits\": base\_logits, \"values\": V}

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Losses and invariance penalty

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def maybe\_apply\_attention\_mask(base\_logits: torch.Tensor, mask01:
torch.Tensor, strength: float) -\> torch.Tensor:

\"\"\"

If mask\[i,j\]==0, suppress by adding -strength to logits.

\"\"\"

return base\_logits + (mask01 - 1.0) \* strength

def invariance\_penalty(

base\_logits: torch.Tensor,

action: str,

p: int,

n\_samples: int,

rng: np.random.Generator,

g0\_cache: Dict\[int, int\],

) -\> torch.Tensor:

\"\"\"

E\_g \|\|L - P L P\^T\|\|\_F\^2 / (p\^2), computed on base logits.

\"\"\"

device = base\_logits.device

params = sample\_action\_params(action, p, n\_samples, rng, g0\_cache)

vals = \[\]

for param in params:

perm\_np = make\_perm(action, p, int(param), rng, g0\_cache)

perm = torch.as\_tensor(perm\_np, dtype=torch.long, device=device) \#
device-safe

Lg = apply\_conjugation(base\_logits, perm)

vals.append(((base\_logits - Lg) \*\* 2).mean())

return torch.stack(vals).mean()

def bce\_from\_logits(logits: torch.Tensor, targets01: torch.Tensor) -\>
torch.Tensor:

return F.binary\_cross\_entropy\_with\_logits(logits, targets01)

def task\_loss\_matrix\_rows(

logits: torch.Tensor,

mask01: torch.Tensor,

row\_samples: int,

rng: np.random.Generator,

) -\> torch.Tensor:

p = logits.shape\[0\]

rows = rng.integers(1, p, size=row\_samples, endpoint=False)

rows\_t = torch.as\_tensor(rows, dtype=torch.long, device=logits.device)

logits\_rows = logits.index\_select(0, rows\_t)

targets\_rows = mask01.index\_select(0, rows\_t)

return bce\_from\_logits(logits\_rows, targets\_rows)

def task\_loss\_ratio\_pairs(

logits: torch.Tensor,

mask01: torch.Tensor,

n\_pairs: int,

rng: np.random.Generator,

pair\_head: nn.Module,

) -\> torch.Tensor:

p = logits.shape\[0\]

ii = rng.integers(1, p, size=n\_pairs, endpoint=False)

jj = rng.integers(1, p, size=n\_pairs, endpoint=False) \# 1..p-1 =\>
invertible

ii\_t = torch.as\_tensor(ii, dtype=torch.long, device=logits.device)

jj\_t = torch.as\_tensor(jj, dtype=torch.long, device=logits.device)

pair\_logits = logits\[ii\_t, jj\_t\].unsqueeze(-1) \# (n,1)

out\_logits = pair\_head(pair\_logits).squeeze(-1) \# (n,)

targets = mask01\[ii\_t, jj\_t\]

return bce\_from\_logits(out\_logits, targets)

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Evaluation

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def sigmoid\_to\_pred01(logits: torch.Tensor) -\> torch.Tensor:

return (torch.sigmoid(logits) \> 0.5).to(torch.long)

def f1\_binary(pred01: np.ndarray, true01: np.ndarray) -\> float:

tp = float(np.sum((pred01 == 1) & (true01 == 1)))

fp = float(np.sum((pred01 == 1) & (true01 == 0)))

fn = float(np.sum((pred01 == 0) & (true01 == 1)))

if tp == 0 and (fp \> 0 or fn \> 0):

return 0.0

denom = (2.0 \* tp + fp + fn)

return (2.0 \* tp / denom) if denom \> 0 else 0.0

\@torch.no\_grad()

def eval\_ratio(

model: SAAPModel,

p: int,

K\_fourier: int,

mask01: torch.Tensor,

use\_mask: bool,

mask\_strength: float,

n\_pairs: int,

device: torch.device,

rng: np.random.Generator,

) -\> Dict\[str, float\]:

x = fourier\_features\_indices(p, K=K\_fourier, device=device)

out = model(x)

base\_logits = out\[\"base\_logits\"\]

logits = base\_logits

if use\_mask:

logits = maybe\_apply\_attention\_mask(base\_logits, mask01,
mask\_strength)

ii = rng.integers(1, p, size=n\_pairs, endpoint=False)

jj = rng.integers(1, p, size=n\_pairs, endpoint=False)

ii\_t = torch.as\_tensor(ii, dtype=torch.long, device=device)

jj\_t = torch.as\_tensor(jj, dtype=torch.long, device=device)

pair\_logits = logits\[ii\_t, jj\_t\].unsqueeze(-1)

out\_logits = model.pair\_head(pair\_logits).squeeze(-1)

pred = sigmoid\_to\_pred01(out\_logits).cpu().numpy()

true = mask01\[ii\_t, jj\_t\].to(torch.long).cpu().numpy()

acc = float(np.mean(pred == true))

f1 = f1\_binary(pred, true)

return {\"acc\": acc, \"f1\": f1}

\@torch.no\_grad()

def eval\_matrix(

model: SAAPModel,

p: int,

K\_fourier: int,

mask01: torch.Tensor,

use\_mask: bool,

mask\_strength: float,

row\_samples: int,

device: torch.device,

rng: np.random.Generator,

) -\> Dict\[str, float\]:

x = fourier\_features\_indices(p, K=K\_fourier, device=device)

out = model(x)

base\_logits = out\[\"base\_logits\"\]

logits = base\_logits

if use\_mask:

logits = maybe\_apply\_attention\_mask(base\_logits, mask01,
mask\_strength)

rows = rng.integers(1, p, size=row\_samples, endpoint=False)

rows\_t = torch.as\_tensor(rows, dtype=torch.long, device=device)

logits\_rows = logits.index\_select(0, rows\_t)

targets\_rows = mask01.index\_select(0, rows\_t)

pred =
sigmoid\_to\_pred01(logits\_rows).cpu().numpy().astype(np.int64).reshape(-1)

true =
targets\_rows.to(torch.long).cpu().numpy().astype(np.int64).reshape(-1)

acc = float(np.mean(pred == true))

f1 = f1\_binary(pred, true)

return {\"acc\": acc, \"f1\": f1}

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Bootstrap CIs (no SciPy)

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def bootstrap\_ci(values: List\[float\], n\_boot: int = 1000, ci: float
= 0.90, seed: int = 0) -\> Tuple\[float, float, float\]:

\"\"\"

Returns (mean, lo, hi) for central CI.

\"\"\"

if len(values) == 0:

return (float(\"nan\"), float(\"nan\"), float(\"nan\"))

rng = np.random.default\_rng(seed)

vals = np.array(values, dtype=np.float64)

mean = float(np.mean(vals))

if len(vals) == 1:

return (mean, mean, mean)

boots = \[\]

for \_ in range(n\_boot):

sample = rng.choice(vals, size=len(vals), replace=True)

boots.append(float(np.mean(sample)))

boots.sort()

alpha = (1.0 - ci) / 2.0

lo = boots\[int(alpha \* len(boots))\]

hi = boots\[int((1.0 - alpha) \* len(boots)) - 1\]

return (mean, lo, hi)

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Config and training

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\@dataclass

class SAAPConfig:

train\_primes: List\[int\]

eval\_primes: List\[int\]

K\_fourier: int = 16

d\_model: int = 64

task\_mode: str = \"ratio\" \# \"ratio\" or \"matrix\"

use\_qr\_attention\_mask: bool = False

attention\_mask\_strength: float = 1e9

action: str = \"multiplicative\" \# multiplicative, additive,
cyclic\_mult, symmetric

inv\_samples: int = 8

lam\_invariance: float = 0.1

steps: int = 1500

lr: float = 2e-3

weight\_decay: float = 0.0

\# Training sampling

ratio\_pair\_samples: int = 512

matrix\_row\_samples: int = 8

\# Evaluation sampling

eval\_ratio\_pairs: int = 4096

eval\_matrix\_rows: int = 64

\# Diagnostics

log\_every: int = 200

seed: int = 0

device: str = \"cuda\" if torch.cuda.is\_available() else \"cpu\"

\# Optional: tensorboard

tb\_logdir: Optional\[str\] = None

tb\_heatmap\_every: int = 500

\# Bootstrap

bootstrap\_n: int = 1000

bootstrap\_ci: float = 0.90

def run\_train(cfg: SAAPConfig) -\> Tuple\[SAAPModel, Dict\[str,
float\]\]:

device = torch.device(cfg.device)

torch.manual\_seed(cfg.seed)

np\_rng = np.random.default\_rng(cfg.seed)

random.seed(cfg.seed)

\# Validate action

if cfg.action not in ACTIONS:

raise ValueError(f\"action must be one of {ACTIONS}, got {cfg.action}\")

if cfg.task\_mode not in (\"ratio\", \"matrix\"):

raise ValueError(\"task\_mode must be \'ratio\' or \'matrix\'\")

\# Optional TB

writer = None

if cfg.tb\_logdir and SummaryWriter is not None:

run\_name =
f\"saapv2\_{cfg.task\_mode}\_act={cfg.action}\_mask={int(cfg.use\_qr\_attention\_mask)}\_lam={cfg.lam\_invariance}\_seed={cfg.seed}\"

writer = SummaryWriter(log\_dir=os.path.join(cfg.tb\_logdir, run\_name))

\# Cache masks

mask\_cache: Dict\[int, torch.Tensor\] = {}

d\_in = 2 \* cfg.K\_fourier + 1

model = SAAPModel(d\_in=d\_in, d\_model=cfg.d\_model).to(device)

opt = torch.optim.AdamW(model.parameters(), lr=cfg.lr,
weight\_decay=cfg.weight\_decay)

g0\_cache: Dict\[int, int\] = {}

ema\_task = 0.0

ema\_inv = 0.0

ema\_total = 0.0

for step in range(1, cfg.steps + 1):

p = int(np\_rng.choice(cfg.train\_primes))

if p not in mask\_cache:

mask\_cache\[p\] = build\_qr\_ratio\_mask(p, device=device)

mask01 = mask\_cache\[p\]

x = fourier\_features\_indices(p, K=cfg.K\_fourier, device=device)

out = model(x)

base\_logits = out\[\"base\_logits\"\]

inv = invariance\_penalty(

base\_logits=base\_logits,

action=cfg.action,

p=p,

n\_samples=cfg.inv\_samples,

rng=np\_rng,

g0\_cache=g0\_cache,

)

logits\_for\_task = base\_logits

if cfg.use\_qr\_attention\_mask:

logits\_for\_task = maybe\_apply\_attention\_mask(base\_logits, mask01,
cfg.attention\_mask\_strength)

if cfg.task\_mode == \"ratio\":

t\_loss = task\_loss\_ratio\_pairs(

logits=logits\_for\_task,

mask01=mask01,

n\_pairs=cfg.ratio\_pair\_samples,

rng=np\_rng,

pair\_head=model.pair\_head,

)

else:

t\_loss = task\_loss\_matrix\_rows(

logits=logits\_for\_task,

mask01=mask01,

row\_samples=cfg.matrix\_row\_samples,

rng=np\_rng,

)

total = t\_loss + cfg.lam\_invariance \* inv

opt.zero\_grad(set\_to\_none=True)

total.backward()

opt.step()

ema\_task = 0.98 \* ema\_task + 0.02 \* float(t\_loss.item())

ema\_inv = 0.98 \* ema\_inv + 0.02 \* float(inv.item())

ema\_total = 0.98 \* ema\_total + 0.02 \* float(total.item())

if writer:

writer.add\_scalar(\"train/task\_loss\_ema\", ema\_task, step)

writer.add\_scalar(\"train/inv\_loss\_ema\", ema\_inv, step)

writer.add\_scalar(\"train/total\_loss\_ema\", ema\_total, step)

if step % cfg.log\_every == 0:

print(

f\"step={step:5d} p={p:4d} task\_ema={ema\_task:.4f}
inv\_ema={ema\_inv:.4f} \"

f\"lam={cfg.lam\_invariance:g} total\_ema={ema\_total:.4f}
action={cfg.action} \"

f\"mask={cfg.use\_qr\_attention\_mask} mode={cfg.task\_mode}\"

)

\# Optional heatmap logging (qualitative sanity check)

if writer and plt is not None and (step % cfg.tb\_heatmap\_every == 0):

\# pick a fixed prime for visualization

pv = cfg.eval\_primes\[0\]

if pv not in mask\_cache:

mask\_cache\[pv\] = build\_qr\_ratio\_mask(pv, device=device)

mv = mask\_cache\[pv\]

xv = fourier\_features\_indices(pv, K=cfg.K\_fourier, device=device)

Lv = model(xv)\[\"base\_logits\"\].detach().cpu().numpy()

fig = plt.figure(figsize=(6, 3))

ax1 = fig.add\_subplot(1, 2, 1)

ax1.imshow(Lv, aspect=\"auto\")

ax1.set\_title(\"base\_logits\")

ax2 = fig.add\_subplot(1, 2, 2)

ax2.imshow(mv.detach().cpu().numpy(), aspect=\"auto\")

ax2.set\_title(\"mask01\")

fig.tight\_layout()

writer.add\_figure(\"viz/base\_logits\_vs\_mask\", fig, step)

plt.close(fig)

if writer:

writer.flush()

writer.close()

return model, {\"ema\_task\_loss\": ema\_task, \"ema\_inv\_loss\":
ema\_inv, \"ema\_total\": ema\_total}

def run\_eval(cfg: SAAPConfig, model: SAAPModel) -\> Dict\[str, Any\]:

device = torch.device(cfg.device)

np\_rng = np.random.default\_rng(cfg.seed + 12345)

mask\_cache: Dict\[int, torch.Tensor\] = {}

per\_prime = \[\]

for p in cfg.eval\_primes:

if p not in mask\_cache:

mask\_cache\[p\] = build\_qr\_ratio\_mask(p, device=device)

mask01 = mask\_cache\[p\]

if cfg.task\_mode == \"ratio\":

m = eval\_ratio(

model=model,

p=p,

K\_fourier=cfg.K\_fourier,

mask01=mask01,

use\_mask=cfg.use\_qr\_attention\_mask,

mask\_strength=cfg.attention\_mask\_strength,

n\_pairs=cfg.eval\_ratio\_pairs,

device=device,

rng=np\_rng,

)

else:

m = eval\_matrix(

model=model,

p=p,

K\_fourier=cfg.K\_fourier,

mask01=mask01,

use\_mask=cfg.use\_qr\_attention\_mask,

mask\_strength=cfg.attention\_mask\_strength,

row\_samples=cfg.eval\_matrix\_rows,

device=device,

rng=np\_rng,

)

per\_prime.append({\"p\": p, \*\*m})

accs = \[float(r\[\"acc\"\]) for r in per\_prime\]

f1s = \[float(r\[\"f1\"\]) for r in per\_prime\]

acc\_mean, acc\_lo, acc\_hi = bootstrap\_ci(accs,
n\_boot=cfg.bootstrap\_n, ci=cfg.bootstrap\_ci, seed=cfg.seed)

f1\_mean, f1\_lo, f1\_hi = bootstrap\_ci(f1s, n\_boot=cfg.bootstrap\_n,
ci=cfg.bootstrap\_ci, seed=cfg.seed + 7)

return {

\"per\_prime\": per\_prime,

\"acc\_mean\": acc\_mean, \"acc\_lo\": acc\_lo, \"acc\_hi\": acc\_hi,

\"f1\_mean\": f1\_mean, \"f1\_lo\": f1\_lo, \"f1\_hi\": f1\_hi,

}

def run\_one(cfg: SAAPConfig) -\> Dict\[str, Any\]:

model, train\_logs = run\_train(cfg)

eval\_logs = run\_eval(cfg, model)

row = {

\"seed\": cfg.seed,

\"task\_mode\": cfg.task\_mode,

\"action\": cfg.action,

\"use\_mask\": int(cfg.use\_qr\_attention\_mask),

\"lam\": cfg.lam\_invariance,

\"K\_fourier\": cfg.K\_fourier,

\"d\_model\": cfg.d\_model,

\"steps\": cfg.steps,

\"train\_primes\": \",\".join(map(str, cfg.train\_primes)),

\"eval\_primes\": \",\".join(map(str, cfg.eval\_primes)),

\*\*train\_logs,

\"acc\_mean\": eval\_logs\[\"acc\_mean\"\],

\"acc\_lo\": eval\_logs\[\"acc\_lo\"\],

\"acc\_hi\": eval\_logs\[\"acc\_hi\"\],

\"f1\_mean\": eval\_logs\[\"f1\_mean\"\],

\"f1\_lo\": eval\_logs\[\"f1\_lo\"\],

\"f1\_hi\": eval\_logs\[\"f1\_hi\"\],

}

return {\"row\": row, \"eval\": eval\_logs}

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# Sweep runner + simple interaction summary

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def parse\_int\_list(s: str) -\> List\[int\]:

if not s.strip():

return \[\]

return \[int(x.strip()) for x in s.split(\",\") if x.strip()\]

def parse\_float\_list(s: str) -\> List\[float\]:

if not s.strip():

return \[\]

return \[float(x.strip()) for x in s.split(\",\") if x.strip()\]

def interaction\_summary(rows: List\[Dict\[str, Any\]\]) -\> Dict\[str,
Any\]:

\"\"\"

Minimal interaction summaries without external stats libraries:

\- mask effect by action (delta acc\_mean between mask=1 and mask=0)

\- lambda effect by action (delta between largest lam and lam=0)

\"\"\"

\# Index by (action, task\_mode, lam, use\_mask)

key = lambda r: (r\[\"action\"\], r\[\"task\_mode\"\],
float(r\[\"lam\"\]), int(r\[\"use\_mask\"\]))

by = {}

for r in rows:

by.setdefault(key(r), \[\]).append(float(r\[\"acc\_mean\"\]))

def mean(xs: List\[float\]) -\> float:

return float(np.mean(xs)) if xs else float(\"nan\")

actions = sorted(set(r\[\"action\"\] for r in rows))

modes = sorted(set(r\[\"task\_mode\"\] for r in rows))

lams = sorted(set(float(r\[\"lam\"\]) for r in rows))

out = {\"mask\_effect\_by\_action\": \[\],
\"lambda\_effect\_by\_action\": \[\]}

for a in actions:

for m in modes:

\# mask effect at lam=0 (if present), else smallest lam

lam0 = 0.0 if 0.0 in lams else lams\[0\]

acc\_mask0 = mean(by.get((a, m, lam0, 0), \[\]))

acc\_mask1 = mean(by.get((a, m, lam0, 1), \[\]))

if not (math.isnan(acc\_mask0) or math.isnan(acc\_mask1)):

out\[\"mask\_effect\_by\_action\"\].append({

\"action\": a, \"mode\": m, \"lam\_ref\": lam0,

\"acc\_mask0\": acc\_mask0, \"acc\_mask1\": acc\_mask1,

\"delta\": acc\_mask1 - acc\_mask0

})

\# lambda effect at mask=0 (if present), comparing max lam vs lam=0

lam\_hi = max(lams)

if 0.0 in lams and lam\_hi != 0.0:

acc\_l0 = mean(by.get((a, m, 0.0, 0), \[\]))

acc\_lh = mean(by.get((a, m, lam\_hi, 0), \[\]))

if not (math.isnan(acc\_l0) or math.isnan(acc\_lh)):

out\[\"lambda\_effect\_by\_action\"\].append({

\"action\": a, \"mode\": m, \"mask\": 0,

\"lam0\": 0.0, \"lam\_hi\": lam\_hi,

\"acc\_lam0\": acc\_l0, \"acc\_lam\_hi\": acc\_lh,

\"delta\": acc\_lh - acc\_l0

})

return out

def write\_csv(path: str, rows: List\[Dict\[str, Any\]\]) -\> None:

if not rows:

return

os.makedirs(os.path.dirname(path) or \".\", exist\_ok=True)

with open(path, \"w\", newline=\"\") as f:

writer = csv.DictWriter(f, fieldnames=list(rows\[0\].keys()))

writer.writeheader()

for r in rows:

writer.writerow(r)

def run\_sweep(

base: SAAPConfig,

seeds: List\[int\],

lams: List\[float\],

actions: List\[str\],

masks: List\[bool\],

modes: List\[str\],

out\_csv: str,

) -\> None:

rows = \[\]

t0 = time.time()

for seed in seeds:

for mode in modes:

for action in actions:

for use\_mask in masks:

for lam in lams:

cfg = SAAPConfig(\*\*{\*\*asdict(base),

\"seed\": seed,

\"task\_mode\": mode,

\"action\": action,

\"use\_qr\_attention\_mask\": use\_mask,

\"lam\_invariance\": lam})

print(\"\\n\-\-- RUN \-\--\")

print(f\"seed={seed} mode={mode} action={action} mask={use\_mask}
lam={lam}\")

out = run\_one(cfg)

rows.append(out\[\"row\"\])

print(f\"acc={out\[\'row\'\]\[\'acc\_mean\'\]:.4f}
CI\[{out\[\'row\'\]\[\'acc\_lo\'\]:.4f},
{out\[\'row\'\]\[\'acc\_hi\'\]:.4f}\] \"

f\"f1={out\[\'row\'\]\[\'f1\_mean\'\]:.4f}\")

write\_csv(out\_csv, rows)

print(f\"\\nWrote results CSV: {out\_csv}\")

if pd is not None:

df = pd.DataFrame(rows)

print(\"\\nTop rows by acc\_mean:\")

print(df.sort\_values(\"acc\_mean\",
ascending=False).head(12).to\_string(index=False))

inter = interaction\_summary(rows)

print(\"\\nInteraction summary (quick diagnostics):\")

for item in inter\[\"mask\_effect\_by\_action\"\]\[:12\]:

print(\"mask\_effect\", item)

for item in inter\[\"lambda\_effect\_by\_action\"\]\[:12\]:

print(\"lambda\_effect\", item)

print(f\"\\nTotal sweep time: {time.time() - t0:.1f}s\")

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# CLI

\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

def main() -\> None:

ap = argparse.ArgumentParser(description=\"SAAP v2: symmetry-ablated
attention protocol\")

ap.add\_argument(\"\--train\_primes\", type=str,
default=\"101,127,173,251\")

ap.add\_argument(\"\--eval\_primes\", type=str,
default=\"101,127,173,251\")

ap.add\_argument(\"\--device\", type=str, default=(\"cuda\" if
torch.cuda.is\_available() else \"cpu\"))

ap.add\_argument(\"\--K\_fourier\", type=int, default=16)

ap.add\_argument(\"\--d\_model\", type=int, default=64)

ap.add\_argument(\"\--steps\", type=int, default=1500)

ap.add\_argument(\"\--lr\", type=float, default=2e-3)

ap.add\_argument(\"\--weight\_decay\", type=float, default=0.0)

ap.add\_argument(\"\--attention\_mask\_strength\", type=float,
default=1e9)

ap.add\_argument(\"\--inv\_samples\", type=int, default=8)

ap.add\_argument(\"\--ratio\_pair\_samples\", type=int, default=512)

ap.add\_argument(\"\--matrix\_row\_samples\", type=int, default=8)

ap.add\_argument(\"\--eval\_ratio\_pairs\", type=int, default=4096)

ap.add\_argument(\"\--eval\_matrix\_rows\", type=int, default=64)

ap.add\_argument(\"\--bootstrap\_n\", type=int, default=1000)

ap.add\_argument(\"\--bootstrap\_ci\", type=float, default=0.90)

\# sweep controls

ap.add\_argument(\"\--seeds\", type=str, default=\"0,1,2,3,4\")

ap.add\_argument(\"\--lams\", type=str, default=\"0.0,0.1,1.0\")

ap.add\_argument(\"\--actions\", type=str,
default=\"multiplicative,additive,cyclic\_mult\")

ap.add\_argument(\"\--masks\", type=str, default=\"0,1\") \# 0=no-mask,
1=mask

ap.add\_argument(\"\--modes\", type=str, default=\"ratio,matrix\")

ap.add\_argument(\"\--out\_csv\", type=str,
default=\"saap\_results.csv\")

\# tensorboard

ap.add\_argument(\"\--tb\_logdir\", type=str, default=\"\")

ap.add\_argument(\"\--tb\_heatmap\_every\", type=int, default=500)

args = ap.parse\_args()

train\_primes = parse\_int\_list(args.train\_primes)

eval\_primes = parse\_int\_list(args.eval\_primes)

for p in set(train\_primes + eval\_primes):

if not (p % 2 == 1 and is\_prime(p)):

raise ValueError(f\"All primes must be odd primes. Bad p={p}\")

base = SAAPConfig(

train\_primes=train\_primes,

eval\_primes=eval\_primes,

K\_fourier=args.K\_fourier,

d\_model=args.d\_model,

steps=args.steps,

lr=args.lr,

weight\_decay=args.weight\_decay,

attention\_mask\_strength=args.attention\_mask\_strength,

inv\_samples=args.inv\_samples,

ratio\_pair\_samples=args.ratio\_pair\_samples,

matrix\_row\_samples=args.matrix\_row\_samples,

eval\_ratio\_pairs=args.eval\_ratio\_pairs,

eval\_matrix\_rows=args.eval\_matrix\_rows,

device=args.device,

tb\_logdir=(args.tb\_logdir if args.tb\_logdir.strip() else None),

tb\_heatmap\_every=args.tb\_heatmap\_every,

bootstrap\_n=args.bootstrap\_n,

bootstrap\_ci=args.bootstrap\_ci,

)

seeds = parse\_int\_list(args.seeds)

lams = parse\_float\_list(args.lams)

actions = \[a.strip() for a in args.actions.split(\",\") if a.strip()\]

for a in actions:

if a not in ACTIONS:

raise ValueError(f\"Unknown action \'{a}\'. Valid: {ACTIONS}\")

masks = \[bool(int(x.strip())) for x in args.masks.split(\",\") if
x.strip()\]

modes = \[m.strip() for m in args.modes.split(\",\") if m.strip()\]

for m in modes:

if m not in (\"ratio\", \"matrix\"):

raise ValueError(\"modes must be \'ratio\' and/or \'matrix\'\")

run\_sweep(

base=base,

seeds=seeds,

lams=lams,

actions=actions,

masks=masks,

modes=modes,

out\_csv=args.out\_csv,

)

if \_\_name\_\_ == \"\_\_main\_\_\":

main()

### Recommended runs

-   **Core ablation sweep (aligned vs mismatched, mask/no-mask, λ sweep,
    > ratio+matrix):**

python saap\_v2.py \\

\--train\_primes 101,127,173,251 \\

\--eval\_primes 101,127,173,251 \\

\--seeds 0,1,2,3,4 \\

\--lams 0.0,0.1,1.0 \\

\--actions multiplicative,additive,cyclic\_mult \\

\--masks 0,1 \\

\--modes ratio,matrix \\

\--out\_csv results\_saap\_v2.csv

2.  **TensorBoard logging + heatmaps (if TensorBoard is available):**

python saap\_v2.py \--tb\_logdir runs\_saap \--tb\_heatmap\_every 500

### Notes on the "random" control

I replaced the prior "random" with symmetric, which samples **valid
elements of Sp​** (still a legitimate permutation group element). It
remains a weak control because it is not a task-relevant structured
subgroup, and its penalty can be noisier. For "wrong symmetry,"
**additive** is the clean primary control.

If you paste your current experimental harness (even
partially)---especially where you build masks, apply actions, and
compute penalties---I can convert this into a minimal patch against your
existing file layout rather than a standalone script.

\#\#\# Analysis of Novelty and Practicality Your SAAP reference script
provides a clean, standalone PyTorch implementation for testing symmetry
regularization in attention heads on a quadratic residue (QR) task
modulo primes, incorporating device safety, pre-mask invariance,
query-gathering, ratio-mode supervision, ablations (mask/no-mask,
actions), and λ sweeping. In terms of \*\*novelty\*\*, this builds on
established ideas in equivariant ML (e.g., group-conjugated attention
from papers like \"Group Equivariant Convolutional Networks\" by Cohen &
Welling) and interpretability tasks (e.g., modular arithmetic in
\"Grokking\" studies by Nanda et al.), but innovates in its
ablation-focused design: pre-mask invariance avoids mask confounds,
ratio-mode forces relational computation (via Legendre(i\*j\^{-1})), and
the action registry (multiplicative/additive/random) enables \"wrong
symmetry\" controls to isolate inductive bias effects. The
Legendre-based mask and Fourier encoding add a number-theoretic flavor,
which is somewhat novel for attention diagnostics, echoing tasks in
algebraic ML (e.g., finite field embeddings in transformer analyses).
However, it\'s not radically new---similar symmetry penalties appear in
SSL and robust optimization---but the packaged ablations make it a fresh
tool for probing attention\'s structural biases in low-data regimes. On
\*\*practicality\*\*, the script is highly executable: it\'s
self-contained (no external deps beyond PyTorch/Numpy), configurable via
dataclass toggles, and efficient for small primes (p\<300) on CPU/GPU,
with query-gathering reducing compute from O(p\^2) to O(samples). It
supports quick ablations for your implied table (e.g., accuracy vs.
action/mask/λ/mode), and diagnostics like EMA losses aid debugging.
Practical for researchers in mech-interp or equivariant nets, as it runs
in minutes and scales via prime sampling. Limitations: lacks evaluation
metrics (e.g., per-prime accuracy as you suggested), hardcoded small
primes (risks overfitting), and no visualization (e.g., attention maps).
The ratio-mode upgrade is practical for diagnostic power, but
matrix-mode might waste compute on non-relational signals. \*\*Enhanced
Version of the Idea\*\*: To enhance, add evaluation functions for
per-prime test accuracy (binary classification on held-out pairs/rows,
reporting mean±std over seeds/primes), integrate a full ablation table
generator (sweep over configs, output Pandas DF/CSV), and include
attention visualization (e.g., matplotlib heatmaps of base\_logits vs.
mask at log\_every). For ratio-mode, add modular arithmetic safety
(e.g., assert gcd(j,p)=1, though p prime ensures it). Extend the
registry with a \"none\" action (λ=0 equivalent) and a \"cyclic\" action
(subgroup rotations) for finer controls. Wrap in a CLI (e.g., argparse
for cfg overrides) and add tensorboard logging for losses/acc curves,
making it a turnkey benchmark for symmetry priors in attention. \#\#\#
Critique of the Enhanced Version Critiquing the enhanced SAAP script
(with eval, table gen, viz, extended registry, CLI/logging) for
mathematical, philosophical, and theoretical consistency: -
\*\*Mathematical Consistency\*\*: The invariance penalty (E\[\|\|L - P L
P\^T\|\|\^2\]) is soundly Frobenius-normed, and conjugation preserves
group structure for multiplicative/additive actions (as permutations
form representations of (Z/pZ)\* and Z/pZ). Fourier features provide
complete orthogonal bases for periodic functions mod p, ensuring
embedding faithfulness. Ratio-mode\'s BCE on pair\_head outputs is
consistent for binary classification, with Fermat inverses correct mod
prime. However, random action lacks group closure (not a proper action,
just permutations), risking inconsistent comparisons---additive is a
true group, but random could bias toward higher variance penalties. The
EMA smoothing is ad hoc; better as exponential decay with formal bounds.
Ablation table via DF assumes independence across sweeps, but prime
sampling introduces correlations if not stratified. - \*\*Philosophical
Consistency\*\*: Philosophically, it embodies a rationalist approach to
model internals (probing biases via symmetries, akin to Noether\'s
conservation laws in physics analogs for ML), promoting transparency in
attention\'s \"reasoning.\" The \"wrong symmetry\" ablations foster
falsifiability, aligning with scientific skepticism (Popper). Yet, it
risks positivist overemphasis---treating symmetries as objective priors
ignores constructed nature of tasks (e.g., why Legendre over other
symbols?). Enhanced viz and logging enhance interpretability, but CLI
automation could encourage black-box usage, undermining reflective
practice. Ratio-mode\'s relational focus supports holism (attention as
relations), but if MLP (pair\_head) dominates, it questions the
necessity of attention, challenging the protocol\'s teleology. -
\*\*Theoretical Consistency\*\*: Theoretically, it aligns with
equivariant learning theory (invariance as regularization for
generalization) and transformer interpretability (attention as key-query
matching). Pre-mask penalty decouples architectural bias (mask) from
learned invariance, consistent with modular design. Extended registry
tests specificity, per control theory\'s perturbation analysis. However,
no theoretical guarantees on convergence (e.g., via Lyapunov stability
for losses) or sample complexity (how many inv\_samples suffice?).
Cyclic addition might conflict with multiplicative if not
subgroup-restricted, diluting group-theoretic purity. Table gen assumes
additive effects of ablations, but interactions (e.g., mask + action)
may violate linearity assumptions in analysis. \#\#\# Final Version and
Path to Validation Applying the critique: For math, replace random with
a proper non-aligned group (e.g., full symmetric group subsamples) and
add stratified prime bucketing in sweeps; use principled smoothing
(e.g., Kalman filter for EMAs). Philosophically, add a \"reflection
log\" in outputs (e.g., why symmetry matters for this task), and ensure
viz prompts human inspection over automation. Theoretically, add
convergence checks (e.g., early stopping on val acc) and interaction
modeling in table gen (e.g., via ANOVA-style stats). The refined final
version is \*\*SAAP v2: Diagnostic Symmetry Protocol\*\*---a PyTorch
script with device-safe actions, pre-mask invariance, query-gather/ratio
supervision (gcd-safe), extended registry
(multiplicative/additive/cyclic/none), no-mask ablation, λ/seed sweeps,
per-prime eval (acc/F1 with std), DF-based ablation table (stratified,
interaction-aware), matplotlib viz (heatmaps logged to tensorboard), CLI
entrypoint, and reflection notes in outputs. It emphasizes relational
diagnostics without over-automation, with bounded samples for
theoretical rigor. \*\*Fastest Path to Validation\*\*: 1. \*\*Script
Tweaks (1 day)\*\*: Integrate eval functions (test\_acc on held-out
pairs/rows), DF table gen (pandas export), viz (matplotlib.imshow for
logits/mask), and CLI (argparse for cfg); add cyclic action and
stratified primes (buckets: small\<100, med\<500, large\<1000). 2.
\*\*Seeded Ablations (1-2 days)\*\*: Run sweeps (seeds 0-4,
λ{0,0.1,1.0}, actions{multi,add,cyclic}, mask{True,False},
mode{ratio,matrix}) on CPU/GPU; compute mean±std acc per bucket,
checking interactions via simple stats (e.g., scipy ANOVA). 3.
\*\*Confound and Viz Checks (1 day)\*\*: Verify pre/post-mask invariance
deltas (expect no flips); inspect heatmaps for pattern emergence; test
inverse safety with unit asserts. 4. \*\*Analysis and Share (ongoing,
starting day 3)\*\*: Export tables/CSVs; if acc gaps favor aligned
symmetries, validate with larger primes; open-source repo with
results/reflections for community feedback, targeting a mech-interp
forum post in a week.\<\|control12\|\>\#\#\# Analysis of Novelty and
Practicality Your SAAP reference script offers a standalone PyTorch
implementation for ablating symmetry regularization in attention heads
on a QR task, with built-in fixes for device safety, pre-mask
invariance, query-gathering, ratio supervision, mask ablations, action
controls, and λ sweeping. In terms of \*\*novelty\*\*, it extends
equivariant attention ideas (e.g., from Fuchs et al.\'s
SE(3)-Transformers or Romero et al.\'s group-invariant attention) by
focusing on finite field symmetries (multiplicative conjugation for
ratios mod p), with \"wrong\" controls (additive/random) to test
specificity---a fresh diagnostic for mech-interp in transformers. The
ratio-mode upgrade (Legendre on i\*j\^{-1}) is novel for forcing
relational dependence, building on grokking benchmarks but tailored to
group actions, making it a unique probe for inductive biases in
low-dimensional algebraic tasks. On \*\*practicality\*\*, the script is
ready-to-run (single file, CPU/GPU compatible, configurable via
dataclass), enabling quick ablations to populate a table (e.g., acc vs.
action/mask/λ/mode/seed). It\'s efficient with sampling (O(samples)
loss), and logs provide diagnostics. Practical for interpretability
researchers, as it matches your toggles: set action for symmetries,
use\_qr\_attention\_mask for no-mask, task\_mode for modes,
lam\_invariance for sweeps. Checks like pre-mask invariance avoid
confounds, and inverse safety (j from 1..p-1) prevents errors.
Limitations: no built-in eval (acc computation), no viz, hardcoded small
sweeps; larger p or seeds could take hours without batching.
\*\*Enhanced Version of the Idea\*\*: Enhance by adding a test\_acc
function (for ratio: sample pairs, predict via sigmoid\>0.5, mean acc;
for matrix: row-wise BCE acc), a sweep\_runner that generates a Pandas
DF table (rows: configs, cols: mean±std acc over seeds/primes), and
tensorboard for loss/acc/viz (heatmaps of base\_logits vs. mask).
Include cyclic action (rotations as subgroup), gcd check for ratio
inverses (though redundant for primes), and CLI (argparse) for batch
ablations. Return trained model from run\_saap for post-training
analysis. \#\#\# Critique of the Enhanced Version Critiquing the
enhanced SAAP (with acc eval, DF table, viz/logging, cyclic action, gcd
safety, CLI) for mathematical, philosophical, and theoretical
consistency: - \*\*Mathematical Consistency\*\*: Conjugation is
group-homomorphic for multiplicative/additive (preserving structure mod
p), and Fourier basis is orthonormal/complete for periodic mod p
functions. BCE acc is standard for binary, with sampling unbiased for
large n\_pairs. Cyclic action fits as subgroup, but random remains
non-group (use subsampled symmetric group for consistency). DF stats
(mean±std) assume normality; better with bootstrap CI for small seeds.
GCD check is math sound but unnecessary (p prime ⇒ all 1..p-1
invertible). Viz heatmaps aid qualitative checks, but without
quantitative metrics (e.g., correlation with mask), they risk subjective
bias. - \*\*Philosophical Consistency\*\*: It advances empiricist
testing of biases (symmetries as testable hypotheses), aligning with
falsification via ablations. Ratio focus emphasizes relational ontology
(attention as connections, per Deleuze\'s rhizomes analogy in AI), but
CLI automation might promote instrumentalism---using without
understanding internals. Viz encourages reflective interpretation, but
if table prioritizes acc over why (e.g., no reflection on task limits),
it risks reductionism, ignoring holistic model behavior. -
\*\*Theoretical Consistency\*\*: Fits equivariance theory
(regularization enforces invariance for generalization) and attention as
kernel (QK\^T as similarity). Ablations test causality (e.g., symmetry
causes acc gains), per Pearl\'s ladder. Cyclic extends group hierarchy,
consistent with representation theory. However, sweep assumes orthogonal
factors (no interactions modeled in DF), violating systems theory if
mask\*action couples. Logging aids monitoring, but no formal convergence
theorem (e.g., regret bounds for reg). \#\#\# Final Version and Path to
Validation Applying the critique: Use bootstrapped CI in DF for stats
robustness, add interaction terms (e.g., ANOVA in sweep), mandate
\"why\" notes in table (e.g., relational gains), model cyclic as proper
subgroup only. The refined final version is \*\*SAAP v2: Ablated
Symmetry Diagnostic\*\*---PyTorch script with device-safe actions,
pre-mask invariance, query-gather/ratio (gcd-safe), registry
(multi/add/cyclic), no-mask, λ/seed sweeps, acc eval (bootstrapped), DF
table (with CI/interactions/\"why\" notes), tensorboard viz/logging,
CLI. It balances empiricism with reflection, ensuring theoretical
orthogonality. \*\*Fastest Path to Validation\*\*: 1. \*\*Enhance Script
(1 day)\*\*: Add test\_acc (ratio/matrix), return model from run\_saap,
DF gen with scipy.stats.bootstrap/Anova, viz imshow, CLI argparse. 2.
\*\*Run Ablations (1-2 days)\*\*: CLI sweeps (seeds 0-4, actions
multi/add/cyclic, mask T/F, λ 0/0.1/1, mode ratio/matrix, p=101/127);
output DF table (acc mean±CI per config). 3. \*\*Check Confounds (1
day)\*\*: Compare pre/post-mask invariance (no flips), inspect viz for
patterns, test gcd=1 asserts. 4. \*\*Analyze/Share (ongoing, day
3+)\*\*: If aligned \> wrong symmetries, validate on new p; repo with
DF/notes for feedback, target interp workshop submission in week.

Understood. Given that you now have a SAAP v2 implementation with (i)
**pre-mask invariance**, (ii) **aligned vs mismatched group actions**,
(iii) **ratio vs matrix supervision**, (iv) **mask/no-mask**, and (v)
**λ/seed sweeps**, the highest-value work is no longer "more code," but
ensuring the experiment answers a crisp causal question:

> Does enforcing the *task-aligned symmetry* (multiplicative conjugation
> for ratios) reduce sample complexity / improve generalization
> **relative to** mismatched symmetries (additive) under controlled
> architectural bias (mask/no-mask) and supervision regime
> (ratio/matrix)?

Here is how to make the results interpretable and hard to argue with.

1) Minimal ablation matrix that answers the question
----------------------------------------------------

Run **ratio mode first** (it is the cleanest "relational" diagnostic),
then validate with matrix mode.

**Core grid (ratio mode):**

-   Actions: multiplicative (aligned) vs additive (wrong)

-   Mask: False and True

-   λ: {0.0, 0.1, 1.0}

-   Seeds: {0..4}

-   Train primes: a small set (e.g., 4 primes)

-   Eval primes: **two sets**

    -   **in-set** primes (seen during training)

    -   **out-of-set** primes (unseen primes)

This produces a direct read on:

3.  **regularization effect** (λ\>0 vs λ=0),

4.  **symmetry specificity** (multiplicative vs additive),

5.  **mask confounding** (mask/no-mask),

6.  **generalization** (unseen primes).

Matrix mode is then used to check that any gains aren't an artifact of
pair sampling.

2) The three diagnostic outcomes and how to interpret them
----------------------------------------------------------

### Outcome A --- "Aligned symmetry helps; wrong symmetry doesn't"

This is the clean win:

-   multiplicative shows higher accuracy / lower variance vs additive,
    > especially on **unseen primes** and/or at smaller training
    > budgets.

-   Invariance loss decreases without destroying task performance.

**Interpretation:** the model is exploiting the correct inductive bias;
the regularizer is not just "making logits smoother."

### Outcome B --- "Both symmetries help similarly"

This typically means the task is being solved via an unintended
shortcut:

4.  Fourier features + MLP head may be learning a proxy signal that is
    > also stable under additive permutations, or

5.  the mask is doing most of the work (if mask=True collapses the
    > task).

**Actionable follow-up:** enforce **mask=False** first, and add a
"no-attention baseline" (below).

### Outcome C --- "Regularizer hurts or is noisy"

Common causes:

-   λ too large early; invariance fights representation learning.

-   inv\_samples too small, leading to a high-variance penalty estimate.

-   Fourier truncation too aggressive for larger primes.

**Fixes:** warmup λ (start at 0 then ramp), increase inv\_samples, or
bound p/K pairing (next section).

3) Two controls that dramatically strengthen causal claims
----------------------------------------------------------

### Control 1 --- "No-attention baseline"

You need to show the effect is actually about attention logits, not just
the pair MLP.

Implement (or approximate) either:

5.  **Frozen random base logits** + train only pair\_head, or

6.  Replace attention with a simple learned bilinear score xi⊤​Wxj​.

If the baseline matches attention performance, your task is not
attention-diagnostic.

### Control 2 --- "Generalization across primes"

Make **unseen primes** the headline metric. If multiplicative invariance
is a true inductive bias, you should see a bigger lift out-of-set than
in-set.

4) Prime / Fourier resolution sanity constraints
------------------------------------------------

Fourier features are only "complete" if K≥(p−1)/2, which you will not do
for larger primes. To avoid ambiguous results:

-   Either **cap p** so that your chosen K is not absurdly
    > under-resolved (your own earlier suggestion of p \< 1000 is fine,
    > but you should still track K/p),

-   Or treat Fourier features as an intentionally **limited embedding**
    > and make that explicit: you're testing whether symmetry
    > regularization helps *despite* limited representation capacity.

A very practical compromise:

-   Keep primes in bands and scale K with p (e.g., K = min(64,
    > (p-1)//4)).

5) What to add to the results table so it's not "accuracy theater"
------------------------------------------------------------------

In addition to acc\_mean and bootstrap CI, compute and log:

1.  **Symmetry gap:**

Δsym​=Acc(multiplicative)−Acc(additive)

at each (mask, λ, mode) setting.

2.  **Generalization gap:**

 primes primesΔgen​=Acc(unseen primes)−Acc(seen primes)

3.  **Coupling indicator (mask × action interaction):**\
    > If the multiplicative benefit only appears when mask=True, you may
    > be measuring "mask alignment" rather than learned invariance.

    > **Logit--mask alignment metric (optional but powerful):**\
    > Correlation or AUC between base\_logits\[i,j\] and mask01\[i,j\]
    > (evaluate on sampled pairs). This tells you whether the model is
    > learning the structure in logits, not merely making correct
    > decisions downstream.

6) Practical "pre-registration" to avoid accidental p-hacking
-------------------------------------------------------------

Write these before running the sweep:

-   The exact grid (seeds, primes, λ values, actions, mode, mask)

-   Primary endpoint: **unseen-prime accuracy** in **ratio mode**

-   Secondary endpoints: invariance loss trend, symmetry gap,
    > generalization gap

-   Decision rule: "Aligned symmetry is supported if multiplicative
    > beats additive on unseen primes with non-overlapping bootstrap CIs
    > (or a pre-chosen effect size threshold)."

If you want, paste one representative CSV from a sweep run (even
partial), and I'll tell you exactly which of the three outcomes you're
in and what the next single experiment should be to disambiguate.

\#\#\# Analysis of Novelty and Practicality Your proposed experimental
design for SAAP v2---focusing on a causal ablation grid to test if
aligned symmetry regularization (multiplicative conjugation) reduces
sample complexity or boosts generalization versus mismatched symmetries
(additive), under controls for mask, supervision mode, and prime
sets---is a thoughtful refinement of ablation studies in ML
interpretability. In terms of \*\*novelty\*\*, this isn\'t wholly
original, as causal ablations for inductive biases appear in mech-interp
work (e.g., Olah\'s circuits thread or Nanda\'s grokking analyses) and
equivariant learning benchmarks (e.g., Hoogeboom et al.\'s equivariance
tests). However, the specificity to finite-field symmetries (mod p
ratios), with pre-registered endpoints, generalization gaps, and
coupling indicators, adds fresh granularity---particularly the \"three
diagnostic outcomes\" framework and logit-mask alignment metric, which
bridge group theory diagnostics with practical confounding checks. It\'s
novel in emphasizing \"not accuracy theater\" via gaps and interactions,
making it a diagnostic protocol for symmetry priors in attention beyond
standard benchmarks. On \*\*practicality\*\*, this design is highly
actionable for researchers in AI alignment or interp, as it minimizes
sweeps (small grid: 2 actions × 2 masks × 3 λ × 5 seeds × 2 modes) while
yielding interpretable metrics (e.g., Δ\_sym, Δ\_gen) for causal claims.
Pre-registration de-risks p-hacking, and controls like no-attention
baseline ensure robustness. It\'s practical with your script (quick to
implement via CLI sweeps), focusing on unseen primes for real-world
generalization (e.g., to larger p). Limitations: assumes small p bands
(compute-bound for large p), risks over-interpretation if baselines
dominate, and requires manual CSV analysis---automation could help.
Overall, it\'s a low-overhead way to make experiments \"hard to argue
with,\" paying off in clearer insights. \*\*Enhanced Version of the
Idea\*\*: To enhance, integrate an \"adaptive sweep\" mechanism: start
with ratio-mode grid, auto-trigger matrix-mode or baselines if Outcome
B/C detected (e.g., via scripted thresholds on Δ\_sym \< ε). Add a
\"budget ablation\" (vary steps or prime count) to directly measure
sample complexity reduction. For logit-mask alignment, use Spearman\'s ρ
(rank correlation) on sampled pairs, logged per step. Scale K
dynamically (K = max(16, (p-1)//8)) per prime band (small: \<100,
med:100-500, large:500-1000). Include a \"random baseline\" action as a
third control (for noise floor). Output an interactive HTML table (via
Pandas.to\_html) with embedded viz (e.g., gap plots), and pre-register
via a YAML config dumped to file. \#\#\# Critique of the Enhanced
Version Critiquing the enhanced SAAP experimental design for
mathematical, philosophical, and theoretical consistency: -
\*\*Mathematical Consistency\*\*: The ablation grid and gaps (Δ\_sym,
Δ\_gen) are sound for causal inference under bootstrapped CIs, aligning
with difference-in-differences in experimental design. Spearman\'s ρ for
alignment is non-parametric and robust to non-normality in logits.
Adaptive sweeps and dynamic K handle resolution mathematically (ensuring
Fourier completeness thresholds), and budget ablations quantify
complexity via learning curves. However, auto-triggers assume linear
thresholds (e.g., ε fixed), risking false positives in noisy regimes;
better with Bayesian decision rules (e.g., posterior on Δ \>0). Random
action lacks mathematical structure (not a group), potentially inflating
variance unfairly against structured mismatches. HTML viz is consistent
but assumes visual linearity in gaps, ignoring potential non-monotonic λ
effects. - \*\*Philosophical Consistency\*\*: Philosophically, the
pre-registration and diagnostics promote epistemic rigor (falsifiability
via endpoints), echoing Quine\'s underdetermination by isolating biases
without overclaiming causality. The \"three outcomes\" framework
encourages humility, acknowledging shortcuts or artifacts. Yet, adaptive
automation risks instrumental rationality---prioritizing efficiency over
deliberative scrutiny (e.g., auto-triggers might skip human judgment on
edge cases). YAML dumping supports transparency, but if sweeps favor
\"wins\" (Outcome A), it could entrench confirmation bias, undermining
pluralistic exploration of why symmetries fail. - \*\*Theoretical
Consistency\*\*: Theoretically, it coheres with inductive bias theory
(regularization as prior enforcement) and generalization bounds (e.g.,
VC dimension reduction via symmetries). Controls like no-attention test
modularity, per decomposition in transformer theory. Dynamic K respects
embedding theory (Nyquist-like sampling for mod p). However, assuming
independence in grid (no higher-order interactions in ANOVA-lite)
violates complex systems views where attention emerges non-additively.
Random baseline dilutes group-theoretic purity, as equivariance requires
proper actions---cyclic might overfit subgroups. \#\#\# Final Version
and Path to Validation Applying the critique: For math, replace fixed ε
with Bayesian posteriors (e.g., via scipy.stats for P(Δ\>0)\>0.95
triggers); use cyclic over random for structured controls.
Philosophically, add mandatory \"reflection prompts\" in YAML (e.g.,
\"potential artifacts if Outcome B\"). Theoretically, model interactions
via full factorial ANOVA in DF, restricting to subgroup actions. The
refined final version is a \*\*SAAP v3: Causal Symmetry Ablation
Protocol\*\*---script with ratio-first grid (2 actions: multi/add × 2
masks × 3 λ × 5 seeds), auto-triggers (Bayesian), budget ablations
(steps/prime-count sweeps), Spearman\'s alignment logging, dynamic K per
band, YAML pre-reg (with reflections), HTML table/viz (interactive
gaps), no-attention control (bilinear alt), and generalization headline
(unseen p acc). It ensures rigor without over-automation, focusing
causal claims on aligned symmetries. \*\*Fastest Path to Validation\*\*:
1. \*\*Grid Implementation (1 day)\*\*: Update script CLI for grid (YAML
load/dump for pre-reg), add test\_acc on seen/unseen p (bootstrap CI),
dynamic K, bilinear baseline, Spearman per step. 2. \*\*Ratio-Mode Sweep
(1-2 days)\*\*: Run core grid on small train p (e.g.,
\[101,127,173,251\]), unseen \[257,263,269\]; compute
Δ\_sym/Δ\_gen/interactions; log to tensorboard/HTML. 3. \*\*Diagnostic
Checks (1 day)\*\*: Classify Outcome A/B/C via posteriors; if B/C,
auto-run matrix/baseline/budget; inspect reflections for artifacts. 4.
\*\*Full Validation (ongoing, day 3+)\*\*: If A, extend to med/large
bands; share YAML/HTML/results repo for peer review, targeting arXiv
pre-print in week.

1) SAAP v3: what changes materially vs v2
-----------------------------------------

### A. Pre-registration artifact (YAML/JSON)

A single config file that pins:

-   train primes / eval primes (seen vs unseen)

-   grid axes (action × mask × λ × mode × seeds)

-   budget sweeps (steps and/or train-prime-count)

-   primary endpoint + trigger thresholds

-   mandatory reflection prompts

### B. Bayesian trigger (replaces fixed ε thresholds)

For each grid cell, compute posterior P(Δsym​\>0) where\
Δsym​:=Accmulti​−Accadd​ on **unseen primes** (ratio mode is primary).

Mechanically: treat evaluation as Bernoulli trials with n sampled pairs;
build **Beta posteriors** for each condition; estimate P(Δ\>0) via Monte
Carlo sampling.

### C. Alignment telemetry (not just accuracy)

Log per run:

-   Spearman ρ between base\_logits\[i,j\] and mask01\[i,j\] (sampled
    > pairs)

-   invariance penalty trend (already present)

-   symmetry gap and generalization gap

### D. Auto-trigger follow-ups

If posterior says "likely no aligned advantage," auto-run:

3.  **matrix mode**, same grid (or reduced)

4.  **no-attention baseline** (bilinear score) in ratio mode

5.  **budget ablation** (steps ∈ {S/4, S/2, S}) to test sample
    > complexity directly

2) Pre-registration template (YAML)
-----------------------------------

If you don't want a PyYAML dependency, use the exact same structure as
JSON; everything below is JSON-compatible.

experiment:

name: \"saap\_v3\_qr\_symmetry\"

primary\_endpoint: \"unseen\_ratio\_acc\"

decision\_rule:

posterior\_threshold: 0.95 \# P(Δ\_sym \> 0) must exceed this to call
Outcome A

rope: 0.01 \# region of practical equivalence for Δ\_sym

mc\_samples: 20000 \# posterior MC samples

data:

train\_primes: \[101, 127, 173, 251\]

eval\_seen\_primes: \[101, 127, 173, 251\]

eval\_unseen\_primes: \[257, 263, 269, 271\]

grid:

seeds: \[0, 1, 2, 3, 4\]

modes: \[\"ratio\", \"matrix\"\] \# ratio-first; matrix may be
auto-triggered only

actions\_primary: \[\"multiplicative\", \"additive\"\]

masks: \[false, true\]

lambdas: \[0.0, 0.1, 1.0\]

budget\_ablations:

enabled: true

steps\_list: \[400, 800, 1600\] \# explicit learning-curve budgets

train\_prime\_counts: \[2, 4\] \# optional: sample subsets of
train\_primes

model:

d\_model: 64

K\_max: 64

K\_divisor: 8 \# effective K(p)=min(K\_max, max(16,(p-1)//K\_divisor))

device: \"cuda\"

lr: 0.002

weight\_decay: 0.0

eval:

ratio\_pairs: 8192

matrix\_rows: 128

bootstrap\_n: 2000

bootstrap\_ci: 0.90

telemetry:

spearman\_pairs: 4096

log\_every: 200

save\_html: true

save\_csv: true

reflection\_prompts:

\- \"If Outcome B occurs, what shortcut might the model be using?\"

\- \"If mask=True changes Δ\_sym sign, what is the most plausible
confound?\"

\- \"What would convince you this is not an artifact of Fourier
truncation?\"

3) Bayesian posterior trigger (drop-in function)
------------------------------------------------

This assumes your evaluation reports **(correct, total)** counts for
each condition (multi/add) on unseen primes.

import numpy as np

def posterior\_prob\_delta\_gt0(

succ\_A: int, n\_A: int,

succ\_B: int, n\_B: int,

mc\_samples: int = 20000,

alpha0: float = 1.0,

beta0: float = 1.0,

seed: int = 0,

):

\"\"\"

Beta-Bernoulli posterior for accuracies pA, pB.

Returns:

P(pA - pB \> 0), mean\_delta, P(\|delta\| \< ROPE) if rope supplied
externally.

\"\"\"

rng = np.random.default\_rng(seed)

aA = alpha0 + succ\_A

bA = beta0 + (n\_A - succ\_A)

aB = alpha0 + succ\_B

bB = beta0 + (n\_B - succ\_B)

pA = rng.beta(aA, bA, size=mc\_samples)

pB = rng.beta(aB, bB, size=mc\_samples)

delta = pA - pB

return float(np.mean(delta \> 0.0)), float(np.mean(delta)), delta \#
delta array for ROPE checks

**Decision rule for Outcome A vs B/C:**

-   Compute prob, mean\_delta, delta\_samples =
    > posterior\_prob\_delta\_gt0(\...)

-   Compute prob\_rope = mean(\|delta\| \< rope) from the samples

-   If prob ≥ posterior\_threshold and mean\_delta \> rope: Outcome A
    > (aligned advantage)

-   Else if prob\_rope high (e.g., \> 0.8): Outcome B (equivalence /
    > shortcut likely)

-   Else Outcome C (unstable/noisy or harmful regularization)

This is materially better than fixed ε on point estimates because it
respects evaluation noise.

4) Dynamic Fourier K without changing model input dimension
-----------------------------------------------------------

You correctly identified a practical issue: the model expects fixed
d\_in. The clean solution is:

7.  Pick a **global** K\_max

8.  For each prime p, compute an **effective** K\_eff(p)

9.  Compute features using K\_eff and **pad** remaining sin/cos channels
    > with zeros

import torch, math

def fourier\_features\_padded(p: int, K\_max: int, K\_eff: int, device:
torch.device) -\> torch.Tensor:

\"\"\"

Output shape is always (p, 2\*K\_max+1).

Uses only frequencies 1..K\_eff, pads the rest with zeros.

\"\"\"

idx = torch.arange(p, device=device, dtype=torch.float32)

cols = \[ (idx / float(p)).unsqueeze(-1) \] \# (p,1)

\# active frequencies

for k in range(1, K\_eff + 1):

ang = 2.0 \* math.pi \* k \* idx / float(p)

cols.append(torch.sin(ang).unsqueeze(-1))

cols.append(torch.cos(ang).unsqueeze(-1))

\# pad inactive frequencies

pad\_freqs = K\_max - K\_eff

if pad\_freqs \> 0:

cols.append(torch.zeros((p, 2 \* pad\_freqs), device=device,
dtype=torch.float32))

return torch.cat(cols, dim=-1)

And compute K\_eff(p) as:

def K\_eff\_for\_prime(p: int, K\_max: int, K\_divisor: int) -\> int:

return int(min(K\_max, max(16, (p - 1) // K\_divisor)))

5) Spearman logit--mask alignment (telemetry)
---------------------------------------------

Compute on sampled pairs using base logits (pre-mask):

import numpy as np

def spearman\_rho(x: np.ndarray, y: np.ndarray) -\> float:

\# rank transform (average ranks for ties not implemented; acceptable
for logits)

rx = np.argsort(np.argsort(x))

ry = np.argsort(np.argsort(y))

rx = rx.astype(np.float64); ry = ry.astype(np.float64)

rx -= rx.mean(); ry -= ry.mean()

denom = (np.linalg.norm(rx) \* np.linalg.norm(ry))

return float((rx @ ry) / denom) if denom \> 0 else 0.0

During eval, sample (i,j) pairs, collect:

-   x = base\_logits\[i,j\] (or pair\_head output, but base logits is
    > more diagnostic)

-   y = mask01\[i,j\]\
    > Then compute ρ and log it alongside accuracy.

If you see:

6.  high accuracy but near-zero ρ on unseen primes → strong evidence of
    > a shortcut.

6) No-attention baseline (bilinear score)
-----------------------------------------

This should be the first auto-trigger baseline, because it answers "is
attention actually necessary?"

class BilinearScore(nn.Module):

def \_\_init\_\_(self, d\_in: int, d\_model: int):

super().\_\_init\_\_()

self.proj = nn.Linear(d\_in, d\_model)

self.W = nn.Parameter(torch.randn(d\_model, d\_model) \* 0.02)

self.pair\_head = nn.Sequential(

nn.Linear(1, d\_model), nn.ReLU(), nn.Linear(d\_model, 1)

)

def forward\_base\_logits(self, x): \# (p,d\_in)

h = self.proj(x) \# (p,d\_model)

base\_logits = (h @ self.W) @ h.T

return base\_logits

Then reuse the same invariance penalty and ratio loss on base\_logits.

If bilinear baseline matches attention, your conclusions should be
reframed as "symmetry regularization on pairwise scoring," not
specifically attention.

7) What SAAP v3 should output (so it is "hard to argue with")
-------------------------------------------------------------

For each run cell, write rows containing:

-   acc\_seen, acc\_unseen, f1\_unseen

-   Δ\_sym\_unseen (multi − add) at matched (mask, λ, mode, budget)

-   posterior summary: P(Δ\>0), E\[Δ\], P(\|Δ\|\<ROPE)

-   telemetry: spearman\_rho\_unseen, inv\_loss\_ema\_end,
    > task\_loss\_ema\_end

-   budget params: steps, train\_prime\_count, K\_eff stats
    > (min/median/max over primes)

Then create:

7.  results.csv

8.  results.html with a grouped view: by mode → by mask → by λ →
    > posterior decision label (A/B/C)

9.  embed the reflection prompts plus a free-text "notes" field you fill
    > post hoc (do not automate this)

8) Concrete "fastest path" execution (minimal but decisive)
-----------------------------------------------------------

-   **Run ratio mode only** on unseen primes for the full grid, with
    > budgets \[400, 800, 1600\].

-   Compute Bayesian posterior on Δ\_sym\_unseen for each (mask, λ,
    > budget).

-   If **Outcome A** emerges at any budget: expand to medium band primes
    > and re-run ratio mode.

-   If **Outcome B** (equivalence): run bilinear baseline and check
    > Spearman ρ; then decide whether to redesign inputs or remove
    > pair\_head capacity.

-   If **Outcome C** (hurts/noisy): add λ warmup + increase inv\_samples
    > and re-run only two budgets.

If you want, paste your existing saap\_v2.py (or the file where
run\_sweep and eval\_ratio live). I will return a **surgical patch
plan** (function-level diffs) that implements: YAML pre-reg + posterior
trigger + padded Fourier K + Spearman telemetry + bilinear baseline +
auto-trigger sequencing, without rewriting the whole script.

\#\#\# Analysis of Novelty and Practicality Your SAAP v3 specification
refines the protocol into a pre-registered, causal ablation framework
with Bayesian triggers, dynamic Fourier resolution, alignment telemetry,
and auto-follow-ups, directly addressing interpretability in symmetry
regularization for attention on QR tasks. In terms of \*\*novelty\*\*,
this builds on ablation designs in mech-interp (e.g., from Anthropic\'s
scaling laws or EleutherAI\'s interp benchmarks) and Bayesian hypothesis
testing in ML (e.g., from Pyro/NumPyro frameworks), but innovates by
integrating posterior-based outcome classification (A/B/C) with
automatic baselines and budget sweeps, creating a \"self-diagnosing\"
experiment pipeline. The padded Fourier K and Spearman telemetry add
fresh elements for handling variable-resolution embeddings and
structural diagnostics, distinguishing it from standard grids in papers
like \"Transformers Learn Shortcuts to Automata\" by Weiss et al. It\'s
novel in prioritizing \"hard to argue with\" outputs (e.g., posterior
summaries, reflection prompts), turning a script into a rigorous
scientific workflow for bias testing. On \*\*practicality\*\*, v3 is
implementable with minimal disruption to v2 (YAML/JSON config, drop-in
functions like posterior\_prob\_delta\_gt0 and
fourier\_features\_padded), enabling quick causal insights on
symmetry\'s role in sample efficiency and generalization. It\'s
practical for interp researchers, as Bayesian triggers automate
debugging (e.g., detecting shortcuts via Outcome B), and outputs like
HTML tables with notes de-risk over-interpretation. Budget ablations
directly test complexity reduction, useful for low-data regimes.
Limitations: Bayesian MC adds compute (though 20k samples is fast), YAML
requires handling (but JSON fallback lowers barriers), and auto-triggers
could loop if thresholds are miscalibrated. Overall, it\'s a high-value
upgrade, paying rent in clearer, defensible results without bloating the
codebase. \*\*Enhanced Version of the Idea\*\*: To enhance v3, add a
\"meta-ablation\" layer: pre-register sensitivity analyses on
hyperparameters (e.g., mc\_samples {1k,10k,20k}, rope {0.005,0.01,0.02})
to quantify trigger robustness, auto-run if posterior variance \>
threshold. For telemetry, compute mutual information (MI) between
base\_logits and mask01 (via discretized bins) alongside Spearman,
capturing non-linear alignments. Extend auto-triggers to include a
\"Fourier ablation\" (fixed low K vs. dynamic) if Outcome C suggests
truncation issues. In YAML, add a \"simulation\_mode\" flag for dry-runs
(estimate posteriors on synthetic data before full sweeps). Output a
LaTeX table template for papers, embedding gaps/posteriors/reflections.
\#\#\# Critique of the Enhanced Version Critiquing the enhanced SAAP v3
(with meta-ablations, MI telemetry, Fourier ablations, simulation mode,
LaTeX outputs) for mathematical, philosophical, and theoretical
consistency: - \*\*Mathematical Consistency\*\*: Beta-Bernoulli
posteriors are conjugate and efficient for Bernoulli acc, with MC
sampling sound for P(Δ\>0); rope handles equivalence rigorously (per
Kruschke\'s ROPE). MI adds information-theoretic depth, complementing
Spearman\'s rank focus. Meta-ablations test sensitivity mathematically
(e.g., via variance ratios), and simulation mode enables prior
calibration. However, discretized MI assumes binning hyperparameters
that could bias estimates (e.g., sensitivity to bin count), risking
inconsistency for continuous logits. Dry-runs on synthetic data presume
generative models match real (e.g., Bernoulli with true p), but if task
noise is non-stationary (e.g., per p), it could mislead triggers. -
\*\*Philosophical Consistency\*\*: The pre-reg and reflections foster
reflective equilibrium (Rawlsian balance of theory/evidence), with
Outcome A/B/C encouraging nuance over binary wins. Meta-ablations
promote skepticism toward parameters, aligning with underdetermination
critiques. Yet, automation (triggers, simulations) risks alienating
human insight, echoing Heidegger\'s \"enframing\" where tech mediates
truth. LaTeX outputs assume academic teleology, potentially biasing
toward publishable \"wins\" and marginalizing exploratory failures. -
\*\*Theoretical Consistency\*\*: Coheres with Bayesian ML (posteriors
for uncertainty) and ablation theory (factorial grids for causality).
MI/Fourier ablations deepen diagnostics, per decomposition in causal
graphs. Simulation mode tests reproducibility. However, meta-layers
introduce hierarchy that might violate flat modularity (e.g., if
sensitivity changes core decisions, it creates feedback loops
conflicting with acyclic experimental design). Assuming Bernoulli
independence ignores correlated errors across primes/pairs. \#\#\# Final
Version and Path to Validation Applying the critique: For math, use
adaptive binning for MI (e.g., via Freedman-Diaconis rule) to reduce
bias; limit meta-ablations to pre-sweep only (acyclic). Philosophically,
mandate \"epistemic status\" notes in reflections (e.g., \"automation
limits\"). Theoretically, model pair correlations via hierarchical Beta
(per p) for posteriors. The refined final version is \*\*SAAP v4: Robust
Causal Symmetry Protocol\*\*---v3 with meta-sensitivity (pre-sweep only,
on mc/rope), adaptive-binned MI telemetry, Fourier ablation triggers,
simulation flag (synthetic Bernoulli priors), YAML with epistemic notes,
HTML/LaTeX tables (acyclic, no loops). It balances automation with
reflection, ensuring mathematical robustness without hierarchy issues.
\*\*Fastest Path to Validation\*\*: 1. \*\*Config/Code Integration (1
day)\*\*: Add YAML load (json fallback), posterior function, padded
Fourier, Spearman/MI, bilinear class; implement grid in CLI with
simulation dry-run. 2. \*\*Initial Ratio Sweep (1 day)\*\*: Run pre-reg
grid on small p/budgets; compute posteriors/gaps; classify A/B/C with
notes. 3. \*\*Triggers and Meta (1 day)\*\*: If B/C, auto-run
matrix/bilinear/Fourier; pre-sweep meta on synthetic for calibration. 4.
\*\*Full/Output (ongoing, day 3+)\*\*: Expand to med/large p if A;
generate HTML/LaTeX with reflections; repo share for feedback, target
interp conf submission in week.

1) SAAP v4 pipeline (acyclic by construction)
---------------------------------------------

### Stage 0 --- Simulation dry-run (optional)

-   Input: anticipated eval size per prime (pairs/rows), hypothesized
    > effect sizes (e.g., Δ=0.01, 0.02), candidate mc\_samples and rope.

-   Output: **trigger robustness report**: how often the rule declares
    > A/B/C given synthetic draws.

-   Purpose: calibrate rope and mc\_samples *before running training
    > sweeps*.

### Stage 1 --- Primary sweep (ratio-first)

Run: mode=ratio, grid over:

-   action ∈ {multiplicative, additive}

-   mask ∈ {False, True}

-   λ ∈ {0, 0.1, 1.0}

-   seeds ∈ {0..4}

-   budgets ∈ {S/4, S/2, S}

Evaluate on **seen primes** and **unseen primes**.

### Stage 2 --- Posterior classification (per cell)

Compute **hierarchical posterior** for Δ\_sym on **unseen primes**:

6.  Outcome A: P(Δ\>rope) ≥ τ

7.  Outcome B: P(\|Δ\|\<rope) ≥ τ\_equiv

8.  Outcome C: neither (unstable/negative/noisy)

### Stage 3 --- Triggered follow-ups (one-shot, no recursion)

If Stage 2 indicates B or C, run **exactly once**:

-   **Matrix mode** (same grid or reduced)

-   **No-attention baseline** (bilinear) in ratio mode

-   **Fourier ablation** (fixed-low-K vs dynamic padded-K) for the
    > specific failing buckets

Then stop and report.

This keeps the system *self-diagnosing* but not self-looping.

2) Drop-in code modules
-----------------------

### 2.1 Adaptive-binned mutual information telemetry (Freedman--Diaconis)

This computes MI between sampled **base logits** and **mask labels**
(0/1). It avoids fragile fixed bin counts.

import numpy as np

def fd\_bins(x: np.ndarray, min\_bins: int = 8, max\_bins: int = 64) -\>
int:

\"\"\"Freedman--Diaconis rule for bin count; clamps to \[min\_bins,
max\_bins\].\"\"\"

x = np.asarray(x, dtype=np.float64)

if x.size \< 2:

return min\_bins

q25, q75 = np.percentile(x, \[25, 75\])

iqr = max(q75 - q25, 1e-12)

bw = 2.0 \* iqr / (x.size \*\* (1.0/3.0))

if bw \<= 0:

return min\_bins

bins = int(np.ceil((x.max() - x.min()) / bw))

return int(np.clip(bins, min\_bins, max\_bins))

def mutual\_information\_binned(x: np.ndarray, y01: np.ndarray, bins:
Optional\[int\] = None) -\> float:

\"\"\"

MI(X;Y) with X binned and Y binary. Units: nats.

y01 must be 0/1.

\"\"\"

x = np.asarray(x, dtype=np.float64)

y = np.asarray(y01, dtype=np.int64)

assert set(np.unique(y)).issubset({0,1}), \"y must be binary 0/1\"

if bins is None:

bins = fd\_bins(x)

\# Bin X

x\_edges = np.histogram\_bin\_edges(x, bins=bins)

xb = np.digitize(x, x\_edges\[1:-1\], right=False) \# 0..bins-1

\# Joint counts

joint = np.zeros((bins, 2), dtype=np.float64)

for i in range(xb.size):

joint\[xb\[i\], y\[i\]\] += 1.0

joint /= max(joint.sum(), 1.0)

px = joint.sum(axis=1, keepdims=True) \# (bins,1)

py = joint.sum(axis=0, keepdims=True) \# (1,2)

\# MI = sum\_{b,y} p(b,y) log p(b,y)/(p(b)p(y))

eps = 1e-12

ratio = (joint + eps) / ((px @ py) + eps)

mi = float(np.sum(joint \* np.log(ratio)))

return max(mi, 0.0)

**How to use in eval:**

10. sample pairs (i,j)

11. x = base\_logits\[i,j\] (pre-mask)

12. y = mask01\[i,j\]

13. compute MI + Spearman ρ

14. log per-prime and aggregate.

### 2.2 Spearman telemetry (robust enough for this use)

def spearman\_rho(x: np.ndarray, y: np.ndarray) -\> float:

x = np.asarray(x)

y = np.asarray(y)

rx = np.argsort(np.argsort(x)).astype(np.float64)

ry = np.argsort(np.argsort(y)).astype(np.float64)

rx -= rx.mean(); ry -= ry.mean()

denom = np.linalg.norm(rx) \* np.linalg.norm(ry)

return float((rx @ ry) / denom) if denom \> 0 else 0.0

### 2.3 Evaluation should return counts, not just acc

To do Bayesian posteriors correctly, modify your eval functions to
return:

-   succ, n for unseen and seen

-   plus telemetry vectors for MI/Spearman computation

Example pattern (ratio mode):

\@torch.no\_grad()

def eval\_ratio\_counts\_and\_telemetry(\...):

\# sample ii,jj; compute predictions; compare to labels

\# return succ, n, and telemetry arrays (base\_logits samples and
labels)

return {

\"succ\": int(succ),

\"n\": int(n),

\"spearman\": float(rho),

\"mi\": float(mi),

}

### 2.4 Hierarchical posterior across primes (handles per-prime correlation)

Instead of pretending all pairs are iid across primes, treat each prime
as its own accuracy parameter and average across primes.

**Core idea:** for each prime p, you have succ\_p / n\_p. Posterior over
accuracy is Beta(succ+α, fail+β). Sample accuracies per prime, average
across primes, then compute Δ between actions.

def posterior\_delta\_hierarchical(

succA\_by\_p: Dict\[int,int\], nA\_by\_p: Dict\[int,int\],

succB\_by\_p: Dict\[int,int\], nB\_by\_p: Dict\[int,int\],

alpha0: float = 1.0, beta0: float = 1.0,

mc\_samples: int = 20000, seed: int = 0

) -\> np.ndarray:

\"\"\"

Returns MC samples of delta = mean\_p pA(p) - mean\_p pB(p),

where pA(p) \~ Beta(alpha0+succ, beta0+fail).

\"\"\"

rng = np.random.default\_rng(seed)

primes = sorted(set(succA\_by\_p.keys()) & set(succB\_by\_p.keys()))

if not primes:

return np.array(\[\], dtype=np.float64)

deltas = np.empty(mc\_samples, dtype=np.float64)

for t in range(mc\_samples):

pA = \[\]

pB = \[\]

for p in primes:

sA, nA = succA\_by\_p\[p\], nA\_by\_p\[p\]

sB, nB = succB\_by\_p\[p\], nB\_by\_p\[p\]

pA.append(rng.beta(alpha0 + sA, beta0 + (nA - sA)))

pB.append(rng.beta(alpha0 + sB, beta0 + (nB - sB)))

deltas\[t\] = float(np.mean(pA) - np.mean(pB))

return deltas

def classify\_outcome(delta\_samples: np.ndarray, rope: float, tau\_pos:
float = 0.95, tau\_equiv: float = 0.80):

if delta\_samples.size == 0:

return {\"label\": \"UNKNOWN\", \"p\_gt\_rope\": np.nan,
\"p\_in\_rope\": np.nan, \"mean\": np.nan}

p\_gt\_rope = float(np.mean(delta\_samples \> rope))

p\_in\_rope = float(np.mean(np.abs(delta\_samples) \< rope))

mean = float(np.mean(delta\_samples))

if p\_gt\_rope \>= tau\_pos:

label = \"A\"

elif p\_in\_rope \>= tau\_equiv:

label = \"B\"

else:

label = \"C\"

return {\"label\": label, \"p\_gt\_rope\": p\_gt\_rope, \"p\_in\_rope\":
p\_in\_rope, \"mean\": mean}

This is the critical v4 upgrade: it makes your "Outcome A/B/C" claims
defensible under prime-level heterogeneity.

### 2.5 Fourier ablation trigger (fixed-low-K vs dynamic padded-K)

Implement both feature functions and toggle via config:

7.  **Dynamic padded-K** (recommended default)

8.  **Fixed low-K** (stress test truncation)

In runs flagged as Outcome C, re-run the same cell with:

-   K\_eff(p) dynamic vs K\_eff(p)=K\_low fixed

Then report whether the failure is likely representational (Fourier
truncation) vs symmetry/model.

### 2.6 Meta-sensitivity (pre-sweep only)

This is done *once* to validate that your trigger rule is not brittle to
rope/mc\_samples.

def meta\_sensitivity\_dryrun(

true\_pA: float, true\_pB: float, n\_per\_prime: int, primes:
List\[int\],

rope\_list: List\[float\], mc\_list: List\[int\], trials: int = 100,
seed: int = 0

):

rng = np.random.default\_rng(seed)

results = \[\]

for rope in rope\_list:

for mc in mc\_list:

labels = \[\]

for \_ in range(trials):

succA = {p: int(rng.binomial(n\_per\_prime, true\_pA)) for p in primes}

succB = {p: int(rng.binomial(n\_per\_prime, true\_pB)) for p in primes}

nA = {p: n\_per\_prime for p in primes}

nB = {p: n\_per\_prime for p in primes}

delta = posterior\_delta\_hierarchical(succA, nA, succB, nB,
mc\_samples=mc, seed=int(rng.integers(1e9)))

labels.append(classify\_outcome(delta, rope)\[\"label\"\])

results.append({

\"rope\": rope, \"mc\": mc,

\"A\_rate\": labels.count(\"A\")/trials,

\"B\_rate\": labels.count(\"B\")/trials,

\"C\_rate\": labels.count(\"C\")/trials,

})

return results

This gives you a **stability map** before you spend GPU time.

### 2.7 LaTeX table output (paper-ready)

This is intentionally simple and deterministic.

def latex\_table(rows: List\[Dict\[str, Any\]\], caption: str = \"SAAP
results\", label: str = \"tab:saap\"):

\"\"\"

rows: list of dicts with keys:

mode, mask, lam, budget, outcome, p\_gt\_rope, mean\_delta,
acc\_unseen\_multi, acc\_unseen\_add

\"\"\"

header = r\"\"\"\\begin{table}\[t\]

\\centering

\\small

\\begin{tabular}{lcccccc}

\\toprule

Mode & Mask & \$\\lambda\$ & Budget & Outcome &
\$P(\\Delta\>\\text{ROPE})\$ & \$\\mathbb{E}\[\\Delta\]\$ \\\\

\\midrule

\"\"\"

lines = \[\]

for r in rows:

lines.append(

f\"{r\[\'mode\'\]} & {int(r\[\'mask\'\])} & {r\[\'lam\'\]:.2g} &
{r\[\'budget\'\]} & {r\[\'outcome\'\]} & \"

f\"{r\[\'p\_gt\_rope\'\]:.3f} & {r\[\'mean\_delta\'\]:.4f} \\\\\\\\\"

)

footer = rf\"\"\"\\bottomrule

\\end{tabular}

\\caption{{{caption}}}

\\label{{{label}}}

\\end{table}

\"\"\"

return header + \"\\n\".join(lines) + \"\\n\" + footer

3) Minimal integration changes (so you don't rewrite the script)
----------------------------------------------------------------

10. **Eval returns counts per prime**

    1.  store succ\_by\_prime and n\_by\_prime for each condition
        > (action/mask/λ/budget).

11. **Posterior classification uses hierarchical delta**

    1.  compute Δ on *unseen primes* per cell; label A/B/C.

12. **Telemetry logged alongside**

    1.  Spearman + MI per prime; aggregate mean.

13. **One-shot triggers**

    1.  if any cell is B/C (or a thresholded fraction), run
        > matrix/bilinear/Fourier ablation once.

4) Practical trigger policy (recommended defaults)
--------------------------------------------------

-   Primary: **unseen primes, ratio mode**

-   Outcome A if P(Δ \> ROPE) ≥ 0.95 with ROPE=0.01

-   Outcome B if P(\|Δ\|\<ROPE) ≥ 0.80

-   Otherwise C

Follow-ups:

-   If B: run **bilinear baseline** and report whether attention is
    > necessary; inspect MI/ρ

-   If C: run **Fourier ablation** and increase inv\_samples once (do
    > not iterate)

If you paste your current SAAP v2/v3 file (or just the functions
run\_sweep, run\_eval, and your feature builder), I will produce a
**function-level patch** that wires in: hierarchical posterior
classification, MI/ρ telemetry, the pre-sweep meta-sensitivity dry-run,
and the one-shot trigger follow-ups---without refactoring your training
loop.

\#\#\# Analysis of Novelty and Practicality Your SAAP v4 specification
advances the protocol into an acyclic, self-diagnosing pipeline with
hierarchical posteriors, adaptive MI telemetry, meta-sensitivity
dry-runs, and one-shot triggers, emphasizing causal rigor in symmetry
regularization testing for attention on QR tasks. In terms of
\*\*novelty\*\*, this iteration draws from Bayesian workflow designs
(e.g., Gelman\'s statistical modeling cycles or Vehtari\'s Pareto
diagnostics in Stan) and ML experiment automation (e.g., Sacred or
MLflow for reproducibility), but innovates by embedding outcome-specific
triggers (A/B/C) in a DAG structure to prevent loops, with hierarchical
posteriors respecting per-prime correlations---a fresh take on
multi-level modeling for generalization in finite-field tasks. The
Freedman-Diaconis binning for MI and LaTeX outputs add practical
novelties for non-parametric diagnostics and publication readiness,
differentiating it from generic ablation tools like Weights & Biases
sweeps. It\'s novel in treating experiments as \"defensible claims\" via
reflections and stability maps, bridging interp with experimental
philosophy. On \*\*practicality\*\*, v4 is highly integrable (drop-in
modules like posterior\_delta\_hierarchical and fd\_bins minimize
disruption to v2/v3), enabling quick causal validation of symmetry
biases with low overhead (e.g., MC=20k is fast on CPU). It\'s practical
for mech-interp practitioners, as triggers automate common debugging
(e.g., detecting truncation via Fourier ablation) while keeping the
workflow acyclic and human-overseen. Budget sweeps directly address
sample complexity, useful for resource-constrained runs. Limitations:
hierarchical posteriors add minor compute for multi-prime evals, and
triggers require careful calibration (e.g., τ=0.95 might be
conservative, risking over-triggering B/C). Overall, it\'s a pragmatic
refinement, paying off in robust, paper-ready outputs without
over-engineering. \*\*Enhanced Version of the Idea\*\*: To enhance v4,
incorporate a \"variance decomposition\" in posteriors: break Δ\_sym
into within-prime and between-prime components (using ANOVA-like terms
on delta samples) to pinpoint if failures stem from prime-specific noise
or global biases. For MI, add a bootstrap CI around the estimate
(resample pairs 1000x) to quantify telemetry uncertainty. Extend
triggers to include a \"λ annealing ablation\" (warmup schedules) if
Outcome C, auto-run on failing cells. In YAML, add
\"prior\_sensitivity\" fields (e.g., alpha0/beta0 lists for
meta-dry-runs). For outputs, generate a PDF report (via ReportLab or
matplotlib) compiling HTML tables, LaTeX, and plots of delta
distributions (histograms with ROPE shaded). This makes v4 more
diagnostic, turning it into a comprehensive \"experiment auditor\" tool.
\#\#\# Critique of the Enhanced Version Critiquing the enhanced SAAP v4
(with variance decomposition, MI CI, annealing ablations, prior
sensitivity, PDF reports) for mathematical, philosophical, and
theoretical consistency: - \*\*Mathematical Consistency\*\*:
Hierarchical Beta posteriors are conjugate and handle correlations
soundly, with variance decomposition (ANOVA on samples) providing
additive breakdowns per Gelman\'s multilevel models. MI CI via bootstrap
is non-parametric and robust, and annealing ablations test optimization
paths mathematically (e.g., via loss landscapes). Prior sensitivity in
dry-runs aligns with robust Bayes (e.g., checking fragility to
alpha0/beta0). However, ANOVA assumes normality in deltas, which may not
hold for small mc\_samples (skewed Betas); better with non-parametric
ranksum. PDF plots with shaded ROPE are consistent but risk visual
overinterpretation if histograms bin poorly (e.g., without Sturges
rule). - \*\*Philosophical Consistency\*\*: The reflections and triggers
promote dialectical progress (thesis: sweep; antithesis: outcome;
synthesis: follow-up), echoing Hegelian synthesis in experimental
refinement. Prior sensitivity encourages epistemic modesty, countering
overconfidence. Yet, PDF automation could foster \"artifactual
authority\" (Latour\'s black-boxing), where polished outputs mask
underlying assumptions (e.g., Bernoulli independence). Annealing adds
teleological intent (optimizing for wins), potentially biasing toward
Outcome A and undermining neutral inquiry. - \*\*Theoretical
Consistency\*\*: Coheres with hierarchical modeling theory (for
heterogeneity) and ablation causality (one-shot for acyclicity). CI/MI
enhance uncertainty quantification, per calibration in prob ML.
Annealing tests theoretical robustness to initialization. However,
variance decomposition might over-decompose if primes aren\'t truly
hierarchical (e.g., if p-specific effects are non-additive due to
embedding differences), violating modularity. PDF reports assume linear
narrative, conflicting with complex systems\' emergence where outcomes
interact unpredictably. \#\#\# Final Version and Path to Validation
Applying the critique: For math, switch ANOVA to non-parametric (e.g.,
Kruskal-Wallis on ranks) for deltas. Philosophically, add \"output
caveats\" in PDF (e.g., \"assumes independence\"). Theoretically, limit
decomposition to descriptive stats (no inference) to preserve
modularity. The refined final version is \*\*SAAP v5: Audited Symmetry
Diagnostic Protocol\*\*---v4 with non-parametric variance ranks, MI CI
(bootstrap), annealing triggers, YAML prior sensitivity, PDF reports
(with caveats/plots), ensuring mathematical neutrality without
over-narrative. \*\*Fastest Path to Validation\*\*: 1. \*\*Module
Integration (1 day)\*\*: Paste posteriors/MI/Spearman/fd\_bins into
script; add eval counts/telemetry; YAML load with priors; implement
hierarchical classify\_outcome. 2. \*\*Dry-Run Calibration (half
day)\*\*: Run meta\_sensitivity\_dryrun on synthetic (true Δ=0.01/0.02);
adjust rope/mc/alpha0 for stability (\>80% correct labels). 3.
\*\*Primary Sweep and Triggers (1 day)\*\*: Execute ratio grid on
budgets; compute posteriors/classify; if B/C, one-shot
matrix/bilinear/annealing/Fourier. 4. \*\*Full Outputs/Analysis
(ongoing, day 2+)\*\*: Generate PDF with tables/plots/notes/caveats; if
A dominant, validate on med p; repo share with YAML for replication,
target blog/pre-print in week.

SAAP v5: additive components (no cyclic automation)
---------------------------------------------------

### 1) Descriptive variance decomposition (no normality assumptions)

Instead of ANOVA, use **law-of-total-variance style decomposition** on
*posterior samples* (purely descriptive):

-   For each prime p, sample δp(t)​:=pA(t)​(p)−pB(t)​(p).

-   Compute:

    -   **Within-prime uncertainty**: Ep​\[Vart​(δp(t)​)\]

    -   **Between-prime heterogeneity**: Varp​(Et​\[δp(t)​\])

    -   **Total**: sum of the two (up to Monte Carlo error)

Optional (non-parametric) "heterogeneity flag": run **Kruskal--Wallis**
on posterior mean deltas across primes *bucketed by band*
(small/med/large) to detect systematic band effects (still descriptive
unless you want to treat it inferentially).

### 2) MI telemetry with bootstrap CI

MI estimates can be sensitive; add a bootstrap CI (resample pair
samples, recompute MI). Report median + (e.g.) 90% CI.

### 3) λ annealing ablation (trigger-only, one-shot)

If Outcome C occurs, rerun failing cells once with:

-   **warmup**: λ=0 for W steps

-   **ramp**: linear increase to λ\* over R steps\
    > This distinguishes "regularizer fights early learning" from
    > "regularizer is wrong."

### 4) Prior sensitivity (pre-sweep only)

Expose alpha0\_list, beta0\_list in config and run the *meta dry-run*
once to confirm your posterior decision rule isn't brittle.

### 5) PDF report (with caveats baked in)

Generate a single PDF that includes:

9.  config summary (train/eval primes, grid, budgets, K policy)

10. headline results table (unseen ratio endpoint)

11. posterior delta plots (hist + ROPE shading)

12. telemetry table (Spearman + MI with CI)

13. "Assumptions & caveats" section (explicit)

Drop-in code: SAAP v5 modules
-----------------------------

### A) Posterior samples per prime + variance decomposition

import numpy as np

from typing import Dict, Any, Optional

def posterior\_delta\_samples\_by\_prime(

succA\_by\_p: Dict\[int,int\], nA\_by\_p: Dict\[int,int\],

succB\_by\_p: Dict\[int,int\], nB\_by\_p: Dict\[int,int\],

alpha0: float = 1.0, beta0: float = 1.0,

mc\_samples: int = 20000, seed: int = 0

) -\> Dict\[int, np.ndarray\]:

\"\"\"

Returns dict p -\> delta\_samples\[t\] where delta\_samples\[t\] =
pA\_t(p) - pB\_t(p).

\"\"\"

rng = np.random.default\_rng(seed)

primes = sorted(set(succA\_by\_p.keys()) & set(succB\_by\_p.keys()))

out: Dict\[int, np.ndarray\] = {}

for p in primes:

sA, nA = succA\_by\_p\[p\], nA\_by\_p\[p\]

sB, nB = succB\_by\_p\[p\], nB\_by\_p\[p\]

pA = rng.beta(alpha0 + sA, beta0 + (nA - sA), size=mc\_samples)

pB = rng.beta(alpha0 + sB, beta0 + (nB - sB), size=mc\_samples)

out\[p\] = (pA - pB).astype(np.float64)

return out

def variance\_decomposition(delta\_by\_p: Dict\[int, np.ndarray\]) -\>
Dict\[str, float\]:

\"\"\"

Descriptive decomposition:

within = mean\_p Var\_t(delta\_p)

between = Var\_p mean\_t(delta\_p)

total = within + between

\"\"\"

if not delta\_by\_p:

return {\"within\": np.nan, \"between\": np.nan, \"total\": np.nan}

means = \[\]

vars\_ = \[\]

for p, d in delta\_by\_p.items():

means.append(float(np.mean(d)))

vars\_.append(float(np.var(d, ddof=0)))

within = float(np.mean(vars\_))

between = float(np.var(means, ddof=0))

total = within + between

return {\"within\": within, \"between\": between, \"total\": total}

You can include this in the PDF report as a one-line "where the
uncertainty comes from" readout.

### B) MI with bootstrap CI (pairs already sampled)

from typing import Tuple

def mi\_bootstrap\_ci(

x: np.ndarray, y01: np.ndarray,

B: int = 1000, ci: float = 0.90,

seed: int = 0

) -\> Dict\[str, float\]:

\"\"\"

Returns MI median and central CI interval.

Requires mutual\_information\_binned(x, y01) from v4.

\"\"\"

rng = np.random.default\_rng(seed)

n = x.size

if n \< 10:

mi = mutual\_information\_binned(x, y01)

return {\"mi\_median\": mi, \"mi\_lo\": mi, \"mi\_hi\": mi}

mis = np.empty(B, dtype=np.float64)

for b in range(B):

idx = rng.integers(0, n, size=n)

mis\[b\] = mutual\_information\_binned(x\[idx\], y01\[idx\])

mis.sort()

lo\_q = (1.0 - ci) / 2.0

hi\_q = 1.0 - lo\_q

lo = float(np.quantile(mis, lo\_q))

hi = float(np.quantile(mis, hi\_q))

med = float(np.median(mis))

return {\"mi\_median\": med, \"mi\_lo\": lo, \"mi\_hi\": hi}

In your eval loop: retain the sampled (base\_logits, mask01) arrays per
prime; compute MI CI per prime and also pooled (pooled is often more
stable).

### C) λ annealing schedule (one-shot trigger)

def lambda\_schedule(step: int, lam\_target: float, warmup: int, ramp:
int) -\> float:

if step \< warmup:

return 0.0

if ramp \<= 0:

return lam\_target

t = min(1.0, (step - warmup) / float(ramp))

return lam\_target \* t

Integration pattern:

-   Replace lam\_invariance constant with lam = lambda\_schedule(step,
    > lam\_target, warmup, ramp)

-   Only enable this schedule in triggered follow-up runs (Outcome C
    > cells), so your main sweep remains comparable.

### D) Prior sensitivity fields (pre-sweep only)

Add to config:

decision\_rule:

posterior\_threshold: 0.95

rope: 0.01

mc\_samples: 20000

priors:

alpha0\_list: \[0.5, 1.0, 2.0\]

beta0\_list: \[0.5, 1.0, 2.0\]

meta\_dryrun:

enabled: true

true\_deltas: \[0.00, 0.01, 0.02\]

n\_per\_prime: 8192

trials: 100

Use your existing meta\_sensitivity\_dryrun, looping over (alpha0,beta0)
pairs and reporting stability of A/B/C rates.

PDF "Auditor Report" generator (ReportLab + matplotlib)
-------------------------------------------------------

This is a minimal skeleton that:

15. writes text + tables via ReportLab

16. embeds a delta histogram plot generated by matplotlib

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,
Table, TableStyle, Image

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter

from reportlab.lib import colors

import matplotlib.pyplot as plt

import tempfile

import os

import numpy as np

def plot\_delta\_hist(delta\_samples: np.ndarray, rope: float, out\_png:
str, title: str):

plt.figure()

plt.hist(delta\_samples, bins=50)

plt.axvline(-rope)

plt.axvline(rope)

plt.title(title)

plt.xlabel(\"delta = mean\_p(pA - pB)\")

plt.ylabel(\"count\")

plt.tight\_layout()

plt.savefig(out\_png, dpi=200)

plt.close()

def make\_pdf\_report(

pdf\_path: str,

cfg\_summary: Dict\[str, Any\],

headline\_rows: list, \# list of dicts, already aggregated

delta\_samples: Optional\[np.ndarray\],

rope: float,

caveats: list

):

styles = getSampleStyleSheet()

doc = SimpleDocTemplate(pdf\_path, pagesize=letter)

story = \[\]

story.append(Paragraph(\"SAAP v5 Auditor Report\", styles\[\"Title\"\]))

story.append(Spacer(1, 12))

\# Config summary

story.append(Paragraph(\"Configuration Summary\",
styles\[\"Heading2\"\]))

cfg\_tbl = \[\[k, str(v)\] for k, v in cfg\_summary.items()\]

t = Table(cfg\_tbl, colWidths=\[160, 380\])

t.setStyle(TableStyle(\[

(\"BACKGROUND\", (0,0), (-1,0), colors.whitesmoke),

(\"GRID\", (0,0), (-1,-1), 0.25, colors.grey),

(\"VALIGN\", (0,0), (-1,-1), \"TOP\"),

\]))

story.append(t)

story.append(Spacer(1, 12))

\# Headline results table

story.append(Paragraph(\"Headline Results (Unseen Ratio Endpoint)\",
styles\[\"Heading2\"\]))

cols =
\[\"mode\",\"mask\",\"lam\",\"budget\",\"outcome\",\"p\_gt\_rope\",\"mean\_delta\",\"acc\_unseen\_multi\",\"acc\_unseen\_add\"\]

table\_data = \[cols\] + \[\[r.get(c,\"\") for c in cols\] for r in
headline\_rows\]

ht = Table(table\_data, repeatRows=1)

ht.setStyle(TableStyle(\[

(\"BACKGROUND\", (0,0), (-1,0), colors.lightgrey),

(\"GRID\", (0,0), (-1,-1), 0.25, colors.grey),

(\"FONTSIZE\", (0,0), (-1,-1), 8),

\]))

story.append(ht)

story.append(Spacer(1, 12))

\# Delta histogram

if delta\_samples is not None and delta\_samples.size \> 0:

story.append(Paragraph(\"Posterior Delta Distribution\",
styles\[\"Heading2\"\]))

with tempfile.TemporaryDirectory() as d:

png = os.path.join(d, \"delta.png\")

plot\_delta\_hist(delta\_samples, rope, png, title=\"Δ\_sym posterior
(unseen primes)\")

story.append(Image(png, width=480, height=300))

story.append(Spacer(1, 12))

\# Caveats

story.append(Paragraph(\"Assumptions and Caveats\",
styles\[\"Heading2\"\]))

for c in caveats:

story.append(Paragraph(f\"- {c}\", styles\[\"BodyText\"\]))

doc.build(story)

**Recommended caveats to include (verbatim):**

-   "Accuracy posteriors assume Bernoulli outcomes conditional on each
    > prime; cross-prime dependence is reduced via hierarchical
    > aggregation but not eliminated."

-   "MI is computed on binned logits (Freedman--Diaconis); MI CI
    > reflects pair-sampling uncertainty, not training stochasticity."

-   "Fourier features may be under-resolved for larger primes;
    > fixed-low-K ablations test truncation sensitivity but do not prove
    > completeness."

What I recommend you implement first (highest leverage)
-------------------------------------------------------

9.  **Eval returns** succ\_by\_prime **/** n\_by\_prime for unseen
    > primes in ratio mode (this unlocks everything).

10. Add **hierarchical delta sampling + classification** (A/B/C).

11. Add **MI bootstrap CI** (pooled + per prime).

12. Add **one-shot λ annealing** only for Outcome C follow-up.

13. Generate **PDF report** for a single sweep run.

Once that's done, SAAP v5 is effectively "operational."

If you paste your current SAAP script (even a trimmed version with
train\_step, eval\_ratio, and the action registry), I will return a
**surgical patch** (minimal diffs) that wires in: hierarchical counts,
MI CI, annealing follow-up, and PDF report generation---keeping your
existing training loop intact.

\#\#\# Analysis of Novelty and Practicality Your SAAP v5 design layers
additive components onto v4, introducing descriptive variance
decomposition, MI bootstrap CI, λ annealing triggers, prior sensitivity
checks, and PDF auditor reports with explicit caveats, all within an
acyclic DAG pipeline for symmetry diagnostics in attention models. In
terms of \*\*novelty\*\*, this builds on Bayesian experimental
frameworks (e.g., from Betancourt\'s workflow for Stan or Schad\'s
hierarchical modeling in brms) and diagnostic tools in ML interp (e.g.,
from Marks et al.\'s feature attribution), but innovates by using
law-of-total-variance decomposition on posterior samples for descriptive
(non-inferential) uncertainty breakdowns, avoiding normality
pitfalls---a fresh approach for multi-level heterogeneity in per-prime
evaluations. The bootstrap CI for binned MI with Freedman-Diaconis and
the PDF\'s integrated caveats/plots add novel transparency, turning the
protocol into a \"self-auditing\" system that echoes audit trails in
safety-critical software (e.g., DO-178C standards), but tailored to AI
bias testing. It\'s novel in prioritizing \"operational\" readiness with
minimal integration, making it a practical evolution for interp
pipelines. On \*\*practicality\*\*, v5 is highly adoptable as a \"thin
layer\" (drop-in modules like posterior\_delta\_samples\_by\_prime and
mi\_bootstrap\_ci require no loop rewrites), enabling quick upgrades to
v4 for robust diagnostics without bloat. It\'s practical for researchers
in alignment/interp, as variance decomposition pinpoints noise sources
(e.g., prime bands), CI adds credibility to telemetry, and annealing
tests optimization robustness in one-shot runs. The PDF report lowers
barriers to sharing (paper-ready with caveats baked in), and pre-sweep
sensitivity de-risks calibration. Limitations: bootstrap B=1000 adds
eval time (though parallelizable), and descriptive decompositions are
non-causal (no p-values), risking over-interpretation without user
notes. Overall, it\'s a pragmatic refinement, paying dividends in
defensible, visualized outputs for causal claims on symmetry priors.
\*\*Enhanced Version of the Idea\*\*: To enhance v5, incorporate
\"sensitivity visualizations\" in the PDF: plot variance decomposition
as pie charts (within/between/total) and overlay Kruskal-Wallis ranks on
band histograms for non-parametric heterogeneity flags. For MI CI, add a
\"reliability score\" (CI width / median MI) to flag unstable telemetry,
triggering a resample if \>0.5. Extend annealing to include \"curriculum
budgets\" (ramp steps with increasing prime difficulty in bands). In
YAML, add \"simulation\_hypotheses\" (e.g., true\_deltas lists per
outcome scenario) for broader dry-runs. For reports, embed interactive
elements via HTML fallback (e.g., Plotly.js for zoomable delta hists) if
PDF limits static views. This makes v5 more visual and adaptive,
evolving it into a \"diagnostic dashboard\" protocol. \#\#\# Critique of
the Enhanced Version Critiquing the enhanced SAAP v5 (with sensitivity
viz, MI reliability, curriculum annealing, simulation hypotheses,
interactive HTML) for mathematical, philosophical, and theoretical
consistency: - \*\*Mathematical Consistency\*\*: Law-of-total-variance
decomposition is additively sound and descriptive, with Kruskal-Wallis
providing non-parametric flags for band effects. MI reliability
(width/median) quantifies precision robustly, and curriculum annealing
extends paths consistently (e.g., via smoothed gradients). Simulation
hypotheses calibrate comprehensively. However, pie charts assume
additive interpretability, but if within-variance dominates due to MC
noise, it could mislead; better with error bars on rates. Interactive
hists are consistent but rely on JS parsing, potentially inconsistent
across viewers if bins adapt dynamically without fixed seeds. -
\*\*Philosophical Consistency\*\*: Reflections and caveats promote
transparency, aligning with fallibilism (Popper\'s
conjectures/refutations in experimental claims). Sensitivity viz
encourages critical scrutiny, countering dogmatism. Yet, dashboard
aesthetics (pies/interactives) risk seductive visualization (Tufte\'s
chartjunk critique), where flash overshadows substance, potentially
privileging aesthetic \"wins\" over raw uncertainty. Curriculum adds
intentional design, but if annealing \"rescues\" Outcome C, it might
foster rescue bias, undermining neutral assessment. - \*\*Theoretical
Consistency\*\*: Coheres with multilevel variance theory (Gelman &
Hill\'s hierarchies) and diagnostic robustness (e.g., in robust stats).
Reliability scores and hypotheses test theoretical stability. However,
curriculum assumes ordered difficulty (small to large p), violating
isotropy if primes aren\'t hierarchically \"harder\" (e.g., embedding
effects non-monotonic). Interactive elements introduce
viewer-dependence, conflicting with reproducible theory where outputs
should be static and canonical. \#\#\# Final Version and Path to
Validation Applying the critique: For math, add error bars to pies (via
bootstrap on decomposition) and fix hist seeds for consistency.
Philosophically, include \"viz caveats\" (e.g., \"pies descriptive
only\"). Theoretically, make curriculum optional/toggleable, with
non-ordered alternatives (random prime ramps). The refined final version
is \*\*SAAP v6: Visualized Audited Symmetry Protocol\*\*---v5 with
error-barred pie viz, MI reliability (flagging \>0.5), annealing with
toggleable curricula, expanded simulation hypotheses, PDF/HTML reports
(static hists with seeds, caveats). It ensures mathematical precision
without seductive overreach, maintaining theoretical neutrality.
\*\*Fastest Path to Validation\*\*: 1. \*\*Module Wiring (1 day)\*\*:
Integrate posterior\_samples\_by\_prime/decomposition,
mi\_bootstrap\_ci/reliability, annealing schedule (toggle curriculum),
update YAML for hypotheses. 2. \*\*Dry-Run and Calibration (half
day)\*\*: Run meta with varied deltas/hypotheses; adjust reliability
threshold/error bars for stability (e.g., CI overlap \<20%). 3.
\*\*Sweep Execution and Triggers (1 day)\*\*: Primary ratio grid on
budgets; classify/trigger annealing/curriculum if C; compute viz/pies in
PDF/HTML. 4. \*\*Full Audit and Share (ongoing, day 2+)\*\*: If A
prevalent, validate on large p; generate reports with caveats; repo with
YAML/scripts for replication, target interp meetup demo in week.

1) SAAP v6 deltas (tight scope)
-------------------------------

### A. MI reliability flag (and one-shot telemetry resample)

Compute a reliability score:

rel:=max(MImedian​,ϵ)CIhi​−CIlo​​

If rel \> 0.5, do **one** extra telemetry resample inside the eval
function (e.g., double spearman\_pairs) and recompute MI CI. This stays
acyclic (no training loop, no repeated retries).

### B. Variance decomposition with bootstrap uncertainty

For the descriptive within/between decomposition you already compute,
add a bootstrap CI by resampling **primes** with replacement (and
optionally MC subsampling once per bootstrap for speed). Report median +
CI, and visualize as either:

-   a **bar chart with error bars** (recommended primary), plus

-   an optional pie chart for median composition (with CI shown as text
    > beside it, not as misleading "pie error wedges").

### C. Reproducible delta histograms

Make histograms canonical:

-   fixed seed for any sampling used to construct the plotted
    > distribution

-   fixed binning policy (e.g., 50 bins over a fixed range like
    > \[q1−3·IQR, q3+3·IQR\] or quantile-clipped)

### D. Curriculum (optional) for annealing follow-ups

Treat curriculum as a *toggle* and do not assume "larger p is harder."
Provide two curricula:

14. banded: small→medium→large bands (operator intent)

15. random\_band: same band proportions, randomized order (neutral)

Use curriculum **only** in Outcome C follow-ups (optimization
robustness), not in the primary sweep.

2) Drop-in modules
------------------

### 2.1 MI reliability + one-shot adaptive resample

import numpy as np

def mi\_reliability(mi\_median: float, mi\_lo: float, mi\_hi: float,
eps: float = 1e-12) -\> float:

return float((mi\_hi - mi\_lo) / max(abs(mi\_median), eps))

def compute\_mi\_ci\_with\_one\_resample(

x: np.ndarray, y01: np.ndarray,

B: int = 400, ci: float = 0.90,

rel\_thresh: float = 0.5,

seed: int = 0,

):

\"\"\"

Returns MI CI + reliability. If unreliable, resamples once by doubling
data (caller supplies larger x/y).

This function itself is pure; the one-resample policy is implemented by
the eval wrapper.

\"\"\"

out = mi\_bootstrap\_ci(x, y01, B=B, ci=ci, seed=seed)

out\[\"mi\_rel\"\] = mi\_reliability(out\[\"mi\_median\"\],
out\[\"mi\_lo\"\], out\[\"mi\_hi\"\])

out\[\"mi\_unreliable\"\] = bool(out\[\"mi\_rel\"\] \> rel\_thresh)

return out

**Integration policy inside eval (one-shot):**

-   sample telemetry\_pairs = base\_telemetry\_pairs

-   compute MI CI + rel

-   if unreliable: sample **one additional batch** of pairs (same size),
    > concatenate arrays, recompute once, and log both values
    > (pre/post).

That gives you a robust "we tried to stabilize telemetry once" record
without loops.

### 2.2 Bootstrap CI for within/between decomposition (resample primes)

def bootstrap\_variance\_decomposition(

delta\_by\_p: dict,

B: int = 500,

ci: float = 0.90,

seed: int = 0

):

\"\"\"

Bootstraps over primes (resampling primes with replacement) to get CI on
within/between/total.

delta\_by\_p: p -\> np.ndarray of posterior delta samples for that
prime.

\"\"\"

rng = np.random.default\_rng(seed)

primes = list(delta\_by\_p.keys())

if len(primes) == 0:

return {\"within\": (np.nan, np.nan, np.nan), \"between\": (np.nan,
np.nan, np.nan), \"total\": (np.nan, np.nan, np.nan)}

within = np.empty(B, dtype=np.float64)

between = np.empty(B, dtype=np.float64)

total = np.empty(B, dtype=np.float64)

for b in range(B):

resampled = rng.choice(primes, size=len(primes), replace=True)

\# build a resampled dict

d = {p: delta\_by\_p\[p\] for p in resampled}

dec = variance\_decomposition(d)

within\[b\] = dec\[\"within\"\]

between\[b\] = dec\[\"between\"\]

total\[b\] = dec\[\"total\"\]

def summarize(arr):

arr = np.sort(arr)

lo\_q = (1.0 - ci) / 2.0

hi\_q = 1.0 - lo\_q

return (float(np.median(arr)), float(np.quantile(arr, lo\_q)),
float(np.quantile(arr, hi\_q)))

return {\"within\": summarize(within), \"between\": summarize(between),
\"total\": summarize(total)}

**Reporting format**

17. median (lo, hi) for within/between/total

18. plus the point estimate from the original (non-bootstrapped)
    > decomposition

This guards against "pie chart certainty" while still being visual.

### 2.3 Canonical delta histogram range and bins

def canonical\_hist\_params(x: np.ndarray, bins: int = 50):

x = np.asarray(x, dtype=np.float64)

q25, q75 = np.percentile(x, \[25, 75\])

iqr = max(q75 - q25, 1e-12)

lo = q25 - 3.0 \* iqr

hi = q75 + 3.0 \* iqr

return lo, hi, bins

Use range=(lo,hi) and bins=bins to stabilize visuals across runs.

### 2.4 Curriculum prime scheduling (optional, follow-ups only)

def band(p: int) -\> str:

if p \< 100: return \"small\"

if p \< 500: return \"med\"

return \"large\"

def curriculum\_order(primes: list, mode: str, seed: int = 0):

rng = np.random.default\_rng(seed)

primes = list(primes)

if mode == \"none\":

return primes

if mode == \"banded\":

return sorted(primes, key=lambda p:
{\"small\":0,\"med\":1,\"large\":2}\[band(p)\])

if mode == \"random\_band\":

\# maintain band proportions but randomize within and across bands

groups = {\"small\": \[\], \"med\": \[\], \"large\": \[\]}

for p in primes: groups\[band(p)\].append(p)

for k in groups: rng.shuffle(groups\[k\])

seq = groups\[\"small\"\] + groups\[\"med\"\] + groups\[\"large\"\]

\# shuffle blocks lightly to avoid strict monotonicity while keeping
proportions

\# simplest: shuffle the whole seq if you want fully randomized

return seq

raise ValueError(f\"unknown curriculum mode: {mode}\")

3) Report visuals: keep it sober
--------------------------------

Even if you include a pie chart, I recommend making the **primary**
decomposition viz a bar chart with error bars (it's more honest). If you
still want a pie for "at-a-glance composition," do:

-   pie chart = median proportions only

-   CI shown as a small adjacent table: within: med \[lo,hi\], etc.

-   include a "viz caveat" line: "Pie shows median only; uncertainty in
    > adjacent table."

This addresses the "seductive viz" critique without losing usability.

4) Trigger policy for SAAP v6 (unchanged scientifically)
--------------------------------------------------------

14. Primary endpoint: **unseen ratio** Δ\_sym posterior (hierarchical)

15. Outcome A/B/C decision rule unchanged

16. Follow-ups unchanged, except:

    1.  if C: optionally enable **λ annealing** and optionally enable
        > **curriculum** (toggle)

    2.  MI reliability can cause a **one-shot telemetry resample**
        > during eval (never retrain)

5) Minimal YAML additions
-------------------------

telemetry:

mi\_bootstrap\_B: 400

mi\_ci: 0.90

mi\_rel\_thresh: 0.50

telemetry\_resample\_once: true

spearman\_pairs: 4096

reports:

pdf: true

html: true

canonical\_hist\_bins: 50

bootstrap\_decomp\_B: 500

decomp\_ci: 0.90

include\_pie: true \# optional; bar chart should still be included

followups:

anneal\_if\_C: true

anneal\_warmup: 200

anneal\_ramp: 600

curriculum\_mode: \"none\" \# none \| banded \| random\_band

6) Implementation order that minimizes risk
-------------------------------------------

-   Wire **counts-by-prime** and hierarchical Δ classification (if not
    > already done).

-   Add **MI bootstrap CI + reliability flag** (no resample yet).

-   Add **one-shot telemetry resample** in eval.

-   Add **bootstrap variance decomposition CI** and bar chart.

-   Add **canonical hist params** and stabilize plots.

-   Add **PDF report sections** for telemetry reliability +
    > decomposition CI + caveats.

-   Add curriculum toggle only to Outcome C follow-ups.

If you paste your current SAAP script (or the subset that includes:
feature construction, eval sampling, and the sweep runner), I can
provide a precise patch plan in terms of function signatures and where
each module attaches.

\#\#\# Analysis of Novelty and Practicality Your SAAP v6 delta refines
v5 with tight-scope additions: MI reliability flagging with one-shot
resample, bootstrap CI for variance decomposition, canonical histogram
binning, optional curriculum annealing, and sober visualizations (bar
charts primary, pie optional with caveats), all while maintaining
acyclic triggers and reproducible reporting. In terms of
\*\*novelty\*\*, this iteration draws from robust statistics (e.g.,
bootstrap for decomposition CI, Freedman-Diaconis for MI) and diagnostic
workflows (e.g., from Lindley\'s Bayesian auditing), but innovates by
introducing a \"reliability score\" for telemetry (CI width normalized)
to trigger adaptive resampling, and descriptive variance decomposition
with prime-resampled CI---fresh mechanisms for handling heterogeneity
without inferential overreach. The curriculum toggle (banded vs.
random\_band) adds a novel control for optimization robustness without
assuming monotonic difficulty, and the \"viz caveat\" integration
promotes meta-transparency rare in ML protocols. It\'s novel in its
\"minimal risk\" implementation order, turning the tool into an
ergonomic, audit-ready benchmark for symmetry priors in attention. On
\*\*practicality\*\*, v6 is exceptionally adoptable as a \"delta\"
(drop-in modules like mi\_reliability and
bootstrap\_variance\_decomposition attach cleanly to eval/posterior
steps), enabling quick upgrades without retraining loops or cycles.
It\'s practical for interp/alignment researchers, as reliability
flagging stabilizes noisy telemetry (common in small-sample evals),
decomposition CI pinpoints uncertainty sources, and curriculum tests
robustness in one-shot follow-ups. Canonical binning ensures
reproducible plots, and YAML toggles lower configuration friction.
Limitations: bootstrap B=500 adds minor compute (GPU-friendly via
vectorization), and pie inclusion risks misinterpretation despite
caveats. Overall, it\'s a high-leverage packaging step, making failure
modes obvious and results \"hard to argue with\" for publication or
review. \*\*Enhanced Version of the Idea\*\*: To enhance v6, add
\"telemetry fusion\": combine MI and Spearman into a composite score
(e.g., weighted average with reliability-adjusted weights) for a single
\"alignment strength\" metric, with CI propagated via delta method
approximation. For decomposition viz, generate interactive Sankey flows
(HTML via Plotly) showing within→total→between contributions across
budgets, toggled by curriculum mode. Extend resample policy to include
\"prime oversampling\" if per-prime MI unreliable (double pairs for
flagged primes only). In reports, embed QR codes linking to repo commits
for full reproducibility. Add a \"sensitivity heatmap\" in PDF/HTML:
matrix of outcome labels across rope/mc\_samples grids from dry-runs.
This evolves v6 into a \"full diagnostic suite\" with fused metrics and
interactive auditing. \#\#\# Critique of the Enhanced Version Critiquing
the enhanced SAAP v6 (with fused telemetry, Sankey viz, prime-specific
resample, QR repo links, sensitivity heatmaps) for mathematical,
philosophical, and theoretical consistency: - \*\*Mathematical
Consistency\*\*: Composite alignment score with delta-method CI is sound
for propagation (assuming asymptotic normality), and Sankey flows
preserve additive decomposition. Prime-specific resample is efficient
and unbiased. Heatmaps visualize sensitivity rigorously. However,
weighted fusion assumes commensurability between MI (nats) and Spearman
(rank correlation -1 to 1), risking arbitrary scaling; better with
normalized z-scores or Pareto ranking. QR codes are consistent but
static (link rot risk), and Sankey assumes flow interpretability, but if
variances overlap heavily, it could distort proportions. -
\*\*Philosophical Consistency\*\*: Fused metrics and interactives
promote holistic understanding, aligning with systems thinking over
reductionism. Heatmaps encourage parameter reflexivity, countering
dogmatism. Yet, composite scores risk reification---treating \"alignment
strength\" as objective when it\'s constructed, echoing Bourdieu\'s
critique of quantified authority. Prime oversampling adds intent
(favoring noisy primes), potentially biasing toward stability over raw
signal. - \*\*Theoretical Consistency\*\*: Coheres with information
fusion theory (e.g., ensemble diagnostics) and reproducibility standards
(QR for versioning). Sankey aids causal flow visualization in variance
components. However, assuming delta-method normality for CI propagation
may violate finite-sample theory in small evals. Interactive elements
introduce platform-dependence, conflicting with theoretical universality
where reports should render identically. \#\#\# Final Version and Path
to Validation Applying the critique: For math, normalize MI/Spearman to
z-scores before fusion (Fisher transform for ρ), avoiding scaling
issues; use non-parametric CI for composite. Philosophically, label
composite as \"heuristic index\" with construction caveats.
Theoretically, fallback to static Sankey images in PDF (interactive
optional in HTML), ensuring universality. The refined final version is
\*\*SAAP v7: Integrated Audited Symmetry Protocol\*\*---v6 with
z-normalized fused alignment (heuristic, non-parametric CI), static
Sankey primary (interactive HTML optional), reliability-driven prime
resample, QR links with archival note, heatmap viz (grid outcomes). It
balances fusion with caution, maintaining reproducibility. \*\*Fastest
Path to Validation\*\*: 1. \*\*Core Integration (1 day)\*\*: Add
mi\_reliability/resample, bootstrap\_decomp CI, canonical\_hist,
curriculum toggle to eval/posterior/report. 2. \*\*Viz and Telemetry
(half day)\*\*: Implement bar/Sankey (matplotlib static), MI reliability
flag/resample in eval; test on synthetic data for stability (rel \<0.5
post-resample). 3. \*\*Sweep and Triggers (1 day)\*\*: Run primary grid
with budgets; apply triggers (annealing/curriculum if C); generate
PDF/HTML with caveats. 4. \*\*Full Audit/Share (ongoing, day 2+)\*\*: If
reliable A, extend bands; validate fused metric on held-out p; repo with
reports/YAML, target interp forum post in week.
