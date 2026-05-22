---
slug: clinical-lab-analytics
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/clinical-lab-analytics/Clinical_Lab_Analytics.md
  last_synced: '2026-03-20T17:17:18.813259Z'
---

    A Production-Ready Framework for Multiplicity Control and
             Quality Control in Clinical Laboratories
                                Kara Olivarria & Ryan O. van Gelder

                                               Citizen Gardens

                                               October 23, 2025


                                                  Abstract
          We formalize a practical, auditable framework for multi-analyte statistical inference and lab-
      oratory quality control. The design combines validated multiplicity adjustments, robust preci-
      sion metrics, classical and multivariate control charts, lot-to-lot equivalence testing, engineering
      interfaces, and quantitative acceptance criteria suitable for regulated environments.


1     Objective
Reduce false positives in multi-analyte panels and strengthen QC using validated, transparent pro-
cedures. Outputs: adjusted p-values, stable precision metrics, timely shift detection, defensible
SOPs.


2     Data Model and Notation
Samples i = 1, . . . , n, analytes j = 1, . . . , m. Measurement Xij . Control result at time t: Qt . Per
analyte: mean µj , standard deviation σj , bias bj , allowable total error TEaj .

2.1    Data-Quality Gates
    • Missingness: compute per-analyte and per-run rates. Warn at 2–4%, block at > 5% unless
      MAR handling is configured. If MCAR test fails [12], escalate to review.
    • Range checks: enforce analytic measurement ranges; soft-flag values within 5% of bounds.
    • Units and monotonicity: verify unit codes; reject mixed units. For control time series,
      forbid impossible jumps given instrument specs.
    • Instrument flags: ingest manufacturer error codes; halt QC updates on critical flags.
    • Duplicates and timing: deduplicate by sample+analyte+timestamp; enforce nondecreasing
      timestamps.
    • Storage: retain raw, cleaned, and derived fields; no destructive edits. All actions logged.


3     Multiplicity Control
Let p1 , . . . , pm be per-analyte p-values.



                                                       1
3.1   Family-wise Error Rate: Holm
Sort p(1) ≤ · · · ≤ p(m) . Find the smallest k with p(k) > α/(m − k + 1). Reject H(r) for r < k.
Controls FWER at α [1].

3.2   False Discovery Rate: Benjamini–Hochberg
Choose target q ∈ (0, 1). Let k = max{r : p(r) ≤ rq/m}. Reject H(1) , . . . , H(k) . Report adjusted
p-values [2].

3.3   Dependence-Aware Options
Benjamini–Yekutieli   controls FDR under arbitrary dependence using thresholds rq/(mHm ) with
Hm = m          [3]. Storey q-values estimate π0 to improve power when many nulls are true [4].
     P
        i=1 1/i

3.4   Reporting Rules
For each panel: report m, method, raw p-values, adjusted p-values, and the set of rejections. Default:
BH at q = 0.05 for exploratory panels; Holm at α = 0.05 for confirmatory reflex rules.

3.5   Pseudocode (BH)

                         Listing 1: Benjamini–Hochberg step-up procedure
import numpy as np

def bh(pvals, q=0.05):
   p = np.asarray(pvals)
   m = len(p)
   order = np.argsort(p)
   thresh = q * (np.arange(1, m+1) / m)
   passed = p[order] <= thresh
   k = np.where(passed)[0].max() + 1 if passed.any() else 0
   reject = np.zeros(m, dtype=bool)
   if k > 0:
      reject[order[:k]] = True
   # adjusted p-values (step-up)
   adj = np.minimum.accumulate((m / np.arange(m, 0, -1)) * p[order][::-1])[::-1]
   adj_full = np.empty_like(p)
   adj_full[order] = np.minimum(adj, 1.0)
   return reject, adj_full



4     Precision and Repeatability
4.1   Coefficient of Variation
Classical CVj = 100 σj /µj %. Robust alternative: σ rob = 1.4826 MAD; use when non-Gaussian.

4.2   Outlier Screening
Robust z-score zi = |Xi − median(X)|/(1.4826 MAD). Flag if zi > 3.5. Review, do not auto-delete.




                                                  2
5     QC Charts
5.1   Shewhart
Limits µ ± 3σ. Rules pre-registered.

5.2   EWMA
Zt = λQt + (1 − λ)Zt−1 , Z0 = µ. Limits µ ± L σ    λ/(2 − λ) [5, 6].
                                                  p

                             Listing 2: Streaming EWMA with limits
class EWMA:
   def __init__(self, mu, sigma, lam=0.2, L=3.0):
      self.mu, self.sigma = mu, sigma
      self.lam, self.L = lam, L
      self.z = mu
   def update(self, q_t):
      self.z = self.lam * q_t + (1 - self.lam) * self.z
      s = (self.sigma * (self.lam / (2 - self.lam)) ** 0.5)
      return self.z, self.mu + self.L * s, self.mu - self.L * s



5.3   CUSUM
Two one-sided CUSUMs: Ct+ = max{0, Qt − (µ + k) + Ct−1
                                                   +
                                                       }, Ct− = max{0, (µ − k) − Qt + Ct−1
                                                                                       −
                                                                                           }.
                     −
Signal if Ct > h or Ct > h [7].
           +



5.4   Multivariate QC
Hotelling T 2 for subgroup mean: T 2 = (x̄ − µ)⊤ Σ−1 (x̄ − µ) with classical F limits [8]. MEWMA
for correlated analytes [9]. Use Ledoit–Wolf covariance shrinkage when p large or n small [10].
Maintain univariate charts for interpretability.


6     Lot-to-Lot Validation
6.1   Design
Paired or bridged patient samples (n ≥ 20) across lots A and B, spanning clinical range. Regression
with intercept and slope; plus equivalence on mean difference.

6.2   TOST Equivalence
Compute ∆ = µB − µA . Accept if −δ < ∆ < δ using two one-sided tests at α = 0.05 [11].

                           Listing 3: Paired TOST for mean difference
from math import sqrt
from statistics import mean, pstdev
from scipy.stats import t, ttest_1samp

def paired_tost(a, b, delta, alpha=0.05):
   d = [bi - ai for ai, bi in zip(a, b)]
   n = len(d)
   mu = mean(d)
   sd = (sum((x - mu) ** 2 for x in d) / (n - 1)) ** 0.5


                                                  3
        se = sd / sqrt(n)
        t1 = (mu + delta) / se # H0: mu <= -delta
        t2 = (delta - mu) / se # H0: mu >= delta
        p1 = 1 - t.cdf(t1, df=n-1)
        p2 = 1 - t.cdf(t2, df=n-1)
        ci = (mu - t.ppf(1 - alpha/2, n-1) * se, mu + t.ppf(1 - alpha/2, n-1) * se)
        return dict(delta_hat=mu, ci=ci, accept=max(p1, p2) <= alpha)



7        Panel-Level Decision Framework
    1. Choose error control (Holm for confirmatory, BH for screening).
    2. Lock thresholds pre-analysis.1
    3. Run and generate adjusted p-values.
    4. Apply clinical interpretation only to rejections.
    5. Record decisions with timestamps and operators.


8        Implementation Architecture
8.1        REST API

                                  Listing 4: FastAPI skeleton for key endpoints
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal, Optional

app = FastAPI()

class PanelRequest(BaseModel):
   panel_id: str
   p_values: List[float]
   method: Literal[’BH’,’Holm’,’BY’] = ’BH’
   q_or_alpha: float = 0.05

@app.post(’/panels/evaluate’)
def panel_evaluate(req: PanelRequest):
   if req.method == ’BH’:
      reject, adj = bh(req.p_values, req.q_or_alpha)
   elif req.method == ’Holm’:
      reject, adj = holm(req.p_values, req.q_or_alpha)
   else:
      reject, adj = by(req.p_values, req.q_or_alpha)
   return {"panel_id": req.panel_id, "adj_p": adj.tolist(), "reject": reject.tolist()}

# /qc/ewma, /qc/cusum, /lot/tost would follow similarly



8.2        Database Schema and Auditability

                                Listing 5: Core tables for audit and configuration
CREATE TABLE audit_log (
    1
        Pre-registration prevents post-hoc tuning on production data.


                                                            4
  id UUID PRIMARY KEY,
  event_time TIMESTAMP NOT NULL,
  user_id VARCHAR NOT NULL,
  endpoint VARCHAR NOT NULL,
  parameters JSONB NOT NULL,
  result JSONB,
  config_version INTEGER NOT NULL
);

CREATE TABLE config_versions (
  version_id INTEGER PRIMARY KEY,
  config_type VARCHAR NOT NULL, -- ’multiplicity’, ’qc’, ’lot’
  parameters JSONB NOT NULL,
  effective_date DATE NOT NULL,
  dataset_hash VARCHAR
);



9     Validation, SLOs, and Acceptance Criteria
9.1    Runtime Targets
Panel evaluation ≤ 100 ms at p99 for m ≤ 500; EWMA update path ≤ 1 s at p99. Uptime ≥ 99.9%.

9.2    Phase 1 Acceptance Criteria
     • Data quality: warnings at 2–4% missing; scoped blocks at > 5%; 100% override audit
       completeness.
     • Multiplicity: BH or Holm live on two panels; latency meets target; reports include m,
       method, raw and adjusted p, rejections.
     • QC replay: ≥20% reduction in detection delay vs baseline at matched false-alarm rate; ≤1
       false alert/1000 runs.
     • Audit: 100% of config changes versioned with author, diff, timestamp.


10      Governance and Training
Parameter board approves λ, L, k, h, q/α pre–go-live. Tiered training by role with competency
checks. Two-week stabilization, advance only if criteria met for two consecutive weeks. Align with
CLIA/CAP and ISO 15189.


11      Rollout Plan
Phase 1: data-quality gates, BH/Holm on 1–2 panels, EWMA on stable controls, Tier-1 dashboard.
Phase 2: CUSUM, TOST, BY, enhanced audit, Tier-2 dashboard. Phase 3: multivariate QC (2–3
analytes), change-point detection, Bayesian equivalence, Tier-3 dashboard.


12      Conclusion
The framework delivers production-grade multiplicity control and QC with clear engineering inter-
faces, measurable acceptance criteria, and defensible governance. It is suitable for immediate Phase
1 deployment with a path to advanced capabilities.

                                                 5
References
 [1] S. Holm, “A simple sequentially rejective multiple test procedure,” Scandinavian Journal of
     Statistics, 6(2):65–70, 1979.

 [2] Y. Benjamini and Y. Hochberg, “Controlling the false discovery rate: a practical and powerful
     approach to multiple testing,” Journal of the Royal Statistical Society: Series B, 57(1):289–300,
     1995.

 [3] Y. Benjamini and D. Yekutieli, “The control of the false discovery rate in multiple testing under
     dependency,” Annals of Statistics, 29(4):1165–1188, 2001.

 [4] J. D. Storey, “A direct approach to false discovery rates,” Journal of the Royal Statistical
     Society: Series B, 64(3):479–498, 2002.

 [5] S. W. Roberts, “Control chart tests based on geometric moving averages,” Technometrics,
     1(3):239–250, 1959.

 [6] J. M. Lucas and M. S. Saccucci, “Exponentially weighted moving average control schemes:
     properties and enhancements,” Technometrics, 32(1):1–12, 1990.

 [7] E. S. Page, “Continuous inspection schemes,” Biometrika, 41(1/2):100–115, 1954.

 [8] H. Hotelling, “Multivariate Quality Control,” in Techniques of Statistical Analysis, 111–184,
     McGraw-Hill, 1947.

 [9] C. A. Lowry, W. H. Woodall, C. W. Champ, and S. E. Rigdon, “A multivariate exponentially
     weighted moving average control chart,” Technometrics, 34(1):46–53, 1992.

[10] O. Ledoit and M. Wolf, “A well-conditioned estimator for large-dimensional covariance matri-
     ces,” Journal of Multivariate Analysis, 88(2):365–411, 2004.

[11] D. J. Schuirmann, “A comparison of the two one-sided tests procedure and the power approach
     for assessing the equivalence of average bioavailability,” Journal of Pharmacokinetics and Bio-
     pharmaceutics, 15(6):657–680, 1987.

[12] R. J. A. Little, “A test of Missing Completely at Random for multivariate data with missing
     values,” Journal of the Royal Statistical Society: Series C (Applied Statistics), 37(3):259–268,
     1988.




                                                  6
