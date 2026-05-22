---
slug: atomic-language-processing-revised
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/Atomic Language Processing - Revised.md
  last_synced: '2026-03-20T17:17:15.270370Z'
---

Atomic Language Processing (ALP) — Revised
Specification
Version: 2.0 (Revised)
Status: Draft / Implementation-Oriented
Scope: Symbolic–numeric framework for prime-based representation of language and semantics, with an
explicit path to UX / interaction modeling.




1. Motivation and Design Goals
Atomic Language Processing (ALP) treats language and related signals (UX events, interaction traces) as
compositions of discrete, prime-indexed atoms. It is not a replacement for neural models, but a
structural layer that:


    1. Provides stable, discrete codes for units (characters, morphemes, words, semantic concepts).
    2. Supports exact factorization into atomic components (via prime-factor structure or exponent
       vectors).
    3. Enforces compositional consistency via simple algebraic laws (addition of exponents; monoid
       structure).
    4. Offers interpretable internal state: factorization and exponent vectors are directly human-
       readable.

The original ALP formulation introduced:


     • Order primes for unit identity and ranking.
     • PETC (Prime-Encoded Tensor Calculus) vectors for feature structure.
     • ACE (Arithmetic Control Engine) for stability (bounded churn and spectral control).

This revised version keeps those ideas but makes four corrections:


    1. Prime products are diagnostic only. The primary representation is an exponent / multiplicity
       vector, not giant integers.
    2. Time semantics are explicit. All decay is defined per second (or per chosen unit) and documented.
    3. Mapping layers are clearly separated. Grapheme → morpheme → lexical → semantic, each with its
       own prime basis.
    4. Integration with machine learning is explicit. ALP states are treated as feature vectors into
       standard models.




                                                     1
2. Core Objects and Notation
We fix two disjoint prime sets:


      • Pord = {p1 , p2 , … }: order primes, used to identify and rank atomic units.
      • Ppetc = {q1 , q2 , … , qd }: feature primes, used to define PETC vectors.

In practice, we never rely on the numeric magnitude of primes; we treat them as stable IDs with algebraic
structure available for diagnostics and interpretability.


2.1 PETC Vectors (Feature Space)

A PETC vector is an integer or real-valued exponent vector:


                                         σ ∈ Rd≥0 ,       σ = (e1 , e2 , … , ed )

where each coordinate ei is the multiplicity (or strength) of feature prime qi .


Composition of two signatures σx , σy is additive:


                                                 σx⊗y = σx + σy .

This is the foundational law: ALP treats composition as additive in exponent space, not multiplicative in
integer space.


2.2 Order Primes (Identity / Rank)

Each atomic unit (e.g., a grapheme, morpheme, or lexical item) is assigned:


      • A unique order prime pu ∈ Pord .
      • An associated PETC vector σu ∈ Rd≥0 .

The “integer materialization” of a unit is:

                                                      d
                                   CZ (u) = pu ⋅ ∏ qiei ,        σu = (e1 , … , ed ).
                                                  i=1

       Important: In this revised spec, CZ exists only for logging, compression, and symbolic
       analysis. All computation uses pu and σu separately.


2.3 ALP Code Tuple

Every unit u is represented as:


                                               ALP(u) = (pu , σu )

      • pu : identity and rank (from Pord ).




                                                             2
     • σu : PETC signature over Ppetc .

Composite units (e.g., words from morphemes, sentences from words) are represented by:


                                          ALP(x ⊗ y) = (px⊗y , σx + σy )

where px⊗y is assigned according to a ranking policy (Section 4), and the PETC part is purely additive.




3. Layered Architecture
We define four main layers, each with its own ALP registry and mapping functions.


    1. L1 – Graphemic Layer: characters / graphemes.
    2. L1.5 – Grapheme-in-Context Layer: dynamic rank adjustments for graphemes in context.
    3. L2 – Morphemic / Subword Layer: morphemes, BPE units, subwords.
    4. L3 – Lexical / Semantic Layer: tokens, phrases, and semantic concepts.

Each layer has its own:


     • Vocabulary VL .
     • Order prime assignment p : VL → Pord .
     • PETC mapping ΦL : VL → Rd≥0 .

3.1 L1: Graphemes

     • Units: Unicode codepoints or normalized graphemes.
     • Order primes: assigned once, typically in frequency order.
     • PETC features: simple structural properties (e.g., letter vs digit, punctuation type, script ID).

Example PETC dimensions at L1:


     • is_alpha , is_digit , is_punct , is_whitespace
     • script:latin , script:cyrillic , ...

3.2 L1.5: Grapheme-in-Context

Purpose:


     • Adapt order primes for graphemes in contextual roles (e.g., inside URLs, numbers, entities).
     • Maintain bounded churn: only a limited number of order swaps per update.

Mechanism (high-level):


    1. Maintain an association matrix A between graphemes and contextual roles.
    2. Update A with exponential moving averages (EMA).
    3. Propose re-ranking of graphemes within each role based on updated scores.
    4. Apply ACE constraints:




                                                        3
     5. Max K rank swaps per update step.
     6. Spectral-norm bound on ΔA to ensure stability.

L1.5 affects only the order primes (ranking) and not the PETC vector; the feature semantics remain stable.


3.3 L2: Morphemes / Subwords

At L2 we map sequences of L1 units to morphemes or subword units.


      • Vocabulary VL2 can be derived from:
      • A fixed BPE / unigram LM segmentation.
      • A morpheme lexicon.
      • Each L2 unit inherits or composes PETC vectors from its L1 components:

                                 σL2 (m) =          ∑           σL1 (g) + Δm ,
                                               g∈graphemes(m)

where Δm encodes morpheme-specific features (e.g. part-of-speech hints, affix type).


3.4 L3: Lexical / Semantic Layer

At L3 we introduce semantic primes and treat ALP as a general semantic factorization framework.


      • Units: tokens, multi-word expressions, semantic concepts.
      • Feature dimensions in PETC space represent semantic attributes, e.g.:
      • sentiment, intent, topic, stance, politeness, subjectivity, etc.
      • For UX/interaction applications, these can include:
      • intent:purchase , emotion:frustration , topic:tech , etc. (as in the semantic-vocabulary
        registry you defined).

For a lexical unit w :


                                              σL3 (w) = fsem (w)

where fsem is a mapping from embeddings, rules, or classifiers into the PETC feature space.


The key constraint: once a semantic dimension (feature prime) is defined, it remains stable, even if its
associated weights in downstream models change.




4. ACE – Arithmetic Control Engine (Stability Layer)
ACE is an optional but important component that regulates updates to:


      • Order primes (rankings) at L1 / L1.5 / L2 / L3.
      • Association matrices (e.g. grapheme–role, morpheme–context).




                                                       4
4.1 Association Updates

Let At be an association matrix at time t (e.g. units × context roles). We update:


                                          At+1 = (1 − α)At + αA^t
      ^t is the association estimated from the most recent batch and α is a learning rate.
where A


4.2 Rank Proposal and Churn Constraints

From At+1 we derive a new rank order for units by sorting association scores per role. ACE then:


    1. Defines the current ranking as a permutation πt .
    2. Defines the proposed ranking as πt∗ .
    3. Computes the difference permutation δ = πt−1 ∘ πt∗ .
    4. Restricts to at most K swaps per update (bounded churn).

This prevents wild oscillations in which units repeatedly swap places in the ranking.


4.3 Spectral Drift Constraint

ACE can also bound the spectral norm of updates:


                                               ∥At+1 − At ∥2 ≤ ε.

Approximated with:


     • Power iteration on At+1 − At .
                 ^t or reducing α if the bound is violated.
     • Rescaling A

In this revision, ACE is optional. For many practical deployments (including UX semantics), one can start
with static rankings and fixed vocabularies, and introduce ACE only when dynamic ranking is required.




5. ALP for Semantic Primes and UX
This section ties ALP directly to the semantic-prime UX engine you designed.


5.1 Semantic Vocabulary as PETC Registry

A semantic vocabulary file (e.g. semantic_vocab.json ) defines:


     • concept_id (string): semantic unit ID, e.g. "intent:purchase" .
     • prime (int): unique prime in Ppetc used for logging and symbolic factorization.
     • index (int): index in the PETC vector.




                                                       5
In ALP terms:


      • Each concept is a feature prime dimension qi with index i.
      • A user’s semantic state is a PETC vector σ ∈ Rd≥0 over these concepts.

5.2 Semantic Mapping Model

A SemanticMappingModel is an ALP-compliant function:


                                            M : Event → {(cj , sj )}\n

where:


      • cj is a concept ID from the vocabulary.
      • sj ∈ [0, 1] is a confidence or intensity score.

The PETC signature for an event is then:


                                                   σevent [i] = ∑ sj .
                                                               j:cj ↦i

Composition over events is additive, giving a user-level state vector:


                                     σuser (t + 1) = e−λΔt ⋅ σuser (t) + σevent .

This is exactly the ALP PETC composition law with temporal decay.


5.3 Score and Adaptation

Given a semantic PETC state σ and a learned weight vector wsem , we define:


                                      S(t) = wsem ⋅ σ(t) = ∑ wsem,i σi (t)
                                                                    i

and influence:


                                              I(t) = γS(t)2 + δeβS(t) .

This scalar I(t) is then mapped to UI decisions (layouts, interventions, etc.). ALP’s role is to ensure that:


      • The semantic basis (dimensions of σ ) is stable and interpretable.
      • Composition and decay are structurally consistent across time.

5.4 Prime Products as Interpretability Only

In this revision, we explicitly forbid using giant prime products as primary state:

                                             σ
      • The canonical state is σ , not ∏i qi i .




                                                           6
     • Integer products are allowed only for logging, indexing, or diagnostics:


     • e.g. to label a user segment by the set of dominant primes (concepts) with exponents above a
       threshold.


     • Factorization is trivial once σ is known.

This fixes the original design flaw where integer products risked overflow and made factorization a
computational bottleneck.




6. Algorithms
This section gives clean, implementation-ready algorithms in ALP terms.


6.1 PETC Composition for Text

Input: sequence of units u1 , … , un at some layer (L1–L3).
Output: ALP code for composite unit.


    1. For each uk : obtain (pk , σk ) = ALP(uk ).
    2. Compute composite PETC vector:
                                                               n
                                                     σcomp = ∑ σk .
                                                              k=1

    3. Assign composite order prime pcomp according to ranking policy (e.g., highest frequency or specific
       lexical registry).
    4. Output (pcomp , σcomp ).

This procedure is associative and compatible with further composition.


6.2 Semantic State Update (UX)

Input: user state σuser (t), event e, mapping model M .
Output: updated state σuser (t + 1).


    1. Compute time delta Δt = tnow − tlast .
    2. Apply decay: σuser (t) ← e−λΔt σuser (t).
    3. Obtain semantic concepts: {(cj , sj )} = M (e).
    4. For each (cj , sj ):
    5. Map to index i = index(cj ).
    6. Update σuser,i (t) ← σuser,i (t) + sj .
    7. Return σuser (t + 1).




                                                        7
6.3 ACE-Constrained Rank Update (Optional)

For a given layer with association matrix At :

               ^t from current batch.
    1. Compute A
                                          ^t .
    2. Propose update At+1 = (1 − α)At + αA
    3. Compute ΔA = At+1 − At .
    4. Estimate ∥ΔA∥2 via power iteration.
                                      ^t until bound holds.
    5. If ∥ΔA∥2 > ε, reduce α or clip A
    6. Extract rankings (sorted indices) per row/role.
    7. Compare with previous ranking and apply at most K swaps.

This ensures gradual evolution of rank structure.




7. Evaluation and Diagnostics
ALP’s value must be established empirically. This revision defines explicit evaluation axes.


7.1 Structural Correctness

      • PETC-law violations: count how often downstream pipelines break the additive law (e.g. by
        mutating σ non-additively).
      • Rank churn: measure number of rank swaps per update; cap at K and report usage.

7.2 Predictive Utility

When ALP states are used as features for prediction (e.g., next token, user reward):


      • Compare models:
      • Baseline embeddings only.
      • Embeddings + ALP features (PETC exponents).
      • ALP-only (for ablation).
      • Metrics: accuracy, log-loss, AUC, calibration.

7.3 Interpretability

Given a PETC state σ :


    1. Extract dominant features: top-k dimensions by exponent.
    2. Map to human-readable concept IDs.
    3. Ask human raters:
    4. Does this list summarize the unit/state meaningfully?
    5. Can they explain a downstream decision from σ alone?

This yields a quantitative interpretability score that can be directly compared to baseline embedding-only
systems.




                                                         8
7.4 Stability

     • Monitor spectral drift of association matrices when ACE is enabled.
     • Track rank churn and outliers (rare, extreme reorderings).
     • For UX: track layout-switch frequency and user-level volatility.




8. Limitations and Non-Goals
This revision is intentionally blunt about what ALP does not guarantee.


    1. No inherent performance boost. ALP provides structure and interpretability; predictive gains are
       UNPROVEN and must be tested empirically.
    2. Ontological arbitrariness. Choice of semantic primitives and feature primes is human-designed or
       learned; different bases may yield equivalent performance.
    3. Scalability of feature space. Large d (thousands of primes) leads to sparsity and the same issues as
       high-dimensional one-hot features.
    4. No magic from primes alone. Primes are used as stable, factorable IDs. Their arithmetic properties
       only matter in diagnostics and interpretability, not in the core learning.
    5. Complexity of ACE. ACE’s spectral and churn constraints are valuable but expensive; many
       deployments will start without ACE and add it only when necessary.




9. Integration Blueprint
To deploy ALP in a real system (e.g., a UX adaptation engine or a language analytics stack):


    1. Define the PETC basis: decide which features (syntactic, morphological, semantic) deserve
       dedicated dimensions.
    2. Build registries: L1–L3 vocabularies with order primes and PETC signatures.
    3. Implement mapping models: from raw input to ALP codes, layer by layer.
    4. Hook into ML pipelines: feed PETC vectors as features alongside embeddings; train predictive
       models.
    5. Add ACE if needed: introduce controlled ranking updates when dynamic reordering becomes
       important.
    6. Measure, don’t assume: evaluate performance and interpretability against baselines and iterate.




10. Conclusion
This revised Atomic Language Processing specification distills the original idea into a form that is:


     • Computationally sane: exponent vectors, not giant integers, are the core representation.
     • Mathematically clean: ALP is a monoid over PETC signatures, with optional stability constraints via
       ACE.




                                                       9
     • Implementation-ready: clear data structures, update rules, and integration points.
     • Falsifiable: makes no promises of automatic performance gains; its value is in structure,
       interpretability, and the ability to factor complex states into atomic components.

Primes, in this framework, are not mystical. They are simply a way to guarantee uniqueness and
factorability of the atomic units and features that matter. The real work—and the real test—is in how well
those units capture the structure of language and experience in practice.




                                                    10
