---
slug: phase-2
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/Phase 2.md
  last_synced: '2026-03-20T17:17:15.120746Z'
---

Here's a concrete Phase 2 expansion that fits the repo you already have:
**calculator stays as-is (FastAPI APIv2), Python core stays as-is, TS
adds two adapters + a tiny Python "engine surface."**

**0) One shared TS contract: EngineAdapter + a thin engine protocol**
---------------------------------------------------------------------

### **TS interface (what orchestrator/runner talks to)**

import type { RunManifest, ArtifactIndex } from \"\@qcalc/schemas\";

export type Capabilities = {

engineId: string; // \"qari-python\"

engineVersion: string; // git/tag or semver

protocolVersion: string; // e.g. \"0.1.0\"

supportedManifestVersions: string\[\];

calculatorApiVersion: string; // \"2.3.0\"

features: {

initStepFinalize: boolean;

streamingMetrics: boolean;

checkpoints: boolean;

};

};

export interface EngineAdapter {

capabilities(): Promise\<Capabilities\>;

run(manifest: RunManifest, runDir: string): Promise\<ArtifactIndex\>; //
full run convenience

// optional lifecycle:

init?(manifest: RunManifest, runDir: string): Promise\<{ stateRef:
string }\>;

step?(stateRef: string, n?: number): Promise\<{ stateRef: string;
events: any\[\] }\>;

finalize?(stateRef: string): Promise\<ArtifactIndex\>;

}

You'll implement:

-   PythonSubprocessAdapter → just calls a Python entrypoint that writes
    > metrics.jsonl + ArtifactIndex.json.

-   PythonHttpAdapter → calls /capabilities, /init, /step, /finalize.

**1) Critical small Python fix: make the core's CalculatorClient speak APIv2**
------------------------------------------------------------------------------

Right now packages/core/qari/calculator\_client.py posts payloads
without api\_version, but APIv2 expects versioned requests.

**Patch** (minimal, safe, doesn't touch the calculator service):

\# packages/core/qari/calculator\_client.py

API\_VERSION = \"2.3.0\"

def \_post(self, path: str, payload: Dict\[str, Any\]) -\> Dict\[str,
Any\]:

self.\_ensure\_enabled()

url = f\"{self.endpoint.rstrip(\'/\')}{path}\"

if \"api\_version\" not in payload:

payload = dict(payload)

payload\[\"api\_version\"\] = API\_VERSION

resp = self.session.post(url, json=payload, timeout=self.timeout)

\...

This single change makes both adapters viable immediately when the
calculator is running as api\_v2.

**2) python-subprocess adapter (fastest end-to-end)**
-----------------------------------------------------

### **Contract**

TS spawns something like:

python -m scripts.qari\_engine\_run \--manifest
\<runDir\>/RunManifest.json \--out \<runDir\>

**Python engine responsibilities**

-   Read manifest (already validated by TS; Python can still
    > sanity-check versions)

-   Run Q-ARI loop (using packages/core/qari/\*)

-   Call calculator APIv2 when enabled

-   Append metrics.jsonl (MetricEvent per step)

-   Write ArtifactIndex.json at end (even on failure if possible)

-   Optionally write checkpoints / arrays

### **Recommended run directory layout**

runDir/

RunManifest.json \# resolved snapshot

metrics.jsonl \# append-only

ArtifactIndex.json

checkpoints/

step\_00025.npz

arrays/

Xi.npy Lam.npy G.npy

logs/

engine.stderr.log

### **Minimal Python entrypoint (new): scripts/qari\_engine\_run.py**

Put it under scripts/ because that's already included and importable
in-repo.

Skeleton (shows the shape you want; fill the "init/sequences" part to
your spec):

\#!/usr/bin/env python3

from \_\_future\_\_ import annotations

import argparse, json, os, sys, time, traceback

from pathlib import Path

import numpy as np

\# Make sure PYTHONPATH includes repo root + packages/core when invoked
by TS.

from qari.core import QARICore, CoreParams

from qari.ethics import EthicsProjector

from qari.operators import apply\_T\_typed

from qari.calculator\_client import CalculatorClient

def write\_json(path: Path, obj) -\> None:

path.write\_text(json.dumps(obj, indent=2) + \"\\n\",
encoding=\"utf-8\")

def append\_jsonl(path: Path, obj) -\> None:

with path.open(\"a\", encoding=\"utf-8\") as f:

f.write(json.dumps(obj) + \"\\n\")

f.flush()

def sha256\_file(path: Path) -\> str:

import hashlib

h = hashlib.sha256()

with path.open(\"rb\") as f:

for chunk in iter(lambda: f.read(1024 \* 1024), b\"\"):

h.update(chunk)

return \"sha256:\" + h.hexdigest()

def main() -\> int:

ap = argparse.ArgumentParser()

ap.add\_argument(\"\--manifest\", required=True)

ap.add\_argument(\"\--out\", required=True)

args = ap.parse\_args()

out = Path(args.out)

out.mkdir(parents=True, exist\_ok=True)

metrics\_path = out / \"metrics.jsonl\"

index\_path = out / \"ArtifactIndex.json\"

started\_at = time.strftime(\"%Y-%m-%dT%H:%M:%SZ\", time.gmtime())

\# load manifest

manifest =
json.loads(Path(args.manifest).read\_text(encoding=\"utf-8\"))

\# quick mapping (manifest is canonical)

budgets = manifest.get(\"budgets\", {}) or {}

core = manifest.get(\"core\", {}) or {}

schedule = manifest.get(\"schedule\", {}) or {}

petc = manifest.get(\"petc\", {}) or {}

calc = manifest.get(\"calculator\", {}) or {}

steps = int(schedule.get(\"steps\", 200))

tol = core.get(\"tol\", None)

params = CoreParams(

epsilon=float(budgets.get(\"epsilon\", 0.05)),

op\_norm\_T=float(budgets.get(\"opNormT\", 1.0)),

max\_steps=steps,

tol=float(tol) if tol is not None else 1.0e-6,

petc\_fail\_raises=bool(petc.get(\"failOnViolation\", True)),

)

calc\_enabled = bool(calc.get(\"enabled\", True))

calc\_endpoint = calc.get(\"endpoint\", \"\")

calculator\_client = CalculatorClient(endpoint=str(calc\_endpoint),
enabled=calc\_enabled) if calc\_enabled else CalculatorClient.disabled()

\# PRIME AXES: enforceMultiplicity =\> provide primes; else None
disables PETC signature checks naturally

prime\_set = manifest.get(\"model\", {}).get(\"primeSet\")

prime\_axes = None

if bool(petc.get(\"enforceMultiplicity\", True)) and
isinstance(prime\_set, list) and len(prime\_set) \> 0:

prime\_axes = \[int(p) for p in prime\_set\]

\# TODO: define init and sequences contract (examples below)

\# For now, assume extensions.engine provides dim and generator knobs:

eng = (manifest.get(\"extensions\", {}) or {}).get(\"engine\", {}) or {}

dim = int(eng.get(\"dim\", 3))

seed = int((manifest.get(\"seed\", {}) or {}).get(\"global\", 0))

rng = np.random.default\_rng(seed)

X = rng.standard\_normal((dim, 1))

\# Generate Xi/Lam/G sequences (minimal default)

Xi\_seq = \[np.eye(dim) for \_ in range(steps)\]

Lam\_seq = \[np.zeros((dim, dim)) for \_ in range(steps)\]

G\_seq = \[np.zeros((dim, 1)) for \_ in range(steps)\]

\# Ethics projector and T operator: placeholder --- wire to your real
ones

P = EthicsProjector(eta\_budget=float(budgets.get(\"etaBudget\", 0.0)))

def T(x: np.ndarray) -\> np.ndarray:

return x \# TODO replace with your operator (Langlands Prism / typed T /
etc.)

core\_engine = QARICore(P=P, T=T, params=params,
calculator\_client=calculator\_client)

status = \"running\"

err\_msg = None

try:

for t in range(steps):

X\_next = core\_engine.step(X, Xi\_seq\[t\], Lam\_seq\[t\], G\_seq\[t\],
t=t, prime\_axes=prime\_axes)

drift = float(np.linalg.norm(X\_next - X))

X = X\_next

evt = {

\"metricVersion\": \"1.0.0\",

\"step\": t,

\"timestamp\": time.strftime(\"%Y-%m-%dT%H:%M:%SZ\", time.gmtime()),

\"drift\": drift,

}

append\_jsonl(metrics\_path, evt)

except Exception as e:

status = \"failed\"

err\_msg = f\"{type(e).\_\_name\_\_}: {e}\"

(out / \"logs\").mkdir(exist\_ok=True)

(out / \"logs\" /
\"engine.stderr.log\").write\_text(traceback.format\_exc(),
encoding=\"utf-8\")

finished\_at = time.strftime(\"%Y-%m-%dT%H:%M:%SZ\", time.gmtime())

\# Always write ArtifactIndex (best effort)

files = \[\]

if metrics\_path.exists():

files.append({

\"path\": \"metrics.jsonl\",

\"role\": \"metrics\",

\"contentType\": \"application/x-ndjson\",

\"hash\": sha256\_file(metrics\_path)

})

files.append({

\"path\": Path(args.manifest).name,

\"role\": \"manifest\",

\"contentType\": \"application/json\",

\"hash\": sha256\_file(Path(args.manifest))

})

artifact\_index = {

\"artifactIndexVersion\": \"1.0.0\",

\"runId\": manifest.get(\"runId\", \"\"),

\"status\": status,

\"startedAt\": started\_at,

\"finishedAt\": finished\_at,

\"engine\": {\"kind\": \"python-subprocess\", \"protocolVersion\":
manifest.get(\"engine\", {}).get(\"protocolVersion\", \"\")},

\"files\": files,

\"metrics\": {\"jsonl\": \"metrics.jsonl\" if metrics\_path.exists()
else None},

\"extensions\": {\"error\": err\_msg} if err\_msg else {},

}

write\_json(index\_path, artifact\_index)

return 0 if status == \"succeeded\" else 1

if \_\_name\_\_ == \"\_\_main\_\_\":

raise SystemExit(main())

### **What TS subprocess adapter does**

-   Writes the resolved RunManifest.json into runDir

-   Spawns python

-   Tails metrics.jsonl if you want live UI

-   Reads ArtifactIndex.json when done and validates it with Zod

**3) python-http adapter (scale + remote execution)**
-----------------------------------------------------

You add a **separate** Q-ARI Engine API service; calculator remains
separate and is called internally.

### **Endpoints**

-   GET /capabilities

-   POST /init → returns { stateRef, runId }

-   POST /step → returns { stateRef, events: MetricEvent\[\],
    > checkpoints?: \... }

-   POST /finalize → returns ArtifactIndex

### **State model (simple, works well)**

Maintain an in-memory store keyed by stateRef:

STATE\[stateRef\] = {

\"manifest\": manifest,

\"t\": 0,

\"X\": np.ndarray,

\"Xi\": list\[np.ndarray\], \"Lam\": list\[np.ndarray\], \"G\":
list\[np.ndarray\],

\"out\": runDirPath

}

Later you can swap state backend to Redis, sqlite, etc.

### **Minimal FastAPI engine service (new): scripts/qari\_engine\_api.py**

from \_\_future\_\_ import annotations

import uuid, time

from pathlib import Path

from typing import Any, Dict, Optional

import numpy as np

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from qari.core import QARICore, CoreParams

from qari.ethics import EthicsProjector

from qari.calculator\_client import CalculatorClient

app = FastAPI(title=\"Q-ARI Engine API\")

STATE: Dict\[str, Dict\[str, Any\]\] = {}

class InitReq(BaseModel):

manifest: Dict\[str, Any\]

runDir: str

class InitResp(BaseModel):

stateRef: str

runId: Optional\[str\] = None

class StepReq(BaseModel):

stateRef: str

n: int = 1

class StepResp(BaseModel):

stateRef: str

events: list\[dict\]

class FinalizeReq(BaseModel):

stateRef: str

\@app.get(\"/capabilities\")

def capabilities():

return {

\"engineId\": \"qari-python\",

\"engineVersion\": \"0.1.0\",

\"protocolVersion\": \"0.1.0\",

\"supportedManifestVersions\": \[\"1.0.0\"\],

\"calculatorApiVersion\": \"2.3.0\",

\"features\": {\"initStepFinalize\": True, \"streamingMetrics\": False,
\"checkpoints\": True},

}

\@app.post(\"/init\", response\_model=InitResp)

def init(req: InitReq):

m = req.manifest

run\_dir = Path(req.runDir)

run\_dir.mkdir(parents=True, exist\_ok=True)

budgets = m.get(\"budgets\", {}) or {}

core = m.get(\"core\", {}) or {}

schedule = m.get(\"schedule\", {}) or {}

petc = m.get(\"petc\", {}) or {}

calc = m.get(\"calculator\", {}) or {}

steps = int(schedule.get(\"steps\", 200))

tol = core.get(\"tol\", 1.0e-6)

params = CoreParams(

epsilon=float(budgets.get(\"epsilon\", 0.05)),

op\_norm\_T=float(budgets.get(\"opNormT\", 1.0)),

max\_steps=steps,

tol=float(tol),

petc\_fail\_raises=bool(petc.get(\"failOnViolation\", True)),

)

calc\_enabled = bool(calc.get(\"enabled\", True))

calc\_endpoint = calc.get(\"endpoint\", \"\")

calculator\_client = CalculatorClient(endpoint=str(calc\_endpoint),
enabled=calc\_enabled) if calc\_enabled else CalculatorClient.disabled()

P = EthicsProjector(eta\_budget=float(budgets.get(\"etaBudget\", 0.0)))

def T(x: np.ndarray) -\> np.ndarray:

return x \# TODO wire real operator

engine = QARICore(P=P, T=T, params=params,
calculator\_client=calculator\_client)

\# TODO init state + sequences contract; start with deterministic
defaults:

dim = int(((m.get(\"extensions\", {}) or {}).get(\"engine\", {}) or
{}).get(\"dim\", 3))

seed = int((m.get(\"seed\", {}) or {}).get(\"global\", 0))

rng = np.random.default\_rng(seed)

X = rng.standard\_normal((dim, 1))

Xi = \[np.eye(dim) for \_ in range(steps)\]

Lam = \[np.zeros((dim, dim)) for \_ in range(steps)\]

G = \[np.zeros((dim, 1)) for \_ in range(steps)\]

state\_ref = str(uuid.uuid4())

STATE\[state\_ref\] = {\"engine\": engine, \"manifest\": m, \"t\": 0,
\"X\": X, \"Xi\": Xi, \"Lam\": Lam, \"G\": G, \"runDir\": run\_dir}

return InitResp(stateRef=state\_ref, runId=m.get(\"runId\"))

\@app.post(\"/step\", response\_model=StepResp)

def step(req: StepReq):

st = STATE.get(req.stateRef)

if st is None:

raise HTTPException(404, \"unknown stateRef\")

engine: QARICore = st\[\"engine\"\]

m = st\[\"manifest\"\]

petc = m.get(\"petc\", {}) or {}

prime\_set = (m.get(\"model\", {}) or {}).get(\"primeSet\")

prime\_axes = None

if bool(petc.get(\"enforceMultiplicity\", True)) and
isinstance(prime\_set, list) and len(prime\_set) \> 0:

prime\_axes = \[int(p) for p in prime\_set\]

events = \[\]

for \_ in range(max(1, int(req.n))):

t = st\[\"t\"\]

if t \>= len(st\[\"Xi\"\]):

break

X\_prev = st\[\"X\"\]

X\_next = engine.step(X\_prev, st\[\"Xi\"\]\[t\], st\[\"Lam\"\]\[t\],
st\[\"G\"\]\[t\], t=t, prime\_axes=prime\_axes)

drift = float(np.linalg.norm(X\_next - X\_prev))

st\[\"X\"\] = X\_next

st\[\"t\"\] = t + 1

events.append({

\"metricVersion\": \"1.0.0\",

\"step\": t,

\"timestamp\": time.strftime(\"%Y-%m-%dT%H:%M:%SZ\", time.gmtime()),

\"drift\": drift,

})

return StepResp(stateRef=req.stateRef, events=events)

\@app.post(\"/finalize\")

def finalize(req: FinalizeReq):

st = STATE.pop(req.stateRef, None)

if st is None:

raise HTTPException(404, \"unknown stateRef\")

\# TODO: write ArtifactIndex.json, metrics.jsonl if you buffered; return
ArtifactIndex object

return {\"ok\": True}

TS HTTP adapter can either:

-   stream steps (call /step repeatedly, append events to
    > metrics.jsonl), then /finalize, or

-   let Python write metrics and return artifact index (your choice).

**4) TS implementation sketches**
---------------------------------

### **Subprocess adapter skeleton**

import { spawn } from \"node:child\_process\";

import { readFile } from \"node:fs/promises\";

import path from \"node:path\";

import type { RunManifest, ArtifactIndex } from \"\@qcalc/schemas\";

import { ArtifactIndex as ArtifactIndexSchema } from
\"\@qcalc/schemas/artifactIndex\"; // wherever you export

export class PythonSubprocessAdapter {

async capabilities() {

return {

engineId: \"qari-python\",

engineVersion: \"dev\",

protocolVersion: \"0.1.0\",

supportedManifestVersions: \[\"1.0.0\"\],

calculatorApiVersion: \"2.3.0\",

features: { initStepFinalize: false, streamingMetrics: true,
checkpoints: true }

};

}

async run(manifest: RunManifest, runDir: string):
Promise\<ArtifactIndex\> {

const manifestPath = path.join(runDir, \"RunManifest.json\");

// assume runner already wrote it; or write here

await new Promise\<void\>((resolve, reject) =\> {

const env = {

\...process.env,

PYTHONPATH: \[

process.cwd(), // repo root

path.join(process.cwd(), \"packages/core\"),

\].join(path.delimiter),

};

const p = spawn(\"python\", \[\"-m\", \"scripts.qari\_engine\_run\",
\"\--manifest\", manifestPath, \"\--out\", runDir\], {

stdio: \[\"ignore\", \"inherit\", \"pipe\"\],

env

});

p.stderr?.on(\"data\", (d) =\> process.stderr.write(d));

p.on(\"error\", reject);

p.on(\"close\", (code) =\> (code === 0 ? resolve() : resolve())); //
still read ArtifactIndex

});

const idx = JSON.parse(await readFile(path.join(runDir,
\"ArtifactIndex.json\"), \"utf8\"));

return ArtifactIndexSchema.parse(idx);

}

}

### **HTTP adapter skeleton**

export class PythonHttpAdapter {

constructor(private endpoint: string) {}

async capabilities() {

const r = await fetch(\`\${this.endpoint}/capabilities\`);

if (!r.ok) throw new Error(\`capabilities failed: \${r.status}\`);

return r.json();

}

async init(manifest: any, runDir: string) {

const r = await fetch(\`\${this.endpoint}/init\`, {

method: \"POST\",

headers: { \"content-type\": \"application/json\" },

body: JSON.stringify({ manifest, runDir })

});

if (!r.ok) throw new Error(\`init failed: \${r.status}\`);

return r.json() as Promise\<{ stateRef: string; runId?: string }\>;

}

async step(stateRef: string, n = 1) {

const r = await fetch(\`\${this.endpoint}/step\`, {

method: \"POST\",

headers: { \"content-type\": \"application/json\" },

body: JSON.stringify({ stateRef, n })

});

if (!r.ok) throw new Error(\`step failed: \${r.status}\`);

return r.json() as Promise\<{ stateRef: string; events: any\[\] }\>;

}

async finalize(stateRef: string) {

const r = await fetch(\`\${this.endpoint}/finalize\`, {

method: \"POST\",

headers: { \"content-type\": \"application/json\" },

body: JSON.stringify({ stateRef })

});

if (!r.ok) throw new Error(\`finalize failed: \${r.status}\`);

return r.json(); // parse to ArtifactIndex once you return it

}

async run(manifest: any, runDir: string) {

const { stateRef } = await this.init(manifest, runDir);

// loop /step, append metrics.jsonl on TS side (or engine side)

while (true) {

const { events } = await this.step(stateRef, 10);

if (!events.length) break;

// append events to metrics.jsonl\...

}

return this.finalize(stateRef);

}

}

**5) The missing piece you should decide now: "init/sequences contract"**
-------------------------------------------------------------------------

Your QARICore needs X0, Xi(t), Lam(t), G(t).

For Phase 2, pick one of these minimal contracts (both fit cleanly under
manifest.extensions.engine):

### **Option A (recommended): engine generates sequences deterministically**

\"extensions\": {

\"engine\": {

\"dim\": 3,

\"sequence\": { \"kind\": \"generated\", \"xi\": 1.0, \"lam\": 0.0,
\"gBias\": 0.0 }

}

}

### **Option B: TS provides arrays (paths)**

\"extensions\": {

\"engine\": {

\"dim\": 3,

\"sequence\": {

\"kind\": \"paths\",

\"Xi\": \"arrays/Xi.npy\",

\"Lam\": \"arrays/Lam.npy\",

\"G\": \"arrays/G.npy\"

}

}

}

You can start with A, and later add B for cross-engine comparability (TS
can standardize those arrays and multiple engines can consume them).

**Suggested "Phase 2 done" checklist**
--------------------------------------

-   Patch CalculatorClient to include api\_version: \"2.3.0\"
    > automatically

-   Add scripts/qari\_engine\_run.py that writes metrics.jsonl +
    > ArtifactIndex.json

-   Implement TS PythonSubprocessAdapter that spawns it and validates
    > outputs

-   Add scripts/qari\_engine\_api.py (FastAPI) with /capabilities,
    > /init, /step, /finalize

-   Implement TS PythonHttpAdapter

-   Decide initial extensions.engine contract (generated vs paths)

If you tell me which init/sequences contract you want first (generated
vs paths), I'll tighten the Python runner skeleton to use **real**
qari.gen-equivalent generation or load .npy arrays, and I'll align the
emitted MetricEvent fields to your q/gapLB/margin/certified semantics.
