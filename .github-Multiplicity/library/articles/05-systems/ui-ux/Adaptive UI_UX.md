---
slug: adaptive-ui-ux
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/ui-ux/Adaptive UI_UX.md
  last_synced: '2026-03-20T17:17:17.655032Z'
---

**1. Adaptive UX Engine -- Engineering-Facing Spec**
----------------------------------------------------

### **1.1. Goal & Scope**

**Goal\
** Build an online service that:

1.  Consumes user interaction events.

2.  Encodes them (either with **prime IDs** or **standard
    > IDs/embeddings**).

3.  Maintains a per-user state vector.

4.  Computes an "adaptation score" and chooses UI variants in real time.

5.  Logs everything for offline training and A/B analysis.

**Explicit non-goals (for v1)**

-   No real quantum hardware.

-   No tensor network research toys; we approximate with standard
    > emb+ML.

-   No claim that primes improve performance; they're just an
    > alternative encoding we will test.

### **1.2. High-Level Architecture**

Components:

1.  **Event Collector\
    > **

    -   Accepts front-end events (page\_view, click, scroll, etc.).

    -   Normalizes + timestamps them.

2.  **Interaction Encoder\
    > **

    -   Maps an (event\_type, metadata) → integer ID.

    -   Two interchangeable strategies:

        -   PrimeEncoder: event → prime number.

        -   StandardEncoder: event → non-prime integer ID or embedding
            > index.

3.  **User State Store\
    > **

    -   Maintains per-user feature vectors and scalar summary S(t).

4.  **Adaptation Engine\
    > **

    -   Given (user state, context), outputs:

        -   UI layout choice / content variant.

        -   Adaptation intensity (how much to change).

5.  **Policy Store\
    > **

    -   Holds model parameters (α\_k, model weights, thresholds).

6.  **Logger\
    > **

    -   Writes all inputs/outputs to an immutable store for offline
        > learning.

7.  **Offline Trainer\
    > **

    -   Trains/updates model parameters from logs.

    -   Produces new policies to deploy.

### **1.3. Core Data Structures (conceptual)**

// Event schema after frontend -\> backend normalization

struct InteractionEvent {

string user\_id

string session\_id

string event\_type // e.g. \"click\", \"page\_view\", \"form\_submit\"

map\<string, any\> props // e.g. { \"element\_id\": \"btn\_signup\",
\"page\": \"/home\" }

int64 timestamp\_ms

}

// Encoded event

struct EncodedEvent {

string user\_id

int64 event\_id // prime or standard int

float weight // initial weight (e.g., 1.0) or derived

int64 timestamp\_ms

}

// User state

struct UserState {

string user\_id

vector\<float\> features // learned features or counts

float S // scalar score derived from features

int64 last\_updated\_ms

}

// Adaptation decision

struct AdaptationDecision {

string user\_id

string layout\_id // e.g. \"control\", \"var\_A\", \"var\_B\"

float adaptation\_score // I(t)

float policy\_version

int64 timestamp\_ms

}

### **1.4. Interaction Encoding Module**

We make encoding **pluggable** so prime vs standard becomes a simple
switch.

#### **1.4.1. PrimeEncoder**

Assigns a unique prime to each interaction key.

interface Encoder {

int64 encode(InteractionEvent e)

}

// Mapping keys, not raw events, to primes:

string make\_key(InteractionEvent e) {

// Example: event\_type + \":\" + stable element/page identifier

element = e.props.get(\"element\_id\", \"none\")

page = e.props.get(\"page\", \"none\")

return e.event\_type + \"\|\" + page + \"\|\" + element

}

class PrimeEncoder implements Encoder {

map\<string, int64\> key\_to\_prime

list\<int64\> prime\_pool // e.g. \[2,3,5,7,11,\...\] pre-generated

int64 encode(InteractionEvent e) {

string key = make\_key(e)

if key\_to\_prime.contains(key) {

return key\_to\_prime\[key\]

}

// Assign next prime

int64 p = prime\_pool.pop\_front()

key\_to\_prime\[key\] = p

return p

}

}

#### **1.4.2. StandardEncoder (Control)**

Same concept, without primes:

class StandardEncoder implements Encoder {

map\<string, int64\> key\_to\_id

int64 next\_id = 1

int64 encode(InteractionEvent e) {

string key = make\_key(e)

if key\_to\_id.contains(key) {

return key\_to\_id\[key\]

}

key\_to\_id\[key\] = next\_id

next\_id += 1

return key\_to\_id\[key\]

}

}

Backend will pick one encoder depending on experiment arm (see A/B
design later).

### **1.5. User State Update Logic**

We approximate your S(t)=∑kαk(t)pkS(t) = \\sum\_k \\alpha\_k(t)
p\_kS(t)=∑k​αk​(t)pk​ using vector ops.

#### **1.5.1. Model Parameters**

struct ModelParams {

matrix\<float\> embedding\_matrix // \[num\_ids x d\], trains alpha-like
weights

vector\<float\> w // \[d\], projects to scalar S(t)

float gamma // for quadratic term

float delta // for exponential term

float beta // for exponential term

float learning\_rate

}

#### **1.5.2. Online Update (Per Event)**

function handle\_event(event: InteractionEvent, encoder: Encoder, model:
ModelParams):

// 1. Encode event

id = encoder.encode(event)

// 2. Look up / create user state

state = UserStateStore.get\_or\_init(event.user\_id)

// 3. Build feature increment

// Simple version: embedding lookup

v = model.embedding\_matrix\[id\] // vector\<float\> of dimension d

// 4. Update user feature state (exponential decay + new info)

dt = max(0, event.timestamp\_ms - state.last\_updated\_ms)

decay\_factor = exp(-lambda \* dt) // lambda: hyperparam

state.features = decay\_factor \* state.features + v

// 5. Compute scalar S(t)

state.S = dot(model.w, state.features)

// 6. Persist updated state

state.last\_updated\_ms = event.timestamp\_ms

UserStateStore.put(state)

// 7. Optionally compute adaptation decision (if event\_type triggers
it)

if should\_adapt(event):

decision = make\_adaptation\_decision(state, model)

Logger.log\_decision(event, state, decision)

return decision

else:

return null

### **1.6. Adaptation Decision Logic**

We implement your non-linear influence function:

I(t)=γS(t)2+δeβS(t)I(t) = \\gamma S(t)\^2 + \\delta e\^{\\beta
S(t)}I(t)=γS(t)2+δeβS(t)

#### **1.6.1. Pseudocode**

function compute\_influence(S: float, model: ModelParams) -\> float:

return model.gamma \* S \* S + model.delta \* exp(model.beta \* S)

function make\_adaptation\_decision(state: UserState, model:
ModelParams) -\> AdaptationDecision:

score = compute\_influence(state.S, model)

// Map influence score into discrete layout choice.

// Example thresholds -- tune empirically.

if score \< tau\_1:

layout = \"control\_layout\"

else if score \< tau\_2:

layout = \"layout\_soft\_adapt\"

else:

layout = \"layout\_aggressive\_adapt\"

decision = AdaptationDecision(

user\_id = state.user\_id,

layout\_id = layout,

adaptation\_score = score,

policy\_version = CURRENT\_POLICY\_VERSION,

timestamp\_ms = now\_ms()

)

return decision

### **1.7. Reward & Offline Training**

We define a simple reward: e.g. 1 if user completes desired action
within session, 0 otherwise. Replace with your actual KPI.

#### **1.7.1. Logged Row for Training**

struct TrainingSample {

vector\<float\> features // state.features snapshot at decision time

string layout\_id

float reward // observed later

bool is\_prime\_arm // true if prime encoding

int64 policy\_version

}

#### **1.7.2. Training Loop (Sketch)**

function train\_model(samples: list\<TrainingSample\>) -\> ModelParams:

model = init\_model()

for epoch in 1..NUM\_EPOCHS:

shuffle(samples)

for batch in batches(samples, BATCH\_SIZE):

loss = 0

grad\_w = zeros\_like(model.w)

grad\_embeddings = zeros\_like(model.embedding\_matrix)

for sample in batch:

// predicted S, then I, then p(success \| S)

S\_pred = dot(model.w, sample.features)

I\_pred = compute\_influence(S\_pred, model)

p = sigmoid(I\_pred) // simple logistic link

// binary cross-entropy loss

loss += - (sample.reward \* log(p) + (1 - sample.reward) \* log(1 - p))

// backpropigate to w and embeddings as usual

// (not fully expanded here, but standard autodiff in practice)

update\_grads(\...)

apply\_gradients(model, grad\_w, grad\_embeddings, learning\_rate)

return model

Engineers would implement this with a normal ML framework and auto-diff;
we've defined the objective.

### **1.8. Integration with Frontend**

**Frontend responsibilities:**

-   Attach user\_id or anon ID.

-   Emit InteractionEvent JSON payloads via HTTP or message bus.

-   On page load/navigation:

    -   Call Adaptation API → get layout\_id.

    -   Render corresponding UI variant.

**Adaptation API (simplified REST)**

POST /adapt

{

\"user\_id\": \"\...\",

\"session\_id\": \"\...\",

\"context\": { \"page\": \"/home\", \"device\": \"mobile\" }

}

Response:

{

\"layout\_id\": \"layout\_soft\_adapt\",

\"policy\_version\": 7,

\"timestamp\_ms\": 1734300000000

}

Backend then logs decision and subsequent events for training.

### **1.9. Limitations (Called Out, Not Hidden)**

-   Prime encoding & standard encoding are **interchangeable** in this
    > design; no algorithmic advantage is assumed.

-   All "multiplicity" structure is currently implemented as "different
    > IDs / embeddings".

-   Quantum stuff is **removed**; if you want it back, it goes into
    > Offline Trainer as a separate research project, not production.

**2. A/B Experiment: Prime vs Standard Encoding**
-------------------------------------------------

Goal: **Empirically test** whether prime-based encoding yields any
meaningful UX or model performance gains vs standard integer IDs.

### **2.1. Hypotheses**

We'll define everything crisply:

-   **H₀ (null)**: Prime encoding ≡ standard encoding; no difference in
    > key UX metrics.

-   **H₁ (alt)**: Prime encoding produces **different** outcomes (better
    > or worse) on key metrics.

(If you want directional, you can set H₁: prime \> standard, but I'd
start two-sided.)

### **2.2. Experiment Arms**

-   **Arm A -- Standard\
    > **

    -   Encoder: StandardEncoder (non-prime IDs).

    -   Everything else identical.

-   **Arm B -- Prime\
    > **

    -   Encoder: PrimeEncoder (primes for events).

    -   Same model architecture, same training frequency, same feature
        > pipeline.

**Important constraint:\
** No other differences. Same UI variants, thresholds, hyperparams,
environments.

### **2.3. Randomization & Unit**

-   **Randomization unit**: user\_id.

-   **Assignment**: sticky (once assigned, always in same arm).

Pseudocode:

function assign\_arm(user\_id: string) -\> string:

hash\_val = stable\_hash(user\_id)

bucket = hash\_val % 100

if bucket \< 50:

return \"standard\" // Arm A

else:

return \"prime\" // Arm B

-   **Traffic split**: 50/50 unless you're resource-constrained.

### **2.4. Eligibility & Exposure**

-   Include users who:

    -   Have at least 1 session with ≥ N interactions (e.g. N = 3) to
        > avoid noise.

    -   Are not bots (apply whatever filters you already use).

-   Exposure start: first time we see a user after experiment start
    > timestamp.

### **2.5. Metrics**

Pick a **single primary metric**, a couple of secondaries, and
guardrails.

#### **2.5.1. Primary Metric (choose one)**

Depends on your product; examples:

1.  **Task completion rate\
    > **

    -   E.g., % of users who complete signup / checkout within 24h of
        > first session in experiment.

2.  **Click-through rate on key CTA\
    > **

    -   (\# of users who click primary CTA at least once) / (total
        > users).

Choose **one** as primary and pre-register it.

#### **2.5.2. Secondary Metrics**

-   Engagement: average \# interactions per session.

-   Time-to-task-completion.

-   Layout-switch rate: how often the adaptation engine changes layout
    > for a user.

#### **2.5.3. Guardrail Metrics (to ensure no harm)**

-   Error rate (JS errors, 4xx/5xx).

-   Bounce rate / rage-clicks.

-   Latency of Adaptation API (p95, p99).

### **2.6. Sample Size & Duration**

You want enough users to detect a realistic effect size.

Let:

-   pAp\_ApA​ = baseline primary metric rate (e.g. current completion
    > rate = 0.20).

-   pBp\_BpB​ = expected rate with prime encoding.

-   You want to detect a **relative lift** of L (e.g. 2--5%).

Use standard two-proportion sample size formula:

n≈2⋅(z1−α/2+z1−β)2⋅pˉ(1−pˉ)Δ2n \\approx \\frac{2 \\cdot
(z\_{1-\\alpha/2} + z\_{1-\\beta})\^2 \\cdot \\bar{p} (1 -
\\bar{p})}{\\Delta\^2}n≈Δ22⋅(z1−α/2​+z1−β​)2⋅pˉ​(1−pˉ​)​

Where:

-   pˉ=(pA+pB)/2\\bar{p} = (p\_A + p\_B)/2pˉ​=(pA​+pB​)/2,

-   Δ=∣pB−pA∣\\Delta = \|p\_B - p\_A\|Δ=∣pB​−pA​∣,

-   α\\alphaα = 0.05 (two-sided), z1−α/2≈1.96z\_{1-\\alpha/2} \\approx
    > 1.96z1−α/2​≈1.96,

-   β\\betaβ = 0.2 → power 80%, z1−β≈0.84z\_{1-\\beta} \\approx
    > 0.84z1−β​≈0.84.

**Concrete example** (just to sanity-check):

-   Assume baseline completion: pA=0.20p\_A = 0.20pA​=0.20.

-   You care about a +3% absolute lift: pB=0.23p\_B = 0.23pB​=0.23 (this
    > is already optimistic).

-   pˉ=0.215\\bar{p} = 0.215pˉ​=0.215, Δ=0.03\\Delta = 0.03Δ=0.03.

Compute:

n≈2(1.96+0.84)2⋅0.215(1−0.215)0.032n \\approx \\frac{2 (1.96 + 0.84)\^2
\\cdot 0.215(1 - 0.215)}{0.03\^2}n≈0.0322(1.96+0.84)2⋅0.215(1−0.215)​

You'd plug this into a calculator; ballpark is on the order of **tens of
thousands of users per arm**. If you're smaller, you will **not** detect
tiny effects; accept that.

Duration:

-   Run until you hit **required sample size** *and* a **minimum time
    > window** (e.g. 2--4 weeks) to cover weekly cycles.

### **2.7. Logging Requirements**

You **must** log enough to reconstruct the experiment offline:

For each adaptation decision:

{

\"user\_id\": \"\...\",

\"arm\": \"standard\" \| \"prime\",

\"encoded\_event\_ids\": \[123, 456, \...\], // or summary

\"features\": \[\...\], // hashed or internal ID

\"S\": 0.42,

\"I\": 1.23,

\"layout\_id\": \"layout\_soft\_adapt\",

\"policy\_version\": 7,

\"timestamp\_ms\": 1734300000000

}

For each subsequent "reward" event:

{

\"user\_id\": \"\...\",

\"arm\": \"standard\" \| \"prime\",

\"event\_type\": \"task\_completed\",

\"timestamp\_ms\": \...

}

You can then join decisions with rewards (e.g., within 24h) to compute
per-user reward.

### **2.8. Analysis Plan**

1.  **Define analysis population\
    > **

    -   Users with at least one decision and at least one day of
        > observation afterward.

2.  **Aggregate to user-level\
    > **

    -   For primary metric, compute 0/1 per user: completed task vs not.

    -   This avoids multiple-counting heavy users.

3.  **Compute statistics\
    > **

    -   Let p\_A = completion rate in Arm A, p\_B in Arm B.

    -   Use two-proportion z-test or a logistic regression with arm as
        > covariate:

        -   logit(p) = β0 + β1 \* I(arm == prime) + controls

4.  **Decision rule\
    > **

    -   If p-value \< 0.05 and effect size is **practically
        > meaningful**, then:

        -   **If prime is better**: keep prime encoding.

        -   **If prime is worse**: kill the idea.

    -   If no significant difference and CIs are tight around 0, then:

        -   Treat "primes improve UX" as **falsified at that effect-size
            > scale**.

5.  **Secondary analysis\
    > **

    -   Check secondary metrics for patterns, but don't flip decision
        > based on them unless pre-specified.

    -   Inspect guardrails: if any harm \> threshold, stop experiment
        > early.

### **2.9. Operational Safeguards**

-   **Pre-registration**: Write down hypotheses, metrics, and stop rules
    > before launch. No p-hacking.

-   **Kill switch**: If guardrail metrics cross thresholds (e.g., +5%
    > error rate), auto-stop the experiment and revert to standard.

-   **Version pinning**: If you update the model during the experiment,
    > **freeze weights per arm** or restart the experiment. Otherwise,
    > you contaminate results.

### **2.10. Reality Check**

Brutal assessment:

-   If prime vs standard encoding shows **no measurable benefit** under
    > this design, the honest move is:

    -   Admit primes are *representational fluff* in this UX context.

    -   Keep the adaptive engine architecture.

    -   Drop the prime metaphysics from any performance claims.

**Adaptive UX Engine & Prime-Encoding A/B Experiment**
======================================================

**1. Purpose**
--------------

This document specifies:

1.  An **Adaptive UX Engine** that:

    -   Encodes user interactions as discrete IDs (either
        > **prime-based** or **standard**).

    -   Maintains per-user adaptive state.

    -   Chooses UI variants in real time via an **Adaptation API**.

    -   Logs decisions and rewards for offline training.

2.  An **A/B experiment** to directly test:

    -   **Arm A**: Standard integer encoding.

    -   **Arm B**: Prime-based encoding.

    -   Hypothesis: prime encoding provides **no measurable advantage**
        > unless proven otherwise.

Quantum/metaphysical language is explicitly excluded from this spec.
This is a production-oriented design.

**2. System Overview**
----------------------

### **2.1 Components**

-   **Frontend Client\
    > **

    -   Emits interaction events.

    -   Calls Adaptation API to retrieve layout\_id.

    -   Renders the chosen UI layout.

-   **Event Collector\
    > **

    -   Receives normalized InteractionEvents from frontend.

    -   Forwards them to:

        -   Encoder

        -   User State Store

        -   Logger

-   **Encoder\
    > **

    -   PrimeEncoder or StandardEncoder.

    -   Maps (event\_type, context) → integer ID.

-   **User State Store\
    > **

    -   Maintains UserState per user\_id.

    -   Updates based on encoded events and time decay.

-   **Adaptation Engine\
    > **

    -   Computes scalar state S(t) and non-linear influence I(t).

    -   Chooses a layout\_id given thresholds and rules.

-   **Policy Store\
    > **

    -   Holds model parameters (embeddings, weights, thresholds).

    -   Versioned (policy\_version).

-   **Logger\
    > **

    -   Logs:

        -   Raw events.

        -   Adaptation decisions.

        -   Reward events.

-   **Offline Trainer\
    > **

    -   Trains/upgrades model parameters from logged data.

    -   Outputs new ModelParams and policy\_version.

**3. Data Model**
-----------------

### **3.1 InteractionEvent**

Normalized incoming event.

InteractionEvent:

user\_id: string

session\_id: string

event\_type: string // e.g. \"click\", \"page\_view\", \"form\_submit\"

props: map\<string, any\> // e.g. { \"element\_id\": \"btn\_signup\",
\"page\": \"/home\" }

timestamp\_ms: int64

### **3.2 EncodedEvent**

Backend representation after encoding.

EncodedEvent:

user\_id: string

event\_id: int64 // prime or non-prime integer

weight: float // e.g. 1.0 or derived

timestamp\_ms: int64

### **3.3 UserState**

Per-user state.

UserState:

user\_id: string

features: vector\<float\> // dimension d

S: float // scalar state = dot(w, features)

last\_updated\_ms: int64

### **3.4 AdaptationDecision**

Decision logged at time of adaptation.

AdaptationDecision:

user\_id: string

layout\_id: string // \"control\_layout\" \| \"layout\_soft\_adapt\" \|
\"layout\_aggressive\_adapt\" \| \...

adaptation\_score: float // I(t)

policy\_version: int

timestamp\_ms: int64

### **3.5 ModelParams**

Model and adaptation hyperparameters.

ModelParams:

embedding\_matrix: \[num\_ids x d\] float

w: vector\<float\> // projection to scalar S

gamma: float // influence quadratic term

delta: float // influence exponential term

beta: float // influence exponential term

learning\_rate: float

tau\_1: float // threshold for layout selection

tau\_2: float

version: int

### **3.6 TrainingSample**

Logged example used for offline training.

TrainingSample:

features: vector\<float\> // snapshot at decision time

layout\_id: string

reward: float // e.g. 0/1

is\_prime\_arm: bool // true = prime encoding, false = standard

policy\_version: int

**4. Encoding Design**
----------------------

### **4.1 Event Key**

All encoders use a stable "event key" derived from the InteractionEvent.

key = event\_type + \"\|\" + page + \"\|\" + element\_id

-   page = props\[\"page\"\] or \"none\".

-   element\_id = props\[\"element\_id\"\] or \"none\".

### **4.2 StandardEncoder (Arm A: Control)**

-   Maintains map\<key, int64\> key\_to\_id.

-   Assigns consecutive integers starting at 1 to unseen keys.

### **4.3 PrimeEncoder (Arm B: Treatment)**

-   Maintains map\<key, int64\> key\_to\_prime.

-   Uses a pre-generated list of primes (e.g. first N primes) and
    > assigns them sequentially to new keys.

-   Otherwise identical semantics to StandardEncoder.

**Note:** No performance benefit is assumed a priori.

**5. State Update & Adaptation Logic**
--------------------------------------

### **5.1 State Update**

For each InteractionEvent:

1.  Encode event to event\_id.

2.  Fetch or initialize UserState for user\_id.

3.  Apply temporal decay to features.

4.  Add the embedding vector for event\_id to features.

5.  Compute scalar state S(t) = dot(w, features).

6.  Persist updated UserState.

### **5.2 Influence Function**

Use the non-linear influence function:

I(t)=γS(t)2+δeβS(t)I(t) = \\gamma S(t)\^2 + \\delta e\^{\\beta
S(t)}I(t)=γS(t)2+δeβS(t)

### **5.3 Layout Selection**

Given I(t):

-   If I(t) \< tau\_1 → layout\_id = \"control\_layout\".

-   Else if I(t) \< tau\_2 → layout\_id = \"layout\_soft\_adapt\".

-   Else → layout\_id = \"layout\_aggressive\_adapt\".

Exact layouts and thresholds are configurable; logic is fixed.

**6. Adaptation API**
---------------------

### **6.1 Endpoint**

**POST** /adapt

**Request:**

{

\"user\_id\": \"string\",

\"session\_id\": \"string\",

\"context\": {

\"page\": \"/home\",

\"device\": \"mobile\"

},

\"timestamp\_ms\": 1734300000000

}

**Response:**

{

\"layout\_id\": \"layout\_soft\_adapt\",

\"policy\_version\": 7,

\"adaptation\_score\": 1.23,

\"timestamp\_ms\": 1734300001000,

\"arm\": \"standard\" // or \"prime\"

}

### **6.2 Behavior**

-   Determines experiment arm for user\_id (prime vs standard).

-   Updates user state based on recent events (if needed).

-   Computes S(t) and I(t).

-   Chooses layout\_id.

-   Logs an AdaptationDecision.

**7. Logging Requirements**
---------------------------

For each event:

-   Raw InteractionEvent (post-normalization).

For each adaptation:

-   AdaptationDecision.

-   Current UserState.S and maybe a compressed representation of
    > features (e.g., hashed/projection and/or embedding ID indices).

-   arm (standard/prime).

For each reward:

-   RewardEvent with:

    -   user\_id

    -   event\_type (e.g. \"task\_completed\")

    -   timestamp\_ms

    -   arm

    -   Optional payload (task metadata).

All logs must be immutable and timestamped.

**8. Offline Training**
-----------------------

### **8.1 Reward Definition**

-   Binary reward per user for primary metric, e.g.:

    -   reward = 1 if user completes signup/checkout within 24h of first
        > adaptation decision in the experiment period.

    -   reward = 0 otherwise.

### **8.2 Training Flow**

1.  Join AdaptationDecision with subsequent RewardEvents by user\_id.

2.  Build TrainingSamples.

3.  Train a model with:

    -   Input: features at decision time.

    -   Target: reward.

    -   Link: p = sigmoid(I(t)).

4.  Optimize via gradient descent using standard ML framework.

5.  Emit new ModelParams + policy\_version.

**9. A/B Experiment Design: Prime vs Standard**
-----------------------------------------------

### **9.1 Hypotheses**

-   **H₀ (Null)**: Prime encoding produces no difference in primary
    > metric vs standard encoding.

-   **H₁ (Alt)**: Prime encoding changes the primary metric (two-sided)
    > OR improves it (one-sided, if you want to commit).

### **9.2 Arms**

-   **Arm A -- Standard\
    > **

    -   Encoder = StandardEncoder.

-   **Arm B -- Prime\
    > **

    -   Encoder = PrimeEncoder.

All other components identical.

### **9.3 Randomization**

-   Randomization unit: user\_id.

Assignment (sticky):\
\
bucket = hash(user\_id) % 100

if bucket \< 50 → Arm A (standard)

else → Arm B (prime)

-   

### **9.4 Metrics**

**Primary Metric** (choose one and commit):

-   Example: **Task Completion Rate\
    > **

    -   Fraction of users who complete target action
        > (signup/checkout/etc.) within 24h of first adaptation.

**Secondary Metrics:**

-   Engagement: interactions/session.

-   Time-to-task-completion.

-   Layout switch frequency.

**Guardrail Metrics:**

-   Error rates (JS errors, HTTP 4xx/5xx).

-   Bounce rate.

-   UX latency (Adaptation API p95/p99).

### **9.5 Sample Size & Duration**

-   Use standard two-proportion z-test sample size calculation.

-   Choose:

    -   Significance: α = 0.05 (two-sided).

    -   Power: 1 − β = 0.8 (β = 0.2).

    -   Target minimum effect size (e.g. 2--5% absolute change in
        > primary metric).

-   Duration:

    -   Run until:

        -   Required n users per arm reached **and\
            > **

        -   At least 2--4 weeks have passed to cover weekly cycles.

### **9.6 Analysis Plan**

-   Population: users with at least one adaptation decision and one day
    > of observation.

-   Aggregate metrics at user-level.

-   Compare Arm A vs Arm B:

    -   Two-proportion z-test, or

    -   Logistic regression with arm as a binary covariate.

-   Decision:

    -   If difference is significant and practically meaningful → adopt
        > winner.

    -   If no significant, small CI around zero → treat "prime encoding
        > helps" as falsified at that scale.

### **9.7 Safeguards**

-   Pre-register:

    -   Hypotheses

    -   Metrics

    -   Stopping criteria

-   Implement kill switches based on guardrails.

-   Avoid mid-experiment model changes; otherwise restart or freeze.

**Code Skeletons**
==================

Below are **non-trivial skeletons**, not toy snippets. They give
realistic structure but leave out implementation details like database,
auth, etc.

**1. Python Backend (FastAPI-style)**
-------------------------------------

### **1.1. models.py**

\# models.py

from dataclasses import dataclass, field

from typing import Dict, Any, List

import time

import math

Vector = List\[float\]

\@dataclass

class InteractionEvent:

user\_id: str

session\_id: str

event\_type: str

props: Dict\[str, Any\]

timestamp\_ms: int

\@dataclass

class UserState:

user\_id: str

features: Vector

S: float

last\_updated\_ms: int

\@dataclass

class AdaptationDecision:

user\_id: str

layout\_id: str

adaptation\_score: float

policy\_version: int

timestamp\_ms: int

arm: str \# \"standard\" or \"prime\"

\@dataclass

class ModelParams:

embedding\_dim: int

gamma: float

delta: float

beta: float

tau\_1: float

tau\_2: float

learning\_rate: float

version: int

\# embedding\_matrix is assumed to be managed by a separate component

### **1.2. encoder.py**

\# encoder.py

from typing import Dict

from .models import InteractionEvent

def make\_key(event: InteractionEvent) -\> str:

page = str(event.props.get(\"page\", \"none\"))

element\_id = str(event.props.get(\"element\_id\", \"none\"))

return f\"{event.event\_type}\|{page}\|{element\_id}\"

class Encoder:

\"\"\"Abstract base encoder.\"\"\"

def encode(self, event: InteractionEvent) -\> int:

\"\"\"Return an integer ID representing this event.\"\"\"

raise NotImplementedError

class StandardEncoder(Encoder):

\"\"\"Maps stable event keys to consecutive integer IDs.\"\"\"

def \_\_init\_\_(self) -\> None:

self.key\_to\_id: Dict\[str, int\] = {}

self.\_next\_id: int = 1

def encode(self, event: InteractionEvent) -\> int:

key = make\_key(event)

if key in self.key\_to\_id:

return self.key\_to\_id\[key\]

event\_id = self.\_next\_id

self.key\_to\_id\[key\] = event\_id

self.\_next\_id += 1

return event\_id

class PrimeEncoder(Encoder):

\"\"\"Maps stable event keys to distinct prime numbers.

For simplicity, we assume a pre-generated list of primes.

In production you would likely store primes in a DB/config.

\"\"\"

def \_\_init\_\_(self, prime\_pool: list\[int\]) -\> None:

if not prime\_pool:

raise ValueError(\"prime\_pool must be non-empty\")

self.key\_to\_prime: Dict\[str, int\] = {}

self.\_prime\_pool = prime\_pool\[:\] \# copy

def encode(self, event: InteractionEvent) -\> int:

key = make\_key(event)

if key in self.key\_to\_prime:

return self.key\_to\_prime\[key\]

if not self.\_prime\_pool:

raise RuntimeError(\"Prime pool exhausted\")

p = self.\_prime\_pool.pop(0)

self.key\_to\_prime\[key\] = p

return p

### **1.3. state\_store.py**

\# state\_store.py

from typing import Dict

import math

import time

from .models import UserState

from .models import InteractionEvent

from .encoder import Encoder

DEFAULT\_EMBEDDING\_DIM = 32

DEFAULT\_DECAY\_LAMBDA = 1e-4 \# tweak as needed

class UserStateStore:

\"\"\"Simple in-memory user state store.

Replace with Redis/DB-backed version in production.

\"\"\"

def \_\_init\_\_(self, embedding\_dim: int = DEFAULT\_EMBEDDING\_DIM)
-\> None:

self.\_store: Dict\[str, UserState\] = {}

self.\_embedding\_dim = embedding\_dim

def get\_or\_init(self, user\_id: str) -\> UserState:

if user\_id in self.\_store:

return self.\_store\[user\_id\]

state = UserState(

user\_id=user\_id,

features=\[0.0\] \* self.\_embedding\_dim,

S=0.0,

last\_updated\_ms=int(time.time() \* 1000),

)

self.\_store\[user\_id\] = state

return state

def put(self, state: UserState) -\> None:

self.\_store\[state.user\_id\] = state

class EmbeddingStore:

\"\"\"Placeholder for ID -\> embedding lookup.

In production this might be:

\- a matrix in RAM updated regularly

\- or a model server

\"\"\"

def \_\_init\_\_(self, dim: int = DEFAULT\_EMBEDDING\_DIM) -\> None:

self.dim = dim

self.\_embs: Dict\[int, list\[float\]\] = {}

def get\_or\_init(self, event\_id: int) -\> list\[float\]:

if event\_id in self.\_embs:

return self.\_embs\[event\_id\]

\# Simple random or zero init; real impl should be better

v = \[0.0\] \* self.dim

self.\_embs\[event\_id\] = v

return v

def decay\_features(

features: list\[float\],

last\_updated\_ms: int,

current\_ms: int,

lambda\_: float = DEFAULT\_DECAY\_LAMBDA,

) -\> list\[float\]:

dt = max(0, current\_ms - last\_updated\_ms)

decay\_factor = math.exp(-lambda\_ \* dt)

return \[decay\_factor \* x for x in features\]

### **1.4. adaptation\_engine.py**

\# adaptation\_engine.py

import time

import math

from typing import Tuple

from .models import InteractionEvent, UserState, AdaptationDecision,
ModelParams

from .encoder import Encoder

from .state\_store import UserStateStore, EmbeddingStore,
decay\_features

def dot(w: list\[float\], x: list\[float\]) -\> float:

return sum(w\_i \* x\_i for w\_i, x\_i in zip(w, x))

def compute\_influence(S: float, params: ModelParams) -\> float:

return params.gamma \* S \* S + params.delta \* math.exp(params.beta \*
S)

class AdaptationEngine:

def \_\_init\_\_(

self,

encoder\_standard: Encoder,

encoder\_prime: Encoder,

user\_state\_store: UserStateStore,

embedding\_store: EmbeddingStore,

model\_params: ModelParams,

) -\> None:

self.encoder\_standard = encoder\_standard

self.encoder\_prime = encoder\_prime

self.user\_state\_store = user\_state\_store

self.embedding\_store = embedding\_store

self.params = model\_params

def assign\_arm(self, user\_id: str) -\> str:

\"\"\"Deterministic user → arm assignment.\"\"\"

h = hash(user\_id) % 100

return \"standard\" if h \< 50 else \"prime\"

def \_select\_encoder(self, arm: str) -\> Encoder:

if arm == \"prime\":

return self.encoder\_prime

return self.encoder\_standard

def update\_state\_and\_decide(

self, event: InteractionEvent

) -\> AdaptationDecision:

arm = self.assign\_arm(event.user\_id)

encoder = self.\_select\_encoder(arm)

\# 1. Encode event

event\_id = encoder.encode(event)

\# 2. Get user state

state = self.user\_state\_store.get\_or\_init(event.user\_id)

\# 3. Decay features

now\_ms = event.timestamp\_ms or int(time.time() \* 1000)

state.features = decay\_features(

state.features,

state.last\_updated\_ms,

now\_ms,

)

\# 4. Lookup embedding and add

emb = self.embedding\_store.get\_or\_init(event\_id)

state.features = \[f + e for f, e in zip(state.features, emb)\]

\# 5. Compute scalar S

\# In production, w is stored/generated somewhere else

\# Here we just assume it\'s part of params and length = embedding\_dim

S = dot(self.params.w, state.features)

state.S = S

state.last\_updated\_ms = now\_ms

\# 6. Persist state

self.user\_state\_store.put(state)

\# 7. Compute influence and layout

I = compute\_influence(S, self.params)

layout\_id = self.choose\_layout(I)

decision = AdaptationDecision(

user\_id=event.user\_id,

layout\_id=layout\_id,

adaptation\_score=I,

policy\_version=self.params.version,

timestamp\_ms=now\_ms,

arm=arm,

)

return decision

def choose\_layout(self, influence\_score: float) -\> str:

if influence\_score \< self.params.tau\_1:

return \"control\_layout\"

if influence\_score \< self.params.tau\_2:

return \"layout\_soft\_adapt\"

return \"layout\_aggressive\_adapt\"

### **1.5. logger.py**

\# logger.py

from typing import Any, Dict

from .models import InteractionEvent, AdaptationDecision

class Logger:

\"\"\"Simple pluggable logger.

Replace print() with real log infra (Kafka, Kinesis, etc.)

\"\"\"

def log\_event(self, event: InteractionEvent) -\> None:

record: Dict\[str, Any\] = {

\"type\": \"interaction\",

\"user\_id\": event.user\_id,

\"session\_id\": event.session\_id,

\"event\_type\": event.event\_type,

\"props\": event.props,

\"timestamp\_ms\": event.timestamp\_ms,

}

print(record)

def log\_decision(self, decision: AdaptationDecision, state\_S: float)
-\> None:

record: Dict\[str, Any\] = {

\"type\": \"decision\",

\"user\_id\": decision.user\_id,

\"layout\_id\": decision.layout\_id,

\"adaptation\_score\": decision.adaptation\_score,

\"policy\_version\": decision.policy\_version,

\"arm\": decision.arm,

\"S\": state\_S,

\"timestamp\_ms\": decision.timestamp\_ms,

}

print(record)

def log\_reward(self, user\_id: str, reward: float, arm: str) -\> None:

record: Dict\[str, Any\] = {

\"type\": \"reward\",

\"user\_id\": user\_id,

\"reward\": reward,

\"arm\": arm,

}

print(record)

### **1.6. api.py (FastAPI Adaptation API)**

\# api.py

from fastapi import FastAPI

from pydantic import BaseModel

import time

from .models import InteractionEvent, ModelParams

from .encoder import StandardEncoder, PrimeEncoder

from .state\_store import UserStateStore, EmbeddingStore

from .adaptation\_engine import AdaptationEngine

from .logger import Logger

\# \-\-- Request/Response schemas \-\--

class AdaptRequest(BaseModel):

user\_id: str

session\_id: str

context: dict

timestamp\_ms: int \| None = None

class AdaptResponse(BaseModel):

layout\_id: str

policy\_version: int

adaptation\_score: float

timestamp\_ms: int

arm: str

\# \-\-- Instantiate global components (for skeleton only) \-\--

app = FastAPI()

standard\_encoder = StandardEncoder()

prime\_encoder = PrimeEncoder(prime\_pool=\[2, 3, 5, 7, 11, 13, 17, 19,
23, 29\])

user\_state\_store = UserStateStore()

embedding\_store = EmbeddingStore()

\# Dummy model params; in real system, load from persistent store

dummy\_params = ModelParams(

embedding\_dim=32,

gamma=0.1,

delta=0.01,

beta=0.001,

tau\_1=0.5,

tau\_2=1.5,

learning\_rate=0.01,

version=1,

)

\# Example weight vector --- all ones; replace with actual trained
weights

dummy\_params.w = \[1.0\] \* dummy\_params.embedding\_dim \# type:
ignore\[attr-defined\]

engine = AdaptationEngine(

encoder\_standard=standard\_encoder,

encoder\_prime=prime\_encoder,

user\_state\_store=user\_state\_store,

embedding\_store=embedding\_store,

model\_params=dummy\_params,

)

logger = Logger()

\# \-\-- Endpoint implementation \-\--

\@app.post(\"/adapt\", response\_model=AdaptResponse)

def adapt(req: AdaptRequest) -\> AdaptResponse:

now\_ms = req.timestamp\_ms or int(time.time() \* 1000)

\# Build synthetic InteractionEvent representing the page/context

event = InteractionEvent(

user\_id=req.user\_id,

session\_id=req.session\_id,

event\_type=\"page\_view\", \# or more specific

props=req.context,

timestamp\_ms=now\_ms,

)

logger.log\_event(event)

decision = engine.update\_state\_and\_decide(event)

logger.log\_decision(decision, state\_S=decision.adaptation\_score) \#
or state.S

return AdaptResponse(

layout\_id=decision.layout\_id,

policy\_version=decision.policy\_version,

adaptation\_score=decision.adaptation\_score,

timestamp\_ms=decision.timestamp\_ms,

arm=decision.arm,

)

**2. TypeScript (Frontend / Client-Side Skeletons)**
----------------------------------------------------

Assume a typical TypeScript setup (e.g., React frontend or Node client).

### **2.1. types.ts**

// types.ts

export interface InteractionEvent {

userId: string;

sessionId: string;

eventType: string;

props: Record\<string, any\>;

timestampMs: number;

}

export interface AdaptRequest {

user\_id: string;

session\_id: string;

context: Record\<string, any\>;

timestamp\_ms?: number;

}

export interface AdaptResponse {

layout\_id: string;

policy\_version: number;

adaptation\_score: number;

timestamp\_ms: number;

arm: \"standard\" \| \"prime\";

}

### **2.2. encoder.ts (Client-Side, Optional)**

Most encoding happens server-side, but if you want symmetry:

// encoder.ts

import { InteractionEvent } from \"./types\";

export interface Encoder {

encode(event: InteractionEvent): number;

}

function makeKey(event: InteractionEvent): string {

const page = String(event.props?.page ?? \"none\");

const elementId = String(event.props?.element\_id ??
event.props?.elementId ?? \"none\");

return \`\${event.eventType}\|\${page}\|\${elementId}\`;

}

export class StandardEncoder implements Encoder {

private keyToId: Map\<string, number\> = new Map();

private nextId = 1;

encode(event: InteractionEvent): number {

const key = makeKey(event);

const existing = this.keyToId.get(key);

if (existing !== undefined) return existing;

const id = this.nextId++;

this.keyToId.set(key, id);

return id;

}

}

export class PrimeEncoder implements Encoder {

private keyToPrime: Map\<string, number\> = new Map();

private primePool: number\[\];

constructor(primePool: number\[\]) {

if (!primePool.length) {

throw new Error(\"primePool must be non-empty\");

}

this.primePool = \[\...primePool\];

}

encode(event: InteractionEvent): number {

const key = makeKey(event);

const existing = this.keyToPrime.get(key);

if (existing !== undefined) return existing;

if (!this.primePool.length) {

throw new Error(\"Prime pool exhausted\");

}

const p = this.primePool.shift()!;

this.keyToPrime.set(key, p);

return p;

}

}

### **2.3. stateStore.ts (Client-Side Session State)**

This is **not** the authoritative user-state (that's backend), but it
can hold local session context.

// stateStore.ts

export interface ClientUserState {

userId: string;

lastLayoutId?: string;

lastAdaptationScore?: number;

lastPolicyVersion?: number;

lastUpdatedMs?: number;

}

export class ClientStateStore {

private store: Map\<string, ClientUserState\> = new Map();

getOrInit(userId: string): ClientUserState {

const existing = this.store.get(userId);

if (existing) return existing;

const state: ClientUserState = {

userId,

lastUpdatedMs: Date.now(),

};

this.store.set(userId, state);

return state;

}

update(userId: string, partial: Partial\<ClientUserState\>):
ClientUserState {

const state = this.getOrInit(userId);

const updated = { \...state, \...partial, lastUpdatedMs: Date.now() };

this.store.set(userId, updated);

return updated;

}

}

### **2.4. adaptationApiClient.ts**

// adaptationApiClient.ts

import { AdaptRequest, AdaptResponse } from \"./types\";

export class AdaptationApiClient {

constructor(private baseUrl: string) {}

async adapt(req: AdaptRequest): Promise\<AdaptResponse\> {

const res = await fetch(\`\${this.baseUrl}/adapt\`, {

method: \"POST\",

headers: {

\"Content-Type\": \"application/json\",

},

body: JSON.stringify(req),

});

if (!res.ok) {

throw new Error(\`Adaptation API error: \${res.status}\`);

}

const data = (await res.json()) as AdaptResponse;

return data;

}

}

### **2.5. logger.ts (Frontend → Backend Logging)**

// logger.ts

import { InteractionEvent } from \"./types\";

export class FrontendLogger {

constructor(private logEndpoint: string) {}

async logInteraction(event: InteractionEvent): Promise\<void\> {

try {

await fetch(this.logEndpoint, {

method: \"POST\",

headers: { \"Content-Type\": \"application/json\" },

body: JSON.stringify({

type: \"interaction\",

user\_id: event.userId,

session\_id: event.sessionId,

event\_type: event.eventType,

props: event.props,

timestamp\_ms: event.timestampMs,

}),

keepalive: true, // browsers may send even on unload

});

} catch {

// Swallow errors; logging must not break UX

}

}

async logReward(userId: string, reward: number, arm?: \"standard\" \|
\"prime\") {

try {

await fetch(this.logEndpoint, {

method: \"POST\",

headers: { \"Content-Type\": \"application/json\" },

body: JSON.stringify({

type: \"reward\",

user\_id: userId,

reward,

arm,

timestamp\_ms: Date.now(),

}),

keepalive: true,

});

} catch {

// ignore

}

}

}

Bottom line: here's a concrete repo layout you can literally paste into
a README, plus a minimal but real training script that (a) creates/loads
mock logs and (b) runs gradient descent to update ModelParams (including
w, gamma, delta, beta).

**1. Repo Structure**
---------------------

You can copy-paste this into your root README.md or Confluence.

adaptive-ux/

├── README.md

├── .gitignore

│

├── backend/

│ ├── requirements.txt

│ ├── app/

│ │ ├── \_\_init\_\_.py

│ │ ├── models.py

│ │ ├── encoder.py

│ │ ├── state\_store.py

│ │ ├── adaptation\_engine.py

│ │ ├── logger.py

│ │ └── api.py

│ │

│ └── training/

│ ├── \_\_init\_\_.py

│ ├── train\_hello\_world.py

│ └── mock\_logs.jsonl \# optional; can be generated by script

│

└── frontend/

├── package.json

└── src/

├── types.ts

├── encoder.ts

├── stateStore.ts

├── adaptationApiClient.ts

└── logger.ts

-   backend/app = API + core engine.

-   backend/training = offline training scripts.

-   frontend/src = TypeScript client.

You already have most of the backend code from previous responses; this
just anchors where things live.

**2. backend/app/models.py (update)**
-------------------------------------

Make sure ModelParams actually carries the weight vector w. Here is a
cleaned version:

\# backend/app/models.py

from dataclasses import dataclass

from typing import Dict, Any, List

Vector = List\[float\]

\@dataclass

class InteractionEvent:

user\_id: str

session\_id: str

event\_type: str

props: Dict\[str, Any\]

timestamp\_ms: int

\@dataclass

class UserState:

user\_id: str

features: Vector

S: float

last\_updated\_ms: int

\@dataclass

class AdaptationDecision:

user\_id: str

layout\_id: str

adaptation\_score: float

policy\_version: int

timestamp\_ms: int

arm: str \# \"standard\" \| \"prime\"

\@dataclass

class ModelParams:

embedding\_dim: int

w: Vector \# projection vector for S

gamma: float

delta: float

beta: float

tau\_1: float

tau\_2: float

learning\_rate: float

version: int

If you already have a slightly different version, just ensure w is
explicitly part of it and embedding\_dim == len(w).

**3. Hello-World Training Script**
----------------------------------

File: backend/training/train\_hello\_world.py

This script:

-   Loads mock logs from mock\_logs.jsonl **or** generates synthetic
    > data if the file doesn't exist.

-   Treats each record as a TrainingSample with:

    -   features: List\[float\]

    -   reward: 0 or 1

-   Runs a few epochs of SGD to update:

    -   w (feature weights),

    -   gamma, delta, beta (influence parameters).

-   Prints before/after parameters and a basic training loss.

### **3.1. Script Code**

\# backend/training/train\_hello\_world.py

import json

import math

import os

import random

from dataclasses import dataclass

from typing import List

from app.models import ModelParams \# assumes backend/ is on PYTHONPATH
or run via \`python -m\`

\@dataclass

class TrainingSample:

features: List\[float\]

reward: float

def sigmoid(x: float) -\> float:

\# numerically-stable enough for toy purposes

return 1.0 / (1.0 + math.exp(-x))

def dot(w: List\[float\], x: List\[float\]) -\> float:

return sum(w\_i \* x\_i for w\_i, x\_i in zip(w, x))

def generate\_mock\_logs(path: str, num\_samples: int = 1000, dim: int =
8) -\> None:

\"\"\"

Generate synthetic logs consistent with the model form:

S\_true = w\_true · x

I\_true = gamma\_true \* S\_true\^2 + delta\_true \* exp(beta\_true \*
S\_true)

reward \~ Bernoulli(sigmoid(I\_true))

and write them as JSONL.

\"\"\"

print(f\"\[INFO\] Generating synthetic mock logs at {path}\")

\# \"Ground-truth\" parameters for data generation (arbitrary but fixed)

w\_true = \[0.5\] \* dim

gamma\_true = 0.05

delta\_true = 0.01

beta\_true = 0.005

rng = random.Random(42)

with open(path, \"w\", encoding=\"utf-8\") as f:

for \_ in range(num\_samples):

\# sample features from N(0,1) approximated with uniform+CLT

\# or simpler: uniform\[-1,1\]

x = \[rng.uniform(-1.0, 1.0) for \_ in range(dim)\]

S\_true = dot(w\_true, x)

I\_true = gamma\_true \* (S\_true \*\* 2) + delta\_true \*
math.exp(beta\_true \* S\_true)

p = sigmoid(I\_true)

reward = 1.0 if rng.random() \< p else 0.0

record = {

\"features\": x,

\"reward\": reward,

}

f.write(json.dumps(record) + \"\\n\")

print(\"\[INFO\] Synthetic data generation complete\")

def load\_mock\_logs(path: str) -\> List\[TrainingSample\]:

\"\"\"

Load mock logs from JSONL.

Each line: {\"features\": \[\...\], \"reward\": 0 or 1}

\"\"\"

if not os.path.exists(path):

generate\_mock\_logs(path)

samples: List\[TrainingSample\] = \[\]

with open(path, \"r\", encoding=\"utf-8\") as f:

for line in f:

line = line.strip()

if not line:

continue

obj = json.loads(line)

features = obj\[\"features\"\]

reward = float(obj\[\"reward\"\])

samples.append(TrainingSample(features=features, reward=reward))

print(f\"\[INFO\] Loaded {len(samples)} samples from {path}\")

return samples

def init\_model\_params(dim: int) -\> ModelParams:

\"\"\"

Initialize ModelParams with small random weights

and reasonable defaults for gamma/delta/beta.

\"\"\"

rng = random.Random(0)

w = \[rng.uniform(-0.1, 0.1) for \_ in range(dim)\]

params = ModelParams(

embedding\_dim=dim,

w=w,

gamma=0.01, \# starting guesses

delta=0.005,

beta=0.001,

tau\_1=0.5, \# not used in training, but kept for completeness

tau\_2=1.5,

learning\_rate=0.01,

version=1,

)

return params

def train\_model(

samples: List\[TrainingSample\],

params: ModelParams,

num\_epochs: int = 5,

batch\_size: int = 32,

) -\> None:

\"\"\"

Simple SGD training loop.

Minimizes binary cross-entropy between reward and p = sigmoid(I(S)).

\"\"\"

lr = params.learning\_rate

dim = params.embedding\_dim

for epoch in range(num\_epochs):

random.shuffle(samples)

total\_loss = 0.0

n = 0

for i, sample in enumerate(samples):

x = sample.features

y = sample.reward

\# forward

S = dot(params.w, x)

I = params.gamma \* (S \*\* 2) + params.delta \* math.exp(params.beta \*
S)

p = sigmoid(I)

\# binary cross-entropy loss

\# L = -(y log p + (1 - y) log(1 - p))

\# avoid log(0)

eps = 1e-10

loss = -(y \* math.log(p + eps) + (1 - y) \* math.log(1 - p + eps))

total\_loss += loss

n += 1

\# backward

\# dL/dI = p - y

dL\_dI = p - y

\# dI/dS = 2\*gamma\*S + delta \* exp(beta\*S) \* beta

exp\_term = math.exp(params.beta \* S)

dI\_dS = 2.0 \* params.gamma \* S + params.delta \* exp\_term \*
params.beta

\# gradient for w\_j: dL/dw\_j = dL/dI \* dI/dS \* x\_j

factor = dL\_dI \* dI\_dS

grad\_w = \[factor \* x\_j for x\_j in x\]

\# gradients for gamma, delta, beta

\# dI/dgamma = S\^2

grad\_gamma = dL\_dI \* (S \*\* 2)

\# dI/ddelta = exp(beta\*S)

grad\_delta = dL\_dI \* exp\_term

\# dI/dbeta = delta \* exp(beta\*S) \* S

\# store old\_delta to keep gradient strictly consistent

old\_delta = params.delta

grad\_beta = dL\_dI \* old\_delta \* exp\_term \* S

\# SGD update

params.w = \[w\_j - lr \* g\_j for w\_j, g\_j in zip(params.w,
grad\_w)\]

params.gamma -= lr \* grad\_gamma

params.delta -= lr \* grad\_delta

params.beta -= lr \* grad\_beta

\# rudimentary batch \"sync\" -- here we do pure online; leaving
batch\_size hook

if (i + 1) % batch\_size == 0:

\# in a more complex setup you\'d average grads per batch; here it\'s
per-sample.

pass

avg\_loss = total\_loss / max(1, n)

print(

f\"\[EPOCH {epoch+1}/{num\_epochs}\] \"

f\"avg\_loss={avg\_loss:.4f} \"

f\"gamma={params.gamma:.4f} delta={params.delta:.4f}
beta={params.beta:.6f}\"

)

def main() -\> None:

logs\_path = os.path.join(os.path.dirname(\_\_file\_\_),
\"mock\_logs.jsonl\")

samples = load\_mock\_logs(logs\_path)

if not samples:

print(\"\[WARN\] No samples loaded; aborting\")

return

dim = len(samples\[0\].features)

params = init\_model\_params(dim)

print(\"\[INFO\] Initial params:\")

print(f\" w\[:5\] = {params.w\[:5\]}\")

print(f\" gamma={params.gamma}, delta={params.delta},
beta={params.beta}\")

train\_model(samples, params, num\_epochs=5, batch\_size=32)

print(\"\[INFO\] Trained params:\")

print(f\" w\[:5\] = {params.w\[:5\]}\")

print(f\" gamma={params.gamma}, delta={params.delta},
beta={params.beta}\")

if \_\_name\_\_ == \"\_\_main\_\_\":

main()

### **3.2. How this fits the rest of the system**

-   It uses the **same functional form** of I(t) that the online engine
    > uses:\
    > I(t)=γS2+δeβS,S=w⋅x.I(t) = \\gamma S\^2 + \\delta e\^{\\beta
    > S},\\quad S = w \\cdot x.I(t)=γS2+δeβS,S=w⋅x.

-   You can later:

    -   Serialize ModelParams (e.g., JSON or pickle).

    -   Load them into the running API/engine instead of the dummy
        > hardcoded params.

**1. Export trained params → JSON**
-----------------------------------

We'll extend backend/training/train\_hello\_world.py so that after
training, it writes model\_params.json next to mock\_logs.jsonl.

### **1.1. Add helpers to train\_hello\_world.py**

At the **top** of backend/training/train\_hello\_world.py, after
imports, add:

import pathlib

Then **below** init\_model\_params (or anywhere above train\_model),
add:

def model\_params\_to\_dict(params: ModelParams) -\> dict:

\"\"\"Convert ModelParams dataclass to a JSON-serializable dict.\"\"\"

return {

\"embedding\_dim\": params.embedding\_dim,

\"w\": params.w,

\"gamma\": params.gamma,

\"delta\": params.delta,

\"beta\": params.beta,

\"tau\_1\": params.tau\_1,

\"tau\_2\": params.tau\_2,

\"learning\_rate\": params.learning\_rate,

\"version\": params.version,

}

def save\_model\_params\_to\_json(params: ModelParams, path: str) -\>
None:

\"\"\"Save ModelParams to a JSON file.\"\"\"

d = model\_params\_to\_dict(params)

os.makedirs(os.path.dirname(path), exist\_ok=True)

with open(path, \"w\", encoding=\"utf-8\") as f:

json.dump(d, f, indent=2)

print(f\"\[INFO\] Saved ModelParams to {path}\")

### **1.2. Update main() in train\_hello\_world.py**

Replace the current main() with this version (or just patch the bottom):

def main() -\> None:

this\_dir = os.path.dirname(\_\_file\_\_)

logs\_path = os.path.join(this\_dir, \"mock\_logs.jsonl\")

params\_path = os.path.join(this\_dir, \"model\_params.json\")

samples = load\_mock\_logs(logs\_path)

if not samples:

print(\"\[WARN\] No samples loaded; aborting\")

return

dim = len(samples\[0\].features)

params = init\_model\_params(dim)

print(\"\[INFO\] Initial params:\")

print(f\" w\[:5\] = {params.w\[:5\]}\")

print(f\" gamma={params.gamma}, delta={params.delta},
beta={params.beta}\")

train\_model(samples, params, num\_epochs=5, batch\_size=32)

print(\"\[INFO\] Trained params:\")

print(f\" w\[:5\] = {params.w\[:5\]}\")

print(f\" gamma={params.gamma}, delta={params.delta},
beta={params.beta}\")

\# NEW: export to JSON

save\_model\_params\_to\_json(params, params\_path)

if \_\_name\_\_ == \"\_\_main\_\_\":

main()

Running:

cd backend

python -m training.train\_hello\_world

will now create/update:

backend/training/model\_params.json

containing your learned parameters.

**2. Loader for ModelParams in the API**
----------------------------------------

We'll add a small helper module to parse that JSON into a ModelParams
instance, then use it in api.py.

### **2.1. New file: backend/app/model\_io.py**

Create backend/app/model\_io.py:

\# backend/app/model\_io.py

import json

import os

from typing import Any, Dict

from .models import ModelParams

def load\_model\_params\_from\_json(path: str) -\> ModelParams:

\"\"\"Load ModelParams from a JSON file.

Raises FileNotFoundError if file doesn\'t exist.

Raises KeyError/ValueError if structure is wrong.

\"\"\"

with open(path, \"r\", encoding=\"utf-8\") as f:

data: Dict\[str, Any\] = json.load(f)

required\_keys = \[

\"embedding\_dim\",

\"w\",

\"gamma\",

\"delta\",

\"beta\",

\"tau\_1\",

\"tau\_2\",

\"learning\_rate\",

\"version\",

\]

missing = \[k for k in required\_keys if k not in data\]

if missing:

raise KeyError(f\"Missing required keys in model params JSON:
{missing}\")

embedding\_dim = int(data\[\"embedding\_dim\"\])

w = list(map(float, data\[\"w\"\]))

if len(w) != embedding\_dim:

raise ValueError(

f\"Weight vector length {len(w)} does not match embedding\_dim
{embedding\_dim}\"

)

params = ModelParams(

embedding\_dim=embedding\_dim,

w=w,

gamma=float(data\[\"gamma\"\]),

delta=float(data\[\"delta\"\]),

beta=float(data\[\"beta\"\]),

tau\_1=float(data\[\"tau\_1\"\]),

tau\_2=float(data\[\"tau\_2\"\]),

learning\_rate=float(data\[\"learning\_rate\"\]),

version=int(data\[\"version\"\]),

)

return params

**3. Wire the loader into api.py**
----------------------------------

Now modify backend/app/api.py so that it **tries** to load
model\_params.json, and only falls back to dummy parameters if that
fails.

### **3.1. Update imports at top of api.py**

At the top of backend/app/api.py, extend imports:

\# api.py

from fastapi import FastAPI

from pydantic import BaseModel

import time

import os

from .models import InteractionEvent, ModelParams

from .encoder import StandardEncoder, PrimeEncoder

from .state\_store import UserStateStore, EmbeddingStore

from .adaptation\_engine import AdaptationEngine

from .logger import Logger

from .model\_io import load\_model\_params\_from\_json

### **3.2. Replace dummy params block**

Find this block (or similar) in api.py:

\# Dummy model params; in real system, load from persistent store

dummy\_params = ModelParams(

embedding\_dim=32,

gamma=0.1,

delta=0.01,

beta=0.001,

tau\_1=0.5,

tau\_2=1.5,

learning\_rate=0.01,

version=1,

)

\# Example weight vector --- all ones; replace with actual trained
weights

dummy\_params.w = \[1.0\] \* dummy\_params.embedding\_dim \# type:
ignore\[attr-defined\]

engine = AdaptationEngine(

encoder\_standard=standard\_encoder,

encoder\_prime=prime\_encoder,

user\_state\_store=user\_state\_store,

embedding\_store=embedding\_store,

model\_params=dummy\_params,

)

Replace that **entire chunk** with this:

\# \-\-- Load trained model params from JSON (with fallback) \-\--

def load\_or\_default\_model\_params() -\> ModelParams:

\# Allow overriding via env var; default to training output

default\_path = os.path.join(

os.path.dirname(os.path.dirname(\_\_file\_\_)), \# backend/app -\>
backend/

\"training\",

\"model\_params.json\",

)

path = os.getenv(\"MODEL\_PARAMS\_PATH\", default\_path)

try:

params = load\_model\_params\_from\_json(path)

print(f\"\[INFO\] Loaded ModelParams from {path}\")

return params

except FileNotFoundError:

print(f\"\[WARN\] Model params JSON not found at {path}; using dummy
defaults\")

except Exception as e:

print(f\"\[WARN\] Failed to load ModelParams from {path}: {e}; using
dummy defaults\")

\# Fallback dummy parameters

embedding\_dim = 32

w = \[1.0\] \* embedding\_dim

return ModelParams(

embedding\_dim=embedding\_dim,

w=w,

gamma=0.1,

delta=0.01,

beta=0.001,

tau\_1=0.5,

tau\_2=1.5,

learning\_rate=0.01,

version=0,

)

model\_params = load\_or\_default\_model\_params()

engine = AdaptationEngine(

encoder\_standard=standard\_encoder,

encoder\_prime=prime\_encoder,

user\_state\_store=user\_state\_store,

embedding\_store=embedding\_store,

model\_params=model\_params,

)

### **3.3. Behavior**

-   In dev/prod:

Run training:\
\
cd backend

python -m training.train\_hello\_world

-   This creates backend/training/model\_params.json.

Start API (e.g.):\
\
uvicorn app.api:app \--reload

-   

```{=html}
<!-- -->
```
-   On startup, api.py will:

    -   Compute default path backend/training/model\_params.json.

    -   Load ModelParams from that file.

    -   Plug them into AdaptationEngine.

-   If the JSON is missing or malformed:

    -   You get a clear warning and the app falls back to hard-coded
        > dummy params.

    -   So it never silently crashes, but you can see from logs if
        > you're accidentally running on dummy weights.
