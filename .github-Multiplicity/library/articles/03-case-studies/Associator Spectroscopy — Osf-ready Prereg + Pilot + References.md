---
slug: associator-spectroscopy-osf-ready-prereg-pilot-references
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Associator Spectroscopy \u2014 Osf-ready Prereg + Pilot +\
    \ References.md"
  last_synced: '2026-03-20T17:17:21.268576Z'
---

Associator Spectroscopy — OSF-Ready
Preregistration
Executive Summary
We propose an experiment to detect and repair closure defects in coarse-grained models by treating
non‑associativity of the macro merge operator as a measurable signal. Using droplet coalescence as the
canonical testbed, we run a two‑path “associator spectroscopy” protocol—(AB)C vs. A(BC)—and
quantify gaps at the level of means and distributions. When gaps persist for a macro variable (e.g., N ,
droplet count), we fit the minimal augmentation C that restores associativity for Ψ = (N , C). We
pre‑register success/failure    criteria,   a   leak‑free     model‑selection          pipeline,    and   an
information‑bottleneck objective that operationalizes minimality.




Hypothesis
For coalescence-like systems, the macro variable N (droplet count) is not closed: the induced binary
operation x ⊕ y on x = N is non‑associative. There exists a low‑dimensional augmentation C such that
Ψ = (N , C) yields an approximately associative ⊕ within pre‑registered tolerances.



System
     • Emulsion droplets generated on chip; merges via Brownian contact.
     • Optional surfactant to modulate interaction strength (suppression factor α ∈ [0, 1]).
     • Time‑windowed stages implemented in identical, isolated microchannels to avoid environmental
       carryover between the left/right parenthesizations.




Macro Variables
     • Primary: N (droplet count).
     • Candidate augmentation **C ** (1–6 scalars): second/third moments (M2 = ∑ m2i , M3 ),
      polydispersity index (PDI), and quantiles (q.25 , q.5 , q.75 ). Total mass M1 = ∑ mi is monitored
      (conserved) and used for the physical null.




Triplet “Associator Spectroscopy” Protocol
    1. Triplets: Prepare matched samples (A, B, C) with equal total mass and closely matched size
      distributions.




                                                      1
    2. Paths: Run two parenthesizations for equal time windows:
    3. Left: (AB)C = merge A with B , then with C .
    4. Right: A(BC) = merge B with C , then with A.
    5. Outcomes:
    6. Mean gap: AE = E[X](AB)C − E[X]A(BC) , for X ∈ {N , Ψ}.
    7. Distributional gap: AD = W1 (ν(AB)C , νA(BC) ) (Wasserstein‑1).
    8. Controls: 4 heterogeneity levels (mono→poly) × 3 surfactant levels.




Matching Tolerance
Require Wasserstein‑1 distance between droplet‑radius distributions to be small:


     • Accept triplets only if W1 (rA , rB ) < τ and W1 (rA , rC ) < τ .
     • Pilot targets: median‑radius mismatch < 2% and W1 < 0.02× median radius.



       To declare a closure defect for the macro variable **N **, we require that both
                                         ~
       ∣AE (N )∣ > 3σnull and AD (N ) > 3σ null in at least 3 of the 4 heterogeneity levels, after
       familywise error correction (Holm–Bonferroni, **α = 0.01**) across all 4 levels.


Definitions:


     • σnull ****: standard deviation of AE (M1 ) across replicates under the physical null (mass
      conservation).
      ~ ****: standard deviation of A from the synthetic associative pipeline (full histogram as
     •σ null                         D
       state; exact concatenation; same measurement/analysis stack).



                                                                                            ~
Declare closure repaired if both E∣AE (Ψ)∣ ≤ ϵE and EAD (Ψ) ≤ ϵD with ϵE = 2σnull and ϵD = 2σ null
across all conditions.




Power & Replicates
                                ~ and standardized effect size d.
     • Pilot determines σnull , σ null
     • With d ≈ 0.5, two‑sided α = 0.01, power 0.8 → n = 50–70 triplet replicates per condition
       (heterogeneity × surfactant). **Total ≈ **4 × 3 × n triplets.



Stage 1 — Associator Measurement. Collect all triplets; split 60/20/20 into Discovery / Validation /
Holdout.




                                                        2
Stage 2 — Minimal Augmentation Search. For each candidate C :


     • Fit macro law G on the first‑merge outcomes in Discovery. Model class: quadratic polynomials in Ψ;
       escalate only if needed to a small ReLU MLP (≤64 hidden units).
     • Evaluate the pair (C, G) on Validation by in‑silico rolling the triplet protocol and measuring
       AE (Ψ), AD (Ψ).
     • Select the first (C, G) meeting tolerances, prioritizing the Information Bottleneck objective
       (below).

Stage 3 — Final Reporting & Robustness. Freeze (C, G). Report triplet and pentagon (four‑merge)
residuals on Holdout; perform ablations (drop each component of C ).


Information Bottleneck Minimality. Primary objective:


$$ \min_{C,G}\ I(\Sigma;C)\ \ \text{s.t.}\ \ \mathbb{E}|A_E(\Psi)|\le \epsilon_E,\ \mathbb{E}A_D(\Psi)\le
\epsilon_D. $$


     • Implementation note: Use a small MLP encoder with spectral normalization and early stopping;
       estimate I(Σ; C) from the available microstate features (full measured histogram). Secondary
       minimality criteria: smallest ∣C∣; predictive sufficiency (next‑step macro ⫫ micro ∣Ψ).




Extended Checks
     • Pentagon identity: four‑step merges; report the “pentagon residual” as a higher‑order associativity
       test.
     • Cocycle residual: if x ⊕ y = x + y + I(x, y), report Δ = [I(x, y) + I(x ⊕ y, z)] − [I(y, z) +
       I(x, y ⊕ z)] before/after augmentation.



Failure Modes (to Report Regardless)
     • No low‑dimensional C achieves tolerance → evidence of intrinsic non‑closability at usable scales
       (strong‑emergence claim).
     • Excess path sensitivity only under extreme heterogeneity → delineates domain of validity for the
       macro model.




In‑Silico Pilot (for Calibration)
Simulator. Time‑windowed Gillespie‑style coalescence with a Brownian‑like kernel; matched triplet
generation using a radius‑based W1 tolerance; equal time windows per stage.


Quick readout (n=8 per cell; small, illustrative):




                                                      3
                         polydispersity σlog     surfactant α     AE (N )     AD (N )

                         0.15                    1.0              −0.125      0.071

                         0.15                    0.5              −0.125      0.357

                         0.45                    1.0              0.250       0.214

                         0.45                    0.5              0.250       0.214


Mass‑null spread was effectively zero at this scale (σnull ≈ 5 × 10−16 ); matching quality W1 on radii ≈
0.002–0.007. Directionality matches expectations: greater heterogeneity → larger associator signal;
surfactant suppression modulates the gap.


      Use this pilot to set τ , n, and ϵ realistically before wet‑lab work; then rerun power with
      stabilized null spreads.




OSF Checklist
-




External References (selected)
     • Coalescence / Smoluchowski.


     • Aldous, D. J. (1999). Deterministic and stochastic models for coalescence (aggregation and coagulation): A
       review of the mean‑field theory for probabilists. Bernoulli, 5(1), 3–48. DOI: 10.2307/3318611. (Open
       PDF via Project Euclid.)


     • Menon, G., & Pego, R. L. (2006). Dynamical scaling in Smoluchowski’s coagulation equations. SIAM
       Review, 48(4), 745–768.
     • Friedlander, S. K. (2000). Smoke, Dust, and Haze: Fundamentals of Aerosol Dynamics (2nd ed.). Oxford
       Univ. Press. (Brownian coagulation kernels, Chap. 7.)

     • Seinfeld, J. H., & Pandis, S. N. (1998/2016). Atmospheric Chemistry and Physics. Wiley. (Continuum
       Brownian kernel forms.)


     • Stochastic simulation.


     • Gillespie, D. T. (1976/1977). Exact stochastic simulation of coupled chemical reactions. J. Stat. Phys. 16,
       311; J. Phys. Chem. 81, 2340–2361.


     • Optimal transport / Wasserstein‑1.


     • Villani, C. (2008/2009). Optimal Transport: Old and New. Springer.




                                                       4
• Peyré, G., & Cuturi, M. (2019). Computational Optimal Transport. Found. & Trends® in ML; also arXiv:
  1803.00567.


• Lumpability (Markov coarse‑graining).


• Kemeny, J. G., & Snell, J. L. (1960/1976). Finite Markov Chains. Springer.


• Buchholz, P. (1994). Exact and ordinary lumpability in finite Markov chains. Journal of Applied
  Probability, 31(1), 59–75.


• Associativity / Coherence.


• Mac Lane, S. (1963). Natural associativity and commutativity. Rice Univ. Studies, 49, 28–46. (Pentagon
  identity.)


• Mac Lane, S. (1998, 2nd ed.). Categories for the Working Mathematician. Springer.


• Information Bottleneck.


• Tishby, N., Pereira, F. C., & Bialek, W. (1999/2000). The Information Bottleneck Method. Allerton Conf.;
  arXiv\:physics/0004057.


• Moment closure / invariant manifolds.


• Gorban, A. N., & Karlin, I. V. (2005). Invariant Manifolds for Physical and Chemical Kinetics. Springer
  (LNP 660).


• Kuehn, C. (2016). Moment Closure — A Brief Review. In: Control of Self‑Organizing Nonlinear Systems,
  253–271; arXiv:1505.02190.


• Microfluidic droplets.


• Teh, S.-Y., Lin, R., Hung, L.-H., & Lee, A. P. (2008). Droplet microfluidics. Lab on a Chip, 8(2), 198–220.


• Multiple testing.


• Holm, S. (1979). A simple sequentially rejective multiple test procedure. Scandinavian Journal of
  Statistics, 6(2), 65–70.


 Where possible, references above include editions or sources with open PDFs/DOIs for
 long‑term OSF linking.




                                                    5
Appendix: Notation Cheatsheet

     • Φ(σ): chosen macro map (here, N ). Ψ(σ) = (Φ(σ), C(σ)).
     • ⊕: induced macro merge under Ψ via fitted law G.
     • AE : mean associator gap; AD : distributional associator gap (Wasserstein‑1).
               ~ : null spreads (physical & synthetic).
     • σnull , σ null
     • ϵE , ϵD : closure tolerances; IB: information bottleneck objective.

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                          6
