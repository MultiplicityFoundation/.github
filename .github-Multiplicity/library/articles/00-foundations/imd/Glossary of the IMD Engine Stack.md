---
slug: glossary-of-the-imd-engine-stack
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/imd/Glossary of the IMD Engine Stack.md
  last_synced: '2026-03-20T17:17:22.324317Z'
---

**An Accessible Glossary of the IMD Engine Stack**
==================================================

### **1.0 Introduction: A New Philosophy for System Safety**

Welcome! This glossary is designed to introduce you to the key software
components of a unique technology stack developed by the Institute of
Mathematical Discovery (IMD). The IMD is a research program building a
\"math-first\" system where properties like safety are core
architectural features, not optional add-ons.

This approach is fundamentally different from how most complex software
is built today. To make this idea more tangible, consider the following
analogy:

\"Imagine building a skyscraper where the safety codes are part of the
steel\'s molecular structure, not just a building inspector\'s checklist
after the fact.\"

Now, let\'s explore the foundational ideas that make this new approach
possible.

### **2.0 The Core Ideas: What Makes the IMD Stack Different?**

The entire IMD stack is built on a few key philosophical pillars. For a
beginner, the two most important ideas are captured in the table below.

  Core Idea                                         What It Means (in Simple Terms)
  ------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Multiplicity & Relations-First**                The system uses prime numbers as stable, unique IDs for every element and action. This allows it to perfectly track all interactions over time, focusing on the *relationships* between things.
  **Lawful Recursion & Mathematics as Alignment**   Safety and ethical rules are built in as strict mathematical constraints. This is like a train that can *only* run on its designated tracks, making it physically impossible to go to an unsafe destination.

These core concepts are enforced through a highly structured and
predictable process: the safety-first control loop.

### **3.0 The Heart of the System: The Safety-First Control Loop**

The IMD stack organizes its software components into a rigid and
predictable process called the \"safety-first control loop.\" This loop
governs how all components work together, ensuring every proposed action
is checked and validated before it can be executed. This process is
defined by \"Global Engine Contracts,\" which act as the system\'s
constitution.

The three most critical rules from these contracts are:

-   **Per-Tick Call Order:** A strict, unchangeable sequence that
    > dictates which engine runs when, ensuring predictability.

-   **Deterministic Replay:** The system must be able to perfectly
    > reproduce its past behavior, which is essential for auditing and
    > accountability.

-   **System Stability Limits:** Non-negotiable mathematical thresholds
    > are enforced to guarantee the system remains stable and
    > predictable at all times.

The software components that operate within this disciplined loop are
grouped below by their primary function.

### **4.0 The Core Components of the IMD Stack**

#### **4.1 Data and Structure Engines: The Foundation**

This group of engines provides the raw data, structural health
diagnostics, and immutable records that the rest of the system relies
on.

### **PQH --- Prime Quantum Hamiltonian**

The PQH provides the essential spectral data---the system\'s \"vital
signs\"---used for analysis and decision-making. By providing a
real-time, mathematically precise snapshot of the system\'s health, the
PQH data allows the ACE safety module to verify stability *before* an
action is proposed, preventing the system from entering unstable states
in the first place.

### **Archivum Ledger**

The Archivum Ledger acts as the immutable, official record-keeper for
the entire system. It logs all states, operations, and safety
certificates to create a perfect, unchangeable audit trail. This makes
the core idea of \"Lawful Recursion\" a practical reality by ensuring
every action can be traced back to a provably valid state.

### **Sato--Tate / Frobenius Sampler**

This engine acts as an early-warning system that monitors the system\'s
structural health by analyzing spectral distributions. By detecting
subtle deviations, it provides critical intelligence to the SPASC
attention module and the ACE safety layer, enabling them to preemptively
tighten constraints and prevent potential instabilities from cascading
into failures.

With this foundation of immutable records and real-time diagnostics in
place, we can now examine the control plane modules that use this
information to enforce the system\'s rigorous safety guarantees.

#### **4.2 Safety and Integration Modules: The Control Plane**

This group of modules acts as the \"control plane,\" managing the flow
of information and enforcing the system\'s safety rules.

### **Langlands Prism**

The Prism is the central integration layer, acting as the system\'s
\"conductor.\" It binds safety (ACE), structure (PETC), learning, and
control together, ensuring all components work in concert according to
the global contracts and that information flows in a lawful and
predictable manner.

### **ACE/SCN (Arithmetic Control Engine / Spectral Control Network)**

As one of the most mature and important components, ACE is the system\'s
primary safety layer. It operates on the spectral data provided by the
PQH to implement a \"projection-first\" safety mechanism. Before any
action can be executed, ACE projects the proposal into a pre-defined
\"lawful set\"---a mathematically defined space of acceptable outcomes.
This process produces a \"KKT certificate,\" which serves as a formal
mathematical proof that the action is safe and compliant, making the
system\'s lawfulness auditable by design.

These control modules establish the verified safe boundaries within
which the system can perform its core tasks.

#### **4.3 Execution and State Modules: The Action Layer**

These modules perform core tasks like attention and state updates, but
always operate within the safe boundaries established by the control
plane.

### **SPASC (Prime-Structured Attention + Certificates)**

SPASC is the system\'s attention mechanism. It uses prime numbers to
structure its focus, making its attention auditable and ensuring it is
always \"lawful\"---like a spotlight that can only point at pre-approved
targets. This structure allows every act of attention to be certified,
guaranteeing that the system\'s focus remains provably aligned with its
operational rules.

### **PIRTM Runtime (State Backbone)**

The PIRTM Runtime is the underlying substrate where the system\'s state
is updated. It enforces bounded, deterministic changes, ensuring that
every update is not only stable but also perfectly consistent with the
official record in the Archivum Ledger, preserving the integrity of the
system\'s history.

Finally, standing ready to intervene at any moment is the system\'s
ultimate failsafe.

#### **4.4 Safety Overrides: The Failsafe**

This component stands ready to intervene if the system ever deviates
from safe operational parameters.

### **Watchdog + OMEGA Node**

The Watchdog serves as the real-time \"emergency stop.\" It constantly
monitors a composite risk metric and can trigger a system freeze or
state rollback if safety limits are breached, ensuring failures are
contained immediately and cannot propagate.

### **5.0 A Note on Auxiliary Engines**

The IMD stack also includes auxiliary engines, such as the *Ethical
Ricci-Flow Regularizer*. It is important for a new learner to understand
that the source material describes these components as \"partially
implemented design sketches.\" Any claims about their advanced
capabilities, such as achieving AGI ethics or physical coherence, are
currently **UNPROVEN**. They represent promising research directions
rather than fully realized parts of the stack.

### **6.0 Conclusion: A System Built on Proof, Not Patchwork**

The IMD stack represents a fundamentally different approach to building
complex systems. Its design is \"certificate-driven,\" meaning every
significant action is accompanied by a mathematical proof of its
validity and safety. By building upon prime-encoded mathematics and a
rigid, safety-first control loop, the IMD aims to create systems where
lawful and safe operation is not an afterthought, but a provable
property of the system itself.
