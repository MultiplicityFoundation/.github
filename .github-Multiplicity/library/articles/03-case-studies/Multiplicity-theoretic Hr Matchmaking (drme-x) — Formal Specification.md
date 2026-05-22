---
slug: multiplicity-theoretic-hr-matchmaking-drme-x-formal-specification
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Multiplicity-theoretic Hr Matchmaking (drme-x) \u2014 Formal\
    \ Specification.md"
  last_synced: '2026-03-20T17:17:20.877546Z'
---

Multiplicity-Theoretic HR Matchmaking (DRME-X)
— Formal Specification
0. Purpose and scope
DRME-X is a matching system between job seekers and employment opportunities that represents
candidates, roles, and organizational context as multiplicity states over a prime-indexed ontology.
Matching is computed via a resonance functional that combines (i) intersection multiplicity, (ii) critical-
constraint penalties, (iii) growth alignment, and (iv) hypergraph context compatibility.


This document formalizes: - the prime ontology (feature universe and how primes are assigned/managed),
- evidence rules (how signals update multiplicities), - uncertainty representation (confidence, partial
observability), - stable operator dynamics (bounded updates), - the resonance functional used for
ranking.




1. Core mathematical objects

1.1 Feature universe and prime index

Let F be the set of all atomic features. Each f ∈ F is assigned a unique prime label pf . In implementation,
primes act as stable unique IDs (we do not multiply primes; we store sparse exponent vectors).


1.2 Multiplicity state space

A multiplicity state is a nonnegative vector over features:


                                       x ∈ RF≥0     (sparse in practice)

Interpretation: xf is the multiplicity/exponent weight of feature f for a candidate/role at time t.


We maintain: - Candidate i: xi (t) - Role j : yj (t) - Candidate growth/trajectory: gi (t) - Candidate context
preference/history: ci (t) - Role context signature (team/project): cj (t)


1.3 Hypergraph context

Let H(t) = (V , E(t)) be a hypergraph. - Nodes V : candidates, roles, teams, projects, departments, skill-
communities - Hyperedges        E(t): multi-way relations (team composition, project staffing, workflow
adjacency)


Define a context aggregation operator          AggH producing a feature-vector signal from a node’s
neighborhood.




                                                        1
2. Prime ontology

2.1 Ontology layers

DRME-X uses a structured ontology with four primary layers:


1) Hard skills / tools / domains - e.g., Python, SQL, Kubernetes, Oncology, Accounting


2) Soft traits / behaviors (never purely self-declared) - e.g., collaboration, ownership, conflict navigation


3) Values / preferences / constraints - e.g., remote-first, mission alignment, travel tolerance, salary bands


4) Context features - e.g., team norms, management style, cadence, product lifecycle stage


Each feature f has metadata: - name, description - type ∈ {hard, soft, value, context} - parent
(taxonomy) - synonyms - evidence_policy (how multiplicity is updated) - wf (importance weight for
intersection) - uf (penalty weight if critical and missing)


2.2 Prime assignment policy

Primes are assigned to features by an ontology service. In implementation they may be stored as integer
IDs, but the policy is written as “prime allocation.”


Invariants 1. Uniqueness: each atomic feature maps to exactly one prime ID. 2. Stability: once assigned, a
prime ID never changes. 3. Non-reuse: retired features are never reassigned. 4. Traceability: every feature
records provenance (who/when/why created).


Creation criteria (when to add a new prime) A new feature f is added if and only if: - it is operationally
distinct (would change a hiring decision in plausible cases), and - it has measurable evidence pathways
(Section 3), and - it cannot be represented as a synonym or alias of an existing feature.


Synonyms and aliasing - Multiple surface forms (e.g., “PyTorch”, “Torch”) map to the same feature f . -
Close but distinct skills (e.g., “TensorFlow” vs “PyTorch”) remain separate features but may be connected via
a similarity graph (optional geometric layer).


2.3 Ontology evolution and versioning

      • The ontology is versioned Ot .
      • Matching logs record the ontology version used.
      • New features are appended; no destructive edits to meaning.




                                                        2
3. Evidence rules (how multiplicities are set and updated)

3.1 Evidence types

Evidence e arrives as structured events with source and reliability: - e ∈ E has fields: source, timestamp,
signal, strength, verifiability

Sources: - Verified: assessments, certifications, work samples, portfolio artifacts, manager ratings with
rubric - Behavioral-structured: structured interview rubric items - Observed: performance outcomes, peer
feedback (with governance) - Self-asserted: resume claims, self-ratings (low reliability by default)


Each source s has a reliability coefficient rs ∈ [0, 1].


3.2 Evidence-to-multiplicity update

For each feature f , define an evidence update function Uf producing an increment Δxf :


                                Δxf = Uf (e) = rsource(e) ⋅ ϕf (e) ⋅ ψ(Δt)

where: - ϕf (e) maps evidence strength to a multiplicity increment, - ψ(Δt) is a recency factor (e.g.,
exponential decay).


Boundedness rule For stability and interpretability, impose:


                                               0 ≤ xf (t) ≤ Xfmax

with Xfmax feature-specific caps.


3.3 Hard skill multiplicity templates

Hard skills are updated via evidence-based templates:


Template HS-1 (work sample / assessment) - If assessment score q ∈ [0, 1]:


                                                Δxf = rs ⋅ af ⋅ q

Template HS-2 (experience duration) - If verified experience months m:


                                          Δxf = rs ⋅ bf ⋅ log(1 + m)

Template HS-3 (credential / certification) - If credential level ℓ ∈ {1, 2, 3}:


                                                Δxf = rs ⋅ cf ⋅ ℓ




                                                           3
3.4 Soft trait multiplicity (evidence-backed)

Soft traits require structured, multi-source evidence.


Define for a soft trait feature f : - a rubric with items k = 1..K , each yielding a score qk ∈ [0, 1] - minimum
evidence diversity: at least two distinct sources among {interview rubric, peer feedback, work sample
observations}


Soft trait update:


                           Δxf = min (Xfmax − xf , rs ⋅ af ⋅ Avg(q1 , … , qK ))

Self-assertion rule (soft traits) Self-asserted soft traits do not directly increase xf ; instead they update a
prior for uncertainty (Section 4) until corroborated.


3.5 Role feature construction

Role vectors yj are built from: - job description parsing (weak evidence) - hiring manager rubric for must-
haves (strong evidence) - team context signatures (strong evidence)


Split role requirements: - Critical thresholds cj (must-have) - Preference components (nice-to-have)




4. Uncertainty representation (PMDM-lite)

4.1 Diagonal uncertainty model

For each candidate i, maintain a diagonal uncertainty vector:


                                                 σi ∈ [0, 1]F

Interpretation: σi,f is uncertainty about xi,f (higher means less certain).


Initialize: - verified evidence ⇒ low uncertainty - self-asserted evidence ⇒ high uncertainty


Update rule:


                     σi,f (t + 1) = (1 − λf ) σi,f (t) + λf exp(−κ evidence_countf )

Where λf is a feature-specific learning rate.


4.2 Uncertainty-aware intersection

Define an uncertainty-discounted intersection:




                                                        4
                                Iunc (x, y; σ) = ∑ wf (1 − σf ) min(xf , yf )
                                                  f ∈F

This causes uncertain claims to contribute less until verified.


4.3 Optional full PMDM

In high-stakes deployments, represent a candidate state as a positive semidefinite matrix ρ over a feature-
embedding space, capturing correlations (e.g., clustered skills). This is optional; DRME-X defaults to
diagonal uncertainty.




5. Stable operator dynamics

5.1 Operator set (bounded semigroup)

Operators act on multiplicity vectors with bounded outputs: - Dilation: Dα (x) = αx, with α ∈ [αmin , αmax ]
- Mixing: MA (x) = Ax, where A ≥ 0, sparse, and ∥A∥ bounded - Projection: PS keeps a selected feature
subset - Context lift: CH (x) = x + γ AggH (x), with γ bounded - Normalization/projection: Π enforces
nonnegativity, caps, and optional ℓ1 sparsity


5.2 Evolution law (candidate)

Let evidence stream for candidate i be ei (t). Then:


                        xi (t + 1) = Π(MA(t) (xi (t)) + U (ei (t)) + γ AggH (xi (t)))

Where U (ei (t)) aggregates Uf (e) over features.


5.3 Evolution law (role)

Roles drift with market and team changes:


                           yj (t + 1) = Π(yj (t) + Δyjmarket (t) + Δyjmanager (t))



6. Resonance functional (match score)

6.1 Intersection (fit) term

                                       Iij (t) = Iunc (xi (t), yj (t); σi (t))

6.2 Growth alignment

                                           Gij (t) = I(gi (t), yj (t))




                                                         5
6.3 Context compatibility

                                            Kij (t) = I(ci (t), cj (t))

6.4 Missing-critical penalty

Let cj be critical thresholds:


                                    Pij (t) = ∑ uf max(0, cj,f − xi,f (t))
                                              f ∈F


6.5 Final match score

                       Matchij (t) = σ(αIij (t) + βGij (t) + ηKij (t) − δPij (t) + bj )

Where σ is a squashing function (e.g., logistic) and bj is a role bias/intercept.




7. Explainability payload (required output)
For each recommendation, return: - top contributing intersection features                 arg maxf wf (1 −
σf ) min(xf , yf ) - missing critical requirements and gap sizes - which context factors contributed -
uncertainty flags (“this claim is unverified; discount applied”)




8. Validation protocol (fast path)

8.1 Offline

      • Evaluate ranking quality: NDCG@k, MAP, Recall@k
      • Calibrate probabilities: reliability diagrams / Brier score
      • Compare against baselines: embedding cosine, LTR, weighted Jaccard

8.2 Online pilot (decision support)

      • Measure recruiter time-to-shortlist, interview-to-offer conversion
      • Track 90/180-day retention uplift
      • Monitor drift and fairness metrics before enabling recursive updates




9. Minimal implementation checklist
      • [ ] Ontology service (feature registry, prime IDs, versioning)
      • [ ] Evidence ingestion + reliability coefficients
      • [ ] Sparse vector store for x/y/g/context + uncertainty
      • [ ] Hypergraph adjacency + aggregation



                                                        6
• [ ] Resonance scorer + explanation payload
• [ ] Logging, audits, fairness monitoring, drift monitoring




                                                 7
