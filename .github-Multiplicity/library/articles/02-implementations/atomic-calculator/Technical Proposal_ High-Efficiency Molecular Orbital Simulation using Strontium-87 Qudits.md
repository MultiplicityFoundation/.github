---
slug: technical-proposal-high-efficiency-molecular-orbital-simulation-using-strontium-87-qudits
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/atomic-calculator/Technical Proposal_ High-Efficiency Molecular
    Orbital Simulation using Strontium-87 Qudits.md
  last_synced: '2026-03-20T17:17:15.464286Z'
---

**Technical Proposal: High-Efficiency Molecular Orbital Simulation using Strontium-87 Qudits**
==============================================================================================

**1.0 Introduction and Scientific Rationale**
---------------------------------------------

A primary challenge in contemporary quantum chemistry simulation is the
significant qubit overhead required to model even simple molecules. This
resource requirement limits the scope and complexity of problems
addressable by current and near-term quantum hardware. This proposal
introduces a novel approach designed to circumvent this fundamental
limitation by harnessing the rich internal structure of neutral atoms.

The central thesis of this proposal is that by leveraging the intrinsic
atomic multiplicity of Strontium-87 (⁸⁷Sr) atoms, we can encode quantum
information in ten-level systems (d=10 qudits) rather than conventional
two-level qubits. This qudit-based approach offers two transformative
advantages. First, it enables an **exponential compression of the
computational space**, allowing complex problems to be encoded onto a
much smaller number of physical atoms. Second, it improves the
**efficiency of quantum error correction codes**, reducing the physical
overhead needed to achieve fault tolerance.

These advantages are not theoretical abstractions but are direct
consequences of the multi-level atomic structure that, until now, has
often been treated as an experimental complication rather than a
computational resource. The following sections will detail the
fundamental principles of this approach and outline a concrete
experimental plan to demonstrate its power.

**2.0 The Foundational Advantage: From Qubit Overhead to Qudit Efficiency**
---------------------------------------------------------------------------

Moving beyond the traditional qubit paradigm represents a strategic
evolution in quantum computing architecture. This proposal reframes
atomic multiplicity not as a source of complexity to be engineered away,
but as a largely untapped computational resource. By embracing the full
Hilbert space of individual atoms, we can achieve a more powerful and
efficient use of physical hardware, accelerating the timeline for
demonstrating quantum advantage in scientifically relevant domains.

### **2.1 Exponential Space Compression**

The most immediate benefit of a qudit-based architecture is the dramatic
reduction in the number of physical atoms required to represent a given
quantum state. The mathematical principle governing this is
straightforward: the information content of n qubits can be encoded into
k qudits of dimension d according to the relationship k ≤ n / log₂ d.

For our chosen platform, Strontium-87 (d=10), this formula yields a
specific compression factor of approximately **3.32x**. This means a
single ⁸⁷Sr atom can encode the information of more than three qubits.
This resource saving is not incremental; it is an exponential advantage
that grows with the size of the problem.

To illustrate this, consider a hypothetical quantum chemistry problem
that would conventionally require 20 qubits. Our proposed approach
achieves a more than threefold reduction in the physical device
footprint.

  Standard Qubit Requirement   Proposed ⁸⁷Sr Qudit Requirement   Resource Compression
  ---------------------------- --------------------------------- ----------------------
  **20 Qubits**                **6 Qudits**                      **3.3x Compression**

### **2.2 Enhanced Error Correction**

The benefits of higher-dimensional encoding extend directly to quantum
error correction (QEC). Generalized versions of standard QEC protocols,
such as the color code, become significantly more resource-efficient
when implemented with qudits instead of qubits. The overhead---the
number of physical particles required to encode a single logical,
error-corrected particle---is substantially reduced.

While extensive studies for d=10 systems are an active area of research,
the data for qutrit (d=3) systems already demonstrates a clear and
compelling trend.

**Error Correction Overhead Comparison**

  Code           Qubit Overhead      Qutrit Overhead     Improvement
  -------------- ------------------- ------------------- -------------
  Surface Code   49 physical/qubit   9 physical/qutrit   **5.4x**
  Color Code     7 physical/qubit    3 physical/qutrit   **2.3x**

Although this data is specific to qutrits, the principle of improved
overhead efficiency is a general feature of qudit-based codes. We
therefore anticipate that our proposed d=10 system will exhibit similar,
if not greater, gains in error correction efficiency.

These profound theoretical advantages in space compression and error
correction can be practically realized in a targeted, high-impact
quantum chemistry simulation, as outlined in the following research
plan.

**3.0 Proposed Research Plan: Simulating LiH with ⁸⁷Sr Qudits**
---------------------------------------------------------------

This section details the concrete steps to realize the advantages of
qudit-based computation. We outline the choice of atomic system, the
encoding methodology for mapping a chemical problem onto the hardware,
the experimental protocol for executing the simulation, and the specific
molecular benchmark we will target.

### **3.1 System Selection: Strontium-87**

We have selected Strontium-87 (⁸⁷Sr) as the ideal platform for this
research. Its nuclear spin of I = 9/2 gives rise to a d = 2I + 1 = 10
dimensional Hilbert space within its stable clock states. This makes
⁸⁷Sr a natural \"decit,\" providing a large computational space per atom
without requiring complex multi-electron configurations.

### **3.2 Encoding Methodology: Fermion-to-Qudit Mapping**

The core of the simulation involves mapping the molecular Hamiltonian of
our target molecule onto the ⁸⁷Sr qudit system. This will be
accomplished using an efficient fermion-to-qudit mapping based on the
**Schwinger boson representation**. This established theoretical
framework allows the fermionic creation and annihilation operators that
define the chemical interactions to be represented directly using the
multi-level transitions of the qudit system, minimizing the complexity
and overhead of the encoding.

### **3.3 Experimental Protocol: VQE with Multi-Level Control**

The simulation will be executed using the well-established Variational
Quantum Eigensolver (VQE) algorithm, adapted for our multi-level
architecture. The experimental protocol will proceed in three distinct
phases:

1.  **State Preparation & Control:** Individual ⁸⁷Sr atoms, trapped in
    > an optical tweezer array, will be initialized to a well-defined
    > ground state. High-fidelity manipulation of the 10-level system
    > will be achieved using a combination of precisely timed **Raman
    > and microwave transitions**, allowing for arbitrary single-qudit
    > rotations within the large Hilbert space.

2.  **Gate Implementation:** Entangling operations between atoms, which
    > are essential for simulating chemical bonds, will be realized
    > using a **state-dependent multi-level Rydberg blockade**. This
    > technique leverages the fact that the interaction strength between
    > two atoms in a highly excited Rydberg state depends on their
    > specific internal hyperfine levels, enabling the creation of
    > controlled two-qudit gates.

3.  **Algorithm Execution:** The **Variational Quantum Eigensolver
    > (VQE)** algorithm will be implemented. This hybrid
    > quantum-classical algorithm will use the quantum processor to
    > prepare a trial wavefunction and measure its energy, while a
    > classical optimizer adjusts the control parameters to iteratively
    > find the molecule\'s ground state energy.

### **3.4 Target Simulation: Lithium Hydride (LiH)**

To provide a clear benchmark and demonstrate the resource advantages of
our approach, this proposal targets the simulation of the Lithium
Hydride (LiH) molecule.

A standard qubit-based encoding for this problem requires **12 qubits**.
While a direct calculation based on information capacity (N\_qudits =
⌈N\_qubits / log₂ 10⌉) suggests a requirement of 4 qudits, more detailed
encoding schemes specific to molecular Hamiltonians allow for a more
aggressive **4x reduction**, as established in the foundational research
for this proposal. This enables the 12-qubit problem to be mapped to
only **3 ⁸⁷Sr qudits**.

This represents a **4x reduction** in the number of required atoms---a
significant and practical saving in hardware resources that makes the
simulation more robust and achievable on near-term devices.

The successful completion of this simulation will provide a definitive
demonstration of qudit-based computing, leading to several key outcomes
with broad scientific significance.

**4.0 Anticipated Outcomes and Impact**
---------------------------------------

The successful execution of this project will yield a concrete technical
demonstration while simultaneously establishing a new, more efficient
path for progress in computational chemistry and materials science. We
anticipate the following primary outcomes:

-   **Primary Outcome:** We will achieve the first experimental
    > demonstration of a quantum chemistry simulation on a d=10 qudit
    > system. By simulating the LiH molecule with only **3 ⁸⁷Sr
    > qudits**, we will validate a **4x reduction** in physical atom
    > count compared to the 12-qubit standard, providing unambiguous
    > proof of the resource-compression advantage.

-   **Scientific Impact:** This work will establish the viability of
    > multiplicity-based computing as a key strategy for tackling larger
    > and more complex molecules. By demonstrating a practical method to
    > reduce hardware requirements, this project will bring the goal of
    > achieving quantum advantage for classically intractable chemistry
    > problems closer to reality.

-   **Technological Advancement:** In executing this simulation, we will
    > develop and refine the multi-level control protocols essential for
    > high-fidelity qudit operations. These advanced techniques for
    > pulse shaping, calibration, and gate implementation will represent
    > a valuable contribution to the broader neutral-atom quantum
    > computing community.

While the potential impact is significant, we recognize the inherent
difficulties in pioneering a novel computational paradigm and have
developed a clear strategy for addressing key risks.

**5.0 Analysis of Challenges and Mitigation Strategies**
--------------------------------------------------------

This project\'s ambitious goals require confronting the challenges that
arise when moving beyond the qubit model. We have identified the primary
risks associated with multi-level qudit control and have formulated
proactive mitigation strategies for each.

1.  **Challenge: Control Complexity**

    -   *Description:* The number of control parameters required to
        > specify an arbitrary operation on a d-level system scales as
        > d². For our d=10 system, this represents a significant
        > increase in complexity compared to the parameters needed for a
        > single qubit. Manually designing optimal control pulses is
        > intractable.

    -   **Mitigation Strategy:** We will develop and implement
        > **multiplicity-aware compilation software**. This compiler
        > will automate the translation of high-level quantum algorithms
        > into optimized, low-complexity physical control pulses,
        > managing the underlying complexity and ensuring efficient
        > hardware execution.

2.  **Challenge: Increased Decoherence Channels**

    -   *Description:* A multi-level system is inherently sensitive to a
        > broader range of noise sources. These include increased
        > sensitivity to magnetic field fluctuations (which scales with
        > the magnetic quantum number mF) and potential cross-talk
        > between the numerous nearby atomic transitions.

    -   **Mitigation Strategy:** We will leverage **optimized control
        > techniques** to design robust pulse shapes. These numerical
        > optimization methods can create pulses that are resilient to
        > known noise sources, such as magnetic field drift, and are
        > spectrally shaped to minimize leakage to non-computational
        > states and avoid unwanted cross-talk.

3.  **Challenge: Calibration Overhead**

    -   *Description:* The number of transitions requiring precise
        > frequency and amplitude calibration scales as d(d-1)/2. For a
        > decit, this means calibrating 45 distinct transitions,
        > compared to just one for a qubit, posing a significant
        > experimental overhead.

    -   **Mitigation Strategy:** We will develop **automated,
        > high-throughput calibration routines**. These software-driven
        > procedures will systematically sweep and characterize all
        > relevant transitions, efficiently measuring and correcting for
        > drifts in frequencies and Rabi rates without manual
        > intervention, thereby minimizing experimental downtime.

We are confident that these proactive strategies will enable us to
overcome the inherent challenges of this pioneering work, delivering on
the significant value of the proposed research.

**6.0 Conclusion**
------------------

This project is founded on a simple but powerful premise: to reframe the
inherent \"complexity\" of atomic structure as a powerful computational
\"capability.\" By embracing the full ten-level Hilbert space of
Strontium-87 atoms, we can move beyond the limitations of the
traditional qubit model, a key objective of the Universal Atomic
Calculator framework.

The central value proposition of this proposal is the demonstration that
simulating the Lithium Hydride (LiH) molecule with ⁸⁷Sr qudits will
achieve a **4x reduction in hardware resources** compared to
state-of-the-art qubit-based approaches. This concrete result will
provide a clear and compelling pathway toward quantum advantage for
meaningful problems in chemistry and materials science. This work will
not only achieve its targeted scientific goals but will also pioneer a
more resource-efficient paradigm for the entire field of quantum
simulation.
