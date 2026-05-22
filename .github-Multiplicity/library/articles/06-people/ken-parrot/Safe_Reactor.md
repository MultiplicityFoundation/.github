---
slug: safe-reactor
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/ken-parrot/Safe_Reactor.md
  last_synced: '2026-03-20T17:17:14.106021Z'
---

                              Safe Reactor
                                 Ken Parrott
                               September 2025


1     Introduction
[12pt]article amsmath,amssymb,geometry,graphicx,xcolor,enumitem,booktabs mar-
gin=1in TriPrime Monumental-Safety Fission Reactor (TP-MSR)
A Prime-Gated, Multi-Barrier, Lightning-Immune Architecture Kenneth Par-
rott


Executive Summary
Mission: Define a fission power system whose safety is “monumental” by con-
struction: (a) inherent low pressure, passively cooled core and drain-down geom-
etry; (b) engineered multi-barriers with inerting and tube-in-tube plumbing; (c)
prime-gated digital control and sensing (TriPrime Physics); (d) lightning/EMI
immunity via Lightning Damping Towers (LDTs), coax down-conductors and
spectral snubbing; (e) hydrogen-hazard elimination by avoiding water in con-
tainment; (f) graceful failure with verified decay-heat removal by natural forces.


2     Core Platform (Safety-First Selection)
Primary choice: Fluoride molten-salt reactor (thermalized) with low-pressure
liquid fuel salt in a graphite-moderated core.
Rationale:
      [nosep]
    • Low pressure ⇒ eliminates large-break loss-of-coolant blowdown hazards.

    • Freeze-plug (gravity-drain to subcritical dump tanks) provides passive,
      operator-independent shutdown on overtemperature or loss of power.
    • Strong negative temperature/void coefficients ⇒ self-stabilizing reactivity.
    • No water in containment ⇒ no zirconium-steam reaction and hydrogen
      deflagration pathway.



                                        1
Secondary cycle: sCO2 Brayton or closed helium (dry, non-hydrogenating),
with helical/spiral compact heat exchangers for high heat transfer and structural
buckling resistance.


3     Monumental Safety Stack (TriPrime Layers)
3.1    Layer A: Passive Geometry & Decay-Heat Removal
      [nosep]

    • Gravity drain through a freeze plug to subcritical, finned, air-cooled
      dump tanks; decay heat rejected to ambient via natural circulation.
    • Natural convection paths in core vessel and guard tank; no forced flow
      required for post-scram cooling.
    • Helical/spiral stiffeners on vessels and exchangers to raise buckling
      loads and add crush stroke under extreme events (seismic/impact).

3.2    Layer B: Multi-Barrier & Inerting
      [nosep]

    • Vessel-in-vessel with a guard tank and inert cover gas (N2 /Ar); annulus
      instrumented for leak-before-break detection.

    • Tube-in-tube salt lines and secondary piping: inner working tube, outer
      containment annulus pre-charged with N2 /CO2 for instant oxygen dilution
      and spray cooling at any breach.
    • Compartment inerting: zoned CO2 /N2 flooding sized to push local O2
      below limiting oxygen concentration (LOC ∼10–12%) in < 1 s.

3.3    Layer C: Hydrogen Pathway Elimination
      [nosep]

    • No liquid water inside primary containment; steam only in isolated tertiary
      systems if used.

    • sCO2 /He cycle removes H2 production mechanisms tied to high-temperature
      steam reactions.




                                        2
3.4    Layer D: TriPrime Control & Sensing (Prime-Gated
       Lawfulness)
Idea: Sample, estimate, and act on the plant state through prime-windowed
timing and triadic sensor fusion to avoid modal aliasing and resonance pile-ups.
Triad of sensors: (i) thermal (fiber-optic, distributed), (ii) acoustic/strain
(vessel, HX), (iii) electromagnetic/chem (salt properties).
Prime-window sampling: telemetry and control loops run with prime-separated
cadences (e.g., 97–101 ms, 283 ms) to decorrelate spurious harmonics.
Lawfulness score L(t) from triad features (normalized):

                    L = w1 ∆Tspatial + w2 ∆Zsalt + w3 Svib .

Ethical/sovereignty gate Θ (CSL) interlocks any control action with hard-coded
safe envelopes; non-commuting commands are nulled.
Outcome: Reduced control-induced oscillations, auditable actuator decisions,
and earlier anomaly detection.

3.5    Layer E: Lightning/EMI Damping
      [nosep]

    • Lightning Damping Towers (LDTs): Faraday capture cage → coax
      (tube-in-tube) down-conductors → staged surge protective devices (SPDs)
      + distributed RC/CLC snubbers.
    • Spectral shaping: lower L dI/dt and notch filters away from plant nat-
      ural modes; target radiated/conducted EMI reduction 10–20 dB.
    • Meshed ground with low step/touch potentials; I&C racks inside RF-
      tight enclosures with fiber isolation.

3.6    Layer F: Seismic & External Hazards
      [nosep]

    • Base isolation for the reactor building; helical/corrugated shells on key
      components increase buckling margins.
    • Flood/Fire: elevated air intakes; compartment CO2 inerting doubles as
      early fire suppression; filtered vent with passive isolation.


4     Thermal-Hydraulic Enhancements
4.1    Helical Heat-Exchange Geometry
      [nosep]


                                       3
    • Dean-vortex enhancement increases Nusselt number; more uniform wall
      temperatures ⇒ lower thermal fatigue.
    • Spiral baffles distribute flow to prevent maldistribution and local film boil-
      ing.

4.2    Salt-to-sCO2 /He Interface
      [nosep]

    • Compact printed or spiral HX modules; tube-in-tube manifolds limit leak
      impact with inert-shroud response.
    • Dry secondary avoids exothermic metal-water reactions.


5     Risk Targets & Safety Case
      [nosep]

    • Core damage frequency (CDF): design target ≤ 10−7 /reactor-yr (drain-
      down geometry + passive cooling).
    • Large early release frequency (LERF): minimized by low pressure,
      multi-barrier, dry containment, filtered vent.
    • Beyond design basis: station blackout ⇒ freeze-plug melts ⇒ gravity
      drain; natural convection air-cooling of dump tanks provides indefinite
      heat removal.


6     Verification & Validation (No-Blueprint Level)
Analysis
      [nosep]

    • Coupled neutronic/thermal CFD for negative reactivity feedback and drain
      kinetics.
    • Probabilistic risk assessment (PRA) including external events (lightning,
      EMI, seismic, flood, fire).




                                         4
Component Testing
      [nosep]

    • Freeze-plug actuation reliability across transients; dump-tank heat rejec-
      tion with natural convection/air.
    • Tube-in-tube breach rigs: inert-shroud oxygen decay to LOC < 12% in
      ≤ 1 s; re-flash suppression.
    • Lightning coupons: 10/350 µs impulses & EMI mapping; SPD/snubber
      clamp levels.

Integrated Demonstrations
      [nosep]

    • Non-nuclear full-heat prototype loop (electric heaters) to validate decay-
      heat removal and HX performance.
    • I&C prime-window timing & CSL gate HIL (hardware-in-loop) to demon-
      strate stability and auditability.


7     TriPrime Physics: Control Lawfulness & Sta-
      bility
In operator form, the plant state update uses a prime-gated projector Πlawful
and an ethical gate Θ:
                                                    
                       Xt+1 = Θ(E, Σ) Πlawful Ξ(t) Xt ,

where Ξ(t) is the recursive controller; Θ rejects non-commuting (unsafe) actions;
Πlawful filters resonant/aliasing modes via prime-timed sampling. Boundedness
is enforced by a multiplicity regulator Λm that limits operator norms (prevents
control blow-up).


8     Lightning/EMI: Design Aims (Quantitative Tar-
      gets)
      [nosep]

    • Entry overvoltage reduction: 40–70% vs. bare down-conductors.
    • Radiated/conducted EMI reduction: 10–20 dB across plant-relevant bands.
    • Ground potential rise shaping: meshed grounds constrain step/touch po-
      tentials below occupational limits.


                                       5
9     Human Factors & Ethics
      [nosep]

    • CSL (Conscious Sovereignty Layer): hard interlocks aligned with
      conservative operating envelopes; explainable-control logs.
    • Cognitive load: alarm prime-windowing and triadic dashboards (ther-
      mal/chem/structural) reduce operator overload and promote earlier, clearer
      decisions.


10     Siting & Containment Philosophy
      [nosep]

    • Below-grade reactor cavity with guard tank; dry, inert primary contain-
      ment; filtered confinement for the building.
    • Modular dump-tank gallery with natural-draft chimneys sized for indefi-
      nite decay-heat removal without power.


Conclusion
The TP-MSR marries inherent molten-salt advantages (low pressure, strong
negative feedback, passive drain) with engineered multi-barriers, inerting, tube-
in-tube plumbing, helical structures, and TriPrime prime-gated controls. Light-
ning/EMI damping hardens I&C against extreme events. The result is a fission
architecture designed to be stable by physics, safe by geometry, auditable by
control, and resilient to external hazards.


Notes
This document outlines safety concepts and verification pathways at a systems
level; it intentionally omits construction blueprints or sensitive specifications.




                                        6
