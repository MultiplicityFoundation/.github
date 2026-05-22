---
slug: prime-oscillation-weil-explicit-formula
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Prime Oscillation & Weil Explicit Formula.md
  last_synced: '2026-03-20T17:17:20.772747Z'
---

Prime Oscillation and the Explicit Formula: A
Rigorous Framework for Zeta Zero Reconstruction
By Ryan O. Van Gelder


Abstract
We reinterpret the Prime Eigenvalue Oscillation Hypothesis (PEOH) within the rigorous framework of the
Weil explicit formula. By expressing smoothed zero-density data as a superposition of von Mangoldt–
weighted prime-power harmonics, we obtain an exact finite reconstruction identity for band-limited test
functions. We formalize the bandwidth–resolution–cost tradeoff for zero reconstruction, propose a
reproducible numerical validation protocol, and state a trace-realization conjecture that cleanly separates
what is rigorous now from what would constitute RH-level progress. This is not a proof of the Riemann
Hypothesis (RH); rather, it is a mathematically defensible research program connecting explicit formula
technology with spectral/trace interpretations.




1. Introduction
The Riemann Hypothesis (RH) asserts that all nontrivial zeros of ζ(s) lie on ℜ(s) = 12 . Attempts to “explain”
zeros as interference among prime oscillations are common but often informal. This note salvages the
prime-oscillation intuition by placing it squarely inside the Weil/Guinand explicit formula. In this framework,
a smoothed zero measure is exactly equal (for suitable band-limited kernels) to a computable Archimedean
term plus a finite von Mangoldt–weighted oscillatory sum over n ≤ eL (hence including prime powers).


Contributions.


    1. RH-neutral formalization of “prime oscillation ↔ zeros” via the shifted explicit formula.
    2. Exact finiteness of the prime-power side for compactly supported f .
    3. A bandwidth–resolution–cost tradeoff: resolving zeros near height T requires L ≫ log T and prime
       powers up to scale eL ≳ T .
    4. A reproducible numerical protocol to verify the explicit formula numerically and to build a zero-
       locating algorithm.
    5. A logically consistent trace-realization conjecture (RH-strength) plus a conditional positivity sanity
       check.

Related work (high-level)

     • Weil/Guinand explicit formula and test-function formalism.
     • Selberg trace formula as a guiding analogy.
     • Connes’ trace-formula viewpoint in noncommutative geometry.
     • Berry–Keating semiclassical operator heuristics.
     • Montgomery pair correlation and Odlyzko’s computations of zero statistics.




                                                       1
2. Mathematical Framework

2.1 Fourier convention

We fix the normalization


$$ \widehat f(u)=\int_{-\infty}^{\infty} f(t)e^{-iut}\,dt,\qquad f(t)=\frac1{2\pi}\int_{-\infty}^{\infty}\widehat
f(u)e^{iut}\,du. $$


2.2 Completed zeta

Let


$$ \xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s). $$


Then ξ is entire and satisfies ξ(s) = ξ(1 − s).


2.3 Zeros and an RH-neutral spectral parameter

Let nontrivial zeros of ζ be ρ = β + iγ with multiplicity. Define


$$ \theta_\rho:=\frac{\rho-\tfrac12}{i}=\gamma+i\Big(\tfrac12-\beta\Big)\in\mathbb C. $$


Under RH, β = 12 and θρ = γ ∈ R.


2.4 Test-function class

Assume


      • f ∈ C0∞ ([−L, L]) is even and real-valued;
      • f is defined via the inverse Fourier transform.

Then f is even, real, Schwartz on R, and entire (Paley–Wiener).




3. Shifted bandlimited explicit formula
Define the smoothed zero-density (RH-neutral):


$$ Z_f(t):=\sum_{\rho} f\big(t-\theta_\rho\big), $$


where the sum is over nontrivial zeros with multiplicity.




                                                          2
Proposition 1 (Shifted bandlimited explicit formula)

There exists an explicit Archimedean term


$$ A_f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty} f(t-\tau)\,\Psi(\tau)\,d\tau, $$


where


$$           \Psi(\tau)=\frac{\Gamma'}{\Gamma}\Big(\tfrac14+\tfrac{i\tau}{2}\Big)+\frac{\Gamma'}{\Gamma}
\Big(\tfrac14-\tfrac{i\tau}{2}\Big)-\log\pi, $$


such that


$$ Z_f(t)=A_f(t)\; -\;2\sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}\,\widehat f(\log n)\,\cos(t\log n). $$


Finiteness. Since supp f ⊂ [−L, L], we have f (log n) = 0 for n > eL . Hence the von Mangoldt sum is
finite and exact at the truncation level n ≤ eL .


Reality. For real-even f , the symmetry ρ ↦ ρ implies Zf (t) ∈ R for real t.


RH specialization. If RH holds, θρ = γ ∈ R and Zf (t) = ∑γ f (t − γ).


Remark (shift mechanism). For the shifted kernel ft (x) := f (t − x), one has ft (u) = e−iut f (u), yielding
cosine terms for real-even f .




4. Prime oscillation interpretation
Define the prime-power oscillation term


$$ P_f(t):=-2\sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}\,\widehat f(\log n)\cos(t\log n). $$


Then Proposition 1 reads Zf (t) = Af (t) + Pf (t).


Interpretation. The smoothed zero measure Zf is exactly the superposition of:


     1. a smooth Archimedean density term Af , and 2) a finite interference pattern of prime-power
        harmonics Pf .

Zero reconstruction mechanism (conditional)

If f ≥ 0 is unimodal and sharply peaked at 0, then Zf is a superposition of bumps centered at θρ . Under
RH, these are centered at the ordinates γ , making local maxima of Zf (t) (equivalently, minima of Pf (t)
after subtracting Af (t)) natural zero estimators.




                                                            3
5. Bandwidth–resolution–cost tradeoff
Let fL be a family with supp fL ⊂ [−L, L].


Proposition 2 (Bandwidth–resolution principle)

The effective temporal width satisfies Δt ≳ 1/L. To resolve individual zeros near height T , whose mean
spacing is approximately


$$ \Delta\gamma(T)\sim \frac{2\pi}{\log(T/2\pi)}, $$


one requires Δt ≪ Δγ(T ), hence


$$ L\gg \log T. $$


Proposition 3 (Bandwidth–cost tradeoff)

Because f (log n) vanishes for n > eL , reconstructing Zf at bandwidth L requires von Mangoldt data up
to n ≤ eL , i.e.


$$ \text{prime-power cutoff}\;N\asymp e^L. $$


In particular, resolving zeros at height T at the mean-spacing scale requires eL ≳ T , and computational
cost is dominated by generating Λ(n) up to N .




6. Numerical validation program

6.1 Deliverable A: explicit-formula verification

Kernel construction. Choose fL ∈ C0∞ ([−L, L]), even and real; define fL by inverse Fourier transform.


Compute three components independently.


     1. AfL (t): numerical quadrature of the Ψ-integral.
     2. PfL (t): finite von Mangoldt sum over n ≤ eL (prime powers included).
     3. ZfL (t): from tabulated zeros ρ (or ordinates γ under RH) up to cutoff Tmax .

Verify


$$ Z_{f_L}(t)\approx A_{f_L}(t)+P_{f_L}(t) $$


on a window t ∈ [T1 , T2 ], and record




                                                       4
$$ \epsilon(L,T_{\max})=\sup_{t\in[T_1,T_2]}\big|Z_{f_L}^{\text{zeros}}(t)-\big(A_{f_L}(t)+P_{f_L}(t)\big)\big|. $
$


Error controls.


      • Prime side: exact at truncation level n ≤ eL ; numerical error from floating-point evaluation of
       cos(t log n).
      • Zero-side truncation: for Schwartz fL , a safe tail control uses the zero counting measure dN :

$$ \sum_{|\gamma|>T_{\max}}|f_L(t-\gamma)|\;\lesssim\;\int_{T_{\max}}^{\infty}|f_L(u)|\,\log u\,du. $$


      • Quadrature error: controlled via adaptive integration.

6.2 Deliverable B: zero location accuracy

Detection kernels (relaxed smoothness). Fejér-type kernels are band-limited but not C ∞ :


$$ \widehat f_L(\xi)=\max\big(1-|\xi|/L,0\big). $$


These often yield robust bump-like reconstructions for detection.


Protocol.


     1. Compute ZfL (t) or PfL (t) on [T1 , T2 ].
     2. Detect candidate ordinates via maxima of ZfL (or minima of PfL after subtracting AfL ).
     3. Compare to known ordinates γn and measure mean/max error and detection rate.




7. Operator-theoretic outlook

7.1 Conjecture (self-adjoint trace realization; RH-strength)

Let W (f ) denote the Weil explicit-formula functional (the right-hand side of Proposition 1 evaluated at t =
0, or the corresponding distributional functional).

Conjecture 1. There exists a Hilbert space H, a self-adjoint operator H with discrete spectrum {γn } ⊂ R,
and a trace regularization Trreg such that for all even f with compactly supported f ,


$$ \operatorname{Tr}_{\mathrm{reg}}(f(H))=W(f). $$


This is RH-strength: a self-adjoint spectral realization would force the relevant spectral parameters to be
real.




                                                        5
7.2 Conditional positivity sanity check

Proposition 4 (conditional positivity). Assume Conjecture 1 holds and Trreg agrees with the usual trace on
positive trace-class operators. Then for all f ≥ 0 in the test class for which f (H) is trace-class,


$$ W(f)=\operatorname{Tr}_{\mathrm{reg}}(f(H))\ge 0. $$


This yields a necessary-condition numerical sanity check (dependent on the regularization).


7.3 Candidate operator: Berry–Keating with cutoff

Consider HBK = 12 (xp + px) with boundary/cutoff choices designed to yield a discrete or effectively
discrete spectrum. The research goal is to establish a controlled semiclassical trace approximation matching
W (f ) at leading order and to bound the remainder under a specific cutoff/regularization.



8. Conclusion
The prime-oscillation intuition can be stated rigorously: for band-limited test functions, a smoothed zero-
density is exactly the sum of an Archimedean gamma term and a finite von Mangoldt–weighted prime-
power interference pattern. This gives a principled route to zero reconstruction with explicit bandwidth–
resolution–cost tradeoffs and a clean numerical validation protocol. The operator-theoretic extension is
explicitly RH-strength and is therefore framed as a conjectural pathway rather than a proof.




Appendix A. Kernel construction examples
A standard smooth compactly supported bump:


$$ \widehat f_L(\xi)=\begin{cases} \exp!\left(-\frac{1}{1-(\xi/L)^2}\right),& |\xi|<L,\
0,& |\xi|\ge L. \end{cases} $$


Then define fL by inverse Fourier transform.


Detection kernels with relaxed smoothness (Fejér-type):


$$ \widehat f_L(\xi)=\max(1-|\xi|/L,0). $$




References
      • A. Weil, Sur les “formules explicites” de la théorie des nombres premiers, 1952.
      • A. Selberg, Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces, 1956.
      • A. Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, 1999.
      • M. V. Berry and J. P. Keating, The Riemann zeros and eigenvalue asymptotics, 1999.




                                                         6
     • H. L. Montgomery, The pair correlation of zeros of the zeta function, 1973.
     • A. M. Odlyzko, On the distribution of spacings between zeros of the zeta function, 1987.

Ryan Van Gelder © 2025 CC-NC-ND 4.0




                                                       7
