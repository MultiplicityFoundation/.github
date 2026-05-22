---
slug: modal-numerosity-as-algorithmic-inference-camera-ready-package
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Modal Numerosity As Algorithmic Inference \u2014 Camera-ready\
    \ Package.md"
  last_synced: '2026-03-20T17:17:21.036573Z'
---

Modal Numerosity as Algorithmic Inference
A consolidated, camera-ready document compiling the formal framework, core theorems, tail bounds, structural
restrictions, code snippets, and a research/validation roadmap.




Abstract
We develop modal numerosity: a quantitative semantics for questions of the form “How many P -things
could there have been?” by pushing a world-measure \\lambda\ forward along a count functional \N\_P\.
The key technical move is to constrain \\lambda\ via effectivity and (optionally) structural axioms
(factorization, additivity, replication), yielding a nontrivial, mathematically characterizable space of
attainable count distributions. We prove: (i) closure of count distributions under computable pushforwards,
(ii) tail bounds for toy ecological numerosity under explicit prefix-code-like priors (polylog tails for Elias–
delta-style priors; polynomial tails for power priors), and (iii) a structural restriction theorem showing that
factorization + additivity impose convolution constraints. The framework generates empirical predictions
(e.g., compressibility effects, tail-decay signatures) testable against graded human modal judgments.




1. Formal Framework

1.1 Effectivity prerequisites

      • A function \f:\mathbb N\to \mathbb R\_{\ge 0}\ is lower semicomputable (l.s.c.) if there exists a
        computable \g:\mathbb N\times\mathbb N\to \mathbb Q\_{\ge 0}\ such that for each \n\, \g(n,k)\ is
        nondecreasing in \k\ and \g(n,k)\uparrow f(n)\ as \k\to\infty\.


      • A semimeasure on a countable set \X\ is a function \m\:X\to[0,1]\ with \\sum\_{x\in X} m(x)\le 1\. If
        equality holds, it is a probability measure.


1.2 World space and laws

Let \W\ be a countable set of worlds/descriptions equipped with an effective presentation: a fixed
bijection \\nu:\mathbb N\to W\.


A law \L\ is a probability mass function on \W\ that is lower semicomputable pointwise: there exists a
computable \h:\mathbb N\times\mathbb N\to\mathbb Q\_{\ge0}\ such that


$$ h(j,t)\uparrow L(\nu(j))\quad\text{as }t\to\infty, $$


with \\sum\_j L(\nu(j))=1\.


Let \\mathcal M={L\_0,L\_1,\dots}\ be a computably enumerable family of laws.




                                                           1
Let \\pi:\mathbb N\to[0,1]\ be a lower semicomputable prior over laws with \\sum\_i \pi(i)\le 1\. Let \\pi\_s(i)\
be a computable rational approximation with \\pi\_s(i)\uparrow\pi(i)\.


1.3 Mixture semimeasure

Define the mixture semimeasure \\lambda\ on \W\ by


$$ \lambda(w)=\sum_{i\in\mathbb N}\pi(i)\,L_i(w). $$


Then \\sum\_{w\in W}\lambda(w)\le 1\.


1.4 Count functionals and pushforward

Let \N\:W\to\mathbb N\cup{\infty}\ be computable relative to the presentation (i.e., \N(\nu(j))\ is
computable from \j\). The induced count distribution (pushforward) is


$$ \lambda_N(n)=\lambda({w\in W: N(w)=n}). $$


Define tail \\tau(n)=\sum\_{k\ge n} \lambda\_N(k)\.




2. The Restriction Theorem (Effectivity Closure)

Theorem 1 (Closure under computable pushforwards)

If \N\ is computable, then \\lambda\_N\ is a lower semicomputable semimeasure on \\mathbb
N\cup{\infty}\.


Proof (sketch with full effectivity bookkeeping). For each \i,n\, because \L\_i\ is l.s.c. and \N\ is
computable, the mass


$$ L_i(N=n) := L_i({w: N(w)=n}) $$


is l.s.c. uniformly in \i,n\. Let \g(i,n,s)\uparrow L\_i(N=n)\ be a computable rational approximation.


Define


$$ G(n,s)=\sum_{i=0}^s \pi_s(i)\,g(i,n,s). $$


Then \G(n,s)\ is computable, nondecreasing in \s\, and \G(n,s)\uparrow \lambda\_N(n)\ as \s\to\infty\. Hence
\\lambda\_N\ is l.s.c. The semimeasure property follows from \\sum\_n\lambda\_N(n)=\sum\_w\lambda(w)
\le1\. ∎




                                                        2
Corollary 2 (Non-attainability via non-l.s.c.)

If a semimeasure \q\ on \\mathbb N\ is not lower semicomputable, then it cannot be represented as \
\lambda\_N\ for any computable-mixture construction above.


Concrete example. Let \A\subseteq\mathbb N\ be non-recursively enumerable. Define


$$ q(n) = c\,2^{-n}\,\mathbf 1_A(n), $$


with \c\ chosen to make \\sum\_n q(n)\le 1\. If \q\ were l.s.c., one could enumerate \A\ by waiting until the
lower approximation to \q(n)\ exceeds a rational threshold, contradicting non-r.e.-ness of \A\. ∎




3. Language-Relative Invariance (Type vs Token)
Let \\mathcal L\ be a modal/first-order language used to describe worlds, and let \P\ be \\mathcal L\-
definable without haecceitistic constants.


Lemma (Definable numerosity is isomorphism invariant)

If \w\cong\_{\mathcal L} w'\ (L-isomorphism), then \N\_P(w)=N\_P(w')\.


Consequence. For qualitative numerosity questions phrased in haecceity-free \\mathcal L\, only the
induced measure on \\mathcal L)-types (isomorphism classes / elementary equivalence classes, as
appropriate) can affect \\(\lambda\_{N\_P}\. Token-multiplicity within a type is invisible unless \\mathcal L\
can name individuals rigidly.




4. Tail Bounds under Explicit Priors (Toy Ecology)

4.1 Ecology model

A law \L=(S,E,\eta)\ has:


- $$ $$ - $$ $$ - $$ $$


Define capacity


$$ N_{\max}(L)=\min\big(S^2,\lfloor E/\eta\rfloor\big). $$


Within-law models:


      • Model B (capacity): \N=N\_{\max}(L)\
      • Model A (uniform): \N\mid L\sim\mathrm{Unif}{0,\dots,N\_{\max}(L)}\

Prior factorizes:



                                                      3
$$ \pi(L)=\pi_S(S)\,\pi_E(E)\,\pi_\eta(\eta). $$


Define tail \\tau(n)=\Pr(N\ge n)\ under the mixture.


4.2 Dominance and factorization

Lemma 3 (Dominance). \\tau\_A(n)\le \Pr(N\_{\max}\ge n)=\tau\_B(n)\.


Lemma 4 (Factorization with η ).


$$ \Pr(N_{\max}\ge n)\le \Pr\big(S\ge\lceil\sqrt n\rceil\big)\cdot\sum_{\eta=1}^{\eta_{\max}}\pi_\eta(\eta)\,
\Pr(E\ge n\eta). $$


Corollary 5 (coarse bound). Since \\Pr(E\ge n\eta)\le\Pr(E\ge n)\,


$$ \Pr(N_{\max}\ge n)\le \Pr\big(S\ge\lceil\sqrt n\rceil\big)\cdot\Pr(E\ge n). $$


4.3 Elias–delta-style priors and polylog tails

Assume for \x\ge 3\:


$$ \pi_S(x)\le \frac{C_S}{x(\log x)^2},\qquad \pi_E(x)\le \frac{C_E}{x(\log x)^2}. $$


(Here \\log\ is natural log; changing base only changes constants.)


Lemma 6 (tail estimate). For \m\ge 3\,


$$ \sum_{x\ge m}\frac{1}{x(\log x)^2}\le \frac{1}{\log(m-1)}. $$


Theorem 7 (polylog tail bound; corrected constants). For \n\ge 16\,


$$ \tau_B(n)\le \frac{C}{(\log n)^2}\quad\text{with }C=8C_SC_E. $$


Consequently \\tau\_A(n)\le C/(\log n)^2\.


Proof (sketch). From Cor. 5 and Lemma 6:


      • For \n\ge 16\, \\Pr(S\ge\lceil\sqrt n\rceil)\le 4C\_S/\log n\.
      • For \n\ge 4\, \\Pr(E\ge n)\le 2C\_E/\log n\. Multiply to get \\le 8C\_SC\_E/(\log n)^2\. Use Lemma 3 for
        Model A. ∎

4.4 Coding sensitivity: polynomial priors

Theorem 8 (power priors imply polynomial tails). If \\pi\_S(x)\le C\_S/x^\alpha\ and \\pi\_E(x)\le C\_E/
x^\alpha\ for some \\alpha>1\, then




                                                         4
$$ \tau_B(n)=O\big(n^{-\tfrac{3}{2}(\alpha-1)}\big). $$


(And \\tau\_A(n)\le\tau\_B(n)\.)




5. Structural Restrictions: Factorization ⇒ Convolution Constraints

5.1 Convolution framework

Let \(W,\otimes)\ be a commutative monoid modeling composition of independent subsystems.


Assume:


     1. Additivity: \N(w\otimes w')=N(w)+N(w')\.
     2. Factorization (within a law): for independent measurable sets \A,B\, $$ $$
     3. Replication closure: for each \L\ and \k\ge1\, there is \L^{(k)}\ whose induced measure is the
        pushforward of \\mathbb P\_L^{\otimes k}\ along \\otimes\:W^k\to W\.

Let \p\_L=(N)\_\*\mathbb P\_L\ be the count distribution under \L\.


Theorem 9 (Convolution constraint)

$$ p_{L^{(k)}}=p_L^{*k}\quad\text{(k -fold convolution).} $$


Thus any mixture \\lambda\_N=\sum\_L\pi(L)p\_L\ lies in the convex hull of a convolution-closed family.


Corollary 10 (Structural non-attainability)

Any target distribution on \\mathbb N\ that cannot arise as a convex mixture of distributions obeying the
convolution/replication constraints is unattainable under these structural axioms.


Interpretation. This is where “structure” bites harder than effectivity alone: effectivity permits all l.s.c.
semimeasures in principle (via degenerate laws), but factorization + additivity + replication exclude many
such constructions.




6. Attainability Landscape

Theorem 3.1 (Unrestricted attainability = all l.s.c. semimeasures)

If \\mathcal M\ is unrestricted enough to include point-mass (degenerate) laws \L\_n\ supported on a single
designated world \w\_n\ with \N(w\_n)=n\, then the attainable \\lambda\_N\ are exactly the l.s.c.
semimeasures on \\mathbb N\.


      • (⇒) follows from Theorem 1.
      • (⇐) given any l.s.c. semimeasure \q\, set \\pi(n)=q(n)\ and use degenerate \L\_n\.




                                                          5
Structural regime

With structural restrictions (e.g., Theorem 9’s axioms), attainable distributions form a proper subset.
Characterizing this subset under additional locality/invariance assumptions is a principal open problem.




7. Empirical Predictions and Validation

7.1 Predictions

    1. Tail-decay signatures distinguish priors:


    2. Elias–delta-style: \\tau(n)\lesssim (\log n)^{-2}\ (polylog)


    3. Power priors: \\tau(n)\lesssim n^{-\beta}\ (polynomial)

    4. Similarity/exponential: \\tau(n)\approx e^{-cn}\ or faster


    5. Compressibility spikes: if numerosity is encoded directly in a simplicity-biased prior, “round” \n\
       (powers of 2/10, etc.) may receive elevated modal ease unless smoothed by the law/typicality layer.


    6. Moderator effects: education/language may change the effective coding people use for numbers,
      modulating compressibility effects.


7.2 Minimal experiment sketch

     • Prompt: “How easily could there have been at least \n\ ravens?” (slider)
     • Use matched-magnitude pairs (e.g., 1024 vs 997; 1,000,000 vs 983,041)
     • Model ratings as monotone transform of \\tau(n)\ plus compressibility predictors




8. Open Problems
    1. Exact structural characterization: for given axioms (factorization/locality/invariance), characterize
       attainable \\lambda\_N\.
    2. Smoothing the prior: formal conditions under which the law/typicality split removes numeral-
       encoding spikes.
    3. Beyond discrete worlds: extend to measurable spaces \W\ via computable measure theory.




Appendix A: Minimal Code Snippets

  import numpy as np

  def compute_tau_capacity(prior_S, prior_E, S_max=1000, E_max=1000, eta_max=1):




                                                         6
    """Compute τ_B(n)=Pr(N>=n) where N=Nmax=min(S^2, floor(E/eta)).

   This returns tau[n] = Pr(Nmax >= n). No extra tail transform is needed.
   """
   maxN = min(S_max**2, E_max//1)
    tau = np.zeros(maxN + 1, dtype=float)
    total_w = 0.0

    # simple factorized prior over S,E; optionally mix over eta
    etas = np.arange(1, eta_max + 1)
    w_eta = np.ones_like(etas, dtype=float) / len(etas)

    for S in range(1, S_max + 1):
        wS = prior_S(S)
        S2 = S * S
        for E in range(1, E_max + 1):
            wE = prior_E(E)
            wSE = wS * wE
            for eta, weta in zip(etas, w_eta):
                Nmax = min(S2, E // eta)
                w = wSE * weta
                tau[:Nmax + 1] += w
                total_w += w

    tau /= total_w
    return tau



import numpy as np

def compute_pmf_and_tail_capacity(prior_S, prior_E, S_max=1000, E_max=1000,
eta_max=1):
    maxN = min(S_max**2, E_max)
    pmf = np.zeros(maxN + 1, dtype=float)
    total_w = 0.0

    etas = np.arange(1, eta_max + 1)
    w_eta = np.ones_like(etas, dtype=float) / len(etas)

    for S in range(1, S_max + 1):
        wS = prior_S(S)
        S2 = S * S
        for E in range(1, E_max + 1):
            wE = prior_E(E)
            wSE = wS * wE
            for eta, weta in zip(etas, w_eta):
                Nmax = min(S2, E // eta)




                                       7
                     w = wSE * weta
                     pmf[Nmax] += w
                     total_w += w

      pmf /= total_w
      tail = np.cumsum(pmf[::-1])[::-1]
      return pmf, tail


A.3 Example priors


 import numpy as np

 def elias_delta_style_prior(x, C=1.0):
     """Proxy for 2^{-ℓ_delta(x)} up to constants: ~ 1/(x (log x)^2) for x>=3."""
     if x < 3:
         return C / max(1, x)
     return C / (x * (np.log(x) ** 2))

 def power_prior(x, alpha=2.0, C=1.0):
     return C / (x ** alpha)




Appendix B: External References (selected)

Algorithmic information / universal priors

    • A. N. Kolmogorov — Foundations of algorithmic complexity (original papers; standard anthologies).
    • R. J. Solomonoff — A formal theory of inductive inference (Parts I & II).
    • L. A. Levin — Universal search / universal semimeasures.
    • M. Li & P. Vitányi — An Introduction to Kolmogorov Complexity and Its Applications.
    • M. Hutter — Universal Artificial Intelligence: Sequential Decisions based on Algorithmic Probability.

Prefix-free codes for integers

    • P. Elias — Universal codeword sets and representations of the integers.

Computable analysis / computable measures

    • K. Weihrauch — Computable Analysis.
    • V. Brattka, P. Hertling, K. Weihrauch (eds.) — Handbook of Computability and Complexity in Analysis.

Modal semantics and measure

    • D. Lewis — On the Plurality of Worlds (modal realism; similarity orderings; counterpart theory).
    • Standard texts on probabilistic/graded modality in formal semantics and epistemology (for measure-
      on-worlds frameworks).




                                                     8
Citizen Gardens © 2025 CC-NC-ND 4.0




                                      9
