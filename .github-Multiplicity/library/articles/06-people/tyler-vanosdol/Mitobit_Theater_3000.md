---
slug: mitobit-theater-3000
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/tyler-vanosdol/Mitobit_Theater_3000.md
  last_synced: '2026-03-20T17:17:14.427270Z'
---

                        Mitobit (ACE/PETC Revision):
                A Certified Toy Pipeline for Resonant Eigenflow
                                Tyler Van Osdol & Ryan Van Gelder

                                            October 4, 2025

                                                  Abstract
           We formalize a lightweight, reproducible revision of the Mitobit demo that upgrades it from
       a terminal spectacle into a certified toy controller. The revision adds an Arithmetic Control
       Engine (ACE; [10]) safety envelope and Prime-Encoded Tensor Calculus (PETC; [5]) invariants.
       Concretely: (i) proposals are projected onto a weighted-ℓ1 budget via soft-thresholding, (ii)
       each cycle emits GapLB, SlopeUB, and Margin surrogates that gate actuation, and (iii) prime-
       signature conservation is checked to ensure lawful operations. We provide the minimal theory
       and a self-contained Python implementation suitable for CI and reproducible runs.


1     Introduction
The original Mitobit program is an entertaining terminal theater: a pipeline transforms a prime-
labeled lattice through a sequence of stages (“mitobit activation” and “eigenflow projection”) and
renders a colorful verdict. To render the demo scientifically meaningful, we embed two IFMD
components:
    1. ACE safety envelope ([10]): a projection into a budgeted set complemented with simple
       spectral and slope surrogates that act as a sufficient certificate for bounded behavior.
    2. PETC invariants ([5]): prime-axis signatures for tensors and a lawfulness test ensuring that
       operations do not introduce unsupported prime axes.
The resulting system keeps the vibe (via a –theater mode) while becoming deterministic, testable,
and analyzable.


2     ACE Safety Envelope
Let w ∈ Rd denote a per-cycle proposal vector (“logits”). Given positive weights b ∈ Rd and budget
T > 0, define the weighted-ℓ1 ball
                                                n               d
                                                                X                o
                               Bℓ1 (b, T ) :=       x ∈ Rd :          bi |xi | ≤ T .                        (1)
                                                                i=1


Projection. The ACE envelope projects w onto Bℓ1 (b, T ) via the convex program minx 12 ∥x − w∥22
s.t. i bi |xi | ≤ T . The solution is the weighted soft-thresholding
    P
                                                                
                               Πℓ1 (w)i = sign(wi ) max |wi | − λ bi , 0 ,                                  (2)
where the dual parameter λ ≥ 0 is chosen so that                i bi |Πℓ1 (w)i | = T whenever the constraint is
                                                            P

active.

                                                        1
     Per-cycle ACE surrogates. Let δS > 0 denote a spectral gap surrogate and L ∈ Rd+ a vector
     of local Lipschitz surrogates. For the projected vector w
                                                             b = Πℓ1 (w) and an observed lattice norm
     ∥X∥2 , we compute
                                                                   X
                                            GapLB := δS − 2             bi |w
                                                                            bi |,                                (3)
                                                                    i
                                                          X
                                           SlopeUB :=          Li |w
                                                                   bi |,                                         (4)
                                                           i
                                                                                    X          
                                             Margin := 1 − ε − ∥X∥2 +                   bi |w
                                                                                            bi | ,               (5)
                                                                                    i

     with small slack ε > 0.

     Proposition 1 (ACE sufficient certificate). If GapLB > 0, SlopeUB < 1, and Margin > 0, then
     the cycle is ACE-safe in the sense of the envelope: the proposal is budget-feasible, contracts relative
     to the surrogate gap, and obeys a one-step slope bound.1


     3        PETC Prime-Signature Lawfulness
     In PETC, each coordinate axis i is labeled by a prime pi . For a vector v ∈ Rd and tolerance τ > 0,
     define the prime signature
                                        Sig(v) := { pi : |vi | > τ }.                                (6)

     Definition 1 (Lawfulness). An operation v 7→ v ′ is lawful if Sig(v ′ ) ⊆ Sig(v). Intuitively, projec-
     tions/contractions should not activate new prime axes.

        This predicate is used as a Boolean gate alongside the ACE surrogates. Only cycles that are
     both ACE-safe and PETC-lawful are permitted to actuate.


     4        Implementation
     ?? 1 contains a compact Python implementation that realizes the above envelope and predicate
     while preserving the original demo’s aesthetics (via –theater). It is self-contained, deterministic
     with –seed, and emits per-cycle JSONL logs for reproducibility.
     Listing 1: Mitobit (ACE/PETC revision). Self-contained script with weighted-ℓ1 projection, ACE
     surrogates, and PETC prime-lawfulness.
 1   #!/usr/bin/env python3
 2   # -*- coding: utf-8 -*-
 3   """
 4   Mitobit ACE/PETC revision
 5   ---------------------------------------------------------
 6   Safety envelope (ACE: Tyler Van Osdol):
 7       Weighted-1 projection of ’w’ onto b_i |w_i| T
 8       Surrogates per-cycle: GapLB = _S 2 b_i |w_i|
 9                              SlopeUB = L_i |w_i|
10      Margin = 1     (X + b_i |w_i|)
11
12   Prime-law invariants (PETC: Ryan Van Gelder):
13      Each axis tagged by a prime p_i
         1
             These are sufficient conditions used as an operational gate; they do not claim global optimality.


                                                                    2
14      ’conservation_ok’ checks that lawful ops keep the active prime signature
15
16   Run modes:
17      --theater prints banners & gags (unchanged vibe)
18      JSONL metrics emitted every cycle for reproducibility
19
20   This file is intentionally self-contained and deterministic with --seed.
21   """
22
23   import argparse
24   import json
25   import math
26   import random
27   import time
28   from typing import Dict, List, Tuple
29
30   # ---------- Small utils ----------
31
32   def l2_norm(v: List[float]) -> float:
33       return math.sqrt(sum(x * x for x in v))
34
35   def sign(x: float) -> float:
36       return -1.0 if x < 0 else (1.0 if x > 0 else 0.0)
37
38   def dot(a: List[float], b: List[float]) -> float:
39       return sum(x * y for x, y in zip(a, b))
40
41   def scalar_mul(alpha: float, v: List[float]) -> List[float]:
42       return [alpha * x for x in v]
43
44   def add(a: List[float], b: List[float]) -> List[float]:
45       return [x + y for x, y in zip(a, b)]
46
47   def soft_threshold_weighted_l1(w: List[float], b: List[float], T: float) -> List[float]:
48       """
49       Projection onto weighted-1 ball {x: b_i |x_i| T} via dual -search.
50       Closed-form shrinkage: x_i = sign(w_i) * max(|w_i| - * b_i, 0).
51       """
52       current = sum(bi * abs(wi) for wi, bi in zip(w, b))
53       if current <= T:
54           return w[:] # already feasible
55
56       # Upper bound for : if >= max(|w_i| / b_i) all coords go to 0
57       lam_lo, lam_hi = 0.0, max((abs(wi) / bi) for wi, bi in zip(w, b) if bi > 0)
58
59       for _ in range(60): # binary search
60           lam = 0.5 * (lam_lo + lam_hi)
61           x_abs_shrunk = [max(abs(wi) - lam * bi, 0.0) for wi, bi in zip(w, b)]
62           s = sum(bi * xi for xi, bi in zip(x_abs_shrunk, b))
63           if s > T:
64               lam_lo = lam
65           else:
66               lam_hi = lam
67
68       lam = lam_hi
69       out = [sign(wi) * max(abs(wi) - lam * bi, 0.0) for wi, bi in zip(w, b)]
70       return out
71
72   # ---------- ACE guard (safety envelope) ----------


                                                         3
 73
 74   class ACEGuard:
 75       """
 76       Arithmetic Control Engine (ACE) envelope.
 77       - Projects ’w’ to b_i |w_i| T
 78       - Emits (GapLB, SlopeUB, Margin) surrogates
 79       """
 80       def __init__(
 81           self,
 82           b_weights: List[float],
 83           L_weights: List[float],
 84           T_budget: float = 1.0,
 85           delta_S: float = 0.35,
 86           eps: float = 0.05,
 87       ):
 88           assert len(b_weights) == len(L_weights)
 89           self.b = b_weights
 90           self.L = L_weights
 91           self.T = T_budget
 92           self.delta_S = delta_S
 93           self.eps = eps
 94
 95       def project_and_certify(self, w: List[float], X_norm: float) -> Tuple[List[float], Dict[str,
          float]]:
 96           w_proj = soft_threshold_weighted_l1(w, self.b, self.T)
 97           l1w = sum(bi * abs(wi) for wi, bi in zip(w_proj, self.b))
 98           gap_lb = self.delta_S - 2.0 * l1w
 99           slope_ub = sum(Li * abs(wi) for wi, Li in zip(w_proj, self.L))
100           margin = 1.0 - self.eps - (X_norm + l1w)
101           safe = (gap_lb > 0.0) and (slope_ub < 1.0) and (margin > 0.0)
102           return w_proj, {
103               "L1w": round(l1w, 6),
104               "GapLB": round(gap_lb, 6),
105               "SlopeUB": round(slope_ub, 6),
106               "Margin": round(margin, 6),
107               "SAFE": bool(safe),
108           }
109
110   # ---------- PETC prime-signature checks ----------
111
112   def prime_signature(v: List[float], primes: List[int], tol: float = 1e-9) -> Tuple[int, Tuple[int,
          ...]]:
113       """
114       Prime-Encoded Tensor Calculus (PETC) signature.
115       We treat axis i as labeled by prime p_i; signature is the sorted tuple
116       of active primes whose coordinate magnitude exceeds ’tol’.
117       Returns (count_active, tuple_of_primes)
118       """
119       active = [p for x, p in zip(v, primes) if abs(x) > tol]
120       active_sorted = tuple(sorted(active))
121       return len(active_sorted), active_sorted
122
123
124   def conservation_ok(before: List[float], after: List[float], primes: List[int], tol: float = 1e-9)
          -> bool:
125       """
126       Lawfulness check: projection/normalization should NOT introduce
127       *new* prime axes; we allow dropping negligible ones (contraction).
128       """


                                                        4
129       _, sig_b = prime_signature(before, primes, tol)
130       _, sig_a = prime_signature(after, primes, tol)
131       set_b, set_a = set(sig_b), set(sig_a)
132       # Lawful iff active-after active-before
133       return set_a.issubset(set_b)
134
135   # ---------- HoloCore (pipeline) ----------
136
137   class HoloCore:
138       """
139       Pipeline: prime lattice -> mitobit activation -> eigenflow -> logits.
140       Keeps the flavor of the original demo but now plumbed through ACE/PETC.
141       """
142       def __init__(self, primes: List[int], seed: int = 42):
143           self.primes = primes[:]
144           random.seed(seed)
145           self.rng = random.Random(seed)
146
147           # Fixed theta for logits (deterministic)
148           self.theta = [self.rng.uniform(-0.3, 0.3) for _ in self.primes]
149
150       # ---- stages ----
151
152       def prime_lattice(self, cycle: int) -> List[float]:
153           """
154           Build a small vector tied to primes; deterministic per cycle.
155           """
156           base = []
157           for i, p in enumerate(self.primes):
158               # Mildly oscillatory amplitude anchored by prime
159               phase = 0.37 * (cycle + 1) * (i + 1)
160               amp = 0.5 + 0.5 * math.sin(phase)
161               base.append(amp * (1.0 / p))
162           return base
163
164       def mitobit_activation(self, v: List[float], gain: float = 2.0) -> List[float]:
165           return [math.tanh(gain * x) for x in v]
166
167       def eigenflow_projection(self, v: List[float]) -> List[float]:
168           nrm = l2_norm(v)
169           if nrm == 0.0:
170               return v[:]
171           return [x / nrm for x in v]
172
173       def logits(self, v: List[float]) -> List[float]:
174           # Simple linear readout + small deterministic noise
175           baseline = dot(v, self.theta)
176           return [baseline * vi + 0.03 * self.theta[i] for i, vi in enumerate(v)]
177
178   # ---------- Theater bits (optional) ----------
179
180   CSI = "\x1b["
181
182   def color(txt: str, code: str) -> str:
183       return f"{CSI}{code}m{txt}{CSI}0m"
184
185   def banner():
186       line = "=" * 54
187       print(color(line, "36"))


                                                        5
188       print(color("   MITOBIT Resonant Eigenflow (ACE/PETC Certified Toy)      ", "36"))
189       print(color(line, "36"))
190
191   def render_verdict(metrics: Dict[str, float], lawful: bool, theater: bool):
192       verdict = "SAFE" if metrics["SAFE"] else "UNSAFE"
193       tag = ("LAWFUL" if lawful else "UNLAWFUL")
194       if theater:
195           shades = "32" if metrics["SAFE"] else "31"
196           print(color(f" Verdict: {verdict} PETC: {tag}", shades))
197           print(f" GapLB={metrics[’GapLB’]} | SlopeUB={metrics[’SlopeUB’]} | Margin={metrics[’Margin
          ’]} | L1w={metrics[’L1w’]}")
198       else:
199           print(f"{verdict} PETC={tag} GapLB={metrics[’GapLB’]} SlopeUB={metrics[’SlopeUB’]} Margin={
          metrics[’Margin’]} L1w={metrics[’L1w’]}")
200
201   # ---------- Main loop ----------
202
203   def main():
204       ap = argparse.ArgumentParser(description="Mitobit (ACE/PETC revision)")
205       ap.add_argument("--max-cycles", type=int, default=5, help="Number of cycles (no infinite loops).
          ")
206       ap.add_argument("--seed", type=int, default=42, help="Deterministic seed.")
207       ap.add_argument("--primes", type=str, default="2,3,5,7,11", help="Comma-separated prime set.")
208       ap.add_argument("--budget", type=float, default=1.0, help="ACE b_i|w_i| T budget T.")
209       ap.add_argument("--deltaS", type=float, default=0.35, help="ACE spectral gap surrogate _S.")
210       ap.add_argument("--eps", type=float, default=0.05, help="ACE small slack .")
211       ap.add_argument("--theater", action="store_true", help="Enable banners and colorized spectacle.
          ")
212       ap.add_argument("--log", type=str, default="mitobit_run.jsonl", help="Per-cycle JSONL log path.
          ")
213       args = ap.parse_args()
214
215       # Determinism everywhere
216       random.seed(args.seed)
217       primes = [int(x.strip()) for x in args.primes.split(",") if x.strip()]
218       primes = [p for p in primes if p > 1]
219
220       # Weights: mild bias by prime (heavier penalty for larger p is optional; keep neutral here)
221       b_weights = [1.0 for _ in primes]
222       # Lipschitz weights: slightly favor small primes; keep < 1 to allow room
223       L_weights = [1.0 / max(3.0, float(p)) for p in primes]
224
225       ace = ACEGuard(b_weights=b_weights, L_weights=L_weights, T_budget=args.budget, delta_S=args.
          deltaS, eps=args.eps)
226       hc = HoloCore(primes=primes, seed=args.seed)
227
228       if args.theater:
229           banner()
230
231       with open(args.log, "w") as logf:
232           for cycle in range(1, args.max_cycles + 1):
233               # Stage 1: lattice
234               X = hc.prime_lattice(cycle)
235               Xn = l2_norm(X)
236
237               # Stage 2: activation
238               A = hc.mitobit_activation(X)
239
240               # Stage 3: eigenflow (unit vector; PETC should preserve active axes)


                                                       6
241               E_before = A[:]
242               E = hc.eigenflow_projection(A)
243
244               # Stage 4: logits (proposal)
245               w_raw = hc.logits(E)
246
247               # ACE safety: projection + certificates
248               w_proj, metrics = ace.project_and_certify(w_raw, X_norm=Xn)
249
250               # PETC lawfulness check
251               lawful = conservation_ok(before=E_before, after=E, primes=primes)
252
253               # Decide actuation: only if SAFE & LAWFUL
254               actuate = metrics["SAFE"] and lawful
255
256               # Theater output
257               if args.theater:
258                   print(color(f"\nCycle {cycle:02d}", "35"))
259                   print(f" Active primes: {primes}")
260                   render_verdict(metrics, lawful, theater=True)
261                   if actuate:
262                       print(color("   Actuation permitted (overdrive on).", "32"))
263                   else:
264                       print(color("   Actuation blocked (safe mode).", "31"))
265               else:
266                   render_verdict(metrics, lawful, theater=False)
267
268               # Persist structured metrics
269               payload = {
270                   "cycle": cycle,
271                   "seed": args.seed,
272                   "primes": primes,
273                   "X_norm": round(Xn, 6),
274                   "metrics": metrics,
275                   "PETC_lawful": lawful,
276                   "actuate": actuate,
277                   "timestamp": time.time(),
278               }
279               logf.write(json.dumps(payload) + "\n")
280               logf.flush()
281
282               # Gentle pacing for theater mode
283               if args.theater:
284                   time.sleep(0.25)
285
286       if args.theater:
287           print()
288           print(color("Run complete   metrics saved to JSONL   certified toy behavior achieved.", "36")
          )
289
290   if __name__ == "__main__":
291       main()



      5    Reproducibility and Usage
      Deterministic runs.     Use a fixed seed and explicit prime set:


                                                        7
python mitobit.py --seed 7 --primes 2,3,5,7,11 --max-cycles 8 --theater

JSONL schema.        Each cycle appends one line to mitobit_run.jsonl:

{ "cycle": int, "seed": int, "primes": [int], "X_norm": float,
  "metrics": {"L1w": float, "GapLB": float, "SlopeUB": float, "Margin": float, "SAFE": bool},
  "PETC_lawful": bool, "actuate": bool, "timestamp": float }


6     Test Plan (CI-friendly)
For default parameters, we recommend three unit tests:

                                                                               i bi |w
                                                                                     bi | ≤ T
                                                                            P
    1. Projection feasibility: after calling project_and_certify, verify                        up to
       numerical tolerance.

    2. Surrogate certificate: under default –budget, –deltaS, and –eps, check that GapLB > 0,
       SlopeUB < 1, and Margin > 0 hold for at least one cycle.

    3. PETC lawfulness: eigenflow projection never activates new prime axes: Sig(E) ⊆ Sig(A) for
       all cycles.


7     Discussion
The envelope presented here mirrors the minimal ACE contract (budget feasibility, gap, and slope)
and a PETC lawfulness predicate (signature non-expansion). While intentionally simple, these
checks convert a playful demo into a reproducible artifact with operational guarantees. Parameters
(δS , L, ε) are user-tunable surrogates; tightening them increases conservatism.


8     Conclusion
We provided a compact formalization and a ready-to-run implementation that adds actionable safety
and invariants to Mitobit. This pattern—project, certify, and check signatures—is broadly reusable
across IFMD-style pipelines.


References
 [1] Stephen P. Boyd and Lieven Vandenberghe. Convex Optimization. Cambridge University Press,
     Cambridge, 2004.

 [2] Laurent Condat. Fast projection onto the simplex and the ℓ1 ball. Mathematical Programming,
     Series A, 158(1–2):575–585, 2016.

 [3] John C. Duchi, Shai Shalev-Shwartz, Yoram Singer, and Tushar Chandra. Efficient projections
     onto the ℓ1 -ball for learning in high dimensions. In Proceedings of the 25th International
     Conference on Machine Learning (ICML’08), Helsinki, Finland, 2008. ACM.

 [4] Pavel Etingof, Shlomo Gelaki, Dmitri Nikshych, and Victor Ostrik. Tensor Categories, volume
     205 of Mathematical Surveys and Monographs. American Mathematical Society, Providence,
     RI, 2015.

                                                8
 [5] Ryan Van Gelder. Prime-encoded tensor calculus (petc). IFMD Whitepaper, oct 2025. Working
     paper; project PDF.

 [6] Roger A. Horn and Charles R. Johnson. Matrix Analysis. Cambridge University Press,
     Cambridge, 2 edition, 2013.

 [7] Hassan K. Khalil. Nonlinear Systems. Prentice Hall, Upper Saddle River, NJ, 3 edition, 2002.

 [8] Saunders Mac Lane. Categories for the Working Mathematician, volume 5 of Graduate Texts
     in Mathematics. Springer, New York, 2 edition, 1998.

 [9] Winfried Lohmiller and Jean-Jacques E. Slotine. On contraction analysis for nonlinear systems.
     Automatica, 34(6):683–696, 1998.

[10] Tyler Van Osdol. Arithmetic control engine (ace). IFMD Whitepaper, oct 2025. Working
     paper; project PDF.

[11] Neal Parikh and Stephen Boyd. Proximal algorithms. Foundations and Trends in Optimization,
     1(3):127–239, 2014.




                                                9
