---
slug: peqbsa-prime-on-coefficients
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Peqbsa (prime-on-coefficients).md
  last_synced: '2026-03-20T17:17:20.196132Z'
---

The Prime-Embedded Quantum Bargmann–Segal
Algorithm (PEQBSA)
Corrected “prime-on-coefficients” formulation (with references)
The Prime-Embedded Quantum Bargmann–Segal Algorithm (PEQBSA) introduces prime-structured
modulation into the Bargmann–Segal (Segal–Bargmann / Fock-space) phase-space formalism by acting on
the Fock/Taylor coefficients of the holomorphic representation [1,2].


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
phase space [1,2]. The discrete Fock index n appears naturally through the Taylor/Fock expansion.


Bargmann–Segal State Representation
Let ∣ψ⟩ be a (single-mode) bosonic quantum state with Fock expansion


$$ |\psi\rangle = \sum_{n=0}^{\infty} \psi_n\,|n\rangle, \qquad \sum_{n=0}^{\infty} |\psi_n|^2 = 1. $$


The corresponding Bargmann–Segal holomorphic function is


$$ \psi(z) = \sum_{n=0}^{\infty} \psi_n\,\frac{z^n}{\sqrt{n!}}, \qquad z\in\mathbb{C}. $$




                                                       1
Equivalently, the coefficients are recovered by


$$ \psi_n = \frac{1}{\sqrt{n!}}\,\left.\frac{d^n}{dz^n}\psi(z)\right|_{z=0}. $$


Prime-Encoded Bargmann–Segal State (prime-on-coefficients)
Define a prime-derived weight sequence wn (built from primes in any desired way). The prime embedding
is implemented by the diagonal (number-basis) modulation operator


$$ M_w := \sum_{n=0}^{\infty} w_n\,|n\rangle\langle n|. $$


The prime-embedded state is


$$ |\psi_w\rangle := M_w|\psi\rangle = \sum_{n=0}^{\infty} (w_n\psi_n)\,|n\rangle. $$


In Bargmann–Segal form, this is


$$ \psi_w(z) := (M_w\psi)(z) = \sum_{n=0}^{\infty} w_n\psi_n\,\frac{z^n}{\sqrt{n!}}. $$


Notes on physical realizability

      • If ∣wn ∣ = 1 for all n, then Mw is unitary (a physically valid closed-system gate).
      • If ∣wn ∣  1 (e.g.,
                         =wn grows with n), then Mw is non-unitary and must be interpreted as a filter /
       postselected / dissipative operation, typically requiring truncation and renormalization.




2. Prime-Modulated Coherent States and Quantum
Amplitudes
Coherent states play a central role in quantum optics and continuous-variable quantum information [3]. In
PEQBSA, primes modulate coherent states by acting on their Fock coefficients.


Coherent States
A coherent state ∣α⟩ (α ∈ C) has the Fock expansion [3]


$$ |\alpha\rangle = e^{-\frac{|\alpha|^2}{2}}\sum_{n=0}^{\infty} \frac{\alpha^n}{\sqrt{n!}}\,|n\rangle. $$


Its Bargmann–Segal function is


$$ \psi_{\alpha}(z) = e^{-\frac{|\alpha|^2}{2}}\sum_{n=0}^{\infty} \frac{(\alpha z)^n}{n!} = e^{-\frac{|\alpha|
^2}{2}} e^{\alpha z}. $$




                                                         2
Prime-Embedded Coherent States
Applying the prime weight operator Mw yields the prime-modulated coherent state


$$ |\alpha;w\rangle := M_w|\alpha\rangle             =       e^{-\frac{|\alpha|^2}{2}}\sum_{n=0}^{\infty}   w_n\,
\frac{\alpha^n}{\sqrt{n!}}\,|n\rangle. $$


Its Bargmann–Segal function is


$$ \psi_{\alpha;w}(z) = e^{-\frac{|\alpha|^2}{2}}\sum_{n=0}^{\infty} w_n\,\frac{(\alpha z)^n}{n!}. $$




Fully worked example: Prime-indicator SNAP phase gate on a
coherent state
A SNAP gate is a number-selective phase operation of the form [4,5]


$$ U_{{\phi_n}} := \sum_{n=0}^{\infty} e^{i\phi_n}\,|n\rangle\langle n|. $$


Prime-indicator phase pattern

Define the prime-indicator function


$$ \chi_{\mathbb{P}}(n) := \begin{cases} 1, & n \text{ is prime}\
0, & n \text{ is not prime} \end{cases} $$


and choose a single phase angle θ ∈ R with


$$ \phi_n = \theta\,\chi_{\mathbb{P}}(n). $$


Then the gate is


$$ U_{\text{prime}}(\theta) := \sum_{n=0}^{\infty} e^{i\theta\chi_{\mathbb{P}}(n)}\,|n\rangle\langle n|. $$


This is exactly a prime-on-coefficients modulation with weights wn = eiθχP (n) .


Applying Uprime (θ) gives


$$ |\alpha;\text{prime},\theta\rangle := U_{\text{prime}}(\theta)|\alpha\rangle = e^{-\frac{|\alpha|^2}{2}}
\sum_{n=0}^{\infty} e^{i\theta\chi_{\mathbb{P}}(n)}\,\frac{\alpha^n}{\sqrt{n!}}\,|n\rangle. $$


The corresponding Bargmann–Segal function is




                                                         3
$$         \psi_{\alpha;\text{prime},\theta}(z)         =           e^{-\frac{|\alpha|^2}{2}}\sum_{n=0}^{\infty}
e^{i\theta\chi_{\mathbb{P}}(n)}\,\frac{(\alpha z)^n}{n!}. $$


A useful decomposition separates prime and non-prime indices:


$$ \psi_{\alpha;\text{prime},\theta}(z) = e^{-\frac{|\alpha|^2}{2}}\left[ \sum_{n\ge 0\,\text{non-prime}}
\frac{(\alpha z)^n}{n!} + e^{i\theta}\sum_{n\in\mathbb{P}} \frac{(\alpha z)^n}{n!} \right]. $$


Equivalently,


$$      \psi_{\alpha;\text{prime},\theta}(z)   =    e^{-\frac{|\alpha|^2}{2}}\left[          e^{\alpha       z}   +
(e^{i\theta}-1)\sum_{n\in\mathbb{P}} \frac{(\alpha z)^n}{n!} \right]. $$


Overlap (fidelity amplitude) with the original coherent state

The overlap of the original coherent state with the prime-gated coherent state is


$$ \langle \alpha|\alpha;\text{prime},\theta\rangle = \langle \alpha|U_{\text{prime}}(\theta)|\alpha\rangle
= \sum_{n=0}^{\infty} |c_n|^2\,e^{i\theta\chi_{\mathbb{P}}(n)}, $$

                     2 ∣α∣2n
where ∣cn ∣2 = e−∣α∣    n!     is a Poisson distribution with mean λ = ∣α∣2 . Hence


$$       \langle     \alpha|\alpha;\text{prime},\theta\rangle         =       e^{-\lambda}\sum_{n=0}^{\infty}
e^{i\theta\chi_{\mathbb{P}}(n)}\,\frac{\lambda^{n}}{n!} = 1 + (e^{i\theta}-1)\,P_{\text{prime}}(\lambda), $$


with


$$ P_{\text{prime}}(\lambda) := e^{-\lambda}\sum_{n\in\mathbb{P}}                     \frac{\lambda^n}{n!}    \quad
\text{(Poisson probability mass on prime }n\text{)}. $$


The corresponding fidelity is ∣⟨α∣α; prime, θ⟩∣2 .


More generally, the coherent-state overlap (useful for Husimi-Q computations) is


$$ \langle \beta|\alpha;\text{prime},\theta\rangle = e^{-\frac{|\alpha|^2+|\beta|^2}{2}}\sum_{n=0}^{\infty}
e^{i\theta\chi_{\mathbb{P}}(n)}\,\frac{(\beta^*\alpha)^n}{n!}. $$


Expected nonclassicality signature

       • Photon-number distribution is unchanged. Because Uprime (θ) is diagonal in ∣n⟩, it preserves
        ∣cn ∣2 . So the output still has a Poisson photon-number distribution.
       • But phase-space structure becomes non-Gaussian. The gate introduces a number-dependent
         phase pattern eiθχP (n) , which reshapes interference between Fock components.
       • Wigner interference fringes and negativity. A coherent state has a strictly positive Gaussian
         Wigner function. After the prime-indicator SNAP gate, the Wigner function typically develops




                                                          4
       oscillatory fringes and, for sufficiently large ∣α∣ and nontrivial θ (e.g., θ = π , a prime-index sign
       flip), exhibits regions of negative Wigner density.

A compact diagnostic expression is the displaced-parity formula [6–8]


$$ W(\beta) = \frac{2}{\pi}\,\langle \alpha;\text{prime},\theta|\,D(\beta)\,\Pi\,D(\beta)^{\dagger}\,|\alpha;
\text{prime},\theta\rangle, $$


where D(β) is the displacement operator and Π = (−1)n^ is the parity operator. Negativity of W (β) at
some β is a direct nonclassicality signature.




3. Prime-Weighted Time Evolution and
Propagation
Time evolution can be prime-modulated in a way that remains consistent with the prime-on-coefficients
principle.


Quantum Time Evolution
The Schrödinger equation is


$$ i\hbar\frac{d}{dt}|\psi(t)\rangle = H(t)|\psi(t)\rangle. $$


In the number basis ∣n⟩, coefficients ψn (t) obey


$$ i\hbar\frac{d}{dt}\psi_n(t) = \sum_{m=0}^{\infty} H_{nm}(t)\,\psi_m(t), \quad H_{nm}(t)=\langle n|H(t)|
m\rangle. $$


Prime-Embedded Time Evolution (coefficient-level control)
A direct prime-structured control term is a diagonal “phase-drive” Hamiltonian


$$ H_{\text{prime}}(t) := \hbar\sum_{n=0}^{\infty} \dot\phi_n(t)\,|n\rangle\langle n|, $$


where ϕn (t) is any prime-derived phase schedule (e.g., ϕn (t) = θ(t)χP (n)).


Then the evolution operator generated by Hprime (t) alone is precisely the SNAP form [4,5]


$$ U(t) = \sum_{n=0}^{\infty} e^{i\phi_n(t)}\,|n\rangle\langle n|. $$




                                                         5
Gate-based (stroboscopic) propagation

PEQBSA can also be implemented as alternating free evolution and prime-phase pulses:


$$ |\psi_{k+1}\rangle = U_{\text{free}}(\Delta t)\,U_{\text{prime}}^{(k)}\,|\psi_k\rangle, $$

                (k)
where each Uprime is a chosen diagonal prime-derived modulation.




4. Prime-Controlled Quantum State Overlap and
Inner Product
Prime control should not be introduced by inserting prime weights into an integral over z without defining
how the discrete index enters the holomorphic representation. Instead, prime control is expressed by
applying modulation operators to the states and then using the standard inner product [1,2].


Quantum State Overlap
In Bargmann–Segal form, the (standard) inner product is [1,2]


$$ \langle \psi_1|\psi_2\rangle = \int_{\mathbb{C}} \psi_1(z)^*\,\psi_2(z)\,e^{-|z|^2}\,\frac{d^2 z}{\pi}. $$


In Fock coefficients, it is


$$ \langle \psi_1|\psi_2\rangle = \sum_{n=0}^{\infty} \psi_{1,n}^*\,\psi_{2,n}. $$


Prime-Embedded Quantum State Overlap
Let ∣ψ1,w ⟩ = Mw ∣ψ1 ⟩ and ∣ψ2,v ⟩ = Mv ∣ψ2 ⟩. Then the prime-controlled overlap is


$$ \langle \psi_{1,w}|\psi_{2,v}\rangle = \langle \psi_1|M_w^{\dagger}M_v|\psi_2\rangle = \sum_{n=0}
^{\infty} \psi_{1,n}^\,(w_n^ v_n)\,\psi_{2,n}. $$


If wn = eiϕn and vn = eiφn , this simplifies to


$$ \langle \psi_{1,w}|\psi_{2,v}\rangle = \sum_{n=0}^{\infty} \psi_{1,n}^*\,e^{i(\varphi_n-\phi_n)}\,\psi_{2,n}.
$$




                                                        6
5. Applications in Quantum Optics, Quantum
Computing, and Phase Space Methods
Quantum Optics
Prime-structured diagonal phase modulation provides a systematic way to engineer non-Gaussian states
from classical-like inputs (e.g., coherent states) [3–5]. This enables controlled creation of phase-space
interference patterns and nonclassical signatures [6–8].


Quantum Computing
In continuous-variable and bosonic encodings, number-selective phase gates are powerful primitives [4,5].
Prime-derived phase schedules provide reproducible, structured modulation patterns for benchmarking,
control design, and state engineering.


Phase Space Representations
Because PEQBSA is formulated directly in the Bargmann–Segal / phase-space language, it connects
naturally to Husimi-Q and Wigner representations [1,2]. Prime modulation yields tunable distortions of
phase-space distributions and interference structure [6–8].




Complete Prime-Embedded Quantum Bargmann–
Segal Algorithm (PEQBSA)
Here’s the complete structure of the Prime-Embedded Quantum Bargmann–Segal Algorithm (PEQBSA) in
prime-on-coefficients form:


Step 1: Prime-Encoded Bargmann–Segal States


     • Choose prime-derived weights wn (preferably ∣wn ∣ = 1 for a unitary embedding).
     • Define Mw = ∑n wn ∣n⟩⟨n∣ and ψw (z) = ∑n wn ψn z n /         n! [1,2].

Step 2: Prime-Modulated Coherent States

                                                  2
     • Start from ∣α⟩ and apply Mw : ∣α; w⟩ = e−∣α∣ /2 ∑n wn αn /    n! ∣n⟩ [3].

Step 3: Prime-Weighted Time Evolution


     • Implement a prime-derived diagonal control Hamiltonian (continuous) or SNAP-style pulses
       (stroboscopic) [4,5]: U (t) = ∑n eiϕn (t) ∣n⟩⟨n∣.




                                                      7
Step 4: Prime-Controlled Quantum State Overlap


      • Compute overlaps via the standard inner product after modulation [1,2]: ⟨ψ1,w ∣ψ2,v ⟩ =
         ⟨ψ1 ∣Mw† Mv ∣ψ2 ⟩.




6. Advantages of PEQBSA
      • Mathematically well-defined: primes act on the discrete Fock/Taylor index n, avoiding undefined
        mixing of discrete and continuous variables [1,2].
      • Physically implementable (unitary mode): choosing ∣wn ∣ = 1 gives a bona fide quantum gate
        (diagonal phase control) [4,5].
      • Controlled nonclassicality: prime-derived number-dependent phases generate non-Gaussian
        phase-space interference and potential Wigner negativity [6–8].
      • Flexible information processing: prime-structured overlaps provide a tunable similarity/contrast
        mechanism between states.




Conclusion
The Prime-Embedded Quantum Bargmann–Segal Algorithm (PEQBSA) can be made precise by
implementing prime structure as a coefficient-level (Fock-basis) modulation. In this corrected form,
PEQBSA becomes a clear operator-theoretic procedure that translates directly into Bargmann–Segal
holomorphic functions and supports concrete, testable protocols such as a prime-indicator SNAP phase
gate on coherent states.




References
[1] V. Bargmann, “On a Hilbert space of analytic functions and an associated integral transform. Part I,”
Communications on Pure and Applied Mathematics 14(3), 187–214 (1961). doi:10.1002/cpa.3160140303.


[2] I. E. Segal, Mathematical Problems of Relativistic Physics (American Mathematical Society, Providence,
1963).


[3] R. J. Glauber, “Coherent and incoherent states of the radiation field,” Physical Review 131, 2766–2788
(1963). doi:10.1103/PhysRev.131.2766.


[4] R. W. Heeres, B. Vlastakis, E. Holland, S. Krastanov, V. V. Albert, L. Frunzio, L. Jiang, and R. J. Schoelkopf,
“Cavity State Manipulation Using Photon-Number Selective Phase Gates,” Physical Review Letters 115, 137002
(2015). doi:10.1103/PhysRevLett.115.137002.




                                                        8
[5] S. Krastanov, V. V. Albert, C. Shen, C.-L. Zou, R. W. Heeres, B. Vlastakis, R. J. Schoelkopf, and L. Jiang,
“Universal Control of an Oscillator with Dispersive Coupling to a Qubit,” Physical Review A 92, 040303(R)
(2015). doi:10.1103/PhysRevA.92.040303.


[6] A. Royer, “Wigner function as the expectation value of a parity operator,” Physical Review A 15, 449–450
(1977). doi:10.1103/PhysRevA.15.449.


[7] K. Banaszek and K. Wódkiewicz, “Direct Probing of Quantum Phase Space by Photon Counting,” Physical
Review Letters 76, 4344–4347 (1996). doi:10.1103/PhysRevLett.76.4344.


[8] L. G. Lutterbach and L. Davidovich, “Method for Direct Measurement of the Wigner Function in Cavity
QED and Ion Traps,” Physical Review Letters 78, 2547–2550 (1997). doi:10.1103/PhysRevLett.78.2547.


Citizen Gardens © 2025 CC-NC-ND 4.0




                                                      9
