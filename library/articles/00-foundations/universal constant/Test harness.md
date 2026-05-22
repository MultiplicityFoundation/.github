---
slug: test-harness
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/universal constant/Test harness.md
  last_synced: '2026-03-20T17:17:22.189941Z'
---

Good --- if the harness's job is to **actually break bounds**, you
should treat **C-CRIT** and **C-LOC-ONLY** as *attack surfaces*, not
"theorems."

Here's a design that will produce **immediate 2×2 counterexamples**,
then scale to systematic search + shrinking.

**0) Non-negotiable framing**
-----------------------------

### **What you're testing (and what you're not)**

-   **C-CRIT**: "Λ = 1/ρ(S) is a safe stability constant."\
    > ✅ **FALSIFIABLE** (fails on non-normal matrices; you can break it
    > in 2×2).

-   **C-LOC-ONLY**: "Λ = γ/r(T) alone ensures stability."\
    > ✅ **FALSIFIABLE** (fails even with r(T)=1, again in 2×2).

-   **C-GLOB**: "Λ = γ/\|\|S\|\| gives contraction."\
    > Not a math target --- it's basically a **norm-computation
    > correctness test**.

So the harness should be built to **find and minimize counterexamples**
for CRIT and LOC-ONLY, not "confirm" anything.

**1) The "killer" unit tests you bake in on day 1**
---------------------------------------------------

### **Minimal CRIT breaker (2×2, integer entries, smallest magnitude)**

Use the shear/Jordan matrix:

S=(1101)S=\\begin{pmatrix}1 & 1\\\\ 0 & 1\\end{pmatrix}S=(10​11​)

-   Spectral radius: ρ(S)=1 ⇒ Λcrit=1

-   But operator 2-norm: \|\|S\|\|₂ = φ ≈ 1.618\
    > (exactly sqrt((3+sqrt 5)/2))

**Oracle:** contraction requires \|\|Λ S\|\| \< 1 (or ≤γ).\
Here: \|\|Λcrit S\|\| = \|\|S\|\|₂ ≈ 1.618 \> 1 ⇒ **FAIL**.

This is the smallest, cleanest "Λcrit is unsafe" certificate. No fuzzing
needed.

### **Minimal LOC-ONLY breaker (same S, simplest T)**

Pick Euclidean inner product, T = e1 = (1,0)ᵀ.\
Then:

-   r(T) = \<T, S T\> / \|\|T\|\|² = 1

-   Λloc = γ / r(T) = γ

-   But \|\|Λloc S\|\|₂ = γ\|\|S\|\|₂

For γ = 0.9, you get 0.9 \* 1.618 = 1.456 \> 1 ⇒ **FAIL**.

So the harness proves: **local-only gate doesn't protect you globally**.

These two tests should be hard-coded regression tests. If they *don't*
fail, your harness is broken.

**2) Harness architecture: make counterexamples first-class artifacts**
-----------------------------------------------------------------------

### **Core entities**

**Case**

-   dimension n

-   operator S (real/complex matrix)

-   declared norm (op2 / op1 / op∞)

-   declared inner product (needed for r(T))

-   optional projectors P\_p (you can ignore projectors initially by
    > setting PN={I})

**Policy under test**

-   CRIT: Λ = 1/ρ(S)

-   LOC-ONLY: Λ = γ / r(T) (with declared T choice rule)

**Oracle**

-   O1 (norm-based): compute c = \|\|Λ S\|\|; FAIL if c ≥ 1 - tol (or
    > c \> γ + tol if you're testing a γ-bound claim)

-   O2 (trajectory-based): pick x0,y0; FAIL if distance doesn't contract
    > (optional, but useful when someone tries to dodge with norm hacks)

**Counterexample artifact**

-   manifest (norm, γ, tol, policy)

-   exact matrix entries (prefer rationals/ints)

-   computed ρ(S), \|\|S\|\|, \|\|ΛS\|\|, r(T)

-   "minimality score" (see shrinker section)

Output should be machine-readable JSON plus a human summary.

**3) Generator families that *systematically* break CRIT and LOC-ONLY**
-----------------------------------------------------------------------

### **Family A: Shears (the guaranteed CRIT killer)**

S(M)=(1M01),M∈ZS(M)=\\begin{pmatrix}1 & M\\\\ 0 & 1\\end{pmatrix},\\quad
M\\in\\mathbb{Z}S(M)=(10​M1​),M∈Z

-   ρ(S)=1 always ⇒ Λcrit=1

-   \|\|S\|\| grows with \|M\| ⇒ CRIT fails for any M≠0 under any
    > induced operator norm that "sees" the shear.

This family makes your harness *deterministic*.

### **Family B: Similarity-amplified non-normality (pseudospectral stress)**

S=VJV−1,J=(1101)S = VJV\^{-1},\\quad J=\\begin{pmatrix}1 & 1\\\\ 0 &
1\\end{pmatrix}S=VJV−1,J=(10​11​)

Eigenvalues unchanged (ρ=1), but you can make \|\|S\|\| arbitrarily
large by making V ill-conditioned.\
This is how you generate "spectral radius looks fine but transient blows
up."

### **Family C: Random near-Jordan blocks (3×3, 4×4)**

Upper triangular with ones on the diagonal and random integers above.\
This tends to create large \|\|S\|\|/ρ(S) ratios and is great for
fuzzing.

**4) Search strategy: brute → fuzz → shrink**
---------------------------------------------

### **Phase 1: brute force (smallest counterexample guarantee)**

Start with n=2, integer entries in {-B,...,B}, but constrain to
structured families first:

-   Shear family \[\[1,M\],\[0,1\]\] with M in {0,±1,±2,...}

-   For each M:

    -   CRIT: compute ρ(S), Λ=1/ρ, check \|\|ΛS\|\|

    -   LOC-ONLY: choose T candidates (e1,e2, random unit vectors),
        > compute r(T), Λ=γ/r(T), check \|\|ΛS\|\|

You'll immediately report M=±1 as the minimal integer counterexample.

### **Phase 2: fuzzing (find "weird" failures)**

Randomly generate:

-   S = D + N where D diagonal, N strictly upper-triangular sparse

-   Random similarity transforms (bounded cond(V) so you don't drown in
    > numeric artifacts)

### **Phase 3: shrinker (make the counterexample embarrassing)**

Given a failing case, reduce in this order:

1.  **dimension** (try to project to invariant subspace / drop rows/cols
    > if failure persists)

2.  **PN size** (if projectors exist, drop them)

3.  **entry magnitudes** (round toward 0 / small integers)

4.  **structure** (force triangular / Jordan form)

**Minimality score** example:\
score = (n, max\_abs\_entry, nnz, \|PN\|) lexicographically.

Your goal: return "2×2 with entries {0,1}" whenever possible.

**5) LOC-ONLY needs a declared "T selection rule" or it becomes slippery**
--------------------------------------------------------------------------

If someone is allowed to pick T adversarially *after* seeing S, LOC-ONLY
can be made to "look okay" in toy cases. So your harness should force a
**T protocol**:

Pick one (or test all):

-   **Fixed basis vectors**: T ∈ {e1,...,en}

-   **Worst-case T**: search over many unit vectors to maximize
    > \|\|ΛS\|\| (this is the honest adversary)

-   **Trajectory T**: T is current state vector (if that's what they
    > claim)

For "break it fast," use **fixed basis** first --- it already fails.

**6) Implementation requirements (so the harness doesn't lie)**
---------------------------------------------------------------

### **Norm computation**

To avoid fake results:

-   op2: SVD for n ≤ \~200 (exact enough)

-   op1: max column sum (exact)

-   op∞: max row sum (exact)

Avoid Frobenius as a "stability certificate" norm unless explicitly
declared as non-induced.

### **Spectral radius**

For small n: eigenvalues directly.\
For fuzzed larger n: approximate is fine, because you're not proving
safety --- you're hunting failures. But when you *report* a
counterexample, re-check it at small n with high precision.

### **Tolerances**

Use tight tolerances (1e-12 scale) and treat "near-boundary" as "needs
recheck," not as a win.

**7) What the harness should report (example)**
-----------------------------------------------

When it finds the minimal breaker:

-   **Target**: C-CRIT

-   **S** = \[\[1,1\],\[0,1\]\]

-   ρ(S)=1 ⇒ Λcrit=1

-   \|\|ΛS\|\|₂ = 1.618... ≥ 1 ⇒ **COUNTEREXAMPLE\
    > **

And for LOC-ONLY (γ=0.9, T=e1):

-   r(T)=1 ⇒ Λloc=0.9

-   \|\|ΛS\|\|₂ = 1.456... ≥ 1 ⇒ **COUNTEREXAMPLE\
    > **

That's clean, reproducible, and impossible to hand-wave away.

**8) Reality check: what this buys you**
----------------------------------------

-   You will **kill** the CRIT and LOC-ONLY universality claims
    > immediately.

-   You will force any "fixed" theory to either:

    1.  restrict assumptions to normal/self-adjoint/orthogonal cases, or

    2.  adopt the **global cap** (hybrid) and admit conservatism.

That's a real win: it prevents wasting months on a branch that only
works on nice matrices.

If you want, I can give you a concrete CLI spec + JSON schema + a
minimal Python reference implementation skeleton next (no fluff, just
enough to run and emit the 2×2 counterexamples on command).
