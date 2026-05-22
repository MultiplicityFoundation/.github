---
slug: field-distribution-engineering-in-fractal-nonlinear-capacitors-integrated-manuscript-draft
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Field-distribution Engineering In Fractal Nonlinear Capacitors
    (integrated Manuscript Draft).md
  last_synced: '2026-03-20T17:17:20.573891Z'
---

Field-Distribution Engineering in Fractal Nonlinear
Capacitors
Integrated, submission-ready manuscript skeleton (Abstract → References), incorporating the final theory/
validation framework, precision edits, and figure-caption mini-results.




Abstract
The relentless scaling of passive components demands strategies beyond conventional material
optimization. While fractal geometries have been explored to increase capacitance density through area
enhancement, their interaction with nonlinear dielectrics remains underexplored. Here, we introduce field-
distribution engineering via self-similar electrodes as a method to tailor the nonlinear capacitive response
of thin-film dielectrics. We present a model that decouples geometric and material contributions: the
differential capacitance is expressed as a weighted field-distribution integral of the intrinsic differential
permittivity εdiff (E) against a geometry-controlled density p(E). Using BaTiO3 as a model nonlinear
dielectric, we fabricate and characterize fractal capacitors of varying iteration depths. We demonstrate
superlinear scaling of capacitance with fractal depth—exceeding predictions from a linear geometric
series—and correlate this with simulated field distributions. The approach yields predictable fractional-
order dynamics, characterized by a constant-phase element exponent α that decreases with iteration
depth. However, field enhancement at fractal tips reduces the breakdown voltage, creating a trade-off that
leads to an optimal iteration depth for maximum usable energy density. This framework of field-
distribution engineering provides a general principle for co-designing geometry and material nonlinearity
in next-generation passive devices.




Introduction

The Need for Geometric Leverage in Capacitor Scaling

The demand for higher capacitance density in integrated passive components continues to outpace the
incremental gains from dielectric material discovery. While high-κ and nonlinear dielectrics (e.g.,
ferroelectrics like BaTiO3 ) offer enhanced permittivity, their response is often strongly field-dependent and
ultimately limited by breakdown [1,2]. This has spurred interest in geometric amplification—using
electrode morphology to increase effective area within a fixed footprint.


Fractal Electrodes: From Area Enhancement to Field Distribution Control

Fractal and interdigitated electrodes are established techniques for increasing capacitance density [3,4]. In
linear dielectrics, their benefit is well-modeled as an increase in effective electrode area or perimeter.
However, in a nonlinear dielectric, where permittivity varies with local electric field ε(E), the device
response is no longer a simple function of geometry alone. The local field, and thus the material's
contribution, is spatially modulated by the electrode morphology. Prior work on fractal capacitors has




                                                      1
largely overlooked this coupled electromechanical response, treating the dielectric as linear or ignoring the
field heterogeneity inherent to self-similar structures [5,6]. This interaction remains underexplored,
particularly in a framework that is both predictive and experimentally validated.


The Concept of Field-Distribution Engineering

We propose that the true design variable for nonlinear capacitors is not merely area, but the statistical
distribution of electric fields p(E) within the dielectric volume. A fractal electrode, by creating a hierarchy
of feature scales, engineers this distribution, concentrating weight in regions of high or low field depending
on the geometry. The device's macroscopic differential capacitance Cd (V ) then becomes a weighted
functional of the material's εdiff (E) over this distribution. This field-distribution engineering paradigm
shifts the focus from maximizing area to sculpting the internal field landscape to optimally sample a
material's nonlinear response.


This Work: A Coupled Theory and Validation

We develop a theoretical framework that separates exact small-signal electrostatics from a practical
geometry–material decoupling approximation, and validate it using planar fractal electrodes of varying
iteration depths paired with a thin-film ferroelectric dielectric (BaTiO3 ). We demonstrate:


    1. Superlinear capacitance scaling with fractal depth, explained by the field-distribution integral of
       εdiff (E) against a simulated p(E).
    2. The emergence of fractional-order dynamics (constant-phase element behavior) that scales with
       geometric complexity.
    3. The critical breakdown-energy trade-off, where field enhancement at fractal tips reduces operating
       voltage, leading to a well-defined optimum in usable energy density.




Theory

1. Small-Signal Differential Capacitance as a Second Variation

We consider an isotropic, nonlinear dielectric described by a constitutive relation D(E) = ε0 E + P (E).
The field-dependent differential permittivity is


$$ \varepsilon_{\mathrm{diff}}(E) = \frac{dD}{dE}. $$


For a fixed electrode geometry G and dielectric domain Ω, the application of a DC bias V establishes a
steady-state potential ϕb (x; V ), with the corresponding electric field Eb (x; V ) = −∇ϕb .


To define the small-signal (differential) capacitance Cd (V ; G), we consider a harmonic perturbation δV ejωt
about the bias point. Linearizing Poisson's equation around the biased state yields a linear problem for the
complex perturbation potential ϕ1 (x; V ), defined as the solution to


$$ \nabla \cdot \left[ \varepsilon_{\mathrm{diff}}(E_b(\mathbf{x}; V)) \, \nabla \phi_1(\mathbf{x}; V) \right] =
0, \tag{A1} $$




                                                        2
with boundary conditions ϕ1 = 1 on the working electrode and ϕ1 = 0 on the counter-electrode. The
differential capacitance is then given by the second variation of the electrostatic energy:


$$ C_d(V; G) = \int_{\Omega} \varepsilon_{\mathrm{diff}}(E_b(\mathbf{x}; V)) \, |\nabla \phi_1(\mathbf{x};
V)|^2 \, d\Omega. \tag{1} $$


2. Field-Distribution Functional Representation

Equation (1) can be reinterpreted as a weighted average of the material response over the spatial field
distribution. We define a normalized weighting measure


$$ d\mu_V(\mathbf{x}) = \frac{\varepsilon_{\mathrm{diff}}(E_b) |\nabla\phi_1|^2 \, d\Omega}{\int_\Omega
\varepsilon_{\mathrm{diff}}(E_b) |\nabla\phi_1|^2 \, d\Omega}. $$


Pushing this measure forward through the mapping x ↦ Eb (x; V ) yields a biased field-distribution
        ~ (E; G), satisfying
density p V


$$ \int_0^\infty f(E) \, \tilde{p}V(E; G) \, dE = \int\Omega f(E_b(\mathbf{x}; V)) \, d\mu_V(\mathbf{x}) $$

                                                            ~ generally depends on both geometry and bias
for any test function f . This representation is exact, but p V
through the biased solution.


To obtain a tractable design rule that separates geometry from material, we introduce a geometry-only
reference. Let ψ1 (x; G) be the solution to Eq. (A1) with a constant εdiff ≡ ε0 (Laplace solution for the same
geometry). Define


$$ C_{\mathrm{geo}}(G) = \varepsilon_0 \int_\Omega |\nabla \psi_1|^2 \, d\Omega, $$


and the corresponding geometry-only field distribution using the unit-bias Laplace field magnitude Eb0 (x):


$$ p(E; G) \, dE = \frac{ \int_{{\mathbf{x}: E_b^0(\mathbf{x}) \in [E, E+dE]}} \varepsilon_0 |\nabla\psi_1|^2 \,
d\Omega }{C_{\mathrm{geo}}(G)}. $$

                                                  ~ (E; G) yields the central design relation:
Using p(E; G) as a zeroth-order approximation for p V


$$ \frac{C_d(V; G)}{C_{\mathrm{geo}}(G)}          \approx    \int_0^\infty   \frac{\varepsilon_{\mathrm{diff}}(E)}
{\varepsilon_0} \, p(E; G) \, dE. \tag{2} $$


This approximation becomes exact for a linear dielectric and remains accurate when spatial variations in
εdiff do not strongly perturb the field pattern from the Laplace solution.

                                  ~                                                                           ~
Normalized-field form. With E = E/(V /d), the geometry-only distribution can be reported as p(E ; G),
bias-invariant by construction.




                                                         3
3. Material Model: Landau-Ginzburg-Devonshire (LGD)

For a ferroelectric dielectric such as BaTiO3 , the nonlinear polarization response is captured by the LGD
free-energy expansion (1D, monodomain):


$$ \mathcal{F}(P, E) = \frac{a}{2} P^2 + \frac{b}{4} P^4 + \frac{c}{6} P^6 - E P, $$


with equilibrium polarization satisfying


$$ E = a P + b P^3 + c P^5. $$


With D = ε0 E + P , the differential permittivity is


$$ \varepsilon_{\mathrm{diff}}(E) = \frac{dD}{dE} = \varepsilon_0 + \frac{dP}{dE} = \varepsilon_0 + \frac{1}{a
+ 3b P^2 + 5c P^4}. \tag{3} $$


4. Self-Similar Electrodes: Geometric Scaling and Field Enhancement

Consider a self-similar electrode iterated to depth     n. Let iteration k introduce N k features with
characteristic length ℓk = s ℓ0 (0 < s < 1). If the capacitive contribution of a feature scales as ℓβ (β ≈ 2
                              k

for area-dominated, β ≈ 1 for fringe-field-dominated), define


$$ \rho_{\mathrm{total}}(n) = \sum_{k=0}^{n} (N s^\beta)^k = \sum_{k=0}^{n} \rho^k, \quad \rho = N
s^\beta. \tag{4} $$


Features at scale k produce local field enhancement κk ≥ 1 relative to Eavg = V /d, i.e., Ek (V ) ≈ κk V /d.
In practice κk and hotspot metrics are extracted from FEM (preferably via high-percentile fields rather than
point maxima).


5. Coupled Geometry–Nonlinearity Scaling Model

A discrete approximation consistent with Eq. (2) is


$$ C_d^{(n)}(V) \approx C_0 \sum_{k=0}^{n} \rho^k \, \gamma_k(V), \qquad \gamma_k(V)                        =
\frac{\varepsilon_{\mathrm{diff}}(\kappa_k V / d)}{\varepsilon_{\mathrm{diff}}(V / d)}. \tag{5} $$


Here C0 is the base capacitance of the k = 0 structure with a linear dielectric.


6. Breakdown-Limited Optimization and Usable Energy

Let Ebd be intrinsic breakdown field. The breakdown voltage is constrained by the maximum enhancement
factor:


$$ V_{\mathrm{bd}}^{(n)} \lesssim \frac{d \cdot E_{\mathrm{bd}}}{\kappa_{\max}(n)}, \qquad \kappa_{\max}
(n)=\max_{k\le n}\kappa_k. \tag{6} $$




                                                         4
                                              (n)
Usable energy at operating voltage Vop ≤ Vbd is


$$ U_{\mathrm{use}}^{(n)}(V_{\mathrm{op}}) = \int_0^{V_{\mathrm{op}}} Q^{(n)}(V) \, dV, \qquad Q^{(n)}(V)
= \int_0^{V} C_d^{(n)}(V') \, dV'. \tag{7} $$


Equivalently,


$$ U_{\mathrm{use}}^{(n)}(V_{\mathrm{op}})=\int_0^{V_{\mathrm{op}}} (V_{\mathrm{op}}-V')\,C_d^{(n)}(V')
\,dV'. $$

                                                           (n)
The model predicts an optimal depth n∗ maximizing Uuse .


7. Fractional-Order Dynamics from Distributed RC Networks

Self-similar morphology yields a broad distribution of time constants. A constant-phase element (CPE)
captures dispersive impedance:


$$ Z_{\mathrm{CPE}}(\omega)=\frac{1}{Q (j\omega)^\alpha},\qquad 0<\alpha<1. \tag{8} $$


For a fractal electrode, α is expected to decrease with iteration depth n, reflecting broader relaxation
spectra. This dispersive behavior is primarily geometric and can be characterized independently from
dielectric nonlinearity via bias-dependent impedance spectroscopy.




Experimental Methods and Validation

1. Device Set and Experimental Matrix

     • Fabricate matched sets: plain, interdigitated, and fractal geometries Gn for n = 0..nmax .
     • Hold constant: footprint A, dielectric thickness d, dielectric stack, electrode metals, process
       conditions.
     • Include replicates: Ndev per geometry/depth across Nwaf / Ndies .

2. Fabrication and Structural Metrology

     • Report gmin (minimum gap), linewidths, etch bias, and rtip (tip radius/rounding) via SEM/CD-SEM/
       AFM.

     • Identify truncation scale ℓmin and quantify variability across device sets.


     • Use parallel-plate control capacitor fabricated with identical dielectric and electrodes.


     • Measure small-signal Cd (V ) with AC perturbation δV chosen to remain in the linearized regime.
     • Map field as E ≈ V /d (account for series drops if relevant).
     • Obtain εdiff (E) ≈ Cd (V ) d/A.
     • Optional: fit εdiff (E) to LGD (Eq. 3) and state hysteresis handling (minor loop / branch selection).




                                                       5
4. Electrical Characterization

      • C–V and loss: measure Cd (V ; G) and tan δ(V ; G) across a safe bias range.
      • EIS: measure Z(ω; V ); fit to CPE (Q, α) + parasitics (Rs , leakage as needed).
      • Time domain (optional): controlled charge/discharge; fit to stretched exponential or multi-
           exponential.

5. Breakdown Testing and Reliability Statistics

      • Measure breakdown voltage Vbd using controlled ramp rate and current compliance.

      • Report Weibull statistics for each n and geometry class.


      • Laplace reference: solve with ε = ε0 and unit bias to compute ψ1 , Cgeo (G), and geometry-only
             ~
           p(E ; G).

      • Hotspot metrics: compute κmax (n) from high-percentile ∣E∣ (mesh-converged, tip-refined meshes).
                                         ~                                                           ~   ~
      • Distribution construction: bin E and accumulate weights ∝ ε0 ∣∇ψ1 ∣2 ; normalize so ∫ p(E )dE =
           1.

7. Model Validation Workflow
                          ~
     1. FEM: compute p(E ; Gn ) for each n.
     2. Material: measure εdiff (E) from control; optionally LGD-fit.
     3. Predict: Cd (V ; Gn ) = Cgeo (Gn ) ∫ (εdiff (E)/ε0 )p(E; Gn )dE .
     4. Verify: compare predicted vs measured Cd (V ), report NRMSE and uncertainty bands.
                                          (n)                               (n)
     5. Breakdown trade-off: correlate Vbd with κmax (n) and compute Uuse up to a conservative Vop .
     6. Dispersion: validate α(n) decreases with n, including low-bias evidence.




Results (Template)
Figure 1 presents the intrinsic nonlinear dielectric response, decoupled from geometric effects. The
differential permittivity εdiff (E) measured on the control parallel-plate capacitor shows [describe trend].
The data are well-described by the LGD model (Eq. 3), with fitted coefficients a = [val], b = [val], c = [val].
Loss tangent tan δ(E) exhibits [trend].


2. Engineered Field Distributions from Fractal Iteration

Figure 2 quantifies geometric manipulation of the field. SEM confirms self-similar patterning and ℓmin =
                                                                     ~         ~
[val]. Laplace-derived, geometry-only field-distribution densities p(E ; Gn ) (E = E/(V /d)) reveal the core
                                                                                  ~
mechanism: with increasing n, the distribution develops a heavier high-E tail. This tail corresponds to
                          ~
enhanced-field regions (E ∼ κk ) that weight εdiff (E) in Eq. (2) and enter the discrete model via γk (V ) in
Eq. (5).




                                                        6
3. Prediction and Measurement of Differential Capacitance

Figure 3 validates Eq. (2). Predicted Cd (V ) (lines) computed from measured εdiff (E) and simulated
   ~
p(E ; Gn ) agrees with measured Cd (V ) (symbols) over V ≤ Vop . Report NRMSE = [X]% with uncertainty
                                                                                  (n)
bands from εdiff noise and FEM discretization. Superlinear scaling is defined as Cd (V ) increasing faster
                                            (n)    n
with n than the linear-dielectric baseline Clin ∝ ∑k=0 ρk .


4. Fractal-Induced Dispersion and Fractional-Order Dynamics

Figure 4 shows EIS and CPE fits. α decreases systematically with iteration depth n, and the trend persists at
low bias where Cd (V ) is nearly constant, supporting a primarily geometric origin for dispersion. Time-
domain discharge shows progression from exponential to stretched-exponential relaxation as n increases.


5. Breakdown Statistics and the Usable Energy Trade-off
                                                                                 (n)
Figure 5 establishes the trade-off. The characteristic breakdown voltage Vbd decreases with n (Weibull).
                                                                                                        (n)
When normalized by simulated κmax (n), the inferred intrinsic breakdown field Ebd ≈ κmax (n)Vbd /d
remains constant within uncertainty, consistent with geometry-driven breakdown reduction. Usable energy
  (n)
Uuse peaks at optimal depth n∗ =[val].

6. Comprehensive Performance Comparison

Figure 6 compares all geometries. Fractal device at n∗ achieves [X]× increase in Cd at [Y] V vs plain;
                                                            2
interdigitated yields [Z]×. Ragone-style plot uses Pmax = Vop /(4Rs ) per unit volume; define how Rs is
extracted and how volume is defined.




Discussion and Limitations

Synthesis of Findings
                               ~
        • Geometry sculpts p(E ; Gn ), enabling predictive control of nonlinear response via Eq. (2).
        • Fractional-order dynamics track geometric complexity (α(n) decreases with n).
        • A breakdown-limited optimum n∗ emerges as predicted by Eq. (6)–(7).

Limitations and Future Directions

(i) Geometry-only approximation: Eq. (2) uses a Laplace-derived p(E; G) as a proxy for the fully coupled
biased distribution; exact for linear dielectrics and accurate when εdiff variations do not strongly reshape
the field pattern. Deviations are expected at highest biases; fully self-consistent nonlinear FEM is a next
step.


(ii) Hysteresis and loss: Small-signal reversible Cd (V ) and tan δ(V ) are emphasized. Large-signal cycling
may introduce hysteresis and additional dissipation; characterize branch selection/minor loops explicitly.




                                                         7
(iii) Leakage and pre-breakdown conduction: Field enhancement may increase leakage; future work
should map J(E, T ) and geometry dependence.


(iv) Feature sensitivity: Hotspot fields depend on rtip and gmin ; mitigate via metrology and FEM mesh
convergence, but scalability requires tighter process control.


(v) Extension to 3D: Planar fractals provide a controlled platform; volumetric architectures may offer
additional leverage but introduce deposition/void/defect challenges.




Conclusion
Self-similar electrodes provide a geometry-first knob—field-distribution engineering—for co-optimizing
nonlinear dielectric response and device performance. The field-distribution integral framework links
electrode design to bias-dependent capacitance, dispersion, breakdown-limited optimization, and usable
energy via a unified, falsifiable model.




Figure Captions (Mini-Results)
Figure 1. Intrinsic nonlinear dielectric response of BaTiO3 . (a) Measured differential permittivity εdiff (E)
(symbols) from a parallel-plate control capacitor, with fit to the LGD model (solid line). Inset: corresponding
loss tangent tan δ(E). (b) Nonlinear polarization response P (E) implied by the fitted LGD constitutive
relation (or measured minor-loop branch, if available).


Figure 2. Engineered field distributions via fractal iteration. (a) SEM micrographs of fabricated
electrodes: plain, interdigitated, and fractal iterations n = 0–3. Scale bars: 2 µm. Inset: measured tip radius
rtip versus design scale ℓk . (b) FEM simulation of ∣E∣ at unit bias (log scale). (c) Geometry-only field-
                         ~                                                                          ~
distribution densities p(E ; Gn ) extracted from Laplace simulations, showing evolution of the high-E tail
                                       ~ ~
with increasing n. Normalized so ∫ p(E )dE = 1.


Figure 3. Prediction and measurement of differential capacitance. (a) Measured Cd (V ) (symbols) for
fractal iterations n = 0–3, compared to predictions (lines) from Eq. (2). Shaded bands represent uncertainty
from εdiff (E) measurement and FEM discretization. (b) Cd at V = 5 V versus iteration depth n.
Superlinear trend exceeds linear-dielectric geometric baseline ∑ ρk . Error bars: device-to-device variation.


Figure 4. Geometric origin of fractional-order dynamics. (a) EIS data and CPE fits for n = 0 and n = 3 at
V = 0 V. (b) CPE exponent α versus n at low bias and high bias; decrease with n persists across bias. (c)
Normalized discharge curves for matched initial charge showing exponential-to-stretched-exponential
progression with increasing n.


Figure 5. Breakdown-energy trade-off and optimization. (a) Weibull plots of failure probability versus
                                              (n)
breakdown voltage Vbd . (b) Characteristic Vbd and simulated κmax (n) versus n. Inset: inferred intrinsic
                                     (n)
breakdown field Ebd = κmax (n)Vbd /d remains approximately constant within uncertainty. (c) Usable
                 (n)                (n)
energy density Uuse at Vop = 0.8 Vbd peaks at n∗ .



                                                      8
Figure 6. Comprehensive performance comparison. (a) Cd versus bias for all geometries: plain,
interdigitated, and fractal at n∗ . (b) Ragone-style plot of usable energy density versus power density, with
         2
Pmax = Vop /(4Rs ) per unit volume.



Submission Checklist (No-Regrets)
Conceptual & Narrative


      • Abstract frames “field-distribution engineering” as core contribution.
      • Intro establishes underexplored coupling of self-similar geometry with nonlinear ε(E).
      • Theory: exact small-signal form (Eq. 1) + practical decoupled approximation (Eq. 2).
                                                   ~
      • Causal chain maintained: geometry → p(E ) → predicted Cd (V ) → measured Cd (V ) and dispersion
       → breakdown-limited optimum.

Technical Precision


      • “Superlinear” defined vs linear-dielectric ∑ ρk baseline.
      • Breakdown voltage decreases with n; intrinsic Ebd inferred \~ constant when normalized by κmax .
          ~
      • p(E ; G) explicitly Laplace-derived (geometry-only) and bias-invariant by construction.
      • Ragone power metric defined explicitly.
      • α(n) trend shown at low bias.

Experimental Rigor

                            ~
      • Methods specify p(E ) computation (binning, weighting, normalization).
      • FEM mesh-convergence and tip-refinement stated.
      • Hysteresis/branch selection stated for BaTiO3 .
      • Weibull breakdown analysis included.
      • Uncertainty bands shown for key plots.




References
[1] Dawber, M.; Rabe, K. M.; Scott, J. F. Physics of thin-film ferroelectric oxides. Rev. Mod. Phys. 77, 1083–1130
(2005). DOI: 10.1103/RevModPhys.77.1083.


[2] Tagantsev, A. K.; Sherman, V. O.; Astafiev, K. F.; Venkatesh, J.; Setter, N. Ferroelectric materials for
microwave tunable applications. Journal of Electroceramics 11(1–2), 5–66 (2003). DOI: 10.1023/B\:JECR.
0000015661.81386.e6.


[3] Samavati, H.; Hajimiri, A.; Shahani, A. R.; Nasserbakht, G. N.; Lee, T. H. Fractal capacitors. IEEE Journal of
Solid-State Circuits 33(12), 2035–2041 (1998). DOI: 10.1109/4.735706.




                                                        9
[4] Kim, E.-S.; Liang, J.-G.; Wang, C.; Cho, M.-Y.; Oh, J.-M.; Kim, N.-Y. Inter-digital capacitors with aerosol-
deposited high-K dielectric layer for highest capacitance value in capacitive super-sensing applications. Scientific
Reports 9, 680 (2019). DOI: 10.1038/s41598-018-37416-7.


[5] Torabi, S.; Cherry, M.; Duijnstee, E. A.; et al. Rough Electrode Creates Excess Capacitance in Thin-Film
Capacitors. ACS Applied Materials & Interfaces 9(32), 27290–27297 (2017). DOI: 10.1021/acsami.7b06451.


[6] Lallart, M.; Wang, L.; Petit, L. Enhancement of electrostatic energy harvesting using self-similar capacitor
patterns. Journal of Intelligent Material Systems and Structures 27(17), 2385–2394 (2016). DOI:
10.1177/1045389X16629573.


[7] Burke, A. Ultracapacitors: why, how, and where is the technology. Journal of Power Sources 91(1), 37–50
(2000). DOI: 10.1016/S0378-7753(00)00485-7.


Additional recommended references (dispersion/CPE and universal dielectric
response)

[8] Brug, G. J.; van den Eeden, A. L. G.; Sluyters-Rehbach, M.; Sluyters, J. H. The analysis of electrode
impedances complicated by the presence of a constant phase element. Journal of Electroanalytical Chemistry
and Interfacial Electrochemistry 176(1–2), 275–295 (1984). DOI: 10.1016/S0022-0728(84)80324-1.


[9] Jonscher, A. K. The ‘universal’ dielectric response. Nature 267, 673–679 (1977). DOI: 10.1038/267673a0.


[10] Barsoukov, E.; Macdonald, J. R. (eds.). Impedance Spectroscopy: Theory, Experiment, and Applications. 2nd
ed., Wiley-Interscience (2005).




Notes / Placeholders to Fill
      • Numeric fit parameters a, b, c and their temperature/processing dependence.
      • Exact nmax , s, N , β used for geometry; report how ρ is extracted.
      • NRMSE and uncertainty propagation method.
      • Definition of volume/mass normalization for energy and power densities.
      • Branch/minor-loop protocol for ferroelectric C–V extraction.

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                        10
