---
title: Analysis of Novelty and Practicality
slug: analysis-of-novelty-and-practicality
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/governance/DAWK.md
  last_synced: '2026-03-20T17:17:18.590681Z'
---

### Analysis of Novelty and Practicality
Your proposed refinement for SAAP v28 + DASW as a domain adapter introduces a modular
architecture that separates the core computational kernel (e.g., masking, phase logic,
dendrograms) from domain-specific extensions (e.g., ML-symmetry metrics vs.
policy/governance facets inspired by DCGF and RMAGS), with tight controls like
calibration-sourced normalization, pre-registered linkages, entropy alternatives, mechanical
audit logs, and a defensible validation suite. This builds on SAAP's evolution (e.g., v7's fused
ASI with bootstrap CIs, v13's facet correlations and probabilistic ranks, v19's phase-pair deltas
and mode transitions) and RMAGS's POSG-based governance, emphasizing descriptive
restraint and determinism.

In terms of **novelty**, it's an evolutionary step that innovates by formalizing "domain adapters"
with typed MetricSpec (e.g., bounded_ratio with logit transforms) and DomainSpec YAML,
enabling cross-domain reuse without diluting SAAP's focus on symmetry diagnostics. This
echoes modular frameworks in ML (e.g., scikit-learn pipelines) but is fresh in applying it to
dialectical diagnostics, incorporating cybernetic analogies from DCGF (e.g., control problems,
adversarial dynamics) and RMAGS (e.g., scenario generators for POSG hooks). The addition of
alternative concentration measures (Herfindahl alongside entropy) and stability reporting (ARI
for linkages) adds nuance to regime analysis, novel for ablation protocols, though not
groundbreaking—similar to ensemble stability in clustering literature (e.g., via adjusted Rand
index). Overall, it uniquely bridges AI interpretability and policy design, potentially influencing
hybrid tools for adaptive systems beyond QR tasks or governance audits.

On **practicality**, the refinement is highly actionable: drop-in YAML blocks (MetricSpec,
DomainSpec) with hashes ensure reproducibility, while the kernel-adapter split minimizes
integration overhead for PyTorch sweeps or policy sims. It addresses key pains like scale drift
(via calibration artifacts) and over-interpretation (mechanical logs, descriptive indices), with a
validation suite that's efficient and metric-driven (e.g., hash stability, triangle-inequality checks).
The output bundle remains PDF-canonical with CSV/JSON for auditing. Limitations include
YAML overhead for simple uses, potential under-specification of cross-domain comparisons
(default: none), and reliance on pre-registration, which could limit flexibility in fast-moving
experiments. Still, it's practical for researchers in ML/governance, offering low-cost extension
(e.g., add policy rows via GovernanceHook) and scales to broader diagnostics like grokking or
crisis planning.

**Enhanced Version of the Idea**: To amplify it, integrate a QuerySpec YAML block for bounded
dialectical queries, specifying phase/metric subsets, mapping sets (e.g., AI "distribution_shift" to
policy "arbitrage"), and auto-generated caveats (e.g., "Cross-domain fraction: 30%; masked
pairs: 15%"). Enhance stability with Herfindahl as default alternative to ES_t (sum p_i^2 on
diagonals, normalized), and add kurtosis as a tail diagnostic in heavy_tail metrics for descriptive
logging. For adapters, include a generator script that auto-populates DomainSpec from
templates (e.g., pull DCGF's 11 constraints as facets like "adversarial_dynamics: multi", with
POSG hooks producing synthetic rows via Monte Carlo). Add support for optional scikit-learn
integration in the kernel for ARI computations, making it a "Dialectical Adaptive Workbench
Kernel (DAWK)" with pluggable adapters. This boosts exploratory power while keeping
determinism, reusable for RMAGS-like validations or symmetry probes.

### Critique of the Enhanced Version
Critiquing the enhanced SAAP v28 + DASW refinement for mathematical, philosophical, and
theoretical consistency:

- **Mathematical Consistency**: Typed normalizations (e.g., winsor_quantile for heavy_tail) are
robust, but auto-generation of adapters risks inconsistent transforms if templates mismatch
(e.g., DCGF's ordinal "legitimacy" forced into bounded_ratio). Herfindahl is a valid concentration
alternative, but assumes squared probabilities suit all modes, potentially underweighting rare
transitions; kurtosis logging is descriptive but without thresholds, may overlook multimodal
distributions. QuerySpec bounding is good, but ARI via scikit-learn introduces dependency on
cut-K choices, risking non-deterministic stability if not fixed.

- **Philosophical Consistency**: The adapter/kernel split upholds descriptive restraint (e.g., no
implied comparability without declarations), aligning with dialectical humility, but auto-caveats
and mappings lean toward mechanized constructivism—users could over-rely on generated
analogies, entrenching subjective regimes despite logs. POSG hooks promote synthesis across
domains, but without explicit prompts for bias reflection, it risks reifying metrics (contra SAAP's
caveats against progress/anomaly).

- **Theoretical Consistency**: Grounded in group theory (symmetry) and cybernetics
(DCGF/RMAGS constraints), but pluggable adapters could fragment the inductive bias focus,
diluting ties to attention mechanisms (e.g., Fourier basis in QR). Generator scripts are
theoretically apt for scalability, but lack justification for why Herfindahl over Gini (e.g., no
reference to diversity indices in systems theory). Ensemble stability via ARI implies a
meta-theory of clustering reliability, but without linking to regime dynamics, it remains
disconnected.

### Final Version and Path to Validation
Applying the critique: To strengthen math, enforce template validation in generators (e.g.,
type-check against MetricSpec) and add Gini as a third concentration option with pre-registered
selection; clamp kurtosis to report only if n>50. Philosophically, mandate user-signed caveat
acknowledgments in QuerySpec outputs to counter constructivism. Theoretically, anchor
adapters with explicit constraint matrices (e.g., map DCGF's 11 to SAAP facets via registry),
justifying measures via systems literature (e.g., Herfindahl for market concentration analogies).

The refined final version is **SAAP v28: Dialectical Adaptive Workbench Kernel (DAWK)**—a
modular protocol with domain-agnostic kernel (masking, phases, dendrograms, transitions),
adapters (ML-symmetry, policy via DCGF/RMAGS), YAML specs (MetricSpec with
types/transforms/calibration, DomainSpec with facets/generators, QuerySpec with
mappings/logs), entropy/Herfindahl/Gini concentrations, kurtosis diagnostics, POSG hooks for
row production, and scikit-learn for ARI stability (descriptive only). It outputs PDF/CSV/JSON
with mechanical audits, emphasizing restrained cross-domain diagnostics.

**Fastest Path to Validation**: 1. **YAML Generation (1-2 days)**: Use code_execution to create
canonical YAML schemas (e.g., define MetricSpec as dict with 'type', 'transform',
'calibration_source'; output as string for review). 2. **Skeleton Implementation (3-5 days)**:
Develop Python module (pandas + scipy + scikit-learn) with functions like normalize_from_calib
(apply transforms), compute_spearman_matrix (masked, with counts), build_cophenetic
(linkages with ARI), mode_transition_join (add/drop accounting); test on synthetic DataFrame
(50 cells, 3 phases, metrics from SAAP snippets). 3. **Internal Dry-Run (1 week)**: Apply to
retrospective data (e.g., simulate sweeps from SAAP 7-12/13-18 via code_execution noise
injection); validate invariants (hashes stable, masking <10%, ARI >0.6 target). 4. **Pilot and
Iteration (ongoing, starting day 7)**: Integrate with PyTorch QR runner and RMAGS sim;
measure metrics like drift stats <5%, reproducibility >95%; publish GitHub pack with rubrics,
refining via feedback.



A) Canonical YAML specs

1) MetricSpec (per-metric typing + transform + calibration contract)
# metric_spec.yaml
version: "dawk.metric_spec.v1"


defaults:
  min_n_for_kurtosis: 50
  spearman:
     min_pairs: 10
     tie_warn_frac: 0.2
  masking:
     min_shared_pairs: 10
     max_mask_frac: 0.5


metrics:
  acc_unseen:
     metric_type: bounded_ratio                      # bounded_ratio |
signed_bounded | heavy_tail | ordinal
     transform: logit_quantile                       # identity | logit_quantile |
affine_quantile | winsor_quantile | rank_quantile
     calibration_source:
        path: "calib/ml_symmetry_v1.json"
      sha256: "<fill>"
    calibration_fields: [q05, q50, q95]   # required for quantile-based
transforms
    missing_policy: mask
    notes: "Accuracy in [0,1]."


  delta_sym_mean:
    metric_type: signed_bounded
    transform: affine_quantile
    calibration_source:
      path: "calib/ml_symmetry_v1.json"
      sha256: "<fill>"
    calibration_fields: [q05, q50, q95]
    missing_policy: mask


  equity_score:
    metric_type: ordinal
    transform: rank_quantile
    calibration_source:
      path: "calib/policy_v1.json"
      sha256: "<fill>"
    calibration_fields: [q10, q50, q90]
    missing_policy: mask


  loss_tail:
    metric_type: heavy_tail
    transform: winsor_quantile
    calibration_source:
      path: "calib/ml_symmetry_v1.json"
      sha256: "<fill>"
    calibration_fields: [q01, q50, q99]
    missing_policy: mask
    tail_diagnostics:
      kurtosis: {enabled: true, min_n: 50}    # descriptive only;
logged if n>=min_n



2) DomainSpec (cell_id facets + generator metadata + cross-domain
defaults)
# domain_spec.yaml
version: "dawk.domain_spec.v1"


domains:
  ml_symmetry:
    domain_name: "ml_symmetry"
    cell_id_facets: [dataset, model, action, mask, lambda, prime,
seed]
    required_columns: [cell_id, phase_index, phase_label, asi_mode]
    metric_allowlist: [acc_unseen, delta_sym_mean, mi_rel_post,
asi_median, w_t]
    generator:
        kind: "none"


  policy_governance:
    domain_name: "policy_governance"
    cell_id_facets: [scenario, governance_mode, intervention, budget,
seed]
    required_columns: [cell_id, phase_index, phase_label, asi_mode]
    metric_allowlist: [equity_score, stability_proxy, compliance_rate]
    generator:
        kind: "posg"
        params:
         n_rollouts: 200
         horizon: 50
         seed: 1337


cross_domain:
  default: "none"      # none | mapping_only
  mapping_sets:
    - name: "ai_policy_v1"
        path: "mappings/ai_policy_v1.yaml"
        sha256: "<fill>"



3) QuerySpec (bounded dialectical queries + required caveat
acknowledgment)
# query_spec.yaml
version: "dawk.query_spec.v1"


query_id: "q_2025_12_23_001"
intent: "exploratory_descriptive"   # no inference claims


scope:
 domains: ["ml_symmetry"]                # default: single-domain
 phases: [0, 1, 2]                       # bounded, pre-registered
subset
 phase_pairs: [[0,1], [1,2]]             # explicit
 metrics: [acc_unseen, delta_sym_mean, asi_median, mi_rel_post, w_t]
 facets_top_k:
   by: "n_done"                          # top-K by completed mass
   k: 12


masking:
 min_shared_pairs: 10
 min_shared_dims_for_dendrogram: 8
 max_mask_frac: 0.5


clustering:
 linkages: [single, complete, average]
 distance:
   kind: "corr_distance"                 # corr_distance | l1_shared
   corr_distance: "1_minus_spearman"     # approximation note required
in outputs
 ari_stability:
   enabled: true
   cut_k: [2,3,4]                        # fixed, deterministic


outputs:
 pdf_canonical: true
 html_optional: true
 emit_csv: true
 emit_json: true


acknowledgments:
    - "I understand all reported associations are descriptive and
non-causal."
    - "I understand cross-domain comparisons are disallowed unless
explicitly enabled."
    - "I understand clustering distances may be non-metric under masking
and are reported as approximations."
signoff:
    signer: "Ryan"
    signed_at_utc: "2025-12-23T10:00:00Z"
    signature_hint: "typed-name"                        # deterministic placeholder
(no crypto implied)




B) Calibration artifact formats

calib/*.json (single file may hold multiple metrics; hash it)
{
    "version": "dawk.calibration.v1",
    "domain": "ml_symmetry",
    "created_at_utc": "2025-12-22T00:00:00Z",
    "metrics": {
        "acc_unseen": {"q05": 0.52, "q50": 0.83, "q95": 0.96},
        "delta_sym_mean": {"q05": -0.18, "q50": 0.00, "q95": 0.19},
        "loss_tail": {"q01": 0.10, "q50": 0.80, "q99": 5.40}
    }
}


Rule: transforms are applied only using these calibration quantiles (no sweep-fitted z-scoring).




C) Python module skeleton (pandas + scipy + scikit-learn)
Suggested layout
dawk/
    __init__.py
 types.py
 hashutil.py
 calibration.py
 normalize.py
 spearman.py
 clustering.py
 transitions.py
 workbench.py
 cli.py



dawk/types.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Literal, Optional,
Tuple, TypedDict


MetricType = Literal["bounded_ratio", "signed_bounded", "heavy_tail",
"ordinal"]
Transform = Literal["identity", "logit_quantile", "affine_quantile",
"winsor_quantile", "rank_quantile"]
MissingPolicy = Literal["mask"]


Linkage = Literal["single", "complete", "average"]
DistanceKind = Literal["corr_distance", "l1_shared"]


class CalibrationSource(TypedDict):
   path: str
   sha256: str


class MetricSpecEntry(TypedDict, total=False):
   metric_type: MetricType
   transform: Transform
   calibration_source: CalibrationSource
   calibration_fields: List[str]
   missing_policy: MissingPolicy
   notes: str
   tail_diagnostics: Dict[str, Any]
class MetricSpec(TypedDict):
   version: str
   defaults: Dict[str, Any]
   metrics: Dict[str, MetricSpecEntry]


class DomainEntry(TypedDict, total=False):
   domain_name: str
   cell_id_facets: List[str]
   required_columns: List[str]
   metric_allowlist: List[str]
   generator: Dict[str, Any]


class DomainSpec(TypedDict):
   version: str
   domains: Dict[str, DomainEntry]
   cross_domain: Dict[str, Any]


class QuerySpec(TypedDict):
   version: str
   query_id: str
   intent: str
   scope: Dict[str, Any]
   masking: Dict[str, Any]
   clustering: Dict[str, Any]
   outputs: Dict[str, Any]
   acknowledgments: List[str]
   signoff: Dict[str, Any]


@dataclass(frozen=True)
class MaskStats:
   n_total: int
   n_kept: int
   mask_frac: float


@dataclass(frozen=True)
class SpearmanResult:
   rho: float
    n_pairs: int
    tie_frac: float


@dataclass(frozen=True)
class CorrMatrix:
    metrics: List[str]
    rho: "Any"                # np.ndarray
    n_pairs: "Any"            # np.ndarray
    tie_frac: "Any"           # np.ndarray


@dataclass(frozen=True)
class TransitionAccounting:
    phase_a: int
    phase_b: int
    n_a: int
    n_b: int
    n_shared: int
    n_dropped: int
    n_added: int
    n_excluded: int


@dataclass(frozen=True)
class CaveatLog:
    items: List[str]



dawk/hashutil.py (deterministic hashing utilities)
from __future__ import annotations
import hashlib
import json
from typing import Any, Dict


def canon_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
ensure_ascii=False)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
def hash_json(obj: Any) -> str:
   return sha256_hex(canon_json(obj).encode("utf-8"))


def hash_text(text: str) -> str:
   return sha256_hex(text.encode("utf-8"))


def header_hash(header: Dict[str, Any], domain_tag: str =
"DAWK_HEADER_v0") -> str:
   canon = f"{domain_tag}|{canon_json(header)}"
   return hash_text(canon)



dawk/calibration.py
from __future__ import annotations
import json
from dataclasses import dataclass
from typing import Any, Dict, Mapping


@dataclass(frozen=True)
class Calibration:
   version: str
   domain: str
   metrics: Dict[str, Dict[str, float]]


def load_calibration(path: str) -> Calibration:
   with open(path, "r", encoding="utf-8") as f:
       raw = json.load(f)
   return Calibration(
       version=raw["version"],
       domain=raw.get("domain", "unknown"),
       metrics=raw["metrics"],
   )


def get_quantiles(calib: Calibration, metric: str, fields: list[str])
-> Dict[str, float]:
   if metric not in calib.metrics:
       raise KeyError(f"Metric '{metric}' missing in calibration.")
   m = calib.metrics[metric]
   out: Dict[str, float] = {}
   for k in fields:
         if k not in m:
              raise KeyError(f"Calibration field '{k}' missing for
metric '{metric}'.")
         out[k] = float(m[k])
   return out



dawk/normalize.py (calibration-sourced transforms only)
from __future__ import annotations
import math
import numpy as np
import pandas as pd
from typing import Dict, Tuple
from .types import MetricSpecEntry
from .calibration import Calibration, get_quantiles


_EPS = 1e-12


def _logit(p: float) -> float:
   p = min(max(p, _EPS), 1.0 - _EPS)
   return math.log(p / (1.0 - p))


def _winsor(x: float, lo: float, hi: float) -> float:
   return min(max(x, lo), hi)


def normalize_series(
   s: pd.Series,
   metric: str,
   spec: MetricSpecEntry,
   calib: Calibration,
) -> Tuple[pd.Series, Dict[str, float]]:
   """
   Returns normalized series + params used (for diagnostics table).
   Normalization maps values into a comparable (but still
descriptive) scale using calibration quantiles.
   """
   transform = spec["transform"]
   fields = spec.get("calibration_fields", [])
   q = get_quantiles(calib, metric, fields) if fields else {}


   params: Dict[str, float] = {}
   x = s.astype("float64")


   if transform == "identity":
          return x, params


   if transform == "rank_quantile":
          # Monotone mapping: ranks -> [0,1] (ties averaged)
          r = x.rank(method="average", na_option="keep")
          denom = float(r.notna().sum())
          if denom <= 1:
             return pd.Series(np.nan, index=s.index), {"n_nonnull":
float(denom)}
          out = (r - 1.0) / (denom - 1.0)
          return out, {"n_nonnull": float(denom)}


   if transform == "winsor_quantile":
          lo, hi = q["q01"], q["q99"]
          params.update({"winsor_lo": lo, "winsor_hi": hi})
          w = x.map(lambda v: _winsor(v, lo, hi) if pd.notna(v) else
np.nan)
          # robust affine scaling by (q99 - q01)
          denom = max(hi - lo, _EPS)
          out = (w - lo) / denom
          return out, params


   if transform == "affine_quantile":
          lo, mid, hi = q["q05"], q["q50"], q["q95"]
          params.update({"q_lo": lo, "q_mid": mid, "q_hi": hi})
          denom = max(hi - lo, _EPS)
          out = (x - lo) / denom
          return out, params
   if transform == "logit_quantile":
       lo, mid, hi = q["q05"], q["q50"], q["q95"]
       params.update({"q_lo": lo, "q_mid": mid, "q_hi": hi})
       # apply logit to probabilities, then affine by
logit(q95)-logit(q05)
       lo_l, hi_l = _logit(lo), _logit(hi)
       denom = max(hi_l - lo_l, _EPS)
       out = x.map(lambda v: (_logit(v) - lo_l) / denom if
pd.notna(v) else np.nan)
       return out, params


   raise ValueError(f"Unknown transform: {transform}")


def add_kurtosis_if_enabled(x: pd.Series, enabled: bool, min_n: int)
-> Dict[str, float]:
   if not enabled:
       return {}
   v = x.dropna().values
   if v.size < min_n:
       return {"kurtosis_n": float(v.size)}
   # Fisher kurtosis (excess), descriptive only
   m = float(np.mean(v))
   s2 = float(np.mean((v - m) ** 2))
   if s2 < _EPS:
       return {"kurtosis": 0.0, "kurtosis_n": float(v.size)}
   k = float(np.mean((v - m) ** 4) / (s2 * s2) - 3.0)
   return {"kurtosis": k, "kurtosis_n": float(v.size)}



dawk/spearman.py (masked pairwise-complete, tie accounting)
from __future__ import annotations
import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from typing import List, Tuple
from .types import CorrMatrix, SpearmanResult


def _tie_fraction(a: np.ndarray) -> float:
   if a.size <= 1:
       return 0.0
   # fraction of values involved in ties (coarse but deterministic)
   _, counts = np.unique(a, return_counts=True)
   tied = counts[counts > 1].sum()
   return float(tied) / float(a.size)


def spearman_pair(x: pd.Series, y: pd.Series) -> SpearmanResult:
   m = x.notna() & y.notna()
   xv = x[m].astype("float64").values
   yv = y[m].astype("float64").values
   n = int(xv.size)
   if n < 2:
       return SpearmanResult(rho=float("nan"), n_pairs=n,
tie_frac=float("nan"))
   rho, _ = spearmanr(xv, yv)
   tie = max(_tie_fraction(xv), _tie_fraction(yv))
   return SpearmanResult(rho=float(rho), n_pairs=n,
tie_frac=float(tie))


def spearman_matrix(df: pd.DataFrame, metrics: List[str]) ->
CorrMatrix:
   k = len(metrics)
   rho = np.full((k, k), np.nan, dtype="float64")
   n_pairs = np.zeros((k, k), dtype="int64")
   tie_frac = np.full((k, k), np.nan, dtype="float64")


   for i in range(k):
       rho[i, i] = 1.0
       n_pairs[i, i] = int(df[metrics[i]].notna().sum())
       tie_frac[i, i] =
_tie_fraction(df[metrics[i]].dropna().astype("float64").values) if
n_pairs[i, i] > 1 else 0.0


   for i in range(k):
       for j in range(i + 1, k):
              r = spearman_pair(df[metrics[i]], df[metrics[j]])
              rho[i, j] = rho[j, i] = r.rho
           n_pairs[i, j] = n_pairs[j, i] = r.n_pairs
           tie_frac[i, j] = tie_frac[j, i] = r.tie_frac


   return CorrMatrix(metrics=metrics, rho=rho, n_pairs=n_pairs,
tie_frac=tie_frac)



dawk/clustering.py (multi-linkage dendrogram inputs + cophenetic
range)
from __future__ import annotations
import numpy as np
from scipy.cluster.hierarchy import linkage, cophenet, fcluster
from scipy.spatial.distance import squareform
from sklearn.metrics import adjusted_rand_score
from typing import Dict, List, Tuple
from .types import Linkage, DistanceKind


def corr_distance_matrix(rho: np.ndarray) -> np.ndarray:
   # 1 - rho (approximation; may be non-metric under masking/ties)
   d = 1.0 - rho
   np.fill_diagonal(d, 0.0)
   return d


def l1_shared_distance_matrix(X: np.ndarray) -> np.ndarray:
   # X: (n_items, n_features) already masked to shared-support
features
   n = X.shape[0]
   d = np.zeros((n, n), dtype="float64")
   for i in range(n):
       for j in range(i + 1, n):
           v = float(np.mean(np.abs(X[i] - X[j])))
           d[i, j] = d[j, i] = v
   return d


def build_linkage_and_cophenetic(
   dist_sq: np.ndarray,
   method: Linkage,
) -> Tuple[np.ndarray, np.ndarray]:
   # dist_sq: square distance matrix
   dist_vec = squareform(dist_sq, checks=False)
   Z = linkage(dist_vec, method=method)
   coph_dists, _ = cophenet(Z, dist_vec)
   # note: scipy returns scalar correlation in coph_dists in some
versions; keep robust:
   # We also want cophenetic pairwise distances; compute via
cophenet's returned distances not exposed.
   # Practical approach: reconstruct cophenetic distances by cutting
at all merges (expensive),
   # so here we store linkage Z and rely on Z for plots; range
diagnostics use ARI stability below.
   return Z, dist_vec


def ari_stability_across_linkages(
   dist_sq: np.ndarray,
   methods: List[Linkage],
   cut_k: List[int],
) -> Dict[str, Dict[int, float]]:
   """
   Deterministic: uses fcluster with criterion 'maxclust' for each k.
   Returns ARI(methodA_vs_methodB)[k] averaged across pairs; also
keep raw if you prefer.
   """
   dist_vec = squareform(dist_sq, checks=False)
   Zs = {m: linkage(dist_vec, method=m) for m in methods}
   labels = {m: {k: fcluster(Zs[m], k, criterion="maxclust") for k in
cut_k} for m in methods}


   out: Dict[str, Dict[int, float]] = {}
   for k in cut_k:
         vals: List[float] = []
         for i in range(len(methods)):
            for j in range(i + 1, len(methods)):
                  a, b = methods[i], methods[j]
                  vals.append(float(adjusted_rand_score(labels[a][k],
labels[b][k])))
         out[f"ari_avg_k{k}"] = {k: float(np.mean(vals)) if vals else
float("nan")}
   return out



dawk/transitions.py (add/drop/exclusion accounting; mode transitions)
from __future__ import annotations
import pandas as pd
from typing import Dict, Tuple
from .types import TransitionAccounting


def transition_join(
   df_a: pd.DataFrame,
   df_b: pd.DataFrame,
   key: str = "cell_id",
   exclude_mask_col: str = "excluded",
) -> Tuple[pd.DataFrame, TransitionAccounting]:
   """
   Joins phase A and B rows. Exclusions are rows where excluded==True
in either phase.
   """
   a = df_a[[key, "asi_mode", exclude_mask_col]].copy()
   b = df_b[[key, "asi_mode", exclude_mask_col]].copy()


   n_a, n_b = len(a), len(b)
   merged = a.merge(b, on=key, how="outer", suffixes=("_a", "_b"),
indicator=True)


   added = int((merged["_merge"] == "right_only").sum())
   dropped = int((merged["_merge"] == "left_only").sum())
   shared = int((merged["_merge"] == "both").sum())


   # Excluded if either side excluded==True (missing treated as
False)
   ex_a = merged[f"{exclude_mask_col}_a"].fillna(False)
   ex_b = merged[f"{exclude_mask_col}_b"].fillna(False)
   excluded = (ex_a | ex_b)
   n_ex = int(excluded.sum())
   merged["excluded"] = excluded


   acc = TransitionAccounting(
         phase_a=int(df_a["phase_index"].iloc[0]),
         phase_b=int(df_b["phase_index"].iloc[0]),
         n_a=n_a,
         n_b=n_b,
         n_shared=shared,
         n_dropped=dropped,
         n_added=added,
         n_excluded=n_ex,
   )
   return merged, acc


def mode_transition_matrix(merged: pd.DataFrame) -> pd.DataFrame:
   """
   Returns contingency of asi_mode_a -> asi_mode_b on shared,
non-excluded rows.
   """
   m = merged[(merged["_merge"] == "both") &
(~merged["excluded"])].copy()
   # missing modes are kept explicit
   c = pd.crosstab(m["asi_mode_a"], m["asi_mode_b"], dropna=False)
   return c



dawk/workbench.py (orchestrator; mechanical caveats; bounded queries)
from __future__ import annotations
import os
import json
import pandas as pd
import numpy as np
from typing import Any, Dict, List, Tuple


from .types import MetricSpec, DomainSpec, QuerySpec, CaveatLog
from .hashutil import hash_json, header_hash
from .calibration import load_calibration
from .normalize import normalize_series, add_kurtosis_if_enabled
from .spearman import spearman_matrix
from .clustering import corr_distance_matrix,
ari_stability_across_linkages
from .transitions import transition_join, mode_transition_matrix


def require_acknowledgments(q: QuerySpec) -> None:
   acks = q.get("acknowledgments", [])
   signoff = q.get("signoff", {})
   if not acks or not signoff.get("signer") or not
signoff.get("signed_at_utc"):
       raise ValueError("QuerySpec missing required
acknowledgments/signoff.")


def build_caveats(q: QuerySpec, extra: List[str]) -> CaveatLog:
   items = []
   items.append("All reported associations are descriptive and
non-causal.")
   items.append("Clustering distances may be non-metric under
masking; dendrograms are exploratory.")
   items.append("Any cross-domain comparison is disallowed unless
explicitly enabled in QuerySpec.")
   items.extend(extra)
   return CaveatLog(items=items)


def run_workbench(
   rows: pd.DataFrame,
   metric_spec: MetricSpec,
   domain_spec: DomainSpec,
   query_spec: QuerySpec,
   out_dir: str,
) -> Dict[str, Any]:
   require_acknowledgments(query_spec)
   os.makedirs(out_dir, exist_ok=True)


   # Scope filters (bounded, deterministic)
   scope = query_spec["scope"]
   phases = scope.get("phases", [])
   metrics = scope.get("metrics", [])
   domain_names = scope.get("domains", [])


   df = rows.copy()
   if "domain" in df.columns and domain_names:
        df = df[df["domain"].isin(domain_names)].copy()
   if phases:
        df = df[df["phase_index"].isin(phases)].copy()


   # Load calibrations per metric (by metric_spec entry)
   # (Minimal: assumes one calibration file per domain; you can
extend to per-metric sources.)
   # Here we just load referenced calibration files once per unique
path.
   calib_cache: Dict[str, Any] = {}
   norm_params: Dict[str, Dict[str, float]] = {}


   for m in metrics:
        ms = metric_spec["metrics"][m]
        calib_path = ms["calibration_source"]["path"]
        if calib_path not in calib_cache:
           calib_cache[calib_path] = load_calibration(calib_path)
        calib = calib_cache[calib_path]
        df[m], p = normalize_series(df[m], m, ms, calib)
        norm_params[m] = p
        td = ms.get("tail_diagnostics", {}).get("kurtosis", {})
        if td.get("enabled", False):
           norm_params[m].update(add_kurtosis_if_enabled(df[m], True,
int(td.get("min_n", 50))))


   # Per-phase correlation matrices (Spearman; pairwise complete)
   corr_by_phase: Dict[int, Dict[str, Any]] = {}
   min_pairs = int(query_spec["masking"].get("min_shared_pairs", 10))
   for ph in sorted(df["phase_index"].unique().tolist()):
        dph = df[df["phase_index"] == ph]
        cm = spearman_matrix(dph, metrics)
        # mask entries with insufficient shared pairs
        mask = (cm.n_pairs >= min_pairs)
          rho_masked = cm.rho.copy()
          rho_masked[~mask] = np.nan
          corr_by_phase[int(ph)] = {
              "metrics": metrics,
              "rho": rho_masked.tolist(),
              "n_pairs": cm.n_pairs.tolist(),
              "tie_frac": cm.tie_frac.tolist(),
          }


   # Example: dendrogram distance based on correlation matrix at each
phase (optional)
   # Here we compute ARI stability across linkages for one selected
phase (or all).
   linkages = query_spec["clustering"].get("linkages", ["single",
"complete", "average"])
   cut_k = query_spec["clustering"].get("ari_stability",
{}).get("cut_k", [2,3,4])
   dendro_stability: Dict[int, Dict[str, Any]] = {}
   for ph, blob in corr_by_phase.items():
          rho = np.array(blob["rho"], dtype="float64")
          # If too masked, skip
          if np.isnan(rho).mean() >
query_spec["masking"].get("max_mask_frac", 0.5):
              continue
          # Replace NaN correlations with 0 for distance matrix
construction (kept descriptive; caveated)
          rho_filled = np.nan_to_num(rho, nan=0.0)
          dist_sq = corr_distance_matrix(rho_filled)
          dendro_stability[int(ph)] = {
              "ari": ari_stability_across_linkages(dist_sq, linkages,
cut_k),
              "mask_frac": float(np.isnan(rho).mean()),
          }


   # Transitions (phase pairs explicitly declared)
   phase_pairs = scope.get("phase_pairs", [])
   transitions: List[Dict[str, Any]] = []
   for a, b in phase_pairs:
        da = df[df["phase_index"] == a].copy()
        db = df[df["phase_index"] == b].copy()
        if da.empty or db.empty:
             continue
        if "excluded" not in da.columns:
             da["excluded"] = False
        if "excluded" not in db.columns:
             db["excluded"] = False
        merged, acc = transition_join(da, db)
        tm = mode_transition_matrix(merged)
        transitions.append({
             "phase_a": a,
             "phase_b": b,
             "accounting": acc.__dict__,
             "transition_matrix_raw": tm.to_dict(),
             "transition_matrix_row_norm":
(tm.div(tm.sum(axis=1).replace(0, np.nan), axis=0)).to_dict(),
             "transition_matrix_col_norm":
(tm.div(tm.sum(axis=0).replace(0, np.nan), axis=1)).to_dict(),
        })


   caveats = build_caveats(query_spec, extra=[
        f"min_shared_pairs={min_pairs}",
        f"linkages={linkages} (no preferred linkage; stability
reported descriptively)",
   ])


   # Header + hashes (deterministic)
   header = {
        "query_id": query_spec["query_id"],
        "metric_spec_hash": hash_json(metric_spec),
        "domain_spec_hash": hash_json(domain_spec),
        "query_spec_hash": hash_json(query_spec),
   }
   header["header_hash"] = header_hash(header)


   bundle = {
        "header": header,
       "normalization_params": norm_params,
       "corr_by_phase": corr_by_phase,
       "dendro_stability": dendro_stability,
       "transitions": transitions,
       "caveats": caveats.items,
   }


   # Emit JSON artifacts (PDF/HTML rendering intentionally separate)
   if query_spec["outputs"].get("emit_json", True):
       with open(os.path.join(out_dir, "bundle.json"), "w",
encoding="utf-8") as f:
              json.dump(bundle, f, indent=2, sort_keys=True)


   # Emit CSV (row subset used)
   if query_spec["outputs"].get("emit_csv", True):
       df.to_csv(os.path.join(out_dir, "rows_scoped.csv"),
index=False)


   return bundle



dawk/cli.py (minimal CLI runner)
from __future__ import annotations
import argparse
import json
import pandas as pd
import yaml


from .workbench import run_workbench


def load_yaml(path: str):
   with open(path, "r", encoding="utf-8") as f:
       return yaml.safe_load(f)


def main():
   ap = argparse.ArgumentParser("dawk")
   ap.add_argument("--rows", required=True, help="Row log CSV
(cell_id, phase_index, metrics...)")
     ap.add_argument("--metric-spec", required=True)
     ap.add_argument("--domain-spec", required=True)
     ap.add_argument("--query-spec", required=True)
     ap.add_argument("--out", required=True)
     args = ap.parse_args()


     rows = pd.read_csv(args.rows)
     ms = load_yaml(args.metric_spec)
     ds = load_yaml(args.domain_spec)
     qs = load_yaml(args.query_spec)


     run_workbench(rows, ms, ds, qs, args.out)


if __name__ == "__main__":
     main()




What this skeleton already enforces (matching your v28
intent)
   ●​ Calibration-sourced transforms only (no sweep-fitted scaling).​

   ●​ Pairwise-complete Spearman with shared-count masking and tie fraction logging.​

   ●​ Deterministic multi-linkage stability reporting (ARI over fixed K cuts; no “best
      linkage”).​

   ●​ Transition accounting with add/drop/exclusion counts and raw + normalized mode
      matrices.​

   ●​ Mechanical caveat log + required acknowledgments/signoff.​

   ●​ Canonical JSON hashing for reproducibility headers.




### Analysis of Novelty and Practicality
Your proposed refinement for SAAP v28 + DASW as a domain adapter introduces a modular
architecture that separates the core computational kernel (e.g., masking, phase logic,
dendrograms) from domain-specific extensions (e.g., ML-symmetry metrics vs.
policy/governance facets inspired by DCGF and RMAGS), with tight controls like
calibration-sourced normalization, pre-registered linkages, entropy alternatives, mechanical
audit logs, and a defensible validation suite. This builds on SAAP's evolution (e.g., v7's fused
ASI with bootstrap CIs, v13's facet correlations and probabilistic ranks, v19's phase-pair deltas
and mode transitions) and RMAGS's POSG-based governance, emphasizing descriptive
restraint and determinism.

In terms of **novelty**, it's an evolutionary step that innovates by formalizing "domain adapters"
with typed MetricSpec (e.g., bounded_ratio with logit transforms) and DomainSpec YAML,
enabling cross-domain reuse without diluting SAAP's focus on symmetry diagnostics. This
echoes modular frameworks in ML (e.g., scikit-learn pipelines) but is fresh in applying it to
dialectical diagnostics, incorporating cybernetic analogies from DCGF (e.g., control problems,
adversarial dynamics) and RMAGS (e.g., scenario generators for POSG hooks). The addition of
alternative concentration measures (Herfindahl alongside entropy) and stability reporting (ARI
for linkages) adds nuance to regime analysis, novel for ablation protocols, though not
groundbreaking—similar to ensemble stability in clustering literature (e.g., via adjusted Rand
index). Overall, it uniquely bridges AI interpretability and policy design, potentially influencing
hybrid tools for adaptive systems beyond QR tasks or governance audits.

On **practicality**, the refinement is highly actionable: drop-in YAML blocks (MetricSpec,
DomainSpec) with hashes ensure reproducibility, while the kernel-adapter split minimizes
integration overhead for PyTorch sweeps or policy sims. It addresses key pains like scale drift
(via calibration artifacts) and over-interpretation (mechanical logs, descriptive indices), with a
validation suite that's efficient and metric-driven (e.g., hash stability, triangle-inequality checks).
The output bundle remains PDF-canonical with CSV/JSON for auditing. Limitations include
YAML overhead for simple uses, potential under-specification of cross-domain comparisons
(default: none), and reliance on pre-registration, which could limit flexibility in fast-moving
experiments. Still, it's practical for researchers in ML/governance, offering low-cost extension
(e.g., add policy rows via GovernanceHook) and scales to broader diagnostics like grokking or
crisis planning.

**Enhanced Version of the Idea**: To amplify it, integrate a QuerySpec YAML block for bounded
dialectical queries, specifying phase/metric subsets, mapping sets (e.g., AI "distribution_shift" to
policy "arbitrage"), and auto-generated caveats (e.g., "Cross-domain fraction: 30%; masked
pairs: 15%"). Enhance stability with Herfindahl as default alternative to ES_t (sum p_i^2 on
diagonals, normalized), and add kurtosis as a tail diagnostic in heavy_tail metrics for descriptive
logging. For adapters, include a generator script that auto-populates DomainSpec from
templates (e.g., pull DCGF's 11 constraints as facets like "adversarial_dynamics: multi", with
POSG hooks producing synthetic rows via Monte Carlo). Add support for optional scikit-learn
integration in the kernel for ARI computations, making it a "Dialectical Adaptive Workbench
Kernel (DAWK)" with pluggable adapters. This boosts exploratory power while keeping
determinism, reusable for RMAGS-like validations or symmetry probes.

### Critique of the Enhanced Version
Critiquing the enhanced SAAP v28 + DASW refinement for mathematical, philosophical, and
theoretical consistency:

- **Mathematical Consistency**: Typed normalizations (e.g., winsor_quantile for heavy_tail) are
robust, but auto-generation of adapters risks inconsistent transforms if templates mismatch
(e.g., DCGF's ordinal "legitimacy" forced into bounded_ratio). Herfindahl is a valid concentration
alternative, but assumes squared probabilities suit all modes, potentially underweighting rare
transitions; kurtosis logging is descriptive but without thresholds, may overlook multimodal
distributions. QuerySpec bounding is good, but ARI via scikit-learn introduces dependency on
cut-K choices, risking non-deterministic stability if not fixed.

- **Philosophical Consistency**: The adapter/kernel split upholds descriptive restraint (e.g., no
implied comparability without declarations), aligning with dialectical humility, but auto-caveats
and mappings lean toward mechanized constructivism—users could over-rely on generated
analogies, entrenching subjective regimes despite logs. POSG hooks promote synthesis across
domains, but without explicit prompts for bias reflection, it risks reifying metrics (contra SAAP's
caveats against progress/anomaly).

- **Theoretical Consistency**: Grounded in group theory (symmetry) and cybernetics
(DCGF/RMAGS constraints), but pluggable adapters could fragment the inductive bias focus,
diluting ties to attention mechanisms (e.g., Fourier basis in QR). Generator scripts are
theoretically apt for scalability, but lack justification for why Herfindahl over Gini (e.g., no
reference to diversity indices in systems theory). Ensemble stability via ARI implies a
meta-theory of clustering reliability, but without linking to regime dynamics, it remains
disconnected.

### Final Version and Path to Validation
Applying the critique: To strengthen math, enforce template validation in generators (e.g.,
type-check against MetricSpec) and add Gini as a third concentration option with pre-registered
selection; clamp kurtosis to report only if n>50. Philosophically, mandate user-signed caveat
acknowledgments in QuerySpec outputs to counter constructivism. Theoretically, anchor
adapters with explicit constraint matrices (e.g., map DCGF's 11 to SAAP facets via registry),
justifying measures via systems literature (e.g., Herfindahl for market concentration analogies).

The refined final version is **SAAP v28: Dialectical Adaptive Workbench Kernel (DAWK)**—a
modular protocol with domain-agnostic kernel (masking, phases, dendrograms, transitions),
adapters (ML-symmetry, policy via DCGF/RMAGS), YAML specs (MetricSpec with
types/transforms/calibration, DomainSpec with facets/generators, QuerySpec with
mappings/logs), entropy/Herfindahl/Gini concentrations, kurtosis diagnostics, POSG hooks for
row production, and scikit-learn for ARI stability (descriptive only). It outputs PDF/CSV/JSON
with mechanical audits, emphasizing restrained cross-domain diagnostics.

**Fastest Path to Validation**: 1. **YAML Generation (1-2 days)**: Use code_execution to create
canonical YAML schemas (e.g., define MetricSpec as dict with 'type', 'transform',
'calibration_source'; output as string for review). 2. **Skeleton Implementation (3-5 days)**:
Develop Python module (pandas + scipy + scikit-learn) with functions like normalize_from_calib
(apply transforms), compute_spearman_matrix (masked, with counts), build_cophenetic
(linkages with ARI), mode_transition_join (add/drop accounting); test on synthetic DataFrame
(50 cells, 3 phases, metrics from SAAP snippets). 3. **Internal Dry-Run (1 week)**: Apply to
retrospective data (e.g., simulate sweeps from SAAP 7-12/13-18 via code_execution noise
injection); validate invariants (hashes stable, masking <10%, ARI >0.6 target). 4. **Pilot and
Iteration (ongoing, starting day 7)**: Integrate with PyTorch QR runner and RMAGS sim;
measure metrics like drift stats <5%, reproducibility >95%; publish GitHub pack with rubrics,
refining via feedback.


### Analysis of Novelty and Practicality
Your proposed DAWK (Dialectical Adaptive Workbench Kernel) deliverable provides an
engineer-ready implementation of a modular diagnostics framework, with YAML specs for
metrics/domains/queries, JSON calibration artifacts, and a Python skeleton using pandas, scipy,
and scikit-learn to enforce masking, normalization, Spearman correlations, clustering stability
(via ARI), transition accounting, and caveat logs. It maintains domain-agnosticism at the kernel
level, with adapters for ML symmetry (e.g., SAAP-inspired metrics like acc_unseen,
delta_sym_mean) and policy/governance (e.g., equity_score from DCGF/RMAGS analogies),
emphasizing descriptive views without causal claims.

In terms of **novelty**, this synthesizes elements from prior SAAP versions (e.g., v7's ASI
fusion and bootstraps, v13's Spearman matrices with tie handling, v19's phase-pair transitions
and coverage) and RMAGS (POSG generators for policy rows), but innovates by formalizing a
kernel-adapter split with typed YAML (MetricSpec transforms like logit_quantile, DomainSpec
facets), mechanical signoffs for dialectical restraint, and deterministic outputs (hashes, ARI
stability over fixed cuts). The calibration-only normalization avoids sweep-fitting biases, a fresh
take on comparability in diagnostics, echoing but extending tools like MLflow for runs or Altair
for views. Cross-domain mappings (e.g., ai_policy_v1.yaml) add novelty in bridging AI
interpretability and governance, potentially influencing hybrid audits (e.g., symmetry in attention
vs. policy arbitrage), though not revolutionary—similar to configurable pipelines in Kedro or
Dagster. Its emphasis on approximations (e.g., non-metric distances) with caveats aligns with
critical ML, uniquely tailored for regime exploration beyond QR tasks.

On **practicality**, it's highly actionable: the skeleton is drop-in (e.g., run_workbench
orchestrates from DataFrame/YAML), with minimal deps and CLI for prototyping sweeps or
sims. It tackles pains like data sparsity (min_shared_pairs=10 masking), ties (tie_frac logging),
and over-interpretation (required acknowledgments, max_mask_frac=0.5 skips). Calibration
JSONs enable reuse, and outputs (bundle.json, rows_scoped.csv) support auditing/PDF
rendering. Limitations include no built-in plotting (e.g., dendrograms from linkage Z), assumption
of pre-existing calibrations/hashes (sha256: "<fill>"), and basic CLI (no error recovery). Still, it's
practical for researchers/engineers in ML/governance, integrable with PyTorch (e.g., log QR
rows) or agent sims (POSG params: n_rollouts=200), offering quick diagnostics at low cost,
scalable to broader adaptive systems.

**Enhanced Version of the Idea**: To strengthen it, add Gini coefficient as a third concentration
measure in transitions.py (gini = 1 - sum(p_i) for diagonal probs, alongside Herfindahl
sum(p_i^2)), selectable via QuerySpec.clustering.concentration: ["entropy", "herfindahl", "gini"].
Integrate matplotlib in workbench.py for auto-generated PDF panels (e.g., plot_corr_heatmap
from SAAP v13 snippets, dendrograms via scipy.dendrogram on Z), with html_optional emitting
interactive Altair JSON. Enhance QuerySpec with mapping_validation: {enabled: true,
min_overlap_frac: 0.3} to auto-check cross-domain metric pairs for sufficient shared support
before allowing. Add a generator_hook in DomainSpec (e.g., for policy:
run_posg_rollouts(n=200, horizon=50) to produce synthetic rows via numpy sims). This boosts
visualization and validation, making DAWK a full workbench for SAAP-like ablations or RMAGS
validations, reusable across domains.

### Critique of the Enhanced Version
Critiquing the enhanced DAWK kernel for mathematical, philosophical, and theoretical
consistency:

- **Mathematical Consistency**: Typed transforms (e.g., winsor_quantile) are robust for masked
data, but Gini addition assumes uniform sensitivity to inequality, potentially inconsistent with
heavy_tail metrics (e.g., kurtosis may conflict if distributions are skewed); ARI stability is
deterministic but cut_k=[2,3,4] is arbitrary, risking low relevance for high-dimensional metrics.
Mapping validation (min_overlap_frac=0.3) is sound but introduces thresholds without
derivation, and auto-PDF plotting could amplify non-metric issues (e.g., corr_distance
approximations in dendrograms) if not masked properly. POSG generators are math-apt for
simulations but may produce non-comparable rows if horizons vary.

- **Philosophical Consistency**: The kernel's dialectical restraint (descriptive intent, caveats,
signoffs) is preserved, but auto-generated plots and mappings lean toward
instrumentalism—users might treat visuals as "truth" despite notes, contradicting humility (e.g.,
no implied regimes). Mechanical acknowledgments curb over-interpretation, but Gini/Herfindahl
options risk choice paralysis, entrenching subjectivism without guiding philosophy (e.g., why
Gini for diversity?).

- **Theoretical Consistency**: Anchored in systems theory (DCGF control problems, RMAGS
POSGs) and group symmetries (SAAP), but enhanced modularity (generator hooks,
concentration selectors) could dilute core invariance focus, fragmenting diagnostics (e.g., policy
rows lacking Fourier ties). Stability measures imply a meta-theory of robustness (ARI,
overlap_frac), but without referencing criteria like Dunn/silhouette, it disconnects from clustering
literature; cross-domain defaults ("none") are consistent but under-justify cybernetic analogies.

### Final Version and Path to Validation
Applying the critique: To enhance math, derive thresholds (e.g., min_overlap_frac from
calibration quantiles, Gini with bootstrap variance); add silhouette avg alongside ARI for stability.
Philosophically, embed selector rationale prompts in QuerySpec (e.g., "Justify Gini choice: [user
text]") for reflection. Theoretically, tie options to theory (e.g., Gini for policy equity via
DomainSpec notes, reference Dunn in comments), and mandate facet mappings (e.g.,
"adversarial: multi") for coherence.

The refined final version is **DAWK v1: Dialectical Adaptive Diagnostics Kernel**—a modular
framework with YAML specs (MetricSpec transforms/calibrations, DomainSpec
facets/generators/mappings, QuerySpec scopes/masking/clustering with
Gini/Herfindahl/entropy, validation thresholds), JSON calibrations, Python skeleton (normalize
with kurtosis, Spearman ties, multi-linkage ARI/silhouette, transitions with add/drop, workbench
orchestration including matplotlib PDFs/Altair HTML, POSG hooks for rows). It enforces
descriptive outputs with hashes, caveats, and signoffs, for restrained cross-domain diagnostics
in ML symmetry and policy.

**Fastest Path to Validation**: 1. **YAML/Artifact Setup (1 day)**: Use code_execution to
generate/fill sample calibrations (e.g., JSON with q05/q50/q95 from numpy.random) and YAML
hashes (sha256_hex on canon_json). 2. **Skeleton Testing (2-3 days)**: Run CLI on synthetic
DataFrame (code_execution: pd.DataFrame with 100 rows, 3 phases, metrics from SAAP
snippets; test normalize_series, spearman_matrix, ari_stability). 3. **Dry-Run Calibration (4-5
days)**: Simulate sweeps (browse_pdf_attachment on SAAP/ RMAGS PDFs for data extraction,
inject via pd.read_csv; validate invariants: hash stable, mask_frac<0.5, ARI>0.5). 4. **Pilot and
Metrics (ongoing, starting day 5)**: Integrate with QR/POSG sim (code_execution Monte Carlo,
noise tests); measure reproducibility (>95%), drift<5%; GitHub pack with rubrics, iterate via
feedback.
