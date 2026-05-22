---
slug: scpn-pmd-report
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/SCPN_PMD Report.md
  last_synced: '2026-03-20T17:17:20.044324Z'
---

Extracted goals, claims, constraints

 ●​ Goals:

      o​ Provide a computationally precise, multi-layer architecture (L1–L16) for
          phase-synchrony and informational transduction.[1]

      o​ Keep the framework empirically open: verification now, validation later, with explicit
          falsification roadmaps.[1]

      o​ Use SCPN as a shared audit surface (UPDE, Knm, Digital Twin, SWARM,
          DIRECTOR_AI, CCW, SCPN‑Studio) rather than as a closed theory.[1]

 ●​ Claims (at v1.0 / v2.6 level):

      o​ UPDE is mathematically coherent and reduces to known synchronization models
          under limit cases.[1]

      o​ The 16-layer stack plus Knm gives a unified phase-dynamics substrate for
          consciousness-related phenomena, but layers 8–16 are largely theoretical or
          stubbed computationally.[1]

      o​ Safety and epistemic safeguards (refusal rules, Ethical Veto, DIRECTOR_AI, SCPN
          boundary discipline) are first-class design elements.[1]

 ●​ Constraints:

      o​ No preregistered, independently replicated empirical validations yet; pilots and
          simulations remain explicitly exploratory.[1]

      o​ High-severity gaps: upper-layer stubs, partial UPDE validation, zero live clinical
          outcomes, incomplete simulation verification.[1]

      o​ Commercialisation and metaphysical readings are out of scope for the technical
          spec and must not be smuggled in as evidence.[1]

 ●​ Stakeholders:

      o​ Framework author and Anulum Institute.[1]

      o​ External auditors, theorists, computational modellers, clinicians, and potential
          funders.[1]
      o​ Downstream implementers of CCW, SCPN‑Studio, DIRECTOR_AI, MAOP, and
         fusion/neuromorphic modules.[1]

 ●​ Horizon:

      o​ Immediate: Q1 2026 (HPC runs, paper validation, pilot RCT).[1]

      o​ Medium-term 2026: Bayesian Knm calibration, Digital Twin validation with live CCW
         sessions, university partnerships.[1]

      o​ Long-term: empirical SCPN validation, regulatory pathway, neuromorphic
         deployment.[1]


Phase mirror dissonance

 ●​ D1 — Verified math vs unverified world [E][S]​
    The spec emphasizes “Verified (Internal)” for UPDE, Knm, and stability logic, while
    world-facing claims (e.g., Li‑6/Li‑7 predictions, Lazarus healing, noospheric phase
    transitions) lack preregistered tests or replications; this creates a tension between formal
    closure and empirical openness that can be misread as overclaiming.[1]

 ●​ D2 — Deep stack vs shallow implementation [S][T]​
    A 16-layer ontology, 32 formalisms, and 678k-file ecosystem coexist with multiple
    high-severity gaps (upper layers as stubs, partial simulation coverage, missing
    HolonomicAtlas runs), so the architectural ambition outpaces what has actually been
    executed and audited end-to-end.[1]

 ●​ D3 — Safety rhetoric vs enforcement reality [S][P][E]​
    DIRECTOR_AI, Ethical Veto, and refusal rules are described as strong safeguards, but they
    currently operate as software patterns with limited external red-teaming and no
    independent safety certification, which undercuts the implied robustness of “malicious
    entropy” containment.[1]

 ●​ D4 — Clinical protocols vs zero outcomes [E][Ec]​
    CCW and the Lazarus Protocol are framed in quasi-clinical language (protocol variants,
    biomarkers, RCT draft, evidence levels) while explicitly noting zero SCPN-mediated
    patient data and heavy reliance on literature extrapolation and simulations, increasing the
    risk of category collapse between “parameterised simulator” and “intervention with
    evidence.”[1]
 ●​ D5 — Centralised authorship vs distributed audit [P][E]​
    Nearly all layers, parameters, and code paths trace back to a single primary
    author/institute while the stated epistemic stance demands adversarial audits,
    independent replications, and Bayesian recalibration; until external groups own specific
    verification streams, governance remains de facto centralised.[1]


Levers to test now

 ●​ [Lead theorist / methods owner] — Lever: Formalise a minimal, externally executable
    UPDE test suite (L1–L4 only) with expected behaviours and pass/fail thresholds. — Metric:
    Number of independent teams that can re-derive UPDE, reproduce Digital Twin R(t)
    trajectories, and match a published reference dataset within predefined error bounds. —
    Horizon: 1–2 quarters.[1]

 ●​ [HolonomicAtlas maintainer] — Lever: Close the “stub gap” by delivering concrete,
    documented solvers for at least one upper-layer Hamiltonian block (e.g., H_geo or
    H_noos) and wiring them into the unified runner. — Metric: Transition of at least 3
    SIMULATION_MAP entries for L7–L12 from “stub/partial” to “verified against internal test
    vectors,” with reproducible notebook artefacts. — Horizon: 1 quarter.[1]

 ●​ [Digital Twin / CCW integration owner] — Lever: Run a tightly-scoped, non-clinical live
    Digital Twin–CCW experiment with healthy volunteers focused solely on signal
    reproducibility (EEG/HRV) rather than outcomes, under preregistered analysis plans. —
    Metric: Fraction of planned sessions completed with full telemetry, plus reproducibility of
    basic coherence metrics (R_global, HRV coherence) across repeated runs; no inference
    about healing. — Horizon: 1–2 quarters.[1]

 ●​ [SWARM_AUTOMATION lead] — Lever: Partition the parameter catalogue into “locked”
    (derivation-frozen) and “live” (subject to SWARM updates) subsets, with explicit
    provenance and confidence labels surfaced in SCPN‑Studio and Digital Twin UIs. —
    Metric: Percentage of parameters with machine-readable provenance, confidence, and
    last-audit timestamp, plus reduction in post-hoc parameter edits flagged by validation
    scripts. — Horizon: 1 quarter.[1]

 ●​ [External auditor / partner PI] — Lever: Design and own one falsifiable SCPN prediction
    test (e.g., Li‑6 vs Li‑7 neural coherence, or T7 protocol gamma increase) with
    preregistration, independent data collection, and a pre-agreed criterion for “framework
       update required.” — Metric: Completion of one such study to analysis, with either
       confirmatory or disconfirmatory results accepted into the INDEXER as a new epistemic
       node. — Horizon: 2–4 quarters.[1]


Optional artifact (check-form riddle)

“When a framework claims only verification, yet markets protocols as if validation were
imminent, which layer is out of phase: the math, the code, or the governance? The phase mirror
answer is: treat every phenomenological promise as a non-binary test case—defined only by
the collapse condition you can actually preregister.”

⁂



    1.​ Technical-specs-SCPN_FRAMEWORK_MONOGRAPH_2026.pdf
