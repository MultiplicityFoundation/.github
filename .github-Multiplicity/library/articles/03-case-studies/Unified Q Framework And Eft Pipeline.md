---
slug: unified-q-framework-and-eft-pipeline
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Unified Q Framework And Eft Pipeline.md
  last_synced: '2026-03-20T17:17:21.515572Z'
---

Unified Q_{μν} Framework & EFT Pipeline
This document compiles the core structures, decisions, and rules we solidified in the conversation. It is the
base spec for the G-Theory / EFT quantum-corrections program.




0. Meta: Epistemic Rules
All work obeys these rules:


      • No bullshit: if something is not derived or computed, it is labeled UNPROVEN.
      • EFT first: prefer standard effective field theory (EFT) and semiclassical gravity over numerology or
        speculative structures.
      • Explicit decomposition: always separate
      • well-defined geometric corrections,
      • semiclassical field corrections,
      • speculative add-ons.
      • Scaling sanity check: before chasing observables, apply dimensional / curvature scaling. If
        suppression is ~(MPl /M )4 for astrophysical scales, it is observationally dead.
      • Speculation quarantine: speculative constructs (primes, exotic entropy functionals, etc.) live in an
        explicit Speculative Archive and never share the same status as EFT pieces.




1. Master EFT Action and Parameters
We fix the gravitational sector to a minimal, physically motivated quadratic gravity EFT:

                                            2
                                          MPl       1         1
                                Lgrav =       [−R+    2 R2 −      Cμνρσ C μνρσ ]
                                           2       6m0       2m22

      • m0 : mass of the scalar (spin-0) mode from the R2 term.
      • m2 : mass of the massive spin-2 mode from the C 2 term.

Relations to traditional couplings (schematically):

             2
      • α ∼ MPl /(12m20 ) for R2 ,
              2
      • β ∼ −MPl /(4m22 ) for C 2 .

Convention: work in Planck units where convenient: MPl = 1, G = 1/(8π), c = ℏ = 1.


The total effective action is


                 Seff = ∫ d4 x −g [Lgrav + Lmatter ] + Sboundary + Storsion + Sspeculative .




                                                        1
2. Canonical Q_{μν} Template
All gravitational equations are written as:

                                                            classical
                                    Gμν + Λgμν + Qμν = 8πG Tμν        .

We always decompose:


                                       Qμν = Qgeom
                                              μν   + Qfield spec
                                                      μν + Qμν .


2.1 Geometric EFT correction Q^{geom}_{μν}

Defined by variation of higher-curvature terms only:


                                  2   δ                M2      M2
                    Qgeom
                     μν   ≡−               ∫ d4 x −g [ Pl2 R2 − Pl2 Cαβγδ C αβγδ ].
                                  −g δg μν            12m0     4m2

      • This is the EFT geometric correction sector.
      • In conformally flat backgrounds (like FLRW), the C 2 term vanishes, so only R2 contributes.

2.2 Field / semiclassical correction Q^{field}_{μν}

Includes expectation values and anomaly-type terms:


                             Qfield     ^           (ϕ)   anomaly
                              μν ≡ 8πG(⟨Tμν ⟩ren + Tμν + Tμν      + … ).

Examples: - Renormalized stress-energy of quantum fields on curved backgrounds. - Effective scalaron
stress tensor in Einstein frame (if desired). - Conformal anomaly stress tensor for conformal fields.


2.3 Speculative sector Q^{spec}_{μν}

Reserve this for constructs not directly derived from EFT/QFT:


     Qspec
      μν ≡ [Speculative terms: prime-weighted curvature, ad-hoc entropy functionals, etc.]

Rules: - Must be explicitly identified as UNPROVEN. - Must not be mixed into predictions without clear
labeling. - Many such constructs (e.g., PWG for BHs) are now known to be phenomenologically inert.


2.4 Epistemic status

      • Qgeom
         μν : Established EFT (up to choice of m0 , m2 ).
      • Qfield
         μν : Established semiclassical QFT (given a field content and state).
      • Qspec
         μν : Speculative; must be quarantined.




                                                       2
3. Cosmology: Q^{geom}_{μν} in FLRW
We implemented the first concrete, executable piece: Q^{geom}_{μν} in flat FLRW.


3.1 Setup

Metric:


                                      ds2 = −dt2 + a(t)2 δij dxi dxj .

Hubble parameter:

                                                           ȧ
                                                 H(t) =       .
                                                           a

We focus on f (R) = R + αR2 with

                                                1
                                         α=               (MPl = 1).
                                              12m20

3.2 Explicit FLRW formulas for Q^{geom}

For the R+R² model in FLRW (C² term vanishes):


     • 00-component:


                                     Qgeom
                                      00   = 18α(6H 2 Ḣ − Ḣ 2 + 2H Ḧ ).

     • Spatial components:


                                              Qgeom
                                               ij   = a2 δij Qspatial ,
                                              ...
                               Qspatial = 6α(2H + 12H Ḧ + 9Ḣ 2 + 18H 2 Ḣ ).

These formulas define the geometric quantum corrections in cosmology.


3.3 Modified Friedmann equation

With these corrections, the modified Friedmann equation (as implemented) is:


                                   3H 2 + Λ = 8πG ρm + Qgeom
                                                        00   + Qfield
                                                                00 .

In code, we currently focus on the geometric piece and set Qfield
                                                            00 = 0 by default.


We expose a diagnostic function:




                                                      3
                       residual(H, Ḣ , Ḧ ; ρm , Λ) = 3H 2 + Λ − 8πGρm − Qgeom
                                                                           00 .

Interpretation: - If residual = 0, the given (H, ρm , Λ) satisfy the modified Friedmann equation. - For a GR-
consistent background without Q (i.e. 3H 2 + Λ = 8πGρm ), the residual reduces to −Q00 , so its
magnitude directly measures how much Q shifts the dynamics.


We explicitly do not claim to solve for H(t) yet; we only evaluate Q on given backgrounds.


3.4 The CosmologicalQ Python class (concept)

Core features (implemented in cosmology_q_calculator.py ):


     • Constructor:
     • Inputs: m0 , m2 (in Planck units).
     • Sets α = 1/(12m20 ), β = −1/(4m22 ).
     • Methods:
     • Q_geom_00(H, Hdot, Hddot) – implements the exact formula above.
     • friedmann_residual(H, Hdot, Hddot, rho_m, Lambda) – returns 3H 2 + Λ − 8πGρm −
       Q00 .
     • evaluate_on_toy_background(t_max, power) – evaluates Q00 on a simple power-law
       background a(t) = tp . Explicit warning: this does not solve the modified equations.
     • plot_toy_background(...) – visualizes Q on this toy background with a disclaimer.
     • starobinsky_inflation_predictions(N) – returns the standard (ns , r) pair for Starobinsky
       inflation as a hard-coded benchmark (currently not derived from m0 inside the code; clearly labeled
       as such).

3.5 Scaling results from the calculator

With realistic parameters:


     • Starobinsky-like inflation: m0 ∼ 1.3 × 10−6 MPl , Hinf ∼ 10−5 MPl , ϵ ∼ 10−3 :
                      geom
     • Numerically, Q00      /(3H 2 ) ∼ −0.18.

     • Interpretation: the R² term is an O(1) contribution — it drives inflation, not a small correction.


     • Late-time universe: H0 ∼ 2.2 × 10−61 MPl :


     • With the same m0 , we find

                                                 ∣Qgeom
                                                   00 (t0 )∣
                                                             ∼ 10−110 .
                                                    3H02

     • Interpretation: R² corrections are utterly negligible at late times.

This matches the expected EFT picture: - At high curvature (inflation scale), higher-curvature terms can
dominate. - At extremely low curvature (today), they effectively turn off.




                                                        4
4. Black Holes: Curvature Scaling Barrier & EFT-Only Pipeline

4.1 Curvature scaling barrier for Planck-triggered effects

For a Schwarzschild black hole of mass M in Planck units:


     • Horizon radius: rs = 2M .
     • Kretschmann scalar:

                                             48M 2                          3
                                    K(r) =         ,       Ks ≡ K(rs ) =        .
                                               r6                          4M 4
     • Thus the ratio to Planck curvature (KPl ∼ 1) is
                                                                  4
                                                    ∼(     ) .
                                                Ks     MPl
                                                KPl    M

For astrophysical black holes (M ≫ MPl ), this is insanely small: - Stellar BH (M ∼ 1038 MPl ): Ks /KPl ∼
10−152 . - Supermassive BH (M ∼ 1047 MPl ): Ks /KPl ∼ 10−188 .

Key conclusion: any modification that “turns on” at K ∼ KPl is suppressed by (MPl /M )4 in BH exteriors
and is unobservable for astrophysical BHs.


4.2 Death certificate for prime-weighted gravity (PWG) in BHs

Prime-weighted curvature models (PWG) introduced a factor

                                                                       1
                                F (K) = ∑ p−2 ,            P (K) = ⌊     ⌋.
                                          p≤P (K)
                                                                       K

In BH exteriors with K ≪ 1, P (K) ≫ 1 and the sum rapidly saturates:


                                    F (K) → F0 ≈ ζprimes (2) ≈ 0.45.

So for astrophysical BHs: - PWG reduces to a constant factor times a K term. - The only relevant scaling is
K ∼ 1/M 4 . - The relative metric corrections at the photon sphere scale as

                                        δA               1
                                           ∼ λK ∼ O(1) × 4 .
                                         A              M

This yields: - ΔRshadow /Rshadow ∼ (MPl /M )4 — ∼ 10−152 for stellar BHs, ∼ 10−188 for SMBHs. - Δω/ω
for QNMs with the same suppression.


Given EHT and LVK sensitivities (~10% at best), PWG-induced deviations are smaller by 150+ orders of
magnitude.


Verdict: - PWG in a Planck-triggered implementation is phenomenologically inert for BHs. - Any attempt
to make it observable requires introducing new, fine-tuned curvature scales K∗ ≪ KPl , which destroys the




                                                       5
original motivation and demotes PWG to a generic, unprincipled deformation. - For BH phenomenology,
PWG is declared dead and archived as a Planck-scale / early-universe curiosity only.


4.3 EFT-only BH pipeline

For BHs, we stick to the EFT action with (m0 , m2 ) and build an observable pipeline:


    1. Metric ansatz:

                                       ds2 = −A(r)dt2 + B(r)−1 dr2 + r2 dΩ2 ,

                                      A(r) = AGR (r)[1 + ϵ0 a0 (x) + ϵ2 a2 (x)],

                                      B(r) = AGR (r)[1 + ϵ0 b0 (x) + ϵ2 b2 (x)],

       where:
    2. AGR = 1 − 2M /r , x = r/rs , rs = 2M .
    3. ϵi = 1/(mi rs )2 .

    4. a0 , a2 , b0 , b2 are dimensionless deformation profiles from solving quadratic gravity's field equations.


    5. Photon sphere and shadow:


    6. Photon sphere rph from A′ (r)/A(r) = 2/r .
    7. Shadow radius Rsh = rph /       A(rph ).
                                           (0)
    8. Linearized deviations: ΔRsh /Rsh = κ0 (M )ϵ0 + κ2 (M )ϵ2 .


    9. QNMs (eikonal):


   10. Orbital frequency: Ωph =                2 .
                                      A(rph )/rph
   11. Lyapunov exponent: λL from second derivative of A/r 2 in tortoise coordinate.
   12. Eikonal QNMs: ωℓn ≈ ℓΩph − i(n + 1/2)λL .

   13. Deviations again linear in ϵ0,2 .


   14. Constraints:


   15. Map EHT and LVK deviations (consistent with 0 at ~10% level) to bounds on ϵ0 , ϵ2 and thus m0 , m2 .
   16. Currently: cosmology + binary pulsars give tighter bounds than BHs, so BHs are primarily cross-
       checks and future targets, not dominant constraints.

The key unification point: the same m0 , m2 used in cosmology are used in BHs. This ties inflationary
physics and BH corrections into a single EFT parameter set.




                                                       6
5. Speculative Archive Rules
We define an explicit Speculative Archive with the following policies:


5.1 Prime-Weighted Gravity (PWG)

     • Status: Retired for BH phenomenology.
     • Reason: curvature scaling yields ∼ (MPl /M )4 suppression; unobservable for astrophysical BHs.
     • Allowed domain: at most early-universe / Planck-scale toy models.
     • Usage: may be mentioned as historical development or mathematical curiosity, never as a core
       prediction engine.

5.2 Novel entropy functionals

     • Form: e.g. BH entropy= A/4Gℏ + ∫ (ρ ln ρ + I(ρ)).
     • Risk: can easily violate the Generalized Second Law (GSL) and first law if I(ρ) is not derived from a
       consistent microstate counting.
     • Status: thermodynamically UNPROVEN.
     • Requirement before use:
     • Show explicitly that proposed I(ρ) respects GSL in basic processes (Hawking evaporation, matter
       infall, etc.).
     • Until then, it cannot be treated as physically meaningful.

5.3 General policy

Speculative constructs: - Do not enter the core Qgeom
                                                 μν   or Qfield
                                                          μν equations. - Must be clearly flagged as
Q^{\text{spec}}_{\mu\nu} with explicit status. - Must not be used to claim observational signatures unless
a full consistency and scaling analysis is done.




6. Implementation Roadmap (Concrete)

Phase 1 – Framework template

     • Create Q_framework.tex that:
     • Defines the master action.
     • Defines the Qμν decomposition.
     • Lists parameter definitions and epistemic status.
     • Include this section verbatim at the start of all new documents.

Phase 2 – Cosmology first (done in code, next in papers)

     • cosmology_q_calculator.py implemented with:
     • CosmologicalQ(m0, m2) class.
               geom
     • Exact Q00      and diagnostic methods.
     • Write Q_cosmology.tex that:
     • Presents the FLRW formulas.




                                                      7
     • Shows inflation vs late-time scaling.
     • Documents the calculator usage and outputs.

Phase 3 – BH consistency check

     • Implement BH EFT metric deformation using same m0 , m2 .
     • Build Python tools (analogous to the cosmology calculator) to:
     • Take metric functions A(r), B(r) as input.
     • Compute photon sphere, shadow radius, and eikonal QNMs.
     • Show explicitly that for realistic m0 , m2 consistent with cosmology, BH deviations are ≪ 10% and
      consistent with current null results.

Phase 4 – Refactor existing documents

     • Update Starobinsky, ToE, wormhole, and TEGR documents to:
     • Reference the canonical Q-framework.
     • Use the Qgeom /Qfield /Qspec split.
     • Drop or quarantine speculative sectors (e.g., PWG in BHs) according to the archive rules.




7. What This Achieves
     • A coherent, reusable Qμν framework anchored in EFT and semiclassical gravity.
     • A working cosmology calculator that:
     • Shows higher-curvature terms drive inflation but die away at late times.
     • Is ready to be extended and reused.
     • A clear verdict on PWG and similar numerological constructs:
     • BH phenomenology: dead by curvature scaling.
     • Allowed only as quarantined speculation in regimes where we genuinely lack better tools.
     • A methodological foundation where every new extension must:
     • Be placed into the Qgeom /Qfield /Qspec taxonomy.
     • Pass scaling and consistency checks before being used for predictions.

This is the baseline spec going forward: no new work should bypass or contradict this structure without an
explicit, justified revision.




                                                     8
