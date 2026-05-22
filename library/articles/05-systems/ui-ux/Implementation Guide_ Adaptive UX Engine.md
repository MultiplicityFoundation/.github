---
slug: implementation-guide-adaptive-ux-engine
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/ui-ux/Implementation Guide_ Adaptive UX Engine.md
  last_synced: '2026-03-20T17:17:17.657202Z'
---

**Implementation Guide: Adaptive UX Engine**
============================================

This document provides software engineers with a comprehensive,
step-by-step manual for building, deploying, and operating the Adaptive
UX Engine. The primary goal of this system is to create a real-time
service that personalizes UI variants based on a user\'s interaction
history, enabling dynamic and responsive user experiences.

**1.0 Introduction and System Goals**
-------------------------------------

### **1.1 Core Objectives**

The system is designed to meet several key objectives, each serving a
specific strategic purpose:

1.  **Consume user interaction events.** The system must ingest a stream
    > of front-end events, which serve as the raw input for
    > understanding user behavior.

2.  **Encode user interactions.** Raw events are mapped to stable,
    > numerical IDs, creating a structured feature representation
    > suitable for machine learning models.

3.  **Maintain a per-user state vector.** The engine tracks each user\'s
    > evolving context by maintaining a feature vector that summarizes
    > their recent interaction history.

4.  **Compute an \"adaptation score\" to choose UI variants.** Using the
    > user\'s state vector and a trained model, the system calculates a
    > score in real-time to determine the most appropriate UI variant to
    > display.

5.  **Log all data for offline analysis and training.** Every event,
    > state change, and decision is logged to an immutable store,
    > creating a rich dataset for offline model training and A/B test
    > analysis.

### **1.2 Explicit Non-Goals (Version 1)**

To maintain focus and ensure a feasible initial implementation, the
following are explicitly out of scope for the first version of the
system:

-   No **real quantum hardware** will be used in the production system.

-   No **tensor network research toys** will be implemented; the system
    > will use standard machine learning techniques for approximation.

-   No a priori claims that **prime encoding improves performance** will
    > be made; this is an experimental variable to be tested rigorously
    > via an A/B framework.

These constraints clarify the project\'s focus on building a practical,
production-oriented adaptive system. The following sections detail the
architecture that enables these goals.

**2.0 System Architecture Overview**
------------------------------------

Understanding the system\'s component-based architecture is critical for
successful implementation and long-term maintenance. This design
promotes modularity, testability, and a clear separation of concerns,
allowing teams to develop, deploy, and scale individual parts of the
system independently.

### **2.1 Component Breakdown**

The Adaptive UX Engine is composed of several distinct components, each
with a single, well-defined responsibility.

  Component             Core Responsibility
  --------------------- --------------------------------------------------------------------------------
  Event Collector       Accepts, normalizes, and timestamps all incoming front-end events.
  Interaction Encoder   Maps a normalized user event to a unique integer ID (prime or standard).
  User State Store      Maintains a feature vector and summary score for each individual user.
  Adaptation Engine     Computes the adaptation score and selects the appropriate UI variant.
  Policy Store          Holds and versions the model parameters that govern adaptation logic.
  Logger                Writes all inputs, decisions, and outcomes to an immutable data store.
  Offline Trainer       Uses logged data to train and update the model parameters in the Policy Store.

### **2.2 End-to-End Data Flow**

The lifecycle of a single user interaction and adaptation decision flows
through the system components in a clear, component-centric sequence:

1.  **Frontend Client:** A user action on the client (e.g., a page view)
    > triggers an API call to the backend service.

2.  **Event Collector:** The API endpoint receives the request,
    > normalizes it into an InteractionEvent, and immediately forwards
    > it to the **Logger** for immutable storage.

3.  **Adaptation Engine:** The event is passed to the engine, which
    > orchestrates the adaptation decision process.

4.  **Adaptation Engine → User State Store:** The engine retrieves the
    > user\'s current UserState from the **User State Store**.

5.  **Adaptation Engine → Interaction Encoder:** Based on the user\'s
    > assigned experiment arm, the engine selects the appropriate
    > encoder (PrimeEncoder or StandardEncoder) and encodes the event
    > into a numerical ID.

6.  **Adaptation Engine → Policy Store:** The engine retrieves the
    > current ModelParams to access the weights and thresholds needed
    > for its calculations.

7.  **Adaptation Engine → User State Store:** After computing the
    > updated user features and score, the engine persists the new
    > UserState back to the **User State Store**.

8.  **Adaptation Engine → Logger:** The final AdaptationDecision is sent
    > to the **Logger**.

9.  **Frontend Client:** The engine returns the decision in the API
    > response, which the **Frontend Client** uses to render the correct
    > UI variant.

10. **Offline Trainer → Logger & Policy Store:** Periodically, the
    > **Offline Trainer** reads historical data from the **Logger**\'s
    > data store, trains a new model, and deploys the updated
    > ModelParams to the **Policy Store**, closing the learning loop.

These distinct components work in concert to deliver a real-time
adaptive experience. The following section provides a detailed guide for
implementing the backend services that power this flow.

**3.0 Backend Implementation Deep Dive**
----------------------------------------

This section provides a detailed walkthrough for implementing the
server-side logic of the Adaptive UX Engine. The provided Python code
skeletons serve as a concrete foundation for building each component of
the backend service.

### **3.1 Foundational Data Models**

The entire system is built upon a set of core data structures. These
dataclasses define the contracts between different components and ensure
data consistency.

#### **InteractionEvent**

This class represents a normalized user interaction event received from
the frontend.

\@dataclass

class InteractionEvent:

user\_id: str

session\_id: str

event\_type: str

props: Dict\[str, Any\]

timestamp\_ms: int

  Field           Type              Description
  --------------- ----------------- --------------------------------------------------------------
  user\_id        str               A unique identifier for the user.
  session\_id     str               An identifier for the user\'s current session.
  event\_type     str               The type of interaction (e.g., \"click\", \"page\_view\").
  props           Dict\[str,Any\]   A key-value map of event metadata (e.g., element\_id, page).
  timestamp\_ms   int               The Unix timestamp of the event in milliseconds.

#### **UserState**

This class captures the evolving state of a user\'s interaction history.

\@dataclass

class UserState:

user\_id: str

features: Vector

S: float

last\_updated\_ms: int

  Field               Type     Description
  ------------------- -------- -----------------------------------------------------------------
  user\_id            str      A unique identifier for the user.
  features            Vector   The feature vector summarizing the user\'s interaction history.
  S                   float    A scalar score derived from the feature vector.
  last\_updated\_ms   int      The timestamp of the last update to this state.

#### **AdaptationDecision**

This class represents the output of the Adaptation Engine for a given
user at a specific point in time.

\@dataclass

class AdaptationDecision:

user\_id: str

layout\_id: str

adaptation\_score: float

policy\_version: int

timestamp\_ms: int

arm: str \# \"standard\" or \"prime\"

  Field               Type    Description
  ------------------- ------- -----------------------------------------------------------------------------
  user\_id            str     The user for whom the decision was made.
  layout\_id          str     The identifier of the UI variant to be rendered.
  adaptation\_score   float   The final score I(t) used to make the layout decision.
  policy\_version     int     The version of the model parameters used.
  timestamp\_ms       int     The timestamp of the decision.
  arm                 str     The A/B experiment arm (\"standard\" or \"prime\") the user is assigned to.

#### **ModelParams**

This class holds the versioned parameters that define the adaptation
model\'s behavior.

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

  Field            Type     Description
  ---------------- -------- ---------------------------------------------------------------------
  embedding\_dim   int      The dimensionality of the feature vectors.
  w                Vector   The weight vector used to project features into the scalar score S.
  gamma            float    The coefficient for the quadratic term in the influence function.
  delta            float    The coefficient for the exponential term in the influence function.
  beta             float    The exponent for the exponential term in the influence function.
  tau\_1           float    The lower threshold for layout selection.
  tau\_2           float    The upper threshold for layout selection.
  learning\_rate   float    The learning rate used during offline training.
  version          int      The version identifier for this set of parameters.

### **3.2 Interaction Encoding Module**

The encoding module is responsible for converting raw InteractionEvent
objects into numerical IDs. This is a critical step, as it creates the
features used by the model. The design is pluggable to allow for A/B
testing different encoding strategies.

The make\_key function is central to both strategies. It creates a
stable, canonical string representation of an event by combining its
type and key properties (e.g., page and element\_id). This ensures that
the same logical interaction always maps to the same key.

The two encoding strategies are compared below:

  Encoder           Core Logic
  ----------------- -----------------------------------------------------------------------------
  StandardEncoder   Assigns the next available consecutive integer (1, 2, 3, \...) to new keys.
  PrimeEncoder      Assigns the next available prime number (2, 3, 5, \...) to new keys.

The complete Python implementation for the encoding module is provided
below for reference.

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

### **3.3 User State Management**

The system maintains a stateful representation of each user\'s
interaction history. This is managed through an online, per-event update
process.

1.  The UserStateStore acts as the persistence layer for user state
    > vectors. In the provided skeleton, this is a simple in-memory
    > dictionary, but in production, it should be replaced with a
    > scalable key-value store like Redis.

2.  To account for the recency of interactions, the existing feature
    > vector is first decayed using an exponential function. The time
    > delta (dt) between the current event and the last update is
    > calculated, and a decay factor is computed: decay\_factor =
    > exp(-lambda \* dt) This formula ensures that older interactions
    > contribute less to the user\'s current state.

3.  The decayed feature vector is then updated by adding the embedding
    > vector emb associated with the current event: state.features =
    > decay\_factor \* state.features + emb

4.  Finally, a scalar summary score, S(t), is computed by taking the dot
    > product of the model\'s weight vector w and the newly updated
    > feature vector: state.S = dot(model.w, state.features)

The following code snippets from state\_store.py and
adaptation\_engine.py illustrate this logic.

\# from state\_store.py

def decay\_features(

features: list\[float\],

last\_updated\_ms: int,

current\_ms: int,

lambda\_: float = DEFAULT\_DECAY\_LAMBDA,

) -\> list\[float\]:

dt = max(0, current\_ms - last\_updated\_ms)

decay\_factor = math.exp(-lambda\_ \* dt)

return \[decay\_factor \* x for x in features\]

\# from adaptation\_engine.py

\# \... inside update\_state\_and\_decide method \...

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

S = dot(self.params.w, state.features)

state.S = S

### **3.4 The Adaptation Decision Engine**

The core business logic resides in the Adaptation Engine, which
transforms a user\'s state into a concrete UI decision.

1.  The engine starts by applying a non-linear influence function to the
    > scalar state S(t) to produce the final \"adaptation score,\" I(t).
    > This function allows the model to capture more complex
    > relationships between user state and the desired outcome.

2.  Next, a simple threshold-based logic is applied to the
    > influence\_score to select a discrete UI layout. The tau\_1 and
    > tau\_2 parameters, stored in ModelParams, define the decision
    > boundaries.

    -   If influence\_score \< tau\_1, the control\_layout is chosen.

    -   If influence\_score \< tau\_2, the layout\_soft\_adapt is
        > chosen.

    -   Otherwise, the layout\_aggressive\_adapt is chosen.

The complete code for adaptation\_engine.py, containing this central
logic, is provided below.

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

\"\"\"Deterministic user -\> arm assignment.\"\"\"

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

### **3.5 Exposing the Adaptation API**

The frontend application interacts with the backend through a single,
public-facing API endpoint.

1.  **Endpoint**: POST /adapt

2.  **Request Body**: The client must send a JSON payload with the
    > user\'s identifiers and current context.

3.  **Success Response**: The API responds with the chosen layout, model
    > version, and other metadata.

The following api.py file uses the FastAPI framework to expose this
endpoint, serving as the primary entry point for the entire online
system.

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

With these components, the backend provides a complete, stateful service
for real-time UI adaptation. The next section details how a frontend
application will integrate with this API.

**4.0 Frontend Integration Guide**
----------------------------------

This section details the client-side responsibilities for integrating
with the Adaptive UX Engine. The primary tasks for the frontend are
calling the /adapt API to determine which UI variant to render and
logging user interactions back to the system to fuel the learning loop.

### **4.1 Client-Side Data Types and API Client**

To ensure type safety and ease of use, we define clear TypeScript types
and a reusable API client class. For consistency with the backend Python
models, all properties use snake\_case.

1.  The following types define the contract for API requests, responses,
    > and logged events on the client side.

2.  The AdaptationApiClient class provides a clean, reusable interface
    > for making requests to the backend. It handles the details of the
    > HTTP POST request and JSON serialization.

### **4.2 Making an Adaptation Request**

On a page load or significant navigation event, the frontend should
follow these steps to get a layout decision from the backend:

1.  Instantiate the AdaptationApiClient with the base URL of the backend
    > service.

2.  Construct the AdaptRequest object, populating it with the current
    > user\_id, session\_id, and page context (e.g., page path, device
    > type).

3.  Call the client.adapt(request) method to fetch the adaptation
    > decision.

4.  Use the layout\_id from the AdaptResponse to conditionally render
    > the correct UI component (e.g., show ControlLayout if layout\_id
    > is \"control\_layout\", or SoftAdaptLayout if it is
    > \"layout\_soft\_adapt\").

### **4.3 Logging Interactions and Rewards**

The frontend plays a crucial role in logging the data needed for the
offline training loop.

1.  The FrontendLogger class provides a simple interface for sending
    > interaction and reward events to a logging endpoint.

2.  The logger.logInteraction(event) method should be called for
    > significant user actions like clicks, scrolls, or form
    > submissions. This provides the raw behavioral data for the system.

3.  The logger.logReward(\...) method should be called when a user
    > completes a primary business goal, such as a successful checkout,
    > signup, or task completion. This \"reward\" signal is critical for
    > training the model to understand which behaviors lead to positive
    > outcomes.

Proper frontend integration is key to collecting the high-quality data
that directly impacts the performance of the offline training pipeline,
which is discussed next.

**5.0 Offline Training and Model Deployment**
---------------------------------------------

The offline training pipeline is the \"learning\" component of the
system. It uses the logged history of user behavior, adaptation
decisions, and reward signals to generate and update the ModelParams
that drive the online adaptation engine.

### **5.1 Training Objective and Data Schema**

1.  The objective of the training process is to learn a set of model
    > parameters (w, gamma, delta, beta) that produce an adaptation
    > score I(t) which accurately predicts a future reward signal.

2.  The model assumes a logistic relationship between the score and the
    > probability of a reward. This is modeled with a sigmoid link
    > function, p(reward) = sigmoid(I(t)), and the model is trained by
    > minimizing a binary cross-entropy loss function.

3.  The training process requires data to be structured in the following
    > format. Each TrainingSample represents a single decision point and
    > its eventual outcome.

### **5.2 Running the Training Script**

A \"Hello World\" training script is provided to demonstrate the core
training loop on mock data.

1.  The script is located in the backend/training/ directory of the
    > recommended repository structure.

2.  The full Python code for backend/training/train\_hello\_world.py is
    > below.

3.  The script\'s primary functions are:

    -   generate\_mock\_logs: Creates synthetic training data if none
        > exists.

    -   load\_mock\_logs: Loads the training data from a JSONL file.

    -   init\_model\_params: Creates an initial ModelParams object with
        > random weights.

    -   train\_model: Implements a simple Stochastic Gradient Descent
        > (SGD) loop to update the model parameters by minimizing binary
        > cross-entropy loss.

4.  To execute the training script, navigate to the backend directory
    > and run it as a module:

### **5.3 Model Artifacts and Deployment**

1.  After a successful run, the training script outputs a file named
    > model\_params.json in the backend/training/ directory. This JSON
    > file is the model artifact, containing all the learned parameters
    > needed by the online system.

2.  The backend/app/model\_io.py module provides a dedicated function,
    > load\_model\_params\_from\_json, for parsing this artifact into a
    > ModelParams dataclass instance.

3.  The api.py module is designed for operational resilience. The
    > load\_or\_default\_model\_params function attempts to load the
    > trained parameters from the JSON file on API startup. If the file
    > is missing or malformed, it logs a warning and gracefully falls
    > back to a set of default dummy parameters, ensuring the API can
    > always start.

This closed loop---online logging feeding offline training to update
online models---is the core mechanism of the adaptive system. The final
section describes how this entire system is deployed within an A/B test
framework to validate its core hypotheses.

**6.0 Implementing the A/B Experiment**
---------------------------------------

The entire Adaptive UX Engine is designed to facilitate a specific A/B
experiment: testing the impact of PrimeEncoder vs. StandardEncoder. This
section provides the implementation details for setting up, running, and
logging this experiment correctly to produce a valid, data-driven
conclusion.

### **6.1 Experiment Design and Hypotheses**

The experiment is designed to empirically test whether prime-based
encoding offers any meaningful performance gains over standard integer
IDs.

1.  **Hypotheses:**

    -   **Null Hypothesis (H₀):** Prime encoding and standard encoding
        > produce no difference in key UX metrics.

    -   **Alternative Hypothesis (H₁):** Prime encoding produces a
        > different outcome (either better or worse) on key UX metrics
        > compared to standard encoding.

2.  **Experiment Arms:** The test consists of two arms, with the
    > encoding strategy being the only variable.

  Arm             Encoder Class     Description
  --------------- ----------------- -----------------------------------------
  A (Control)     StandardEncoder   Uses consecutive non-prime integer IDs.
  B (Treatment)   PrimeEncoder      Uses unique prime numbers as IDs.

### **6.2 User-to-Arm Assignment**

To ensure a fair comparison, users must be randomly but consistently
assigned to an experiment arm.

1.  The randomization unit is the user\_id, and the assignment must be
    > sticky, meaning a user will remain in their assigned arm for the
    > duration of the experiment.

2.  A deterministic assignment is achieved by taking a stable hash of
    > the user\_id. This ensures that the same user is always assigned
    > to the same arm, which is critical for accurate analysis.

### **6.3 Required Logging for Analysis**

To analyze the experiment\'s results, it is critical that all logged
data is tagged with the user\'s assigned arm. Every decision and reward
event *must* include the arm field. The log\_decision and log\_reward
methods in logger.py are designed to capture this information, as shown
in their output record structure. This allows analysts to segment the
data and compare the performance of Arm A directly against Arm B.

By following the steps outlined in this guide, engineers can
successfully build, deploy, and operate the complete Adaptive UX Engine
and its accompanying A/B test framework to drive data-informed
improvements to the user experience.
