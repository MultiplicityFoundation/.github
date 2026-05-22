---
slug: atomic-language-processing-tech-spec
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/Atomic Language Processing - Tech Spec.md
  last_synced: '2026-03-20T17:17:15.199593Z'
---

Atomic Language Processing (ALP)
Engineering Specification / Internal RFC
Status: Draft – Engineering-Facing
Version: 2.0
Audience: Backend / Platform / ML engineers
Primary Use Case: Prime-indexed, interpretable feature layer for text and UX/interaction data.




1. Purpose
ALP (Atomic Language Processing) is a data representation layer. It defines how to:


     • Encode units (characters, morphemes, words, semantic concepts, UX events) as discrete IDs +
       feature vectors.
     • Compose these units via additive feature vectors ("PETC vectors") instead of ad‑hoc feature bags.
     • Keep representations stable and interpretable over time while still allowing updates.

ALP is not a model. It is a spec for vocabularies, data structures, and update algorithms that upstream
and downstream systems can rely on.


Primary design goals:


    1. Stable IDs: Units and features have durable IDs (primes or integers); no silent re-use or collisions.
    2. Compositional features: Composition is defined as simple, additive operations over vectors.
    3. Interpretability: States can be read as "counts/weights of known concepts"; no opaque embedding
       indices.
    4. ML-compatible: ALP outputs are just vectors and IDs – usable by any standard ML stack.

Non-goals (v2.0):


     • Proving ALP improves model performance. That must be tested per application.
     • Providing a full ranking/ACE system in v1 deployments.
     • Acting as a replacement for embeddings or neural encoders.




2. Core Concepts (Engineer-Friendly)

2.1 Units, Features, and Vocabularies

Unit: Any atomic object you want to track, e.g.


     • Text: grapheme, subword, token, phrase.




                                                     1
     • UX: semantic concept like "intent:purchase" , "emotion:frustration" .

Feature basis: Fixed set of feature dimensions. Each feature has:


     • feature_id (string, e.g. "emotion:frustration" )
     • feature_index (int, 0..d−1)
     • Optional: prime (int) for logging / symbolic factorization only.

PETC vector: A non-negative real vector of length d :


     • sigma[i] = intensity / multiplicity of feature dimension i .

2.2 Composition Rule

For ALP, composition is always additive in feature space:



  sigma_comp = sigma_a + sigma_b


Optionally with decay in time-series contexts:



  sigma_t+1 = exp(-lambda * dt) * sigma_t + sigma_event


No giant integer products are used in runtime logic.




3. Data Model

3.1 Core Types

Language-agnostic conceptual model (map directly to code in your language of choice):



  ALPFeature
    feature_id: string                # logical name (e.g., "emotion:frustration")
    index: int                        # 0..d-1, position in feature vector
    prime: int (optional)             # unique prime, for logging/analysis only

  ALPVocabulary
    version: string
    features: List[ALPFeature]
    feature_id_to_index: Map[string -> int]
    index_to_feature_id: Map[int -> string]
    index_to_prime: Map[int -> int] (optional)
    prime_to_index: Map[int -> int] (optional)




                                                       2
  ALPVector
    values: float[d]        # PETC vector; runtime representation

  ALPState
    vector: ALPVector
    last_updated_seconds: float


3.2 Layer-Specific Vocabularies (Optional)

You can define separate vocabularies per layer:


     • L1 : grapheme-level features (script, type, etc.).
     • L2 : morph/subword-level features.
     • L3 : lexical or semantic features.

In practice, for UX semantics we only need a single semantic vocabulary (see Section 6).




4. Algorithms (Generic ALP)

4.1 Vector Composition

Goal: Combine multiple units into a composite unit or state.


Inputs: - sigma_list: List[ALPVector]


Output: - sigma_comp: ALPVector


Pseudo-code:



  def compose_vectors(sigma_list: list[np.ndarray]) -> np.ndarray:
      if not sigma_list:
          raise ValueError("sigma_list must be non-empty")
      # All vectors must share the same dimension d
      d = sigma_list[0].shape[0]
       result = np.zeros(d, dtype=np.float32)
       for s in sigma_list:
           assert s.shape[0] == d
           result += s
       return result


4.2 Time-Decayed State Update

Goal: Maintain a time-varying state with exponential decay.




                                                       3
Inputs:    -      state.vector :     current     PETC     vector       (np.ndarray   of   shape   [d])   -
state.last_updated_seconds : float timestamp - event_vector : PETC vector for new event (shape
[d]) - now_seconds : current time - lambda_ : decay rate per second (float)


Output: - Updated state.vector and state.last_updated_seconds .


Pseudo-code:



  import numpy as np
  import time

  class ALPState:
      def __init__(self, dim: int):
          self.vector = np.zeros(dim, dtype=np.float32)
          self.last_updated_seconds = time.time()

       def update(self, event_vector: np.ndarray, lambda_: float) -> None:
           now = time.time()
           dt = max(0.0, now - self.last_updated_seconds)
           decay = float(np.exp(-lambda_ * dt))
           self.vector *= decay
           self.vector += event_vector
               self.last_updated_seconds = now


4.3 Optional ACE Rank Update

If you need stable rankings (e.g., ordering of units by some association score) and want to avoid wild
oscillations:


     • Maintain an association matrix A (units × roles or contexts).
     • Update via EMA.
     • Enforce:
     • spectral drift bound: ||A_{t+1} - A_t||_2 <= epsilon (approximate via power iteration).
     • churn cap: at most K swaps in sorted rankings per update.

This is optional and not required for the semantic primes UX use case.




5. APIs & File Formats

5.1 Vocabulary File Schema (JSON)

Example schema for a feature vocabulary (used as PETC basis):




                                                     4
    {
        "version": "1.0",
        "description": "Feature vocabulary",
        "features": [
            {
                "feature_id": "emotion:frustration",
                "description": "User is frustrated or annoyed",
                "prime": 3,
                "index": 0
            }
        ]
    }


Validation rules:


        • index must be unique and compact 0..d-1 .
        • prime (if present) must be unique across the vocab.
        • feature_id must be unique.

5.2 Mapping Model Interface

For each layer/application, you implement a mapping:



    from typing import List, Tuple

    class ALPMappingModel:
        def to_features(self, unit) -> List[Tuple[str, float]]:
            """Return a list of (feature_id, score) pairs.

                 - feature_id must exist in the vocabulary
                 - score ∈ [0, 1]
                 - must be deterministic for a given unit
                 """
                 raise NotImplementedError


A   helper       then   converts   (feature_id,   score)      pairs   into   an   aligned   PETC   vector   using
ALPVocabulary.feature_id_to_index .




6. Semantic Primes for UX Adaptation (Internal RFC)
This section specializes ALP to the UX/interaction setting.




                                                       5
6.1 Problem Statement

We want a semantic, interpretable user state for UX adaptation, where:


     • Each dimension represents a stable concept (e.g., intent:purchase , emotion:frustration ,
       topic:tech ).
     • User state is a time-decayed count/intensity of these concepts.
     • The adaptation engine can:
     • Use this state as a feature vector for scoring.
     • Surface the dominant concepts for explanation/debugging.

6.2 Semantic Vocabulary (UX)

We define a 20-concept semantic vocabulary in semantic_vocab.json (example already drafted):


     • concept_id ~ feature_id in generic ALP terms.
     • index = dimension in the PETC vector.
     • prime = unique prime used only for logging/debug.

Engine-facing loader:



  # backend/app/semantic_vocab.py
  import json
  from dataclasses import dataclass
  from typing import Dict, List

  @dataclass
  class SemanticConcept:
      concept_id: str
      description: str
      prime: int
      index: int


  class SemanticVocabulary:
      """Immutable, versioned semantic vocabulary for UX."""

       def __init__(self, vocab_path: str):
           with open(vocab_path, "r", encoding="utf-8") as f:
               data = json.load(f)

            self.version = data["version"]
            self.concepts: List[SemanticConcept] = []

            self.concept_to_prime: Dict[str, int] = {}
            self.concept_to_index: Dict[str, int] = {}
            self.prime_to_concept: Dict[int, str] = {}
            self.index_to_concept: Dict[int, str] = {}




                                                   6
            self.index_to_prime: Dict[int, int] = {}
            self.prime_to_index: Dict[int, int] = {}

            for item in data["concepts"]:
                c = SemanticConcept(
                      concept_id=item["concept_id"],
                      description=item["description"],
                      prime=item["prime"],
                      index=item["index"],
                 )
                 self.concepts.append(c)

                 self.concept_to_prime[c.concept_id] = c.prime
                 self.concept_to_index[c.concept_id] = c.index
                 self.prime_to_concept[c.prime] = c.concept_id
                 self.index_to_concept[c.index] = c.concept_id
                 self.index_to_prime[c.index] = c.prime
                 self.prime_to_index[c.prime] = c.index

          # Basic validation
          n = len(self.concepts)
          assert set(self.index_to_concept.keys()) == set(range(n)),
  "Indices must be 0..n-1"

       @property
       def num_concepts(self) -> int:
           return len(self.concepts)


6.3 Semantic Mapping Model (UX)

We define a deterministic, rule-based mapping model for v1:



  # backend/app/semantic_mapper.py
  from typing import List, Tuple
  from .models import InteractionEvent
  from .semantic_vocab import SemanticVocabulary

  class SemanticMappingModel:
      def predict_concepts(self, event: InteractionEvent) -> List[Tuple[str,
  float]]:
           """Map event -> list of (concept_id, score) pairs.

            - Must be deterministic.
            - concept_id must exist in SemanticVocabulary.
            """
            raise NotImplementedError




                                                   7
class RuleBasedSemanticMapper(SemanticMappingModel):
    def __init__(self, vocab: SemanticVocabulary):
        self.vocab = vocab


    def predict_concepts(self, event: InteractionEvent) -> List[Tuple[str,
float]]:
         concepts: List[Tuple[str, float]] = []


        page = str(event.props.get("page", ""))
        event_type = event.event_type
        element_id = str(event.props.get("element_id", ""))
        scroll_depth = float(event.props.get("scroll_depth", 0.0))
        dwell_ms = float(event.props.get("dwell_time_ms", 0.0))
        user_agent = str(event.props.get("user_agent", ""))

        # Example rules; extend as needed
        if "checkout" in page or "buy" in element_id.lower():
            concepts.append(("intent:purchase", 0.9))
            concepts.append(("emotion:urgency", 0.6))

        if scroll_depth > 0.8 and dwell_ms > 5000:
            concepts.append(("engagement:deep", 0.8))

        if event_type == "rage_click" or "error" in element_id:
            concepts.append(("emotion:frustration", 0.7))
            concepts.append(("emotion:confusion", 0.6))

        if "compare" in page or event_type == "compare_click":
            concepts.append(("intent:compare", 0.8))

        if "signup" in page or "register" in element_id:
            concepts.append(("intent:signup", 0.85))

        if "mobile" in user_agent.lower():
            concepts.append(("context:mobile", 1.0))
        else:
            concepts.append(("context:desktop", 1.0))

        if not concepts:
            # Low-confidence catch-all with small weight
            concepts.append(("uncertainty:low_confidence", 0.1))

        return concepts




                                       8
6.4 Semantic Encoder and State (UX)

Encodes events into indices and maintains user state.



  # backend/app/semantic_encoder.py
  from typing import List, Tuple
  from .models import InteractionEvent
  from .semantic_vocab import SemanticVocabulary
  from .semantic_mapper import SemanticMappingModel

  class SemanticPrimeEncoder:
      """Arm C encoder: event -> semantic concept indices/scores."""

       def __init__(
           self,
           vocab: SemanticVocabulary,
           mapping_model: SemanticMappingModel,
           confidence_threshold: float = 0.3,
       ) -> None:
           self.vocab = vocab
           self.mapping_model = mapping_model
           self.confidence_threshold = confidence_threshold


      def encode_with_scores(self, event: InteractionEvent) -> List[Tuple[int,
  float]]:
           pairs = self.mapping_model.predict_concepts(event)
           result: List[Tuple[int, float]] = []
           for concept_id, score in pairs:
               if score < self.confidence_threshold:
                   continue
               idx = self.vocab.concept_to_index.get(concept_id)
               if idx is not None:
                   result.append((idx, float(score)))
           return result



  # backend/app/semantic_state.py
  import time
  import numpy as np
  from typing import List, Tuple
  from .semantic_vocab import SemanticVocabulary

  class SemanticState:
      """User-level PETC state over semantic concepts."""

       def __init__(self, vocab: SemanticVocabulary):
           self.vocab = vocab



                                                        9
            self.multiplicities = np.zeros(vocab.num_concepts, dtype=np.float32)
            self.last_updated_seconds = time.time()

      def update(self, indices: List[int], scores: List[float], lambda_: float) ->
  None:
            now = time.time()
            dt = max(0.0, now - self.last_updated_seconds)
            decay = float(np.exp(-lambda_ * dt))


            self.multiplicities *= decay
            for idx, score in zip(indices, scores):
                if 0 <= idx < len(self.multiplicities):
                    self.multiplicities[idx] += float(score)

            self.last_updated_seconds = now

       def feature_vector(self) -> np.ndarray:
           return self.multiplicities.copy()

      def dominant_themes(self, top_k: int = 3, min_weight: float = 0.5) ->
  List[Tuple[str, float]]:
          k = min(top_k, len(self.multiplicities))
          if k <= 0:
              return []
          top_idx = np.argpartition(-self.multiplicities, k - 1)[:k]
          top_idx = top_idx[np.argsort(-self.multiplicities[top_idx])]

            themes: List[Tuple[str, float]] = []
            for idx in top_idx:
                weight = float(self.multiplicities[idx])
                if weight < min_weight:
                    continue
                cid = self.vocab.index_to_concept.get(int(idx))
                if cid:
                    themes.append((cid, weight))
            return themes


6.5 Using Semantic State in the Adaptation Engine

At scoring time (Arm C):


    1. Retrieve or init SemanticState for user.
    2. Encode event to (indices, scores) via SemanticPrimeEncoder .
    3. Update state with decay.
    4. Get feature vector sigma = state.feature_vector() .
    5. Compute scalar state S = dot(w_semantic, sigma) (if using ML).
    6. Map S to influence/decision via your standard scoring function.




                                                   10
In code (simplified):



  # inside AdaptationEngine


  def _update_state_and_score_semantic(self, event: InteractionEvent) -> float:
      state = self._get_semantic_state(event.user_id)
      idx_scores = self.semantic_encoder.encode_with_scores(event)
      if not idx_scores:
             return 0.0

       indices, scores = zip(*idx_scores)
       state.update(list(indices), list(scores), lambda_=self.decay_lambda)

       sigma = state.feature_vector()
       # assume w_semantic aligned with vocab.num_concepts
       w = np.array(self.params.w_semantic, dtype=np.float32)
       if len(w) != sigma.shape[0]:
           # pad or truncate as needed (or fail fast in production)
           d = sigma.shape[0]
           w = w[:d] if len(w) >= d else np.pad(w, (0, d - len(w)))

       S = float(np.dot(w, sigma))
       return S


6.6 Experiment & Rollout

Recommended A/B strategy:


     1. Phase 1: Standard vs Semantic arms only.
     2. Phase 2: If semantic shows performance parity and better interpretability, consider adding
        structural or more concepts.

Metrics:


      • Primary: task completion / conversion rate.
      • Secondary: engagement, error/abort rates.
      • Interpretability: human-rated clarity of dominant themes explaining layout decisions.

Kill / promote criteria must be defined at the product level (not in this spec), but a typical pattern is:


      • Kill if semantic < baseline by >1% with statistical significance.
      • Promote if semantic ≥ baseline and interpretability metrics are meaningfully higher.




                                                        11
7. Implementation & Rollout Checklist
Phase 0 – Offline Only


     • [ ] Define PETC basis (features) and JSON vocab files.
     • [ ] Implement SemanticVocabulary , SemanticMappingModel , SemanticState .
     • [ ] Build scripts to encode logs into ALP vectors and run offline analysis.

Phase 1 – Read-Only Online (Logging)


     • [ ] Integrate ALP encoding into live pipelines, but use it only for logging.
     • [ ] Validate stability, performance, and interpretability of logged states.

Phase 2 – Feature in Models


     • [ ] Feed ALP vectors as features into existing models (alongside embeddings).
     • [ ] Evaluate impact on metrics.
     • [ ] Start small A/B with semantic arm.

Phase 3 – Iteration


     • [ ] Tune vocabularies and mapping rules.
     • [ ] Optionally add ACE-like stability constraints if rankings become dynamic.
     • [ ] Promote, demote, or kill based on metrics and operational cost.




8. Summary
This engineering spec for ALP reduces the framework to:


     • Vocabularies (feature bases with stable IDs/indexes).
     • Vectors (PETC exponent/multiplicity vectors).
     • Simple additive update rules (plus optional decay).
     • Optional stability wrapper (ACE) for ranking systems.

The "prime" story is kept as a logging/interpretability layer only; all runtime behavior depends solely on
indices and vectors, compatible with any existing ML and backend infrastructure.




                                                       12
