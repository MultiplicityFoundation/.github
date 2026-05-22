---
slug: vihann-mathur
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/Vihann_Mathur.md
  last_synced: '2026-03-20T17:17:11.803686Z'
---

T IME VARIATIONS T HEORY: A R ECURSIVE F RAMEWORK OF
                                    S PACE -T IME E VOLUTION


                                               Authored by Vihaan Mathur

                                    Enhanced and Formalized by Ryan O. Van Gelder
                                                      Citizen Gardens




                                                       A BSTRACT
          This paper presents an exploratory fusion of speculative metaphysics and experimentally grounded
          quantum phenomena, merging the Time Variations Theory (TVT) with Quantum Time Crystals
          (QTCs) into a novel framework: the Quantum-Temporal Field Theory of Variations (QTFV). We
          translate high-level quantum and relativistic principles into an educational curriculum, gradually
          building from intuitive concepts of time and causality to tensor networks and decoherence. Our goal
          is to construct a rigorous yet accessible curriculum to guide advanced high school and early
          university learners into the frontier of theoretical physics.


1      Introduction (Accessible Overview)

Time is usually thought of as a one-way street: the past is behind us, the present is now, and the future hasn’t happened
yet.

    What if Time Loops?

    Imagine time not as a straight line, but as a branching river. Every decision, even every random event, might split
the river into multiple streams—each one a different version of reality.

    And what if some particles in the quantum world can actually oscillate through time, staying in motion even without
using energy? These ideas inspire two amazing concepts:

        • Time Variations Theory (TVT): The idea that every moment spawns new ”variations” of time—like alternate
          timelines in science fiction. These can merge, split, or loop.

        • Quantum Time Crystals (QTCs): Real quantum systems that show movement in time without expending
          energy. They challenge what we thought was possible in physics.
Preprint - PrimeAI Enhanced Template


      In this paper, we combine both to propose QTFV—a theory where time is like a quantum network of possibilities,
with each branch behaving like a time crystal node. Think of it as a cosmic circuit board of timelines.



2     Foundations of Time Variations Theory (TVT)

2.1    Core Ideas

         • Time is conceptualized as a branching structure composed of infinite variations.

         • Each variation is a possible configuration of events diverging from the main timeline.

         • Variations can be stable, corrupted (via decoherence), or looped (reverse/present variation).


2.2    TVT Postulates

        1. Variation Superposition: The total temporal state is a quantum superposition of multiple timeline
           configurations.

        2. Causal Permittivity: Variations may interact, influencing or collapsing each other.

        3. Loop Permissibility: Time loops are allowed within quantum coherence constraints.


2.3    Variation Probability (QTC Phase-based)

                                                               ∆ϕE
                                                      P (E) = P                                                     (1)
                                                                i ∆ϕi

where ∆ϕE is the phase offset from the dominant QTC variation.


2.4    Corruption Threshold

A variation is considered corrupted when:

                                              Γ > Γc ⇒ ⟨Ci (t)|Ci (0)⟩ → 0                                          (2)



3     Quantum-Temporal Field Theory of Variations (QTFV)

3.1    Fusion with Quantum Time Crystals

         • QTCs provide the physical substrate for TVT’s variations.

         • Oscillating QTCs represent timeline nodes, each capable of sustaining periodic quantum states without energy
           input.

         • The ”space timeline” is a network of coupled QTCs.


                                           Time Variations Theory © 2024 - Citizen Gardens                 Page 2 of 10
                                             Licensed Under MIT and CC BY-NC-SA 4.0.
Preprint - PrimeAI Enhanced Template


3.2     Mathematical Definitions
                                                       N
                                                       X                        X
                                             |ΨT ⟩ =          αi |Ci ⟩,               |αi |2 = 1                   (3)
                                                        i=1


                                                          X
                                                  V̂τ =               λij eiωij t |Cj ⟩⟨Ci |                       (4)
                                                           i,j



                                   dρ    i                         1
                                                      Γk (Lk ρL†k − {L†k Lk , ρ})
                                                    X
                                      = − [Ĥ, ρ] +                                                                (5)
                                   dt    ℏ                         2
                                                                  k


3.3     QTFV Manifold and QTC Coupling

We describe time as a collection of coupled quantum systems:

                                                                        [
                                                           T =               Ci (t)                                (6)
                                                                         i

Each Ci is a timeline node represented by a QTC wavefunction:

                                                  |ψi (t)⟩ = e−iHi t/ℏ |ψi (0)⟩                                    (7)


      - Hi : The energy (Hamiltonian) of the system. - ℏ: Planck’s constant (very small number from quantum physics). -
e−iHi t/ℏ : Describes how the state evolves in time.


3.4     Superposition of Variations

The total state of time can be written as:
                                                   N
                                                   X                                  X
                                       |ΨT ⟩ =           αi |Ci ⟩ with                    |αi |2 = 1               (8)
                                                   i=1


3.5     Transition Operator Between Timelines

To model jumping from one variation to another:

                                                          X
                                                  V̂τ =               λij eiωij t |Cj ⟩⟨Ci |                       (9)
                                                           i,j


3.6     Corruption as Decoherence

Noise in quantum systems leads to corruption:

                                  dρ    i          X       †  1 †
                                                                           
                                     = − [Ĥ, ρ] +  Γk Lk ρLk − {Lk Lk , ρ}                                       (10)
                                  dt    ℏ                      2
                                                              k


                                             Time Variations Theory © 2024 - Citizen Gardens              Page 3 of 10
                                               Licensed Under MIT and CC BY-NC-SA 4.0.
Preprint - PrimeAI Enhanced Template


4     Formal Theorems and Proofs

Theorem 1: Unitary Evolution of QTC Variations

Statement: QTC timelines evolve unitarily via Ui (t) = e−iHi t/ℏ , preserving norm.

      Proof: Since Hi is Hermitian, Ui is unitary. Hence:

                                          ⟨Ci (t)|Ci (t)⟩ = ⟨Ci (0)|U † U |Ci (0)⟩ = 1                (11)




Theorem 2: Stability Under Decoherence

Statement: If Γ < Γc , fidelity of variation loops remains above 1 − ϵ.

      Sketch: Use Lindblad equation to show:

                                              F (t) = |⟨Ci (0)|Ci (t)⟩|2 ∼ e−Γt                       (12)

Solve for threshold Γc given loop time t = nT .


Theorem 3: Transition Resonance

Statement: Transition probability between variations is maximized at ωij = 0.



                                        Pi→j = |λij |2 ,      maximized when ωij → 0                  (13)




5     Experimental and Simulation Blueprint

5.1     QTC Lattice Simulation Plan

         • Build 4–8 node QTC lattice.

         • Apply unitary evolution with decoherence.

         • Measure:

             – Fidelity decay,

             – Variation probability,

             – Phase shifts under retrocausal perturbations.


                                            Time Variations Theory © 2024 - Citizen Gardens   Page 4 of 10
                                              Licensed Under MIT and CC BY-NC-SA 4.0.
Preprint - PrimeAI Enhanced Template


5.2    Quantum-AI Integration

         • Use reinforcement learning to select stable variation paths.

         • Implement prime-indexed recursive learning to align with PIRTM/DRMM.


6     Holographic Time Variations: Bridging QTFV with AdS/CFT

6.1    Core Hypothesis: Time Variations as Holographic Phenomena

We propose that Time Variations Theory (TVT), when viewed through the lens of the AdS/CFT correspondence,
reveals a duality where:

         • The bulk consists of quantum time crystals (QTCs), modeled as oscillating scalar fields C(t, x, z) in AdS
           spacetime. These encode the structure of variations as field excitations.

         • The boundary is a conformal field theory (CFT), where timeline variations correspond to entangled operator
           states O(x), with evolution driven by the QTC frequencies.

      This implies a dynamical correspondence:

                                         C|∂ = J ,      and     ∂t ⟨O(x)⟩ = f (ωQTC )                                       (14)

Here, J is a source field at the boundary, and f encodes the influence of bulk QTC oscillations on boundary operator
dynamics.


6.2    Holographic Dictionary: Enriched Mapping

We summarize the dual relationships below:

    QTFV Bulk (AdS)                       CFT Boundary                          Physical Interpretation
    QTC state |Ci ⟩                       CFT state |ψi ⟩                       Timeline variation with frequency ωi = ∆i /ℏ
    Variation collapse (QTC melting)      Operator scrambling                   Decoherence and thermalization
    Reverse variation                     Non-Hermitian operator O              Retrocausal information flow
    Space timeline (variation density)    UV cutoff Λ                           Discrete resolution of variations
    Sub-variations (fractal QTCs)         OPE terms Cijk                        Nested operator expansions

6.3    Holographic QTC Lagrangian

We model the QTC field C in the AdS bulk as:
                                                                        ∞
                                          "                                       #
                                    √       1 µν                       X
                            LQTC = −g         g (∇µ C)(∇ν C) − V (C) +     gn C n                                           (15)
                                            2                          n=1


                                           Time Variations Theory © 2024 - Citizen Gardens                          Page 5 of 10
                                             Licensed Under MIT and CC BY-NC-SA 4.0.
Preprint - PrimeAI Enhanced Template


                                                    2
         • gµν is the AdS metric, e.g., ds2 = Lz2 (dt2 − d⃗x2 − dz 2 ).

         • V (C) = 21 m2 C 2 , with m2 L2 = ∆(∆ − d).

         • Boundary condition: C(t, ⃗x, z → 0) = J (t, ⃗x).


6.4    Entropy and Loops in the Holographic Regime

Corrupted Variations: When QTC coherence fails (e.g., Γ > Γc ), entropy increases in the bulk, corresponding to
thermalization on the boundary:

                                                 Area(γA )
                                      SCFT =               ,       (Ryu-Takayanagi surface)                                     (16)
                                                   4GN

      Reverse Variations and Time Loops: Retrocausal timeline loops correspond to non-unitary deformations of the
CFT:
                                                                                          ℏ
                                                O → iÕ,         with     Im(λO ) <                                             (17)
                                                                                          β
This enforces stability conditions for closed time-like curves (CTCs) in the bulk.


6.5    Holographic Time Loops

                                                                                             λO(x) dd−1 x where Im(λ) ̸= 0. Then the
                                                                                         R
Statement. Let a boundary CFT admit a non-unitary deformation δS =
AdS bulk admits closed time-like curves (CTCs), stable when:

                                                                             ℏ
                                                             Im(λO ) <                                                          (18)
                                                                             β

Proof Sketch.

                                           R
        1. Deform CFT: SCFT → SCFT +            λO.

        2. By AdS/CFT, this sources a bulk field C with boundary value λ.

        3. This generates a bulk metric perturbation δgtt ∼ Im(λ)C 2 .

        4. Solve Einstein’s equations; condition gtt = 0 implies formation of CTCs if Im(λ) is bounded by inverse
           temperature β.




6.6    Simulation and Experimental Roadmap

SYK + QTC Simulation:

         • Implement a hybrid Hamiltonian:
                                                        Htotal = HSYK + HQTC + Hint                                             (19)


                                               Time Variations Theory © 2024 - Citizen Gardens                          Page 6 of 10
                                                 Licensed Under MIT and CC BY-NC-SA 4.0.
Preprint - PrimeAI Enhanced Template


         • Measure:

             – ⟨C(t)⟩: reveals variation oscillation.

             – SA (t): tracks entanglement entropy across regions.

             – W (t): quasiprobability → detects retrocausality.

      Lab Pathway:

         • IBM’s superconducting hardware (e.g., ibm kyiv) for simulating 7-qubit CFT.

         • IonQ’s trapped ion systems for Ramsey interferometry on QTCs.

      Conclusion. Holographic Time Variations offer a rich, dual-layered architecture uniting TVT’s speculative
temporal topologies, QTC coherence, and the formal strength of AdS/CFT. As a framework, it promises to map the
quantum geometry of time itself.


7     Holographic Time Variations: A Quantum-Temporal Enhancement of General Relativity

This section presents a mathematical framework integrating Quantum Time Crystals (QTCs), Time Variations Theory
(TVT), and holographic principles from AdS/CFT into the Einstein Field Equations (EFE), forming the
Quantum-Temporal Field Theory of Variations (QTFV) gravity model.


7.1     Classical Einstein Field Equations

The standard EFE describe spacetime curvature due to energy-momentum:

                                                1              8πG
                                           Rµν − gµν R + Λgµν = 4 Tµν                                              (20)
                                                2               c

where Rµν is the Ricci curvature tensor, R the Ricci scalar, gµν the metric tensor, Tµν the stress-energy tensor, Λ the
cosmological constant, and G, c are fundamental constants.


7.2     QTC Oscillations: Temporal Stress-Energy

QTCs introduce a periodic quantum contribution to spacetime. The QTC stress-energy tensor is:

                                                   1
                                   QTC
                                       = ∂µ C∂ν C − gµν g αβ (∇α C)(∇β C) − V (C)
                                                                                 
                                  Tµν                                                                              (21)
                                                   2

with:

         • C(t, x): QTC field amplitude.
                              P∞
         • V (C) = 21 m2 C 2 + n=2 gn C n : Potential, where m is the QTC mass and gn couple sub-variations.

This term induces oscillatory curvature, detectable as time-periodic gravitational waves.


                                           Time Variations Theory © 2024 - Citizen Gardens                Page 7 of 10
                                             Licensed Under MIT and CC BY-NC-SA 4.0.
Preprint - PrimeAI Enhanced Template


7.3   Time Variations: Variation Flux Tensor

TVT’s infinite variations contribute a flux of timeline divergence:

                                                       X
                                              Vµν =            αi (∂µ ϕi ∂ν ϕi − gµν Li )                    (22)
                                                           i

where:

         • ϕi (t, x): Scalar field for variation path i.
                                                                  P
         • αi : Probability amplitudes (e.g., from |ΨT ⟩ =           i αi |Ci ⟩).

         • Li = 12 g αβ (∇α ϕi )(∇β ϕi ) − U (ϕi ): Lagrangian density.

Vµν modifies causal structure, potentially observable as curvature fluctuations.


7.4   Holographic Entanglement: Geometric Correction

From AdS/CFT, variation entropy maps to bulk geometry:

                                                                    Area(γvar )
                                                           Svar =                                            (23)
                                                                      4GN

where γvar is the minimal surface bounding variation regions. This induces a metric correction:

                                                        (holo)
                                                      δgµν     = κ∇µ ∇ν Svar                                 (24)

with κ a coupling constant. This term acts as a dynamic cosmological pressure.


7.5   Enhanced Field Equation

The QTFV-enhanced EFE is:

                               1              8πG  matter    QTC
                                                                       
                          Rµν − gµν R + Λgµν = 4 Tµν       + Tµν  + Vµν + κ∇µ ∇ν Svar                        (25)
                               2               c

This incorporates:

            matter
         • Tµν     : Classical matter.
            QTC
         • Tµν  : QTC oscillations.

         • Vµν : Variation flux.

         • κ∇µ ∇ν Svar : Holographic entanglement.


7.6   Physical Implications and Predictions

         • QTC Oscillations: Induce log-periodic gravitational waves, testable via LISA or LIGO-X.


                                              Time Variations Theory © 2024 - Citizen Gardens        Page 8 of 10
                                                Licensed Under MIT and CC BY-NC-SA 4.0.
Preprint - PrimeAI Enhanced Template


         • Variation Flux: Causes curvature anomalies, potentially spike-like gravitational events.

         • Holographic Entropy: Drives a dynamic Λ-like term, observable as entanglement-modulated dark energy.


      article amsmath, amssymb



8     QTFV-LQG Synthesis: Oscillating Spin-Network Theory of Time

This section formalizes the integration of the Quantum-Temporal Field Theory of Variations (QTFV) with Loop
Quantum Gravity (LQG), yielding a spacetime model where quantized geometry oscillates with temporal variations.


8.1    Core Postulates


Postulate 1 (Quantum Temporal Geometry). Spacetime is a spin network Γ = (V, E), with vertices v ∈ V as
Quantum Time Crystals (QTCs) Cv (t) and edges e ∈ E as variation transition channels.

      Postulate 2 (Variation-Embedded Dynamics). The Hamiltonian constraint is:

                                                        X 1                           X
                           ĤQTFV-LQG = ĤLQG +                    (∂t Cv )2 + V (Cv ) +  λe (t)eiωe t                        (26)
                                                               2
                                                        v∈V                                     e∈E


where V (Cv ) = 12 m2 Cv2 + λCv4 .


8.2    QTC-Spin Network Hybrid


The quantum state is:
                                                                                          !                       !
                                         X                              O                           O
                            |ΨΓ ⟩ =                 ψ({je }, {αv })           |Cv (αv )⟩        ⊗         |je ⟩               (27)
                                      {je },{αv }                       v∈V                         e∈E



8.3    Spinfoam Path Integral


The spin foam amplitude incorporates QTC variations:

                                                                      2
                                                     ei dt[ 2 (∂t Cv ) −V (Cv )]
                           XY                       Y R 1                        Y
                      Z=     (2jf + 1)e−γjf (jf +1)                                eiωe τe −Γe τe                             (28)
                            F    f                                 v                                  e


8.4    Variation Entropy Operator


Define:
                                          1      X       p
                                Svar =       min   8πγℓ2P je (je + 1) |⟨Ce (t)|Ce (0)⟩|2                                      (29)
                                         4GN E⊂E
                                                       e∈E


                                              Time Variations Theory © 2024 - Citizen Gardens                         Page 9 of 10
                                                Licensed Under MIT and CC BY-NC-SA 4.0.
Preprint - PrimeAI Enhanced Template


8.5   Key Predictions

       • QTC-Driven Cosmic Bounce: ⟨Cv (t)⟩ ∼ cos(Ωt) pre-Big Bang, testable via cosmological bounce
         signatures.

       • Spin-Network Time Loops: Non-zero ⟨V̂τe ⟩ for closed edges, predicting retrocausal effects.

       • Spacetime Foam Fluctuations: ∆gµν ∼ δSvar , observable as Planck-scale noise.


8.6   Experimental Probes

       • Quantum Simulator: Use a 16-qubit IBM processor to encode Γ and measure Svar -induced decoherence.

       • Holographic MERA: Simulate Svar in an AdS3 -like geometry.

       • Gravitational Waves: Detect log-periodic noise above 103 Hz with LIGO upgrades.




                                        Time Variations Theory © 2024 - Citizen Gardens                Page 10 of 10
                                          Licensed Under MIT and CC BY-NC-SA 4.0.
