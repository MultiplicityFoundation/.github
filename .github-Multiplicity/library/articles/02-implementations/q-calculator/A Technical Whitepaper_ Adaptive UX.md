---
slug: a-technical-whitepaper-adaptive-ux
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/A Technical Whitepaper_ Adaptive UX.md
  last_synced: '2026-03-20T17:17:15.146203Z'
---

A Technical Whitepaper on an Adaptive
User Experience Engine and an Empirical
Evaluation of Prime Number-Based
Interaction Encoding
1.0 Introduction
Creating user experiences that are personalized and responsive in real-time is a significant
challenge in modern digital product development. As user interactions generate a continuous
stream of data, systems must be capable of interpreting these signals to make intelligent
decisions that enhance engagement and usability. This whitepaper details the architecture of a
novel Adaptive UX Engine, a system designed to consume user events, maintain a dynamic
user state, and select appropriate UI variants in real time.

The purpose of this document is twofold. First, it specifies the complete technical architecture of
the online adaptation system, from event collection to decision logging, providing a blueprint for
implementation. Second, it defines a formal A/B experiment designed to rigorously evaluate a
key component: the interaction encoding strategy. The experiment will compare a standard
integer-based encoding method against a prime number-based alternative to empirically
measure their effects on user experience.

This investigation is guided by the following primary research question:

Does prime number-based encoding of user interactions yield a measurable performance
improvement in key UX metrics compared to a standard sequential integer encoding scheme?

To maintain focus and ensure a feasible initial implementation, the scope of this system is
explicitly defined. This version will not use real quantum hardware. The system will not
implement experimental tensor networks; its functionality will be achieved using a standard
machine learning architecture based on embeddings. Furthermore, this document makes no a
priori claims that prime encoding improves performance; it is presented as a testable
hypothesis.

This paper will now proceed with a detailed examination of the system's architecture and its
core components.


2.0 System Architecture and Components
A modular, component-based architecture is of strategic importance for building a scalable and
maintainable real-time machine learning system. By decoupling responsibilities, each
component can be developed, tested, and upgraded independently, which is critical for both
operational stability and iterative improvement. The Adaptive UX Engine is designed around this
principle, comprising seven core components that work in concert to deliver real-time
adaptations.

The seven core components of the Adaptive UX Engine are:

   ●​ Event Collector: This component serves as the system's entry point, accepting and
      normalizing interaction events (e.g., clicks, page views) from frontend clients. It ensures
      all incoming data is consistently timestamped and structured before being passed to
      downstream services.
   ●​ Interaction Encoder: Positioned after the collector, the encoder's function is to map
      a normalized interaction event to a unique integer ID. This module is designed to be
      pluggable, allowing different encoding strategies, such as prime or standard integer
      assignment, to be used interchangeably based on experimental requirements.
   ●​ User State Store: This stateful component maintains a feature vector and a derived
      scalar score for each user. It is responsible for retrieving a user's current state, updating
      it with new interaction data, and persisting the result for future decisions.
   ●​ Adaptation Engine: As the system's central logic unit, the Adaptation Engine
      consumes a user's state to compute an "adaptation score." Based on this score and a
      set of configurable rules, it selects a specific UI layout or content variant to be presented
      to the user.
   ●​ Policy Store: This component is a repository for the model parameters that govern
      the Adaptation Engine's behavior. It holds versioned data, including embedding weights
      and decision thresholds, allowing for safe and consistent model updates.
   ●​ Logger: To enable offline analysis and model training, the Logger captures all inputs
      and outputs of the adaptation process. It writes detailed, immutable records of events,
      user states, and adaptation decisions to a persistent storage layer.
   ●​ Offline Trainer: This component operates on the data collected by the Logger. It is
      responsible for training and updating model parameters by learning from historical user
      interactions and their outcomes, producing new policies for deployment to the Policy
      Store.

The system's operational flow is a stateful loop. When an interaction event arrives at the Event
Collector, it is first encoded by the Interaction Encoder. The system then retrieves the
user's current state from the User State Store. It applies a temporal decay factor to the
user's feature vector before adding the embedding of the new interaction. The updated state is
persisted, and if the event type is configured to trigger an adaptation, the Adaptation Engine
is invoked to compute a new layout decision using parameters from the Policy Store. This
entire transaction—including the user state before and after the update, and the final
decision—is recorded by the Logger.
The following section details the specific data structures that flow between these components.


3.0 Core Data Models
Well-defined data structures are fundamental to the system's reliability and the integrity of the
offline training process. They create a clear contract between components, prevent data
corruption, and ensure that the information logged for analysis is consistent and complete. The
system relies on six primary data structures.

InteractionEvent

This structure represents a normalized user interaction event received from the frontend client.



 Field            Description



 user_id          A unique identifier for the user.



 session_id       An identifier for the user's current session.



 event_type       The type of interaction (e.g., "click", "page_view", "form_submit").



 props            A map of key-value pairs containing event metadata (e.g., element ID,
                  page).



 timestamp_       The millisecond timestamp when the event occurred.
 ms



EncodedEvent

This structure represents an InteractionEvent after it has been processed by the
Interaction Encoder.
 Field                Description



 user_id              A unique identifier for the user.



 event_id             The integer ID (prime or standard) assigned to the event.



 weight               A numerical weight associated with the event (e.g., 1.0).



 timestamp_ms         The millisecond timestamp when the event occurred.



UserState

This structure captures the cumulative state of a user's interactions over time.



 Field                Description



 user_id              A unique identifier for the user.



 features             A learned vector representing the user's interaction history.



 S                    A scalar score derived from the feature vector, summarizing the user's
                      state.



 last_updated_        The timestamp of the last update to this state.
 ms



AdaptationDecision
This structure records the output of the Adaptation Engine for a given user at a specific
point in time.



 Field                  Description



 user_id                A unique identifier for the user.



 layout_id              The identifier of the UI layout selected (e.g., "control", "var_A").



 adaptation_scor        The computed influence score I(t) that led to this decision.
 e



 policy_version         The version of the model parameters used to make the decision.



 timestamp_ms           The millisecond timestamp of the decision.



ModelParams

This structure encapsulates all the learned parameters and configuration required by the
Adaptation Engine.



 Field                 Description



 embedding_matr        A matrix holding the vector representations for each unique event ID.
 ix



 w                     A weight vector used to project the user's feature vector into a scalar S.
 gamma, delta,         Parameters governing the non-linear influence function.
 beta



 tau_1, tau_2          Configurable thresholds for layout selection.



 learning_rate         The learning rate used during model training.



TrainingSample

This structure aggregates the necessary information from logs to form a single example for the
Offline Trainer.



 Field               Description



 features            A snapshot of the user's feature vector at the time of a decision.



 layout_id           The layout that was presented to the user.



 reward              The observed outcome (e.g., 1 if a goal was met, 0 otherwise).



 is_prime_arm        A boolean flag indicating if the user was in the prime encoding group.



 policy_versio       The version of the policy under which the decision was made.
 n



These data models provide the foundation for the system's dynamic logic, which transforms raw
events into actionable decisions.
4.0 System Logic and Computational Flow
This section details the core algorithms of the system, from how user interactions are encoded
into a numerical format to how an adaptive decision is ultimately computed. These steps define
the real-time processing pipeline that translates user behavior into a responsive user
experience.

4.1 Interaction Encoding Module

The system's pluggable encoder design is a critical architectural choice that enables the
empirical testing of different encoding strategies without altering other system components. An
InteractionEvent is first converted into a stable "event key" before being encoded. This key
is created by concatenating the event type with stable page and element identifiers, ensuring
that the same logical interaction always produces the same key.

The key creation logic is as follows: key = event_type + "|" + page + "|" +
element_id

Two encoder implementations are specified for the A/B experiment: PrimeEncoder and
StandardEncoder. Their distinct logics are compared below.



 Encoder Type        Encoding Logic



 PrimeEncoder        Maintains a mapping of event keys to unique prime numbers. When a
                     new, unseen key is encountered, it is assigned the next available prime
                     from a pre-generated pool.



 StandardEncod       Maintains a mapping of event keys to standard sequential integers.
 er                  When a new key is encountered, it is assigned the next consecutive
                     integer (e.g., 1, 2, 3, ...).



The selection of which encoder to use for a given user is determined by their assignment in the
A/B experiment.

4.2 User State Update Dynamics
A user's state vector is updated in a two-step process upon the arrival of a new
EncodedEvent. This ensures the state reflects both the passage of time and the influence of
recent interactions.

First, to account for the decaying relevance of older interactions, a temporal decay factor is
applied to the user's existing feature vector. This factor is calculated using the time delta (dt)
between the current event and the last update: decay_factor = exp(-lambda * dt)
Here, lambda is a configurable hyperparameter that controls the rate of decay.

Second, the embedding vector v corresponding to the new interaction's event_id is retrieved
from the model's embedding_matrix. This vector is then added to the decayed feature vector
to produce the new state: state.features = decay_factor * state.features + v

Finally, the scalar state score S(t), which serves as a one-dimensional summary of the user's
state, is computed by taking the dot product of the model's weight vector w and the updated
feature vector: state.S = dot(model.w, state.features)

4.3 Adaptation Decision Logic

The scalar state S(t) is translated into a final adaptation_score using a non-linear
influence function. This function is designed to amplify the system's response to changes in user
state, creating more distinct adaptation levels.

The influence function I(t) is defined as: I(t) = γS(t)² + δe^(βS(t))

This function's design is intentional: the quadratic term (γS(t)²) provides a stable, predictable
growth response to changes in the user's state, while the exponential term (δe^(βS(t)))
allows for a much more rapid, "explosive" adaptation when S(t) becomes strongly positive.
This duality enables the model to learn both subtle and aggressive response patterns. The
parameters γ (gamma), δ (delta), and β (beta) are learnable and control the shape of this
response.

The final UI layout is selected using threshold-based logic applied to the adaptation_score
I(t). The system compares I(t) against two pre-defined thresholds, tau_1 and tau_2, to
choose one of three possible layouts:

   ●​ If I(t) < tau_1, select control_layout.
   ●​ If tau_1 <= I(t) < tau_2, select layout_soft_adapt.
   ●​ If I(t) >= tau_2, select layout_aggressive_adapt.

This online decision-making logic is directly dependent on the model parameters learned
through the offline training process described next.
5.0 Offline Training and Model Optimization
The offline training loop is a critical feedback mechanism that enables the system to learn from
historical data and continuously improve the parameters governing its real-time adaptation logic.
By analyzing past interactions and their subsequent outcomes, the trainer optimizes the model
to make more effective decisions.

The training process is guided by a well-defined reward signal. For this system, a binary reward
is used: a value of 1 is assigned if a user completes a desired action (e.g., a purchase or
signup) within a specific time window during a session, and 0 otherwise. This provides a clear,
measurable outcome for the model to optimize against.

The training objective is to minimize binary cross-entropy loss. To achieve this, the model uses a
logistic link function, p = sigmoid(I(t)), to connect the predicted influence score I(t) to
the probability of observing a reward. This transforms the regression problem of predicting I(t)
into a classification problem of predicting the likelihood of a positive outcome.

The offline training loop follows these steps:

   1.​ Logged AdaptationDecision data is joined with subsequent reward events based on
       user_id and timestamp to associate outcomes with the state that produced them.
   2.​ TrainingSample instances are constructed from this joined dataset, each containing
       the feature vector snapshot at decision time and the corresponding reward.
   3.​ The trainer iterates through the TrainingSample data in batches, computing the loss
       and gradients for each batch via backpropagation through the influence function.
   4.​ Gradient updates are applied to all of the model's learnable parameters: the
       embedding_matrix, the projection vector w, and the influence function parameters
       gamma, delta, and beta.
   5.​ After training is complete, a new, versioned set of ModelParams is produced and made
       available for deployment to the online system.

This systematic process of learning from past data transitions us from the system's technical
design to the formal methodology for testing its core hypothesis.


6.0 A/B Experiment Design: Prime vs. Standard Encoding
Rigorous, empirical validation is essential for assessing the impact of any novel system
component. Theoretical advantages must be confirmed with real-world data to justify their
inclusion in a production system. This section outlines the formal A/B experiment designed to
test the hypothesis that prime number-based interaction encoding provides a measurable
benefit over a standard integer-based approach.
6.1 Hypotheses and Experimental Arms

The experiment is structured around a clear null hypothesis and a two-sided alternative,
ensuring a decisive outcome.

   ●​ Null Hypothesis (H₀): Prime encoding and standard encoding produce no statistically
      significant difference in key user experience metrics.
   ●​ Alternative Hypothesis (H₁): Prime encoding produces a statistically significant
      difference (either positive or negative) in key user experience metrics compared to
      standard encoding.

To test these hypotheses, users will be randomly assigned to one of two experimental arms,
with the encoding method being the sole differentiating factor.



 Arm              Encoder                 Description
                  Implementation



 Arm A            StandardEncoder         This is the control group. User interactions are
 (Standard)                               mapped to sequential, non-prime integer IDs.



 Arm B            PrimeEncoder            This is the treatment group. User interactions are
 (Prime)                                  mapped to unique prime numbers from a
                                          pre-generated pool.



All other system parameters—including the model architecture, UI variants, and decision
thresholds—will remain identical across both arms.

6.2 Randomization and Population

To ensure unbiased assignment, the randomization unit will be the user_id. Each user will
be assigned to an arm upon their first interaction using a stable hash function. This provides a
"sticky" assignment, guaranteeing that a user remains in the same experimental arm for the
duration of the test.

The population for analysis will be filtered to include only eligible users. The primary eligibility
criterion is a minimum level of engagement, defined as having at least N=3 interactions within
a session. This helps to reduce noise from users who do not meaningfully experience the
system's adaptive capabilities.
6.3 Metrics

A combination of primary, secondary, and guardrail metrics will be used to provide a
comprehensive assessment of the experiment's impact.

   ●​ Primary Metric: A single, pre-selected primary metric will be used to determine the
      experiment's outcome. An example is Task completion rate, defined as the percentage
      of users who complete a key action (e.g., signup) within 24 hours of their first session in
      the experiment.
   ●​ Secondary Metrics: These metrics will provide additional context and insight into
      changes in user behavior. They include:
          ○​ Engagement (average interactions per session)
          ○​ Time-to-task-completion
          ○​ Layout-switch rate (how frequently the layout changes for a user)
   ●​ Guardrail Metrics: These metrics are monitored to ensure the experiment does not
      cause harm to the user experience or system performance. They include:
          ○​ Error rate (client-side or server-side)
          ○​ Bounce rate
          ○​ API latency

6.4 Statistical Plan and Analysis

To ensure the experiment can detect a meaningful effect, the required sample size will be
calculated in advance using the standard formula for comparing two proportions:

n ≈ 2 * (z_{1-α/2} + z_{1-β})² * p̄(1 - p̄) / Δ²

Where:

   ●​ p̄ is the average proportion of the primary metric across both arms, calculated as p̄ =
         (p_A + p_B)/2.
   ●​ Δ is the minimum detectable effect size (the absolute difference in proportions).
   ●​ α (alpha) is the significance level, typically set to 0.05.
   ●​ β (beta) is the probability of a Type II error, with 1-β representing statistical power
      (typically 80%).

For the analysis, metrics will be aggregated at the user level to avoid disproportionate influence
from highly active users. The primary metric will be compared between the two arms using a
two-proportion z-test or a logistic regression model with the experimental arm as a
covariate.

The final decision rule is straightforward: if the resulting p-value is less than 0.05 and the
observed effect size is deemed practically meaningful, the null hypothesis will be rejected in
favor of the winning variant. If no statistically significant difference is found, the hypothesis that
prime encoding improves performance will be considered falsified.

The following section addresses the operational measures required to run this experiment safely
and effectively.


7.0 Operational Considerations
Deploying an adaptive system and running a formal experiment in a production environment
requires careful engineering and procedural discipline. This section outlines the practical
requirements for API integration, data logging, and experimental safeguards to ensure both
system stability and the integrity of the results.

7.1 API Integration

The frontend client has two primary responsibilities. First, it must emit InteractionEvent
payloads for relevant user actions. Second, on key page loads or navigations, it must call the
Adaptation API to retrieve a layout_id and then render the corresponding UI variant.

The system exposes a single RESTful endpoint for this purpose: POST /adapt.

Request Body:

{
    "user_id": "...",
    "session_id": "...",
    "context": { "page": "/home", "device": "mobile" },
    "timestamp_ms": 1734300000000
}


Response Body:

{
    "layout_id": "layout_soft_adapt",
    "policy_version": 7,
    "adaptation_score": 1.23,
    "timestamp_ms": 1734300001000,
    "arm": "standard"
}


Upon receiving a request, the backend determines the user's experimental arm, updates their
state, computes the adaptation decision, and returns the selected layout.
7.2 Logging and Data Integrity

Accurate and comprehensive logging is the foundation of all offline analysis and model training.
For each adaptation decision, the following data points must be logged:

   ●​ user_id
   ●​ arm (e.g., "standard" or "prime")
   ●​ encoded_event_ids (or a summary representation to reconstruct interaction history)
   ●​ features (or a compressed representation)
   ●​ S (scalar state score)
   ●​ I (influence score)
   ●​ layout_id
   ●​ policy_version

All logs must be immutable and accurately timestamped. This ensures that offline analyses
can reconstruct the exact state of the system at the time of each decision, which is critical for
attributing outcomes correctly.

7.3 Experimental Safeguards

To protect the user experience and ensure the validity of the experiment, several operational
safeguards must be implemented.

   ●​ Pre-registration: Before launching the experiment, the hypotheses, metrics, and
      stopping criteria must be formally documented and shared. This prevents "p-hacking"
      and ensures that the analysis plan is fixed ahead of time.
   ●​ Kill Switch: The system must include an automated mechanism to halt the experiment
      and revert all users to the control experience if any guardrail metrics breach pre-defined
      safety thresholds (e.g., a significant increase in error rates).
   ●​ Version Pinning: The model parameters (ModelParams) must not be changed for
      either arm during the experiment. Deploying a new model version mid-flight would
      introduce a confounding variable, contaminating the results and making it impossible to
      isolate the effect of the encoding strategy.

These operational controls provide the necessary framework for deploying the system
responsibly.


8.0 Conclusion
This whitepaper has detailed the architecture of a modular Adaptive UX Engine designed for
real-time UI personalization, alongside a rigorous A/B testing framework for evaluating its core
components. The system's design emphasizes scalability, maintainability, and a clear separation
of concerns, from online decision-making to offline model optimization.
Crucially, this document establishes a commitment to empirical evidence over theoretical claims.
The A/B experiment is designed to provide a "brutal assessment" of the prime number encoding
hypothesis. If the experiment concludes that prime encoding offers no measurable benefit in the
context of this system, that hypothesis will be considered falsified. The flexible architecture of
the engine will be retained, but without any unsubstantiated performance claims tied to the
encoding method.

This integrated approach—building a flexible system while simultaneously designing a robust
methodology for its validation—represents a sound and responsible engineering practice. It
provides a clear path for deploying impactful machine learning-driven products while grounding
innovation in measurable, data-driven outcomes.
