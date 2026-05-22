---
slug: peqbsa-prime-on-coefficients-formulation-revised
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Peqbsa (prime-on-coefficients Formulation) \u2014 Revised.md"
  last_synced: '2026-03-20T17:17:20.338811Z'
---

The Prime-Embedded Quantum Bargmann–Segal
Algorithm (PEQBSA)
Corrected “prime-on-coefficients” formulation
The Prime-Embedded Quantum Bargmann–Segal Algorithm (PEQBSA) introduces prime-structured
modulation into the Bargmann–Segal (Segal–Bargmann / Fock-space) phase-space formalism.


Key correction: in a Bargmann–Segal holomorphic state function ψ(z), primes cannot multiply ψ “directly”
via an undefined index n. Instead, prime structure must act on the Fock/Taylor coefficients {ψn }, i.e., on
the natural discrete label n of the number (Fock) basis.




Structure of Prime-Embedded Quantum Bargmann–Segal
Algorithm (PEQBSA)
The structure of PEQBSA includes the following components:


     • Prime-Encoded Bargmann–Segal Representation
     • Prime-Modulated Coherent States and Quantum Amplitudes
     • Prime-Weighted Time Evolution and Propagation
     • Prime-Controlled Quantum State Overlap and Inner Product
     • Applications in Quantum Optics, Quantum Computing, and Phase Space Methods




1. Prime-Encoded Bargmann–Segal Representation
In the Bargmann–Segal formalism, quantum states are represented by holomorphic functions on complex
phase space. The discrete Fock index n appears naturally through the Taylor/Fock expansion.


Bargmann–Segal State Representation
Let ∣ψ⟩ be a (single-mode) bosonic quantum state with Fock expansion

                                           ∞               ∞
                                   ∣ψ⟩ = ∑ ψn ∣n⟩,         ∑ ∣ψn ∣2 = 1.
                                          n=0              n=0


The corresponding Bargmann–Segal holomorphic function is




                                                      1
                                                  ∞
                                                            zn
                                     ψ(z) = ∑ ψn                ,         z ∈ C.
                                              n=0            n!

Equivalently, the coefficients are recovered by

                                                      1  dn
                                         ψn =                 ψ(z)     .
                                                      n! dz n      z=0


Prime-Encoded Bargmann–Segal State (prime-on-coefficients)
Define a prime-derived weight sequence wn (built from primes in any desired way). The prime embedding
is implemented by the diagonal (number-basis) modulation operator

                                                        ∞
                                           Mw := ∑ wn ∣n⟩⟨n∣.
                                                        n=0

The prime-embedded state is
                                                                ∞
                                     ∣ψw ⟩ := Mw ∣ψ⟩ = ∑(wn ψn ) ∣n⟩.
                                                                n=0

In Bargmann–Segal form, this is simply
                                                                    ∞
                                                                               zn
                                  ψw (z) := (Mw ψ)(z) = ∑ wn ψn                    .
                                                                    n=0         n!

Notes on physical realizability

     • If ∣wn ∣ = 1 for all n, then Mw is unitary (a physically valid closed-system gate).
     • If ∣wn ∣  1 (e.g.,
                        =wn = p(n) growing with n), then Mw is non-unitary and must be interpreted as a
       filter / postselected / dissipative operation, typically requiring truncation and renormalization.




2. Prime-Modulated Coherent States and Quantum
Amplitudes
Coherent states play a central role in quantum optics and continuous-variable quantum information. In
PEQBSA, primes modulate coherent states by acting on their Fock coefficients.


Coherent States
A coherent state ∣α⟩ (α ∈ C) has the Fock expansion




                                                            2
                                                                  ∞
                                                       ∣α∣2       αn
                                         ∣α⟩ = e− 2 ∑                 ∣n⟩.
                                                              n=0  n!

Its Bargmann–Segal function is therefore
                                                       ∞
                                                ∣α∣2       (αz)n     ∣α∣2
                                   ψα (z) = e  − 2
                                                       ∑         = e− 2 eαz .
                                                       n=0
                                                             n!


Prime-Embedded Coherent States
Applying the prime weight operator Mw yields the prime-modulated coherent state

                                                                         ∞
                                                                  ∣α∣2             αn
                                 ∣α; w⟩ := Mw ∣α⟩ = e           − 2
                                                                         ∑ wn          ∣n⟩.
                                                                         n=0        n!

Its Bargmann–Segal function is
                                                                  ∞
                                                         ∣α∣2                  (αz)n
                                      ψα;w (z) = e− 2 ∑ wn                           .
                                                                  n=0
                                                                                 n!



Fully worked example: Prime-indicator SNAP phase gate on a
coherent state
A SNAP gate is a number-selective phase operation of the form

                                                         ∞
                                           U{ϕn } := ∑ eiϕn ∣n⟩⟨n∣.
                                                        n=0


Prime-indicator phase pattern

Define the prime-indicator function


                               χP (n) := {1,     n is prime 0, n is not prime

and choose a single phase angle θ ∈ R with

                                                ϕn = θ χP (n).

Then the gate is
                                                          ∞
                                      Uprime (θ) := ∑ eiθχP (n) ∣n⟩⟨n∣.
                                                        n=0

This is exactly a prime-on-coefficients modulation with weights wn = eiθχP (n) .




                                                              3
Action on a coherent state ∣α⟩

Applying Uprime (θ) gives

                                                                                   ∞
                                                                            ∣α∣2                     αn
                            ∣α; prime, θ⟩ := Uprime (θ)∣α⟩ = e− 2 ∑ eiθχP (n)                            ∣n⟩.
                                                                                   n=0                n!

Bargmann–Segal holomorphic function ψ(z)

The corresponding Bargmann–Segal function is

                                                                      ∞
                                                               ∣α∣2                      (αz)n
                                     ψα;prime,θ (z) = e       − 2
                                                                      ∑ eiθχP (n)              .
                                                                      n=0
                                                                                           n!

A useful decomposition separates prime and non-prime indices:

                                               ∣α∣2                  (αz)n         (αz)n
                        ψα;prime,θ (z) = e− 2                 ∑            + eiθ ∑                              .
                                                       n≥0 non-prime
                                                                       n!            n!
                                                                                               n∈P


Equivalently,


                               ψα;prime,θ (z) = e− 2 [eαz + (eiθ − 1) ∑                              ].
                                                       ∣α∣2                                    (αz)n
                                                                                                 n!
                                                                                         n∈P


Overlap (fidelity amplitude) with the original coherent state

The overlap of the original coherent state with the prime-gated coherent state is

                                                                                     ∞
                              ⟨α∣α; prime, θ⟩ = ⟨α∣Uprime (θ)∣α⟩ = ∑ ∣cn ∣2 eiθχP (n) ,
                                                                                    n=0
                    2 ∣α∣2n
where ∣cn ∣2 = e−∣α∣    n!    is a Poisson distribution with mean λ = ∣α∣2 . Hence
                                                      ∞
                                                                       λn
                       ⟨α∣α; prime, θ⟩ = e−λ ∑ eiθχP (n)                  = 1 + (eiθ − 1) Pprime (λ),
                                                      n=0
                                                                       n!

with

                                               λn
                  Pprime (λ) := e−λ ∑                   (Poisson probability mass on prime n).
                                               n!
                                         n∈P

The corresponding fidelity is ∣⟨α∣α; prime, θ⟩∣2 .


More generally, the coherent-state overlap (useful for Husimi-Q computations) is




                                                                 4
                                                                   ∞
                                                      ∣α∣2 +∣β∣2                 (β ∗ α)n
                               ⟨β∣α; prime, θ⟩ = e−        2       ∑ eiθχP (n)            .
                                                                   n=0
                                                                                    n!


Expected nonclassicality signature

     • Photon-number distribution is unchanged. Because Uprime (θ) is diagonal in ∣n⟩, it preserves
       ∣cn ∣2 . So the output still has a Poisson photon-number distribution.
     • But phase-space structure becomes non-Gaussian. The gate introduces a number-dependent
       phase pattern eiθχP (n) , which reshapes interference between Fock components.
     • Wigner interference fringes and negativity. A coherent state has a strictly positive Gaussian
       Wigner function. After the prime-indicator SNAP gate, the Wigner function typically develops
       oscillatory fringes and, for sufficiently large ∣α∣ and nontrivial θ (e.g., θ = π , a prime-index sign
       flip), exhibits regions of negative Wigner density.

A compact diagnostic expression is the displaced-parity formula

                                      2
                            W (β) =     ⟨α; prime, θ∣ D(β) Π D(β)† ∣α; prime, θ⟩,
                                      π
where D(β) is the displacement operator and Π = (−1)n^ is the parity operator. Negativity of W (β) at
some β is a direct nonclassicality signature.




3. Prime-Weighted Time Evolution and
Propagation
Time evolution can be prime-modulated in a way that remains consistent with the prime-on-coefficients
principle.


Quantum Time Evolution
The Schrödinger equation is

                                              d
                                         iℏ      ∣ψ(t)⟩ = H(t)∣ψ(t)⟩.
                                              dt
In the number basis ∣n⟩, coefficients ψn (t) obey
                                        ∞
                            d
                       iℏ      ψn (t) = ∑ Hnm (t) ψm (t),            Hnm (t) = ⟨n∣H(t)∣m⟩.
                            dt          m=0



Prime-Embedded Time Evolution (coefficient-level control)
A direct prime-structured control term is a diagonal “phase-drive” Hamiltonian




                                                         5
                                                          ∞
                                      Hprime (t) := ℏ ∑ ϕ̇n (t) ∣n⟩⟨n∣,
                                                          n=0

where ϕn (t) is any prime-derived phase schedule (e.g., ϕn (t) = θ(t)χP (n)).


Then the evolution operator generated by Hprime (t) alone is precisely the SNAP form

                                                    ∞
                                         U (t) = ∑ eiϕn (t) ∣n⟩⟨n∣.
                                                    n=0


Gate-based (stroboscopic) propagation

PEQBSA can also be implemented as alternating free evolution and prime-phase pulses:

                                                                (k)
                                      ∣ψk+1 ⟩ = Ufree (Δt) Uprime ∣ψk ⟩,
                (k)
where each Uprime is a chosen diagonal prime-derived modulation.




4. Prime-Controlled Quantum State Overlap and
Inner Product
Prime control should not be introduced by inserting p(n) into an integral over z without defining how n
enters the holomorphic representation. Instead, prime control is expressed by applying modulation
operators to the states and then using the standard inner product.


Quantum State Overlap
In Bargmann–Segal form, the (standard) inner product is


                                                                          d2 z
                                  ⟨ψ1 ∣ψ2 ⟩ = ∫ ψ1 (z)∗ ψ2 (z) e−∣z∣
                                                                      2
                                                                               .
                                                C                          π
In Fock coefficients, it is
                                                          ∞
                                          ⟨ψ1 ∣ψ2 ⟩ = ∑ ψ1,n
                                                         ∗
                                                             ψ2,n .
                                                          n=0



Prime-Embedded Quantum State Overlap
Let ∣ψ1,w ⟩ = Mw ∣ψ1 ⟩ and ∣ψ2,v ⟩ = Mv ∣ψ2 ⟩. Then the prime-controlled overlap is




                                                          6
                                                                ∞
                           ⟨ψ1,w ∣ψ2,v ⟩ = ⟨ψ1 ∣Mw† Mv ∣ψ2 ⟩ = ∑ ψ1,n
                                                                  ∗
                                                                      (wn∗ vn ) ψ2,n .
                                                               n=0

If wn = eiϕn and vn = eiφn , this simplifies to
                                                     ∞
                                    ⟨ψ1,w ∣ψ2,v ⟩ = ∑ ψ1,n
                                                       ∗
                                                           ei(φn −ϕn ) ψ2,n .
                                                    n=0




5. Applications in Quantum Optics, Quantum
Computing, and Phase Space Methods
Quantum Optics
Prime-structured diagonal phase modulation provides a systematic way to engineer non-Gaussian states
from classical-like inputs (e.g., coherent states). This enables controlled creation of phase-space
interference patterns and nonclassical signatures.


Quantum Computing
In continuous-variable and bosonic encodings, number-selective phase gates are powerful primitives.
Prime-derived phase schedules provide reproducible, structured modulation patterns for benchmarking,
control design, and state engineering.


Phase Space Representations
Because PEQBSA is formulated directly in the Bargmann–Segal / phase-space language, it connects
naturally to Husimi-Q and Wigner representations. Prime modulation yields tunable distortions of phase-
space distributions and interference structure.




Complete Prime-Embedded Quantum Bargmann–
Segal Algorithm (PEQBSA)
Here’s the complete structure of the Prime-Embedded Quantum Bargmann–Segal Algorithm (PEQBSA) in
prime-on-coefficients form:


Step 1: Prime-Encoded Bargmann–Segal States - Choose prime-derived weights wn (preferably ∣wn ∣ = 1
for a unitary embedding). - Define Mw = ∑n wn ∣n⟩⟨n∣ and ψw (z) = ∑n wn ψn z n /         n!.




                                                         7
Step    2:    Prime-Modulated    Coherent    States   -   Start   from   ∣α⟩ and apply Mw : ∣α; w⟩ =
 −∣α∣2 /2
e           ∑n wn α / n! ∣n⟩.
                   n



Step 3: Prime-Weighted Time Evolution - Implement a prime-derived diagonal control Hamiltonian
(continuous) or SNAP-style pulses (stroboscopic): U (t) = ∑n eiϕn (t) ∣n⟩⟨n∣.


Step 4: Prime-Controlled Quantum State Overlap - Compute overlaps via the standard inner product
after modulation: ⟨ψ1,w ∣ψ2,v ⟩ = ⟨ψ1 ∣Mw† Mv ∣ψ2 ⟩.




6. Advantages of PEQBSA
       • Mathematically well-defined: primes act on the discrete Fock/Taylor index n, avoiding undefined
         mixing of discrete and continuous variables.
       • Physically implementable (unitary mode): choosing ∣wn ∣ = 1 gives a bona fide quantum gate
         (diagonal phase control).
       • Controlled nonclassicality: prime-derived number-dependent phases generate non-Gaussian
         phase-space interference and potential Wigner negativity.
       • Flexible information processing: prime-structured overlaps provide a tunable similarity/contrast
         mechanism between states.




Conclusion
The Prime-Embedded Quantum Bargmann–Segal Algorithm (PEQBSA) can be made precise by
implementing prime structure as a coefficient-level (Fock-basis) modulation. In this corrected form,
PEQBSA becomes a clear operator-theoretic procedure that translates directly into Bargmann–Segal
holomorphic functions and supports concrete, testable protocols such as a prime-indicator SNAP phase
gate on coherent states.




                                                      8
