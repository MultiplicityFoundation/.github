---
slug: mtpi-node-js
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "02-implementations/\u039Bproof/MTPI - NODE.js.md"
  last_synced: '2026-03-20T17:17:15.655371Z'
---

here's a clean, production‑ready JS architecture that ports
**mtpi\_test\_app.py** into a browser/Node DApp that drives proofs and
talks to the MTPI contracts.

**High‑level goals**
====================

-   **Keep Solidity on-chain; move orchestration to JS.\
    > **

-   **Generate/verify zk proofs client‑side** (WASM via snarkjs) or
    > server‑side (Node worker).

-   **Enforce prime‑gated & CSL "silent mode" in the client** so you
    > only hit chain after gates open.

-   **Abstract proof + contract I/O** behind a small "Proof Manager" so
    > UI and infra stay decoupled.

**Monorepo layout (turborepo / pnpm)**
======================================

bash

CopyEdit

mtpi-dapp/

├─ apps/

│ ├─ web/ \# Next.js (or Vite+React) DApp

│ └─ relay/ \# Optional Node "quiet relay" (no user data, only proof
forwarding)

├─ packages/

│ ├─ proof-manager/ \# WASM/zk orchestration (snarkjs, wasm runners,
vkey mgmt)

│ ├─ mtpi-contracts/ \# TypeChain bindings + deployment scripts (hardhat
or foundry+viem)

│ ├─ csl/ \# CSL & drift policies (pure TS), Miller--Rabin, prime-gate
utilities

│ ├─ poseidon/ \# Poseidon hash utils (circomlibjs) + domain separators

│ └─ shared/ \# types, constants, env schema (zod), logging, errors

└─ infra/

├─ docker/

├─ k8s/

└─ ci/

**Core modules (what replaces the Python app)**
===============================================

**1) packages/proof-manager**
-----------------------------

Responsibilities:

-   Load circuit artifacts (\*.wasm, \*.zkey, \*\_vk.json) for:

    -   root\_contract.circom

    -   recovery\_contract.circom

-   Build witnesses in browser (WASM) or Node (headless).

-   Create Groth16 proofs (snarkjs.groth16.prove), verify locally
    > (groth16.verify).

-   Normalize inputs/outputs; hash transcripts with Poseidon.

API (TypeScript):

ts

CopyEdit

export type ProofKind = \"root\" \| \"recovery\";

export interface ProofInput {

identityHash: string; // Poseidon(input) --- never raw IDs

stateCommit: string; // Poseidon(state)

params: Record\<string, string \| bigint\>;

}

export interface GeneratedProof {

a: \[string, string\];

b: \[\[string, string\],\[string, string\]\];

c: \[string, string\];

publicSignals: string\[\];

}

export interface ProofManager {

init(): Promise\<void\>;

prove(kind: ProofKind, input: ProofInput): Promise\<GeneratedProof\>;

verify(kind: ProofKind, proof: GeneratedProof): Promise\<boolean\>;

vk(kind: ProofKind): Promise\<any\>; // verification key

}

Implementation notes:

-   Bundle snarkjs + circuit WASM via wasm-loader (web) or lazy‑load
    > (Node).

-   Store vkeys in **immutable** /public/keys/... with content hashes
    > (SRI checked).

-   Use **Web Workers** in the browser to avoid locking the UI during
    > witness gen.

**2) packages/mtpi-contracts**
------------------------------

Responsibilities:

-   Contract ABIs + TypeChain types for MTPI\_Core.sol, Verifier.sol,
    > Poseidon.sol.

-   Thin call wrappers that:

    -   Check **CSL/prime-gate** predicates before any on‑chain tx.

    -   Submit proofs with correct calldata shape.

-   Deployment utilities (Hardhat or Foundry) + Sepolia config.

API:

ts

CopyEdit

export interface MtpiClient {

getConfig(): Promise\<{

network: string;

addresses: { core: string; verifier: string; poseidon: string };

}\>;

quantumTransition(proof: GeneratedProof): Promise\<string\>; // tx hash

enterSilentRecovery(proof: GeneratedProof): Promise\<string\>; // tx
hash

readState(commitment: string): Promise\<any\>;

}

**3) packages/csl**
-------------------

Responsibilities:

-   **CSL/compliance** guards (no surveillance: only hashed inputs).

-   **Drift** checks (δ ≤ 0.3) done off‑chain before proof attempt.

-   **Prime gates** & "Proof of Quiet" rules (e.g., block/commit counts,
    > prime epochs).

-   Deterministic Miller--Rabin for UI gating & consistency.

API (guards that throw on violation):

ts

CopyEdit

export function enforceSilentMode(ctx: Context): void;

export function enforcePrimeGate(ctx: Context): void;

export function enforceDriftBound(delta: number, epsilon = 0.3): void;

export function isPrime(n: bigint): boolean; // fast MR with fixed
witnesses

**4) packages/poseidon**
------------------------

-   Thin wrapper around circomlibjs Poseidon.

-   Adds **domain separation** tags (MTPI:IDENTITY, MTPI:STATE, etc.).

-   Hash helpers for stable, canonical encoding.

**5) apps/web (Next.js or Vite)**
---------------------------------

-   **UI**: Proof forms, state visualizer, drift meter.

-   **Wallet**: wagmi + viem (or ethers v6).

-   **Privacy**: All user inputs are hashed client‑side before any
    > network call.

-   **Modes**:

    -   *Local‑only*: generate+verify proofs, **no chain** (for
        > audits/demos).

    -   *Sepolia*: after gates pass, send tx to MTPI\_Core.

Data flow (happy path):

scss

CopyEdit

User input → csl.enforce\* → poseidon.hash(input) → proofManager.prove()

→ proofManager.verify() → mtpi-contracts.quantumTransition() → receipt

**6) apps/relay (optional)**
----------------------------

-   Stateless Node service that **only forwards proofs** to chain for
    > users who want zero RPC exposure.

-   No PII; just proof blobs and target address. Rate‑limited, HMAC'd.

**Environment & artifacts**
===========================

bash

CopyEdit

/public/keys/

root\_contract.wasm

root\_contract\_final.zkey

root\_contract\_vk.json

recovery\_contract.wasm

recovery\_contract\_final.zkey

recovery\_contract\_vk.json

.env

NEXT\_PUBLIC\_NETWORK=sepolia

NEXT\_PUBLIC\_CORE\_ADDRESS=0x\...

NEXT\_PUBLIC\_VERIFIER\_ADDRESS=0x\...

NEXT\_PUBLIC\_POSEIDON\_ADDRESS=0x\...

NEXT\_PUBLIC\_RPC\_URL=\...

**Porting the Python behaviors → JS**
=====================================

What the old mtpi\_test\_app.py did (conceptually):

-   Prepared inputs (identity hash, state commit).

-   Called local proof generator.

-   Posted proof to chain endpoints.

-   Logged audits.

JS equivalents:

-   **Input prep** → poseidon.hash\*() + csl.enforce\*().

-   **Proof gen** → proof-manager.prove() (WASM, browser or Node).

-   **Chain tx** → mtpi-contracts.quantumTransition() /
    > enterSilentRecovery().

-   **Audit** → append-only log (client IndexedDB + optional relay
    > mirror).

**Example wiring (web app)**
============================

ts

CopyEdit

// apps/web/src/lib/mtpi.ts

import { createMtpiClient } from \"\@mtpi/mtpi-contracts\";

import { makeProofManager } from \"\@mtpi/proof-manager\";

import { enforceDriftBound, enforcePrimeGate, enforceSilentMode } from
\"\@mtpi/csl\";

import { poseidonIdentity, poseidonState } from \"\@mtpi/poseidon\";

export async function runQuantumTransition(rawInput: any, ctx: any) {

enforceSilentMode(ctx);

enforcePrimeGate(ctx);

enforceDriftBound(ctx.delta);

const identityHash = poseidonIdentity(rawInput.identity);

const stateCommit = poseidonState(rawInput.state);

const proofManager = await makeProofManager().init();

const proof = await proofManager.prove(\"root\", {

identityHash, stateCommit, params: ctx.params

});

const ok = await proofManager.verify(\"root\", proof);

if (!ok) throw new Error(\"Local vkey verify failed\");

const mtpi = await createMtpiClient();

const txHash = await mtpi.quantumTransition(proof);

return txHash;

}

**Build & deploy workflow**
===========================

1.  **Install & bootstrap\
    > **

css

CopyEdit

pnpm i

pnpm -w build

2.  **Load artifacts** into /public/keys/\* (hash‑pinned).

3.  **Local mode**: pnpm -F web dev → prove+verify without chain.

4.  **Sepolia config** in .env → pnpm -F web start.

5.  **Contracts** (if you deploy from this repo):

r

CopyEdit

pnpm -F mtpi-contracts deploy:sepolia

\# emits addresses to packages/mtpi-contracts/deployments/sepolia.json

6.  **CI**: run proof-manager tests headless (Node), web e2e
    > (Playwright), gas checks on PR.

**Security & privacy defaults**
===============================

-   **No raw identifiers** leave the browser: only Poseidon commitments.

-   **Proofs verified locally** before any tx (fail fast).

-   **Prime gates** enforced client‑side (prevents noisy calls).

-   **Content‑hash keys/vkeys**; SRI tags on WASM/ZKey.

-   **Worker isolation** for witness building; memory zeroization after
    > use.

-   **Replay protection**: include a **nonce** (Poseidon‑hashed) in
    > public signals.

**Performance tips**
====================

-   Pre‑init WASM at app load with a tiny "warmup" witness.

-   Cache vkeys & WASM in IndexedDB; gate updates by content hash.

-   Use a **Web Worker pool** (2--3) to parallelize proof gen for snappy
    > UX.

**What you'll need from me to finish**
======================================

-   Your current **contract addresses** (Sepolia).

-   The exact **circuit public signals order** (for calldata shaping).

-   Any bespoke **CSL/prime‑gate rules** you want enforced by default.

-   The **artifact bundle** you want shipped (or I can export from your
    > repo).

If you want, I can spin up a minimal starter with this layout (Next.js +
proof manager + a fake circuit shim) so you can drop in your real
\*.wasm/\*.zkey and deploy in an afternoon.
