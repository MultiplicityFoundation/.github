---
slug: cp-ume-revision-spec-and-drop-in-manuscript-section
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Cp-ume Revision Spec And Drop-in Manuscript Section.md
  last_synced: '2026-03-20T17:17:20.625043Z'
---

Certified Prime-Gated Universal Multiplicity
Equation (CP-UME)
This document formalizes the Universal Multiplicity Equation (UME) into the Certified Prime-Gated
Universal Multiplicity Equation (CP-UME), suitable for rigorous analysis, simulation, and falsifiable
evaluation.


It contains:


     1. Implementation Checklist (author-facing, one-page style)
     2. Drop-in Manuscript Section (spec-level text with equations)




1) One-Page Implementation Checklist

1.1 Interpretation Lock: Two Lanes (Choose One Per Model Instance)

Template (dimensional):


$$ \partial_t \psi = A(t)\psi + B(t)!\int_{0}^{t}!K(t-\tau)\,I(\tau)\,d\tau + \Gamma(t)\,\mathcal{T}(\psi,\psi) + D(t)
\,\mathcal{D}\psi + H(t)\,\mathcal{N}(\psi) + \xi(t,\cdot). $$


      • ψ : state (vector field)
      • T : bounded bilinear operator (tensor coupling)
      • N : nonlinearity (e.g., componentwise power)
      • (K): memory kernel (set K≡1 only if you truly want a raw integral; see Gripenberg, Londen &
        Staffans, 1990)
      • D : smoothing/diffusion operator (lane-dependent)
      • ξ : forcing/noise

Lane A — Physical PDE.


      • Domain: x ∈ Ω ⊂ Rd
      • State: ψ(t, x) ∈ RK (or CK )
      • Operator: D = Δx
      • Must declare physical meaning of psi (density/amplitude/order parameter) to fix units.

Lane B — Graph/ML diffusion.


      • Domain: graph G = (V , E), N = ∣V ∣
      • State: ψ(t) ∈ RK×N (or flattened RKN )
      • Operator: D = −LG , where LG is a specified graph Laplacian (normalized or unnormalized; state
        which) (e.g., Chung, 1997; Belkin & Niyogi, 2003; Belkin, Niyogi & Sindhwani, 2006).
      • Must declare adjacency/kernel construction (concept graph, neural connectivity, similarity graph).




                                                          1
Rule: Present the template once, then instantiate Lane A and Lane B separately. Do not mix lanes within
proofs.




1.2 Nondimensionalization (Mandatory; Fixes Dimensional Issues; Enables Numerics)

Choose characteristic scales:


      • amplitude ψ0
      • time t0
      • (Lane A) length x0

Define dimensionless variables:


$$ \phi=\psi/\psi_0,\qquad \tilde t=t/t_0,\qquad \tilde x=x/x_0\;\;\text{(Lane A)}. $$


Rewrite the equation entirely in dimensionless form and use that form for all analysis/simulation.


Typical scaling identities:

        ~~              ~
      • A(t) = t0 A(t0 t)
                              ~ ~          ~
      • Lane A diffusion: D (t) = xt02 D(t0 t)
                                     0
                                                   ~ ~        ~
      • Lane B diffusion (if LG dimensionless): D (t) = t0 D(t0 t)
                              ~ ~               ~
      • Bilinear coefficient: Γ(t) = t0 ψ0 Γ(t0 t)
                                             ~ ~                ~
      • Power nonlinearity N (ψ) = ψ ⊙n : H (t) = t0 ψ0n−1 H(t0 t)
               ~~                  ~
      • Noise: ξ (t, ⋅) = ψt0 ξ(t0 t, ⋅)
                            0




1.3 Constrained Prime Gating (Parsimonious + Identifiable)

Let PN = {2, 3, 5, … , pN } be the first N primes.


For each coefficient operator/matrix C(t) ∈ {A, B, Γ, D, H}:


$$ C(t)=\sum_{p\in P_N} c_p(t)\,W_p. $$


Requirements:


      • {Wp } are declared and linearly independent (preferably orthonormal under Frobenius/Hilbert–
       Schmidt inner product).

Constraints (must appear in the model definition):


     1. Finite support: only primes in PN .
     2. Decay envelope: ∣cp (t)∣ ≤ C p−α (use α > 1 if taking N → ∞ in theory).




                                                        2
    3. Uniform **ℓ1 ** bound: ∑p∈PN ∣cp (t)∣ ≤ C∗ for all t. (Analogous to ℓ¹ sparsity control; see
       Tibshirani, 1996.)
    4. (Optional) Temporal smoothness: ∣ċp (t)∣ ≤ ν p−α .




1.4 Falsifiability Bridge (Prime vs Matched Baselines)

Claim to test: prime gating yields stability/structure not achieved by equally sparse non-prime gating.


Required gating schemes (matched parameter count and matched decay envelope):


     • P (Prime): PN
     • R (Random sparse): RN integers, same size, same decay envelope
     • H (Harmonic/log-spaced): e.g., {1, 2, 4, 8, … } or log-spaced integers
     • S (Scrambled primes): primes kept but permute mapping p ↦ Wp

Required metrics:


     • Stability margin/basin size: fraction of initial conditions with bounded trajectories over horizon
       [0, T ]
     • Largest Lyapunov exponent: λmax (Benettin et al., 1980; Wolf et al., 1985).
     • Scaling with **N **: trends of λmax (N ), basin size vs N

Decision rule:


     • If P does not beat R/H/S reproducibly on at least one primary metric, reframe as “structured sparse
       spectral gating,” not prime-specific structure.




1.5 Fast Validation (2–5 Days)

A (1–2 days): Minimal simulation


     • Lane A: 1D PDE on [0, 1] with Neumann BCs, or Lane B: small graph N ≈ 50
     • Use K = 3
                        ~
     • Sweep (α, C∗ , D )
     • Report basin size + λmax for P/R/H/S

B (2–3 days): ML task


     • Implement discretized CP-UME as a recurrent cell
     • Train on chaotic prediction (Lorenz) or long-horizon memory task (Bengio, Simard & Frasconi, 1994).
     • Report gradient explosion incidence + test error for P/R/H/S

C: Only if A and B show prime-specific advantage, proceed to quantum/tunneling framing tests.




                                                     3
2) Drop-in Manuscript Section (Spec-Level)

3. Certified Prime-Gated Universal Multiplicity Equation (CP-UME)

3.1 Template Model and Two-Lane Instantiation

We define a general dynamical template for a K -component state ψ with linear drift, memory, bilinear
coupling, smoothing/diffusion, nonlinearity, and forcing:


$$ \partial_t \psi = A(t)\psi + B(t)!\int_{0}^{t}!K(t-\tau)\,I(\tau)\,d\tau + \Gamma(t)\,\mathcal{T}(\psi,\psi) + D(t)
\,\mathcal{D}\psi + H(t)\,\mathcal{N}(\psi) + \xi(t,\cdot). \tag{1} $$


Here T is a bilinear operator and N is a nonlinear map (e.g., componentwise power). The smoothing
operator D is chosen according to one of two instantiations:


Lane A (Physical PDE). Let Ω ⊂ Rd and ψ(t, ⋅) ∈ L2 (Ω; RK ) (or CK ). We set D = Δx and interpret ψ as a
physical field (e.g., density, amplitude, order parameter), which fixes units.


Lane B (Graph/ML). Let G = (V , E) be a graph with N = ∣V ∣ and ψ(t) ∈ RK×N . We set D = −LG ,
where LG is a specified graph Laplacian constructed from an explicitly defined adjacency/kernel. (e.g.,
Chung, 1997; Belkin & Niyogi, 2003; Belkin, Niyogi & Sindhwani, 2006).


All analyses and experiments are performed within one lane at a time; Lane A and Lane B are separate
instantiations of the shared template (1).



3.2 Nondimensionalization (Primary Form)

To ensure dimensional consistency and numerical stability, we nondimensionalize (1). Choose characteristic
scales: amplitude ψ0 , time t0 , and (Lane A) length x0 . Define


$$ \phi=\psi/\psi_0,\qquad \tilde t=t/t_0,\qquad \tilde x=x/x_0\quad\text{(Lane A)}. \tag{2} $$

                                                 ~   ~
In Lane A, Δx = x−2
                 0 Δx . Writing all terms in (t, x) yields the dimensionless evolution
                    ~


$$ \partial_{\tilde t}\phi = \tilde A(\tilde t)\phi + \tilde B(\tilde t)!\int_{0}^{\tilde t}!\tilde K(\tilde t-\tilde\tau)\,
\tilde I(\tilde\tau)\,d\tilde\tau + \tilde\Gamma(\tilde t)\,\mathcal{T}(\phi,\phi) + \tilde D(\tilde t)\,
\tilde{\mathcal{D}}\phi + \tilde H(\tilde t)\,\tilde{\mathcal{N}}(\phi) + \tilde\xi(\tilde t,\cdot). \tag{3} $$


Typical coefficient scalings are


$$ \tilde A(\tilde t)=t_0\,A(t_0\tilde t), \qquad \tilde\Gamma(\tilde t)=t_0\psi_0\,\Gamma(t_0\tilde t), \tag{4} $$


$$ \tilde D(\tilde t)= \begin{cases} \dfrac{t_0}{x_0^2}D(t_0\tilde t), & \text{Lane A},\
t_0D(t_0\tilde t), & \text{Lane B if }L_G\text{ is dimensionless}, \end{cases} \qquad \tilde\xi(\tilde t,
\cdot)=\dfrac{t_0}{\psi_0}\,\xi(t_0\tilde t,\cdot). \tag{5} $$



                                                             4
                                                                         ~
For a componentwise power nonlinearity N (ψ) = ψ ⊙n , we take N (ϕ) = ϕ⊙n and define


$$ \tilde H(\tilde t)=t_0\psi_0^{\,n-1}H(t_0\tilde t), \tag{6} $$

                                                        ~
absorbing all dimensional dependence into H . Equation (3) is therefore dimensionally consistent by
construction and is used throughout.



3.3 Certified Prime-Mixture Coefficients (Prime Gating)

                                                                                                        ~
Let PN = {2, 3, 5, … , pN } denote the first N primes. For each coefficient operator/matrix C(t) ∈
 ~ ~ ~ ~ ~
{A, B , Γ, D, H }, we impose the constrained prime-mixture representation

$$ C(\tilde t)=\sum_{p\in P_N} c_p(\tilde t)\,W_p, \tag{7} $$


where {Wp }p∈PN are fixed, declared, and linearly independent basis operators (preferably orthonormal
under the Hilbert–Schmidt/Frobenius inner product). The scalar weights satisfy


      • Finite support: only p ∈ PN .
                                ~
      • Decay envelope: ∣cp (t)∣ ≤ C p−α (use α > 1 for asymptotic theory).
                                                ~                   ~
      • Uniform **ℓ1 ** bound: ∑p∈PN ∣cp (t)∣ ≤ C∗ for all t.
                                                    ~
      • (Optional) Temporal smoothness: ∣ċp (t)∣ ≤ ν p−α .

These constraints ensure prime gating is a parsimonious, identifiable modulation rather than a generic
function approximator.



3.4 Well-Posedness (Theorem-Ready Conditions)

Let H be the relevant Hilbert space (Lane A: L2 (Ω; RK ); Lane B: RK×N ). Define the linear operator


$$ \tilde{\mathcal{L}}(\tilde t):=\tilde A(\tilde t)+\tilde D(\tilde t)\,\tilde{\mathcal{D}}. $$


Assume:

        ~ ~                                         ~               ~
                                                 ~) with ∥U (t, s~)∥ ≤ M e−ω(t−s) .  ~ ~
     1. L(t) generates an evolution family U (t, s
     2. T is bounded bilinear: ∥T (u, v)∥ ≤ b∗ ∥u∥ ∥v∥.
        ~ ~
     3. N (t, ⋅) is locally Lipschitz on bounded sets.
     4. Prime-mixture constraints (7) hold.

Theorem 1 (Local well-posedness). Under assumptions 1–4, for any ϕ0 ∈ H there exists T > 0 and a
unique mild solution ϕ ∈ C([0, T ]; H) to (3). If, additionally, linear dissipation dominates nonlinear growth
(standard energy/small-gain conditions), the solution is global. See, e.g., Pazy (1983), Henry (1981), Temam
(1988), and Evans (1998).




                                                            5
3.5 Falsifiable Predictions and Mandatory Baselines

CP-UME makes a prime-specific empirical claim:


Claim (Prime-specific stability). Under matched parameter budgets and matched decay envelopes, prime
gating yields increased stability (larger basin of attraction and/or more negative λmax ) compared to non-
prime sparse gating.


Mandatory baseline gating schemes (matched N , matched decay envelope):


     • P: primes PN
     • R: random sparse integers RN
     • H: harmonic/log-spaced integers (e.g., {1, 2, 4, 8, … })
     • S: scrambled primes (permute mapping p ↦ Wp )

Primary metrics:


    1. Stability margin (bounded trajectory fraction over [0, T ]).
    2. Largest Lyapunov exponent λmax .
    3. Scaling with N : trends of λmax (N ) and basin size vs N .

A positive result requires P to exceed R/H/S reproducibly on at least one primary metric; otherwise the
contribution should be reframed as structured sparse spectral gating.




3) Notation Defaults (Recommended)
     • Use ψ for dimensional state, ϕ for dimensionless.
           ~  ~ for dimensionless variables.
     • Use t, x
     • Use D = Δx (Lane A) and D = −LG (Lane B).
     • Use ⊙ for componentwise powers.




4) Minimal Experimental Protocol (Appendix-ready)
     • Fix K = 3, choose a simple bounded T (e.g., [T (u, v)]k = ∑j,l Tkjl uj vl with bounded Tkjl ).
     • Choose N ∈ {5, 10, 20} and compare P/R/H/S at each N .
     • Report (i) basin size estimate, (ii) λmax , (iii) scaling curves vs N .

References

    1. Pazy, A. (1983). Semigroups of Linear Operators and Applications to Partial Differential Equations
       (Applied Mathematical Sciences, Vol. 44). Springer.
    2. Henry, D. (1981). Geometric Theory of Semilinear Parabolic Equations (Lecture Notes in Mathematics,
       Vol. 840). Springer.




                                                           6
    3. Temam, R. (1988). Infinite-Dimensional Dynamical Systems in Mechanics and Physics (Applied
       Mathematical Sciences, Vol. 68). Springer.
    4. Gripenberg, G., Londen, S.-O., & Staffans, O. (1990). Volterra Integral and Functional Equations.
       Cambridge University Press.
    5. Chung, F. R. K. (1997). Spectral Graph Theory (CBMS Regional Conference Series in Mathematics, No.
       92). American Mathematical Society.
    6. Belkin, M., & Niyogi, P. (2003). Laplacian eigenmaps for dimensionality reduction and data
       representation. Neural Computation, 15(6), 1373–1396.
    7. Belkin, M., Niyogi, P., & Sindhwani, V. (2006). Manifold regularization: A geometric framework for
       learning from labeled and unlabeled examples. Journal of Machine Learning Research, 7, 2399–2434.
    8. Bengio, Y., Simard, P., & Frasconi, P. (1994). Learning long-term dependencies with gradient descent
       is difficult. IEEE Transactions on Neural Networks, 5(2), 157–166.
    9. Benettin, G., Galgani, L., Giorgilli, A., & Strelcyn, J.-M. (1980). Lyapunov characteristic exponents for
       smooth dynamical systems and for Hamiltonian systems: A method for computing all of them.
       Meccanica.
   10. Wolf, A., Swift, J. B., Swinney, H. L., & Vastano, J. A. (1985). Determining Lyapunov exponents from a
       time series. Physica D: Nonlinear Phenomena, 16, 285–317.
   11. Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. Journal of the Royal Statistical
       Society: Series B, 58(1), 267–288.
   12. Evans, L. C. (1998). Partial Differential Equations (Graduate Studies in Mathematics, Vol. 19). American
       Mathematical Society.

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                       7
