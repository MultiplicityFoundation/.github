---
slug: phase-1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/Phase 1.md
  last_synced: '2026-03-20T17:17:15.109953Z'
---

Phase 1 is where we "lock the physics" of the system: **every
run/sweep/artifact/metric event is a JSON document with a stable
schema**, and TS owns that contract.

Below is a concrete, repo-friendly implementation plan (files + code
skeletons) that won't disturb Python packaging.

**1) Root workspace wiring (pnpm + turbo)**
-------------------------------------------

### **pnpm-workspace.yaml (repo root)**

Include the existing dashboard at frontend/ plus new TS packages:

packages:

\- \"frontend\"

\- \"packages-ts/\*\"

### **turbo.json (repo root)**

Keep it minimal at first (schema package drives types + JSON Schema
output):

{

\"\$schema\": \"https://turbo.build/schema.json\",

\"tasks\": {

\"build\": {

\"dependsOn\": \[\"\^build\"\],

\"outputs\": \[\"dist/\*\*\", \"build/\*\*\", \".next/\*\*\"\]

},

\"dev\": { \"cache\": false, \"persistent\": true },

\"lint\": {},

\"test\": {}

}

}

### **Root package.json (repo root)**

This is *only* for the TS workspace; Python stays as-is.

{

\"name\": \"qcalc-workspace\",

\"private\": true,

\"packageManager\": \"pnpm\@9.15.0\",

\"scripts\": {

\"build\": \"turbo build\",

\"dev\": \"turbo dev\",

\"lint\": \"turbo lint\",

\"test\": \"turbo test\"

}

}

**2) New TS package: \@qcalc/schemas**
--------------------------------------

### **Folder layout**

packages-ts/

schemas/

package.json

tsconfig.json

src/

index.ts

versions.ts

common.ts

runManifest.ts

sweepSpec.ts

artifactIndex.ts

metrics.ts

apiV2.ts

jsonSchema.ts

### **packages-ts/schemas/package.json**

{

\"name\": \"\@qcalc/schemas\",

\"version\": \"0.1.0\",

\"type\": \"module\",

\"main\": \"./dist/index.js\",

\"types\": \"./dist/index.d.ts\",

\"exports\": {

\".\": \"./dist/index.js\",

\"./json-schema/\*\": \"./dist/json-schema/\*\"

},

\"scripts\": {

\"build\": \"tsc -p tsconfig.json && node dist/jsonSchema.js\",

\"lint\": \"eslint .\",

\"test\": \"vitest\"

},

\"dependencies\": {

\"zod\": \"\^3.24.1\",

\"zod-to-json-schema\": \"\^3.23.5\"

},

\"devDependencies\": {

\"typescript\": \"\^5.8.3\",

\"vitest\": \"\^2.1.8\",

\"\@types/node\": \"\^22.16.5\"

}

}

### **packages-ts/schemas/tsconfig.json**

{

\"compilerOptions\": {

\"target\": \"ES2022\",

\"module\": \"ES2022\",

\"moduleResolution\": \"Bundler\",

\"declaration\": true,

\"outDir\": \"dist\",

\"strict\": true,

\"skipLibCheck\": true

},

\"include\": \[\"src/\*\*/\*.ts\"\]

}

**3) Versioning rules (the "contract spine")**
----------------------------------------------

### **src/versions.ts**

export const RUN\_MANIFEST\_VERSION = \"1.0.0\" as const;

export const SWEEP\_SPEC\_VERSION = \"1.0.0\" as const;

export const ARTIFACT\_INDEX\_VERSION = \"1.0.0\" as const;

export const METRIC\_EVENT\_VERSION = \"1.0.0\" as const;

// This is your orchestration protocol, separate from manifest shape.

export const ENGINE\_PROTOCOL\_VERSION = \"0.1.0\" as const;

// Python calculator API v2 version (must match Python side).

export const PY\_CALC\_API\_VERSION = \"2.3.0\" as const;

**Policy:**

-   Additive optional fields → bump **minor**.

-   Breaking changes → bump **major**.

-   Store unknown blocks verbatim under extensions (so experiments never
    > lose context).

**4) Common primitives (IDs, hashes, semver, timestamps)**
----------------------------------------------------------

### **src/common.ts**

import { z } from \"zod\";

export const Semver =
z.string().regex(/\^\\d+\\.\\d+\\.\\d+(-\[0-9A-Za-z.-\]+)?\$/);

export const IsoDateTime = z.string().datetime(); // RFC3339-ish

export const ContentHash = z.string().regex(

/\^(sha256:)\[0-9a-f\]{64}\$/i,

\"expected sha256:\<64-hex\>\"

);

export const RunId = z.string().min(8).max(80); // e.g. ulid/uuid/custom

export const JsonRecord = z.record(z.string(), z.unknown());

**5) RunManifest.json (single-run definition)**
-----------------------------------------------

### **Design goals**

-   Everything needed to reproduce: engine + model + seeds + schedule +
    > budgets + artifact preferences.

-   Explicit **protocol versions** and **api versions**.

-   A single place to hang "research extras" without breaking consumers:
    > extensions.

### **src/runManifest.ts**

import { z } from \"zod\";

import { IsoDateTime, JsonRecord, RunId, Semver } from \"./common.js\";

import { ENGINE\_PROTOCOL\_VERSION, PY\_CALC\_API\_VERSION,
RUN\_MANIFEST\_VERSION } from \"./versions.js\";

export const EngineRef = z.discriminatedUnion(\"kind\", \[

z.object({

kind: z.literal(\"python-subprocess\"),

pythonModule: z.string().min(1), // e.g. \"qari\_engine.run\"

args: z.array(z.string()).optional(), // extra CLI args

protocolVersion: Semver.default(ENGINE\_PROTOCOL\_VERSION)

}),

z.object({

kind: z.literal(\"python-http\"),

endpoint: z.string().url(), // e.g. http://127.0.0.1:7071

protocolVersion: Semver.default(ENGINE\_PROTOCOL\_VERSION)

})

\]);

export const ModelSpec = z.object({

name: z.string().min(1),

variant: z.string().optional(),

primeSet: z.union(\[

z.array(z.number().int().positive()).min(1),

z.string().min(1) // allow \"firstN:256\" or \"p\<=997\"

\]),

dtype: z.enum(\[\"float32\", \"float64\"\]).default(\"float64\")

});

export const SeedSpec = z.object({

global: z.number().int().nonnegative(),

streams: z.record(z.string(),
z.number().int().nonnegative()).default({})

});

export const ScheduleSpec = z.object({

steps: z.number().int().positive(),

logEvery: z.number().int().positive().default(1),

checkpointEvery: z.number().int().positive().optional()

});

export const CertBudgets = z.object({

epsilon: z.number().positive().default(0.05), // contraction margin

opNormT: z.number().positive().default(1.0),

etaBudget: z.number().min(0).default(0.0), // non-commutation budget if
used

csl: z.object({

enforce: z.boolean().default(true),

failOnViolation: z.boolean().default(true)

}).default({ enforce: true, failOnViolation: true })

});

export const ArtifactPrefs = z.object({

saveTraces: z.boolean().default(true),

saveArrays: z.boolean().default(false),

saveCheckpoints: z.boolean().default(true),

formats: z.array(z.enum(\[\"jsonl\", \"json\", \"npy\",
\"parquet\"\])).default(\[\"jsonl\", \"json\"\])

});

export const RunManifest = z.object({

manifestVersion: Semver.default(RUN\_MANIFEST\_VERSION),

runId: RunId.optional(), // runner can assign if omitted

createdAt: IsoDateTime.optional(),

engine: EngineRef,

// The calculator is a dependency even if the engine is subprocess.

calculator: z.object({

apiVersion:
z.literal(PY\_CALC\_API\_VERSION).default(PY\_CALC\_API\_VERSION),

endpoint: z.string().url().optional() // if engine doesn't embed
calculator

}).default({ apiVersion: PY\_CALC\_API\_VERSION }),

model: ModelSpec,

seed: SeedSpec,

schedule: ScheduleSpec,

budgets: CertBudgets.default({}),

artifacts: ArtifactPrefs.default({}),

tags: z.record(z.string(), z.string()).default({}),

notes: z.string().optional(),

// Always preserve unknown experimental knobs here:

extensions: JsonRecord.default({})

});

**6) SweepSpec.json (grids / LHS / zip / conditionals)**
--------------------------------------------------------

### **src/sweepSpec.ts**

import { z } from \"zod\";

import { JsonRecord, Semver } from \"./common.js\";

import { SWEEP\_SPEC\_VERSION } from \"./versions.js\";

export const ParamPath = z.string().min(1); // e.g. \"budgets.epsilon\"
or JSONPointer \"/budgets/epsilon\"

export const ParamValue = z.union(\[z.string(), z.number(), z.boolean(),
z.null(), z.array(z.any()), z.record(z.any())\]);

export const ParamAxis = z.object({

path: ParamPath,

values: z.array(ParamValue).min(1)

});

export const SweepSpec = z.object({

sweepVersion: Semver.default(SWEEP\_SPEC\_VERSION),

// You can embed a base manifest or reference a file path in runner
layer.

baseManifest: z.record(z.any()),

axes: z.array(ParamAxis).default(\[\]),

policy: z.enum(\[\"cartesian\", \"zip\"\]).default(\"cartesian\"),

// Seeds policy:

seed: z.object({

base: z.number().int().nonnegative().default(0),

perRunOffset: z.boolean().default(true)

}).default({}),

// Room for conditionals (phase 2): "if budgets.epsilon \< 0.03 then
..."

conditionals: z.array(z.object({

when: z.string(),

set: z.record(z.any())

})).default(\[\]),

extensions: JsonRecord.default({})

});

**7) ArtifactIndex.json (what a run produced)**
-----------------------------------------------

### **src/artifactIndex.ts**

import { z } from \"zod\";

import { ContentHash, IsoDateTime, JsonRecord, RunId, Semver } from
\"./common.js\";

import { ARTIFACT\_INDEX\_VERSION } from \"./versions.js\";

export const ArtifactFile = z.object({

path: z.string().min(1), // relative to run root

role: z.enum(\[\"manifest\", \"metrics\", \"checkpoint\", \"array\",
\"report\", \"log\", \"other\"\]).default(\"other\"),

contentType: z.string().min(1), // e.g. \"application/json\"

bytes: z.number().int().nonnegative().optional(),

hash: ContentHash

});

export const ArtifactIndex = z.object({

artifactIndexVersion: Semver.default(ARTIFACT\_INDEX\_VERSION),

runId: RunId,

status: z.enum(\[\"running\", \"succeeded\", \"failed\",
\"canceled\"\]).default(\"running\"),

startedAt: IsoDateTime,

finishedAt: IsoDateTime.optional(),

engine: z.object({

kind: z.string(),

version: z.string().optional(),

protocolVersion: z.string().optional()

}),

provenance: z.object({

gitSha: z.string().optional(),

platform: z.record(z.string(), z.string()).default({})

}).default({ platform: {} }),

files: z.array(ArtifactFile).default(\[\]),

// quick pointers for UI:

metrics: z.object({

jsonl: z.string().optional()

}).default({}),

certificates: z.array(z.object({

name: z.string(),

path: z.string(),

hash: ContentHash

})).default(\[\]),

extensions: JsonRecord.default({})

});

**8) MetricEvent + metrics.jsonl**
----------------------------------

### **src/metrics.ts**

import { z } from \"zod\";

import { IsoDateTime, JsonRecord, Semver } from \"./common.js\";

import { METRIC\_EVENT\_VERSION } from \"./versions.js\";

export const ArchivumMeta = z.object({

prime\_id: z.number().int().positive(),

multiplicity: z.string(),

hash: z.string(),

CSL\_flags: z.record(z.string(), z.any()).default({}),

links: z.array(z.object({ rel: z.string(), href: z.string()
})).default(\[\])

}).partial(); // allow partial if not always present

export const MetricEvent = z.object({

metricVersion: Semver.default(METRIC\_EVENT\_VERSION),

runId: z.string().optional(),

step: z.number().int().nonnegative(),

timestamp: IsoDateTime,

// Core stability witnesses:

q: z.number().optional(),

gapLB: z.number().optional(),

slopeUB: z.number().optional(),

loss: z.number().optional(),

energy: z.number().optional(),

drift: z.number().optional(),

certified: z.boolean().optional(),

budget: z.number().optional(),

margin: z.number().optional(),

// Link to calculator ledger semantics if present:

archivum: ArchivumMeta.optional(),

tags: z.record(z.string(), z.string()).default({}),

extensions: JsonRecord.default({})

});

**9) Python Calculator APIv2 schemas (TS-side validation)**
-----------------------------------------------------------

This is TS mirroring what Python enforces (including api\_version:
\"2.3.0\"), so the runner/orchestrator can validate requests and
responses at the boundary.

### **src/apiV2.ts**

import { z } from \"zod\";

import { PY\_CALC\_API\_VERSION } from \"./versions.js\";

export const ApiVersion = z.literal(PY\_CALC\_API\_VERSION);

export const VersionedRequest = z.object({

api\_version: ApiVersion.default(PY\_CALC\_API\_VERSION)

});

export const NumberMatrix = z.array(z.array(z.number()));

export const ArchivumLink = z.object({ rel: z.string(), href: z.string()
});

export const ArchivumMetadata = z.object({

prime\_id: z.number().int().positive(),

links: z.array(ArchivumLink),

multiplicity: z.string(),

hash: z.string(),

CSL\_flags: z.record(z.string(), z.any()).default({})

});

export const CertifyStepRequest = VersionedRequest.extend({

q\_t: z.number(),

budget: z.number()

});

export const CertifyStepResponse = z.object({

q\_t: z.number(),

budget: z.number(),

certified: z.boolean(),

margin: z.number(),

logs: z.array(z.string()),

archivum: ArchivumMetadata

});

export const ProjectWeightsRequest = VersionedRequest.extend({

Xi: NumberMatrix,

Lam: NumberMatrix,

op\_norm\_T: z.number().default(1.0),

target: z.number().default(0.9)

});

export const ProjectWeightsResponse = z.object({

Xi: NumberMatrix,

Lam: NumberMatrix,

scale: z.number(),

archivum: ArchivumMetadata

});

export const FixedPointRequest = VersionedRequest.extend({

Xi: NumberMatrix,

Lam: NumberMatrix,

G: NumberMatrix,

op\_norm\_T: z.number().default(1.0)

});

export const FixedPointResponse = z.object({

x\_star: NumberMatrix,

tail\_bound: z.number(),

archivum: ArchivumMetadata

});

export const MonitorRequest = VersionedRequest.extend({

X\_prev: NumberMatrix,

X\_curr: NumberMatrix,

invariants: z.record(z.string(), z.any()).default({})

});

export const MonitorResponse = z.object({

residuals: NumberMatrix,

drift: z.number(),

invariants: z.record(z.string(), z.any()),

archivum: ArchivumMetadata

});

**10) JSON Schema export (for validation + UI introspection)**
--------------------------------------------------------------

### **src/jsonSchema.ts**

import { zodToJsonSchema } from \"zod-to-json-schema\";

import { mkdirSync, writeFileSync } from \"node:fs\";

import { RunManifest } from \"./runManifest.js\";

import { SweepSpec } from \"./sweepSpec.js\";

import { ArtifactIndex } from \"./artifactIndex.js\";

import { MetricEvent } from \"./metrics.js\";

mkdirSync(new URL(\"../dist/json-schema/\", import.meta.url), {
recursive: true });

const out = (name: string, schema: any) =\> {

writeFileSync(

new URL(\`../dist/json-schema/\${name}.schema.json\`, import.meta.url),

JSON.stringify(schema, null, 2)

);

};

out(\"RunManifest\", zodToJsonSchema(RunManifest, \"RunManifest\"));

out(\"SweepSpec\", zodToJsonSchema(SweepSpec, \"SweepSpec\"));

out(\"ArtifactIndex\", zodToJsonSchema(ArtifactIndex,
\"ArtifactIndex\"));

out(\"MetricEvent\", zodToJsonSchema(MetricEvent, \"MetricEvent\"));

**11) src/index.ts (public exports)**
-------------------------------------

export \* from \"./versions.js\";

export \* from \"./common.js\";

export \* from \"./runManifest.js\";

export \* from \"./sweepSpec.js\";

export \* from \"./artifactIndex.js\";

export \* from \"./metrics.js\";

export \* from \"./apiV2.js\";

**12) Canonical example documents**
-----------------------------------

### **RunManifest.json**

{

\"manifestVersion\": \"1.0.0\",

\"engine\": {

\"kind\": \"python-subprocess\",

\"pythonModule\": \"qari\_engine.run\",

\"protocolVersion\": \"0.1.0\"

},

\"calculator\": {

\"apiVersion\": \"2.3.0\",

\"endpoint\": \"http://127.0.0.1:7070\"

},

\"model\": {

\"name\": \"qari-core\",

\"variant\": \"pirtm-ace\",

\"primeSet\": \[2,3,5,7,11,13\],

\"dtype\": \"float64\"

},

\"seed\": { \"global\": 123, \"streams\": { \"init\": 1, \"noise\": 2 }
},

\"schedule\": { \"steps\": 200, \"logEvery\": 1, \"checkpointEvery\": 25
},

\"budgets\": { \"epsilon\": 0.05, \"opNormT\": 1.0, \"etaBudget\": 0.0,
\"csl\": { \"enforce\": true, \"failOnViolation\": true } },

\"artifacts\": { \"saveTraces\": true, \"saveArrays\": false,
\"saveCheckpoints\": true, \"formats\": \[\"jsonl\",\"json\"\] },

\"tags\": { \"experiment\": \"baseline\", \"engine\": \"subprocess\" },

\"extensions\": {}

}

### **metrics.jsonl (one line per event)**

{\"metricVersion\":\"1.0.0\",\"step\":0,\"timestamp\":\"2025-12-18T12:00:00Z\",\"q\":0.83,\"gapLB\":0.12,\"certified\":true,\"tags\":{\"phase\":\"init\"}}

{\"metricVersion\":\"1.0.0\",\"step\":1,\"timestamp\":\"2025-12-18T12:00:01Z\",\"q\":0.81,\"gapLB\":0.14,\"drift\":0.02,\"certified\":true}

### **ArtifactIndex.json**

{

\"artifactIndexVersion\": \"1.0.0\",

\"runId\": \"01JFP9R5M5E4Y8B7J2S3Q2P0H1\",

\"status\": \"running\",

\"startedAt\": \"2025-12-18T12:00:00Z\",

\"engine\": { \"kind\": \"python-subprocess\", \"protocolVersion\":
\"0.1.0\" },

\"files\": \[

{ \"path\": \"RunManifest.json\", \"role\": \"manifest\",
\"contentType\": \"application/json\", \"hash\":
\"sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"
},

{ \"path\": \"metrics.jsonl\", \"role\": \"metrics\", \"contentType\":
\"application/x-ndjson\", \"hash\":
\"sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\"
}

\],

\"metrics\": { \"jsonl\": \"metrics.jsonl\" },

\"extensions\": {}

}

**What Phase 1 "Done" looks like**
----------------------------------

-   \@qcalc/schemas builds and outputs:

    -   TypeScript types (for runner/orchestrator/UI)

    -   dist/json-schema/\*.schema.json (for runtime validation, UI
        > introspection, docs)

-   A run can be represented *entirely* by:

    -   RunManifest.json

    -   metrics.jsonl

    -   ArtifactIndex.json

-   TS can also validate the calculator boundary (api\_version:
    > \"2.3.0\") before/after every call.

Here's a tight, **deterministic** mapping so configs/qari.yaml becomes a
*legacy defaults source*, while **RunManifest.json is canonical**.

**1) Canonical rule: "Manifest wins, YAML fills gaps"**
-------------------------------------------------------

When building the *effective* run config:

1.  Start with RunManifest.json (canonical).

2.  If \--legacy-qari-yaml configs/qari.yaml is provided, **only fill
    > missing fields** in the manifest from YAML defaults.

3.  Persist the **resolved** manifest snapshot into the run folder (so
    > reproduction never depends on YAML later).

That gives you: YAML is allowed for convenience, but the run is always
reproducible from JSON alone.

**2) Field-by-field mapping (configs/qari.yaml → RunManifest)**
---------------------------------------------------------------

Given your repo's configs/qari.yaml structure:

### **Core dynamics + schedule**

  **qari.yaml**   **meaning**             **RunManifest target**
  --------------- ----------------------- ------------------------------------------------
  max\_steps      total iterations        schedule.steps
  tol             convergence tolerance   core.tol *(recommended new first-class field)*

✅ **Recommendation:** add a small core object to RunManifest for engine
params that aren't "budgets":

core: z.object({

tol: z.number().positive().optional()

}).default({})

### **Contraction / certification budgets**

  **qari.yaml**   **meaning**           **RunManifest target**
  --------------- --------------------- ------------------------
  epsilon         contraction margin    budgets.epsilon
  op\_norm\_T     operator norm bound   budgets.opNormT

### **Ethics**

  **qari.yaml**        **meaning**                   **RunManifest target**
  -------------------- ----------------------------- ------------------------
  ethics.eta\_budget   "prefer commuting P" budget   budgets.etaBudget

### **PETC / multiplicity enforcement**

These aren't CSL budgets per se; keep them explicit (best), or preserve
under extensions.

**Best (make first-class):**

  **qari.yaml**                **RunManifest target**
  ---------------------------- --------------------------
  petc.enforce\_multiplicity   petc.enforceMultiplicity
  petc.fail\_on\_violation     petc.failOnViolation

If you don't want to expand RunManifest yet:

-   store under extensions.petc = { ... } verbatim.

### **Telemetry**

Telemetry belongs to orchestration/observability, not math. Treat it as
*metadata*:

  **qari.yaml**          **RunManifest target**
  ---------------------- ---------------------------------
  telemetry.level        extensions.telemetry.level
  telemetry.provenance   extensions.telemetry.provenance

(You can later promote this into a first-class telemetry block if you
want UI controls.)

### **Calculator endpoint**

  **qari.yaml**         **meaning**                          **RunManifest target**
  --------------------- ------------------------------------ ----------------------------------------------
  calculator.enabled    whether to call calculator service   calculator.enabled *(recommended new field)*
  calculator.endpoint   URL                                  calculator.endpoint

**Recommendation:** update RunManifest's calculator block to include
enabled?: boolean so the engine adapter can explicitly disable remote
calls.

**3) Minimal schema tweaks to support the mapping cleanly**
-----------------------------------------------------------

To make the mapping "tight" (no weird stuffing into extensions), I'd add
**two small first-class blocks**:

### **A) core**

core: z.object({

tol: z.number().positive().optional()

}).default({})

### **B) petc**

petc: z.object({

enforceMultiplicity: z.boolean().default(true),

failOnViolation: z.boolean().default(true)

}).default({})

### **C) calculator.enabled**

calculator: z.object({

enabled: z.boolean().default(true),

apiVersion:
z.literal(PY\_CALC\_API\_VERSION).default(PY\_CALC\_API\_VERSION),

endpoint: z.string().url().optional()

}).default({ enabled: true, apiVersion: PY\_CALC\_API\_VERSION })

Everything else can remain as-is.

**4) Concrete example: your current configs/qari.yaml → RunManifest**
---------------------------------------------------------------------

Given:

epsilon: 0.05

op\_norm\_T: 1.0

max\_steps: 200

tol: 1.0e-6

ethics:

eta\_budget: 0.0

petc:

enforce\_multiplicity: true

fail\_on\_violation: true

telemetry:

level: info

provenance: local

calculator:

enabled: true

endpoint: \"http://127.0.0.1:7070\"

Resolved manifest fields become:

{

\"schedule\": { \"steps\": 200 },

\"core\": { \"tol\": 0.000001 },

\"budgets\": { \"epsilon\": 0.05, \"opNormT\": 1.0, \"etaBudget\": 0.0
},

\"petc\": { \"enforceMultiplicity\": true, \"failOnViolation\": true },

\"calculator\": { \"enabled\": true, \"apiVersion\": \"2.3.0\",
\"endpoint\": \"http://127.0.0.1:7070\" },

\"extensions\": { \"telemetry\": { \"level\": \"info\", \"provenance\":
\"local\" } }

}

**5) Implementation detail: conversion helpers (TS)**
-----------------------------------------------------

You'll want **two functions** (these make adapters easy too):

### **qariYamlToManifestDefaults(qariYaml)**

-   Produces a *partial* manifest object (only fields derived from YAML)

-   No assumptions, no IDs

### **mergeManifestWithDefaults(manifest, defaults)**

-   Fills missing manifest fields only

-   Returns a **resolved manifest** that you then write into the run
    > folder

Pseudo-code shape:

function mergeMissing\<T\>(base: T, defaults: Partial\<T\>): T {

// deep-merge but only where base is undefined

}

Also: store legacy provenance in the resolved manifest so you can always
prove where defaults came from:

-   extensions.legacy.qariYamlPath

-   extensions.legacy.qariYamlSha256

-   extensions.legacy.mergedAt

Below are **both** deliverables:

1.  a tiny **validate-manifest CLI** (TS)

2.  a **stricter YAML merge mode** (fill-missing vs prefer-yaml vs
    > overwrite specific paths)

I'm keeping this consistent with your ESM/tsc build setup.

**A) Stricter merge modes in fromQariYaml.ts**
==============================================

Replace your packages-ts/schemas/src/fromQariYaml.ts with the version
below (or lift the new parts into it). This adds:

-   mergeMode: \"fill-missing\" \| \"prefer-yaml\" \|
    > \"overwrite-paths\"

-   overwritePaths: string\[\] (dot-paths like budgets.epsilon or JSON
    > Pointer like /budgets/epsilon)

-   resolveRunManifestFromQariYaml() (returns validated manifest without
    > writing)

-   emitRunManifestFromQariYaml() (writes snapshot, calls resolve
    > internally)

import { createHash, randomUUID } from \"node:crypto\";

import { readFile, writeFile } from \"node:fs/promises\";

import path from \"node:path\";

import YAML from \"yaml\";

import { RunManifestSchema, type RunManifest } from
\"./runManifest.js\";

type PlainObject = Record\<string, unknown\>;

function isPlainObject(x: unknown): x is PlainObject {

return typeof x === \"object\" && x !== null && !Array.isArray(x);

}

function sha256Hex(data: string): string {

return createHash(\"sha256\").update(data, \"utf8\").digest(\"hex\");

}

function num(x: unknown): number \| undefined {

return typeof x === \"number\" && Number.isFinite(x) ? x : undefined;

}

function bool(x: unknown): boolean \| undefined {

return typeof x === \"boolean\" ? x : undefined;

}

function str(x: unknown): string \| undefined {

return typeof x === \"string\" ? x : undefined;

}

/\*\* Deep-merge ONLY missing (undefined) fields from defaults into
base. \*/

function mergeMissing\<T\>(base: T, defaults: Partial\<T\>): T {

if (!isPlainObject(base) \|\| !isPlainObject(defaults)) return (base ??
defaults) as T;

const out: PlainObject = { \...defaults, \...base }; // base wins
top-level

for (const \[k, defVal\] of Object.entries(defaults)) {

const baseVal = (base as PlainObject)\[k\];

if (baseVal === undefined) {

out\[k\] = defVal as unknown;

continue;

}

if (isPlainObject(baseVal) && isPlainObject(defVal)) {

out\[k\] = mergeMissing(baseVal, defVal);

}

}

return out as T;

}

/\*\* Deep-merge where YAML (defaults) overrides base ONLY when YAML
provides a defined value. \*/

function mergePreferYaml\<T\>(base: T, defaults: Partial\<T\>): T {

if (defaults === undefined) return base;

if (!isPlainObject(base) \|\| !isPlainObject(defaults)) {

// if defaults is defined, it wins

return (defaults as T) ?? base;

}

const out: PlainObject = { \...base };

for (const \[k, defVal\] of Object.entries(defaults)) {

const baseVal = (base as PlainObject)\[k\];

if (defVal === undefined) continue;

if (isPlainObject(baseVal) && isPlainObject(defVal)) {

out\[k\] = mergePreferYaml(baseVal, defVal);

} else {

// arrays/scalars: override whole value

out\[k\] = defVal;

}

}

return out as T;

}

/\*\* Dot-path (a.b.c) or JSON Pointer (/a/b/c) into path segments \*/

function parsePath(p: string): string\[\] {

if (p.startsWith(\"/\")) {

// JSON Pointer

return p

.split(\"/\")

.slice(1)

.map((s) =\> s.replace(/\~1/g, \"/\").replace(/\~0/g, \"\~\"))

.filter(Boolean);

}

return p.split(\".\").filter(Boolean);

}

function getAtPath(obj: unknown, p: string): unknown {

const segs = parsePath(p);

let cur: any = obj;

for (const s of segs) {

if (!isPlainObject(cur) && !Array.isArray(cur)) return undefined;

cur = cur\[s\];

if (cur === undefined) return undefined;

}

return cur;

}

function setAtPath(obj: unknown, p: string, value: unknown): unknown {

const segs = parsePath(p);

if (segs.length === 0) return obj;

const root = isPlainObject(obj) ? { \...obj } : {};

let cur: any = root;

for (let i = 0; i \< segs.length; i++) {

const key = segs\[i\]!;

const isLast = i === segs.length - 1;

if (isLast) {

cur\[key\] = value;

break;

}

const next = cur\[key\];

cur\[key\] = isPlainObject(next) ? { \...next } : {};

cur = cur\[key\];

}

return root;

}

export type YamlMergeMode = \"fill-missing\" \| \"prefer-yaml\" \|
\"overwrite-paths\";

function applyYamlMerge(

baseManifest: unknown,

yamlDefaults: Partial\<RunManifest\>,

mode: YamlMergeMode,

overwritePaths: string\[\] = \[\]

): unknown {

if (mode === \"prefer-yaml\") {

return mergePreferYaml(baseManifest as any, yamlDefaults as any);

}

// Start with fill-missing baseline

let merged = mergeMissing(baseManifest as any, yamlDefaults as any);

if (mode === \"overwrite-paths\") {

for (const p of overwritePaths) {

const v = getAtPath(yamlDefaults, p);

if (v !== undefined) merged = setAtPath(merged, p, v);

}

}

return merged;

}

/\*\*

\* Convert configs/qari.yaml (legacy defaults) -\> partial RunManifest
fields.

\* Does NOT fabricate required manifest fields like engine/model/seed.

\*/

export function qariYamlToManifestDefaults(yamlObj: unknown):
Partial\<RunManifest\> {

if (!isPlainObject(yamlObj)) return {};

const ethics = isPlainObject(yamlObj.ethics) ? yamlObj.ethics : {};

const petc = isPlainObject(yamlObj.petc) ? yamlObj.petc : {};

const telemetry = isPlainObject(yamlObj.telemetry) ? yamlObj.telemetry :
{};

const calculator = isPlainObject(yamlObj.calculator) ?
yamlObj.calculator : {};

const defaults: Partial\<RunManifest\> = {

schedule: {

\...(num(yamlObj.max\_steps) !== undefined ? { steps:
num(yamlObj.max\_steps)! } : {}),

} as any,

core: {

\...(num(yamlObj.tol) !== undefined ? { tol: num(yamlObj.tol)! } : {}),

} as any,

budgets: {

\...(num(yamlObj.epsilon) !== undefined ? { epsilon:
num(yamlObj.epsilon)! } : {}),

\...(num(yamlObj.op\_norm\_T) !== undefined ? { opNormT:
num(yamlObj.op\_norm\_T)! } : {}),

\...(num(ethics.eta\_budget) !== undefined ? { etaBudget:
num(ethics.eta\_budget)! } : {}),

} as any,

petc: {

\...(bool(petc.enforce\_multiplicity) !== undefined

? { enforceMultiplicity: bool(petc.enforce\_multiplicity)! }

: {}),

\...(bool(petc.fail\_on\_violation) !== undefined

? { failOnViolation: bool(petc.fail\_on\_violation)! }

: {}),

} as any,

calculator: {

\...(bool(calculator.enabled) !== undefined ? { enabled:
bool(calculator.enabled)! } : {}),

\...(str(calculator.endpoint) !== undefined ? { endpoint:
str(calculator.endpoint)! } : {}),

} as any,

extensions: {

telemetry: {

\...(str(telemetry.level) !== undefined ? { level: str(telemetry.level)!
} : {}),

\...(str(telemetry.provenance) !== undefined ? { provenance:
str(telemetry.provenance)! } : {}),

},

},

};

return defaults;

}

export type ResolveRunManifestFromQariYamlOptions = {

qariYamlPath: string;

baseManifest: unknown;

autoFillIds?: boolean;

mergeMode?: YamlMergeMode; // default \"fill-missing\"

overwritePaths?: string\[\]; // only used for \"overwrite-paths\"

};

export async function resolveRunManifestFromQariYaml(

opts: ResolveRunManifestFromQariYamlOptions

): Promise\<RunManifest\> {

const raw = await readFile(opts.qariYamlPath, \"utf8\");

const yamlObj = YAML.parse(raw);

const yamlDefaults = qariYamlToManifestDefaults(yamlObj);

const legacyMeta = {

legacy: {

qariYaml: {

path: opts.qariYamlPath,

sha256: \`sha256:\${sha256Hex(raw)}\`,

loadedAt: new Date().toISOString(),

},

},

};

const mode: YamlMergeMode = opts.mergeMode ?? \"fill-missing\";

let merged = applyYamlMerge(opts.baseManifest, yamlDefaults, mode,
opts.overwritePaths ?? \[\]);

// Attach legacy provenance without overwriting user-specified
extensions

merged = mergeMissing(merged as any, { extensions: legacyMeta } as any);

if (opts.autoFillIds) {

merged = mergeMissing(merged as any, {

runId: randomUUID(),

createdAt: new Date().toISOString(),

} as any);

}

return RunManifestSchema.parse(merged);

}

export type EmitRunManifestFromQariYamlOptions =
ResolveRunManifestFromQariYamlOptions & {

outPath: string;

};

export async function emitRunManifestFromQariYaml(

opts: EmitRunManifestFromQariYamlOptions

): Promise\<RunManifest\> {

const validated = await resolveRunManifestFromQariYaml(opts);

const outDir = path.dirname(opts.outPath);

await writeFile(path.join(outDir, path.basename(opts.outPath)),
JSON.stringify(validated, null, 2) + \"\\n\", \"utf8\");

return validated;

}

### **Merge modes behavior**

-   fill-missing (default): **manifest wins**, YAML only fills
    > undefined.

-   prefer-yaml: YAML overrides any fields it provides (handy "default
    > run" behavior).

-   overwrite-paths: manifest wins except for explicit paths (e.g. only
    > override schedule.steps and budgets.epsilon).

**B) Tiny validate-manifest CLI (TS)**
======================================

I'd put this in a new package packages-ts/runner so schemas stays
"pure-ish", but it can also live in \@qcalc/schemas if you want.

**packages-ts/runner/package.json**
-----------------------------------

{

\"name\": \"\@qcalc/runner\",

\"version\": \"0.1.0\",

\"private\": true,

\"type\": \"module\",

\"bin\": {

\"qcalc-validate-manifest\": \"./dist/validate-manifest.js\"

},

\"scripts\": {

\"build\": \"tsc -p tsconfig.json\",

\"dev\": \"node dist/validate-manifest.js \--help\"

},

\"dependencies\": {

\"\@qcalc/schemas\": \"workspace:\*\"

},

\"devDependencies\": {

\"\@types/node\": \"\^22.16.5\",

\"typescript\": \"\^5.8.3\"

}

}

**packages-ts/runner/tsconfig.json**
------------------------------------

{

\"compilerOptions\": {

\"target\": \"ES2022\",

\"module\": \"ES2022\",

\"moduleResolution\": \"Bundler\",

\"outDir\": \"dist\",

\"strict\": true,

\"skipLibCheck\": true

},

\"include\": \[\"src/\*\*/\*.ts\"\]

}

**packages-ts/runner/src/validate-manifest.ts**
-----------------------------------------------

\#!/usr/bin/env node

import { readFile, writeFile } from \"node:fs/promises\";

import { resolve } from \"node:path\";

import { ZodError } from \"zod\";

import { resolveRunManifestFromQariYaml, type YamlMergeMode } from
\"\@qcalc/schemas/fromQariYaml.js\";

type Args = {

qariYaml?: string;

baseManifest?: string;

out?: string;

pretty?: boolean;

autoFillIds?: boolean;

mergeMode?: YamlMergeMode;

overwrite?: string\[\];

};

function parseArgs(argv: string\[\]): Args {

const out: Args = { pretty: true, autoFillIds: true, mergeMode:
\"fill-missing\", overwrite: \[\] };

for (let i = 0; i \< argv.length; i++) {

const a = argv\[i\]!;

if (a === \"\--help\" \|\| a === \"-h\") return { \...out, qariYaml:
\"HELP\" };

const \[k, vEq\] = a.includes(\"=\") ? a.split(\"=\", 2) : \[a,
undefined\];

const next = () =\> (vEq ?? argv\[++i\]);

switch (k) {

case \"\--qari-yaml\":

out.qariYaml = next();

break;

case \"\--base-manifest\":

out.baseManifest = next();

break;

case \"\--out\":

out.out = next();

break;

case \"\--pretty\":

out.pretty = true;

break;

case \"\--no-pretty\":

out.pretty = false;

break;

case \"\--autofill-ids\":

out.autoFillIds = true;

break;

case \"\--no-autofill-ids\":

out.autoFillIds = false;

break;

case \"\--yaml-merge\":

out.mergeMode = next() as YamlMergeMode;

break;

case \"\--overwrite\":

{

const val = next();

if (val) out.overwrite!.push(\...val.split(\",\").map((s) =\>
s.trim()).filter(Boolean));

}

break;

default:

if (k.startsWith(\"\--\")) {

console.error(\`Unknown option: \${k}\`);

process.exit(2);

}

}

}

return out;

}

function printHelp() {

console.log(\`

qcalc-validate-manifest

Validates a base RunManifest.json and optionally applies legacy
configs/qari.yaml defaults.

Prints the fully resolved, Zod-validated RunManifest JSON snapshot.

Usage:

qcalc-validate-manifest \--base-manifest path/to/base.json
\[\--qari-yaml configs/qari.yaml\]

\[\--yaml-merge fill-missing\|prefer-yaml\|overwrite-paths\]

\[\--overwrite budgets.epsilon \--overwrite schedule.steps\]

\[\--out resolved.json\]

\[\--no-pretty\]

\[\--no-autofill-ids\]

Examples:

\# manifest canonical; YAML fills missing

qcalc-validate-manifest \--base-manifest base.json \--qari-yaml
configs/qari.yaml

\# YAML overrides wherever it provides values

qcalc-validate-manifest \--base-manifest base.json \--qari-yaml
configs/qari.yaml \--yaml-merge prefer-yaml

\# Only override specific fields from YAML

qcalc-validate-manifest \--base-manifest base.json \--qari-yaml
configs/qari.yaml \\\\

\--yaml-merge overwrite-paths \--overwrite schedule.steps \--overwrite
budgets.epsilon

\`.trim());

}

function formatZodError(err: ZodError): string {

return err.issues

.map((iss) =\> {

const p = iss.path.length ? iss.path.join(\".\") : \"(root)\";

return \`- \${p}: \${iss.message}\`;

})

.join(\"\\n\");

}

async function main() {

const args = parseArgs(process.argv.slice(2));

if (args.qariYaml === \"HELP\" \|\| !args.baseManifest) {

printHelp();

process.exit(args.baseManifest ? 0 : 2);

}

try {

const basePath = resolve(args.baseManifest);

const baseRaw = await readFile(basePath, \"utf8\");

const base = JSON.parse(baseRaw);

const resolved = args.qariYaml

? await resolveRunManifestFromQariYaml({

qariYamlPath: resolve(args.qariYaml),

baseManifest: base,

autoFillIds: args.autoFillIds,

mergeMode: args.mergeMode,

overwritePaths: args.overwrite ?? \[\],

})

: // If no YAML, just validate base as-is.

// (We import schema indirectly through resolveRunManifestFromQariYaml
normally,

// but for simplicity, we can just run it through the same function with
empty defaults.)

await resolveRunManifestFromQariYaml({

qariYamlPath: resolve(args.qariYaml ?? \"\"), // unused if you want:
replace with direct schema parse if preferred

baseManifest: base,

autoFillIds: args.autoFillIds,

mergeMode: \"fill-missing\",

overwritePaths: \[\],

});

const json = JSON.stringify(resolved, null, args.pretty ? 2 : undefined)
+ \"\\n\";

if (args.out) {

await writeFile(resolve(args.out), json, \"utf8\");

console.error(\`Wrote resolved manifest to \${args.out}\`);

} else {

process.stdout.write(json);

}

} catch (e: any) {

if (e instanceof ZodError) {

console.error(\"RunManifest validation failed:\\n\" +
formatZodError(e));

process.exit(1);

}

console.error(\"Error:\", e?.message ?? e);

process.exit(1);

}

}

main();

> Note: if you want the "no YAML" path to avoid the dummy qariYamlPath,
> just import RunManifestSchema directly and parse base. I kept the CLI
> tiny; happy to adjust.

**Recommended CLI defaults**
============================

-   Default \--yaml-merge fill-missing

-   For quick local runs: \--yaml-merge prefer-yaml

-   For controlled override: \--yaml-merge overwrite-paths \--overwrite
    > \...
