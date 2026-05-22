---
slug: two-ness-clinics-the-receipt-test-executable-program-references
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Two-ness Clinics \u2014 The Receipt Test (executable Program\
    \ + References).md"
  last_synced: '2026-03-20T17:17:21.465200Z'
---

Two-ness Clinics — The Receipt Test
Tagline: Can you tell them apart later? Only if you kept the receipt.


This document compiles the finalized, executable synthesis of the Two-ness Clinics into a single program
that works across:


       • Tier 0: museum / public pop-up (7–10 minutes)
       • Tier 1: classroom / undergrad lab (60–120 minutes)
       • Tier 2: research-grade experiments and papers

It also includes print-ready docent + visitor artifacts (Appendices) and a curated external reference list.




1) Core thesis (operational, falsifiable)
Two-ness is not a substance. It is the invertibility class of a description under a chosen individuation
basis.


Operationally:


       • “Two-ness disappears” iff we apply a many-to-one map (forgetting / aggregation) and we do not
         preserve a sufficient audit channel (receipt/provenance record) that would make the map invertible
         in practice.

Public hook: Receipt kept → reversal possible. Receipt erased → reversal impossible (operationally).




2) Minimal formal frame
Let token states live in a space X . Two labeled tokens live in X 2 . The swap group S2 acts by (x1 , x2 ) ↦
(x2 , x1 ).

2.1 Forgetting maps

       • Label-forgetting (quotient by swaps): $$ q: X^2 \to X^2/S_2. $$
       • Aggregation/coarse-graining: $$ f: X^2/S_2 \to A $$ where A is an aggregate description space
        (mixtures, totals, multisets, etc.).

A description preserves token identity exactly when the overall map is injective on the operational domain.


2.2 Audit channel (“receipt”) makes forgetting reversible

Introduce auxiliary information R (audit/provenance/permutation record) and consider




                                                          1
$$ (x_1,x_2) \mapsto (q(x_1,x_2), R). $$


If R is sufficient, the augmented map can be injective even when q and f are not.


2.3 Information–thermodynamics link (what we do and do not claim)

      • If you erase a record, the minimal dissipation scales with the entropy you actually destroy.
      • If you keep correlations/side information, you can make processes reversible up to the moment you
        later reset/standardize that side memory.

Important nuance for the program:


      • Tier 0 (public): show qualitative energy/erasure effects.
      • Tier 2 (research): only claim near-kT ln 2 saturation with a physical 1-bit memory apparatus
       designed for that regime.




3) Audience tiers (explicit)

Tier 0 — Museum/public (5–10 min)

Goal: felt understanding of basis dependence + the receipt toggle.


      • Primary: Clinic D (basis swap + audit toggle)
      • Optional add-ons: Clinic A-lite (energy vs “erase”), short HOM dip video loop
      • Output: live tally/dashboard + take-home card

Tier 1 — Classroom / undergrad lab (60–120 min)

Goal: operational definitions + measurement + uncertainty.


      • Core: Clinic D as an experiment (real dataset)
      • Anchor physics (choose one):
      • Clinic C (HOM) if optics lab exists
      • Clinic B if you can outsource isotope assay
      • Output: worksheet + analysis template

Tier 2 — Research-grade

Goal: publishable physics claims and extensions.


      • Clinic C (HOM) as the cleanest controllable toggle
      • Clinic A2 (physical 1-bit memory) for Landauer saturation and/or conditional-erasure extensions
      • Optional: formal “audit register” protocols (side information / conditional erasure)




                                                      2
4) The clinics

Clinic D — Basis-swap + cognitive dataset (the engine)
Narrative: “How many things are here?” The answer changes when we change the bookkeeping rules.


Materials:


      • Two distinct tokens (beads/coins) with removable labels
      • Opaque capsule/box
      • Sealed Audit Envelope (receipt card)
      • Optional: tablet or paper tally

Conditions (within-subject; counterbalanced):


     1. Label basis: A/B visible
     2. Type basis: labels hidden; tokens identical
     3. Aggregate basis: tokens placed into opaque capsule; treated as one object
     4. Audit toggle: audit exists vs no audit (after aggregation)

Primary measures:


      • Count judgment category: {“2 tokens”, “1 type (2 tokens)”, “1 object”, other}
      • Confidence (0–10)
      • Optional: response time, 1-sentence explanation

Core predictions:


      • P1: Label basis increases “2 tokens” responses
      • P2: Aggregate basis increases “1 object” responses
      • P3 (key): Audit-present increases reconstructibility judgments without necessarily changing
        perceptual oneness

Pass/fail (Tier 0): observable distribution shift across conditions.




Clinic A — Records → Thermodynamics (two-tier)

A-lite (Tier 0/1): “Erasing the receipt costs something”

Goal: show that irreversible reset has an energetic cost in real devices (qualitative).


      • Measure power draw during “store vs reset” operations on a microcontroller or simple memory
        module.
      • Compare “overwrite/reset” vs “keep/append-only audit log.”

Important: do not claim saturation at kT ln 2 in this tier.




                                                        3
A2 (Tier 2): Research-grade Landauer platform

Goal: measure dissipation near the Landauer bound using an apparatus built for that regime (e.g., physical
double-well memory).


     • Investigate scaling with erased entropy (including permutation-code entropy under stated
       distributions).
     • Optional extension: conditional erasure with side information (audit register).




Clinic B — Forensic isotope melt-merge (material provenance)
Narrative: “Melt two into one—did two-ness vanish? What invariants survive?”


Core idea: compositional invariants (e.g., isotopic ratio) can survive aggregation; token-level trajectories
typically do not, absent a provenance channel.


Tier guidance:


     • Tier 0: describe conceptually (no melting on-site)
     • Tier 1: controlled demo with outsourced assay + strong safety constraints

Safety: do not use legal tender; follow PPE and fume extraction; use approved materials.




Clinic C — Quantum indistinguishability (HOM “receipt toggle”)
Narrative: “Two photons: mark them and interference vanishes; unmark them and it returns.”


Control knob: distinguishability via polarization/path delay/spectral filtering.


Pass/fail: statistically significant visibility change: high when unmarked, low when marked, high again when
unmarked.




5) Falsifiability wall statement (museum-safe)
If a receipt/audit record is preserved, ‘loss of two-ness’ is only apparent and is reconstructible. If the
receipt is erased, reversibility fails operationally.




                                                       4
6) Fastest path to validation (momentum-first)

Immediate (run today)

     • Deploy Clinic D with the docent script + visitor worksheet.
     • Collect N ≈ 100–300 responses at an event.
     • Display a simple live tally dashboard.

Next (anchor physics)

     • Add Clinic C if an optics lab exists (best quantitative toggle).
     • Add Clinic B if you prefer a material-science anchor and can outsource isotope assay.

Research pathway

     • Partner for A2 (physical 1-bit memory) to claim Landauer saturation credibly.




7) Print-ready artifacts (already generated)
These are available as PDFs in the workspace:


     • Docent show card (Letter, 1 page): twoness_docent_show_card_letter.pdf
     • Visitor worksheet (Letter, 2 pages): twoness_visitor_worksheet_letter.pdf
     • Combined packet (Letter, 3 pages): twoness_clinics_packet_letter.pdf




Appendix A — Docent Show Card (1 page)
TWO-NESS CLINICS: The Receipt Test
Core Question: Can you tell them apart later? Only if you kept the receipt. Time: 7 min | Audience:
Museum/Public | Tier: 0


MATERIALS

     • Two distinct tokens (e.g., beads, marked coins)
     • Opaque capsule or small box
     • “Audit Envelope” (sealed card showing Token A → Left, Token B → Right)
     • Tablet/Post-it for live response tally (optional)




                                                           5
SCRIPT & FLOW (☐ = PASS/FAIL CHECK)

0. HOOK (30 sec)

“HOW MANY THINGS ARE HERE? Let’s find out—and watch how the answer changes when we change the
rules for keeping track.”


Show two labeled tokens (A & B). Ask: “How many things?”


1. REMOVE THE RECEIPT (60 sec)

Hide/remove labels so tokens look identical. Ask again.


PASS: ☐ Audience count-judgment shifts (toward “one type/multiplicity”).


2. AGGREGATE (60 sec)

Place both tokens into opaque capsule. Ask again.


PASS: ☐ Majority reports “one object.”


3. THE AUDIT TOGGLE — THE KEY (90 sec)

Hold up sealed Audit Envelope. Ask whether it changes what is or what we can know.


CRITICAL PASS BOX:


      • ☐ With audit: reconstruction judged possible
      • ☐ Without audit: reconstruction judged impossible

4. LINK TO PHYSICS (60 sec)

“Erasing a physical receipt has a minimum energy cost per bit; keeping it in a side-channel avoids paying
that cost until you erase it later.”


Optional: show a 10s HOM dip toggle video.


5. HANDOFF (30 sec)

Invite participants to fill the worksheet / scan QR for live results.




                                                         6
Appendix B — Visitor Lab Worksheet (2 pages)
TWO-NESS CLINICS: Data Sheet
Prompt: Can you tell them apart later? Only if you kept the receipt.


PART 1: COUNT JUDGMENTS

For each scenario, circle ONE response + confidence (0–10).


A — Label basis: [2] [1 type (2 tokens)] [1 object] Other: ____ | Confidence: ____


B — Type basis: [2] [1 type (2 tokens)] [1 object] Other: ____ | Confidence: ____


C — Aggregate basis: [2] [1 type (2 tokens)] [1 object] Other: ____ | Confidence: ____


PART 2: THE AUDIT TOGGLE

Case 1: Audit exists → reconstruct                 which     was    which?    [YES]   [NO]   Why   (1   sentence):
___________________________________________


Case 2: No audit → reconstruct                   which     was     which?    [YES]    [NO]   Why   (1   sentence):
___________________________________________


PART 3: PREDICTION CHECK

     1. If audit is kept, “loss” is: [REAL] [APPARENT]


     2. If audit is erased, “loss” is: [REVERSIBLE] [IRREVERSIBLE] (operationally)


PART 4 (optional): HOM station

Record visibility and pass/fail.




External references (starter bibliography)
(Listed by theme; use DOI where available.)


Information → thermodynamics / Landauer
      • R. Landauer, “Irreversibility and Heat Generation in the Computing Process,” IBM Journal of
        Research and Development 5 (1961), 183–191. doi:10.1147/rd.53.0183




                                                         7
     • C. H. Bennett, “Logical Reversibility of Computation,” IBM Journal of Research and Development 17
       (1973), 525–532. doi:10.1147/RD.176.0525
     • A. Bérut et al., “Experimental verification of Landauer’s principle linking information and
       thermodynamics,” Nature 483 (2012), 187–189. doi:10.1038/nature10872
     • A. Bérut, A. Petrosyan, S. Ciliberto, “Information and thermodynamics: Experimental verification
       of Landauer’s erasure principle,” arXiv:1503.06537 (2015).
     • L. del Rio et al., “The thermodynamic meaning of negative entropy,” Nature 474 (2011), 61–63.
       doi:10.1038/nature10123
     • D. Reeb, M. M. Wolf, “An improved Landauer principle with finite-size corrections,” New Journal of
       Physics 16 (2014), 103011. doi:10.1088/1367-2630/16/10/103011
     • J. Goold et al., “The role of quantum information in thermodynamics — a topical review,” J. Phys.
       A: Math. Theor. 49 (2016), 143001. doi:10.1088/1751-8113/49/14/143001


Quantum indistinguishability / Hong–Ou–Mandel
     • C. K. Hong, Z. Y. Ou, L. Mandel, “Measurement of subpicosecond time intervals between two
      photons by interference,” Physical Review Letters 59 (1987), 2044–2046. doi:10.1103/PhysRevLett.
      59.2044



Citizen Gardens © 2025 CC-NC-ND 4.0




                                                   8
