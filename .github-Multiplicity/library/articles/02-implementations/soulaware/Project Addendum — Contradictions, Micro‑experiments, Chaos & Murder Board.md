---
slug: project-addendum-contradictions-micro-experiments-chaos-murder-board
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "02-implementations/soulaware/Project Addendum \u2014 Contradictions, Micro\u2011\
    experiments, Chaos & Murder Board.md"
  last_synced: '2026-03-20T17:17:15.705777Z'
---

Project Addendum — Contradictions,
Micro‑Experiments, Chaos & Murder Board
Purpose: Fold the latest critique into operational practice. Minimal fluff, maximum leverage.




Legend (marking system)
     • Pink = authorial voice (keep as-is).
     • △ Contradiction/Tension = flag with a red triangle and (if highlighting) use #E11D48. Only use for
       genuine aporias you expect to generate insight (not mere confusion).
     • ⚙ Micro‑experiment = 5–10 min test idea (highlight #0EA5E9 or add ⚙ prefix).
     • ☢ Murder‑board items = candidates for pruning/abandonment (highlight #F59E0B).
     • ★ Wild‑card page = chaos spread every 20 pages (free form, no constraints).




A. Contradictions/Tensions Register (△)
Why: Contradictions are generative; track them explicitly and tie each to a test.


Template row fields: - ID · Domain · Pair · Claim A · Claim B · Operational test · Metric(s) · Decision rule ·
Owner · Status


Seed entries: 1. C‑001 · Agency · Barad vs Schneider · Agency is intra‑action, not attribute · Agency implies
discrete agents with commitments · Have actors swap agency framings mid‑scene; measure D/BTI shift and
audience clarity ratings · D↓ + BTI↓ with intra‑action framing or opposite · Rule: keep the framing that
yields ΔD<0 and ↑clarity ≥0.3 SD · Owner: Dir · Status: Planned. 2. C‑002 · Liveness · Live presence vs
Mediation · Co‑presence essential · Mediation intensifies agency via framing · Run A/B: live delivery vs in‑ear
mediated cues; compare ΔD and post‑scene recall · D↓ with mediation and recall↑ → keep mediation as
tool · Owner: SM · Status: In prep. 3. C‑003 · Model · Residual vs Intra‑subspace conflict · D outside Π
captures dissonance · Core dissonance can live within Π · Track BTI alongside D; contradictions should raise BTI
even if D stable · If BTI↑ during known cognitive conflicts while D≈const → elevate BTI to co‑primary
metric · Owner: ML · Status: Running.


       Rule of use: every △ must carry a proposed Operational test; kill any △ without a test after
       30 days.




B. Micro‑Experiments Ledger (⚙)
Why: Convert hunches into 5–10 min etudes; accumulate artistic data.




                                                       1
Card template (copy/paste per item): - ⚙ Title: - Hypothesis (1 line): - Setup (≤5 min): - Observable:
(what changes on stage/in room) - Expected signal: (D↓ / BTI↓ / audience metric, etc.) - Go/No‑Go rule:
(pre‑declared) - Result: (win/lose/ambiguous) - Next: (iterate/retire)


Seed cards: 1) Retrograde speech blocking — actors speak while moving backward.
Hypothesis: retrograde motion surfaces embodied contradiction; BTI↑ transiently then D↓ after repair
cue.
Setup: 2 actors, 8 lines, add one repair prompt.
Go/No‑Go: BTI spike followed by ≥10% D drop within 2 prompts.


2) Chronotope pillow scene — re‑time markers within the scene.
Hypothesis: explicit time‑code anchors reduce confusion component (D↓) without suppressing productive
tension (BTI stable).
Go/No‑Go: ΔD ≤ −15% with |ΔBTI| < 5%.


3) Parts‑dialogue vs mindfulness (N=1).
Hypothesis: guided parts‑dialogue accelerates D decay vs same‑length mindfulness.
Go/No‑Go: ΔD_slope(parts) < ΔD_slope(mindfulness) by ≥20%.


      Discipline: Only keep micro‑experiments with a logged Result within 7 days; otherwise retire.




C. Wild‑Card Pages (★)
Cadence: 1 chaos page every 20 pages.
Allowed: mind‑map, doodles, dialogue between theorists, fake playbill, poem, score, stage diagram—
anything.
Purpose: force non‑linear recombination; harvest at least one △ or ⚙ from each chaos page within 48
hours.




D. Periodic Murder‑Board (☢)
Cadence: every 6–8 weeks.
Prompts: - What have I abandoned—and why?
- Which theorists/methods are not earning their keep?
- What survives only because it was highlighted six months ago?
- Which metrics are Goodhart magnets?
Outputs: a Kill list (to archive), a Keep list (with reason), and ≤3 Pivots (actionable changes to Π/Ξ/
protocols).




E. Where we are (short read)
     • Solid: phenomenology, therapeutic stance, IFS/hypnosis synthesis.




                                                    2
      • UNPROVEN: Hilbert‑space residual as the essence of dissonance; EEG linkage beyond correlation;
        any privileged “prime” framing.
      • Risk posture: treat Π as reference frame, not truth; attach external outcomes to all D/BTI claims.




F. Next useful steps (targeted)
     1. 3–4 page paper: convert “Ode × Multiplicity” executive summary → clean preprint (no metaphysics;
        rename to reference subspace / dictionary atoms).
        Expect: 95% rejection; the 5% signal is the goal.
     2. Single simplest prediction: N=1/Small‑N test—parts‑dialogue should produce faster D decay than
        matched‑length mindfulness. Produce one clear graph.
     3. Outreach: send to hand‑picked researchers (complexity‑friendly clinicians, hypnosis labs, small EEG
        outfits). Keep a contact log and publish nulls.
     4. Open‑source binder (cleaned): notebook, schema, consent template, prereg, risk register, A/
        B+transfer protocol, one end‑to‑end run with hashes.
     5. Governance: keep κ=0 opt‑out live; log subspace drift and descent‑violations; stop on ΔY<0 with
        ΔD<0.




G. Logging extensions (to match the new practice)
Add the following fields to your run logs (JSONLines recommended for per‑session granularity): -
 contradictions : list of {id, domain, claim_A, claim_B, test, decision_rule, status}. -
micro_experiments : list of {id, title, hypothesis, setup, observable, expected_signal, rule, result, next}. -
wildcard_pages : list of {index, harvested_items:[ids]}. - murder_board : {date, kills:[ids], keeps:[ids],
pivots:["change Π basis", "tighten Ξ bounds", ...]}.




H. Artifacts and anchors
      • Protocol + risk register: see companion canvas doc.
      • Notebook & schema: /mnt/data/dissonance_pipeline.ipynb , run_log_schema.json (also
        linked in chat).
      • Source Ode: /mnt/data/Ode to Cognitive Dissonance.docx .




I. Quick checklists
Contradictions pass: △ present → test defined → metric set → decision rule logged → owner assigned →
status updated.


Micro‑experiment pass: hypothesis → setup ≤10 min → observable → expected signal → go/no‑go →
result in 7 days → keep/retire.




                                                       3
Wild‑card harvest: create ★ → extract ≥1 △ or ⚙ within 48 h → log.


Murder‑board: run ☢ → produce kill/keep/pivot → update protocols/log schema → archive killed material.


— End addendum —




                                                  4
