---
slug: quantum-musicality-math-clean-version
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/musicality/Quantum Musicality - Math Clean Version.md
  last_synced: '2026-03-20T17:17:18.874671Z'
---

Quantum Musicality and Multiplicity Dynamics: A
Formal Framework
1. Preliminaries and Notation

1.1 Time and Index Sets

     • Time is discrete:
       t ∈ Z≥0 .
     • Voices (or parts) are indexed by
       V = {1, 2, … , K}.
     • Each voice k ∈ V has an associated feature dimension d ∈ N.

1.2 Musical Feature Space

For each voice k ∈ V and time t, define a musical state vector


                                                  ρk (t) ∈ Rd .

The components of ρk (t) may encode, for example:


     • pitch class or pitch height
     • onset density or rhythmic position
     • dynamic level (e.g., MIDI velocity)
     • timbral or spectral descriptors

The global state at time t is the concatenation


                                     ρ(t) = (ρ1 (t), … , ρK (t)) ∈ RKd .

We also allow an external input term


                                                  Ik (t) ∈ Rd ,

representing performer input, user gestures, or environmental signals. Let

                                     I(t) = (I1 (t), … , IK (t)) ∈ RKd .


2. Multiplicity Dynamics

2.1 Coupled Update Equation

We define a family of coupled nonlinear difference equations governing the evolution of ρ(t). For each
voice k ∈ V ,




                                                       1
                                                                   K
           ρk (t + 1) = ρk (t) + Δt (Ak ρk (t) + Bk Ik (t) + ∑ Γkj S(ρk (t), ρj (t)) + Rk (ρ(t))).
                                                                  j=1

Here:


        • Δt > 0 is a fixed time step.
        • Ak ∈ Rd×d and Bk ∈ Rd×d are local linear operators.
        • Γ = (Γkj ) ∈ RK×K is a coupling matrix between voices.
        • S : Rd × Rd → Rd is a smooth interaction function.
        • Rk : RKd → Rd is a global regularization or constraint term.

The system can be written compactly as


                                     ρ(t + 1) = ρ(t) + Δt F (ρ(t), I(t); θ),

where θ denotes the collection of parameters (Ak , Bk , Γ, S, Rk ).


2.2 Phase-Coupled Interactions

For many musical applications it is useful to introduce a phase associated with each voice. Let


                                            θk (t) = Θ(ρk (t)) ∈ R/2πZ

be a derived phase, for example computed from pitch-class or metrical position. A simple phase-coupled
interaction is given by

                                         S(ρk , ρj ) = Hk (ρk ) cos (θk − θj ),

where Hk : Rd → Rd is a smooth function. In this case, the update equation becomes

                                                           K
 ρk (t + 1) = ρk (t) + Δt (Ak ρk (t) + Bk Ik (t) + ∑ Γkj Hk (ρk (t)) cos (θk (t) − θj (t)) + Rk (ρ(t))).
                                                          j=1


This form captures synchronization and desynchronization effects between voices in a mathematically
explicit way.


3. Prime-Based Encoding of Musical Structures

3.1 Basic Encoding

Fix a finite set of distinct prime numbers


                                               P = {p1 , p2 , … , pM }.

Let A be a finite set of musical atoms, for example pitch classes or pitch–duration pairs. Choose an
injective map

                                                     ϕ : A → P.



                                                           2
For a finite multiset X = {a1 , … , ar } of atoms in A, define the prime encoding

                                                      r
                                         Φ(X) = ∏ ϕ(ai ) ∈ N≥1 .
                                                     i=1


Typical examples:


     • A chord is encoded as the product of the primes assigned to its constituent pitch classes.
     • A rhythmic pattern can be encoded by assigning primes to time positions and multiplying.

3.2 Factorization Vectors and Distances

Every integer n ≥ 1 has a unique prime factorization of the form

                                           M
                                     n = ∏ pemm (n) ,          em (n) ∈ Z≥0 .
                                          m=1

Define the factorization vector

                                    e(n) = (e1 (n), … , eM (n)) ∈ ZM
                                                                   ≥0 .


For two encoded objects n, m ∈ N≥1 , define a distance


                                       dp (n, m) = e(n) − e(m) ,

where ∥ ⋅ ∥ is any norm on RM (e.g. ℓ1 or ℓ2 ). This induces a distance between chords or other encoded
structures.


3.3 Prime-Based Potentials in the Dynamics

Suppose each voice k at time t plays a chord Ck (t) or other encoded object with prime code nk (t) =
Φ(Ck (t)). Define a prime potential for voice k :

                                                K
                                     Uk (t) = ∑ wkj dp (nk (t), nj (t)),
                                               j=1

where wkj ∈ R are coupling weights. A simple way to incorporate this into the dynamics is to set

                                        Rk (ρ(t)) = −∇ρk Ψk (ρ(t)),

where

                                            Ψk (ρ(t)) = η Uk (t)

for some scalar η ∈ R, and where the dependence of nk (t) on ρk (t) is made explicit through a
differentiable decoding from ρk (t) to chord selection. This couples the continuous dynamics of ρ(t) to the
discrete prime-coded structure.




                                                           3
4. Tensor-State Representation of Polyphonic Texture

4.1 Configuration Space

Let C denote a finite set of configurations. A configuration may represent, for example, a K -voice chord
with discretized features:


                                             C = {c1 , c2 , … , cN }.

Each configuration cn may be associated with a prime code Φ(cn ).


Define a complex vector space


                                                     H = CN

with canonical basis {∣cn ⟩}N
                            n=1 . A texture state at time t is a vector

                                                       N
                                           ∣ψ(t)⟩ = ∑ αn (t)∣cn ⟩,
                                                      n=1

with complex amplitudes αn (t) ∈ C. We impose the normalization

                                                N
                                               ∑ αn (t)
                                                            2
                                                                = 1,
                                               n=1

so that ∣αn (t)∣2 can be interpreted as a probability distribution over configurations.


4.2 Linear Texture Evolution

A simple linear, norm-preserving update rule for the texture state is


                                            ∣ψ(t + 1)⟩ = U ∣ψ(t)⟩,

where U ∈ CN ×N is a unitary matrix.


More generally, one may allow a parameterized family U (θ), with parameters learned from data. The
parameters may be constrained to maintain (approximate) unitarity or may be allowed to deviate for
dissipative behavior.


4.3 Connecting Tensor-State and Feature Dynamics

The feature dynamics and texture dynamics can be coupled by defining a mapping


                                                Ξ : RKd → H,

which associates a feature state ρ(t) to a texture state ∣ψ(t)⟩. For example, Ξ could be implemented as a
neural network followed by a softmax-like normalization to produce ∣αn ∣2 .




                                                        4
Conversely, one can define a decoding map


                                                Π : H → RKd ,

which maps a texture state to expected feature values. A simple choice is

                                                      N
                                         Π(∣ψ⟩) = ∑ αn f (cn ),
                                                               2

                                                     n=1

where f : C → RKd assigns a feature vector to each configuration.


Coupled dynamics can then be written as


     ρ(t + 1) = ρ(t) + Δt F (ρ(t), I(t); θ) + G(∣ψ(t)⟩), ∣ψ(t + 1)⟩         = U (θ′ )∣ψ(t)⟩ + H(ρ(t)),

where G and H are coupling terms and θ, θ ′ are parameter sets.


5. Coherence and Superposition

5.1 Coherence Measure

Given a texture state ∣ψ(t)⟩, define its density matrix


                                           ρtex (t) = ∣ψ(t)⟩⟨ψ(t)∣.

In the configuration basis, this is an N × N matrix with entries

                                         (ρtex (t))nm = αn (t) αm (t).

A simple coherence functional is


                                       C(ρtex (t)) = ∑ (ρtex (t))nm .
                                                     n       =m

This quantity is large when the state is a superposition of many basis configurations and small when the
state is close to a basis vector.


5.2 Coherence-Controlled Dynamics

Coherence can be incorporated into the dynamics through a term that depends on C . For example, define


                                      Rk (ρ(t)) = −∂ρk (λ C(ρtex (t))),

with λ ∈ R a scalar parameter. Depending on the sign of λ, the system can be biased toward more
coherent (superposed) states or more localized (basis-like) states.




                                                          5
6. Learning and Parameter Estimation

6.1 Data and Loss Function

Let {x(s) (t)} denote a collection of observed musical sequences, where s indexes sequences and t indexes
time. Each observation is mapped to feature states


                                           ρ(s) (t) = E(x(s) (t)) ∈ RKd ,

via an encoding map E .


Given a parameter set Θ (including θ, θ ′ , U , and any parameters of E, Ξ, Π), define the model-predicted
state ρ(s) (t) by iterating the dynamics from an initial condition. A generic loss function may have the form


                       L(Θ) = ∑ ∑ (ℓ(ρ(s) (t), ρ(s) (t)) + λ1 R1 (Θ) + λ2 R2 (ρ(s) (t))),
                                 s   t

where:


     • ℓ is a data-fit term (e.g., squared error or negative log-likelihood after decoding).
     • R1 is a parameter regularizer.
     • R2 penalizes or encourages certain dynamical behaviors (e.g., prime-structure alignment or
       coherence).

Optimization can be performed by gradient-based methods, provided all components are differentiable (or
subdifferentiable).


6.2 Prime and Coherence Regularization

Two specific regularization terms are:


    1. Prime-structure regularization:


                                         Rprime = ∑ ∑ μkj dp (nk (t), nj (t)),
                                                                   (s)      (s)

                                                   s,t   k,j

                 (s)
         where nk (t) are prime encodings derived from the decoded chords and μkj are weights.


    2. Coherence regularization:


                                               Rcoh = ∑ g(C(ρtex (t))),
                                                                  (s)

                                                           s,t

         where g : R≥0 → R≥0 is a chosen function (e.g., linear or quadratic).


These terms allow explicit control over harmonic relationships (via prime encodings) and textural
superposition (via coherence).




                                                           6
7. Example Implementation Outline
A minimal implementation consistent with the framework proceeds as follows.


    1. Encoding:
    2. Map raw symbolic data (e.g., MIDI) to feature vectors ρ(t) using a fixed encoding E .

    3. Assign primes to pitch classes and encode chords as integers via Φ.


    4. Dynamics:


    5. Initialize parameters Ak , Bk , Γ, and functions Hk .

    6. Implement the update


      ρk (t + 1) = ρk (t) + Δt (Ak ρk (t) + Bk Ik (t) + ∑ Γkj Hk (ρk (t)) cos(θk (t) − θj (t)) − ∇ρk Ψk (ρ(t))),
                                                               j

      with Ψk incorporating prime-based potentials.


    7. Texture State (Optional):


    8. Define a finite configuration set C and maps Ξ and Π.
    9. Initialize ∣ψ(0)⟩ and unitary U .

   10. Update ∣ψ(t)⟩ via ∣ψ(t + 1)⟩ = U ∣ψ(t)⟩.


   11. Decoding:


   12. From ρ(t), decode discrete musical events (e.g., chords, notes) by a deterministic or probabilistic
      map.

   13. From ∣ψ(t)⟩, sample configurations cn with probability ∣αn (t)∣2 , if the texture representation is
      used.


   14. Training and Evaluation:


   15. Fit parameters Θ by minimizing L(Θ) on a corpus.
   16. Compare generated sequences with baselines (e.g., Markov or recurrent models) using both
       quantitative metrics and listening tests.


8. Discussion
The framework above specifies:


     • A concrete state space for multi-voice musical systems.
     • Explicit discrete-time dynamics incorporating local, coupled, and regularizing terms.




                                                       7
     • A prime-based encoding with a clear induced distance and associated potentials.
     • A tensor-state representation that captures textural superposition and coherence.
     • A learning and evaluation strategy based on standard optimization and comparison to baselines.

All components are defined so that they can be instantiated algorithmically and subjected to empirical
evaluation.




                                                   8
