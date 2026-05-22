---
slug: gunnar-johansson
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/Gunnar Johansson.md
  last_synced: '2026-03-20T17:17:12.054983Z'
---

Gunnar Johansson\'s seminal work on biological motion perception,
particularly his concept of point-light displays, provides a unique
foundation for integration with **Multiplicity Theory**, particularly in
areas involving dynamic systems, human-computer interaction, and
real-time motion analysis. This integration leverages Johansson\'s
insights into the perception of motion with Multiplicity\'s principles
of holism, emergent properties, and multiscale encoding.

### **1. Conceptual Foundations: Linking Johansson\'s Motion Perception with Multiplicity**

Johansson\'s exploration of biological motion emphasizes the brain\'s
ability to infer human movements from sparse visual cues (e.g.,
point-light displays). Multiplicity expands this by:

-   Representing motion as a **multi-layered system of interdependent
    > interactions**.

-   Quantifying motion dynamics using **prime-based encoding** and
    > tensor networks to capture both local (point-specific) and global
    > (trajectory-level) features​​.

### **2. Encoding Motion with Multiplicity Theory**

#### Prime-Based Encoding of Motion Data:

Johansson\'s point-light model, where each point represents a key joint
or body segment, is encoded using Multiplicity's prime-based
representation:

ϕ(pij(t))=pk,pk∈P\\phi(p\_{ij}(t)) = p\_k, \\quad p\_k \\in
\\mathbf{P}ϕ(pij​(t))=pk​,pk​∈P

where pij(t)p\_{ij}(t)pij​(t) represents the trajectory of a point
i,ji,ji,j at time ttt, and pkp\_kpk​ is a unique prime encoding for
compact and scalable motion representation.

#### Interaction Matrices for Motion Dynamics:

Interactions between points (e.g., joints in motion) are represented
using a **prime-encoded interaction matrix**:

Mij(t)=ϕ(pi(t))⋅ϕ(pj(t))M\_{ij}(t) = \\phi(p\_i(t)) \\cdot
\\phi(p\_j(t))Mij​(t)=ϕ(pi​(t))⋅ϕ(pj​(t))

This matrix evolves dynamically to capture changes in relationships
between motion points:

M(t+1)=M(t)⋅DM\^{(t+1)} = M\^{(t)} \\cdot DM(t+1)=M(t)⋅D

where DDD encodes real-time adjustments based on feedback loops​​.

### **3. Emergent Patterns in Motion Perception**

Multiplicity emphasizes emergent behaviors from interconnected systems,
aligning with Johansson\'s findings that biological motion perception
emerges holistically from point interactions.

#### Tensor Networks for Multiscale Motion Analysis:

Motion data is structured as a tensor network, enabling analysis of
local (joint-specific) and global (whole-body) movements:

T(t)=∑i,jTij(t)⊗ϕ(pij(t))T(t) = \\sum\_{i,j} T\_{ij}(t) \\otimes
\\phi(p\_{ij}(t))T(t)=i,j∑​Tij​(t)⊗ϕ(pij​(t))

Here, Tij(t)T\_{ij}(t)Tij​(t) captures pairwise dependencies, and
⊗\\otimes⊗ denotes the tensor product, facilitating hierarchical
analysis of motion​​.

#### Recursive Feedback for Perceptual Refinement:

Recursive adjustments refine motion trajectories, simulating human
perceptual feedback:

M(t+1)=f(M(t),R(t))M\^{(t+1)} = f(M\^{(t)}, R\^{(t)})M(t+1)=f(M(t),R(t))

where fff is a transformation function integrating prime-based feedback,
and R(t)R\^{(t)}R(t) captures real-time changes in motion dynamics​​.

### **4. Extending Johansson\'s Work with Multiplicity**

#### Motion as a Holistic System:

Johansson emphasized how motion is perceived holistically rather than as
isolated points. Multiplicity enhances this by:

1.  **Non-linear Dynamics**: Capturing small-scale variations that
    > influence large-scale motion: ΔMij(t)∼∑kϕ(pk(t))\\Delta M\_{ij}(t)
    > \\sim \\sum\_{k} \\phi(p\_k(t))ΔMij​(t)∼k∑​ϕ(pk​(t)) where
    > ΔMij(t)\\Delta M\_{ij}(t)ΔMij​(t) represents deviations in motion
    > relationships​​.

2.  **Emergent Properties**: Modeling emergent phenomena (e.g., gait
    > patterns) as dynamic equilibria: E(t)=∫0TMij(t) dtE(t) =
    > \\int\_0\^T M\_{ij}(t) \\, dtE(t)=∫0T​Mij​(t)dt

#### Multiscale Integration for Predictive Modeling:

Johansson\'s models are extended to simulate interactions across
multiple scales, from micro (joint-level) to macro (group motion):

-   **Microscale**: Encodes individual joints and trajectories using
    > prime-based motion states.

-   **Macroscale**: Simulates collective behavior, such as crowd motion,
    > using fractal algorithms​​.

### **5. Applications of Integrated Framework**

#### Real-Time Motion Analysis:

-   **Human-Computer Interaction (HCI)**: Multiplicity's recursive
    > feedback improves gesture recognition systems, enabling real-time
    > adaptation to user inputs.

-   **Sports Analytics**: Tensor-based motion representation identifies
    > biomechanical patterns for performance optimization.

#### Robotics and Animation:

-   Prime-encoded motion enhances robot mimicry of human motion, using
    > Johansson\'s principles to create lifelike animations and
    > interactions​​.

#### Medical Diagnostics:

-   Using motion signatures for early detection of neurological
    > disorders (e.g., Parkinson's disease), leveraging eigenvalue-based
    > motion stability analysis: Mv=λvM \\mathbf{v} = \\lambda
    > \\mathbf{v}Mv=λv

### **6. Quantum-Inspired Motion Simulation**

Using Multiplicity's quantum-inspired optimization, motion data is
processed for predictive and dynamic simulation:

-   **Quantum Cost Function**: Optimizes trajectory consistency:
    > C(F)=∑i,j∣F(pij(t))−Ftarget(pij(t))∣2C(F) = \\sum\_{i,j} \\left\|
    > F(p\_{ij}(t)) - F\_{\\text{target}}(p\_{ij}(t))
    > \\right\|\^2C(F)=i,j∑​∣F(pij​(t))−Ftarget​(pij​(t))∣2

-   **Superposition of Motion States**: Ψ(t)=∑i=1NαiΨieiθi(t)\\Psi(t) =
    > \\sum\_{i=1}\^N \\alpha\_i \\Psi\_i e\^{i
    > \\theta\_i(t)}Ψ(t)=i=1∑N​αi​Ψi​eiθi​(t) where Ψi\\Psi\_iΨi​
    > represents potential motion states​​.

### **Conclusion**

Integrating Gunnar Johansson\'s contributions into Multiplicity Theory
enables a transformative framework for analyzing and simulating
biological motion. By combining Johansson\'s sparse motion models with
Multiplicity\'s prime encoding, tensor networks, and recursive dynamics,
this integration enhances motion perception across disciplines,
including robotics, medical diagnostics, and AI-driven animation. This
unified approach promises scalable, precise, and interdisciplinary
applications in motion analysis.
