---
slug: design-microbenchmarks-to-isolate-kernel-overhea
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "05-systems/\u03A0\u2011kernel/Design microbenchmarks to isolate \u03A0\u2011\
    Kernel overhea.md"
  last_synced: '2026-03-20T17:17:17.825583Z'
---

![](media/image-7a84d2820cbdfa20c539f9ca47c6492299a4fc18.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**Design microbenchmarks to isolate Π‑Kernel overhead**

Based on the Π-Kernel reference implementation and mathematical
specification, here is a complete microbenchmark suite to isolate each
source of overhead:

**Microbenchmark Suite Overview**

The suite isolates six distinct overhead components: projection,
proposal, ACE safety projection, certificate computation, synthesis, and
ledger commit.[^[\[1\]]{.underline}^](#fn1)[^[\[2\]]{.underline}^](#fn2)

**Benchmark 1: Projection Overhead**

Measures the cost of extracting Π-atom coefficients
$\mathit{c}_{\mathit{\pi}} = \mathit{R}_{\mathit{\pi}}\mathit{x}$.

import numpy as np\
import time\
\
def bench\_projection(grid, x, trials=10000):\
\"\"\"Isolate projection cost: grid.project(x, pi) for all pi\"\"\"\
piids = grid.piids\
\
\# Warm-up\
for \_ in range(100):\
for pi in piids:\
\_ = grid.project(x, pi)\
\
times = \[\]\
for \_ in range(trials):\
t0 = time.perf\_counter\_ns()\
coeffs = {pi: grid.project(x, pi) for pi in piids}\
times.append(time.perf\_counter\_ns() - t0)\
\
return {\
\'mean\_ns\': np.mean(times),\
\'std\_ns\': np.std(times),\
\'per\_atom\_ns\': np.mean(times) / len(piids),\
\'per\_element\_ns\': np.mean(times) / x.size\
}

**Scaling parameters**: Vary n (ambient dimension) and m (number of
Π-atoms).[^[\[2\]]{.underline}^](#fn2)

**Benchmark 2: Proposal Generation**

Measures proposer latency
$\mathit{F}_{\mathit{\pi}}(\mathit{c}_{\mathit{\pi}})$ in isolation.

def bench\_proposer(proposer, coeffs, trials=10000):\
\"\"\"Isolate proposer cost: proposer(c\_pi) for each atom\"\"\"\
piids = list(coeffs.keys())\
\
times = \[\]\
for \_ in range(trials):\
t0 = time.perf\_counter\_ns()\
proposals = {pi: proposer(coeffs\[pi\]) for pi in piids}\
times.append(time.perf\_counter\_ns() - t0)\
\
return {\
\'mean\_ns\': np.mean(times),\
\'per\_atom\_ns\': np.mean(times) / len(piids)\
}

**Variants to test**:

-   DefaultProposer(gamma=0.1) --- simple
    damping[^[\[1\]]{.underline}^](#fn1)

-   Custom gradient-based proposers

-   Rule-synthesis proposers

**Benchmark 3: Weighted-**$\mathit{\ell}_{1}$ **Projection (ACE
Safety)**

The bisection-based soft-threshold is the core ACE
overhead.[^[\[3\]]{.underline}^](#fn3)[^[\[1\]]{.underline}^](#fn1)

from pikernel import projectweightedl1ball\
\
def bench\_l1\_projection(v, w, tau, trials=10000):\
\"\"\"Isolate ACE projection: bisection soft-threshold\"\"\"\
times = \[\]\
iterations = \[\]\
\
for \_ in range(trials):\
t0 = time.perf\_counter\_ns()\
x\_safe, lam = projectweightedl1ball(v, w, tau)\
times.append(time.perf\_counter\_ns() - t0)\
\
return {\
\'mean\_ns\': np.mean(times),\
\'std\_ns\': np.std(times),\
\'per\_element\_ns\': np.mean(times) / v.size\
}\
\
\# Sweep test: vary ball radius tau relative to \|\|v\|\|\_1\
def sweep\_l1\_tightness(n=256, trials=1000):\
\"\"\"How projection cost scales with constraint tightness\"\"\"\
v = np.random.randn(n)\
w = np.ones(n)\
v\_norm = np.sum(w \* np.abs(v))\
\
results = \[\]\
for ratio in \[0.1, 0.3, 0.5, 0.7, 0.9, 1.0, 1.5, 2.0\]:\
tau = ratio \* v\_norm\
r = bench\_l1\_projection(v, w, tau, trials)\
r\[\'tau\_ratio\'\] = ratio\
r\[\'inside\_ball\'\] = ratio \>= 1.0\
results.append(r)\
return results

**Key insight**: When
$\sum_{\mathit{i}}\mspace{2mu}\mathit{w}_{\mathit{i}}|\mathit{v}_{\mathit{i}}| \leq \mathit{\tau}$,
the projection returns v unchanged with zero bisection iterations
[^[\[1\]]{.underline}^](#fn1).

**Benchmark 4: Certificate Computation**

Measures SlopeUB and GapLB computation from coupling matrix
$\mathit{K}$.[^[\[3\]]{.underline}^](#fn3)[^[\[2\]]{.underline}^](#fn2)

from pikernel import slopeupperbound, gaplowerbound\
\
def bench\_certificates(m\_values, trials=10000):\
\"\"\"Isolate certificate cost: scales as O(m\^2) for dense K\"\"\"\
results = \[\]\
\
for m in m\_values:\
alphas = np.full(m, 0.25)\
K = 0.05 \* np.ones((m, m))\
np.fill\_diagonal(K, 0.0)\
\
times = \[\]\
for \_ in range(trials):\
t0 = time.perf\_counter\_ns()\
slope = slopeupperbound(alphas, K)\
gap = gaplowerbound(slope)\
times.append(time.perf\_counter\_ns() - t0)\
\
results.append({\
\'m\': m,\
\'mean\_ns\': np.mean(times),\
\'per\_m2\_ns\': np.mean(times) / (m \* m)\
})\
return results

**Expected scaling**: $\mathit{O}(\mathit{m}^{2})$ for the matrix
construction, $\mathit{O}(\mathit{m})$ for row-sum
($\| \cdot \|_{\infty}$) [^[\[2\]]{.underline}^](#fn2).

**Benchmark 5: Synthesis/Recomposition**

Measures the cost of
$\mathit{x}_{\text{new}} = \sum_{\mathit{\pi}}\mspace{2mu}\mathit{R}_{\mathit{\pi}}^{\mathit{T}}\mathit{c}_{\mathit{\pi}}$.[^[\[2\]]{.underline}^](#fn2)

def bench\_synthesis(grid, coeffs, trials=10000):\
\"\"\"Isolate synthesis cost: sum of projector applications\"\"\"\
piids = grid.piids\
n = grid.dim\
\
times = \[\]\
for \_ in range(trials):\
t0 = time.perf\_counter\_ns()\
xnew = np.zeros(n)\
for pi in piids:\
xnew += coeffs\[pi\] \# For index-based projectors\
times.append(time.perf\_counter\_ns() - t0)\
\
return {\
\'mean\_ns\': np.mean(times),\
\'per\_atom\_ns\': np.mean(times) / len(piids)\
}

**Benchmark 6: Ledger Commit**

Measures hash computation and I/O for audit
trail.[^[\[1\]]{.underline}^](#fn1)[^[\[3\]]{.underline}^](#fn3)

from pikernel import Ledger, PoseidonLedger\
import tempfile\
\
def bench\_ledger(ledger\_class, record, trials=1000):\
\"\"\"Isolate ledger commit cost: hash + append\"\"\"\
with tempfile.NamedTemporaryFile(suffix=\'.jsonl\') as f:\
ledger = ledger\_class(f.name)\
\
\# Warm-up\
for \_ in range(10):\
ledger.append(record)\
\
times = \[\]\
for \_ in range(trials):\
t0 = time.perf\_counter\_ns()\
ledger.append(record)\
times.append(time.perf\_counter\_ns() - t0)\
\
return {\
\'mean\_ns\': np.mean(times),\
\'std\_ns\': np.std(times)\
}\
\
\# Compare SHA-256 vs Poseidon\
def compare\_ledgers():\
record = {\'pi\': \[0, 1\], \'alpha\': 0.25, \'tau\': 1.5,
\'lambda\_soft\': 0.1}\
return {\
\'sha256\': bench\_ledger(Ledger, record),\
\'poseidon\': bench\_ledger(PoseidonLedger, record)\
}

**Benchmark 7: End-to-End Step Breakdown**

Instruments a full kernel.step() to attribute
overhead.[^[\[1\]]{.underline}^](#fn1)

def bench\_step\_breakdown(kernel, x, trials=1000):\
\"\"\"Full step with per-phase timing\"\"\"\
phases = \[\'project\', \'propose\', \'l1proj\', \'cert\',
\'synthesis\', \'ledger\'\]\
timings = {p: \[\] for p in phases}\
\
for \_ in range(trials):\
\# Phase 1: Projection\
t0 = time.perf\_counter\_ns()\
coeffs = {pi: kernel.grid.project(x, pi) for pi in kernel.piids}\
timings\[\'project\'\].append(time.perf\_counter\_ns() - t0)\
\
\# Phase 2: Proposal\
t0 = time.perf\_counter\_ns()\
proposals = {pi: kernel.proposer(coeffs\[pi\]) for pi in kernel.piids}\
timings\[\'propose\'\].append(time.perf\_counter\_ns() - t0)\
\
\# Phase 3: ACE projection\
t0 = time.perf\_counter\_ns()\
safe = {}\
for pi in kernel.piids:\
safe\[pi\], \_ = projectweightedl1ball(\
proposals\[pi\], kernel.weights\[pi\], kernel.tau\[pi\]\
)\
timings\[\'l1proj\'\].append(time.perf\_counter\_ns() - t0)\
\
\# Phase 4: Certificates\
t0 = time.perf\_counter\_ns()\
alphas = np.array(\[kernel.alphas\[pi\] for pi in kernel.piids\])\
slope = slopeupperbound(alphas, kernel.K)\
gap = gaplowerbound(slope)\
timings\[\'cert\'\].append(time.perf\_counter\_ns() - t0)\
\
\# Phase 5: Synthesis\
t0 = time.perf\_counter\_ns()\
xnew = sum(safe\[pi\] for pi in kernel.piids)\
timings\[\'synthesis\'\].append(time.perf\_counter\_ns() - t0)\
\
\# Phase 6: Ledger (if enabled)\
if kernel.ledger:\
t0 = time.perf\_counter\_ns()\
kernel.ledger.append({\'pi\': list(kernel.piids\[\^0\])})\
timings\[\'ledger\'\].append(time.perf\_counter\_ns() - t0)\
\
x = xnew\
\
return {p: {\'mean\_ns\': np.mean(v), \'pct\': 0} for p, v in
timings.items()}

**Benchmark 8: Projector Family Comparison**

Compare overhead across different projector
types.[^[\[4\]]{.underline}^](#fn4)[^[\[1\]]{.underline}^](#fn1)

  ------------------- -------------------------------------------- -------------------------------------------------------------------- ------ ----------------
  Benchmark           Setup                                        Expected Complexity                                                         
  **Index-based**     ProjectorFamily(\[\[0,1\],\[2,3\]\], \...)   (O(                                                                  S\_k   )) array slice
  **Spectral**        eighprojectors(L, bands)                     $\mathit{O}(\mathit{n}^{2})$ setup, $\mathit{O}(\mathit{n})$ apply          
  **RNS encode**      rns.encode(x)                                $\mathit{O}(\mathit{L}\mathit{n})$ modular reduction                        
  **RNS decode**      rns.decode(residues)                         $\mathit{O}(\mathit{L}\mathit{n})$ CRT reconstruction                       
  **Poseidon hash**   poseidon.hash(limbs)                         $\mathit{O}(65 \cdot \mathit{t})$ field ops                                 
  ------------------- -------------------------------------------- -------------------------------------------------------------------- ------ ----------------

def bench\_projector\_types(n=256):\
\"\"\"Compare projector family overhead\"\"\"\
from pikernel import RNS, eighprojectors\
\
x = np.random.randn(n)\
results = {}\
\
\# Index-based (baseline)\
from pikernel import ProjectorFamily, PiIndexGrid\
A = ProjectorFamily(\[list(range(0, n//2)), list(range(n//2, n))\],
name=\'A\')\
grid = PiIndexGrid(\[A\])\
results\[\'index\'\] = bench\_projection(grid, x, trials=5000)\
\
\# Spectral bands\
L = 2\*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)\
bands = \[(0, 1.0), (1.0, 2.5), (2.5, 4.0)\]\
U, evals, masks = eighprojectors(L, bands)\
\# \... benchmark apply\_band\_projector\
\
\# RNS encode/decode\
moduli = \[65521, 65519, 65513\]\
rns = RNS(moduli)\
xint = np.random.randint(0, 10000, size=n, dtype=object)\
\# \... benchmark encode/decode\
\
return results

**Expected Results Summary**

  -------------------------------- ---------------------- -----------------------------------------
  Component                        Target (n=256, m=16)   Dominant Factor
  Projection                       \< 500 ns/atom         Memory access
  Proposal                         Domain-dependent       Proposer complexity
  $\mathit{\ell}_{1}$-projection   \< 2 μs/atom           Bisection iterations (\~20)
  Certificates                     \< 500 ns total        $\mathit{O}(\mathit{m}^{2})$ matrix ops
  Synthesis                        \< 500 ns/atom         Memory write
  SHA-256 ledger                   \~1 μs/record          Hash + I/O
  Poseidon ledger                  \~10 μs/record         Field arithmetic
  -------------------------------- ---------------------- -----------------------------------------

**Total step overhead**: Target **\< 50 μs** for
$\mathit{m} = 16,\mathit{n} = 256$ with 10% touched
atoms.[^[\[2\]]{.underline}^](#fn2)

**Running the Suite**

if \_\_name\_\_ == \'\_\_main\_\_\':\
from pikernel import ProjectorFamily, PiIndexGrid, PiKernel, Ledger\
\
\# Setup\
n, m\_families = 256, 4\
families = \[ProjectorFamily(\
\[list(range(i\*n//m\_families, (i+1)\*n//m\_families))\],\
name=f\'F{i}\'\
) for i in range(m\_families)\]\
grid = PiIndexGrid(families)\
\
x = np.random.randn(n)\
\
\# Run benchmarks\
print(\"Projection:\", bench\_projection(grid, x))\
print(\"L1 sweep:\", sweep\_l1\_tightness())\
print(\"Certificates:\", bench\_certificates(\[4, 16, 64, 256\]))\
print(\"Ledger:\", compare\_ledgers())

⁂

1.  P-Kernel-1.pdf

2.  P-kernel-A-Mathematical-Note.pdf

3.  P-kernel-Multiplicity-Runtime-Bridge-A-Mathematical-Note.pdf

4.  P-Kernel.pdf

5.  [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/23bd1879-ef01-4906-a675-ebf35515107d/Mr-Boundary-Theory-Zero-As-Boundary-Operator-roles-M-And-Spectral-Tests.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/23bd1879-ef01-4906-a675-ebf35515107d/Mr-Boundary-Theory-Zero-As-Boundary-Operator-roles-M-And-Spectral-Tests.pdf)

6.  [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/7360180a-eb07-467f-bffc-c4f35c5bafc7/Modes-Of-Infinity-As-Modes-Of-Being-Formalization-Blueprint.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/7360180a-eb07-467f-bffc-c4f35c5bafc7/Modes-Of-Infinity-As-Modes-Of-Being-Formalization-Blueprint.pdf)

7.  [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/694b3c1d-d7eb-4aee-8bd8-83063abfd89f/Ccn-V2-Minimal-Axioms-Representation-Theorem-finite-Case.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/694b3c1d-d7eb-4aee-8bd8-83063abfd89f/Ccn-V2-Minimal-Axioms-Representation-Theorem-finite-Case.pdf)

8.  [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/0d7783d8-4cc2-4204-8b05-e7565198bfab/Alp-The-Auditable-Landauer-Principle-canvas-Package.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/0d7783d8-4cc2-4204-8b05-e7565198bfab/Alp-The-Auditable-Landauer-Principle-canvas-Package.pdf)

9.  [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/e2d110f3-9a3b-4ac7-a00e-b68fd9b45984/Ofa-ii-Iterator-Arithmetic-Reference-Spec-V1.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/e2d110f3-9a3b-4ac7-a00e-b68fd9b45984/Ofa-ii-Iterator-Arithmetic-Reference-Spec-V1.pdf)

10. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/d00c501d-9bcd-417a-a1dd-acc4b1d7653b/Determinacy-Algebra-Being-Becoming-And-Laws-That-Bite-canvas-Edition.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/d00c501d-9bcd-417a-a1dd-acc4b1d7653b/Determinacy-Algebra-Being-Becoming-And-Laws-That-Bite-canvas-Edition.pdf)

11. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/17668332-59bb-4e97-b781-866734f1be86/Lawful-Composition-Calculus-lcc-Associator-Spectroscopy-V0.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/17668332-59bb-4e97-b781-866734f1be86/Lawful-Composition-Calculus-lcc-Associator-Spectroscopy-V0.pdf)

12. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/61beb223-02cc-4d6e-b5e4-ae047b8200cf/Associator-Spectroscopy-Osf-ready-Prereg-Pilot-References.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/61beb223-02cc-4d6e-b5e4-ae047b8200cf/Associator-Spectroscopy-Osf-ready-Prereg-Pilot-References.pdf)

13. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/45419ca8-9742-46bf-93c6-646aad344629/Boundary-spectral-Governance-Regime-Dossier-System-v1.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/45419ca8-9742-46bf-93c6-646aad344629/Boundary-spectral-Governance-Regime-Dossier-System-v1.pdf)

14. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/012ab520-abfa-4b33-85b4-db7596f61739/Operational-Negatives-Preregistration-Package-canvas.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/012ab520-abfa-4b33-85b4-db7596f61739/Operational-Negatives-Preregistration-Package-canvas.pdf)

15. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/0ca7a26a-c4b8-49cc-ab00-b474faeb97f4/Moral-continuity-Ledger-mcl-Rc1.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/0ca7a26a-c4b8-49cc-ab00-b474faeb97f4/Moral-continuity-Ledger-mcl-Rc1.pdf)

16. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/f710e95f-6bda-43a8-95d1-357ee22e3cfb/Ac-os-V0.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/f710e95f-6bda-43a8-95d1-357ee22e3cfb/Ac-os-V0.pdf)

17. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/0950f529-1af9-4db7-8557-e5c4ec8931d2/Qpf-Lab-Associator-Spectroscopy-final-Engineering-Spec.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/0950f529-1af9-4db7-8557-e5c4ec8931d2/Qpf-Lab-Associator-Spectroscopy-final-Engineering-Spec.pdf)

18. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/cb831e8e-630a-4ac3-8996-9c3defd878a6/Two-ness-Clinics-The-Receipt-Test-executable-Program-References.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/cb831e8e-630a-4ac3-8996-9c3defd878a6/Two-ness-Clinics-The-Receipt-Test-executable-Program-References.pdf)

19. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/b83d0758-82f9-4822-b64d-3dcbf7f72970/Spin\_Foam\_Microfoundations.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/b83d0758-82f9-4822-b64d-3dcbf7f72970/Spin_Foam_Microfoundations.pdf)

20. Kernelized-Sieve-Framework-Simulator-B-d-window-Multiplicity-Stability-Diagram.pdf

21. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/a141816b-9334-4946-9217-8704fe9aac9d/Entangled-Aggregation\_-Non-associativity-As-A-Closure-Defect-Under-Coarse-grained-Composition.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/a141816b-9334-4946-9217-8704fe9aac9d/Entangled-Aggregation_-Non-associativity-As-A-Closure-Defect-Under-Coarse-grained-Composition.pdf)

22. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/cde50055-3feb-4652-99d3-39b81cc1c0ae/Becoming-two-Vs-Being-two-Twoness-As-Functorial-Forgetting-with-External-References.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/cde50055-3feb-4652-99d3-39b81cc1c0ae/Becoming-two-Vs-Being-two-Twoness-As-Functorial-Forgetting-with-External-References.pdf)

23. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/3290f19e-4112-44fb-9470-017f509e944f/Qpf-Methods-Protocol-gallows-proof-V1.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/3290f19e-4112-44fb-9470-017f509e944f/Qpf-Methods-Protocol-gallows-proof-V1.pdf)

24. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/ade039ff-edad-4017-b2e4-061bef5d53fb/Modal-Numerosity-As-Algorithmic-Inference-Camera-ready-Package.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/ade039ff-edad-4017-b2e4-061bef5d53fb/Modal-Numerosity-As-Algorithmic-Inference-Camera-ready-Package.pdf)

25. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/61bf5339-7360-4f5d-9e4d-51a40a6e0a77/Where-Do-Negatives-Come-From\_-Operational-Closure-Completion-And-Baselines.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/61bf5339-7360-4f5d-9e4d-51a40a6e0a77/Where-Do-Negatives-Come-From_-Operational-Closure-Completion-And-Baselines.pdf)
