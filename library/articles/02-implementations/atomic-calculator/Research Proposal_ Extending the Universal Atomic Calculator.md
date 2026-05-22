---
slug: research-proposal-extending-the-universal-atomic-calculator
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/atomic-calculator/Research Proposal_ Extending the Universal
    Atomic Calculator.md
  last_synced: '2026-03-20T17:17:15.449161Z'
---

**Research Proposal: Extending the Universal Atomic Calculator Framework to Complex Materials Simulation**
==========================================================================================================

**1.0 Foundational Success and Vision**
---------------------------------------

This research proposal builds upon the demonstrated success of the
Universal Atomic Calculator (UAC), a novel computational paradigm that
has achieved chemical-accuracy simulations of fundamental molecules. Our
objective is to extend this proven framework, scaling its application
from simple diatomic systems to industrially and scientifically relevant
complex materials. This work represents the next critical step in
transitioning a breakthrough theoretical concept into a powerful tool
for scientific discovery.

The core concept of the UAC is a paradigm shift in quantum computation.
It is founded on the principle of \"atomic self-simulation\"---the
insight that the intrinsic physical behaviors of atomic systems can be
directly harnessed as a computational resource. Instead of building a
general-purpose computer, the UAC framework maps the fundamental
principles of atomic physics directly to computational primitives.
Electron probability distributions are mapped to qubit superposition
states, electromagnetic interactions are mapped to entanglement
operations, and wavefunction collapse is mapped to quantum measurement.
This transforms a neutral-atom quantum processor into a specialized
calculator for evaluating the exponential state spaces of molecular
systems.

The foundational viability of the UAC has been experimentally validated
on state-of-the-art quantum processing units. These initial
demonstrations achieved the benchmark standard of chemical accuracy for
well-understood molecular systems, providing a solid empirical basis for
the research proposed herein.

-   **Hydrogen (H₂):** Achieved chemical accuracy for the ground-state
    > energy with a final error of 1.3 ± 0.8 mHa using a **4-qubit**
    > simulation.

-   **Lithium Hydride (LiH):** Achieved chemical accuracy with a final
    > error of 2.9 ± 2.1 mHa, successfully scaling the demonstration to
    > a **12-qubit** system.

The conceptual novelty of the UAC framework, which underpins its
efficiency and potential, can be distilled into four key
differentiators:

-   **Atomic Self-Simulation:** The recursive and philosophically potent
    > idea of using the physics of atomic systems to compute the
    > properties of other atomic systems.

-   **Hardware-Native Co-design:** A methodology that designs algorithms
    > specifically around the physical phenomena of the hardware---in
    > this case, the long coherence of nuclear spins and
    > Rydberg-mediated interactions---to achieve maximum resource
    > efficiency.

-   **The Calculator Metaphor:** Framing the quantum system as a
    > specialized calculator, rather than a universal computer, focuses
    > its purpose on efficiently evaluating complex exponential state
    > spaces, which is where quantum systems hold a distinct advantage.

-   **The Generalization Pathway:** The framework provides a systematic
    > template for mapping the principles of any physical system to a
    > set of computational primitives, offering a clear path to
    > leveraging other quantum technologies.

Despite these foundational successes, the UAC framework\'s application
is currently constrained by hardware scale, a technological limitation
that this proposal directly seeks to address.

**2.0 Problem Statement: The Frontier of Computational Scale**
--------------------------------------------------------------

The central challenge this proposal addresses is the scaling of the
Universal Atomic Calculator beyond its initial proof-of-concept
demonstrations. While the UAC\'s principles have been validated with
chemical accuracy, its application has been restricted to small-scale
diatomic molecules. This limitation, while understandable for a nascent
technology, prevents its immediate application to the complex materials
and chemical processes of significant industrial and scientific
interest, thereby hindering the realization of its full potential.

The primary limitation of the current work is that the UAC\'s
demonstration is confined to systems of **12 qubits or fewer**. This
scale is insufficient, representing less than a third of the qubit
resources required for materials of even moderate complexity, such as
FeS. This gap between demonstrated capability and practical application
represents a critical barrier that must be overcome to unlock the UAC\'s
transformative power.

The following table starkly contrasts the complexity of molecules
successfully simulated to date with the class of materials this research
targets, highlighting the computational leap required.

  System                   Required Qubits (minimum)
  ------------------------ ---------------------------
  Hydrogen (H₂)            4
  Lithium Hydride (LiH)    12
  Iron(II) Sulfide (FeS)   40

This proposal outlines a specific, actionable, and targeted research
plan to decisively cross this computational frontier.

**3.0 Proposed Research: Simulating Iron(II) Sulfide (FeS)**
------------------------------------------------------------

The core objective of this research is to extend and validate the
Universal Atomic Calculator framework by performing the first
chemical-accuracy simulation of a complex, transition-metal compound:
Iron(II) Sulfide (FeS). This work will bridge the gap between
small-scale demonstration and large-scale application, establishing a
clear pathway toward practical quantum advantage in computational
chemistry.

The selection of FeS as the target molecule is deliberate. Simulating
FeS requires a minimum of **40 qubits**, representing a significant and
meaningful leap in computational complexity beyond the **12-qubit** LiH
simulation. Successfully modeling a transition-metal compound like FeS,
with its intricate electron correlation effects, will serve as a
definitive proof-of-concept for the UAC\'s scalability. It will validate
that our \'calculator\' can handle the complex \'equations\' posed by
transition-metal chemistry, which are intractable for classical devices.

The projected resource requirements for the FeS simulation, based on our
scaling analysis, are as follows:

-   **Qubit Requirement:** 40 qubits

-   **Projected Gate Depth:** 80

-   **Projected Measurement Shots:** 10⁷

This research will be guided by a central question that addresses the
core challenge of scalability:

Can the UAC\'s hardware-native co-design principles, proven effective
for simple hydrides, be scaled by a factor of \>3x in system size to
maintain chemical accuracy for a transition-metal compound, thereby
crossing a critical threshold for industrial relevance?

To answer this question, we will employ a robust technical methodology
built upon the validated UAC framework, leveraging next-generation
quantum hardware.

**4.0 Technical Approach and Methodology**
------------------------------------------

Our methodology leverages the established UAC computational
framework---mapping atomic functions to computational primitives (Table
1)---while scaling the hardware implementation to meet the expanded
computational demands of the FeS simulation. This approach minimizes
theoretical risk by building upon a proven foundation and focuses
resources on the primary engineering and experimental challenge:
scaling.

To meet the **40-qubit** requirement for the FeS simulation, a critical
evaluation of available hardware is necessary. The initial
demonstrations were performed on the Pasqal Orion platform, which was
sufficient for the shallow circuits of H₂ and LiH. However, the
projected gate depth of 80 for FeS makes **long coherence time the
single most critical hardware parameter.** We therefore identify
neutral-atom platforms utilizing hybrid nuclear-spin encoding as
essential candidates. A platform such as that developed by **Atom
Computing**, with a specified coherence time of **3 s**, is the
presumptive choice, pending rigorous benchmarking against other leading
systems. This capability is essential for minimizing decoherence errors
during the execution of deeper quantum circuits.

The algorithmic kernel for this work will be the **Variational Quantum
Eigensolver (VQE)**, which has already been successfully deployed. We
will use the established hardware-efficient ansatz, which is
specifically optimized for the physical connectivity of neutral-atom
processors by **restricting entanglement operations to atom pairs within
the Rydberg blockade radius**. This hardware-native approach ensures
optimal gate execution and minimizes circuit depth.

Addressing the challenge of increased error rates in larger quantum
systems is a cornerstone of our technical plan. We will build upon the
proven error mitigation techniques successfully applied in our
foundational work, including **Zero-Noise Extrapolation (ZNE)** and
**Symmetry Verification**. This project also aligns with the broader
roadmap towards fault tolerance; the target hardware platforms are
actively developing logical qubit encoding schemes, and our work will
provide critical data for validating these approaches at the
**40-qubit** scale, consistent with the scaling law for surface codes.

This technical approach provides the foundation for a structured
research plan with clear, achievable milestones.

**5.0 Research Plan and Milestones**
------------------------------------

The proposed work is structured according to a clear, multi-year
strategic roadmap with defined, measurable milestones. This plan ensures
methodical progress, provides regular benchmarks for success, and aligns
the research with a concrete timeline for achieving its primary
objective.

1.  **Year 1 (2026): Foundational Scaling and Platform Integration**

    -   **Q1-Q2:** Benchmark and select the optimal \>40 qubit
        > neutral-atom hardware platform for the FeS simulation based on
        > fidelity, coherence, and qubit accessibility.

    -   **Q3-Q4:** Implement and validate logical qubit encoding schemes
        > on a small scale on the selected platform, adapting the
        > fault-tolerant extension model.

2.  **Year 2 (2027): Large-Scale Simulation and Analysis**

    -   **Q1-Q2:** Execute the full 40-qubit VQE simulation of the
        > ground-state energy of Iron(II) Sulfide (FeS) on the selected
        > platform.

    -   **Q3-Q4:** Perform a comprehensive analysis of the simulation
        > results, benchmark against classical computational chemistry
        > methods, and apply advanced error mitigation protocols to
        > achieve the target of chemical accuracy.

3.  **Year 3 (2028): Dissemination and Industrial Pathway**

    -   **Q1:** Publish the findings, including the FeS ground-state
        > energy calculation and hardware performance benchmarks, in a
        > high-impact, peer-reviewed scientific journal.

    -   **Q2-Q4:** Develop a prototype API endpoint for the FeS
        > calculator, demonstrating a clear and viable path toward a
        > future \"industrial quantum chemistry as a service\" model.

The successful execution of this plan will yield significant outcomes
with broad scientific and industrial impact.

**6.0 Anticipated Outcomes and Broader Impact**
-----------------------------------------------

The successful simulation of FeS will be a landmark achievement, serving
as a critical proof-of-concept that demonstrates a clear path from
fundamental quantum research to practical quantum advantage. This
project will not only validate the UAC\'s scalability but also unlock
new frontiers in computational science by providing a powerful new tool
for materials discovery.

The primary anticipated outcomes of this research are:

-   **Outcome 1: Validated Scalability.** This project will provide the
    > first definitive demonstration of the Universal Atomic Calculator
    > framework\'s applicability to complex materials, successfully
    > transitioning the paradigm from simple diatomic molecules to
    > industrially relevant compounds.

-   **Outcome 2: A New Computational Tool.** The project will deliver a
    > validated quantum algorithm and an end-to-end workflow for
    > accurately determining the ground-state energy of FeS, a molecule
    > that poses a significant challenge to classical simulation
    > methods.

-   **Outcome 3: Benchmarking Data.** This research will generate
    > high-fidelity performance data from a \>40 qubit quantum
    > simulation. This data will be an invaluable resource for the
    > broader quantum hardware and software community, guiding future
    > architectural improvements and algorithmic design.

Beyond these immediate deliverables, the broader implications of this
work are profound. By establishing a scalable method for quantum
simulation, this project will serve as a gateway for applying the UAC
framework to other high-impact computational domains:

-   **Materials Science:** Enabling first-principles band structure
    > calculations via Hubbard models, critical for understanding
    > strongly correlated materials like FeS, and accelerating the
    > design of novel materials with tailored electronic and magnetic
    > properties.

-   **Combinatorial Optimization:** Extending the framework\'s
    > state-space evaluation capabilities to solve complex optimization
    > problems relevant to logistics, finance, and network design using
    > algorithms like QAOA.

-   **Fundamental Physics:** Creating new avenues for simulating quantum
    > field theories and lattice gauge theories, allowing for
    > exploration of physical regimes inaccessible to classical
    > computation.

Ultimately, funding this research is an investment in maturing the
paradigm of atomic self-simulation, proving that the most complex
computational tools are not built, but discovered within the laws of
physics themselves.
