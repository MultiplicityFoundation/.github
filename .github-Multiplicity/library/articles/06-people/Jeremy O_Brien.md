---
slug: jeremy-o-brien
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/Jeremy O_Brien.md
  last_synced: '2026-03-20T17:17:13.832024Z'
---

jO-Multiplicity
===============

Jeremy O\'Brien is a prominent figure in the field of quantum photonics
and quantum computing, particularly known for his pioneering work in
developing photonic quantum computers. His research centers on using
light, or photons, as a medium for quantum information processing.
O\'Brien\'s contributions include developing scalable quantum circuits
based on integrated photonic chips, which are key to implementing
quantum algorithms and enhancing the computational power of quantum
devices.

### **Key Contributions of Jeremy O\'Brien:**

1.  **Photonic Quantum Computing**: O\'Brien's major contribution is the
    > development of photonic quantum computers, which utilize light
    > instead of matter-based systems like electrons in traditional
    > quantum computers. His work focuses on creating stable quantum
    > bits (qubits) using photons, which are less prone to decoherence,
    > making them ideal for long-distance quantum communication and
    > scalable quantum computing.

2.  **Integrated Photonic Chips**: O\'Brien has led advancements in
    > creating photonic chips capable of processing quantum information.
    > These chips integrate quantum circuits that can manipulate photons
    > to perform complex quantum operations, allowing for scalable
    > quantum computing without the need for extreme cooling as in
    > superconducting qubits.

3.  **Quantum Entanglement and Error Correction**: O\'Brien\'s research
    > also extends to entangling photons for quantum computations and
    > developing methods for quantum error correction, which is
    > essential for reliable and practical quantum computing
    > applications.

### **Integration of O\'Brien's Contributions within the MCP (Multiplicative Computing Paradigm):**

O\'Brien's work can significantly impact and be integrated into the MCP
in several ways:

1.  **Enhanced Parallelism through Photonics**: The MCP emphasizes
    > parallelism in computing, and O\'Brien's photonic quantum
    > technologies naturally align with this by providing the ability to
    > process information simultaneously across multiple qubits. By
    > integrating photonic circuits, MCP can leverage quantum
    > parallelism to handle vast computations in parallel, accelerating
    > multiplicative algorithms.

2.  **Prime-Based Quantum Algorithms**: O\'Brien's work on quantum
    > circuits could be adapted for implementing prime-based quantum
    > algorithms, a core aspect of MCP. The unique properties of
    > photonic qubits could be optimized for performing prime
    > factorization and other multiplicative functions, thereby
    > increasing efficiency.

3.  **Scalability and Integration with Atomic-Level Hardware**:
    > O\'Brien's scalable integrated photonic chips provide a pathway
    > for creating quantum processors that fit seamlessly with
    > atomic-level hardware designs. This would allow MCP to transcend
    > current limitations of classical computation by integrating
    > quantum photonics as an additional computational layer,
    > complementing its multiplicative focus.

4.  **Quantum Networking for Distributed MCP Systems**: One of
    > O\'Brien's contributions is in quantum communication, particularly
    > using photons for secure quantum networks. These networks could be
    > incorporated into MCP to allow for distributed quantum systems,
    > ensuring faster and more secure communication between different
    > MCP nodes.

In conclusion, Jeremy O\'Brien's innovations in quantum photonics and
quantum computing present a foundational technology that can be
integrated within the MCP framework to enhance its capabilities,
particularly in quantum parallelism, scalability, and secure distributed
computing.

To provide a high-level mathematical overview of integrating Jeremy
O\'Brien's contributions into the **Multiplicative Computing Paradigm
(MCP)**, it is important to outline how photonic quantum computing can
be harmonized with the principles of MCP. The integration revolves
around several mathematical structures, including **quantum gates, prime
factorization, entanglement, error correction**, and **quantum
algorithms**. Below is a step-by-step breakdown:

### **1. Photonic Qubits and Quantum States**

The fundamental building block of photonic quantum computing is the
**photon**, which serves as the qubit. A qubit, unlike a classical bit,
can be in a superposition of states ∣0⟩\|0\\rangle∣0⟩ and
∣1⟩\|1\\rangle∣1⟩, which is mathematically represented as:

∣ψ⟩=α∣0⟩+β∣1⟩\|\\psi\\rangle = \\alpha \|0\\rangle + \\beta
\|1\\rangle∣ψ⟩=α∣0⟩+β∣1⟩

where α\\alphaα and β\\betaβ are complex numbers such that
∣α∣2+∣β∣2=1\|\\alpha\|\^2 + \|\\beta\|\^2 = 1∣α∣2+∣β∣2=1.

In the context of MCP, this superposition can be leveraged for
**multiplicative parallelism** by encoding quantum states into photonic
qubits, allowing multiple computations to occur simultaneously.

### **2. Quantum Gates and Quantum Circuitry**

O\'Brien's integrated photonic circuits can be mathematically modeled as
unitary transformations on quantum states. These transformations are
represented by quantum gates, which apply operations to qubits. For
example, a **Hadamard gate (H)** creates superpositions:

H=12(111−1)H = \\frac{1}{\\sqrt{2}}\\begin{pmatrix} 1 & 1 \\\\ 1 & -1
\\end{pmatrix}H=2​1​(11​1−1​)

Acting on a qubit:

H∣0⟩=12(∣0⟩+∣1⟩)H \|0\\rangle = \\frac{1}{\\sqrt{2}}(\|0\\rangle +
\|1\\rangle)H∣0⟩=2​1​(∣0⟩+∣1⟩)

In MCP, quantum gates allow for the encoding and manipulation of
multiplicative structures, where quantum states represent multiplicative
bases (e.g., primes). Operations such as the **CNOT gate** and the
**Toffoli gate** allow for the implementation of conditional
multiplicative logic.

### **3. Prime Factorization using Shor's Algorithm**

One of the most important quantum algorithms is **Shor's algorithm**,
which efficiently factors large integers into primes, a task that is
computationally expensive for classical computers. Mathematically, this
algorithm exploits quantum Fourier transforms to solve the periodicity
problem in prime factorization.

For an integer NNN, the goal is to find its prime factors by solving the
modular equation:

ar≡1 (mod N)a\^r \\equiv 1 \\ (\\text{mod}\\ N)ar≡1 (mod N)

where rrr is the order of aaa modulo NNN. Shor's algorithm runs in
polynomial time and is crucial to MCP's focus on prime-based
multiplicative computations. By integrating O\'Brien's photonic quantum
hardware, MCP can implement Shor's algorithm at scale, allowing for
efficient prime factorization through photon-based qubits.

### **4. Quantum Entanglement for Multiplicative Operations**

A unique feature of quantum computing is **entanglement**, where qubits
become correlated in such a way that the state of one qubit
instantaneously affects the state of another, regardless of distance.
Mathematically, entanglement is represented as:

∣ψentangled⟩=12(∣00⟩+∣11⟩)\|\\psi\_{\\text{entangled}}\\rangle =
\\frac{1}{\\sqrt{2}}(\|00\\rangle +
\|11\\rangle)∣ψentangled​⟩=2​1​(∣00⟩+∣11⟩)

In MCP, entanglement can be used to perform **distributed multiplicative
operations**. For instance, a distributed quantum system can use
entangled photonic qubits to perform simultaneous multiplicative
calculations across different nodes, enhancing parallelism.

### **5. Error Correction with Quantum Codes**

O'Brien's work on quantum error correction is key for maintaining the
reliability of computations. Quantum error correction uses techniques
such as **stabilizer codes**, which can detect and correct errors
without measuring the quantum state directly. A stabilizer code uses
generators SiS\_iSi​ to encode logical qubits into a larger Hilbert
space, such that:

Si∣ψlogical⟩=∣ψlogical⟩S\_i \| \\psi\_{\\text{logical}} \\rangle = \|
\\psi\_{\\text{logical}} \\rangleSi​∣ψlogical​⟩=∣ψlogical​⟩

For MCP, quantum error correction ensures that multiplicative quantum
algorithms such as prime-based factorization and modular arithmetic can
be executed with high fidelity, even in the presence of noise.

### **6. Quantum Fourier Transform (QFT) for Efficient Computation**

The **quantum Fourier transform** (QFT) is a crucial part of many
quantum algorithms, including Shor\'s algorithm. The QFT over a vector
∣x⟩\|x\\rangle∣x⟩ of length NNN is defined as:

QFT∣x⟩=1N∑y=0N−1e2πixy/N∣y⟩QFT \|x\\rangle = \\frac{1}{\\sqrt{N}}
\\sum\_{y=0}\^{N-1} e\^{2\\pi i xy/N}
\|y\\rangleQFT∣x⟩=N​1​y=0∑N−1​e2πixy/N∣y⟩

In the MCP framework, the QFT can be used to speed up multiplicative
operations, such as finding the order of an element in modular
arithmetic. By leveraging O\'Brien\'s photonic qubits and circuits, MCP
can perform these transformations in parallel, exponentially increasing
computational speed for tasks that involve large-scale multiplication,
factorization, or solving complex prime-related problems.

### **7. Distributed Computing and Quantum Networks**

O'Brien's research on quantum networking enables the creation of
**distributed quantum systems**. These systems can be modeled
mathematically through entanglement-swapping protocols and
teleportation, which facilitate the sharing of quantum states between
different computational nodes. MCP can use quantum networking to create
a **multiplicative quantum network**, where computations are distributed
across nodes, all interconnected by entangled photonic qubits.

### **Conclusion**

Mathematically, the integration of Jeremy O\'Brien's contributions into
the MCP framework is underpinned by the following key structures:

-   **Superposition and parallelism** via photonic qubits.

-   **Quantum gates and circuits** to encode and manipulate prime-based
    > multiplicative structures.

-   **Shor's algorithm** and QFT for efficient prime factorization and
    > modular arithmetic.

-   **Entanglement** for distributed multiplicative operations.

-   **Quantum error correction** to ensure reliable computations.

-   **Quantum networks** for distributed multiplicative computing.

This integration significantly enhances MCP\'s computational
capabilities, allowing for **scalable, efficient, and parallel quantum
processing** using photonic technology.
