---
slug: phase-3
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/Phase 3.md
  last_synced: '2026-03-20T17:17:15.382866Z'
---

Phase 3 is where TS becomes the "lab OS": **it decides what runs exist,
where artifacts go, how they're indexed, how metrics are summarized, and
how comparisons/regressions are computed.** Below is a concrete,
implementation-ready expansion.

**1) \@qcalc/runner CLI**
-------------------------

### **Commands**

**qcalc run \<RunManifest.json\>**

-   Validate (Zod) + resolve legacy defaults (\--qari-yaml) → write
    > **resolved snapshot** into the run folder.

-   Create run directory + artifact layout.

-   Select engine adapter (python-subprocess or python-http) and
    > execute.

-   Stream metrics.jsonl (tail file or from HTTP events) and update
    > summaries.

-   Finalize: validate ArtifactIndex.json, compute any missing hashes,
    > insert into sqlite.

**qcalc sweep \<SweepSpec.json\>**

-   Expand sweep deterministically (stable ordering).

-   For each derived run:

    -   materialize a derived resolved manifest

    -   schedule concurrency (\--jobs N)

    -   resume partially completed sweeps (\--resume reads sqlite + run
        > folders)

-   Emit sweep-level summary report (and optionally a "compare all"
    > matrix).

**qcalc reproduce \<run-id\>**

-   Pull canonical RunManifest.json snapshot from store by run-id.

-   Re-run (same seed + same engine version constraints if possible).

-   Compare:

    -   manifest hash equality (should match)

    -   metric deltas

    -   artifact hash equality where applicable

-   Emit an evidence bundle: manifest + artifactIndex +
    > comparison.json + report.md.

### **Minimal CLI package layout**

packages-ts/

runner/

src/

cli.ts

commands/run.ts

commands/sweep.ts

commands/reproduce.ts

engine/selectAdapter.ts

util/stableJson.ts

util/fs.ts

### **Deterministic ordering + run identity**

Two IDs are useful:

-   runId: ULID/UUID for human + filesystem

-   runKey: **sha256 of stable-canonical manifest** (this is what makes
    > reproduce + dedupe clean)

Rule:

-   runKey =
    > sha256(stableStringify(resolvedManifestMinusRunIdCreatedAt))

-   store both in sqlite; let users search by tags, filter, etc.

**2) \@qcalc/store --- content-hashed artifact layout + sqlite index**
----------------------------------------------------------------------

### **Key design principle**

Treat artifacts as **content-addressed blobs**, and runs as **manifests
+ references**.

That gives you:

-   dedupe across runs/sweeps

-   consistent future S3 support

-   fast "export evidence bundle" (just collect references)

### **Recommended on-disk layout (local filesystem store)**

.qcalc-store/

db.sqlite

blobs/

sha256/

ab/

sha256\_abcd\... (raw bytes)

runs/

\<runId\>/

RunManifest.json

ArtifactIndex.json

metrics.jsonl

links/

checkpoint\_latest.npz -\> ../../blobs/sha256/ab/sha256\_abcd\...

reports/

compare.json

report.md

**Rules**

-   Every file with value gets hashed sha256:\<hex\> and stored in
    > blobs/.

-   The run folder holds:

    -   canonical snapshots (RunManifest.json, ArtifactIndex.json,
        > metrics.jsonl)

    -   *links* (either symlinks or tiny JSON pointers) to blob objects
        > for large arrays/checkpoints.

### **Store API (TS)**

export interface BlobStore {

putBytes(bytes: Uint8Array): Promise\<{ hash: string; bytes: number }\>;

putFile(path: string): Promise\<{ hash: string; bytes: number }\>;

open(hash: string): Promise\<NodeJS.ReadableStream\>;

}

export interface RunStore {

initRun(runId: string): Promise\<{ runDir: string }\>;

writeManifest(runId: string, manifest: unknown): Promise\<{
manifestPath: string; manifestHash: string }\>;

finalizeRun(runId: string, artifactIndex: unknown): Promise\<void\>;

linkBlob(runId: string, logicalPath: string, blobHash: string):
Promise\<void\>;

db: StoreDb;

}

### **SQLite schema (practical, query-friendly)**

**runs**

-   run\_id TEXT PRIMARY KEY

-   run\_key TEXT UNIQUE (sha256 of canonical manifest)

-   status TEXT (running\|succeeded\|failed\|canceled)

-   engine\_kind TEXT

-   engine\_version TEXT

-   protocol\_version TEXT

-   manifest\_version TEXT

-   manifest\_hash TEXT

-   started\_at TEXT

-   finished\_at TEXT

-   tags\_json TEXT (stringified JSON)

-   notes TEXT

-   git\_sha TEXT

-   platform\_json TEXT

**artifacts**

-   id INTEGER PRIMARY KEY

-   run\_id TEXT

-   role TEXT (manifest\|metrics\|checkpoint\|array\|report\|log\|other)

-   path TEXT (run-relative logical path)

-   hash TEXT (sha256:\...)

-   content\_type TEXT

-   bytes INTEGER

**metrics\_summary**

-   run\_id TEXT

-   series TEXT (e.g. q, gapLB, drift)

-   count INTEGER

-   min REAL, max REAL, mean REAL, m2 REAL (Welford)

-   first\_step INTEGER, last\_step INTEGER

-   optional: p50 REAL, p90 REAL (if you add quantiles)

**sweeps**

-   sweep\_id TEXT PRIMARY KEY

-   sweep\_hash TEXT UNIQUE

-   created\_at TEXT

-   status TEXT

**sweep\_runs**

-   sweep\_id TEXT

-   run\_id TEXT

-   axis\_values\_json TEXT (the concrete axis assignments)

Indexes:

-   (engine\_kind, engine\_version)

-   (status, started\_at)

-   (run\_key)

-   json tags (optional: store a few commonly filtered tags into columns
    > later)

### **Optional S3 later (no rewrite)**

Define BlobStore as above and implement:

-   LocalBlobStore now

-   S3BlobStore later (same hash key ⇒ same object key)

**3) \@qcalc/metrics --- streaming aggregation + compare + regressions**
------------------------------------------------------------------------

### **Streaming ingestion from metrics.jsonl**

You want the ability to:

-   show live charts in UI

-   compute per-run summaries incrementally

-   enable CI regression checks without loading huge arrays

**Ingest loop**

-   tail metrics.jsonl (subprocess case) or consume event stream (http
    > case)

-   parse MetricEvent via Zod

-   update online stats per series

### **Online stats (simple + effective)**

Use Welford for mean/variance without storing all points:

-   count, mean, m2, min/max, first/last step.

Keep this in memory during run and periodically flush to sqlite
metrics\_summary and/or a small runs/\<runId\>/metrics\_summary.json.

If you want quantiles later:

-   add P² quantile estimator or tdigest; keep optional.

### **Compare runs (single vs single, or group vs group)**

Outputs:

-   aligned-by-step delta series: Δq, ΔgapLB, Δdrift

-   aggregate deltas: mean absolute delta, RMS delta, max delta

-   pass/fail vs thresholds

**Compare API**

export type CompareSpec = {

metrics: string\[\]; // \[\"q\",\"gapLB\",\"drift\"\]

align: \"step\"; // later: timestamp

window?: { start?: number; end?: number };

thresholds?: Record\<string, { maxAbsMean?: number; maxAbsMax?: number
}\>;

};

export function compareRuns(aMetricsPath: string, bMetricsPath: string,
spec: CompareSpec): Promise\<{

summary: any;

series?: Record\<string, Array\<{ step: number; a?: number; b?: number;
delta?: number }\>\>;

}\>;

### **Regression detection (CI-friendly)**

A "regression" is just a compare against a baseline with thresholds.

Add a CLI:

-   qcalc regression \--baseline \<run-id\|tag query\> \--candidate
    > \<run-id\|path\> \--spec regression.json

Where regression.json is like:

{

\"metrics\": \[\"gapLB\", \"q\", \"drift\"\],

\"window\": { \"start\": 50, \"end\": 200 },

\"thresholds\": {

\"gapLB\": { \"maxAbsMean\": 0.02, \"maxAbsMax\": 0.05 },

\"drift\": { \"maxAbsMean\": 0.01 }

}

}

Exit codes:

-   0 pass

-   1 regression detected

-   2 config/error

This becomes the backbone of "this commit changed stability/fidelity by
X".

**4) Reproducibility layout (what gets frozen per run)**
--------------------------------------------------------

Each run folder should contain enough to reproduce *without any external
context*:

**Always**

-   RunManifest.json (resolved snapshot; includes
    > extensions.legacy.qariYaml.sha256 if YAML was used)

-   metrics.jsonl

-   ArtifactIndex.json

-   provenance.json (optional but recommended):

    -   git sha

    -   python version

    -   node version

    -   OS/arch

    -   engine capabilities snapshot

    -   calculator endpoint + api version

**Optionally**

-   inputs/ (copied input arrays/seeds if you want maximal determinism)

-   reports/ (compare/regression outputs)

**1) packages-ts/store: concrete SQLite choice + WAL + locking story**
----------------------------------------------------------------------

### **SQLite library choice**

Use **better-sqlite3** for Phase 3.

Why:

-   fastest + simplest for a local "lab index"

-   synchronous API makes **short, explicit transactions** easy
    > (critical for avoiding lock chaos)

-   works well with WAL and busy timeouts

**Dependencies**

-   better-sqlite3

-   \@types/better-sqlite3 (dev)

### **WAL + PRAGMA profile (recommended defaults)**

On open, set:

-   PRAGMA journal\_mode=WAL;

-   PRAGMA synchronous=NORMAL; (good balance for local dev; switch to
    > FULL for ultra-safety)

-   PRAGMA foreign\_keys=ON;

-   PRAGMA busy\_timeout=5000; (or 10--30s for big sweeps)

-   PRAGMA temp\_store=MEMORY;

-   PRAGMA wal\_autocheckpoint=1000; (tune later)

### **Locking story for concurrent workers**

SQLite WAL gives **many readers + one writer** at a time. If you let
every worker write continuously, you'll see SQLITE\_BUSY.

**Phase 3 recommended locking model**

-   **One writer process**: the orchestrator (qcalc sweep / qcalc run)
    > is the only component that writes to sqlite.

-   Workers (python subprocesses) write *only to runDir files*
    > (metrics.jsonl, ArtifactIndex.json, checkpoints).

-   Orchestrator tails metrics and updates sqlite **infrequent /
    > batched** (or only at run end).

This is extremely robust and keeps sqlite happy.

**If you later want multi-node / multi-process writers**

-   Add a small "store daemon" (HTTP/IPC) that serializes writes, or

-   use a queue table + leasing in sqlite (still one-writer at a time,
    > but coordinated).

**2) packages-ts/store minimal implementation skeleton**
--------------------------------------------------------

### **packages-ts/store/package.json**

{

\"name\": \"\@qcalc/store\",

\"version\": \"0.1.0\",

\"type\": \"module\",

\"main\": \"./dist/index.js\",

\"types\": \"./dist/index.d.ts\",

\"exports\": { \".\": \"./dist/index.js\" },

\"scripts\": { \"build\": \"tsc -p tsconfig.json\" },

\"dependencies\": { \"better-sqlite3\": \"\^11.8.1\" },

\"devDependencies\": { \"\@types/better-sqlite3\": \"\^7.6.12\",
\"typescript\": \"\^5.8.3\" }

}

### **packages-ts/store/tsconfig.json**

{

\"compilerOptions\": {

\"target\": \"ES2022\",

\"module\": \"ES2022\",

\"moduleResolution\": \"Bundler\",

\"outDir\": \"dist\",

\"declaration\": true,

\"strict\": true,

\"skipLibCheck\": true,

\"esModuleInterop\": true,

\"allowSyntheticDefaultImports\": true

},

\"include\": \[\"src/\*\*/\*.ts\"\]

}

### **packages-ts/store/src/schema.sql.ts**

export const SCHEMA\_SQL = \`

PRAGMA foreign\_keys=ON;

CREATE TABLE IF NOT EXISTS runs (

run\_id TEXT PRIMARY KEY,

run\_key TEXT UNIQUE,

status TEXT NOT NULL,

engine\_kind TEXT,

engine\_version TEXT,

protocol\_version TEXT,

manifest\_version TEXT,

manifest\_hash TEXT,

started\_at TEXT,

finished\_at TEXT,

tags\_json TEXT,

notes TEXT,

git\_sha TEXT,

platform\_json TEXT

);

CREATE TABLE IF NOT EXISTS artifacts (

id INTEGER PRIMARY KEY AUTOINCREMENT,

run\_id TEXT NOT NULL,

role TEXT NOT NULL,

path TEXT NOT NULL,

hash TEXT NOT NULL,

content\_type TEXT,

bytes INTEGER,

FOREIGN KEY (run\_id) REFERENCES runs(run\_id) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS metrics\_summary (

run\_id TEXT NOT NULL,

series TEXT NOT NULL,

count INTEGER NOT NULL,

min REAL,

max REAL,

mean REAL,

m2 REAL,

first\_step INTEGER,

last\_step INTEGER,

PRIMARY KEY (run\_id, series),

FOREIGN KEY (run\_id) REFERENCES runs(run\_id) ON DELETE CASCADE

);

CREATE INDEX IF NOT EXISTS idx\_runs\_status\_started ON runs(status,
started\_at);

CREATE INDEX IF NOT EXISTS idx\_runs\_engine ON runs(engine\_kind,
engine\_version);

CREATE INDEX IF NOT EXISTS idx\_artifacts\_run ON artifacts(run\_id);

\`;

### **packages-ts/store/src/db.ts**

import Database from \"better-sqlite3\";

import { SCHEMA\_SQL } from \"./schema.sql.js\";

export type Db = Database.Database;

export function openDb(dbPath: string): Db {

const db = new Database(dbPath, { timeout: 5000 }); // busy timeout at
the driver level too

db.pragma(\"journal\_mode = WAL\");

db.pragma(\"synchronous = NORMAL\");

db.pragma(\"foreign\_keys = ON\");

db.pragma(\"busy\_timeout = 5000\");

db.pragma(\"temp\_store = MEMORY\");

db.pragma(\"wal\_autocheckpoint = 1000\");

db.exec(SCHEMA\_SQL);

return db;

}

export function withTx\<T\>(db: Db, fn: () =\> T): T {

const tx = db.transaction(fn);

return tx();

}

### **packages-ts/store/src/hash.ts**

import { createHash } from \"node:crypto\";

import { createReadStream } from \"node:fs\";

export async function sha256File(filePath: string): Promise\<string\> {

const h = createHash(\"sha256\");

await new Promise\<void\>((resolve, reject) =\> {

const s = createReadStream(filePath);

s.on(\"data\", (d) =\> h.update(d));

s.on(\"error\", reject);

s.on(\"end\", () =\> resolve());

});

return \`sha256:\${h.digest(\"hex\")}\`;

}

### **packages-ts/store/src/blobStore.ts**

import { mkdir, access, copyFile, writeFile, rename } from
\"node:fs/promises\";

import path from \"node:path\";

import { randomUUID } from \"node:crypto\";

import { sha256File } from \"./hash.js\";

export class LocalBlobStore {

constructor(private root: string) {}

private blobPath(hash: string): string {

// hash format: sha256:\<hex\>

const hex = hash.slice(\"sha256:\".length);

const prefix = hex.slice(0, 2);

return path.join(this.root, \"blobs\", \"sha256\", prefix, hash);

}

async putFile(srcPath: string): Promise\<{ hash: string; bytes: number;
blobPath: string }\> {

const hash = await sha256File(srcPath);

const dst = this.blobPath(hash);

try {

await access(dst);

// already exists

} catch {

await mkdir(path.dirname(dst), { recursive: true });

const tmp = \`\${dst}.tmp.\${randomUUID()}\`;

await copyFile(srcPath, tmp);

await rename(tmp, dst);

}

const st = await (await import(\"node:fs/promises\")).stat(srcPath);

return { hash, bytes: st.size, blobPath: dst };

}

async putBytes(bytes: Uint8Array): Promise\<{ hash: string; bytes:
number; blobPath: string }\> {

const { createHash } = await import(\"node:crypto\");

const h = createHash(\"sha256\");

h.update(bytes);

const hash = \`sha256:\${h.digest(\"hex\")}\`;

const dst = this.blobPath(hash);

try {

await access(dst);

} catch {

await mkdir(path.dirname(dst), { recursive: true });

const tmp = \`\${dst}.tmp.\${randomUUID()}\`;

await writeFile(tmp, bytes);

await rename(tmp, dst);

}

return { hash, bytes: bytes.byteLength, blobPath: dst };

}

}

### **packages-ts/store/src/runStore.ts**

import path from \"node:path\";

import { mkdir, writeFile } from \"node:fs/promises\";

import type { Db } from \"./db.js\";

import { withTx } from \"./db.js\";

import { LocalBlobStore } from \"./blobStore.js\";

import { sha256File } from \"./hash.js\";

export class RunStore {

public blobs: LocalBlobStore;

constructor(

public db: Db,

public root: string

) {

this.blobs = new LocalBlobStore(root);

}

runDir(runId: string) {

return path.join(this.root, \"runs\", runId);

}

async initRun(runId: string): Promise\<{ runDir: string }\> {

const dir = this.runDir(runId);

await mkdir(dir, { recursive: true });

await mkdir(path.join(dir, \"logs\"), { recursive: true });

await mkdir(path.join(dir, \"reports\"), { recursive: true });

await mkdir(path.join(dir, \"links\"), { recursive: true });

return { runDir: dir };

}

async writeManifest(runId: string, manifest: unknown): Promise\<{
manifestPath: string; manifestHash: string }\> {

const dir = this.runDir(runId);

const manifestPath = path.join(dir, \"RunManifest.json\");

await writeFile(manifestPath, JSON.stringify(manifest, null, 2) +
\"\\n\", \"utf8\");

const manifestHash = await sha256File(manifestPath);

return { manifestPath, manifestHash };

}

insertRun(row: {

runId: string;

runKey: string;

status: string;

engineKind: string;

protocolVersion?: string;

manifestVersion?: string;

manifestHash?: string;

startedAt: string;

tagsJson?: string;

notes?: string;

}) {

withTx(this.db, () =\> {

this.db.prepare(\`

INSERT INTO runs (run\_id, run\_key, status, engine\_kind,
protocol\_version, manifest\_version, manifest\_hash, started\_at,
tags\_json, notes)

VALUES (\@runId, \@runKey, \@status, \@engineKind, \@protocolVersion,
\@manifestVersion, \@manifestHash, \@startedAt, \@tagsJson, \@notes)

\`).run(row);

});

}

updateRunStatus(runId: string, status: string, finishedAt?: string) {

withTx(this.db, () =\> {

this.db.prepare(\`UPDATE runs SET status = ?, finished\_at = COALESCE(?,
finished\_at) WHERE run\_id = ?\`)

.run(status, finishedAt ?? null, runId);

});

}

upsertMetricsSummary(runId: string, series: string, s: {

count: number; min?: number; max?: number; mean?: number; m2?: number;
first\_step?: number; last\_step?: number;

}) {

withTx(this.db, () =\> {

this.db.prepare(\`

INSERT INTO metrics\_summary (run\_id, series, count, min, max, mean,
m2, first\_step, last\_step)

VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

ON CONFLICT(run\_id, series) DO UPDATE SET

count=excluded.count, min=excluded.min, max=excluded.max,
mean=excluded.mean, m2=excluded.m2,

first\_step=excluded.first\_step, last\_step=excluded.last\_step

\`).run(runId, series, s.count, s.min ?? null, s.max ?? null, s.mean ??
null, s.m2 ?? null, s.first\_step ?? null, s.last\_step ?? null);

});

}

addArtifact(runId: string, a: { role: string; path: string; hash:
string; contentType?: string; bytes?: number }) {

withTx(this.db, () =\> {

this.db.prepare(\`

INSERT INTO artifacts (run\_id, role, path, hash, content\_type, bytes)

VALUES (?, ?, ?, ?, ?, ?)

\`).run(runId, a.role, a.path, a.hash, a.contentType ?? null, a.bytes ??
null);

});

}

}

### **packages-ts/store/src/index.ts**

export \* from \"./db.js\";

export \* from \"./blobStore.js\";

export \* from \"./runStore.js\";

export \* from \"./hash.js\";

**3) Minimal qcalc run skeleton: schemas + store + subprocess adapter + metrics ingestion**
===========================================================================================

This is a runnable "thin vertical slice":

-   validate + resolve manifest

-   create run in store

-   spawn python engine runner

-   tail metrics.jsonl and update online stats

-   read ArtifactIndex.json and index artifacts

**packages-ts/runner dependencies**
-----------------------------------

Add:

-   \@qcalc/schemas (already)

-   \@qcalc/store

-   (optional) none else

### **packages-ts/runner/src/util/stableJson.ts**

export function stableStringify(x: any): string {

if (x === null \|\| typeof x !== \"object\") return JSON.stringify(x);

if (Array.isArray(x)) return
\`\[\${x.map(stableStringify).join(\",\")}\]\`;

const keys = Object.keys(x).sort();

return \`{\${keys.map(k =\> JSON.stringify(k) + \":\" +
stableStringify(x\[k\])).join(\",\")}}\`;

}

### **packages-ts/runner/src/util/hash.ts**

import { createHash } from \"node:crypto\";

export function sha256Text(s: string): string {

return \"sha256:\" + createHash(\"sha256\").update(s,
\"utf8\").digest(\"hex\");

}

### **packages-ts/runner/src/metrics/onlineStats.ts**

export type Online = { count: number; mean: number; m2: number; min:
number; max: number; firstStep: number; lastStep: number };

export function updateOnline(s: Online \| undefined, step: number,
value: number): Online {

if (!Number.isFinite(value)) return s ?? {

count: 0, mean: 0, m2: 0, min: Infinity, max: -Infinity, firstStep:
step, lastStep: step

};

if (!s) {

return { count: 1, mean: value, m2: 0, min: value, max: value,
firstStep: step, lastStep: step };

}

const count = s.count + 1;

const delta = value - s.mean;

const mean = s.mean + delta / count;

const delta2 = value - mean;

const m2 = s.m2 + delta \* delta2;

return {

count,

mean,

m2,

min: Math.min(s.min, value),

max: Math.max(s.max, value),

firstStep: Math.min(s.firstStep, step),

lastStep: Math.max(s.lastStep, step),

};

}

### **packages-ts/runner/src/metrics/tailJsonl.ts**

import { open } from \"node:fs/promises\";

export async function tailJsonl(

filePath: string,

onLine: (line: string) =\> Promise\<void\> \| void,

opts: { pollMs?: number; stopWhen?: () =\> boolean } = {}

) {

const pollMs = opts.pollMs ?? 200;

let pos = 0;

let buffer = \"\";

while (!opts.stopWhen?.()) {

try {

const fh = await open(filePath, \"r\");

const st = await fh.stat();

if (st.size \> pos) {

const len = st.size - pos;

const b = Buffer.alloc(len);

await fh.read(b, 0, len, pos);

pos = st.size;

buffer += b.toString(\"utf8\");

let idx: number;

while ((idx = buffer.indexOf(\"\\n\")) \>= 0) {

const line = buffer.slice(0, idx).trim();

buffer = buffer.slice(idx + 1);

if (line) await onLine(line);

}

}

await fh.close();

} catch {

// file may not exist yet; ignore

}

await new Promise((r) =\> setTimeout(r, pollMs));

}

}

### **packages-ts/runner/src/engine/pythonSubprocess.ts**

import { spawn } from \"node:child\_process\";

import path from \"node:path\";

export async function runPythonSubprocess(runDir: string):
Promise\<number\> {

const manifestPath = path.join(runDir, \"RunManifest.json\");

const env = {

\...process.env,

PYTHONPATH: \[

process.cwd(),

path.join(process.cwd(), \"packages\"),

path.join(process.cwd(), \"packages/core\"),

\].join(path.delimiter),

};

return await new Promise\<number\>((resolve, reject) =\> {

const p = spawn(

\"python\",

\[\"-m\", \"scripts.qari\_engine\_run\", \"\--manifest\", manifestPath,
\"\--out\", runDir\],

{ stdio: \[\"ignore\", \"inherit\", \"pipe\"\], env }

);

p.stderr?.on(\"data\", (d) =\> process.stderr.write(d));

p.on(\"error\", reject);

p.on(\"close\", (code) =\> resolve(code ?? 1));

});

}

### **packages-ts/runner/src/commands/run.ts**

import path from \"node:path\";

import { readFile } from \"node:fs/promises\";

import { randomUUID } from \"node:crypto\";

import { openDb, RunStore } from \"\@qcalc/store\";

import { RunManifestSchema, MetricEvent, ArtifactIndex as
ArtifactIndexSchema } from \"\@qcalc/schemas\";

import { resolveRunManifestFromQariYaml } from
\"\@qcalc/schemas/fromQariYaml.js\";

import { stableStringify } from \"../util/stableJson.js\";

import { sha256Text } from \"../util/hash.js\";

import { runPythonSubprocess } from \"../engine/pythonSubprocess.js\";

import { tailJsonl } from \"../metrics/tailJsonl.js\";

import { updateOnline, type Online } from \"../metrics/onlineStats.js\";

export type RunArgs = {

manifestPath: string;

qariYaml?: string;

storeDir?: string;

};

export async function cmdRun(args: RunArgs) {

const storeRoot = args.storeDir ?? path.join(process.cwd(),
\".qcalc-store\");

const db = openDb(path.join(storeRoot, \"db.sqlite\"));

const store = new RunStore(db, storeRoot);

const baseRaw = await readFile(args.manifestPath, \"utf8\");

const base = JSON.parse(baseRaw);

// Resolve manifest (YAML fills gaps if provided)

const resolved = args.qariYaml

? await resolveRunManifestFromQariYaml({

qariYamlPath: args.qariYaml,

baseManifest: base,

autoFillIds: true,

mergeMode: \"fill-missing\",

})

: RunManifestSchema.parse({ \...base, runId: base.runId ?? randomUUID(),
createdAt: base.createdAt ?? new Date().toISOString() });

const runId = resolved.runId!;

await store.initRun(runId);

// Canonical manifest snapshot

const { manifestPath, manifestHash } = await store.writeManifest(runId,
resolved);

// runKey = sha256(stable manifest without volatile fields)

const { runId: \_rid, createdAt: \_ca, \...stableCore } = resolved as
any;

const runKey = sha256Text(stableStringify(stableCore));

store.insertRun({

runId,

runKey,

status: \"running\",

engineKind: resolved.engine.kind,

protocolVersion: (resolved.engine as any).protocolVersion,

manifestVersion: resolved.manifestVersion,

manifestHash,

startedAt: new Date().toISOString(),

tagsJson: JSON.stringify(resolved.tags ?? {}),

notes: resolved.notes,

});

// Metrics ingestion (tail file while python runs)

const metricsPath = path.join(store.runDir(runId), \"metrics.jsonl\");

const stats: Record\<string, Online \| undefined\> = {};

let pythonDone = false;

const stopWhen = () =\> pythonDone;

const tailer = tailJsonl(metricsPath, async (line) =\> {

const evt = MetricEvent.parse(JSON.parse(line));

const step = evt.step;

// update selected series if present

for (const k of \[\"q\", \"gapLB\", \"slopeUB\", \"loss\", \"energy\",
\"drift\", \"margin\"\] as const) {

const v = (evt as any)\[k\];

if (typeof v === \"number\") stats\[k\] = updateOnline(stats\[k\], step,
v);

}

}, { stopWhen, pollMs: 200 });

// Run engine

const code = await runPythonSubprocess(store.runDir(runId));

pythonDone = true;

await tailer; // let tail loop exit cleanly

// Read ArtifactIndex

const artifactIndexPath = path.join(store.runDir(runId),
\"ArtifactIndex.json\");

const idxRaw = await readFile(artifactIndexPath, \"utf8\");

const artifactIndex = ArtifactIndexSchema.parse(JSON.parse(idxRaw));

// Index artifacts & blobs (minimal: manifest + metrics + artifact index
itself)

// You can extend this to all files listed in ArtifactIndex.

const blobMetrics = await store.blobs.putFile(metricsPath).catch(() =\>
null);

if (blobMetrics) {

store.addArtifact(runId, { role: \"metrics\", path: \"metrics.jsonl\",
hash: blobMetrics.hash, contentType: \"application/x-ndjson\", bytes:
blobMetrics.bytes });

}

// Manifest already hashed; store it too as an artifact row

store.addArtifact(runId, { role: \"manifest\", path:
\"RunManifest.json\", hash: manifestHash, contentType:
\"application/json\" });

// ArtifactIndex as artifact

const idxBlob = await store.blobs.putFile(artifactIndexPath);

store.addArtifact(runId, { role: \"other\", path:
\"ArtifactIndex.json\", hash: idxBlob.hash, contentType:
\"application/json\", bytes: idxBlob.bytes });

// Flush metrics summary to sqlite (single write batch)

for (const \[series, s\] of Object.entries(stats)) {

if (!s) continue;

store.upsertMetricsSummary(runId, series, {

count: s.count,

min: Number.isFinite(s.min) ? s.min : undefined,

max: Number.isFinite(s.max) ? s.max : undefined,

mean: s.mean,

m2: s.m2,

first\_step: s.firstStep,

last\_step: s.lastStep,

});

}

// Update run status

store.updateRunStatus(runId, artifactIndex.status ?? (code === 0 ?
\"succeeded\" : \"failed\"), new Date().toISOString());

console.log(JSON.stringify({ runId, status: artifactIndex.status ??
(code === 0 ? \"succeeded\" : \"failed\") }, null, 2));

}

### **packages-ts/runner/src/cli.ts**

\#!/usr/bin/env node

import { cmdRun } from \"./commands/run.js\";

function parse(argv: string\[\]) {

const out: any = {};

for (let i = 0; i \< argv.length; i++) {

const a = argv\[i\]!;

const \[k, vEq\] = a.includes(\"=\") ? a.split(\"=\", 2) : \[a,
undefined\];

const next = () =\> (vEq ?? argv\[++i\]);

if (k === \"run\") out.cmd = \"run\";

else if (k === \"\--manifest\") out.manifestPath = next();

else if (k === \"\--qari-yaml\") out.qariYaml = next();

else if (k === \"\--store\") out.storeDir = next();

else if (k === \"\--help\" \|\| k === \"-h\") out.help = true;

}

return out;

}

const args = parse(process.argv.slice(2));

if (args.help \|\| !args.cmd) {

console.log(\`Usage:

qcalc run \--manifest RunManifest.json \[\--qari-yaml
configs/qari.yaml\] \[\--store .qcalc-store\]

\`);

process.exit(args.cmd ? 0 : 2);

}

if (args.cmd === \"run\") {

if (!args.manifestPath) throw new Error(\"\--manifest is required\");

await cmdRun(args);

}

**Notes on concurrency + DB updates**
-------------------------------------

The skeleton above is intentionally "sqlite-friendly":

-   writes a small run row at start

-   tails metrics but **does not write per event**

-   writes summaries once at the end

That's the core trick that avoids lock contention when you later do
sweep \--jobs N (still one orchestrator process writing sqlite).

Below is a **minimal but solid** qcalc sweep skeleton that:

-   expands a SweepSpec.json deterministically

-   runs **N Python subprocess runs concurrently\
    > **

-   keeps SQLite writes **serialized (single-writer)** in the
    > *orchestrator process\
    > *

-   supports \--resume by skipping runs already completed (via runs
    > table **and/or** runs/\<runId\>/ArtifactIndex.json)

This assumes you already have:

-   \@qcalc/schemas (RunManifest + SweepSpec + MetricEvent +
    > ArtifactIndex)

-   \@qcalc/store (RunStore + openDb)

-   the python subprocess engine (python -m scripts.qari\_engine\_run
    > \...) from Phase 2

-   cmdRun exists (but we won't call it; we inline the core to avoid
    > multiple DB opens)

**1) packages-ts/runner/src/commands/sweep.ts**
===============================================

import path from \"node:path\";

import { readFile } from \"node:fs/promises\";

import { existsSync } from \"node:fs\";

import { openDb, RunStore } from \"\@qcalc/store\";

import { SweepSpec, RunManifestSchema, MetricEvent, ArtifactIndex as
ArtifactIndexSchema } from \"\@qcalc/schemas\";

import { stableStringify } from \"../util/stableJson.js\";

import { sha256Text } from \"../util/hash.js\";

import { runPythonSubprocess } from \"../engine/pythonSubprocess.js\";

import { tailJsonl } from \"../metrics/tailJsonl.js\";

import { updateOnline, type Online } from \"../metrics/onlineStats.js\";

/\*\* Serialize DB writes even though we\'re single-process (keeps logic
clean). \*/

function createDbWriter() {

let chain = Promise.resolve();

return async \<T\>(fn: () =\> T \| Promise\<T\>): Promise\<T\> =\> {

const next = chain.then(fn, fn);

// keep chain alive even if a write fails

chain = next.then(() =\> undefined, () =\> undefined);

return next;

};

}

type AxisValue = { path: string; value: unknown };

type RunPlan = { ordinal: number; axisValues: AxisValue\[\]; manifest:
any; runKey: string; runId: string };

function parsePath(p: string): string\[\] {

if (p.startsWith(\"/\")) {

return p

.split(\"/\")

.slice(1)

.map((s) =\> s.replace(/\~1/g, \"/\").replace(/\~0/g, \"\~\"))

.filter(Boolean);

}

return p.split(\".\").filter(Boolean);

}

function setAtPath(obj: any, p: string, value: unknown): any {

const segs = parsePath(p);

if (segs.length === 0) return obj;

const root = (obj && typeof obj === \"object\" && !Array.isArray(obj)) ?
{ \...obj } : {};

let cur: any = root;

for (let i = 0; i \< segs.length; i++) {

const key = segs\[i\]!;

const last = i === segs.length - 1;

if (last) {

cur\[key\] = value;

} else {

const next = cur\[key\];

cur\[key\] = (next && typeof next === \"object\" &&
!Array.isArray(next)) ? { \...next } : {};

cur = cur\[key\];

}

}

return root;

}

function normalizeAxes(spec: any) {

const axes = Array.isArray(spec.axes) ? spec.axes.slice() : \[\];

// deterministic ordering: sort by path

axes.sort((a: any, b: any) =\>
String(a.path).localeCompare(String(b.path)));

// values order stays as given

return axes;

}

function expandSweep(specObj: any): RunPlan\[\] {

const spec = SweepSpec.parse(specObj);

const axes = normalizeAxes(spec);

const base = spec.baseManifest; // object (per your schema)

const policy = spec.policy ?? \"cartesian\";

// Build all axis assignments deterministically

let assignments: AxisValue\[\]\[\] = \[\];

if (axes.length === 0) {

assignments = \[\[\]\];

} else if (policy === \"zip\") {

const minLen = Math.min(\...axes.map((a: any) =\> a.values.length));

assignments = Array.from({ length: minLen }, (\_, i) =\>

axes.map((a: any) =\> ({ path: a.path, value: a.values\[i\] }))

);

} else {

// cartesian

assignments = \[\[\]\];

for (const a of axes) {

const next: AxisValue\[\]\[\] = \[\];

for (const prev of assignments) {

for (const v of a.values) {

next.push(\[\...prev, { path: a.path, value: v }\]);

}

}

assignments = next;

}

}

// Materialize manifests + stable run keys

const plans: RunPlan\[\] = assignments.map((axisValues, ordinal) =\> {

let m: any = base;

for (const av of axisValues) m = setAtPath(m, av.path, av.value);

// tags: record axis values for querying

const axisTags: Record\<string, string\> = {};

for (const av of axisValues) axisTags\[\`axis:\${av.path}\`\] =
JSON.stringify(av.value);

m = setAtPath(m, \"tags\", { \...(m.tags ?? {}), \...axisTags });

// validate shape (will still be resolved w/ ids later)

const validated = RunManifestSchema.parse(m);

// runKey from stable manifest WITHOUT runId/createdAt (canonical
identity)

const { runId: \_rid, createdAt: \_ca, \...stableCore } = validated as
any;

const runKey = sha256Text(stableStringify(stableCore));

const hex = runKey.slice(\"sha256:\".length);

const runId = \`r\_\${hex.slice(0, 24)}\`; // deterministic runId for
resume

// enforce deterministic runId in manifest:

const withIds = RunManifestSchema.parse({

\...validated,

runId,

createdAt: new Date().toISOString(),

});

return { ordinal, axisValues, manifest: withIds, runKey, runId };

});

return plans;

}

function readArtifactIndexStatus(runDir: string): { ok: boolean;
status?: string } {

const p = path.join(runDir, \"ArtifactIndex.json\");

if (!existsSync(p)) return { ok: false };

try {

const raw = require(\"node:fs\").readFileSync(p, \"utf8\");

const idx = ArtifactIndexSchema.parse(JSON.parse(raw));

return { ok: true, status: idx.status };

} catch {

return { ok: false };

}

}

/\*\*

\* Resume rule (minimal):

\* - if runDir exists AND ArtifactIndex says succeeded =\> skip

\* - else if DB says succeeded =\> skip (even if file missing)

\*/

function shouldSkipRun(store: RunStore, runId: string, runKey: string,
resume: boolean): boolean {

if (!resume) return false;

const runDir = store.runDir(runId);

// Folder-level truth (best)

const ai = readArtifactIndexStatus(runDir);

if (ai.ok && ai.status === \"succeeded\") return true;

// DB-level truth

const row = store.db.prepare(\`SELECT status FROM runs WHERE run\_id = ?
OR run\_key = ? LIMIT 1\`).get(runId, runKey) as any;

if (row?.status === \"succeeded\") return true;

return false;

}

/\*\* One run execution: filesystem + python + metrics tail + DB updates
(DB updates go through writer queue). \*/

async function runOne(plan: RunPlan, store: RunStore, dbWrite:
ReturnType\<typeof createDbWriter\>) {

const { runId, runKey, manifest } = plan;

await store.initRun(runId);

const runDir = store.runDir(runId);

// Write manifest snapshot

const { manifestHash } = await store.writeManifest(runId, manifest);

// Insert run row (serialized)

await dbWrite(() =\> {

store.insertRun({

runId,

runKey,

status: \"running\",

engineKind: manifest.engine.kind,

protocolVersion: (manifest.engine as any).protocolVersion,

manifestVersion: manifest.manifestVersion,

manifestHash,

startedAt: new Date().toISOString(),

tagsJson: JSON.stringify(manifest.tags ?? {}),

notes: manifest.notes,

});

});

// Metrics tailer (in-memory stats)

const metricsPath = path.join(runDir, \"metrics.jsonl\");

const stats: Record\<string, Online \| undefined\> = {};

let done = false;

const tailer = tailJsonl(

metricsPath,

async (line) =\> {

const evt = MetricEvent.parse(JSON.parse(line));

const step = evt.step;

for (const k of \[\"q\", \"gapLB\", \"slopeUB\", \"loss\", \"energy\",
\"drift\", \"margin\"\] as const) {

const v = (evt as any)\[k\];

if (typeof v === \"number\") stats\[k\] = updateOnline(stats\[k\], step,
v);

}

},

{ stopWhen: () =\> done, pollMs: 200 }

);

// Run Python

const code = await runPythonSubprocess(runDir);

done = true;

await tailer;

// Read ArtifactIndex (required)

const idxPath = path.join(runDir, \"ArtifactIndex.json\");

const idxRaw = await readFile(idxPath, \"utf8\");

const artifactIndex = ArtifactIndexSchema.parse(JSON.parse(idxRaw));

// Serialize DB updates (single-writer)

await dbWrite(() =\> {

// artifacts: store manifest + metrics + artifact index hashes (minimal)

store.addArtifact(runId, { role: \"manifest\", path:
\"RunManifest.json\", hash: manifestHash, contentType:
\"application/json\" });

if (existsSync(metricsPath)) {

// hash metrics as artifact (blob store optional; here we just record
hash)

// If you want dedup blobs: store.blobs.putFile(metricsPath) outside the
tx, then addArtifact with that hash/bytes.

// Minimal: just compute and store hash later---keeping this skeleton
light.

}

// metrics summaries

for (const \[series, s\] of Object.entries(stats)) {

if (!s) continue;

store.upsertMetricsSummary(runId, series, {

count: s.count,

min: Number.isFinite(s.min) ? s.min : undefined,

max: Number.isFinite(s.max) ? s.max : undefined,

mean: s.mean,

m2: s.m2,

first\_step: s.firstStep,

last\_step: s.lastStep,

});

}

store.updateRunStatus(

runId,

artifactIndex.status ?? (code === 0 ? \"succeeded\" : \"failed\"),

new Date().toISOString()

);

});

return { runId, status: artifactIndex.status ?? (code === 0 ?
\"succeeded\" : \"failed\") };

}

/\*\* Simple worker pool without external deps \*/

async function runPool\<T, R\>(

items: T\[\],

jobs: number,

worker: (item: T) =\> Promise\<R\>

): Promise\<R\[\]\> {

const results: R\[\] = \[\];

let i = 0;

const runners = Array.from({ length: Math.max(1, jobs) }, async () =\> {

while (true) {

const idx = i++;

if (idx \>= items.length) break;

results\[idx\] = await worker(items\[idx\]!);

}

});

await Promise.all(runners);

return results;

}

export type SweepArgs = {

sweepPath: string;

storeDir?: string;

jobs?: number;

resume?: boolean;

};

export async function cmdSweep(args: SweepArgs) {

const storeRoot = args.storeDir ?? path.join(process.cwd(),
\".qcalc-store\");

const db = openDb(path.join(storeRoot, \"db.sqlite\"));

const store = new RunStore(db, storeRoot);

const dbWrite = createDbWriter();

const sweepRaw = await readFile(args.sweepPath, \"utf8\");

const sweepObj = JSON.parse(sweepRaw);

const plansAll = expandSweep(sweepObj);

// Resume filtering

const plans = plansAll.filter((p) =\> !shouldSkipRun(store, p.runId,
p.runKey, Boolean(args.resume)));

console.log(

JSON.stringify(

{

sweep: path.basename(args.sweepPath),

total: plansAll.length,

scheduled: plans.length,

skipped: plansAll.length - plans.length,

jobs: args.jobs ?? 1,

resume: Boolean(args.resume),

},

null,

2

)

);

const jobs = args.jobs ?? 1;

const results = await runPool(plans, jobs, async (plan) =\> {

try {

return await runOne(plan, store, dbWrite);

} catch (e: any) {

// best effort: mark failed

await dbWrite(() =\> store.updateRunStatus(plan.runId, \"failed\", new
Date().toISOString()));

return { runId: plan.runId, status: \"failed\", error: e?.message ??
String(e) } as any;

}

});

const counts = results.reduce(

(acc: any, r: any) =\> {

acc.total++;

acc\[r.status\] = (acc\[r.status\] ?? 0) + 1;

return acc;

},

{ total: 0 }

);

console.log(JSON.stringify({ completed: results.length, counts }, null,
2));

}

**2) Wire into CLI: packages-ts/runner/src/cli.ts**
===================================================

Add parsing for sweep:

import { cmdRun } from \"./commands/run.js\";

import { cmdSweep } from \"./commands/sweep.js\";

function parse(argv: string\[\]) {

const out: any = {};

for (let i = 0; i \< argv.length; i++) {

const a = argv\[i\]!;

const \[k, vEq\] = a.includes(\"=\") ? a.split(\"=\", 2) : \[a,
undefined\];

const next = () =\> (vEq ?? argv\[++i\]);

if (k === \"run\") out.cmd = \"run\";

else if (k === \"sweep\") out.cmd = \"sweep\";

else if (k === \"\--manifest\") out.manifestPath = next();

else if (k === \"\--sweep\") out.sweepPath = next();

else if (k === \"\--store\") out.storeDir = next();

else if (k === \"\--jobs\") out.jobs = Number(next());

else if (k === \"\--resume\") out.resume = true;

else if (k === \"\--help\" \|\| k === \"-h\") out.help = true;

}

return out;

}

const args = parse(process.argv.slice(2));

if (args.help \|\| !args.cmd) {

console.log(\`Usage:

qcalc run \--manifest RunManifest.json \[\--store .qcalc-store\]

qcalc sweep \--sweep SweepSpec.json \[\--jobs 4\] \[\--resume\]
\[\--store .qcalc-store\]

\`);

process.exit(args.cmd ? 0 : 2);

}

if (args.cmd === \"run\") {

if (!args.manifestPath) throw new Error(\"\--manifest is required\");

await cmdRun(args);

}

if (args.cmd === \"sweep\") {

if (!args.sweepPath) throw new Error(\"\--sweep is required\");

await cmdSweep(args);

}

**3) How \--resume works (minimal, robust)**
============================================

A run is skipped if:

-   runs/\<runId\>/ArtifactIndex.json exists and says status:
    > \"succeeded\", **or\
    > **

-   sqlite runs table has status=\"succeeded\" for either run\_id or
    > run\_key

Because runId is deterministic from runKey in this skeleton, resume
works even if:

-   the previous sweep crashed mid-way

-   sqlite exists but run folder is partially there

-   run folder exists but sqlite row is missing

**4) Why this keeps SQLite "single-writer"**
============================================

-   Only the orchestrator process opens sqlite and writes to it.

-   Python subprocesses write to files only.

-   Writes are routed through dbWrite(() =\> \...) which serializes
    > logical write phases.

-   No per-metric-point DB writes (only end-of-run summaries).
