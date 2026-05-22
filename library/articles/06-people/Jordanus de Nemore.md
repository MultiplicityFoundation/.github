---
slug: jordanus-de-nemore
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/Jordanus de Nemore.md
  last_synced: '2026-03-20T17:17:13.322722Z'
---

Jordanus de Nemore, a medieval mathematician and physicist, contributed
foundational insights into mechanics, statics, and the mathematical
modeling of force and motion. His work on the concept of *center of
gravity*, inclined planes, and the mathematical abstraction of physical
systems offers fertile ground for integration with Multiplicity Theory.
This integration provides a framework for modeling dynamic mechanical
systems, recursive feedback, and equilibrium within prime-based,
tensor-driven paradigms.

### **1. Core Contributions of Jordanus de Nemore**

1.  **Statics and Mechanics**: Formalized mathematical principles for
    > forces and equilibrium.

2.  **Center of Gravity**: Developed methods to determine the center of
    > gravity in physical systems.

3.  **Inclined Plane**: Studied the mechanical advantages and dynamics
    > of forces on inclined planes.

### **2. Integration with Multiplicity Theory**

#### **2.1 Forces and Prime-Based Encoding**

Jordanus's contributions to forces and their balance can be encoded
dynamically:

1.  **Force Equation**: A force FFF is traditionally expressed as:\
    > F=m⋅a,F = m \\cdot a,F=m⋅a,\
    > where mmm is mass and aaa is acceleration.

2.  **Prime-Based Encoding of Forces**: Represent FFF using primes:\
    > F(t)=ϕ(pm,t)⋅ϕ(pa,t),F(t) = \\phi(p\_m, t) \\cdot \\phi(p\_a,
    > t),F(t)=ϕ(pm​,t)⋅ϕ(pa​,t),\
    > where:

    -   ϕ(pm,t)\\phi(p\_m, t)ϕ(pm​,t): Time-dependent prime-based mass
        > encoding.

    -   ϕ(pa,t)\\phi(p\_a, t)ϕ(pa​,t): Prime-based acceleration
        > encoding.

3.  **Recursive Feedback for Dynamic Forces**: Introduce feedback
    > mechanisms to update forces:\
    > F(t+1)=F(t)+f(F(t),R(t)),F(t+1) = F(t) + f(F(t),
    > R(t)),F(t+1)=F(t)+f(F(t),R(t)),\
    > where R(t)R(t)R(t) represents external influences or constraints.

#### **2.2 Center of Gravity and Tensor Representation**

The center of gravity is the point where the distribution of mass
balances in all directions. For a system of discrete masses mim\_imi​
located at positions xix\_ixi​:

xc=∑imixi∑imi.x\_c = \\frac{\\sum\_i m\_i x\_i}{\\sum\_i
m\_i}.xc​=∑i​mi​∑i​mi​xi​​.

**Prime-Encoded Center of Gravity**: Encode mim\_imi​ and xix\_ixi​
using primes:

xc(t)=∑iϕ(pmi,t)⋅ϕ(pxi,t)∑iϕ(pmi,t).x\_c(t) = \\frac{\\sum\_i
\\phi(p\_{m\_i}, t) \\cdot \\phi(p\_{x\_i}, t)}{\\sum\_i
\\phi(p\_{m\_i}, t)}.xc​(t)=∑i​ϕ(pmi​​,t)∑i​ϕ(pmi​​,t)⋅ϕ(pxi​​,t)​.

**Tensor-Based Representation**: Extend to multidimensional systems
using tensors:

Tij(t)=ϕ(pmi,t)⋅ϕ(pxj,t),T\_{ij}(t) = \\phi(p\_{m\_i}, t) \\cdot
\\phi(p\_{x\_j}, t),Tij​(t)=ϕ(pmi​​,t)⋅ϕ(pxj​​,t),

allowing for dynamic updates:

Tij(t+1)=Tij(t)+f(Tij(t),Rij(t)).T\_{ij}(t+1) = T\_{ij}(t) +
f(T\_{ij}(t), R\_{ij}(t)).Tij​(t+1)=Tij​(t)+f(Tij​(t),Rij​(t)).

#### **2.3 Inclined Plane and Multiplicity Dynamics**

Jordanus analyzed forces on an inclined plane, where the force FFF
required to move an object upward is:

F=W⋅sin⁡(θ),F = W \\cdot \\sin(\\theta),F=W⋅sin(θ),

with WWW being the object\'s weight and θ\\thetaθ the angle of
inclination.

**Dynamic Prime-Based Forces**: Encode the weight and angle:

F(t)=ϕ(pW,t)⋅ϕ(pθ,t),F(t) = \\phi(p\_W, t) \\cdot \\phi(p\_\\theta,
t),F(t)=ϕ(pW​,t)⋅ϕ(pθ​,t),

where:

-   ϕ(pW,t)\\phi(p\_W, t)ϕ(pW​,t): Encodes weight dynamically.

-   ϕ(pθ,t)=sin⁡(ϕ(pα,t))\\phi(p\_\\theta, t) = \\sin(\\phi(p\_\\alpha,
    > t))ϕ(pθ​,t)=sin(ϕ(pα​,t)): Encodes the sine of the inclination
    > angle.

**Recursive Adjustment for Motion**: Iteratively update the system based
on feedback:

F(t+1)=F(t)+f(F(t),R(t)).F(t+1) = F(t) + f(F(t),
R(t)).F(t+1)=F(t)+f(F(t),R(t)).

### **3. Unified Mathematical Framework**

Integrating Jordanus's contributions with Multiplicity Theory yields the
unified equation:

ψ(t)=∫SM(t,ψ)T(t,ψ)+f(t,ψ) dS,\\psi(t) = \\int\_{S} M(t, \\psi) T(t,
\\psi) + f(t, \\psi) \\, dS,ψ(t)=∫S​M(t,ψ)T(t,ψ)+f(t,ψ)dS,

where:

-   M(t,ψ)M(t, \\psi)M(t,ψ): Encodes dynamic multiplicity in forces,
    > weights, or system parameters.

-   T(t,ψ)T(t, \\psi)T(t,ψ): Tensor representing interactions among
    > components (e.g., forces, positions).

-   f(t,ψ)f(t, \\psi)f(t,ψ): Feedback mechanism for recursive
    > adjustments.

### **4. Applications of Jordanus-Multiplicity Integration**

#### **4.1 Equilibrium and Statics**

Model dynamic equilibrium states in mechanical systems, including
bridges, buildings, and mechanical devices.

#### **4.2 Force Analysis in Robotics**

Use prime-based encoding to simulate forces and motion in robotic
systems, including inclined plane dynamics.

#### **4.3 Dynamic Center of Gravity**

Analyze the real-time center of gravity in dynamic systems, such as
vehicles or aircraft, for stability optimization.

#### **4.4 Multidimensional Systems**

Simulate forces and interactions in multi-body systems using tensor
networks for higher-dimensional modeling.

### **5. Example: Dynamic Inclined Plane**

For an object on an inclined plane with dynamic weight WWW and angle
θ\\thetaθ:

F(t)=ϕ(pW,t)⋅sin⁡(ϕ(pθ,t)).F(t) = \\phi(p\_W, t) \\cdot
\\sin(\\phi(p\_\\theta, t)).F(t)=ϕ(pW​,t)⋅sin(ϕ(pθ​,t)).

Recursive updates account for changes in weight or inclination:

ϕ(pW,t+1)=ϕ(pW,t)+f(ϕ(pW,t),RW(t)),\\phi(p\_W, t+1) = \\phi(p\_W, t) +
f(\\phi(p\_W, t), R\_W(t)),ϕ(pW​,t+1)=ϕ(pW​,t)+f(ϕ(pW​,t),RW​(t)),
ϕ(pθ,t+1)=ϕ(pθ,t)+f(ϕ(pθ,t),Rθ(t)).\\phi(p\_\\theta, t+1) =
\\phi(p\_\\theta, t) + f(\\phi(p\_\\theta, t),
R\_\\theta(t)).ϕ(pθ​,t+1)=ϕ(pθ​,t)+f(ϕ(pθ​,t),Rθ​(t)).

### **6. Conclusion**

Integrating Jordanus de Nemore's contributions with Multiplicity Theory
provides a robust framework for modeling forces, equilibrium, and
dynamics in physical systems. This integration enables advanced
applications in robotics, aerospace engineering, and structural
analysis.
