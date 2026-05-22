---
slug: phase-4
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/Phase 4.md
  last_synced: '2026-03-20T17:17:15.264240Z'
---

Here's a concrete Phase 4 that turns the existing Vite/shadcn dashboard
(Q-Calculator-Multiplicity/frontend/) into a **lab console** powered by
the TS control plane---**UI talks only to a TS "orchestrator API"**,
which in turn talks to sqlite + run folders + (optionally) engines.

**1) Add a TS Orchestrator API (UI never touches sqlite directly)**
-------------------------------------------------------------------

### **New package**

packages-ts/

orchestrator/

src/

server.ts

routes/

runs.ts

metrics.ts

compare.ts

bundles.ts

services/

store.ts

metricsTail.ts

compare.ts

bundleZip.ts

### **Implementation choice**

Use **Fastify** (lean, easy streaming) + **SSE** for live metrics
(simpler than WS, works great with Vite).

Key: Orchestrator is the **single sqlite writer** (same Phase 3 story).

### **API surface (v1)**

**Runs**

-   GET
    > /v1/runs?status=&engine\_kind=&tag=axis:budgets.epsilon&limit=&offset=

-   GET /v1/runs/:runId

-   GET /v1/runs/:runId/artifacts

-   GET /v1/runs/:runId/blobs (from run\_blobs table)

**Metrics**

-   GET /v1/runs/:runId/metrics/summary (from metrics\_summary)

-   GET /v1/runs/:runId/metrics/tail?fromByteOffset= (polling fallback)

-   GET /v1/runs/:runId/metrics/stream (SSE: emits parsed MetricEvent
    > lines)

**Compare**

-   POST /v1/compare body: { aRunId, bRunId, metrics:
    > \[\"q\",\"gapLB\"\], window?: {start,end} }

    -   returns: { summary, series?: downsampled }

**Evidence bundle**

-   GET /v1/runs/:runId/bundle.zip (streams zip)

    -   includes: RunManifest.json, ArtifactIndex.json,
        > metrics\_summary.json, metrics.jsonl (optional),
        > run\_blobs.json, provenance.json (if present)

> This keeps the UI thin: it fetches "views" from the orchestrator, not
> raw files.

### **Dev wiring (frontend → orchestrator)**

Add in frontend/vite.config.ts:

-   proxy /qcalc-api → http://localhost:8787

So UI calls /qcalc-api/v1/\... without CORS pain.

**2) Frontend: add an API client layer + react-query hooks**
------------------------------------------------------------

Your existing frontend already uses \@tanstack/react-query and
react-router, so do this:

### **New UI client files**

frontend/src/

lib/qcalc/

client.ts \# fetch wrapper + base URL + Zod validation

types.ts \# reuse \@qcalc/schemas types where possible

hooks/

useRuns.ts

useRunDetails.ts

useMetricStream.ts

useCompare.ts

### **Fetch wrapper (pattern)**

-   centralize base URL: import.meta.env.VITE\_QCALC\_API\_BASE ??
    > \"/qcalc-api\"

-   validate responses with Zod (from \@qcalc/schemas), so the UI never
    > silently drifts.

**3) UI feature 1: Run browser**
--------------------------------

### **Page behavior**

-   Table/grid of runs with:

    -   runId, status, engine\_kind, started/finished, key tags, quick
        > metrics (mean drift / final q)

-   Filters:

    -   status, engine\_kind, tag search (including axis:\*), time range

-   Click run → run detail

### **Backend support**

Orchestrator query:

-   runs table for rows

-   metrics\_summary for quick columns (join or separate endpoint)

-   optional: return "denormalized" rows to keep UI fast

**4) UI feature 2: Live metrics chart**
---------------------------------------

### **Preferred approach: SSE**

UI opens EventSource(\"/qcalc-api/v1/runs/:runId/metrics/stream\")

Orchestrator:

-   tails runs/\<runId\>/metrics.jsonl

-   for each new line:

    -   parse JSON (validate with MetricEvent)

    -   res.write(\"data: \<json\>\\n\\n\")

UI:

-   maintains an in-memory series buffer (e.g. last 2--10k points)

-   renders chart (Recharts is fine; you can downsample client-side
    > later)

Fallback (if SSE not available):

-   GET /metrics/tail?fromByteOffset= polling

**Important:** do not plot raw arrays from Python in UI initially; just
plot MetricEvent scalars.

**5) UI feature 3: Compare runs overlay**
-----------------------------------------

### **UX (minimal)**

-   On run detail page: "Compare..." button

-   choose another run from a dropdown/search (runId)

-   call POST /v1/compare

-   show:

    -   overlay plot (a vs b)

    -   delta plot

    -   summary card: mean abs delta, max abs delta, pass/fail
        > thresholds

### **Backend compare implementation**

-   read metrics.jsonl for both runs (or precomputed downsample)

-   align by step

-   compute summary stats + return optionally downsampled series

This keeps the "compare logic" authoritative and consistent for
CI/regression too.

**6) UI feature 4: Export evidence bundle**
-------------------------------------------

Button on run detail:

-   GET /v1/runs/:runId/bundle.zip

-   browser download stream

Bundle contents (minimum):

-   RunManifest.json

-   ArtifactIndex.json

-   metrics\_summary.json (generated from sqlite)

-   run\_blobs.json (from run\_blobs)

-   optionally metrics.jsonl (toggleable if huge)

This becomes your "send to reviewer / auditor / collaborator" artifact.

**7) Keep the Gemini "bring-to-life" app as optional tool later**
-----------------------------------------------------------------

When you're ready:

-   mount it as a route in the main dashboard: /tools/bring-to-life

-   treat generated HTML/ZIP as a normal artifact:

    -   store via blob store

    -   attach to a "tool run" row in sqlite (same indexing)

-   don't merge dependency stacks until you align Vite/React versions;
    > easiest is embedding it via iframe or porting the minimal
    > components.

**Minimal Phase 4 milestones (practical order)**
------------------------------------------------

1.  **Orchestrator v1**: GET /runs, GET /runs/:id, GET
    > /metrics\_summary, GET /metrics/stream

2.  **Runs page** wired to sqlite

3.  **Run detail** with live chart (SSE)

4.  **Compare** endpoint + UI overlay

5.  **Evidence bundle** download

If you want, I can sketch the **Fastify orchestrator server** (routes +
SSE tailer) in \~1--2 files so you can drop it into
packages-ts/orchestrator and immediately point the existing dashboard at
/qcalc-api.

Below are two drop-in files for packages-ts/orchestrator/src/:

server.ts (Fastify app + routes)

sseTail.ts (JSONL tail → SSE)

They assume:

your local store lives at .qcalc-store/ (same layout you designed)

sqlite is at .qcalc-store/db.sqlite

runs are at .qcalc-store/runs/\<runId\>/\...

They also default to serving under /qcalc-api, so your dashboard can
call /qcalc-api/v1/\... immediately.

packages-ts/orchestrator/src/sseTail.ts

import { open } from \"node:fs/promises\";

import { existsSync } from \"node:fs\";

type TailSseOpts = {

filePath: string;

pollMs?: number;

heartbeatMs?: number;

fromByteOffset?: number;

/\*\*

\* Called per parsed line; return null to skip emitting.

\* Throwing will emit an error event and continue.

\*/

mapLine?: (line: string) =\> any \| null;

};

function sleep(ms: number) {

return new Promise((r) =\> setTimeout(r, ms));

}

function writeSse(res: NodeJS.WritableStream, event: string, data: any)
{

res.write(\`event: \${event}\\n\`);

res.write(\`data: \${JSON.stringify(data)}\\n\\n\`);

}

export async function tailJsonlAsSse(

req: { raw: NodeJS.ReadableStream & { on: any } },

reply: { raw: NodeJS.WritableStream; headers: (h: any) =\> any; code:
(c: number) =\> any },

opts: TailSseOpts

) {

const pollMs = opts.pollMs ?? 250;

const heartbeatMs = opts.heartbeatMs ?? 15000;

let pos = Math.max(0, opts.fromByteOffset ?? 0);

let buffer = \"\";

let closed = false;

let lastHeartbeat = Date.now();

// SSE headers

reply

.code(200)

.headers({

\"content-type\": \"text/event-stream; charset=utf-8\",

\"cache-control\": \"no-cache, no-transform\",

connection: \"keep-alive\",

\"x-accel-buffering\": \"no\",

});

// Close handling

req.raw.on(\"close\", () =\> {

closed = true;

});

req.raw.on(\"end\", () =\> {

closed = true;

});

// initial hello

writeSse(reply.raw, \"hello\", { file: opts.filePath, fromByteOffset:
pos });

while (!closed) {

// Heartbeat (keeps proxies from killing stream)

if (Date.now() - lastHeartbeat \>= heartbeatMs) {

reply.raw.write(\`: heartbeat \${new Date().toISOString()}\\n\\n\`);

lastHeartbeat = Date.now();

}

// File may not exist yet

if (!existsSync(opts.filePath)) {

await sleep(pollMs);

continue;

}

try {

const fh = await open(opts.filePath, \"r\");

const st = await fh.stat();

if (st.size \> pos) {

const len = st.size - pos;

// Read new bytes

const b = Buffer.alloc(len);

await fh.read(b, 0, len, pos);

pos = st.size;

buffer += b.toString(\"utf8\");

// Emit complete lines only

let idx: number;

while ((idx = buffer.indexOf(\"\\n\")) \>= 0) {

const line = buffer.slice(0, idx).trim();

buffer = buffer.slice(idx + 1);

if (!line) continue;

try {

const mapped = opts.mapLine ? opts.mapLine(line) : JSON.parse(line);

if (mapped !== null) {

writeSse(reply.raw, \"metric\", { offset: pos, event: mapped });

}

} catch (e: any) {

writeSse(reply.raw, \"error\", {

message: e?.message ?? String(e),

linePreview: line.slice(0, 240),

});

}

}

}

await fh.close();

} catch (e: any) {

writeSse(reply.raw, \"error\", { message: e?.message ?? String(e) });

}

await sleep(pollMs);

}

}

packages-ts/orchestrator/src/server.ts

import Fastify from \"fastify\";

import cors from \"\@fastify/cors\";

import path from \"node:path\";

import { readFileSync } from \"node:fs\";

import { openDb, RunStore } from \"\@qcalc/store\";

import { MetricEvent } from \"\@qcalc/schemas\";

import { tailJsonlAsSse } from \"./sseTail.js\";

type Env = {

PORT?: string;

HOST?: string;

QCALC\_STORE\_DIR?: string; // default: .qcalc-store

QCALC\_API\_PREFIX?: string; // default: /qcalc-api

};

function num(v: any, d: number) {

const n = Number(v);

return Number.isFinite(n) ? n : d;

}

function safeJsonParse(s: string) {

try { return JSON.parse(s); } catch { return null; }

}

async function main() {

const env = process.env as Env;

const port = num(env.PORT, 8787);

const host = env.HOST ?? \"127.0.0.1\";

const storeRoot = env.QCALC\_STORE\_DIR ?? path.join(process.cwd(),
\".qcalc-store\");

const apiPrefix = env.QCALC\_API\_PREFIX ?? \"/qcalc-api\";

const db = openDb(path.join(storeRoot, \"db.sqlite\"));

const store = new RunStore(db, storeRoot);

const app = Fastify({ logger: true });

// If you proxy via Vite, CORS isn\'t required. But harmless for local
multi-origin dev.

await app.register(cors, { origin: true });

// Health

app.get(\`\${apiPrefix}/health\`, async () =\> ({ ok: true, storeRoot
}));

// \-\-\-- Runs list \-\-\--

app.get(\`\${apiPrefix}/v1/runs\`, async (req, reply) =\> {

const q = (req.query as any) ?? {};

const limit = Math.min(200, Math.max(1, num(q.limit, 50)));

const offset = Math.max(0, num(q.offset, 0));

const status = typeof q.status === \"string\" ? q.status : undefined;

const engineKind = typeof q.engine\_kind === \"string\" ? q.engine\_kind
: undefined;

// tag filter: repeated ?tag=axis:budgets.epsilon:\"0.05\" or
?tag=experiment:baseline

const tags = (\[\] as string\[\]).concat(q.tag ?? \[\]).filter((x) =\>
typeof x === \"string\");

// Minimal tag filtering: LIKE on tags\_json. (Works fine for early
phase.)

const where: string\[\] = \[\];

const params: any\[\] = \[\];

if (status) { where.push(\"r.status = ?\"); params.push(status); }

if (engineKind) { where.push(\"r.engine\_kind = ?\");
params.push(engineKind); }

for (const t of tags) {

// match \`\"key\":\"value\"\` substring; user can pass \`key:value\`

const parts = t.split(\":\", 2);

if (parts.length === 2) {

const key = parts\[0\]!;

const val = parts\[1\]!;

where.push(\"r.tags\_json LIKE ?\");

params.push(\`%\${JSON.stringify(key)}:\${JSON.stringify(val).slice(1)}\`);
// mild hack; acceptable for v0

} else {

where.push(\"r.tags\_json LIKE ?\");

params.push(\`%\${t}%\`);

}

}

const whereSql = where.length ? \`WHERE \${where.join(\" AND \")}\` :
\"\";

// Include a couple quick summaries (join drift + q mean if present)

const rows = store.db.prepare(\`

SELECT

r.run\_id, r.run\_key, r.status, r.engine\_kind, r.engine\_version,
r.protocol\_version,

r.started\_at, r.finished\_at, r.tags\_json,

ms\_d.mean AS drift\_mean, ms\_q.mean AS q\_mean

FROM runs r

LEFT JOIN metrics\_summary ms\_d ON ms\_d.run\_id = r.run\_id AND
ms\_d.series = \'drift\'

LEFT JOIN metrics\_summary ms\_q ON ms\_q.run\_id = r.run\_id AND
ms\_q.series = \'q\'

\${whereSql}

ORDER BY r.started\_at DESC

LIMIT ? OFFSET ?

\`).all(\...params, limit, offset);

return rows.map((r: any) =\> ({

runId: r.run\_id,

runKey: r.run\_key,

status: r.status,

engine: { kind: r.engine\_kind, version: r.engine\_version,
protocolVersion: r.protocol\_version },

startedAt: r.started\_at,

finishedAt: r.finished\_at,

tags: safeJsonParse(r.tags\_json) ?? {},

quick: { driftMean: r.drift\_mean ?? null, qMean: r.q\_mean ?? null },

}));

});

// \-\-\-- Run detail \-\-\--

app.get(\`\${apiPrefix}/v1/runs/:runId\`, async (req) =\> {

const { runId } = req.params as any;

const r = store.db.prepare(\`

SELECT \* FROM runs WHERE run\_id = ?

\`).get(runId) as any;

if (!r) return { error: \"not\_found\", runId };

const summaries = store.db.prepare(\`

SELECT series, count, min, max, mean, m2, first\_step, last\_step

FROM metrics\_summary

WHERE run\_id = ?

ORDER BY series ASC

\`).all(runId) as any\[\];

return {

runId: r.run\_id,

runKey: r.run\_key,

status: r.status,

engine: { kind: r.engine\_kind, version: r.engine\_version,
protocolVersion: r.protocol\_version },

manifest: { version: r.manifest\_version, hash: r.manifest\_hash },

startedAt: r.started\_at,

finishedAt: r.finished\_at,

tags: safeJsonParse(r.tags\_json) ?? {},

notes: r.notes ?? null,

summaries,

};

});

// \-\-\-- Run blobs (fast) \-\-\--

app.get(\`\${apiPrefix}/v1/runs/:runId/blobs\`, async (req) =\> {

const { runId } = req.params as any;

const rows = store.db.prepare(\`

SELECT logical\_path, role, hash

FROM run\_blobs

WHERE run\_id = ?

ORDER BY logical\_path ASC

\`).all(runId) as any\[\];

return rows;

});

// \-\-\-- Metrics summary only \-\-\--

app.get(\`\${apiPrefix}/v1/runs/:runId/metrics/summary\`, async (req)
=\> {

const { runId } = req.params as any;

const rows = store.db.prepare(\`

SELECT series, count, min, max, mean, m2, first\_step, last\_step

FROM metrics\_summary

WHERE run\_id = ?

ORDER BY series ASC

\`).all(runId) as any\[\];

return rows;

});

// \-\-\-- SSE metrics stream \-\-\--

// UI: new EventSource(\`/qcalc-api/v1/runs/\${runId}/metrics/stream\`)

app.get(\`\${apiPrefix}/v1/runs/:runId/metrics/stream\`, async (req,
reply) =\> {

const { runId } = req.params as any;

const q = (req.query as any) ?? {};

const from = Math.max(0, num(q.fromByteOffset, 0));

const metricsPath = path.join(store.runDir(runId), \"metrics.jsonl\");

return tailJsonlAsSse(

req as any,

reply as any,

{

filePath: metricsPath,

fromByteOffset: from,

pollMs: 250,

heartbeatMs: 15000,

mapLine: (line) =\> {

// Validate/normalize events so UI always receives schema-valid
MetricEvent

const evt = MetricEvent.parse(JSON.parse(line));

return evt;

},

}

);

});

// (Optional) raw file fetch for debugging

app.get(\`\${apiPrefix}/v1/runs/:runId/files/:name\`, async (req, reply)
=\> {

const { runId, name } = req.params as any;

const p = path.join(store.runDir(runId), name);

try {

const data = readFileSync(p);

reply.header(\"content-type\", \"application/octet-stream\");

return data;

} catch {

reply.code(404);

return { error: \"not\_found\" };

}

});

await app.listen({ port, host });

app.log.info(\`QCalc orchestrator listening on
http://\${host}:\${port}\${apiPrefix}\`);

}

main().catch((e) =\> {

// eslint-disable-next-line no-console

console.error(e);

process.exit(1);

});

Minimal package deps for packages-ts/orchestrator

You'll need (at least):

fastify

\@fastify/cors

\@qcalc/store

\@qcalc/schemas

(Keep it ESM like the rest.)

Frontend wiring (Vite proxy)

Because the server already serves with prefix /qcalc-api, your Vite
proxy can be simple (no rewrite):

// frontend/vite.config.ts

server: {

proxy: {

\"/qcalc-api\": {

target: \"http://127.0.0.1:8787\",

changeOrigin: true

}

}

}

Then the UI calls:

GET /qcalc-api/v1/runs

EventSource(\'/qcalc-api/v1/runs/\<id\>/metrics/stream\')

Below are two drop-in files for packages-ts/orchestrator/src/:

server.ts (Fastify app + routes)

sseTail.ts (JSONL tail → SSE)

They assume:

your local store lives at .qcalc-store/ (same layout you designed)

sqlite is at .qcalc-store/db.sqlite

runs are at .qcalc-store/runs/\<runId\>/\...

They also default to serving under /qcalc-api, so your dashboard can
call /qcalc-api/v1/\... immediately.

packages-ts/orchestrator/src/sseTail.ts

import { open } from \"node:fs/promises\";

import { existsSync } from \"node:fs\";

type TailSseOpts = {

filePath: string;

pollMs?: number;

heartbeatMs?: number;

fromByteOffset?: number;

/\*\*

\* Called per parsed line; return null to skip emitting.

\* Throwing will emit an error event and continue.

\*/

mapLine?: (line: string) =\> any \| null;

};

function sleep(ms: number) {

return new Promise((r) =\> setTimeout(r, ms));

}

function writeSse(res: NodeJS.WritableStream, event: string, data: any)
{

res.write(\`event: \${event}\\n\`);

res.write(\`data: \${JSON.stringify(data)}\\n\\n\`);

}

export async function tailJsonlAsSse(

req: { raw: NodeJS.ReadableStream & { on: any } },

reply: { raw: NodeJS.WritableStream; headers: (h: any) =\> any; code:
(c: number) =\> any },

opts: TailSseOpts

) {

const pollMs = opts.pollMs ?? 250;

const heartbeatMs = opts.heartbeatMs ?? 15000;

let pos = Math.max(0, opts.fromByteOffset ?? 0);

let buffer = \"\";

let closed = false;

let lastHeartbeat = Date.now();

// SSE headers

reply

.code(200)

.headers({

\"content-type\": \"text/event-stream; charset=utf-8\",

\"cache-control\": \"no-cache, no-transform\",

connection: \"keep-alive\",

\"x-accel-buffering\": \"no\",

});

// Close handling

req.raw.on(\"close\", () =\> {

closed = true;

});

req.raw.on(\"end\", () =\> {

closed = true;

});

// initial hello

writeSse(reply.raw, \"hello\", { file: opts.filePath, fromByteOffset:
pos });

while (!closed) {

// Heartbeat (keeps proxies from killing stream)

if (Date.now() - lastHeartbeat \>= heartbeatMs) {

reply.raw.write(\`: heartbeat \${new Date().toISOString()}\\n\\n\`);

lastHeartbeat = Date.now();

}

// File may not exist yet

if (!existsSync(opts.filePath)) {

await sleep(pollMs);

continue;

}

try {

const fh = await open(opts.filePath, \"r\");

const st = await fh.stat();

if (st.size \> pos) {

const len = st.size - pos;

// Read new bytes

const b = Buffer.alloc(len);

await fh.read(b, 0, len, pos);

pos = st.size;

buffer += b.toString(\"utf8\");

// Emit complete lines only

let idx: number;

while ((idx = buffer.indexOf(\"\\n\")) \>= 0) {

const line = buffer.slice(0, idx).trim();

buffer = buffer.slice(idx + 1);

if (!line) continue;

try {

const mapped = opts.mapLine ? opts.mapLine(line) : JSON.parse(line);

if (mapped !== null) {

writeSse(reply.raw, \"metric\", { offset: pos, event: mapped });

}

} catch (e: any) {

writeSse(reply.raw, \"error\", {

message: e?.message ?? String(e),

linePreview: line.slice(0, 240),

});

}

}

}

await fh.close();

} catch (e: any) {

writeSse(reply.raw, \"error\", { message: e?.message ?? String(e) });

}

await sleep(pollMs);

}

}

packages-ts/orchestrator/src/server.ts

import Fastify from \"fastify\";

import cors from \"\@fastify/cors\";

import path from \"node:path\";

import { readFileSync } from \"node:fs\";

import { openDb, RunStore } from \"\@qcalc/store\";

import { MetricEvent } from \"\@qcalc/schemas\";

import { tailJsonlAsSse } from \"./sseTail.js\";

type Env = {

PORT?: string;

HOST?: string;

QCALC\_STORE\_DIR?: string; // default: .qcalc-store

QCALC\_API\_PREFIX?: string; // default: /qcalc-api

};

function num(v: any, d: number) {

const n = Number(v);

return Number.isFinite(n) ? n : d;

}

function safeJsonParse(s: string) {

try { return JSON.parse(s); } catch { return null; }

}

async function main() {

const env = process.env as Env;

const port = num(env.PORT, 8787);

const host = env.HOST ?? \"127.0.0.1\";

const storeRoot = env.QCALC\_STORE\_DIR ?? path.join(process.cwd(),
\".qcalc-store\");

const apiPrefix = env.QCALC\_API\_PREFIX ?? \"/qcalc-api\";

const db = openDb(path.join(storeRoot, \"db.sqlite\"));

const store = new RunStore(db, storeRoot);

const app = Fastify({ logger: true });

// If you proxy via Vite, CORS isn\'t required. But harmless for local
multi-origin dev.

await app.register(cors, { origin: true });

// Health

app.get(\`\${apiPrefix}/health\`, async () =\> ({ ok: true, storeRoot
}));

// \-\-\-- Runs list \-\-\--

app.get(\`\${apiPrefix}/v1/runs\`, async (req, reply) =\> {

const q = (req.query as any) ?? {};

const limit = Math.min(200, Math.max(1, num(q.limit, 50)));

const offset = Math.max(0, num(q.offset, 0));

const status = typeof q.status === \"string\" ? q.status : undefined;

const engineKind = typeof q.engine\_kind === \"string\" ? q.engine\_kind
: undefined;

// tag filter: repeated ?tag=axis:budgets.epsilon:\"0.05\" or
?tag=experiment:baseline

const tags = (\[\] as string\[\]).concat(q.tag ?? \[\]).filter((x) =\>
typeof x === \"string\");

// Minimal tag filtering: LIKE on tags\_json. (Works fine for early
phase.)

const where: string\[\] = \[\];

const params: any\[\] = \[\];

if (status) { where.push(\"r.status = ?\"); params.push(status); }

if (engineKind) { where.push(\"r.engine\_kind = ?\");
params.push(engineKind); }

for (const t of tags) {

// match \`\"key\":\"value\"\` substring; user can pass \`key:value\`

const parts = t.split(\":\", 2);

if (parts.length === 2) {

const key = parts\[0\]!;

const val = parts\[1\]!;

where.push(\"r.tags\_json LIKE ?\");

params.push(\`%\${JSON.stringify(key)}:\${JSON.stringify(val).slice(1)}\`);
// mild hack; acceptable for v0

} else {

where.push(\"r.tags\_json LIKE ?\");

params.push(\`%\${t}%\`);

}

}

const whereSql = where.length ? \`WHERE \${where.join(\" AND \")}\` :
\"\";

// Include a couple quick summaries (join drift + q mean if present)

const rows = store.db.prepare(\`

SELECT

r.run\_id, r.run\_key, r.status, r.engine\_kind, r.engine\_version,
r.protocol\_version,

r.started\_at, r.finished\_at, r.tags\_json,

ms\_d.mean AS drift\_mean, ms\_q.mean AS q\_mean

FROM runs r

LEFT JOIN metrics\_summary ms\_d ON ms\_d.run\_id = r.run\_id AND
ms\_d.series = \'drift\'

LEFT JOIN metrics\_summary ms\_q ON ms\_q.run\_id = r.run\_id AND
ms\_q.series = \'q\'

\${whereSql}

ORDER BY r.started\_at DESC

LIMIT ? OFFSET ?

\`).all(\...params, limit, offset);

return rows.map((r: any) =\> ({

runId: r.run\_id,

runKey: r.run\_key,

status: r.status,

engine: { kind: r.engine\_kind, version: r.engine\_version,
protocolVersion: r.protocol\_version },

startedAt: r.started\_at,

finishedAt: r.finished\_at,

tags: safeJsonParse(r.tags\_json) ?? {},

quick: { driftMean: r.drift\_mean ?? null, qMean: r.q\_mean ?? null },

}));

});

// \-\-\-- Run detail \-\-\--

app.get(\`\${apiPrefix}/v1/runs/:runId\`, async (req) =\> {

const { runId } = req.params as any;

const r = store.db.prepare(\`

SELECT \* FROM runs WHERE run\_id = ?

\`).get(runId) as any;

if (!r) return { error: \"not\_found\", runId };

const summaries = store.db.prepare(\`

SELECT series, count, min, max, mean, m2, first\_step, last\_step

FROM metrics\_summary

WHERE run\_id = ?

ORDER BY series ASC

\`).all(runId) as any\[\];

return {

runId: r.run\_id,

runKey: r.run\_key,

status: r.status,

engine: { kind: r.engine\_kind, version: r.engine\_version,
protocolVersion: r.protocol\_version },

manifest: { version: r.manifest\_version, hash: r.manifest\_hash },

startedAt: r.started\_at,

finishedAt: r.finished\_at,

tags: safeJsonParse(r.tags\_json) ?? {},

notes: r.notes ?? null,

summaries,

};

});

// \-\-\-- Run blobs (fast) \-\-\--

app.get(\`\${apiPrefix}/v1/runs/:runId/blobs\`, async (req) =\> {

const { runId } = req.params as any;

const rows = store.db.prepare(\`

SELECT logical\_path, role, hash

FROM run\_blobs

WHERE run\_id = ?

ORDER BY logical\_path ASC

\`).all(runId) as any\[\];

return rows;

});

// \-\-\-- Metrics summary only \-\-\--

app.get(\`\${apiPrefix}/v1/runs/:runId/metrics/summary\`, async (req)
=\> {

const { runId } = req.params as any;

const rows = store.db.prepare(\`

SELECT series, count, min, max, mean, m2, first\_step, last\_step

FROM metrics\_summary

WHERE run\_id = ?

ORDER BY series ASC

\`).all(runId) as any\[\];

return rows;

});

// \-\-\-- SSE metrics stream \-\-\--

// UI: new EventSource(\`/qcalc-api/v1/runs/\${runId}/metrics/stream\`)

app.get(\`\${apiPrefix}/v1/runs/:runId/metrics/stream\`, async (req,
reply) =\> {

const { runId } = req.params as any;

const q = (req.query as any) ?? {};

const from = Math.max(0, num(q.fromByteOffset, 0));

const metricsPath = path.join(store.runDir(runId), \"metrics.jsonl\");

return tailJsonlAsSse(

req as any,

reply as any,

{

filePath: metricsPath,

fromByteOffset: from,

pollMs: 250,

heartbeatMs: 15000,

mapLine: (line) =\> {

// Validate/normalize events so UI always receives schema-valid
MetricEvent

const evt = MetricEvent.parse(JSON.parse(line));

return evt;

},

}

);

});

// (Optional) raw file fetch for debugging

app.get(\`\${apiPrefix}/v1/runs/:runId/files/:name\`, async (req, reply)
=\> {

const { runId, name } = req.params as any;

const p = path.join(store.runDir(runId), name);

try {

const data = readFileSync(p);

reply.header(\"content-type\", \"application/octet-stream\");

return data;

} catch {

reply.code(404);

return { error: \"not\_found\" };

}

});

await app.listen({ port, host });

app.log.info(\`QCalc orchestrator listening on
http://\${host}:\${port}\${apiPrefix}\`);

}

main().catch((e) =\> {

// eslint-disable-next-line no-console

console.error(e);

process.exit(1);

});

Minimal package deps for packages-ts/orchestrator

You'll need (at least):

fastify

\@fastify/cors

\@qcalc/store

\@qcalc/schemas

(Keep it ESM like the rest.)

Frontend wiring (Vite proxy)

Because the server already serves with prefix /qcalc-api, your Vite
proxy can be simple (no rewrite):

// frontend/vite.config.ts

server: {

proxy: {

\"/qcalc-api\": {

target: \"http://127.0.0.1:8787\",

changeOrigin: true

}

}

}

Then the UI calls:

GET /qcalc-api/v1/runs

EventSource(\'/qcalc-api/v1/runs/\<id\>/metrics/stream\')
