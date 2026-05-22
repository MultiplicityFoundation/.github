---
slug: one-loop-health-education-curriculum-outline-v0
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "04-domains/education/One-loop Health\u2013education Curriculum Outline (v0.md"
  last_synced: '2026-03-20T17:17:19.859734Z'
---

One-Loop Health–Education Curriculum Outline
(v0.1)
0) Purpose and Scope
Design a dual-skin health education program that runs on the One-Loop architecture. Patient-facing and
student-facing experiences share modules, telemetry, and governance. Focus areas: sleep, stress, metabolic
health, systems thinking, and health literacy. Integrates with clinical protocols and preserves privacy and
equity.


1) System Map (Curriculum ↔ One-Loop)
     • Context layer: Hologram Health provides consent-scoped Visit Packs; Spectra renders safety checks
       and rationale.
     • Data/AI plane: Intrinsica ingests signals (wearables, EHR, surveys), generates risk vectors, and
       drives personalization.
     • Learning layer: HEP/ULMS delivers XR micromodules, captures attempts and outcomes, and
       exposes privacy-safe telemetry for control and audit.
     • Clinical layer: S2H micro-brands (e.g., Youth Fountain, VaricardStar, BodyArt, Diet/Skin) align
       education with care plans.
     • Governance: Consent, de-ID, equity dashboards, and audit.


2) Audiences and Tracks
     • K–12: Middle and high school emphasis (grades 8–12). Dual-skin delivery inside school day and after-
       school wellness.
     • Postsecondary & Workforce: Allied health, public health, educators-in-training.
     • Community & Family: Caregivers, adult learners, community health workers.
     • Clinicians & Staff: Patient education and protocol-aligned microlearning.


3) Learning Outcomes (Program)
Graduates can: 1. Apply sleep, stress, and metabolism habits to improve daily functioning and adherence. 2.
Interpret basic biometrics (HRV, sleep efficiency, activity) to guide self-care. 3. Use systems thinking to plan
habit change and troubleshoot barriers. 4. Demonstrate health literacy: evidence appraisal, uncertainty
management, consent and privacy basics. 5. Collaborate with care teams; document actions and reflections
in a Portable Education Record.


4) Module Families (Dual Skin)
       Each module exists in Student Mode (pedagogy-first) and Patient Mode (adherence-first).
       IDs are shared.




                                                       1
A. Sleep–Stress–Metabolism (SSM)

    • sleep-101: Breath pacing, stimulus control, sleep window setting.
    • stress-201: Box breathing, cognitive reframe, micro-break planning.
    • metabolism-101: Meal timing, movement snacks, hydration scaffolds.

B. Quantum Literacy Lite (QLL)

    • Copy-vs-no-clone puzzles, chance boxes, and error-budget framing to build scientific reasoning and
      uncertainty handling.

C. Systems Health (SH)

    • Routine braids/swaps, random-walk recovery plans, and dependency mapping for chronic-condition
      management.

D. S2H-aligned Micro-Brand Packs (XR MaaS)

    • Youth Fountain: Adolescent sleep, mood, movement, digital boundaries.
    • VaricardStar: Cardiometabolic self-checks, home BP prep, HRV reflections.
    • BodyArt: Form-aware rehab flows; range-of-motion and fatigue self-tracking.
    • Diet/Skin: Anti-inflammatory nutrition routines; symptom journaling.


5) Module Template (applies to all)
    • ID & Mode: e.g., xr.sleep.101 | Student/Patient.
    • Duration: 6–12 minutes XR micromodule; 2–4 per week.
    • Preconditions: TCI ≥ threshold; CSL state “clear.”
    • Objectives: 2–3 measurable behaviors or understandings.
    • Content blocks: Short concept vignette; 1–2 guided practices; action plan.
    • Practice: 1–3 micro-habits, adjustable by risk vector and EchoBraid pacing (when needed).
    • Evidence (MLEM): Quiz items, reflection prompt, optional provider acknowledgement, behavioral
      telemetry.
    • Transfer task: Apply skill in new context within 7–14 days.
    • Safety: Explain-first flags; medication/condition contraindication checks (patient mode).


6) Assessment and Telemetry
    • PER: Portfolio of assigned modules, attempts, outcomes, reflections.
    • MLEM: Evidence map ties objectives to scoring rules.
    • TCI: Concept–need alignment index; gates launches and logs.
    • CSLState: Gate for clarity, sovereignty, lawfulness; blocks when load or policy risk is high.
    • KPIs (program):
    • Engagement rate (active share over eligible cohort).
    • Risk-delta in targeted dimension per module window.
    • Adherence rate (completed/prescribed modules).
    • Equity gap reduction across approved cohorts.
    • Privacy pass-rate.




                                                      2
7) Inclusion & Neurodiversity
    • EchoBraid accommodations: Pacing envelopes, call‑and‑response intervals, predictable transitions;
      enable for ASD-flagged cohorts at S2. Targets: reduced TCI variance, higher completion, no increase
      in aborts.
    • Accessibility: Low-bandwidth, offline bundles; multi-language packs.


8) Ethics, Privacy, and Safety
    • Consent-first: Purpose-bound consent; patient holds keys to share slices of context.
    • Data minimization: No PHI at HEP ingress; de-identified telemetry only.
    • Ledgered provenance: Hash-on-write for data, models, and policies; machine-checkable receipts.
    • Quality gates: Privacy pass-rate ≥ target; CSL overload ≤ target; zero Severity-1 incidents.


9) Implementation Plan (90 Days → Scale)

Phase S0 – Foundation (Weeks 0–2)

    • Stand up consent registry, ULMS webhooks, feature store v0 (HRV, sleep efficiency), ledger
      bootstrap.
    • Smoke-test FHIR subscriptions and sovereign sync.

Phase S1 – Live Pilot (Weeks 3–8)

    • Launch sleep-101 , stress-201 , metabolism-101 in dual skin.
    • Enable PER/MLEM/TCI logging; deploy CSL library.
    • Run Teacher PD; cohort size N≈25–60.
    • Ethical Vital Signs dashboard v1 (engagement, CSL hits, reciprocity, privacy).

Phase S2 – Expansion & Evaluation (Weeks 9–13)

    • Enable EchoBraid for neurodiversity.
    • Launch population/equity dashboards; run DPIA.
    • Add biweekly S2H tele‑coaching; sovereignty features (offline sync/CRDT).
    • Final evaluation and scale plan.


10) Weekly Pacing Models
    • Student Mode: 2 XR micromodules + 1 project/practice block + 1 reflection.
    • Patient Mode: 3 shorter adherence blocks + 1 reflection; provider acknowledgment optional.


11) Professional Development
    • 2-hour kickoff: One-Loop basics, privacy and consent, PER/MLEM authoring.
    • 1-hour labs: CSL/TCI operations, EchoBraid setup, equity dashboard use.
    • Monthly case reviews tying module performance to care outcomes.




                                                     3
12) Integrations and Contracts
     • Launch: LTI 1.3; xAPI for attempted/completed/answered.
     • Webhooks: /hooks/attempted , /module-complete , /csl-change .
     • Events: intrinsica.risk.update.v1 , privacy.audit.event.v1 .
     • FHIR: Observation, QuestionnaireResponse, CarePlan, Provenance.


13) Required Resources
     • XR-capable devices or web; low-end Android tablets acceptable.
     • Wearables or smart rings for selected cohorts (pilot scale sufficient).
     • Authoring access for module updates; localization pipeline.


14) Validation Plan
     • Primary endpoints: Engagement ≥ target; adherence +8pp vs baseline; equity gap −0.15.
     • Secondary endpoints: HRV and sleep efficiency deltas; transfer index ≥ 0.60 within 14 days; privacy
       pass-rate ≥ 0.98.
     • Design: Pre/post with matched controls where feasible; DP-safe cohort analytics.
     • UNPROVEN until pilot data confirm effect sizes.


15) Risks and Mitigations
     • Cognitive overload → CSL gating, EchoBraid pacing, micro‑habit caps.
     • Privacy breaches → purpose‑bound consent, de‑ID egress, ledger proofs.
     • Equity gaps → acceptance bands and reciprocity guardrails; auto intensity reduction when energy
       balance deteriorates.
     • Content drift → model/version gating and rollback; periodic audits.


16) Roadmap Hints (6 months)
     • Expand SSM with metabolism-201 and systems-101 .
     • Add culturally responsive content packs.
     • Publish PD toolkit; open API for partner modules with MLEM compliance.



Appendix A — Module Stubs - xr.sleep.101 - Objectives: link sleep to longevity; implement 2 micro-
habits for 7 days. - Evidence: quiz (≥70%), reflection, adherence check. - xr.stress.201 - Objectives:
apply box breathing; identify one cognitive reframe. - Evidence: guided practice completion; reflection;
provider note (patient mode). - xr.metabolism.101 - Objectives: set feeding window; schedule 3
movement snacks/day. - Evidence: adherence tally; reflection; optional glucose proxy from wearable if
available.


Appendix B — CSL/TCI Ops - Default thresholds and cool-downs. - Sovereign holds for policy conflicts; audit
trail fields.




                                                       4
Appendix C — Equity Dashboard Cards - Engagement by cohort; overload rate; reciprocity balance; pass-
rate; small-cell suppression rules.




                                                 5
