---
slug: imd-overview-working-draft-v0-1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/imd/Imd Overview Working Draft V0 1.md
  last_synced: '2026-03-20T17:17:22.244009Z'
---

Institute of Mathematical Discovery (IMD)
Working overview v0.1 — grounded in current IMD specs and papers




0. Bottom line
     • What IMD is: A small, math‑first research program building a prime‑indexed, certificate‑driven stack
       for AI, control, and quantum / physical systems.
     • Core bet: you can encode structure, safety, and ethics directly into the math (primes, spectra,
       projections, invariants), not bolt them on as an afterthought.
     • Status:
     • Some parts are concrete and reproducible (ACE/SCN, PETC, ALP, Π‑kernel, engine contracts).
     • Others are speculative / UNPROVEN (global multiplicity metaphysics, DRMM‑level AGI claims,
       universal ethical constants).
     • Usefulness right now: most useful as a rigorous playground for lawful recursion and certified
       models; not yet a production platform.




1. Identity and scope

1.1 What IMD actually is

     • A research "institute" centered on:
     • Multiplicity Theory (prime‑based modeling of complex systems).
     • Prime‑Encoded Tensor Calculus (PETC).
     • Prime‑Indexed Recursive Tensor Mathematics (PIRTM).
     • A family of control and safety engines (ACE, SCN, Langlands Prism, Moonshine, SPASC, etc.).
     • It operates in tight collaboration with Citizen Gardens and related open research efforts.
     • Deliverables are primarily technical memoranda, specs, and reference code, not commercial
       products.

1.2 What IMD is not

     • Not a generic AI lab chasing benchmarks.
     • Not a cloud product, SaaS platform, or LLM vendor.
     • Not claiming new number‑theory theorems or physical laws.
     • Not yet a full AGI stack; anything in that direction is UNPROVEN and explicitly labeled as such in the
       docs.




                                                      1
2. Philosophical core: multiplicity and lawfulness
IMD’s worldview is built around a few core ideas:


    1. Multiplicity as the base object.
    2. Mathematical / physical systems are described as prime‑indexed multisets and operators rather
       than just vectors and matrices.
    3. Prime labels act as stable identities and channels for constraints.
    4. Relations‑first modeling.
    5. Focus on relations, feedback loops, and resonance instead of isolated objects.
    6. Hypergraphs and operator words (sequences of prime‑indexed operators) are the basic units of
       description.
    7. Lawful recursion.
    8. Any recursive system must carry:
            ◦ A contractive or non‑expansive update law (small‑gain, Lyapunov, or projection proof).
            ◦ Per‑channel invariants that are auditable and roll‑backable.
    9. Mathematics as alignment.
   10. Ethics / lawfulness are treated as constraints on trajectories (CSL, Λ y m, Mϕ, etc.), not as post‑hoc
       policy layers.
   11. Wherever possible, there is a path to zero‑knowledge proofs of lawfulness.

Some of this is hard math + code. Some is philosophy and UNPROVEN.




3. Core mathematical pillars
This is the base layer IMD keeps building on.


3.1 Multiplicity Theory

     • Treats complex systems (quantum, biological, social, astrophysical) as prime‑encoded interaction
       networks.
     • Each element gets a unique prime; multiplicities (exponents) encode intensity or recurrence.
     • Interaction matrices become products of primes; stability is analyzed spectrally.
     • Claims:
     • Can model stability and feedback better than generic linear models.
     • Shows promising behavior in simulations (GRNs, social networks, astrophysics).
     • Validation:
     • Partly validated via simulations and toy examples.
     • Extrapolations to physics / society are UNPROVEN and should be treated as hypotheses, not facts.

3.2 Prime‑Encoded Tensor Calculus (PETC)

     • A strict, certified encoding of tensor structure:
     • Tensors carry prime signatures (exponent vectors over primes).
     • Tensor product = addition of signatures; dual = negation; a multiplicity functor maps this to rational
       units.




                                                      2
     • Why it matters:
     • Provides a ledger‑like invariant for tensor operations.
     • Lets you check conservation, legality of contractions, and compositionality symbolically, separate
       from floating‑point numerics.
     • Status:
     • Formal laws are well‑defined and modest in scope.
     • Integrations into real tensor libraries are early; production deployment is UNPROVEN.

3.3 Prime‑Indexed Recursive Tensor Mathematics (PIRTM)

     • A broader framework where prime indices label recursive tensor channels over time.
     • Central ideas:
     • Track state evolution with prime‑sharded operators.
     • Use a global Multiplicity Constant Λ y m (and variants like Mϕ) as convergence / stability gates.
     • Intended use:
     • Backing runtime backbones (PIRTM engine, RPMT Evolver, DRMM operator) for recursive systems.
     • Status:
     • Conceptually coherent; specs and proofs cover local contraction conditions.
     • Full stack integration (quantum devices, AGI loops, etc.) is UNPROVEN.

3.4 Π‑kernel and Π‑atoms

     • Π‑kernel: a factorized projector kernel built from a family of Π‑atoms (projectors) that decompose a
       Banach or Hilbert space.
     • Properties:
     • Orthogonal or tight‑frame decomposition, with lossless recomposition.
     • Per‑atom update laws with local contraction (damped updates, Lipschitz bounds).
     • Per‑atom zk‑friendly audits (commitments per Π‑ID, batched proofs).
     • Role in IMD:
     • Provides the local building blocks for attention, control, and runtime state updates.

3.5 DRMM and Mϕ / Λ

ym


     • Dynamic Recursive Meta‑Mathematics (DRMM):
     • A prime‑indexed operator for recursive dynamics across quantum sensing, cognition, and other
       domains.
     • Used as a conceptual umbrella for real‑time recursive feedback (e.g., atomic clocks, AGI safety
       loops).
     • Mϕ (Multiplicity Constant) and Λ y m:
     • Proposed as attractor values / invariants for ethical or lawful recursion.
     • ϕ ≈ 0.618 is argued (via simulations) to minimize “ethical drift” in certain CSL dynamics.
     • Status:
     • Mathematically defined; simulations exist.
     • As universal laws of “ethical cognition” they are UNPROVEN.




                                                     3
4. Engine stack: how IMD actually runs things
IMD’s stack is organized as engines and modules with explicit contracts. Think of it as a safety‑first control
loop wrapped around prime‑encoded math.


4.1 Global engine contracts

The core engine spec defines:


     • A per‑tick call order (build spectra, estimate structure, compile policy, project safely, act, update
       runtime, log, watchdog).
     • Global constants:
     • Gap floors (relative and absolute) for spectral stability.
     • Small‑gain bounds.
     • Time budget per control tick.
     • Cross‑cutting requirements:
     • Deterministic replay (fixed seeds, versioned ops).
     • Telemetry for all metrics (gaps, budgets, norms, lawfulness scores).
     • Minimal acceptance tests for each engine.

This is one of the more concrete, implementation‑ready parts of IMD.


4.2 Core engines

High‑level roles only; each has a detailed contract elsewhere.


    1. PQH — Prime Quantum Hamiltonian


    2. Maintains the spectral object (Hecke‑like operators, prime‑indexed channels) used by higher layers.


    3. Provides eigenpairs, gaps, and diagnostics.

    4. Status: grounded in classical spectral theory; realistic but domain‑limited.


    5. CSL/Ξ Governor


    6. Compiles high‑level policies into trajectories in a Categorical Semantic Lawfulness (CSL) space.


    7. Enforces lawfulness budgets and acts as a gate between abstract goals and concrete control signals.

    8. Status: mathematically defined; implementation maturity depends on specific application.


    9. Archivum Ledger


   10. Immutable ledger of states, budgets, and certificates.


   11. Supports deterministic replay and audit.




                                                       4
  12. Status: technically straightforward; value depends on everything else being well‑designed.


  13. Sato–Tate / Frobenius Sampler


  14. Samples and monitors spectral distributions as a proxy for arithmetic or structural health (e.g.,
      Sato–Tate bands).


  15. Feeds diagnostics to attention and control modules.


  16. Ihara–Graph Zeta Sieve


  17. Operates on graphs / networks to tighten gaps and adjust masks (for SPASC and related modules).


  18. Provides monotone gap improvements with finite termination guarantees.


  19. Watchdog + OMEGA Node


  20. Real‑time safety trip.


  21. Monitors a composite risk metric; triggers margin boosts, projection freezes, or rollbacks within
      bounded delay.
  22. Design is explicitly small‑gain‑safe.

4.3 Core modules (IMD Core Modules)

   1. Langlands Prism (Integration Layer)


   2. Binds safety (ACE), structure (PETC), learning, and control.


   3. Routes flows, manages budgets, and preserves pipeline invariants (deterministic order,
      idempotence, budget conservation).


   4. Moonshine Operator (Speculative → Certified Controller)


   5. Zeta / automorphic‑weighted scalar controller.


   6. Consumes Ramanujan‑type bounds and gap data; constrained by ACE and SCN.

   7. Heavily theoretical; practical control gains are still UNPROVEN outside toy settings.


   8. SPASC (Prime‑Structured Attention + Certificates)


   9. Attention mechanism where masks and structure are prime‑typed.


  10. Enforces spectral certificates (slope upper bounds, gap bounds) and unitary internal blocks when
      certified.




                                                       5
11. PIRTM Runtime / State Backbone


12. The actual state‑update substrate.


13. Enforces bounded updates per tick, deterministic RNG, and ledger consistency.


14. Automorphic Learning (∞/CSL)


15. Training regime for models with finite automorphic invariance and prime‑structured masks.


16. Includes preregistration, lints, and pass/fail gates; ACE projection is in the loop.


17. Alpha Function (Unified Special‑Function Kernel)


18. Provides certified numerical transforms (special functions) with interval error bounds and stability
    flags.


19. Intended as a "safe math" backend for PQH/ACE/PETC; this is relatively standard numerical analysis
    with extra guardrails.


20. ACE/SCN (Arithmetic Control Engine + Spectral Control Network)


21. ACE: safety layer that projects control proposals into a constrained set using weighted‑ℓ¹ projection
    and KKT certificates.


22. SCN: deep‑ish network mapping spectral state to perturbations, with unitary‑constrained internal
    layers and spectral certificates (Weyl, Davis–Kahan).

23. This is one of the most mature, testable components; its scope is modest but real.


24. PGM–MPS (Multiplicity Backbone for M)


25. Formalizes the multiplicity operator M as a functor from signatures to Q×, backed by integer ledgers
    and sector weights.


26. Acts as a routing + stability object for other modules.


27. Π‑kernel (Factorized Projector Kernel)


28. Per‑atom proximal projector aggregating to a global operator.


29. Stabilizes attention and control; exports SlopeUB and Lyapunov‑style descent data.




                                                     6
4.4 Auxiliary engines

These are side‑modules that enforce stability, ethics, or calibration.


      • Λ y m Estimator: tracks multiplicity constant / entropy bounds, allocates ACE margin and Π‑steps.
      • RPMT Evolver: runtime backbone under PIRTM, with entropy‑based gates and convergence criteria.
      • PBQN (Prime Bayesian Quantum Network): PETC estimator with uncertainty + lawfulness priors;
        emits posterior budgets.
      • Narrative‑State Engine: cognitive gate; only allows actions when certain CSL metrics and an ethical
        “angle” are within bounds.
      • BEC Coherence Probe: physical coherence assay; ties spectral coherence of physical systems back
        into ACE budgets.
      • Fractal‑Cavity Capacitor: calibration for SPASC spectral proxies.
      • Ethical Ricci‑Flow Regularizer: curvature‑based drift control on feature manifolds.
      • Ramanujan‑Bound Filter: shrinkage prior for Moonshine / SCN weights based on automorphic
        bounds.
      • Prime‑Embedded Berry Phase / Prime Compactifier / Recursive Renormalizer / Gelfand–C
        Mapper:* various stabilizers, compactifiers, and verifiers for high‑dimensional dynamics.

Almost all of these are partially implemented design sketches. Some will work fine as standard numerical
procedures with a prime‑flavored twist; others (especially physical coherence / AGI ethics claims) are
UNPROVEN.




5. Application verticals
IMD’s machinery is pointed at several domains. In each, note what is real vs aspirational.


5.1 Arithmetic spectral control

      • ACE/SCN:
      • Exact Hecke operators on spaces of modular forms.
      • SCN uses unitary‑constrained blocks to map spectral states to control perturbations.
      • Arithmetic and stability guarantees are well‑defined and testable.

5.2 Atomic Language Processing (ALP)

      • Three‑layer prime‑encoded language stack:
      • L1: graphemic level with fixed primes by frequency.
      • L1.5: grapheme‑in‑context with EMA + isotonic rank adjustment.
      • L2/L3: morphemic / lexical levels with dynamic prime assignments under ACE constraints.
      • Uses PETC and ACE to keep ranks and associations stable under updates.
      • This is fairly concrete: there is reference code and standard matrix perturbation theory backing the
        guarantees.

5.3 ∞/CSL automorphic transformers

      • Transformers with:



                                                       7
     • Prime‑structured indices and finite group actions (AGL(1, p)).
     • Additive masking semantics compatible with Legendre / CRT embeddings.
     • Unitarization and Sato–Tate‑style spectral diagnostics.
     • ACE projection and preregistration gates.
     • The spec is mathematically explicit; the model is research‑grade, not production‑grade.

5.4 Quantum / physical systems

     • Multiplicity and DRMM are applied to:
     • Quantum error suppression, atomic clocks, gravitational wave sensing.
     • Coherence probes via BEC or cavity setups.
     • These are high‑aspiration targets.
     • The math is consistent.
     • Actual hardware‑level performance claims are UNPROVEN; they require serious experiments with
       domain experts.

5.5 Recursive AGI / cognitive safety

     • IMD proposes:
     • Narrative‑state machines gated by CSL.
     • Ethical potentials per prime channel.
     • DRMM‑based safe recursion (cognitive crash engineering).
     • These are clearly labeled as research directions.
     • No evidence yet that they solve AGI safety in the wild.
     • They are interesting design templates, not guarantees.




6. Governance, lawfulness, and proofs
IMD’s main differentiator vs generic AI work is the obsession with certificates and auditability.


Key patterns:


    1. Projection‑first safety (ACE).


    2. Always project proposals into a lawful set before acting.


    3. Provide KKT certificates for each projection.


    4. Spectral certificates.


    5. Use standard inequalities (Weyl, Davis–Kahan, etc.) to bound eigenvalues and eigenspaces.


    6. Encode these as explicit runtime checks.


    7. Prime‑sharded law slots.




                                                       8
   8. Each prime channel carries a specific constraint + proof obligation.


   9. If all slots verify, global lawfulness follows by construction (under stated assumptions).


  10. Zero‑knowledge‑ready design.


  11. State and updates are structured so they can be embedded into zk circuits:


          ◦ Per‑prime commitments.
          ◦ Small, uniform circuits repeated across channels.

  12. Actual zk deployments are early / UNPROVEN, but the shapes are chosen to be compatible.


  13. Preregistration and linting.


  14. Experiments and models are specified ahead of time (∞/CSL prereg schema).


  15. A linter enforces that only declared metrics and tests are used for claims.




7. Maturity, limitations, and realistic impact

7.1 Technology readiness snapshot (rough)

    • TRL 3–4 (experimental proofs‑of‑concept):
    • ACE/SCN arithmetic control.
    • PETC / PGM‑MPS signatures and ledgers.
    • ALP core algorithms.
    • Π‑kernel local update patterns.
    • TRL 2–3 (formal specs + partial prototypes):
    • Full IMD engine stack orchestration (Prism, SPASC, PIRTM runtime, auxiliary engines).
    • ∞/CSL automorphic transformers.
    • TRL 1–2 (conceptual, simulations, or manifesto‑grade):
    • DRMM as a universal operator for quantum + cognitive systems.
    • Mϕ / Λ y m as global ethical invariants.
    • AGI‑level narrative‑state + ethical Ricci‑flow stabilizers.

7.2 Main bottlenecks

    • Complexity and overhead. Prime‑indexed everything is not cheap; bookkeeping and proof
      generation add real cost.
    • Data / domain fit. Many domains may not justify the prime machinery vs simpler models.
    • Experimental validation. Most physics and AGI claims need serious external experiments, not
      internal sims.
    • Tooling. Full integration with mainstream ML / control / quantum stacks is incomplete.




                                                      9
7.3 Realistic near‑term impact

    • Provide better‑founded control and safety layers for niche spectral / arithmetic systems.
    • Act as a design library for people building lawful recursion, audits, and zk‑friendly proof logs.
    • Offer a clean test bed for combining symbolic structure (primes, signatures) with continuous
      dynamics.




                                                    10
