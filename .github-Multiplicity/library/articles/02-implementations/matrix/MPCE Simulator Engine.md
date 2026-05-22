---
slug: mpce-simulator-engine
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/matrix/MPCE Simulator Engine.md
  last_synced: '2026-03-20T17:17:15.867255Z'
---

// MPCE Simulator Engine Starter (TS/TSX/FSX/JSON)

//

// This is a \*simulator\* implementation aligned to the equations
described in the MPCE PDFs.

// It is NOT a hardware-accurate or cryptographically secure
implementation.

//

//
─────────────────────────────────────────────────────────────────────────────

// FILE: package.json

//
─────────────────────────────────────────────────────────────────────────────

{

\"name\": \"mpce-sim\",

\"version\": \"0.1.0\",

\"private\": true,

\"type\": \"module\",

\"scripts\": {

\"build\": \"tsc -p tsconfig.json\",

\"sim\": \"node \--enable-source-maps dist/index.js
./src/config/example.mpce.json\",

\"sim:watch\": \"node \--watch \--enable-source-maps dist/index.js
./src/config/example.mpce.json\",

\"typecheck\": \"tsc -p tsconfig.json \--noEmit\"

},

\"dependencies\": {

\"zod\": \"\^3.25.7\"

},

\"devDependencies\": {

\"\@types/node\": \"\^22.10.2\",

\"typescript\": \"\^5.7.2\"

}

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: tsconfig.json

//
─────────────────────────────────────────────────────────────────────────────

{

\"compilerOptions\": {

\"target\": \"ES2022\",

\"lib\": \[\"ES2022\"\],

\"module\": \"ES2022\",

\"moduleResolution\": \"Bundler\",

\"outDir\": \"dist\",

\"rootDir\": \"src\",

\"strict\": true,

\"esModuleInterop\": true,

\"skipLibCheck\": true,

\"forceConsistentCasingInFileNames\": true,

\"noUncheckedIndexedAccess\": true

},

\"include\": \[\"src\"\]

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/config/schema.mpce.json (human-oriented; use Zod for
runtime validation)

//
─────────────────────────────────────────────────────────────────────────────

{

\"\$schema\": \"https://json-schema.org/draft/2020-12/schema\",

\"title\": \"MPCE Simulator Config\",

\"type\": \"object\",

\"required\": \[\"run\", \"encoder\", \"tensor\", \"feedback\",
\"error\"\],

\"properties\": {

\"run\": {

\"type\": \"object\",

\"required\": \[\"seed\", \"steps\"\],

\"properties\": {

\"seed\": {\"type\": \"integer\"},

\"steps\": {\"type\": \"integer\", \"minimum\": 1},

\"logEvery\": {\"type\": \"integer\", \"minimum\": 1, \"default\": 1}

}

},

\"encoder\": {

\"type\": \"object\",

\"required\": \[\"dictionary\", \"weights\", \"epsilonStd\"\],

\"properties\": {

\"dictionary\": {\"type\": \"array\", \"items\": {\"type\":
\"string\"}},

\"weights\": {\"type\": \"array\", \"items\": {\"type\": \"number\"}},

\"epsilonStd\": {\"type\": \"number\", \"minimum\": 0},

\"historyWindow\": {\"type\": \"integer\", \"minimum\": 1, \"default\":
8},

\"primeStartIndex\": {\"type\": \"integer\", \"minimum\": 0,
\"default\": 0},

\"crypto\": {

\"type\": \"object\",

\"properties\": {

\"modulusQ\": {\"type\": \"string\", \"description\": \"Optional big
prime modulus as decimal string.\"}

}

}

}

},

\"tensor\": {

\"type\": \"object\",

\"required\": \[\"nodes\", \"edges\"\],

\"properties\": {

\"nodes\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}},

\"edges\": {

\"type\": \"array\",

\"items\": {

\"type\": \"object\",

\"required\": \[\"from\", \"to\", \"weight\"\],

\"properties\": {

\"from\": {\"type\": \"integer\"},

\"to\": {\"type\": \"integer\"},

\"weight\": {\"type\": \"number\"}

}

}

},

\"primeModulation\": {\"type\": \"number\", \"default\": 0.15}

}

},

\"feedback\": {

\"type\": \"object\",

\"required\": \[\"learningRate\", \"noiseStd\", \"convergeEps\"\],

\"properties\": {

\"learningRate\": {\"type\": \"number\", \"minimum\": 0},

\"noiseStd\": {\"type\": \"number\", \"minimum\": 0},

\"convergeEps\": {\"type\": \"number\", \"minimum\": 0},

\"maxMatrixSize\": {\"type\": \"integer\", \"minimum\": 2, \"default\":
8}

}

},

\"error\": {

\"type\": \"object\",

\"required\": \[\"injectRate\"\],

\"properties\": {

\"injectRate\": {\"type\": \"number\", \"minimum\": 0, \"maximum\": 1},

\"errorPrimePool\": {\"type\": \"array\", \"items\": {\"type\":
\"string\"}, \"default\": \[\"101\", \"103\", \"107\", \"109\"\]}

}

}

}

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/config/example.mpce.json

//
─────────────────────────────────────────────────────────────────────────────

{

\"run\": {\"seed\": 42, \"steps\": 60, \"logEvery\": 1},

\"encoder\": {

\"dictionary\": \[\"A\", \"B\", \"C\", \"D\", \"E\", \"F\"\],

\"weights\": \[0.35, 0.25, 0.2, 0.12, 0.06, 0.02\],

\"epsilonStd\": 0.5,

\"historyWindow\": 8,

\"primeStartIndex\": 0,

\"crypto\": {\"modulusQ\": \"0\"}

},

\"tensor\": {

\"nodes\": \[\"enc\", \"tensor\", \"fb\", \"err\"\],

\"edges\": \[

{\"from\": 0, \"to\": 1, \"weight\": 0.9},

{\"from\": 1, \"to\": 2, \"weight\": 0.6},

{\"from\": 2, \"to\": 1, \"weight\": 0.3},

{\"from\": 2, \"to\": 3, \"weight\": 0.25},

{\"from\": 3, \"to\": 2, \"weight\": 0.2}

\],

\"primeModulation\": 0.12

},

\"feedback\": {\"learningRate\": 0.08, \"noiseStd\": 0.01,
\"convergeEps\": 1e-4, \"maxMatrixSize\": 6},

\"error\": {\"injectRate\": 0.12, \"errorPrimePool\": \[\"101\",
\"103\", \"107\", \"109\", \"113\", \"127\"\]}

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/rng.ts

//
─────────────────────────────────────────────────────────────────────────────

export type RNG = {

next(): number; // uniform \[0,1)

normal(mean?: number, std?: number): number;

int(minInclusive: number, maxExclusive: number): number;

};

export function makeRng(seed: number): RNG {

// Mulberry32 --- small, fast, deterministic (simulation only).

let t = seed \>\>\> 0;

const next = () =\> {

t += 0x6d2b79f5;

let x = Math.imul(t \^ (t \>\>\> 15), 1 \| t);

x \^= x + Math.imul(x \^ (x \>\>\> 7), 61 \| x);

return ((x \^ (x \>\>\> 14)) \>\>\> 0) / 4294967296;

};

const normal = (mean = 0, std = 1) =\> {

// Box--Muller

let u = 0;

let v = 0;

while (u === 0) u = next();

while (v === 0) v = next();

const z = Math.sqrt(-2.0 \* Math.log(u)) \* Math.cos(2.0 \* Math.PI \*
v);

return mean + std \* z;

};

const int = (minInclusive: number, maxExclusive: number) =\> {

const r = next();

return minInclusive + Math.floor(r \* (maxExclusive - minInclusive));

};

return { next, normal, int };

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/math.ts

//
─────────────────────────────────────────────────────────────────────────────

export function gcdBigInt(a: bigint, b: bigint): bigint {

a = a \< 0n ? -a : a;

b = b \< 0n ? -b : b;

while (b !== 0n) {

const t = b;

b = a % b;

a = t;

}

return a;

}

export function clamp(x: number, lo: number, hi: number): number {

return Math.max(lo, Math.min(hi, x));

}

export function l2Norm(vec: Float64Array): number {

let s = 0;

for (let i = 0; i \< vec.length; i++) s += vec\[i\] \* vec\[i\];

return Math.sqrt(s);

}

export function normalize(vec: Float64Array, eps = 1e-12): Float64Array
{

const n = l2Norm(vec);

const d = n \< eps ? 1 : n;

for (let i = 0; i \< vec.length; i++) vec\[i\] /= d;

return vec;

}

export function dot(a: Float64Array, b: Float64Array): number {

const n = Math.min(a.length, b.length);

let s = 0;

for (let i = 0; i \< n; i++) s += a\[i\] \* b\[i\];

return s;

}

export function log2BigInt(x: bigint): number {

if (x \<= 0n) return -Infinity;

// exact bit length gives floor(log2)

const bits = x.toString(2).length;

// refine using leading 53 bits

const shift = BigInt(Math.max(0, bits - 53));

const top = Number(x \>\> shift);

return (bits - 1) + Math.log2(top / Math.pow(2, 52));

}

export function mulMod(a: bigint, b: bigint, mod: bigint): bigint {

if (mod === 0n) return a \* b;

return (a \* b) % mod;

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/primes.ts

//
─────────────────────────────────────────────────────────────────────────────

export function isPrime(n: number): boolean {

if (n \<= 1) return false;

if (n \<= 3) return true;

if (n % 2 === 0 \|\| n % 3 === 0) return false;

for (let i = 5; i \* i \<= n; i += 6) {

if (n % i === 0 \|\| n % (i + 2) === 0) return false;

}

return true;

}

export function nthPrime(n: number): number {

if (n \< 0) throw new Error(\"nthPrime: n must be \>= 0\");

let count = -1;

let x = 1;

while (count \< n) {

x++;

if (isPrime(x)) count++;

}

return x;

}

export function firstNPrimes(n: number, startIndex = 0): bigint\[\] {

const out: bigint\[\] = \[\];

for (let i = 0; i \< n; i++) out.push(BigInt(nthPrime(startIndex + i)));

return out;

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/encoder.ts

// Implements the simulator form of: p(x,t) = Fp(t) · φ(x)

// and Fp(t) = Σ wk · pk(t) + εp(t)

//
─────────────────────────────────────────────────────────────────────────────

import { firstNPrimes } from \"./primes.js\";

import { log2BigInt, mulMod } from \"./math.js\";

import type { RNG } from \"./rng.js\";

export type EncoderConfig = {

dictionary: string\[\];

weights: number\[\];

epsilonStd: number;

historyWindow: number;

primeStartIndex: number;

modulusQ: bigint; // 0n =\> no modulus

};

export type EncodedStep = {

t: number;

symbols: string\[\];

basePrimes: bigint\[\]; // φ(x)

dynamicStates: bigint\[\]; // p(x,t)

product: bigint; // ∏ p(x,t) (optionally mod q)

sizeBits: number;

log2Product: number;

Fp: bigint;

};

export class PrimeEncoder {

private baseMap = new Map\<string, bigint\>();

private basePrimePool: bigint\[\];

private history: bigint\[\] = \[\];

constructor(private cfg: EncoderConfig, private rng: RNG) {

const needed = cfg.dictionary.length + 16;

this.basePrimePool = firstNPrimes(needed, cfg.primeStartIndex);

cfg.dictionary.forEach((sym, i) =\> {

this.baseMap.set(sym, this.basePrimePool\[i\]!);

});

}

basePrime(sym: string): bigint {

const p = this.baseMap.get(sym);

if (!p) throw new Error(\`Unknown symbol: \${sym}\`);

return p;

}

private feedbackFactor(): bigint {

const w = this.cfg.weights;

const window = Math.max(1, this.cfg.historyWindow);

const hist = this.history.slice(-window);

let acc = 0;

for (let i = 0; i \< w.length; i++) {

const pk = hist\[hist.length - 1 - i\];

if (!pk) break;

acc += w\[i\]! \* log2BigInt(pk);

}

const eps = this.rng.normal(0, this.cfg.epsilonStd);

// Map to a positive integer scale \>= 1.

const scale = Math.max(1, Math.round(Math.exp((acc + eps) / 8)));

return BigInt(scale);

}

encode(t: number, symbols: string\[\]): EncodedStep {

const basePrimes = symbols.map((s) =\> this.basePrime(s));

const Fp = this.feedbackFactor();

const dynamicStates = basePrimes.map((p) =\> p \* Fp);

// Update history with dynamic states (pk(t) in the papers is
underspecified; this is a simple choice).

this.history.push(\...dynamicStates);

const sizeBits = symbols.reduce((s, x) =\> s + x.length \* 8, 0);

const log2Product = dynamicStates.reduce((s, p) =\> s + log2BigInt(p),
0);

let product = 1n;

for (const p of dynamicStates) product = mulMod(product, p,
this.cfg.modulusQ);

return { t, symbols, basePrimes, dynamicStates, product, sizeBits,
log2Product, Fp };

}

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/errorCorrection.ts

// Implements simulator form of: p\_corrected = φ(p\_ij) / gcd(φ(p\_ij),
E)

// Here we treat E as a cumulative multiplicative error term of primes.

//
─────────────────────────────────────────────────────────────────────────────

import { gcdBigInt, mulMod } from \"./math.js\";

import type { RNG } from \"./rng.js\";

export type ErrorConfig = {

injectRate: number; // probability of injecting an error factor

errorPrimePool: bigint\[\]; // primes to multiply in

};

export type ErrorState = {

cumulativeE: bigint; // E

introduced: bigint\[\];

detectedCount: number;

correctedCount: number;

};

export function initErrorState(): ErrorState {

return { cumulativeE: 1n, introduced: \[\], detectedCount: 0,
correctedCount: 0 };

}

export function maybeInjectError(

rng: RNG,

cfg: ErrorConfig,

value: bigint,

modQ: bigint,

st: ErrorState

): bigint {

if (cfg.injectRate \<= 0) return value;

if (rng.next() \>= cfg.injectRate) return value;

const ep = cfg.errorPrimePool\[rng.int(0, cfg.errorPrimePool.length)\]!;

st.cumulativeE = mulMod(st.cumulativeE, ep, modQ);

st.introduced.push(ep);

// Multiplicative corruption

return mulMod(value, ep, modQ);

}

export function correctPrimeState(phiPij: bigint, E: bigint): {
corrected: bigint; gcd: bigint } {

const g = gcdBigInt(phiPij, E);

if (g === 0n) return { corrected: phiPij, gcd: 0n };

const corrected = phiPij / g;

return { corrected, gcd: g };

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/tensorNetwork.ts

// Simulator approximation of: T = Σ\_{i,j} T\_ij ⊗ φ(p\_ij)

// We model a weighted directed graph with prime-modulated edge
strengths.

//
─────────────────────────────────────────────────────────────────────────────

import { dot, l2Norm, log2BigInt, normalize } from \"./math.js\";

import type { RNG } from \"./rng.js\";

export type Edge = { from: number; to: number; weight: number };

export type TensorConfig = {

nodes: string\[\];

edges: Edge\[\];

primeModulation: number; // scale for prime influence on weights

};

export type TensorStep = {

state: Float64Array;

lambdaMax: number; // estimated spectral radius / max eigenvalue
magnitude

};

export class TensorNetwork {

private n: number;

private W: Float64Array; // row-major NxN

private state: Float64Array;

constructor(private cfg: TensorConfig, private rng: RNG) {

this.n = cfg.nodes.length;

if (this.n \< 2) throw new Error(\"TensorNetwork: need \>=2 nodes\");

this.W = new Float64Array(this.n \* this.n);

for (const e of cfg.edges) {

if (e.from \< 0 \|\| e.to \< 0 \|\| e.from \>= this.n \|\| e.to \>=
this.n) continue;

this.W\[e.from \* this.n + e.to\] += e.weight;

}

this.state = new Float64Array(this.n);

for (let i = 0; i \< this.n; i++) this.state\[i\] = this.rng.normal(0,
1);

normalize(this.state);

}

get weights(): Float64Array {

return this.W;

}

get currentState(): Float64Array {

return this.state;

}

private matVec(W: Float64Array, v: Float64Array): Float64Array {

const out = new Float64Array(this.n);

for (let i = 0; i \< this.n; i++) {

let s = 0;

const row = i \* this.n;

for (let j = 0; j \< this.n; j++) s += W\[row + j\]! \* v\[j\]!;

out\[i\] = s;

}

return out;

}

estimateLambdaMax(iter = 20): number {

let v = new Float64Array(this.n);

for (let i = 0; i \< this.n; i++) v\[i\] = this.rng.normal(0, 1);

normalize(v);

let lam = 0;

for (let k = 0; k \< iter; k++) {

const wv = this.matVec(this.W, v);

const nrm = l2Norm(wv);

if (nrm \< 1e-12) break;

for (let i = 0; i \< this.n; i++) v\[i\] = wv\[i\]! / nrm;

const wv2 = this.matVec(this.W, v);

lam = dot(v, wv2);

}

return lam;

}

step(primeStates: bigint\[\]): TensorStep {

// Prime modulation: alter weights based on log2 of provided prime
states.

// We use a safe summary scalar to avoid enormous BigInt-\>Number
conversion.

const primeSignal = primeStates.length

? primeStates.reduce((s, p) =\> s + log2BigInt(p), 0) /
primeStates.length

: 0;

const mod = 1 + this.cfg.primeModulation \* Math.tanh(primeSignal / 64);

const Wm = new Float64Array(this.W.length);

for (let i = 0; i \< this.W.length; i++) Wm\[i\] = this.W\[i\]! \* mod;

// Linear update + mild nonlinearity

const next = new Float64Array(this.n);

for (let i = 0; i \< this.n; i++) {

let s = 0;

const row = i \* this.n;

for (let j = 0; j \< this.n; j++) s += Wm\[row + j\]! \*
this.state\[j\]!;

next\[i\] = Math.tanh(s);

}

this.state = normalize(next);

// Update internal weights to modulated weights (simulates evolving
tensor interactions)

this.W = Wm;

const lambdaMax = this.estimateLambdaMax(18);

return { state: this.state, lambdaMax };

}

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/feedback.ts

// Implements simulator form of: M(t+1) = f(M(t), R(t)) + ε\_M(t)

// with convergence when \|\|M(t+1)-M(t)\|\| -\> 0

// We treat M as a small matrix capturing evolving correlations.

//
─────────────────────────────────────────────────────────────────────────────

import { clamp } from \"./math.js\";

import type { RNG } from \"./rng.js\";

export type FeedbackConfig = {

learningRate: number;

noiseStd: number;

convergeEps: number;

maxMatrixSize: number;

};

export type FeedbackStep = {

deltaNorm: number;

converged: boolean;

};

export class FeedbackLoop {

private n: number;

private M: Float64Array; // n x n row-major

constructor(private cfg: FeedbackConfig, private rng: RNG, size: number)
{

this.n = Math.max(2, Math.min(cfg.maxMatrixSize, size));

this.M = new Float64Array(this.n \* this.n);

// Start as near-identity

for (let i = 0; i \< this.n; i++) this.M\[i \* this.n + i\] = 1;

}

get matrix(): Float64Array {

return this.M;

}

step(R: Float64Array): FeedbackStep {

// R is a vector of length \>= n. We compute an outer product target.

const lr = clamp(this.cfg.learningRate, 0, 1);

const prev = this.M.slice();

for (let i = 0; i \< this.n; i++) {

for (let j = 0; j \< this.n; j++) {

const target = R\[i\]! \* R\[j\]!;

const idx = i \* this.n + j;

const noise = this.rng.normal(0, this.cfg.noiseStd);

this.M\[idx\] = (1 - lr) \* this.M\[idx\]! + lr \* (target + noise);

}

}

// delta norm

let s = 0;

for (let k = 0; k \< this.M.length; k++) {

const d = this.M\[k\]! - prev\[k\]!;

s += d \* d;

}

const deltaNorm = Math.sqrt(s);

return { deltaNorm, converged: deltaNorm \< this.cfg.convergeEps };

}

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/metrics.ts

// Implements simulator metrics aligned to the papers:

// - Compression efficiency C = log2(∏ p(x\_i)) / Size(X)

// - Error correction rate Er = corrected / introduced

//
─────────────────────────────────────────────────────────────────────────────

export function compressionEfficiency(log2Product: number, sizeBits:
number): number {

if (sizeBits \<= 0) return 0;

return log2Product / sizeBits;

}

export function errorCorrectionRate(corrected: number, introduced:
number): number {

if (introduced \<= 0) return 1;

return corrected / introduced;

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/core/simulator.ts

// Orchestrates encode -\> inject/correct -\> tensor step -\> feedback
step -\> metrics

//
─────────────────────────────────────────────────────────────────────────────

import { z } from \"zod\";

import { makeRng } from \"./rng.js\";

import { PrimeEncoder } from \"./encoder.js\";

import { TensorNetwork } from \"./tensorNetwork.js\";

import { FeedbackLoop } from \"./feedback.js\";

import {

correctPrimeState,

initErrorState,

maybeInjectError,

type ErrorConfig,

} from \"./errorCorrection.js\";

import { compressionEfficiency, errorCorrectionRate } from
\"./metrics.js\";

export const MpceConfigZ = z.object({

run: z.object({

seed: z.number().int(),

steps: z.number().int().min(1),

logEvery: z.number().int().min(1).default(1)

}),

encoder: z.object({

dictionary: z.array(z.string()).min(1),

weights: z.array(z.number()).min(1),

epsilonStd: z.number().min(0),

historyWindow: z.number().int().min(1).default(8),

primeStartIndex: z.number().int().min(0).default(0),

crypto: z.object({ modulusQ: z.string().default(\"0\") }).default({
modulusQ: \"0\" })

}),

tensor: z.object({

nodes: z.array(z.string()).min(2),

edges: z.array(z.object({ from: z.number().int(), to: z.number().int(),
weight: z.number() })),

primeModulation: z.number().default(0.15)

}),

feedback: z.object({

learningRate: z.number().min(0),

noiseStd: z.number().min(0),

convergeEps: z.number().min(0),

maxMatrixSize: z.number().int().min(2).default(8)

}),

error: z.object({

injectRate: z.number().min(0).max(1),

errorPrimePool: z.array(z.string()).default(\[\"101\", \"103\", \"107\",
\"109\"\])

})

});

export type MpceConfig = z.infer\<typeof MpceConfigZ\>;

export type RunLogRow = {

t: number;

symbols: string\[\];

Fp: string;

encodedProduct: string;

correctedProduct: string;

compressionC: number;

lambdaMax: number;

feedbackDelta: number;

converged: boolean;

errIntroduced: number;

errCorrected: number;

errRate: number;

};

export class MpceSimulator {

readonly cfg: MpceConfig;

private rng;

private encoder;

private tensor;

private feedback;

private errCfg: ErrorConfig;

private errState = initErrorState();

constructor(cfg: MpceConfig) {

this.cfg = MpceConfigZ.parse(cfg);

this.rng = makeRng(this.cfg.run.seed);

const modulusQ = BigInt(this.cfg.encoder.crypto?.modulusQ ?? \"0\");

this.encoder = new PrimeEncoder(

{

dictionary: this.cfg.encoder.dictionary,

weights: this.cfg.encoder.weights,

epsilonStd: this.cfg.encoder.epsilonStd,

historyWindow: this.cfg.encoder.historyWindow,

primeStartIndex: this.cfg.encoder.primeStartIndex,

modulusQ

},

this.rng

);

this.tensor = new TensorNetwork(

{

nodes: this.cfg.tensor.nodes,

edges: this.cfg.tensor.edges,

primeModulation: this.cfg.tensor.primeModulation

},

this.rng

);

this.feedback = new FeedbackLoop(

{

learningRate: this.cfg.feedback.learningRate,

noiseStd: this.cfg.feedback.noiseStd,

convergeEps: this.cfg.feedback.convergeEps,

maxMatrixSize: this.cfg.feedback.maxMatrixSize

},

this.rng,

this.cfg.tensor.nodes.length

);

this.errCfg = {

injectRate: this.cfg.error.injectRate,

errorPrimePool: this.cfg.error.errorPrimePool.map((s) =\> BigInt(s))

};

}

private sampleSymbols(): string\[\] {

// Simple synthetic workload: randomly sample 3--7 symbols from the
dictionary.

const dict = this.cfg.encoder.dictionary;

const n = 3 + this.rng.int(0, 5);

const out: string\[\] = \[\];

for (let i = 0; i \< n; i++) out.push(dict\[this.rng.int(0,
dict.length)\]!);

return out;

}

step(t: number): RunLogRow {

const symbols = this.sampleSymbols();

const enc = this.encoder.encode(t, symbols);

// Inject errors on the product (simulation of noisy channel)

const modQ = BigInt(this.cfg.encoder.crypto?.modulusQ ?? \"0\");

const corrupted = maybeInjectError(this.rng, this.errCfg, enc.product,
modQ, this.errState);

// Correct using the paper-style gcd correction (simulate on the
product)

// NOTE: This is a simplification. In a fuller model you\'d correct per
prime state and propagate.

const { corrected, gcd } = correctPrimeState(corrupted,
this.errState.cumulativeE);

// Detection heuristic: if gcd \> 1, we assume an error was detected.

if (gcd \> 1n) this.errState.detectedCount++;

if (corrected !== corrupted) this.errState.correctedCount++;

// Tensor update uses dynamic prime states (more detailed signal than
product)

const ten = this.tensor.step(enc.dynamicStates);

// Feedback uses tensor state as R(t)

const fb = this.feedback.step(ten.state);

const compressionC = compressionEfficiency(enc.log2Product,
enc.sizeBits);

const errRate = errorCorrectionRate(this.errState.correctedCount,
this.errState.introduced.length);

return {

t,

symbols,

Fp: enc.Fp.toString(),

encodedProduct: enc.product.toString(),

correctedProduct: corrected.toString(),

compressionC,

lambdaMax: ten.lambdaMax,

feedbackDelta: fb.deltaNorm,

converged: fb.converged,

errIntroduced: this.errState.introduced.length,

errCorrected: this.errState.correctedCount,

errRate

};

}

run(): RunLogRow\[\] {

const rows: RunLogRow\[\] = \[\];

const steps = this.cfg.run.steps;

const logEvery = this.cfg.run.logEvery;

for (let t = 0; t \< steps; t++) {

const row = this.step(t);

if (t % logEvery === 0) rows.push(row);

if (row.converged) {

// still log the converged point

if (t % logEvery !== 0) rows.push(row);

break;

}

}

return rows;

}

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/index.ts

// Simple CLI runner: node dist/index.js ./src/config/example.mpce.json

//
─────────────────────────────────────────────────────────────────────────────

import { readFileSync } from \"node:fs\";

import { MpceSimulator } from \"./core/simulator.js\";

function main() {

const path = process.argv\[2\];

if (!path) {

console.error(\"Usage: node dist/index.js \<config.json\>\");

process.exit(1);

}

const raw = readFileSync(path, \"utf-8\");

const cfg = JSON.parse(raw);

const sim = new MpceSimulator(cfg);

const rows = sim.run();

// JSONL to stdout

for (const r of rows) console.log(JSON.stringify(r));

}

main();

//
─────────────────────────────────────────────────────────────────────────────

// FILE: src/ui/App.tsx (optional UI sketch; drop into any React+Vite
project)

//
─────────────────────────────────────────────────────────────────────────────

import React, { useMemo, useState } from \"react\";

import { MpceSimulator } from \"../core/simulator\";

type Row = ReturnType\<MpceSimulator\[\"run\"\]\>\[number\];

export default function App() {

const \[configText, setConfigText\] =
useState\<string\>(JSON.stringify({

run: { seed: 42, steps: 60, logEvery: 1 },

encoder: { dictionary: \[\"A\",\"B\",\"C\",\"D\"\], weights:
\[0.4,0.3,0.2,0.1\], epsilonStd: 0.5, historyWindow: 8, primeStartIndex:
0, crypto: { modulusQ: \"0\" } },

tensor: { nodes: \[\"enc\",\"tensor\",\"fb\"\], edges:
\[{from:0,to:1,weight:0.9},{from:1,to:2,weight:0.6},{from:2,to:1,weight:0.25}\],
primeModulation: 0.12 },

feedback: { learningRate: 0.08, noiseStd: 0.01, convergeEps: 1e-4,
maxMatrixSize: 6 },

error: { injectRate: 0.12, errorPrimePool:
\[\"101\",\"103\",\"107\",\"109\",\"113\"\] }

}, null, 2));

const \[rows, setRows\] = useState\<Row\[\]\>(\[\]);

const \[err, setErr\] = useState\<string\>(\"\");

const stats = useMemo(() =\> {

if (!rows.length) return null;

const last = rows\[rows.length - 1\]!;

return {

steps: rows.length,

compressionC: last.compressionC,

lambdaMax: last.lambdaMax,

feedbackDelta: last.feedbackDelta,

errRate: last.errRate,

converged: last.converged

};

}, \[rows\]);

const run = () =\> {

setErr(\"\");

try {

const cfg = JSON.parse(configText);

const sim = new MpceSimulator(cfg);

setRows(sim.run());

} catch (e: any) {

setErr(e?.message ?? String(e));

}

};

return (

\<div style={{ padding: 16, fontFamily: \"ui-sans-serif, system-ui\"
}}\>

\<h1 style={{ margin: 0 }}\>MPCE Simulator (Preview)\</h1\>

\<p style={{ marginTop: 6, color: \"\#555\" }}\>

Edit JSON config, run, and inspect metrics per tick.

\</p\>

\<div style={{ display: \"grid\", gridTemplateColumns: \"1fr 1fr\", gap:
12 }}\>

\<div\>

\<h3\>Config\</h3\>

\<textarea

value={configText}

onChange={(e) =\> setConfigText(e.target.value)}

rows={18}

style={{ width: \"100%\", fontFamily: \"ui-monospace, SFMono-Regular\",
fontSize: 12 }}

/\>

\<div style={{ display: \"flex\", gap: 8, marginTop: 8 }}\>

\<button onClick={run}\>Run\</button\>

{err ? \<span style={{ color: \"crimson\" }}\>{err}\</span\> : null}

\</div\>

\</div\>

\<div\>

\<h3\>Summary\</h3\>

{stats ? (

\<ul\>

\<li\>Steps: {stats.steps}\</li\>

\<li\>Compression C: {stats.compressionC.toFixed(4)}\</li\>

\<li\>λ\_max: {stats.lambdaMax.toFixed(4)}\</li\>

\<li\>Feedback Δ: {stats.feedbackDelta.toExponential(3)}\</li\>

\<li\>Error correction rate: {(stats.errRate \* 100).toFixed(1)}%\</li\>

\<li\>Converged: {String(stats.converged)}\</li\>

\</ul\>

) : (

\<p\>No run yet.\</p\>

)}

\<h3\>Rows (JSON)\</h3\>

\<pre style={{ height: 260, overflow: \"auto\", background:
\"\#f6f6f6\", padding: 8 }}\>

{rows.map((r) =\> JSON.stringify(r)).join(\"\\n\")}

\</pre\>

\</div\>

\</div\>

\</div\>

);

}

//
─────────────────────────────────────────────────────────────────────────────

// FILE: scripts/mpce\_math.fsx (optional F\# script for sanity checks)

// Run: dotnet fsi scripts/mpce\_math.fsx

//
─────────────────────────────────────────────────────────────────────────────

(\*\*\*

open System

let rec gcd (a: bigint) (b: bigint) : bigint =

if b = 0I then abs a else gcd b (a % b)

let isPrime (n:int) =

if n \<= 1 then false

elif n \<= 3 then true

elif n % 2 = 0 \|\| n % 3 = 0 then false

else

let mutable i = 5

let mutable ok = true

while ok && i\*i \<= n do

if n % i = 0 \|\| n % (i+2) = 0 then ok \<- false

i \<- i + 6

ok

let nthPrime (k:int) =

let mutable count = -1

let mutable x = 1

while count \< k do

x \<- x + 1

if isPrime x then count \<- count + 1

x

// p\_corrected = phi(pij) / gcd(phi(pij), E)

let correctPrimeState (phiPij: bigint) (E: bigint) =

let g = gcd phiPij E

if g = 0I then phiPij else phiPij / g

// Demo: treat error as multiplicative prime factor

let basePrime = bigint (nthPrime 5) // 13

let Fp = 3I

let phiPij = basePrime \* Fp // 39

let errorPrime = 101I

let E = errorPrime

let corrupted = phiPij \* errorPrime // 3939

let corrected = correctPrimeState corrupted E

printfn \"base=%A Fp=%A phiPij=%A\" basePrime Fp phiPij

printfn \"corrupted=%A E=%A corrected=%A\" corrupted E corrected

\*\*\* )
