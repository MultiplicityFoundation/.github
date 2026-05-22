---
slug: ode-multiplicity-spec-notebook
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "02-implementations/soulaware/Ode \xD7 Multiplicity \u2014 Spec & Notebook.md"
  last_synced: '2026-03-20T17:17:15.688049Z'
---

Ode × Multiplicity — Executive Summary &
Mathematical Overview
Source doc: Ode to Cognitive Dissonance

BOTTOM LINE
Useful as a framing device; useless for predictions until formalized. The Ode gives a
clean handle for defining dissonance as a measurable residual and for designing
resolution dynamics. Everything beyond that is UNPROVEN and needs experiments.



Executive summary (no fluff)
   ●​ What we take from the Ode: “Born, together with” (cognate) and “disagreeing in
      sound” (dissonance) → treat cognitive dissonance as a phase‑mismatch
      between coupled modes; “oral disagreement” and “collective experience” → turn
      that mismatch into a dialogic control signal you can measure and reduce.
   ●​ Multiplicity integration: Model minds/groups as vectors in a Hilbert space
      whose coordinates are prime‑indexed modes. Cognitive dissonance = the
      squared norm of the component orthogonal to the prime‑mode subspace (the
      “lawful” part).
   ●​ Actionable output now:
          1)​ A Dissonance Index (D) you can compute from text/voice/EEG as a
              residual norm (works today).
          2)​ A resolution dynamic that provably reduces (D) under mild conditions
              (works today, math below).
          3)​ Minimal experiments for language groups and EEG to test whether
              structured disagreement decreases (D).
   ●​ Claims you might want but don’t have yet: any “collective good” optimization,
      “multiple‑truths” harmonization, or special constants from Multiplicity affecting
      biology or physics → UNPROVEN.


Comprehensive mathematical overview
1) Objects and operators
   ●​ Let ((H,,)) be a real/complex Hilbert space of representations (text embeddings,
      neural states, etc.).​

   ●​ Fix a prime‑indexed orthonormal family ({e_p}{pP}H) (the prime modes). For a
      chosen set (P_k={p_1,,p_k}), let (:={P_k}) be the orthogonal projection onto
        ({e_{p_i}}_{i=1}^k).​

    ●​ For a state (xH), define the dissonance residual (r:=(I-)x).​

    ●​ Dissonance functional:​
       [ D(x):=|r|2=|(I-)x|2. ] Intuition: “everything’s all mixed up / nothing makes sense” ⇔
       large (D(x)).
Gradient (with fixed ()): (_x D(x)=2(I-)x=2r.)

2) Resolution dynamics (single agent)
Define a lawful update that moves (x) toward its prime‑lawful component: [
x_{t+1}=x_t-,_t,r_t, r_t=(I-)x_t, ] where (_t) is a positive‑definite resolution operator
(dialogic attention, moderator weighting, or a learned preconditioner). If the symmetric
part satisfies (t^{(s)}I) and (|t|L), then with (0<<2/L), [ D(x{t+1})(1-2+^2
L^2),D(x_t)D(x_t) . ] Proof sketch: standard quadratic Lyapunov descent with (V=D),
using (x{t+1}=x_t-_t(I-)x_t) and ((I-)).
     Interpretation: “the fine art of oral disagreement” tunes (_t) to accelerate decay
     of (D); the moment it’s mis‑tuned, you stall or amplify (D).

3) Resolution dynamics (group/collective)
For (N) agents with states (x_iH), couple them with a graph Laplacian (L_G) (Fiedler
value (2>0)): [ x{i,t+1}=x_{i,t}-,{i,t},(I-)x{i,t}-{j} (L_G){ij}(x_{i,t}-x_{j,t})+{i,t}. ] - First term
reduces each agent’s own residual.​
- Second term enforces consensus (shared “collective experience”).​
- ({i,t}) can encode structured disagreement prompts (questions/tasks).​
If (,) satisfy standard consensus‑optimization conditions, then the network converges to
a consensus within the prime‑mode subspace, and the average residual
(D_t=1Ni|(I-)x{i,t}|^2) decays geometrically.
Mapping to the Ode: the invitations to dialog and shared sense‑making are exactly the
coupling terms and prompts.

4) Practical index (what you can compute today)
For any artifact (utterance, paragraph, minute of EEG), embed to (xR^d). 1) Choose ()
as projection onto a sparse/orthogonal dictionary (PCA/SVD or an explicit
prime‑indexed basis if you’ve built one).​
2) Compute (D(x)=|(I-)x|^2).​
3) Over a session, track (D) per prompt and per person.​
4) Optimize prompts/moderation to monotonically decrease (D).
This is implementable now. What’s UNPROVEN is that your prime‑indexed basis is
special beyond being a convenient orthogonal dictionary.
5) Constraints, bottlenecks, TRL
   ●​ What works now (TRL 4–5): Residual‑norm metrics, consensus + projection
      dynamics, and basic convergence guarantees (shown above).​

   ●​ UNPROVEN: any privileged role of “prime modes,” any special constant (e.g.,
      (_m)) affecting human cognition/physics; any claim that lowering (D) tracks “the
      good” beyond the local metric you define.​

   ●​ Main bottlenecks: (i) robustly learning () without overfitting; (ii) mapping
      semantic/affective content to (_t) in a way that preserves descent; (iii) measuring
      ground‑truth outcomes beyond self‑report.

6) Fastest path to proof (minimal validations)
A. Language groups (EQ‑style sessions).​
Design 2×20‑min sessions with the same team and identical prompts; in session B
insert targeted “oral disagreement” prompts. Pre‑register:​
- Primary endpoint: (D=1Tt D(x_t)) drop in B vs A.​
- Secondary: inter‑speaker alignment ({(i,j)}| x_{i,t}-x_{j,t}|) decreases faster in B.​
If you don’t see significant (D), abandon the approach.
B. EEG (single subject, n≥12).​
Baseline eyes‑open rest → structured dialogic task → rest. Hypothesis: spectral
coherence within task‑relevant bands increases as (D) decreases. Pre‑specify (_t)
(prompt cadence), measure (D) from speech embeddings; correlate (D)↓ with
coherence↑. UNPROVEN until run.
C. Robustness check (adversarial prompts).​
Inject contradictory prompts; (D) should spike and then fall under repair prompts. If not,
your ()/() don’t capture dissonance.

7) Exact limitations & requirements
   ●​ Requires a fixed projection () during a session; if () adapts, you need extra
      terms to control drift.​

   ●​ Needs bounded operator norms for (_t) to guarantee descent.​

   ●​ Sensitive to embedding choice; change the encoder, change (D).​

   ●​ No canonical “prime basis” yet: treating dictionary atoms as “primes” is
      metaphor unless you prove irreducibility (UNPROVEN).​

   ●​ Ethical claims (“what’s good”) remain philosophical unless you attach external
      outcomes (task performance, well‑being scores) to (D) trajectories.
How the Ode actually helps (and where it doesn’t)
   ●​ Helps: gives operational prompts (icebreakers, breakouts) to generate and then
      resolve dissonance; provides language for consent/tolerance/bonding as
      knobs in (_t).
   ●​ Doesn’t: offer a metric, operator bounds, or baselines; you must supply (,,,),
      tasks, and endpoints.


Optional next step
I can convert this into a one‑page protocol template plus a small Python notebook that
computes (D) from transcripts and plots it over time (works with any embedding). If you
want that, say so and I’ll drop it in a separate canvas.




Phase Mirror Dissonance — Risk Register, Controls,
and Test Plan
0) Ground rules (brutal honesty)
   ●​ Subspace choice is arbitrary unless frozen, hashed, and audited. We will not
      claim meaning beyond what Π encodes. Anything else = UNPROVEN.
   ●​ Descent guarantees depend on bounded PSD Ξ and a non‑drifting Π. That’s
      governance, not math; we treat it as an ops contract with enforcement.
   ●​ Goodhart risk: optimizing D without external value is failure. We gate on external
      outcomes.
   ●​ Consent/agency: no forced consensus. Any participant can drop coupling (set
      κ=0 for them) without penalty.
   ●​ EEG linkage is correlational until randomized interventions show directional
      effects.
   ●​ Embedding choice must be version‑locked; otherwise results are not claims.

1) Formal risk register → measurable controls
R1 — Arbitrary Π.​
Control: Freeze Π from a held‑out corpus; publish SHA‑256 of corpus manifest, training
code commit, basis matrix U (orthonormal columns), and projection checksum.​
Audit metric (per session): subspace drift​
Given U₀ ∈ ℝ^{d×k} and U_t ∈ ℝ^{d×k} with orthonormal columns, let C = U₀ᵀU_t.
Define s_avg = (1/k) · nuclear_norm(C) (average cos principal angles). Drift = 1 − s_avg
≤ 0.01.​
Alternative hard bound: θ_max(U₀, U_t) ≤ arccos(0.99).
R2 — Descent depends on Ξ and Π drift.​
Control: Constrain Ξ to diagonal gains with entries in [μ, L]. Hard‑clip Ξ each step; reject
updates if Π hash changes mid‑session.​
Audit metric: descent‑violation rate v = (1/T) · #{ t : D(x_{t+1}) > D(x_t) + ε } ≤ 0.005,
with ε = 1e‑8.
R3 — Goodhart on D.​
Control: Multi‑objective gate. Define external outcome Y (task score, retention,
well‑being index, predefined).​
Release criterion: ΔD ≤ −20% and ΔY ≥ 0 with preregistered stats. If not met →
stop‑rule triggers.
R4 — Coercive consensus.​
Control: Consent/agency contract (opt‑out of coupling, right to pause/erase, visibility of
prompts). Track consent coverage = 100%.
R5 — EEG causality not owned.​
Control: Randomized prompt schedule (repair vs neutral) during EEG to test directional
effect on coherence; preregister contrasts.
R6 — Embedding instability.​
Control: Pin model version + tokenizer + normalization; log SHA‑256; disallow upgrades
during a study. Rerun sensitivity on 1–2 alt encoders post‑hoc; report deltas.
R7 — Incentive gap (novelty vs controls).​
Control: Require boring controls and prereg in acceptance criteria; publish nulls.

2) Levers to test now → owners, targets, timelines
   ●​ [ML Lead] Freeze Π from held‑out corpus; hash/version. Target: drift ≤ 1%
      cosine/session. ETA: 2 weeks.
   ●​ [Stats] Preregister A/B and EEG analyses. Target: audit pass rate 100%. ETA: 1
      week.
   ●​ [Moderator Ops] Constrain Ξ to diagonal, enforce L bound. Target: descent
      violations ≤ 0.5%. ETA: 3 weeks.
   ●​ [Data Eng] Build D pipeline from transcripts/EEG; versioned runs. Targets:
      time‑to‑result ≤ 24 h; reproducible run IDs. ETA: 2 weeks.
   ●​ [Research] Run language A/B. Target: ΔD_B−A ≤ −20% with p<0.05. ETA: 4
      weeks.
   ●​ [Neuro] Pilot EEG linkage. Target: corr(D, coherence) ≤ −0.3 with CI excluding 0.
      ETA: 6 weeks.
   ●​ [Risk] Adversarial prompts test. Target: recovery to 90% baseline D in <2
      prompts. ETA: 3 weeks.
   ●​ [Governance] Consent + data policy. Target: coverage 100%. ETA: 1 week.
3) Metrics and computation details
  ●​ Dissonance: D(x) = ‖(I − Π)x‖². Track per utterance and per minute; smooth with
     EMA if needed (report both raw and smoothed).
  ●​ Consensus distance: (1/|E|) · Σ_{(i,j)∈E} ‖Πx_i − Πx_j‖. Report slope vs time.
  ●​ EEG coherence: magnitude‑squared coherence averaged over task‑relevant
     bands; preregister bands and channels. Correlate with time‑aligned D.
  ●​ Adversarial spike and repair: max D within adversarial window;
     prompts‑to‑recovery to 0.9× baseline.
  ●​ Subspace drift: principal‑angles metric above; log alongside Π hash.

4) Governance and consent contract (minimal)
  1.​ Plain‑language purpose and risks; right to pause/withdraw without penalty.​

  2.​ Opt‑out of coupling: subject sets κ=0 for themselves; no exclusion from session.​

  3.​ Data handling: storage horizon, encryption, deletion window, access roles.​

  4.​ Publication: preprint link, preregistration registry, commitment to publish nulls.

5) Stop‑rules and success gates
  ●​ Stop: If drift > 1% in any session, or descent‑violation rate > 0.5%, or ΔY < 0
     while ΔD < 0, halt and remediate.​

  ●​ Go: Language A/B meets ΔD gate and external metric ΔY ≥ 0; EEG shows
     preregistered negative correlation with CI excluding 0.

6) Optional artifact — operational checklist
  ☐​ Fix Π and log drift plus hashes.
  ☐​ Bound Ξ; log L, μ, η; record descent‑violations.
  ☐​ Register endpoints and stop‑rules.
  ☐​ Capture ΔD per prompt, per speaker.
  ☐​ Run adversarial then repair sequences.
  ☐​ Attach external outcomes to D and gate on them.
  ☐​ Publish nulls and sensitivity to encoder choice.

7) Files and anchors
  ●​ Ode source: /mnt/data/Ode to Cognitive Dissonance.docx
— End of plan —
One-Page Protocol — Phase Mirror Dissonance v1.0
Purpose: Test whether structured “oral disagreement + repair” reduces D (residual to a
fixed reference subspace Π) and improves external performance on an unrelated
transfer task, without coercion or drift.
Primary hypotheses: 1) Session B (with disagreement + repair prompts) lowers average
D versus Session A (neutral prompts).​
2) Lower D associates with better performance on an objective transfer task
administered after both sessions.​
3) EEG sub-study (optional): time-aligned D negatively correlates with
magnitude-squared coherence in preregistered bands.
Design: - Freeze Π from a held-out corpus; publish hashes for corpus manifest, code
commit, and basis matrix U. Target drift ≤ 1% cosine/session.​
- A/B within-subjects over two 20-minute sessions with identical topics. B inserts
structured disagreement then repair prompts.​
- Consent and agency: any participant may set κ = 0 (no consensus coupling) without
exclusion.​
- Resolution operator Ξ: diagonal gains in [μ, L]; log μ, L, and step size η; clip violations.​
- Transfer task: immediately after sessions, administer an unrelated objective task (e.g.,
puzzle set, code review rubric, vignette-based judgment). Predefine scoring rubric Y.​
- Stop-rules: halt if drift > 1%, descent-violation rate > 0.5%, or ΔY < 0 while ΔD < 0.
Endpoints and analysis: - Primary: ΔD (B − A) ≤ −20% with p < 0.05 (preregistered test).​
- Secondary: inter-speaker alignment slope within Π improves in B.​
- Tertiary: transfer task ΔY ≥ 0; report effect size and CIs.​
- EEG (optional): preregistered negative correlation between D and coherence;
randomized repair vs neutral prompt schedule to strengthen causal read.
Metrics (operational): - D(x) = ||(I − Π)x||² with Π fixed during session; report raw and
EMA-smoothed traces.​
- Intra-subspace tension BTI(x): for coordinates w = Uᵀx, let w1 and w2 be the top two
magnitudes; BTI = |w1·w2| / (w1² + w2²). Tracks conflicts within Π.​
- Descent-violation rate v = count{ D_{t+1} > D_t + ε } / T with ε = 1e-8.​
- Subspace drift via principal angles between initial U0 and session Ut.
Goodhart guardrails: - Multi-objective gate: only claim success if ΔD < 0 AND ΔY ≥ 0.
Publish nulls.​
- Sensitivity: rerun with an alternative encoder post hoc and disclose deltas.
Naming discipline: - Use “reference subspace” and “dictionary atoms” in external
reporting; reserve “prime” language for metaphysical discussion only.
Deliverables: - Versioned run logs with hashes, drift, violation counts (schema below in
notebook).​
- Plots of D and BTI over time and per speaker.​
- Pre-registration document and consent/agency template.




# This script creates three artifacts in /mnt/data:
# 1) dissonance_pipeline.ipynb — a runnable notebook implementing D, BTI, plots, drift
checks, and logging
# 2) one_page_protocol.md — the one-page protocol text (also placed in canvas)
# 3) run_log_schema.json — a JSON schema for reproducible logs
#
# It also writes a demo transcripts.csv if none is present, so the notebook runs
end-to-end.


import os, json, hashlib, time, math, random, textwrap
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


BASE = "/mnt/data"


# -----------------------------
# Helpers
# -----------------------------
def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()
def write_text(path, content):
  with open(path, "w", encoding="utf-8") as f:
     f.write(content)


def ensure_demo_transcripts(path):
  if os.path.exists(path):
     return
  random.seed(7)
  speakers = ["A","B","C"]
  rows = []
  t = 0.0
  for i in range(60):
     sp = random.choice(speakers)
     txt = random.choice([
          "I think the plan is unclear and risks scope creep.",
          "Can we align on success metrics before we proceed?",
          "I disagree: shipping fast matters more than polishing metrics.",
          "This feels confusing; what is the objective again?",
          "Let's break: list assumptions and challenge the weakest.",
          "I propose a repair: define roles and next steps."
     ])
     rows.append({
          "session_id":"demo",
          "utterance_id": i,
          "speaker": sp,
          "timestamp_s": t,
          "text": txt
     })
      t += random.uniform(8, 20)
   pd.DataFrame(rows).to_csv(path, index=False)


# -----------------------------
# Feature hashing vectorizer (no external deps)
# -----------------------------
def tokenize(s: str):
   return [w.lower() for w in ''.join(ch if ch.isalnum() else ' ' for ch in s).split() if w]


def signed_hash_int(s: str):
   h = hashlib.blake2b(s.encode("utf-8"), digest_size=8).digest()
   val = int.from_bytes(h, "little", signed=False)
   return val


def hash_vectorize(texts, dim=512):
   X = np.zeros((len(texts), dim), dtype=np.float64)
   for i, s in enumerate(texts):
      for tok in tokenize(s):
         h = signed_hash_int(tok)
         j = h % dim
         sign = 1 if ((h >> 63) & 1) == 0 else -1
         X[i, j] += sign
      nrm = np.linalg.norm(X[i])
      if nrm > 0:
         X[i] /= nrm
   return X


# -----------------------------
# Basis construction and drift
# -----------------------------
def orthonormal_basis_from_data(X, k=16, seed=0):
   # Center then SVD on a small dataset; returns U with orthonormal columns
   np.random.seed(seed)
   Xc = X - X.mean(axis=0, keepdims=True)
   # Economy SVD
   U_svd, S, Vt = np.linalg.svd(Xc, full_matrices=False)
   # Take top-k right singular vectors (principal axes in feature space)
   W = Vt[:k].T # shape [d, k]
   # Orthonormalize (QR) to be safe
   Q, _ = np.linalg.qr(W)
   return Q[:, :k]


def principal_angles_drift(U0, Ut):
   # U0, Ut: [d, k] with orthonormal columns
   C = U0.T @ Ut # [k, k]
  # nuclear norm equals sum of singular values; for orthonormal cols, these are
cosines of principal angles
   svals = np.linalg.svd(C, compute_uv=False)
   s_avg = svals.mean()
   drift = float(1.0 - s_avg)
   return drift, float(svals.max()), float(svals.min())


# -----------------------------
# Metrics
# -----------------------------
def D_residual(x, U):
   # D(x) = ||(I - UU^T)x||^2
   proj = U @ (U.T @ x)
   r = x - proj
   return float(np.dot(r, r))


def D_trace(X, U):
   return np.array([D_residual(x, U) for x in X])


def BTI_trace(X, U):
   # BTI = |w1*w2| / (w1^2 + w2^2) for top-2 magnitude components of w = U^T x
   W=X@U
   bti = []
   for w in W:
      idx = np.argsort(np.abs(w))[::-1]
      if len(idx) < 2 or (w[idx[0]] == 0 and w[idx[1]] == 0):
         bti.append(0.0)
      else:
         w1 = w[idx[0]]
         w2 = w[idx[1]]
         denom = (w1*w1 + w2*w2)
         bti.append(float(abs(w1*w2) / denom) if denom > 0 else 0.0)
   return np.array(bti)


# -----------------------------
# Create artifacts
# -----------------------------
transcripts_csv = os.path.join(BASE, "transcripts.csv")
ensure_demo_transcripts(transcripts_csv)
# Load transcripts
df = pd.read_csv(transcripts_csv)
df = df.sort_values(["session_id","timestamp_s","utterance_id"],
kind="mergesort").reset_index(drop=True)


# Vectorize
dim = 512
X = hash_vectorize(df["text"].tolist(), dim=dim)


# Build or load basis
basis_path = os.path.join(BASE, "basis_U.npy")
if os.path.exists(basis_path):
  U0 = np.load(basis_path)
else:
  # held-out first 20% to build basis
  n = len(X)
  held = max(8, int(0.2 * n))
  U0 = orthonormal_basis_from_data(X[:held], k=16, seed=42)
  np.save(basis_path, U0)


# For demo: allow a simulated session-time basis Ut = U0 (no drift)
Ut = U0.copy()


# Metrics
D_vals = D_trace(X, Ut)
BTI_vals = BTI_trace(X, Ut)
# Simple EMA smoothing for D
alpha = 0.2
D_ema = []
acc = None
for v in D_vals:
  acc = v if acc is None else alpha*v + (1-alpha)*acc
  D_ema.append(acc)
D_ema = np.array(D_ema)


# Drift
drift, smax, smin = principal_angles_drift(U0, Ut)


# Plots
plt.figure()
plt.plot(df["timestamp_s"].values, D_vals)
plt.xlabel("time (s)")
plt.ylabel("D (residual norm squared)")
plt.title("D over time")
plt.tight_layout()
plot_D_path = os.path.join(BASE, "D_over_time.png")
plt.savefig(plot_D_path)
plt.close()


plt.figure()
plt.plot(df["timestamp_s"].values, BTI_vals)
plt.xlabel("time (s)")
plt.ylabel("BTI (intra-subspace tension)")
plt.title("BTI over time")
plt.tight_layout()
plot_BTI_path = os.path.join(BASE, "BTI_over_time.png")
plt.savefig(plot_BTI_path)
plt.close()


# Run log + schema
run_log = {
  "created_at_utc": datetime.utcnow().isoformat() + "Z",
  "inputs": {
       "transcripts_csv": transcripts_csv,
       "dim": dim,
       "heldout_fraction": 0.2,
       "k": 16,
       "alpha_ema": alpha
  },
  "artifacts": {
       "basis_U_path": basis_path,
       "plot_D_path": plot_D_path,
       "plot_BTI_path": plot_BTI_path
  },
  "hashes": {
       "basis_U_sha256": sha256_bytes(np.load(basis_path).tobytes()),
       "transcripts_sha256": sha256_bytes(open(transcripts_csv, "rb").read())
  },
  "metrics": {
       "subspace_drift": drift,
       "principal_cos_max": smax,
       "principal_cos_min": smin,
          "D_mean": float(D_vals.mean()),
          "D_median": float(np.median(D_vals)),
          "BTI_mean": float(BTI_vals.mean())
     },
   "notes": "Demo run. Replace transcripts.csv with your data; freeze basis_U.npy for
study runs."
}
run_log_path = os.path.join(BASE, "run_log.json")
with open(run_log_path, "w", encoding="utf-8") as f:
     json.dump(run_log, f, indent=2)


schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "PhaseMirror Run Log",
    "type": "object",
    "required": ["created_at_utc","inputs","artifacts","hashes","metrics"],
    "properties": {
     "created_at_utc": {"type":"string"},
     "inputs": {
      "type":"object",
      "properties": {
          "transcripts_csv":{"type":"string"},
          "dim":{"type":"integer"},
          "heldout_fraction":{"type":"number"},
          "k":{"type":"integer"},
          "alpha_ema":{"type":"number"}
      },
      "required":["transcripts_csv","dim","heldout_fraction","k","alpha_ema"]
},
"artifacts": {
 "type":"object",
 "properties": {
     "basis_U_path":{"type":"string"},
     "plot_D_path":{"type":"string"},
     "plot_BTI_path":{"type":"string"}
 },
 "required":["basis_U_path"]
},
"hashes": {
 "type":"object",
 "properties": {
     "basis_U_sha256":{"type":"string"},
     "transcripts_sha256":{"type":"string"}
 },
 "required":["basis_U_sha256"]
},
"metrics": {
 "type":"object",
 "properties": {
     "subspace_drift":{"type":"number"},
     "principal_cos_max":{"type":"number"},
     "principal_cos_min":{"type":"number"},
     "D_mean":{"type":"number"},
     "D_median":{"type":"number"},
     "BTI_mean":{"type":"number"}
 },
         "required":["subspace_drift","D_mean"]
        },
        "notes":{"type":"string"}
    }
}
schema_path = os.path.join(BASE, "run_log_schema.json")
with open(schema_path, "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)


# -----------------------------
# Write notebook (single cell with the full pipeline for users)
# -----------------------------
notebook_code = r'''
# Phase Mirror Dissonance — Minimal Notebook
# This notebook computes D and BTI from transcripts, with a hashed-vectorizer (no
external deps),
# builds/loads a reference subspace U, logs hashes and drift, and plots results.
# Files expected/produced in /mnt/data:
# - transcripts.csv (input). If missing, a small demo will be generated by the helper code
below.
# - basis_U.npy (frozen across sessions for reproducibility)
# - run_log.json (metrics and hashes)
# - D_over_time.png, BTI_over_time.png


import os, json, hashlib, random
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


BASE = "/mnt/data"


def sha256_bytes(b: bytes) -> str:
  return hashlib.sha256(b).hexdigest()


def tokenize(s: str):
  return [w.lower() for w in ''.join(ch if ch.isalnum() else ' ' for ch in s).split() if w]


def signed_hash_int(s: str):
  h = hashlib.blake2b(s.encode("utf-8"), digest_size=8).digest()
  return int.from_bytes(h, "little", signed=False)


def hash_vectorize(texts, dim=512):
  X = np.zeros((len(texts), dim), dtype=np.float64)
  for i, s in enumerate(texts):
     for tok in tokenize(s):
        h = signed_hash_int(tok)
        j = h % dim
        sign = 1 if ((h >> 63) & 1) == 0 else -1
        X[i, j] += sign
     nrm = np.linalg.norm(X[i])
     if nrm > 0:
        X[i] /= nrm
  return X


def orthonormal_basis_from_data(X, k=16, seed=0):
  np.random.seed(seed)
  Xc = X - X.mean(axis=0, keepdims=True)
  U_svd, S, Vt = np.linalg.svd(Xc, full_matrices=False)
  W = Vt[:k].T
  Q, _ = np.linalg.qr(W)
  return Q[:, :k]


def principal_angles_drift(U0, Ut):
  C = U0.T @ Ut
  svals = np.linalg.svd(C, compute_uv=False)
  s_avg = svals.mean()
  drift = float(1.0 - s_avg)
  return drift, float(svals.max()), float(svals.min())


def D_trace(X, U):
  # D(x) = ||(I - UU^T)x||^2
  proj = X @ U @ U.T
  R = X - proj
  return np.sum(R*R, axis=1)


def BTI_trace(X, U):
  W=X@U
  bti = []
  for w in W:
     idx = np.argsort(np.abs(w))[::-1]
     if len(idx) < 2 or (w[idx[0]] == 0 and w[idx[1]] == 0):
        bti.append(0.0)
     else:
          w1 = w[idx[0]]
          w2 = w[idx[1]]
          denom = (w1*w1 + w2*w2)
          bti.append(float(abs(w1*w2) / denom) if denom > 0 else 0.0)
  return np.array(bti)


# Load or generate transcripts
transcripts_csv = os.path.join(BASE, "transcripts.csv")
if not os.path.exists(transcripts_csv):
  # Minimal demo data
  random.seed(7)
  speakers = ["A","B","C"]
  rows = []
  t = 0.0
  for i in range(60):
     sp = random.choice(speakers)
     txt = random.choice([
          "I think the plan is unclear and risks scope creep.",
          "Can we align on success metrics before we proceed?",
          "I disagree: shipping fast matters more than polishing metrics.",
          "This feels confusing; what is the objective again?",
          "Let's break: list assumptions and challenge the weakest.",
          "I propose a repair: define roles and next steps."
     ])
      rows.append({"session_id":"demo","utterance_id": i,"speaker": sp,"timestamp_s":
t,"text": txt})
     t += random.uniform(8, 20)
  pd.DataFrame(rows).to_csv(transcripts_csv, index=False)
df =
pd.read_csv(transcripts_csv).sort_values(["session_id","timestamp_s","utterance_id"]).r
eset_index(drop=True)


# Vectorize
dim = 512
X = hash_vectorize(df["text"].tolist(), dim=dim)


# Build or load basis
basis_path = os.path.join(BASE, "basis_U.npy")
if os.path.exists(basis_path):
  U0 = np.load(basis_path)
else:
  n = len(X)
  held = max(8, int(0.2 * n))
  U0 = orthonormal_basis_from_data(X[:held], k=16, seed=42)
  np.save(basis_path, U0)


Ut = U0.copy() # freeze within session
D_vals = D_trace(X, Ut)
W = X @ Ut
BTI_vals = BTI_trace(X, Ut)


# Plots (matplotlib, single-plot figures, no explicit colors)
plt.figure()
plt.plot(df["timestamp_s"].values, D_vals)
plt.xlabel("time (s)"); plt.ylabel("D (residual norm squared)"); plt.title("D over time");
plt.tight_layout()
plot_D_path = os.path.join(BASE, "D_over_time.png"); plt.savefig(plot_D_path);
plt.close()


plt.figure()
plt.plot(df["timestamp_s"].values, BTI_vals)
plt.xlabel("time (s)"); plt.ylabel("BTI (intra-subspace tension)"); plt.title("BTI over time");
plt.tight_layout()
plot_BTI_path = os.path.join(BASE, "BTI_over_time.png"); plt.savefig(plot_BTI_path);
plt.close()


# Log
run_log = {
    "created_at_utc": datetime.utcnow().isoformat() + "Z",
  "inputs": {"transcripts_csv": transcripts_csv, "dim": dim, "heldout_fraction": 0.2, "k":
16},
   "artifacts": {"basis_U_path": basis_path, "plot_D_path": plot_D_path, "plot_BTI_path":
plot_BTI_path},
    "hashes": {
         "basis_U_sha256": hashlib.sha256(np.load(basis_path).tobytes()).hexdigest(),
         "transcripts_sha256": hashlib.sha256(open(transcripts_csv,"rb").read()).hexdigest()
    },
    "metrics": {
         "subspace_drift": principal_angles_drift(U0, Ut)[0],
         "D_mean": float(D_vals.mean()),
         "D_median": float(np.median(D_vals)),
         "BTI_mean": float(BTI_vals.mean())
    },
  "notes": "Freeze basis_U.npy for study runs. Replace demo transcripts with your
data."
}
with open(os.path.join(BASE, "run_log.json"), "w", encoding="utf-8") as f:
      json.dump(run_log, f, indent=2)


print("Notebook run complete. See:", basis_path, plot_D_path, plot_BTI_path,
os.path.join(BASE, "run_log.json"))
'''


nb = {
 "cells": [
    {"cell_type":"markdown","metadata":{},"source":[
      "# Phase Mirror Dissonance — Minimal Notebook\n",
  "Implements D and BTI, freezes a reference subspace, and logs hashes and
metrics.\n",
  "**WARNING:** This measures alignment to a chosen reference subspace, not truth.
Treat Π as a reference frame, not a law.\n"
    ]},


{"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":[notebook
_code]}
 ],
 "metadata":{
      "kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},
      "language_info":{"name":"python","version":"3.x"}
 },
 "nbformat":4,
 "nbformat_minor":5
}
nb_path = os.path.join(BASE, "dissonance_pipeline.ipynb")
with open(nb_path, "w", encoding="utf-8") as f:
  json.dump(nb, f, indent=2)


# Also write one_page_protocol.md mirroring the canvas section
one_pager_path = os.path.join(BASE, "one_page_protocol.md")
one_pager = """# One-Page Protocol — Phase Mirror Dissonance v1.0


Purpose: Test whether structured “oral disagreement + repair” reduces D (residual to a
fixed reference subspace Π) and improves external performance on an unrelated
transfer task, without coercion or drift.


Primary hypotheses:
1) Session B (with disagreement + repair prompts) lowers average D versus Session A
(neutral prompts).
2) Lower D associates with better performance on an objective transfer task
administered after both sessions.
3) EEG sub-study (optional): time-aligned D negatively correlates with
magnitude-squared coherence in preregistered bands.


Design:
- Freeze Π from a held-out corpus; publish hashes for corpus manifest, code commit,
and basis matrix U. Target drift ≤ 1% cosine/session.
- A/B within-subjects over two 20-minute sessions with identical topics. B inserts
structured disagreement then repair prompts.
- Consent and agency: any participant may set κ = 0 (no consensus coupling) without
exclusion.
- Resolution operator Ξ: diagonal gains in [μ, L]; log μ, L, and step size η; clip violations.
- Transfer task: immediately after sessions, administer an unrelated objective task (e.g.,
puzzle set, code review rubric, vignette-based judgment). Predefine scoring rubric Y.
- Stop-rules: halt if drift > 1%, descent-violation rate > 0.5%, or ΔY < 0 while ΔD < 0.


Endpoints and analysis:
- Primary: ΔD (B − A) ≤ −20% with p < 0.05 (preregistered test).
- Secondary: inter-speaker alignment slope within Π improves in B.
- Tertiary: transfer task ΔY ≥ 0; report effect size and CIs.
- EEG (optional): preregistered negative correlation between D and coherence;
randomized repair vs neutral prompt schedule to strengthen causal read.


Metrics (operational):
- D(x) = ||(I − Π)x||² with Π fixed during session; report raw and EMA-smoothed traces.
- Intra-subspace tension BTI(x): for coordinates w = Uᵀx, let w1 and w2 be the top two
magnitudes; BTI = |w1·w2| / (w1² + w2²).
- Descent-violation rate v = count{ D_{t+1} > D_t + ε } / T with ε = 1e-8.
- Subspace drift via principal angles between initial U0 and session Ut.


Goodhart guardrails:
- Multi-objective gate: only claim success if ΔD < 0 AND ΔY ≥ 0. Publish nulls.
- Sensitivity: rerun with an alternative encoder post hoc and disclose deltas.


Naming discipline:
- Use “reference subspace” and “dictionary atoms” in external reporting; reserve “prime”
language for metaphysical discussion only.


Deliverables:
- Versioned run logs with hashes, drift, violation counts (schema below).
- Plots of D and BTI over time and per speaker.
- Pre-registration document and consent/agency template.
"""
write_text(one_pager_path, one_pager)


print("Created files:")
print(" -", nb_path)
print(" -", one_pager_path)
print(" -", run_log_path)
print(" -", schema_path)
