---
slug: benchmark-plan-to-measure-kernel-latency-overhea
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "05-systems/\u03A0\u2011kernel/Benchmark plan to measure \u03A0\u2011Kernel\
    \ latency overhea.md"
  last_synced: '2026-03-20T17:17:17.898837Z'
---

![](media/image-f6ab3230c798e15f083a1cd3e6699f33b7f83167.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**Benchmark plan to measure Π‑Kernel latency overhead**

Based on the Π-Kernel architecture and standard benchmarking
methodologies, here is a comprehensive benchmark plan to measure
Π-Kernel latency overhead:

**Benchmark Objectives**

The plan measures three categories of overhead: (1) per-Π-atom
projection/synthesis latency, (2) ACE safety envelope computation
(SlopeUB/GapLB), and (3) ledger commit
costs.[^[\[1\]]{.underline}^](#fn1)[^[\[2\]]{.underline}^](#fn2)

**Phase 1: Baseline Measurements**

**Raw Operation Microbenchmarks**

  ---------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------- --------------------------------------------------------------------------
  Operation                                                                                                        Measurement Target                                                   Method
  **Projection** $\mathit{c}_{\mathit{\pi}} = \mathit{R}_{\mathit{\pi}}\mathit{x}$                                 Time per Π-atom coefficient extraction                               Dependency chain timing with perf counters [^[\[3\]]{.underline}^](#fn3)
  **Synthesis** $\sum_{\mathit{\pi}}\mspace{2mu}\mathit{R}_{\mathit{\pi}}^{\mathit{T}}\mathit{c}_{\mathit{\pi}}$   Recomposition latency                                                Wall-clock + GPU event timing [^[\[4\]]{.underline}^](#fn4)
  **Weighted-**$\mathit{\ell}_{1}$ **projection**                                                                  ACE soft-threshold bisection                                         Isolate projectweightedl1ball() calls [^[\[5\]]{.underline}^](#fn5)
  **SlopeUB computation**                                                                                          $\|\mathit{A}\|_{\infty}$ from $\mathit{\alpha},\mathit{K}$ matrix   Matrix norm overhead per step [^[\[1\]]{.underline}^](#fn1)
  ---------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------- --------------------------------------------------------------------------

**Test Harness Setup**

\# Timing scaffold for Π-Kernel step\
import time\
import numpy as np\
\
def benchmark\_step(kernel, x, warmup=100, trials=1000):\
\# Warm-up phase (thermal stabilization) \[web:59\]\
for \_ in range(warmup):\
kernel.step(x)\
\
timings = {\'project\': \[\], \'propose\': \[\], \'l1proj\': \[\],\
\'certificates\': \[\], \'synthesis\': \[\], \'ledger\': \[\]}\
\
for \_ in range(trials):\
\# Instrument each phase separately\
t0 = time.perf\_counter\_ns()\
coeffs = {pi: kernel.grid.project(x, pi) for pi in kernel.piids}\
timings\[\'project\'\].append(time.perf\_counter\_ns() - t0)\
\# \... continue for each phase\
\
return {k: (np.mean(v), np.std(v)) for k, v in timings.items()}

**Phase 2: Scaling Experiments**

**Grid Size Sweep**

Measure latency as a function of Π-atom count
$\mathit{m} = |\text{piids}|$:

-   **Small**: $\mathit{m} = 4$ (2×2 family grid)

-   **Medium**: $\mathit{m} = 16$ (4×4 or 2×2×2×2)

-   **Large**: $\mathit{m} = 64$ (spectral bands × RNS lanes × wavelet
    packets)

-   **Production**: $\mathit{m} = 256 +$ (full tensor factorization)

**Dimension Sweep**

Fix $\mathit{m}$ and vary ambient dimension $\mathit{n}$:

$$\mathit{n} \in \{ 64,256,1024,4096,16384\}$$

Expected complexity: projection is $\mathit{O}(\mathit{n})$ per atom,
synthesis is $\mathit{O}(\mathit{m}\mathit{n})$, certificates are
$\mathit{O}(\mathit{m}^{2})$ for the coupling matrix
$\mathit{K}$.[^[\[1\]]{.underline}^](#fn1)

**Phase 3: Component Breakdown**

**Per-Phase Latency Attribution**

  ------------------------------------------------------------------------ ----------------------------------- --------------------------------------------------------
  Phase                                                                    Expected Dominant Cost              Metric
  **1. Projection**                                                        Memory bandwidth                    $\mathit{t}_{\text{proj}}/\mathit{n}$ (ns/element)
  **2. Proposal** $\mathit{F}_{\mathit{\pi}}(\mathit{c}_{\mathit{\pi}})$   Domain-dependent                    Profile proposer() separately
  **3. ACE** $\mathit{\ell}_{1}$**-projection**                            Bisection iterations                $$\mathit{t}_{\text{l1}}/(\log(1/\mathit{\epsilon}))$$
  **4. Certificate computation**                                           $\|\mathit{A}\|_{\infty}$ row-sum   $$\mathit{t}_{\text{cert}}/\mathit{m}^{2}$$
  **5. Synthesis**                                                         Memory write                        $$\mathit{t}_{\text{synth}}/\mathit{n}$$
  **6. Ledger commit**                                                     Hash + I/O                          $\mathit{t}_{\text{ledger}}$ (fixed per touch)
  ------------------------------------------------------------------------ ----------------------------------- --------------------------------------------------------

**Overhead vs. Baseline Ratio**

Define overhead ratio:

$$\text{Overhead}_{\mathit{\pi}} = \frac{\mathit{t}_{\text{Π-step}} - \mathit{t}_{\text{raw\ update}}}{\mathit{t}_{\text{raw\ update}}}$$

where $\mathit{t}_{\text{raw\ update}}$ is a direct
$\mathit{x} \leftarrow \mathit{F}(\mathit{x})$ without
projection/certification.[^[\[3\]]{.underline}^](#fn3)

**Phase 4: Projector Family Comparison**

Benchmark each projector type
independently:[^[\[6\]]{.underline}^](#fn6)[^[\[5\]]{.underline}^](#fn5)

  ---------------------------- ---------------------- -------------------------------------------------------------------- --------- ---------------
  Family                       Operation              Expected Complexity                                                            
  **Index-based** (baseline)   Array slice            (O(                                                                  S\_k      ))
  **Spectral bands**           eigh + mask multiply   $\mathit{O}(\mathit{n}^{2})$ setup, $\mathit{O}(\mathit{n})$ apply             
  **RNS lanes**                CRT encode/decode      $\mathit{O}(\mathit{L}\mathit{n})$ where $\mathit{L}$ = lane count             
  **Wavelet packets**          Lifting scheme         $$\mathit{O}(\mathit{n}\log\mathit{n})$$                                       
  **NTT/DFT**                  FFT-based              $$\mathit{O}(\mathit{n}\log\mathit{n})$$                                       
  **Poseidon hash**            Field arithmetic       (O(                                                                  payload   )) per commit
  ---------------------------- ---------------------- -------------------------------------------------------------------- --------- ---------------

**Phase 5: Concurrency and Cache Effects**

**Parallelization Overhead**

Since Π-atoms are independent, measure:

-   **Sequential**: Single-threaded loop over piids

-   **Parallel**: ThreadPoolExecutor or multiprocessing

-   **SIMD/GPU**: Batched projection via NumPy broadcasting or CuPy

\# Parallel vs sequential comparison\
from concurrent.futures import ThreadPoolExecutor\
\
def parallel\_project(grid, x, piids, workers=4):\
with ThreadPoolExecutor(max\_workers=workers) as ex:\
return dict(ex.map(lambda pi: (pi, grid.project(x, pi)), piids))

**Cache Miss Analysis**

Use perf stat to capture:

-   L1/L2/L3 cache miss rates during projection

-   Memory bandwidth utilization during synthesis

[^[\[7\]]{.underline}^](#fn7)[^[\[3\]]{.underline}^](#fn3)

**Phase 6: End-to-End Trajectory Benchmarks**

**Convergence Speed vs. Overhead Tradeoff**

Run full trajectories and measure:

  -------------------------------- ------------------------------------------------------------------------------------------------------
  Metric                           Definition
  **Steps to convergence**         $$\min\{\mathit{t}:\|\mathit{x}_{\mathit{t} + 1} - \mathit{x}_{\mathit{t}}\| < \mathit{\epsilon}\}$$
  **Wall-clock to convergence**    Total time including all overhead
  **Effective throughput**         Atoms updated per second
  **Certificate overhead ratio**   $$\mathit{t}_{\text{cert}}/\mathit{t}_{\text{total}}$$
  -------------------------------- ------------------------------------------------------------------------------------------------------

**Stability Margin Impact**

Sweep coupling strength $\|\mathit{K}\|_{\infty}$ and measure:

-   How SlopeUB computation time scales with dense vs. sparse
    $\mathit{K}$

-   GapLB certificate failures and rollback
    frequency[^[\[2\]]{.underline}^](#fn2)

**Recommended Tools**

  ----------------------- ---------------------------------------------------------------------------
  Tool                    Purpose
  **LMbench**             System call and memory latency baseline [^[\[3\]]{.underline}^](#fn3)
  **perf**                CPU cycles, cache misses, branch prediction [^[\[3\]]{.underline}^](#fn3)
  **cyclictest**          Kernel scheduling latency (if real-time) [^[\[8\]]{.underline}^](#fn8)
  **NVIDIA Nsight**       GPU kernel launch latency [^[\[4\]]{.underline}^](#fn4)
  **py-spy / cProfile**   Python-level profiling
  ----------------------- ---------------------------------------------------------------------------

**Expected Overhead Targets**

Based on the reference implementation
complexity:[^[\[5\]]{.underline}^](#fn5)[^[\[1\]]{.underline}^](#fn1)

  -------------------------------- ------------------------------------ ----------------------------------------
  Component                        Target Latency                       Notes
  Projection (per Π-atom)          \< 1 μs for $\mathit{n} < 1024$      Memory-bound
  $\mathit{\ell}_{1}$-projection   \< 10 μs (20 bisection iterations)   CPU-bound
  SlopeUB/GapLB                    \< 1 μs for $\mathit{m} < 64$        $\mathit{O}(\mathit{m}^{2})$ matrix op
  SHA-256 ledger commit            \~1 μs per record                    I/O can be batched
  Poseidon commit                  \~10 μs per record                   Field arithmetic overhead
  -------------------------------- ------------------------------------ ----------------------------------------

Total step overhead for $\mathit{m} = 16,\mathit{n} = 256$: target **\<
100 μs** with 10-15% touched atoms per
step.[^[\[1\]]{.underline}^](#fn1)

⁂

1.  P-kernel-A-Mathematical-Note.pdf

2.  P-kernel-Multiplicity-Runtime-Bridge-A-Mathematical-Note.pdf

3.  [[https://embedkari.org/2025/05/10/understanding-benchmarking-measuring-system-and-core-performance-with-tools-like-lmbench/]{.underline}](https://embedkari.org/2025/05/10/understanding-benchmarking-measuring-system-and-core-performance-with-tools-like-lmbench/)

4.  [[https://microsoft.github.io/superbenchmark/docs/user-tutorial/benchmarks/micro-benchmarks/]{.underline}](https://microsoft.github.io/superbenchmark/docs/user-tutorial/benchmarks/micro-benchmarks/)

5.  P-Kernel.pdf

6.  P-Kernel-1.pdf

7.  [[https://www.reddit.com/r/kernel/comments/1ccrqmh/how\_to\_measure\_performance\_of\_the\_kernel/]{.underline}](https://www.reddit.com/r/kernel/comments/1ccrqmh/how_to_measure_performance_of_the_kernel/)

8.  [[http://events17.linuxfoundation.org/sites/events/files/slides/ELC2017-
    Effectively Measure and Reduce Kernel Latencies for Real-time
    Constraints
    (1).pdf]{.underline}](http://events17.linuxfoundation.org/sites/events/files/slides/ELC2017-%20Effectively%20Measure%20and%20Reduce%20Kernel%20Latencies%20for%20Real-time%20Constraints%20(1).pdf)

9.  [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/cde50055-3feb-4652-99d3-39b81cc1c0ae/Becoming-two-Vs-Being-two-Twoness-As-Functorial-Forgetting-with-External-References.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/cde50055-3feb-4652-99d3-39b81cc1c0ae/Becoming-two-Vs-Being-two-Twoness-As-Functorial-Forgetting-with-External-References.pdf)

10. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/3290f19e-4112-44fb-9470-017f509e944f/Qpf-Methods-Protocol-gallows-proof-V1.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/3290f19e-4112-44fb-9470-017f509e944f/Qpf-Methods-Protocol-gallows-proof-V1.pdf)

11. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/ade039ff-edad-4017-b2e4-061bef5d53fb/Modal-Numerosity-As-Algorithmic-Inference-Camera-ready-Package.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/ade039ff-edad-4017-b2e4-061bef5d53fb/Modal-Numerosity-As-Algorithmic-Inference-Camera-ready-Package.pdf)

12. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/61bf5339-7360-4f5d-9e4d-51a40a6e0a77/Where-Do-Negatives-Come-From\_-Operational-Closure-Completion-And-Baselines.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/61bf5339-7360-4f5d-9e4d-51a40a6e0a77/Where-Do-Negatives-Come-From_-Operational-Closure-Completion-And-Baselines.pdf)

13. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/23bd1879-ef01-4906-a675-ebf35515107d/Mr-Boundary-Theory-Zero-As-Boundary-Operator-roles-M-And-Spectral-Tests.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/23bd1879-ef01-4906-a675-ebf35515107d/Mr-Boundary-Theory-Zero-As-Boundary-Operator-roles-M-And-Spectral-Tests.pdf)

14. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/7360180a-eb07-467f-bffc-c4f35c5bafc7/Modes-Of-Infinity-As-Modes-Of-Being-Formalization-Blueprint.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/7360180a-eb07-467f-bffc-c4f35c5bafc7/Modes-Of-Infinity-As-Modes-Of-Being-Formalization-Blueprint.pdf)

15. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/694b3c1d-d7eb-4aee-8bd8-83063abfd89f/Ccn-V2-Minimal-Axioms-Representation-Theorem-finite-Case.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/694b3c1d-d7eb-4aee-8bd8-83063abfd89f/Ccn-V2-Minimal-Axioms-Representation-Theorem-finite-Case.pdf)

16. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/0d7783d8-4cc2-4204-8b05-e7565198bfab/Alp-The-Auditable-Landauer-Principle-canvas-Package.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/0d7783d8-4cc2-4204-8b05-e7565198bfab/Alp-The-Auditable-Landauer-Principle-canvas-Package.pdf)

17. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/e2d110f3-9a3b-4ac7-a00e-b68fd9b45984/Ofa-ii-Iterator-Arithmetic-Reference-Spec-V1.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/e2d110f3-9a3b-4ac7-a00e-b68fd9b45984/Ofa-ii-Iterator-Arithmetic-Reference-Spec-V1.pdf)

18. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/d00c501d-9bcd-417a-a1dd-acc4b1d7653b/Determinacy-Algebra-Being-Becoming-And-Laws-That-Bite-canvas-Edition.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/d00c501d-9bcd-417a-a1dd-acc4b1d7653b/Determinacy-Algebra-Being-Becoming-And-Laws-That-Bite-canvas-Edition.pdf)

19. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/17668332-59bb-4e97-b781-866734f1be86/Lawful-Composition-Calculus-lcc-Associator-Spectroscopy-V0.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/17668332-59bb-4e97-b781-866734f1be86/Lawful-Composition-Calculus-lcc-Associator-Spectroscopy-V0.pdf)

20. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/61beb223-02cc-4d6e-b5e4-ae047b8200cf/Associator-Spectroscopy-Osf-ready-Prereg-Pilot-References.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/61beb223-02cc-4d6e-b5e4-ae047b8200cf/Associator-Spectroscopy-Osf-ready-Prereg-Pilot-References.pdf)

21. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/45419ca8-9742-46bf-93c6-646aad344629/Boundary-spectral-Governance-Regime-Dossier-System-v1.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/45419ca8-9742-46bf-93c6-646aad344629/Boundary-spectral-Governance-Regime-Dossier-System-v1.pdf)

22. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/012ab520-abfa-4b33-85b4-db7596f61739/Operational-Negatives-Preregistration-Package-canvas.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/012ab520-abfa-4b33-85b4-db7596f61739/Operational-Negatives-Preregistration-Package-canvas.pdf)

23. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/0ca7a26a-c4b8-49cc-ab00-b474faeb97f4/Moral-continuity-Ledger-mcl-Rc1.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/0ca7a26a-c4b8-49cc-ab00-b474faeb97f4/Moral-continuity-Ledger-mcl-Rc1.pdf)

24. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/f710e95f-6bda-43a8-95d1-357ee22e3cfb/Ac-os-V0.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/f710e95f-6bda-43a8-95d1-357ee22e3cfb/Ac-os-V0.pdf)

25. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/0950f529-1af9-4db7-8557-e5c4ec8931d2/Qpf-Lab-Associator-Spectroscopy-final-Engineering-Spec.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/0950f529-1af9-4db7-8557-e5c4ec8931d2/Qpf-Lab-Associator-Spectroscopy-final-Engineering-Spec.pdf)

26. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/cb831e8e-630a-4ac3-8996-9c3defd878a6/Two-ness-Clinics-The-Receipt-Test-executable-Program-References.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/cb831e8e-630a-4ac3-8996-9c3defd878a6/Two-ness-Clinics-The-Receipt-Test-executable-Program-References.pdf)

27. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/b83d0758-82f9-4822-b64d-3dcbf7f72970/Spin\_Foam\_Microfoundations.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/b83d0758-82f9-4822-b64d-3dcbf7f72970/Spin_Foam_Microfoundations.pdf)

28. Kernelized-Sieve-Framework-Simulator-B-d-window-Multiplicity-Stability-Diagram.pdf

29. [[https://forums.developer.nvidia.com/t/any-way-to-measure-the-latency-of-a-kernel-launch/221413]{.underline}](https://forums.developer.nvidia.com/t/any-way-to-measure-the-latency-of-a-kernel-launch/221413)

30. [[https://www.osti.gov/servlets/purl/2217711]{.underline}](https://www.osti.gov/servlets/purl/2217711)

31. [[https://arxiv.org/html/2502.20075v1]{.underline}](https://arxiv.org/html/2502.20075v1)

32. [[https://www.usenix.org/legacyurl/micro-benchmarks-0]{.underline}](https://www.usenix.org/legacyurl/micro-benchmarks-0)

33. [[https://arxiv.org/html/2506.05878v1]{.underline}](https://arxiv.org/html/2506.05878v1)

34. [[https://forums.developer.nvidia.com/t/how-to-write-micro-benchmark-to-test-latency-of-specific-instruction/212705]{.underline}](https://forums.developer.nvidia.com/t/how-to-write-micro-benchmark-to-test-latency-of-specific-instruction/212705)

35. [[https://www.baeldung.com/linux/benchmarking]{.underline}](https://www.baeldung.com/linux/benchmarking)

36. [[https://gereon-kremer.de/static/2017-scsc-projection-operators.pdf]{.underline}](https://gereon-kremer.de/static/2017-scsc-projection-operators.pdf)

37. [[https://www.sciencedirect.com/science/article/abs/pii/S0167637721000882]{.underline}](https://www.sciencedirect.com/science/article/abs/pii/S0167637721000882)

38. [[https://dl.acm.org/doi/10.1145/3624062.3624203]{.underline}](https://dl.acm.org/doi/10.1145/3624062.3624203)

39. [[https://xtom.com/blog/best-linux-benchmarking-scripts/]{.underline}](https://xtom.com/blog/best-linux-benchmarking-scripts/)

40. [[https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection\_db8780eb-1711-4089-ab46-59917f9f0fc0/a141816b-9334-4946-9217-8704fe9aac9d/Entangled-Aggregation\_-Non-associativity-As-A-Closure-Defect-Under-Coarse-grained-Composition.pdf]{.underline}](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59917f9f0fc0/a141816b-9334-4946-9217-8704fe9aac9d/Entangled-Aggregation_-Non-associativity-As-A-Closure-Defect-Under-Coarse-grained-Composition.pdf)
