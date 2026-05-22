---
slug: research-proposal
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/soulaware/Research Proposal.md
  last_synced: '2026-03-20T17:17:15.671039Z'
---

**Research Proposal: A Formal Framework for Modeling Psychosocial Dynamics in Embodied Practice**
=================================================================================================

### **1.0 Introduction and Rationale**

This research addresses a fundamental challenge at the intersection of
therapeutic practice and computational science: how to bridge the gap
between the rich, qualitative insights of embodied interventions and the
rigorous, predictive power of quantitative psychosocial modeling. While
practices such as Dance Me Through the Panic (DMTP) offer powerful
methods for trauma integration, their phenomenal depth has remained
largely inaccessible to formal analysis. This project aims to close that
gap, creating a replicable, evidence-based framework that translates the
subjective experience of psychological conflict and resolution into a
computable and testable model.

The current problem is one of measurement and replicability. Somatic and
parts-based modalities like DMTP and Internal Family Systems (IFS)
provide profound phenomenological tools for navigating internal states,
yet they lack a formal, computable framework. Without such a framework,
it is difficult to precisely measure internal state changes,
systematically test the efficacy of specific interventions, or develop
evidence-based protocols that can be reliably scaled and validated. This
leaves a wealth of clinical wisdom in an anecdotal state, limiting its
integration into mainstream research and practice.

The proposed solution is a novel synthesis of three distinct domains:

-   **Dance Me Through the Panic (DMTP):** A trauma-informed,
    > tango-based embodied practice that utilizes structured interaction
    > to externalize and work with internal psychological states.

-   **Internal Family Systems (IFS):** A parts-based psychological model
    > that provides the conceptual syntax for understanding the mind as
    > a collective of sub-personalities (e.g., Exiles, Managers,
    > Firefighters) and a core Self.

-   **A Novel Mathematical Framework:** A formal model that represents
    > internal states as vectors in a Hilbert space, allowing
    > psychological dissonance to be quantified as a measurable
    > residual.

The overarching goal of this project is to formalize the concepts of
psychological dissonance and resolution into a measurable, testable
protocol that can quantify the effects of embodied interventions on an
individual\'s internal coherence.

Our investigation will be guided by three primary research aims:

-   **Aim 1:** To validate a computable Dissonance Index, D(x), as a
    > reliable metric for tracking internal conflict and coherence from
    > linguistic and physiological data.

-   **Aim 2:** To test the hypothesis that structured, dialogic
    > interventions, derived from DMTP/IFS principles, measurably reduce
    > this dissonance in a predictable manner.

-   **Aim 3:** To conduct an integrated pilot study to establish the
    > external validity of the complete framework by correlating changes
    > in model-derived metrics with established clinical indicators of
    > well-being.

To achieve these aims, we will test the following core hypotheses:

1.  Structured \"oral disagreement + repair\" prompts will produce a
    > significantly greater reduction in average Dissonance D(x)
    > compared to neutral prompts in small group interactions.

2.  Decreases in D(x) as measured from verbal transcripts will
    > negatively correlate with magnitude-squared coherence in
    > pre-registered EEG bands.

3.  In the integrated DMTP pilot, a decrease in the \"lawfulness\"
    > functional δ\_eth will demonstrate a statistically significant
    > positive correlation (ρ ≥ 0.4) with reductions in negative affect,
    > as measured by the PANAS-N scale.

This work seeks to provide a robust scientific foundation for powerful
therapeutic practices, laying the groundwork for a new generation of
evidence-based, sovereignty-respecting interventions.

### **2.0 Background and Significance**

Addressing complex psychosocial phenomena like trauma requires new
paradigms that can unify insights from traditionally siloed fields. This
research is situated at the confluence of psychotherapy, complexity
science, and the performing arts, proposing a framework that leverages
the strengths of each to create a new, formally testable model of
internal state dynamics. By operationalizing concepts from embodied
practice within a rigorous mathematical structure, this project seeks to
make the mechanisms of trauma integration observable, measurable, and
ultimately, more effective.

The theoretical foundations of this project are threefold. First is
**Dance Me Through the Panic (DMTP)**, a tango-based, trauma-informed
practice that uses the structure of partnered dance to create a safe
container for exploring and integrating internal states. DMTP provides
the embodied grammar for the protocol, translating abstract
psychological dynamics into concrete, observable interactions like
leading, following, pausing, and navigating shared space. It offers a
tangible method for externalizing internal conflict and moving through
it, quite literally, with a partner.

Second, **Internal Family Systems (IFS)** provides the psychological
syntax for the DMTP practice. IFS posits that the mind is not a monolith
but is naturally comprised of multiple \"parts\"---sub-personalities
with distinct roles, such as protective \"Managers,\" reactive
\"Firefighters,\" and vulnerable, trauma-holding \"Exiles.\" At the core
is the Self, a seat of consciousness characterized by qualities like
calm, curiosity, and compassion. This model provides a non-pathologizing
language for mapping the internal landscape, framing therapeutic work as
a process of building trust and collaboration between the Self and these
various parts.

Third, we reframe **Cognitive Dissonance as a Computable Residual**.
Drawing inspiration from signal processing, we treat dissonance not
merely as a psychological discomfort but as a measurable
\"phase-mismatch.\" An individual\'s state (represented by a vector
derived from their speech, movement, or neural activity) is projected
onto a \"coherent\" reference subspace representing a shared or lawful
reality. Dissonance is operationalized as the squared norm of the part
of the state vector that lies *outside* this subspace---the residual.
This transforms a subjective feeling of being \"mixed up\" into a
quantifiable signal that can be tracked over time.

This research aims to fill critical gaps in the current landscape.
Existing quantitative methods in psychotherapy often struggle to capture
the dynamic, relational, and embodied nature of the therapeutic process.
Conversely, embodied practices lack the formal models needed for
rigorous, falsifiable testing. Specifically, current research lacks
methods that can (1) quantify the real-time dynamics of \"parts work,\"
(2) provide a formal, mathematical link between an embodied action and a
change in psychological state, and (3) offer a testable model for
therapeutic processes that is fundamentally grounded in participant
consent and agency.

The primary innovation of this work is the creation of a direct,
mathematical bridge between a personal trauma narrative (the \"Ode\"),
an embodied resolution dynamic (the \"Dance\"), and a formal, testable
protocol. This unification has the potential for significant impact
across multiple domains:

-   **Therapeutic Practice:** Development of new, evidence-based
    > protocols for trauma integration that provide objective, real-time
    > feedback to both clinicians and clients.

-   **Creative and Performance Arts:** Creation of replicable tools for
    > managing and utilizing creative tension and interpersonal
    > dissonance in performance, rehearsal, and collaborative settings.

-   **Scientific Research:** A novel quantitative methodology for
    > psychotherapy research that respects participant sovereignty and
    > can model complex, non-linear psychological phenomena.

While the therapeutic power of DMTP and IFS is anecdotally potent, and
the mathematical tools for measuring residuals are well-defined, the
central, unproven assertion of this work is that the latter can be made
to rigorously model the former. The following framework and research
plan are designed to subject this assertion to falsifiable, multi-modal
testing.

### **3.0 Formal Mathematical Framework**

This section provides the formal, operational definitions for the core
concepts of dissonance and resolution, making them amenable to
computation and empirical testing. Grounding our qualitative hypotheses
in a precise mathematical language is essential for ensuring the
project\'s scientific rigor, replicability, and ultimate contribution to
the field.

#### **State Representation and the Dissonance Index D(x)**

We begin by defining the space in which psychological states are
represented. Let H be a real or complex Hilbert space capable of holding
representations of a psychological state, such as text embeddings from a
transcript, neural state vectors from EEG data, or features from
movement sensors.

Within this space, we define a reference subspace Π via an orthogonal
projection onto a basis of vectors {e\_p}. Following the naming
discipline from our internal specification, we will refer to these as
\"dictionary atoms\" and Π as a \"reference subspace\" in all external
reporting. The hypothesis that this basis holds a privileged, \"prime\"
role in cognition is a core, and currently unproven, claim to be tested,
not an axiom.

The dissonance of a state x ∈ H is formally defined as the squared norm
of the component of x that is orthogonal to the reference subspace Π.
This is expressed by the dissonance functional:

D(x) := \|\|(I - Π)x\|\|²

Here, (I - Π)x is the residual component of x. Intuitively, a state x
with a large D(x) corresponds to a subjective experience of being
\"mixed up,\" incoherent, or nonsensical, as it has a large component
that cannot be represented by the basis of coherent states.

#### **Resolution Dynamics**

The process of reducing dissonance is modeled as a dynamic update rule
that systematically moves a state vector closer to the coherent
subspace. For a single agent, the update equation is:

x\_{t+1} = x\_t - η\_t Ξ\_t r\_t, where r\_t = (I - Π)x\_t

The key component here is the resolution operator Ξ\_t, which is the
mathematical representation of a therapeutic or dialogic intervention.
This operator can model various actions, such as a facilitator\'s
structured prompts, attentional weighting, or a learned preconditioner
designed to accelerate dissonance reduction. The term η\_t is a
step-size parameter. Under mild conditions (specifically, when Ξ\_t is
positive-definite and its operator norm is bounded by L, with 0 \< η \<
2/L), this process is mathematically guaranteed to be stable and cause
D(x) to decrease.

To model the dialogic and consensus-seeking dynamics central to
practices like DMTP, we extend the single-agent model to a network of N
agents. This introduces two crucial terms: a graph Laplacian L\_G to
model the pull toward a \"shared collective experience,\" and a prompt
term ε\_{i,t} to represent the structured, dissonance-inducing
interventions of a facilitator.

x\_{i,t+1} = x\_{i,t} - η\_{i,t} Ξ\_{i,t} (I-Π)x\_{i,t} - Σ\_j
(L\_G)\_{ij}(x\_{i,t} - x\_{j,t}) + ε\_{i,t}

This equation models how individuals reduce their own dissonance while
also moving toward a shared understanding, with external prompts serving
to introduce or resolve collective disagreement.

#### **Complementary Metrics for Internal States**

While D(x) captures incoherence *relative to* the reference subspace,
other metrics are needed to characterize the state *within* that
subspace. We introduce two such metrics:

-   **Lawfulness Functional (δ\_eth):** This metric penalizes both
    > internal conflict and a lack of focus. It is defined as δ\_eth(x)
    > = x⊤Lx + μ\|\|x\|\|₁, where the quadratic term x⊤Lx penalizes
    > conflict between active components (e.g., antagonism between
    > different psychological \"parts\") and the L1-norm term
    > μ\|\|x\|\|₁ encourages sparsity, penalizing a state where too many
    > parts are active at once.

-   **Intra-subspace Tension (BTI):** This metric is designed to detect
    > conflict *within* the coherent subspace Π, which D(x) alone cannot
    > capture. It measures the degree to which the two most active
    > components of a state\'s projection onto Π are in tension with
    > each other. A high BTI can indicate a coherent but polarized or
    > conflicted internal state.

Together, these formalisms provide a multi-faceted toolkit for
quantifying the complex dynamics of psychological states, bridging from
theoretical concepts to the practical research plan designed to test
them.

### **4.0 Proposed Research Plan and Methodology**

Our research strategy employs a multi-study, phased approach designed to
systematically validate the core components of our framework. We will
begin by validating the primary metrics in controlled laboratory
settings before proceeding to test the fully integrated protocol in a
rich, embodied context. This staged methodology ensures that each layer
of the model is robustly tested before being combined, maximizing the
rigor and reliability of our final results.

#### **4.1 Study 1: Validation of the Dissonance Index in Dyadic Interaction**

-   **Objective:** To test the hypothesis that the Dissonance Index D(x)
    > is a valid and sensitive measure of interpersonal disagreement and
    > resolution, responding predictably to structured dialogic
    > interventions.

-   **Design:** This study will use a within-subjects A/B experimental
    > design. Small teams will participate in two 20-minute sessions
    > focused on identical topics. Session A will use neutral,
    > convergent prompts. Session B will use the same prompts but will
    > interleave targeted \"oral disagreement\" prompts followed by
    > structured \"repair\" prompts designed to facilitate resolution.
    > Verbal interactions will be transcribed for analysis.

-   **Endpoints:** The pre-registered primary endpoint is a
    > statistically significant reduction in the average Dissonance D(x)
    > (computed from text embeddings of the transcripts) in Session B
    > compared to Session A. The secondary endpoint is a faster rate of
    > decrease in inter-speaker alignment, measured as \|\|x\_i -
    > x\_j\|\|, during Session B, indicating more efficient
    > consensus-building following structured disagreement.

#### **4.2 Study 2: Neurophysiological Correlates of Dissonance Reduction**

-   **Objective:** To test the hypothesis that model-derived reductions
    > in dissonance correlate with measurable changes in brain activity
    > associated with cognitive coherence, thereby establishing a
    > neurophysiological basis for the D(x) metric.

-   **Design:** This study will involve a single-subject (n≥12) protocol
    > using electroencephalography (EEG). Each participant will undergo
    > a three-phase session: (1) baseline eyes-open rest, (2) a
    > structured dialogic task involving prompts designed to induce and
    > resolve dissonance, and (3) a final post-task rest period.

-   **Endpoints:** The primary hypothesis is that decreases in D(x),
    > computed from the participant\'s speech embeddings during the
    > task, will negatively correlate with increases in
    > magnitude-squared spectral coherence within pre-registered,
    > task-relevant frequency bands. To strengthen causal inference, the
    > prompt schedule will be randomized between \"repair\" prompts and
    > \"neutral\" prompts.

#### **4.3 Study 3: Integrated Pilot of the DMTP × Multiplicity Protocol**

-   **Objective:** To assess the feasibility, safety, and preliminary
    > efficacy of the fully integrated protocol, combining the DMTP
    > embodied practice, the IFS psychological model, and the complete
    > mathematical framework.

-   **Design:** Approximately 12 participants will engage in the
    > protocol over two sessions (Day 0 and Day 7). The protocol
    > involves a sequence of baseline assessment, IFS-based priming,
    > structured tango-based dance blocks, and post-session reframing
    > and assessment.

-   **Data Collection:** A rich, multi-modal dataset will be collected,
    > including: Inertial Measurement Unit (IMU) and video data to
    > capture movement dynamics; pre- and post-session self-report
    > surveys, including the Positive and Negative Affect Schedule
    > (PANAS); and real-time micro-annotations of active IFS parts by
    > trained observers.

-   **Pre-Registered Kill-Switch Criteria:** To ensure scientific rigor
    > and avoid confirmation bias, the mathematical layer of this study
    > is subject to three pre-defined, non-negotiable pass/fail gates.

    1.  **Basis Advantage:** The prime-indexed basis must demonstrate a
        > superior ability to decode IFS parts from the data, showing a
        > change in Area Under the Curve (ΔAUC) of at least 0.05 over
        > the best-performing baseline basis (e.g., Random, Fourier,
        > Learned).

    2.  **Parts Decoding:** A classifier trained on the data must be
        > able to identify active IFS parts with a weighted F1 score of
        > at least 0.55 on held-out data.

    3.  **External Validity:** The change in the lawfulness functional,
        > Δδ\_eth, from pre- to post-session must show a statistically
        > significant positive correlation (ρ ≥ 0.4) with the reduction
        > in negative affect as measured by the PANAS-N scale.

-   Failure on two or more of these gates will result in sunsetting the
    > mathematical layer, preserving only the DMTP workshop protocol for
    > future development.

#### **Data Analysis Plan**

The primary analyses for Studies 1 and 2 will consist of pre-registered
statistical tests, including t-tests for the A/B comparison and
correlation analyses for the EEG data, to assess the pre-specified
hypotheses. For Study 3, the core analysis will be a rigorous ablation
study comparing the performance of the proposed \"prime\" basis against
a suite of other orthonormal bases (Random, Fourier, Wavelet, and a
Learned dictionary basis) on the parts-decoding task. To ensure full
transparency and reproducibility, all analysis code, particularly the
Python notebook for computing the metrics (dissonance\_pipeline.ipynb),
and all data schemas (run\_log\_schema.json) will be version-controlled
and made publicly available upon publication.

This comprehensive plan provides a clear and rigorous pathway to
validating this novel, integrated approach.

### **5.0 Ethical Framework and Participant Sovereignty**

Research that intentionally induces and measures psychological
dissonance operates under a unique ethical burden. Standard consent
models, designed for static risk assessment, are inadequate for dynamic
processes where a participant\'s own internal state is the subject of
inquiry. This project therefore treats its ethical framework not as a
procedural safeguard, but as a core component of the scientific
methodology itself---a \"sovereignty-first\" architecture designed to be
as rigorous and testable as the mathematical models it supports.

#### **The Sovereignty Spine**

Our ethical framework is built on a set of core principles designed to
protect and enhance participant authority over their own experience and
data at all times.

-   **Participant-Authored, Revocable Everything:** All patterns,
    > reference frames (\"primes\"), and mappings used by the system are
    > defined in collaboration with the participant. The participant
    > retains the right to alter, pause, or permanently delete any of
    > these definitions at any time without penalty.

-   **Perspectives, Not Truths:** All outputs from the system, including
    > metrics like the Dissonance Index, are explicitly framed as one
    > possible perspective on the participant\'s state, never as an
    > objective or diagnostic truth.

-   **Drop to Baseline Anytime:** Participants have continuous access to
    > a \"No More Magic\" mode. Activating this immediately halts all
    > complex interventions and data processing, returning the session
    > to simple, grounding exercises and basic human connection.

-   **No Hidden Cross-Layer Inference:** Any analytical integration
    > between different data streams (e.g., linking movement patterns to
    > linguistic content) is made transparent and requires separate,
    > explicit consent.

#### **Novel Consent Protocols**

We conceptualize **\"Consent as Choreography,\"** moving beyond a
one-time signature to a dynamic, ongoing process. This is
operationalized through stateful consent maps where participants can use
intensity dials to set their boundaries for different types of
engagement (e.g., cognitive play vs. emotional exploration). These maps
are revisited at midpoint recalibration checks, and consent can be
modified in real-time through non-verbal signals, including physical
gestures and pre-agreed chat commands.

#### **Operational Safeguards and Risk Mitigation**

We have developed a formal risk register that pairs potential harms with
specific, measurable controls. Key technical and human-in-the-loop
safeguards are integrated directly into the experimental procedure.

  Risk ID                      Risk Description                                                                                                                                           Control Measure
  ---------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **R1: Arbitrary Π**          The choice of reference subspace Π is arbitrary, potentially imposing a biased or meaningless frame on participant data.                                   The basis matrix Π is frozen pre-study, derived from a held-out corpus. Its cryptographic hash (SHA-256) is published with the pre-registration. Subspace drift is monitored and must not exceed 1 − s\_avg ≤ 0.01 per session.
  **Descent Violation**        The mathematical guarantee of dissonance reduction (D(x)) fails, potentially leading to unintended amplification of distress.                              The resolution operator Ξ is constrained to maintain descent. The descent-violation rate is automatically monitored and must not exceed v ≤ 0.005 per session.
  **R3: Goodhart on D**        Optimizing for a reduction in the Dissonance Index D(x) may not correspond to a genuine improvement in well-being and could become a meaningless target.   A multi-objective gate is pre-registered. Success is only claimed if a reduction in D(x) is accompanied by a non-negative change in an external outcome measure (e.g., PANAS score, task performance).
  **R4: Coercive Consensus**   Group dynamics could implicitly pressure participants into aligning with a group norm, violating their agency.                                             Participants can opt-out of the consensus-coupling term (κ=0) at any time without penalty, allowing them to remain in the session without being algorithmically nudged toward the group average.

In addition to these technical controls, a human **Guardian** will be
present in all sessions. The Guardian\'s sole responsibility is to
monitor the psychological safety of participants, and they are empowered
with unilateral authority to pause the experiment or trigger a \"No More
Magic\" state if they observe signs of distress. This human oversight
serves as the ultimate circuit breaker, ensuring safety protocols are
not solely reliant on automated systems.

### **6.0 Project Timeline and Deliverables**

The project will be executed according to a pragmatic and phased
timeline, structured to validate foundational components in early stages
before proceeding to more complex integrations. This approach minimizes
risk and ensures that each phase of the research is built on a solid
empirical foundation.

#### **Project Timeline**

  Phase             Key Activities & Milestones
  ----------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Weeks 1-2**     **Project Setup & Pre-registration:** Finalize all analysis plans for Studies 1 and 2. Freeze the Π basis for Study 1 and publish its cryptographic hash. Complete and submit the pre-registration document.
  **Weeks 3-4**     **Study 1 Execution:** Conduct the Language A/B study on dyadic interaction. Collect and process all transcript data.
  **Weeks 5-8**     **Study 2 Execution & Analysis:** Pilot and run the EEG linkage study. Analyze data from both Study 1 and Study 2. Develop the predictive intervention system based on preliminary findings.
  **Weeks 9-12**    **Study 3 Execution & Final Analysis:** Conduct the integrated DMTP pilot study. Run the pre-registered ablation analysis and test the kill-switch criteria. Synthesize findings from all three studies.
  **Weeks 13-16**   **Dissemination:** Prepare the preprint manuscript detailing the framework and results. Assemble the open-source digital binder. Write and submit the final project report.

#### **Project Deliverables**

Upon completion, this project will produce the following concrete
deliverables:

-   **A Pre-registration Document:** A comprehensive document, publicly
    > filed prior to data collection, detailing all hypotheses, primary
    > and secondary endpoints, statistical analysis plans, and
    > kill-switch criteria for the pilot study.

-   **An Open-Source Digital Binder:** A publicly accessible repository
    > containing all tools necessary for replication and extension of
    > this work. This will include:

    -   The runnable Python notebook for computing dissonance metrics
        > (dissonance\_pipeline.ipynb).

    -   The data schema for reproducible run logs
        > (run\_log\_schema.json).

    -   The one-page protocol for the integrated DMTP pilot.

    -   The consent templates and sovereignty framework documents.

-   **A Preprint Manuscript:** A scientific paper detailing the
    > mathematical framework, the design and results of the three
    > studies, and a full discussion of the findings. This will include
    > a commitment to publishing null findings to ensure a balanced
    > contribution to the scientific record.

-   **A Final Report:** A summary report detailing the outcomes of the
    > three studies, evaluating the success of the project against its
    > stated aims, and making concrete recommendations for future
    > research and development in this area.

This structured plan ensures that the project will not only generate
valuable scientific insights but also produce tangible, high-quality
assets for the broader research community.

### **7.0 Conclusion**

This project represents a unique, interdisciplinary effort to build a
robust, quantitative bridge between the profound insights of embodied
therapeutic practices and the rigorous methods of computational science.
By formalizing psychological dissonance into a measurable, computable
construct, this research offers a novel path to understanding the deep
mechanics of trauma integration, conflict resolution, and the
cultivation of internal coherence. We are not merely proposing a new
metric, but an entire framework for modeling and influencing the
dynamics of embodied cognition.

A validated framework of this nature has the potential for significant,
multi-domain impact. For therapeutic practice, it promises to introduce
objective feedback loops that can enhance the efficacy and replicability
of powerful somatic and parts-based interventions. For scientific
research, it offers a new paradigm for modeling psychological processes
that honors their complexity, non-linearity, and inherent subjectivity,
while maintaining the highest standards of empirical rigor.

With its rigorous mathematical foundation, a feasible and phased
research plan, and a sovereignty-first ethical framework designed for
testability, this project is poised to make a timely and vital
contribution. It offers not only a new model for embodied cognition, but
a new blueprint for how to conduct ethical, participant-centered
research on the deepest aspects of human experience.
