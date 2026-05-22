---
slug: adaptive-ux-engine-technical-blueprint
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/Adaptive Ux Engine - Technical Blueprint.md
  last_synced: '2026-03-20T17:17:15.290937Z'
---

Adaptive UX Engine – Technical Blueprint
Status: Draft – Engineering Design
Audience: Backend, Data/ML, Frontend
Primary Goal: Serve adaptive UI decisions per user/session based on interaction history, with support for
standard, structural-prime, and semantic-prime state representations.




1. System Overview
The Adaptive UX Engine is a backend service that:


    1. Collects client-side interaction events (page views, clicks, scrolls, etc.).
    2. Maintains user-level state via one of several encoders (arms).
    3. Computes an adaptation score and returns a layout / variant ID.
    4. Logs everything for offline training and A/B evaluation.

We support three experiment arms:


     • Arm A – Standard: event-level IDs + embeddings.
     • Arm B – Structural Primes: primes for structural attributes (page, element, event type) →
       multiplicity vector.
     • Arm C – Semantic Primes: primes for semantic concepts (intent, emotion, topic) → multiplicity
       vector.

The engine is designed so that encoding choice is pluggable; downstream scoring and adaptation logic
are shared.




2. High-Level Architecture
Components:


    1. Frontend SDK
    2. Captures interaction events.

    3. Sends /event and /adapt requests to backend.


    4. API Layer (FastAPI)


    5. Endpoints:
           ◦ POST /event – ingest interaction events.
           ◦ POST /adapt – compute layout decision for current context.

    6. Auth, rate limiting, basic validation.




                                                         1
    7. Adaptation Engine


    8. Core logic for state update and scoring.
    9. Maintains pluggable encoders for each arm.

   10. Returns AdaptationDecision objects.


   11. State Stores


   12. UserStateStore – per-user state for standard/structural arms.
   13. SemanticStateStore – per-user semantic PETC state (Arm C).

   14. In-memory for v1, pluggable to Redis/DB later.


   15. Model Params Loader


   16. Loads ModelParams from versioned JSON.

   17. Supports separate w and w_semantic vectors.


   18. Logging Pipeline


   19. Appends normalized events and decisions to log sink.

   20. Supports offline training, replay, and analysis.


   21. Training & Evaluation


   22. Offline jobs to train/update ModelParams per arm.

   23. Scripts to export params → JSON for deployment.


   24. Experiment Manager


   25. Deterministic user → arm assignment.
   26. Stores experiment config (splits, variants).




3. Data Model

3.1 Core DTOs

InteractionEvent (request-time and logging):



  class InteractionEvent(BaseModel):
      user_id: str




                                                          2
      session_id: str
      event_type: str                  # e.g. "page_view", "click", "scroll",
  "rage_click"
      props: dict                      # arbitrary context (page, element_id, device,
  etc.)
      timestamp_ms: int                # event time in ms since epoch


AdaptationDecision (response + logging):



  class AdaptationDecision(BaseModel):
      user_id: str
      layout_id: str             # chosen variant ID
      adaptation_score: float    # I(t)
      policy_version: int        # ModelParams.version
      timestamp_ms: int          # server decision time
      arm: str                   # "standard" | "structural" | "semantic"


3.2 User State (Standard / Structural)


  class UserState(BaseModel):
      user_id: str
      features: List[float]            # generic feature vector
      S: float                         # scalar state
      last_updated_ms: int             # for decay


     • Used by Arm A and Arm B.
     • features can grow over time as needed; dot-products only use overlapping dims.

3.3 Semantic State (Arm C)


  class SemanticState:
      vocab: SemanticVocabulary
      multiplicities: np.ndarray               # shape [num_concepts]
      last_updated_seconds: float


     • multiplicities[i] = decayed intensity of semantic concept i .

3.4 Model Parameters


  class ModelParams(BaseModel):
      embedding_dim: int               # for standard arm
      w: List[float]                   # weights for standard/structural features
      w_semantic: List[float]          # weights for semantic features (len =




                                                 3
  num_concepts)
      gamma: float
      delta: float
      beta: float
      tau_1: float                      # threshold 1 for layout selection
          tau_2: float                  # threshold 2 for layout selection
          learning_rate: float
          version: int


3.5 Semantic Vocabulary

      • Stored in semantic_vocab.json .


  {
      "version": "1.0",
    "description": "Semantic concepts for UX adaptation",
    "concepts": [
      { "concept_id": "intent:purchase", "description": "User intends to buy",
  "prime": 2, "index": 0 },
      { "concept_id": "emotion:frustration", "description": "User is frustrated",
  "prime": 3, "index": 1 }
      // ... up to 20 concepts
      ]
  }


Loaded by SemanticVocabulary , which exposes:



  class SemanticVocabulary:
      version: str
      num_concepts: int
      concept_to_index: Dict[str, int]
      concept_to_prime: Dict[str, int]
      index_to_concept: Dict[int, str]
      index_to_prime: Dict[int, int]


Primes are used only for logging and interpretability, not in model math.




4. Encoding & State Update
Each arm defines how an InteractionEvent updates state.




                                                   4
4.1 Arm A – Standard Encoder

Encoder:



  class StandardEncoder:
      def __init__(self):
          self.key_to_id: Dict[str, int] = {}
          self._next_id: int = 1


      def encode(self, event: InteractionEvent) -> int:
          page = str(event.props.get("page", "none"))
          element_id = str(event.props.get("element_id", "none"))
          key = f"{event.event_type}|{page}|{element_id}"
          if key not in self.key_to_id:
              self.key_to_id[key] = self._next_id
              self._next_id += 1
          return self.key_to_id[key]


State update:



  def update_state_standard(
      event: InteractionEvent,
      state: UserState,
      encoder: StandardEncoder,
      embedding_store: EmbeddingStore,
      params: ModelParams,
      decay_lambda: float,
      now_ms: int,
  ) -> None:
      # decay features
      state.features = decay_features(state.features, state.last_updated_ms,
  now_ms, decay_lambda)

      event_id = encoder.encode(event)
      state.features = ensure_dim(state.features, len(params.w))

      emb = embedding_store.get_or_init(event_id)
      emb = resize_vector(emb, len(state.features))

      state.features = [f + e for f, e in zip(state.features, emb)]
      state.last_updated_ms = now_ms




                                         5
4.2 Arm B – Structural Prime Encoder

Idea: Each event is decomposed into structural attributes (type, page, element, device), each mapped to a
prime, then to a basis index. State is a multiplicity vector over this basis.


Encoder:



  class StructuralPrimeEncoder:
       def __init__(self, prime_pool: List[int]):
           self.type_prime: Dict[str, int] = {}
           self.page_prime: Dict[str, int] = {}
           self.element_prime: Dict[str, int] = {}
           self.device_prime: Dict[str, int] = {}

            self.prime_to_index: Dict[int, int] = {}
            self.index_to_prime: List[int] = []
            self._prime_pool = prime_pool[:] # copy

       def _get_index_for_value(self, mapping: Dict[str, int], key: str) -> int:
           if key in mapping:
               p = mapping[key]
           else:
                 if not self._prime_pool:
                     raise RuntimeError("Prime pool exhausted")
                 p = self._prime_pool.pop(0)
                 mapping[key] = p

            if p not in self.prime_to_index:
                idx = len(self.index_to_prime)
                self.prime_to_index[p] = idx
                self.index_to_prime.append(p)
            return self.prime_to_index[p]

       def encode_factor_indices(self, event: InteractionEvent) -> List[int]:
           page = str(event.props.get("page", "none"))
           element_id = str(event.props.get("element_id", "none"))
           device = str(event.props.get("device", "unknown"))

            idx_type = self._get_index_for_value(self.type_prime, event.event_type)
            idx_page = self._get_index_for_value(self.page_prime, page)
            idx_element = self._get_index_for_value(self.element_prime, element_id)
            idx_device = self._get_index_for_value(self.device_prime, device)

            return [idx_type, idx_page, idx_element, idx_device]


State update (structural arm):




                                                   6
  def update_state_structural(
      event: InteractionEvent,
      state: UserState,
      encoder: StructuralPrimeEncoder,
      decay_lambda: float,
      now_ms: int,
  ) -> None:
      state.features = decay_features(state.features, state.last_updated_ms,
  now_ms, decay_lambda)

       indices = encoder.encode_factor_indices(event)
       if not indices:
           return

       max_idx = max(indices)
       state.features = ensure_dim(state.features, max_idx + 1)

       for idx in indices:
           if 0 <= idx < len(state.features):
               state.features[idx] += 1.0

       state.last_updated_ms = now_ms


4.3 Arm C – Semantic Prime Encoder

Idea: Map events to semantic concepts (intent, emotion, topic). Maintain a PETC-style multiplicity vector
over these concepts per user.


Mapping model and encoder: see Section 6 of the ALP spec (already defined in separate doc).


State update (semantic arm):



  def update_state_semantic(
      event: InteractionEvent,
      state: SemanticState,
      encoder: SemanticPrimeEncoder,
      decay_lambda: float,
  ) -> None:
      idx_score_pairs = encoder.encode_with_scores(event)
      if not idx_score_pairs:
          return

       indices, scores = zip(*idx_score_pairs)
       state.update(list(indices), list(scores), lambda_=decay_lambda)




                                                   7
5. Scoring & Adaptation

5.1 Scalar State S(t)

For each arm, we reduce the feature vector to a scalar S :


     • Standard / Structural arms:


  S = dot(params.w, state.features)


     • Semantic arm:


  sigma = semantic_state.feature_vector() # shape [num_concepts]
  w_sem = np.array(params.w_semantic, dtype=np.float32)
  # ensure same length as sigma
  if len(w_sem) != sigma.shape[0]:
      d = sigma.shape[0]
      w_sem = w_sem[:d] if len(w_sem) >= d else np.pad(w_sem, (0, d - len(w_sem)))
  S = float(np.dot(w_sem, sigma))


5.2 Influence Function I(t)

Shared non-linear transformation:



  def compute_influence(S: float, params: ModelParams) -> float:
      return params.gamma * S * S + params.delta * math.exp(params.beta * S)


5.3 Layout Selection

Three regions based on I :



  def choose_layout(I: float, params: ModelParams) -> str:
      if I < params.tau_1:
          return "control_layout"
      if I < params.tau_2:
          return "layout_soft_adapt"
      return "layout_aggressive_adapt"


5.4 End-to-End /adapt Flow

    1. Frontend calls POST /adapt with user_id , session_id , and context.
    2. API converts to InteractionEvent (e.g., synthetic "page_view" event).



                                                     8
    3. Engine assigns arm via deterministic hash of user_id .
    4. Engine updates the corresponding state (standard, structural, or semantic).
    5. Engine computes S , I , and layout_id .
    6. Engine logs (event, state summary, decision) .
    7. API returns AdaptationDecision payload.




6. Experimentation & Logging

6.1 Arm Assignment

Simple deterministic assignment by hash bucket:



  def assign_arm(user_id: str) -> str:
       h = hash(user_id) % 100
       if h < 50:
           return "standard"                # 50%
       elif h < 75:
           return "structural"              # 25%
       else:
           return "semantic"                # 25%


Splits are configurable; start with Standard vs Semantic only if traffic is low.


6.2 Logged Fields

For each event + decision, log:


      • user_id , session_id , timestamp_ms
      • arm
      • event_type , props
      • layout_id
      • S , I
      • For semantic arm:
      • semantic_top_themes : output of SemanticState.dominant_themes()
      • Optional: semantic_prime_product_debug : result of debug_prime_product() (for offline
       only)

6.3 Metrics

Per arm:


      • Primary: conversion / task completion rate.
      • Secondary: average pages per session, time on task, error rate.
      • Operational: p95 latency, error rates, CPU/memory.




                                                        9
Interpretability (semantic arm):


     • Sample sessions, extract semantic_top_themes and decisions.
     • Human raters score how well themes explain the layout choice.




7. Training & Deployment Pipeline

7.1 Offline Training Data

From logs, construct per-event training records:


     • Input:
     • user_id , arm , features (state features or semantic vector snapshot).
     • Target:
     • reward (e.g. conversion, success flag).

7.2 Model Training

For each arm (optional for v1):


     • Train a simple linear/logistic model on features → reward.
     • Use learned weights to update:
     • params.w (standard/structural arms).
     • params.w_semantic (semantic arm).

7.3 Params Export

     • Serialize ModelParams to model_params.json with version bump.
     • API/engine reloads on deploy.

7.4 Rollout

     • Start with read-only semantic logging (no live decisions).
     • Move to small traffic semantic arm (5–10%).
     • Evaluate metrics and interpretability.
     • Promote / demote / kill based on pre-defined criteria.




8. Operational Concerns

8.1 Performance Targets

     • p95 latency for /adapt < 50–100 ms server-side.
     • State updates O(d) where d is feature dimension (keep d small: 20–200 for semantic arm).




                                                     10
8.2 State Storage

v1: In-memory stores (Python dicts).
v2+: Redis or key-value store per arm for horizontal scaling.


8.3 Fault Tolerance

     • On state lookup failure: re-init state with zeros.
     • On model params load failure: fall back to previous version or safe defaults.
     • If semantic mapping fails: default to standard arm or control layout.

8.4 Configuration

     • model_params_path : path to model_params.json .
     • semantic_vocab_path : path to semantic_vocab.json .
     • decay_lambda : time-decay rate per second.
     • experiment_config : optional dynamic config for arm fractions.




9. Extensibility
Future extensions (non-breaking to core design):


     • Add new semantic concepts by extending semantic_vocab.json and retraining w_semantic .
     • Introduce dynamic semantic mapping (classifier-based) behind SemanticMappingModel while
       keeping public interface stable.
     • Add ACE-style stability controls for any layer that starts using dynamic rankings.
     • Support additional adaptation targets (not just layout_id, but also copy variants, content modules,
       etc.).

The blueprint above is sufficient for a v1 implementation: engineers can build the service, wire the three
arms, log correctly, and iterate on models without revisiting the underlying representation choices.




                                                      11
