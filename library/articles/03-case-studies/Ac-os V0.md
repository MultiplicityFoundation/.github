---
slug: ac-os-v0
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Ac-os V0.md
  last_synced: '2026-03-20T17:17:21.143175Z'
---

AC‑OS v0.2 — Aspectual Counting Operating
System (Research‑Grade Package)

Executive Summary
AC‑OS turns identity/count disputes into a constraint‑selected bridge problem with principled certificates.
We model aspects as functors to finite sets, bridges as lax natural relations (modalities: id, map, evidence),
and strictness as cannot‑link relations. Selection becomes core‑guided Weighted Partial MaxSAT / ILP over
a conflict hypergraph; explanation is via unsat cores/MUS, k‑shadow (arity‑bounded relaxations),
dominance and unavoidable‑tail certificates. v0.2 adds explicit situation scope, modality constraints,
simplified certificates, and context‑merge provenance.




1) Novelty + Practicality
Novel (as a package)


     • Counting = audited bridge selection. “No bridge, no transfer.” Paradoxes reduce to selecting a
       maximum‑weight feasible subset with proofs.
     • Interaction order as a diagnostic. Use minimal conflict arity and k‑shadow convergence to certify
       when pairwise governance fails.

Practical


     • Ship v1 with Weighted MaxSAT or ILP, MUS/core extraction, and human‑readable witness paths.
     • k‑shadow gives monotone tightening: fast approximate decisions with explicit convergence tests.




2) Enhanced Version (v0.2 highlights)
     • Situation scope: bridge scope ∈ {per‑situation, cross‑situation, global} ; per‑edge
        situation required in the first case.
     • Modality constraints: map requires max_out_degree ; evidence requires
        evidence_threshold (bridge‑level), with optional per‑situation thresholds.
     • Certificate simplification: k_shadow reports {k, objective} ; cores have stable string IDs;
       methods renamed to neutral ( fractional_matching , lp_dual , hitting_set ).
     • Context join semantics: provenance via ancestors , merge_strategy , and semantic weight
       merges ( sum , left_prefer , right_prefer , max ).




                                                      1
3) Internal Critique (stress points)
      • Closure overcommit: not all bridges should induce equivalence. We address this with modalities
        and modality‑specific closure rules.
      • Partiality vs functoriality: bridges modeled as lax natural relations to legitimate lossy/partial
        transfer.
      • Arity terminology: use conflict arity and practical conflict arity (k where k‑shadow = optimum) to
        avoid overload with classical Helly.
      • Dominance cost: certify dominance relative to a discovered core basis (solver traces), not the full
        MUS family.




4) Final Spec + Predictions

Semantics

      • Situations: category Oc (context‑scoped).
      • Aspects: functors Uα : Oc → FinSet.
      • Bridges: candidates τ (b) : Uα ⇒ Uβ , modality ∈ { id , map , evidence }, scope as above.
      • Strictness: cannot‑links Sα,X .
      • Selection: choose Γ ⊆ Bc maximizing total weight subject to no cannot‑link is forced by the
       modality closure under Γ.

Predictions

    1. Arity spikes under context joins: benign contexts often have arity 2–3; joins trigger higher arity
       exactly when governance collides.
    2. Concentrated unavoidable drops: #-strict contexts produce a small, interpretable set of excluded
       bridges.
    3. k‑shadow as thermometer: early convergence ⇒ pairwise suffices; delayed convergence ⇒
       genuine higher‑order coupling.
    4. Explanation stability correlates with core stability under small weight perturbations.




5) Mathematical Overview (formal spine)

5.1 Closure & feasibility

Let VX = ⨆α Uα (X). Each bridge b contributes edges Eb,X ⊆ VX × VX . Define modality‑aware closure
RΓ,X = Clmod (⋃b∈Γ Eb,X ).
Feasible iff no (u, v) ∈ SX lies in RΓ,X .


5.2 Conflict hypergraph

Minimal conflicts (MUS‑analogues) Mc yield Hc = (Bc , Mc ). Selection ≡ maximum‑weight independent
set with constraints ∑b∈M xb ≤ ∣M ∣ − 1.




                                                     2
5.3 k‑shadow

Enforce only cores with ∣M ∣ ≤ k . Objectives OPTk decrease monotonically to OPT. The practical conflict
arity is the smallest k where equality holds.


5.4 Certificates

     • Cores with witness paths (shortest‑path forcing a cannot‑link).
     • Dominance (basis‑relative).
     • Unavoidable tail via fractional matchings / LP duals / hitting sets.




6) Fastest Validation Path
    1. Executable core: data ingestion, modality closures, feasibility check.
    2. Solver: Weighted Partial MaxSAT (preferred) or ILP; adopt core‑guided flow.
    3. Artifacts: cores with witness paths; k‑shadow trajectory (k=2,3,4,…).
    4. Datasets: (i) Synthetic Theseus (tunable arity); (ii) ER/record‑linkage with must/cannot‑links.
    5. Success: optimum found; explanations stable; k‑shadow distinguishes MUS2 vs higher‑order.




7) Artifacts (v0.2)
     • Schemas: acos_instance.v0.2.schema.json , acos_certificate.v0.2.schema.json
     • Utilities: acos_validate.py (schema + semantic checks), acos_witness.py (shortest‑path
       witness).
     • Examples: example_v0.2_instance.json (with map + evidence ),
        example_v0.2_certificate.json , plus example_v0.2_core_based.wcnf and
        example_v0.2_from_cores.lp .

       Note: Downloads were shared in‑chat; keep these filenames synchronized with your repo.




8) CLI Sketch

  acos solve
    --instance example_v0.2_instance.json
    --model weighted_maxsat|ilp
    --encoding core_based|full
    --k-shadow 2..6
    --emit witness
    --out certificate.json
    --validate




                                                      3
9) Witness Generation (algorithmic note)
  1. Build mixed‑mode graph from selected bridges ( id undirected; map directed; expand evidence
    into active id edges once thresholds are met).
  2. For each cannot‑link pair, run BFS/shortest‑path; the first reachable pair yields a minimal witness
     path.
  3. Store (violation_pair, path) in the certificate core.




10) Benchmarking & Prediction Tests
   • Arity spikes: run k‑shadow on two benign contexts and on their join; visualize OPTk .
   • Core stability under perturbations: jitter weights; compute Jaccard of core memberships.
   • Human trust vs artifacts: A/B test explanations with/without witness paths and unavoidable‑tail
     bounds.




External References (selected)
   • Core‑guided / iterative MaxSAT surveys and solvers; MUS/MCS/MSS definitions; DRAT/DRAT‑trim
     proof infrastructure; abstract argumentation; constrained ER; hypergraphs, hitting sets, and
     Helly‑style properties; profunctors/spans in category theory.
     See the reference list at end; URLs are provided for reproducibility.




Reference List (with URLs)
   • Morgado, Heras, Marques‑Silva, Planes. Iterative and Core‑Guided MaxSAT Solving: A Survey and
     Assessment (Constraints). PDF: https://sun.iwu.edu/\~mliffito/publications/
     constraints_morgado_maxsat_survey.pdf
   • Pan et al. An Efficient Core‑Guided Solver for Weighted Partial MaxSAT (IJCAI 2025). PDF: https://
     www.ijcai.org/proceedings/2025/0295.pdf
   • Bendík et al. Counting Minimal Unsatisfiable Subsets (CAV 2021). PDF: https://jar-ben.github.io/papers/
     CAV2021.pdf
   • Heule. The DRAT format and DRAT‑trim checker (arXiv:1610.06229). https://arxiv.org/abs/1610.06229
     Wetzler, Heule, Hunt. DRAT‑trim: Efficient Checking and Trimming (SAT/UTexas). PDF: https://
     www.cs.utexas.edu/\~marijn/publications/drat-trim.pdf
   • Ansótegui et al. An (In)Complete Algorithm for Weighted Partial MaxSAT (AIJ 2017). https://
     www.sciencedirect.com/science/article/pii/S0004370217300693
   • Dung. On the Acceptability of Arguments… (AI 1995). PDF: https://cse-robotics.engr.tamu.edu/dshell/
     cs631/papers/dung95acceptability.pdf
   • Wang et al. Provenance‑Aware Entity Resolution (DASFAA 2015). PDF: https://users.cecs.anu.edu.au/
     \~u5170295/papers/dasfaa-wang-2015.pdf
     (See also standard ER/linkage surveys.)




                                                    4
     • Berge. Hypergraphs: Combinatorics of Finite Sets (Elsevier 1989). Archive: https://archive.org/details/
       hypergraphscombi0000berg
     • Gyárfás. A Note on Hypergraphs with the Helly Property. PDF: https://users.renyi.hu/\~gyarfas/Cikkek/
       12_Gyarfas_ANoteOnHypergraphsWithTheHellyProperty.pdf
     • nLab. Profunctor. https://ncatlab.org/nlab/show/profunctor
       (Background on profunctors/spans as categorical relations.)



Citizen Gardens © 2025 CC-NC-ND 4.0




                                                       5
