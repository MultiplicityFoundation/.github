---
title: '**Comprehensive Mathematical Overview of Parity-Time (PT) and Anti-PT States
  in Bragg Gratings in Spherical Coordinates with Multiplicity Theory**'
slug: comprehensive-mathematical-overview-of-parity-time-pt-and-anti-pt-states-in-bragg-gratings-in-spherical-coordinates-with-multiplicity-theory
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/algorithms/Bragg Gratings.md
  last_synced: '2026-03-20T17:17:16.448209Z'
---

### **Comprehensive Mathematical Overview of Parity-Time (PT) and Anti-PT States in Bragg Gratings in Spherical Coordinates with Multiplicity Theory**

#### **1. Background**

Bragg gratings are periodic structures with refractive index modulations
that exhibit PT and anti-PT symmetric behaviors when gain and loss are
appropriately designed. Their properties can be analyzed using spherical
coordinates, encapsulating design parameters like phase (θ\\thetaθ),
real index perturbation (Δnr\\Delta n\_rΔnr​), and imaginary index
perturbation (Δni\\Delta n\_iΔni​)​.

Multiplicity Theory enhances this representation by introducing
interconnected eigenvalue dynamics and feedback loops, enabling advanced
control and scalability.

### **2. PT Symmetry and Spherical Representation**

#### **2.1 Refractive Index Distribution**

The refractive index distribution of a Bragg grating along the
propagation direction zzz is:

n(z)=nave+Δnrsin⁡(2πΛz)+jΔnicos⁡(2πΛz+θ),n(z) = n\_{\\text{ave}} +
\\Delta n\_r \\sin \\left(\\frac{2\\pi}{\\Lambda} z \\right) + j \\Delta
n\_i \\cos \\left(\\frac{2\\pi}{\\Lambda} z + \\theta
\\right),n(z)=nave​+Δnr​sin(Λ2π​z)+jΔni​cos(Λ2π​z+θ),

where:

-   naven\_{\\text{ave}}nave​: Average refractive index.

-   Δnr,Δni\\Delta n\_r, \\Delta n\_iΔnr​,Δni​: Real and imaginary
    > perturbation amplitudes.

-   Λ\\LambdaΛ: Period of the grating.

-   θ\\thetaθ: Phase offset between real and imaginary perturbations.

#### **2.2 Spherical Coordinates**

The spherical representation encodes the system\'s state:

-   **Radius**: r=∣nave∣r = \|n\_{\\text{ave}}\|r=∣nave​∣.

-   **Azimuthal Angle**: θ\\thetaθ, determines PT (θ=nπ\\theta =
    > n\\piθ=nπ) or anti-PT (θ=nπ±π/2\\theta = n\\pi \\pm
    > \\pi/2θ=nπ±π/2) symmetry.

-   **Polar Angle**: ϕ=cos⁡−1(Δni−ΔnrΔni+Δnr)\\phi = \\cos\^{-1}
    > \\left(\\frac{\\Delta n\_i - \\Delta n\_r}{\\Delta n\_i + \\Delta
    > n\_r}\\right)ϕ=cos−1(Δni​+Δnr​Δni​−Δnr​​), distinguishes broken
    > (Δni\>Δnr\\Delta n\_i \> \\Delta n\_rΔni​\>Δnr​) and unbroken
    > (Δni\<Δnr\\Delta n\_i \< \\Delta n\_rΔni​\<Δnr​) symmetry.

Special points on the PT sphere include:

-   **North Pole**: Δnr=0\\Delta n\_r = 0Δnr​=0 (extreme anti-PT broken
    > state).

-   **South Pole**: Δni=0\\Delta n\_i = 0Δni​=0 (extreme PT unbroken
    > state).

-   **Equator**: Exceptional Points (EPs) where Δnr=Δni\\Delta n\_r =
    > \\Delta n\_iΔnr​=Δni​.

### **3. Enhanced Mathematical Modeling with Multiplicity Theory**

#### **3.1 Eigenvalue Dynamics**

The system\'s eigenvalues transition between real (unbroken symmetry)
and complex (broken symmetry) states:

HPTψ=λψ,HPT=PTHPTPT,H\_{\\text{PT}} \\psi = \\lambda \\psi, \\quad
H\_{\\text{PT}} = P T H\_{\\text{PT}} P T,HPT​ψ=λψ,HPT​=PTHPT​PT,

where:

-   HPTH\_{\\text{PT}}HPT​: Non-Hermitian Hamiltonian.

-   PPP: Parity operator, Pz=−zP z = -zPz=−z.

-   TTT: Time-reversal operator, Ti=−iT i = -iTi=−i.

Incorporating Multiplicity Theory, the time-evolution of eigenvalues is:

λ(t)=λ0+∫0t\[M(t′,ψ)⋅∇C(t′)\]dt′,\\lambda(t) = \\lambda\_0 + \\int\_0\^t
\\left\[M(t\', \\psi) \\cdot \\nabla \\mathcal{C}(t\') \\right\]
dt\',λ(t)=λ0​+∫0t​\[M(t′,ψ)⋅∇C(t′)\]dt′,

where C(t)\\mathcal{C}(t)C(t) captures creative dynamics introduced by
feedback mechanisms.

#### **3.2 Tensor Coupling for PT Symmetry**

Tensor coupling in Multiplicity Theory extends the representation:

T(t,ψ)=∑i,jTij(t) ψiψj,T(t, \\psi) = \\sum\_{i,j} T\_{ij}(t) \\,
\\psi\_i \\psi\_j,T(t,ψ)=i,j∑​Tij​(t)ψi​ψj​,

where Tij(t)T\_{ij}(t)Tij​(t) encodes the interactions between real and
imaginary perturbations.

#### **3.3 Feedback Dynamics**

Recursive feedback loops adjust perturbations dynamically:

M(t+1)=M(t)+α∇C(t),M(t+1) = M(t) + \\alpha \\nabla
\\mathcal{C}(t),M(t+1)=M(t)+α∇C(t),

where α\\alphaα is a weighting factor and ∇C(t)\\nabla
\\mathcal{C}(t)∇C(t) evolves based on PT state transitions.

### **4. Applications in PT States of Bragg Gratings**

#### **4.1 Exceptional Points**

EPs occur at the equator of the PT sphere (ϕ=π/2\\phi = \\pi/2ϕ=π/2)
where:

Δnr=Δniandθ=nπ±π/2.\\Delta n\_r = \\Delta n\_i \\quad \\text{and} \\quad
\\theta = n\\pi \\pm \\pi/2.Δnr​=Δni​andθ=nπ±π/2.

At EPs, gratings exhibit unidirectional reflection, with the eigenvalues
becoming degenerate:

λ1=λ2,ψ1≠ψ2.\\lambda\_1 = \\lambda\_2, \\quad \\psi\_1 \\neq
\\psi\_2.λ1​=λ2​,ψ1​=ψ2​.

#### **4.2 Broken and Unbroken Symmetry**

-   **Broken Symmetry** (Δnr\<Δni\\Delta n\_r \< \\Delta
    > n\_iΔnr​\<Δni​): Amplifying passbands and localized fields.

-   **Unbroken Symmetry** (Δnr\>Δni\\Delta n\_r \> \\Delta
    > n\_iΔnr​\>Δni​): Stopbands and periodic fields.

### **5. Enhanced Spherical Representation with Multiplicity Theory**

Multiplicity Theory adds layers of complexity:

-   **Eigenvalue Multiplicity**: Tracks degeneracies at EPs.

-   **Quantum Coherence**: Captures phase relationships between real and
    > imaginary components: ψ(t)=∑iaieiλit.\\psi(t) = \\sum\_{i} a\_i
    > e\^{i\\lambda\_i t}.ψ(t)=i∑​ai​eiλi​t.

-   **Feedback Adaptation**: Modulates perturbations for tunable lasing
    > and sensing applications.

### **6. Conclusion**

Integrating PT and anti-PT states in Bragg gratings with Multiplicity
Theory enhances their mathematical representation and functional
adaptability. The spherical coordinate system, augmented by eigenvalue
dynamics, tensor coupling, and feedback loops, provides a robust
framework for exploring applications in tunable lasers, sensors, and
exceptional point engineering. This synergy advances both theoretical
understanding and practical design of optical systems.
