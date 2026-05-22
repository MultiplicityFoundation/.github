---
slug: entangled-aggregation-non-associativity-as-a-closure-defect-under-coarse-grained-composition
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Entangled Aggregation_ Non-associativity As A Closure Defect
    Under Coarse-grained Composition.md
  last_synced: '2026-03-20T17:17:20.032843Z'
---

Entangled Aggregation: Non-Associativity as a
Closure Defect under Coarse-Grained Composition
Abstract
Many “addition-like” operations fail to be strictly additive when units interact, merge, overlap, or otherwise
change their individuation upon contact. We formalize this by separating micro-level composition
(associative on a rich state space) from macro-level aggregation (performed after coarse-graining). We
show that non-associativity of the induced macro operation is a quantitative diagnostic of lost state
(memory / non-closure) introduced by coarse-graining. This yields a principled goal: find a minimal
augmented macrostate (x, c) that restores (approximate) associativity—equivalently, a minimal sufficient
statistic for compositional prediction.




1. Motivation and scope
Let x denote an observable used to “count” or “aggregate” a system. In interacting systems, an additive
baseline can be corrected by an interaction term


$$ x \oplus y = x + y + I(x,y). $$


When I  0, =
            associativity can fail and order of aggregation can matter. The central claim of this paper is:


        Non-associativity is not a pathology but a closure defect. It signals that the observable x
        is not a sufficient state to predict outcomes of sequential compositions.


We develop a two-layer formalism:


      • Micro layer: associative composition M on a microstate space Σ (or an associative convolution on
        distributions over Σ).
      • Macro layer: coarse-graining Φ : Σ → X yielding a macro observable x ∈ X .
      • Entangled aggregation: non-associativity of the induced macro composition is an observable of
        information loss under Φ.
      • Goal: identify a minimal augmentation (x, c) that restores associativity (closure).




2. Micro-to-macro setup

2.1 Microstate space and associative composition

Let Σ be a set of microstates. A (deterministic) micro-composition is a map




                                                       1
$$ \mathcal{M}: \Sigma\times\Sigma \to \Sigma, $$


assumed associative:


$$             \mathcal{M}(\mathcal{M}(\sigma_1,\sigma_2),\sigma_3)=\mathcal{M}(\sigma_1,\mathcal{M}
(\sigma_2,\sigma_3))\quad\forall\sigma_1,\sigma_2,\sigma_3\in\Sigma. $$


Stochastic micro-composition. More generally, let M be a Markov kernel M(⋅ ∣ σ1 , σ2 ) on Σ. It induces
an associative binary operation ⋆ on probability measures μ on Σ:


$$ \mu_1 \star \mu_2 := \text{Law}(\Sigma' ),\quad \Sigma'\sim\mathcal{M}(\cdot\mid \Sigma_1,\Sigma_2),\
\Sigma_i\sim\mu_i\ \text{independent}. $$


Associativity of M implies associativity of ⋆.


2.2 Coarse-graining and observables

A coarse-graining is a measurable map


$$ \Phi: \Sigma \to X, $$


with macro observable x = Φ(σ). Examples:


      • droplets: σ =size multiset; x = N (σ)=number of clusters;
      • graphs: σ =graph with edge weights; x=community count under a rule;
      • economics: σ =firm network; x=number of independent entities.




3. Induced macro composition and the associator

3.1 Deterministic closure (exact homomorphism)

We say Φ is closed (or homomorphic) for M if there exists ⊕ : X × X → X such that


$$                                                                                   \Phi\big(\mathcal{M}
(\sigma_1,\sigma_2)\big)=\Phi(\sigma_1)\oplus\Phi(\sigma_2)\quad\forall\sigma_1,\sigma_2\in\Sigma. $$


Proposition 1 (Associativity under closure). If M is associative and Φ is closed, then ⊕ is associative.


Proof sketch. Apply Φ to micro-associativity and use closure to rewrite both sides in terms of ⊕.




                                                      2
3.2 Stochastic setting: closure as sufficiency

In stochastic systems, exact closure rarely holds. Define the macro pushforward ν = Φ# μ for μ ∈ P(Σ). If
we had a canonical “lifting” L : P(X) → P(Σ) (a choice of representative micro-distribution consistent
with the macro one), we could define an induced macro operation on distributions:


$$ \nu_1 \boxplus \nu_2 := \Phi_#\big(\mathcal{L}(\nu_1)\star \mathcal{L}(\nu_2)\big). $$


Non-associativity typically arises because many micro-distributions share the same macro projection; i.e.,
the lifting is not unique and no low-dimensional macro state closes the dynamics.


3.3 The associator as a closure defect

For a binary operation ⊕ on X , define the associator


$$ \mathcal{A}(x,y,z):=(x\oplus y)\oplus z - x\oplus (y\oplus z) $$


when subtraction is meaningful (e.g., X ⊆ R), or more generally define a discrepancy on outcomes/
distributions:


$$ \mathcal{A}D(x,y,z):=D\big(\nu\big), $$},\nu_{x(yz)


for a probability-metric D (total variation, Wasserstein, etc.).


Interpretation. If micro-composition is associative, then A  0 indicates
                                                                    =         that the macro description is
missing state needed to predict future composition. In this sense, A is a quantitative memory diagnostic.




4. Restoring associativity via minimal augmented macrostate

4.1 Augmented coarse-graining

Let C be an auxiliary state space and define an augmented map


$$ \Psi: \Sigma\to Y:=X\times C,\quad \Psi(\sigma)=(\Phi(\sigma),\,C(\sigma)). $$


We seek C such that Ψ is (approximately) closed for M:


$$ \Psi(\mathcal{M}(\sigma_1,\sigma_2)) \approx G\big(\Psi(\sigma_1),\Psi(\sigma_2)\big) $$


for some binary operator G on Y . When this holds, the induced macro operation on Y is (approximately)
associative, and the original non-associativity is explained as loss of c.




                                                         3
4.2 Minimality criteria

There are multiple legitimate notions of “minimal” c:


     1. State-space minimality: minimize ∣C∣ (finite case) subject to A below tolerance.
     2. Information minimality: minimize mutual information I(Σ; C) subject to approximate associativity
        (an information bottleneck view).
     3. Predictive sufficiency: c is sufficient if, conditional on (x, c), the distribution of the next coarse-
         grained outcome is independent of the fine microstate.

In Markovian settings, this connects directly to lumpability: a partition/coarse-graining produces a
Markovian reduced chain iff certain consistency conditions hold; failure implies memory that can be
repaired only by augmenting the state.




5. Phenomenological interaction terms and cocycle constraints
Assume X is an abelian group under + and define


$$ x\oplus y = x+y+I(x,y). $$


Then ⊕ is associative if and only if I satisfies the cocycle-like identity


$$ I(x,y)+I(x\oplus y,z)=I(y,z)+I(x,y\oplus z). $$


Thus:


        • I  0 does
                = not imply non-associativity;
        • non-associativity is the obstruction to solving this identity within the chosen closure.

This ties entangled aggregation to classical cocycle equations in group extensions/cohomology and to
associative functional equation theory.




6. Measurement and identification: “associator spectroscopy”
A practical workflow that applies across physical and social domains:


     1. Choose a macro observable x = Φ(σ) (e.g., cluster count).
     2. Design a 3-step composition protocol producing two parenthesizations: ((x ⊕ y) ⊕ z) vs (x ⊕
         (y ⊕ z)).
     3. Measure the associator in mean and/or distribution:
     4. mean: AE = E[X(xy)z ] − E[Xx(yz) ];
     5. distribution: AD = D(ν(xy)z , νx(yz) ).
     6. Hypothesize candidate hidden state features c and fit an augmented model (x, c).
     7. Validate closure by reduction of A across controlled perturbations.




                                                          4
A key prediction:


       ∣A∣ typically grows with heterogeneity in latent interaction-relevant features (size dispersion,
       overlap, connectivity) and shrinks when interactions are suppressed (e.g., surfactants
       preventing coalescence).




7. Canonical example: coalescence / coagulation
Let σ encode a multiset of cluster masses {mi } (total mass conserved). Micro-dynamics merge two clusters
at a rate/kernel K(mi , mj ). The classical mean-field limit yields Smoluchowski-type coagulation equations.


      • Macro observable: x = N (σ) (number of clusters).
      • Natural candidate augmentation: c = a low-dimensional summary of the size distribution (e.g.,
                        p
       moments ∑i mi , or quantiles).

The framework predicts non-associativity in N -aggregation whenever the merge kernel depends on sizes
so that early merges reshape the distribution and alter future merge rates.




8. Connections and positioning
This formalism sits at the intersection of:


      • Nonextensive statistics / deformed algebras: generalized sums capture correlations (e.g., q -
        addition).
      • Aggregation function theory: associative aggregation operators (t-norms, conorms, uninorms)
        provide a contrasting “closed” universe where associativity is axiomatic.
      • Coarse-graining & renormalization: effective theories acquire new couplings after coarse-graining;
        here the associator is a fast diagnostic of missing effective state.
      • Markov coarse-graining: lumpability characterizes when coarse-grained dynamics remain Markov;
        failure corresponds to memory that c must encode.
      • Compositional stochastic processes: open Markov processes can be composed; coarse-graining
        interacts nontrivially with composition.
      • Cocycle/cohomology viewpoints: associativity constraints translate into cocycle equations for
        interaction terms.




9. Summary of contributions
     1. A two-layer definition of entangled aggregation: associative micro-composition M, coarse-graining
        Φ, and non-associativity of induced macro operation as a measurable closure defect.
     2. A principled objective: find minimal augmentation (x, c) that restores associativity (closure) and
       thereby identifies the missing state.




                                                      5
    3. A practical validation scheme (“associator spectroscopy”) based on 3-step composition experiments
       and distributional discrepancy measures.




References (selected)
     • D. J. Aldous, Deterministic and stochastic models for coalescence (aggregation and coagulation): a review
       of the mean-field theory for probabilists, Bernoulli 5(1):3–48 (1999).
     • J. C. Baez, B. Fong, B. Pollard, Coarse-graining open Markov processes, (2018).
     • G. Beliakov, A. Pradera, T. Calvo, Aggregation Functions: A Guide for Practitioners, Springer (2007).
     • E. P. Borges, A possible deformed algebra and calculus inspired in nonextensive thermostatistics, Physica
       A 340:95–101 (2004).
     • K. S. Brown, Cohomology of Groups, Springer (1982).
     • J. G. Kemeny and J. L. Snell, Finite Markov Chains, Van Nostrand (1960); reprint Springer (1983).
     • E. P. Klement, R. Mesiar, E. Pap, Triangular Norms, Springer (2000).
     • M. N. Jacobi, C. Pantazis, I. M. J. Hall, Coarse graining Markov chains by partitioning / strong lumpability,
       arXiv:0710.1986 (2007/2008).
     • M. Smoluchowski, Drei Vorträge über Diffusion, Brownsche Molekularbewegung und Koagulation von
       Kolloidteilchen, Physikalische Zeitschrift (1916).
     • C. Tsallis, Possible generalization of Boltzmann–Gibbs statistics, Journal of Statistical Physics 52:479–
       487 (1988).
     • K. G. Wilson, Renormalization group and critical phenomena. I. Renormalization group and the Kadanoff
       scaling picture, Physical Review B 4(9):3174–3183 (1971).
     • C. A. Weibel, An Introduction to Homological Algebra, Cambridge University Press (1994) (see group
       homology/cohomology chapter).

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                         6
