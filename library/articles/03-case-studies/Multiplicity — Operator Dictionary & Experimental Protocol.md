---
slug: multiplicity-operator-dictionary-experimental-protocol
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Multiplicity \u2014 Operator Dictionary & Experimental Protocol.md"
  last_synced: '2026-03-20T17:17:20.099493Z'
---

Multiplicity: Operator Dictionary (State = (x, H))
This document specifies (a) a precise operator dictionary where each symbol denotes a total/partial
function on a state (x, H), and (b) a concrete experimental protocol (datasets, baselines, ablations)
aligned with the blueprint’s predictions.




0) Notation and state space

Cyclic index set

     • Fix n ∈ N with prime factorization n = ∏i pi i .
                                                      a

     • Let G := Z/nZ (indices t are taken mod n).

Signal component

     • Let dx be the signal dimension.
     • A signal is x : G → Rdx . Equivalently, x ∈ Rn×dx with rows indexed by t ∈ G.

Hypergraph component

Use an attributed, role-aware hypergraph:


     • H := (V , E, ι, ρ, aV , aE )
     • V : finite vertex set.
     • E : finite hyperedge set.
     • ι : E → List(V ): incidence list (ordered) of vertices per edge.
     • ρ : E → List(R): role labels aligned with ι(e) (same length).
     • aV : V → RdV : vertex attributes.
     • aE : E → RdE : edge attributes.

       Using ordered incidence (lists) + roles makes n-ary relations explicit.


Full state

     • State := X × H where X = L2 (G; Rdx ) (finite-dimensional here) and H is the space of such
       hypergraphs.
     • Operators are functions State → State, possibly partial (defined only when preconditions hold).

Convention

For an operator O :


     • O(x, H) = (x′ , H ′ ).
     • If O acts only on one component, the other is unchanged.




                                                          1
1) Prime-power “level” operators on signals
We define level operators using subgroup-averaging on G.


1.1 Subgroups and coset averaging

For each divisor d ∣ n define subgroup


$$ H_d := {0, d, 2d, \dots, (\tfrac{n}{d}-1)d}\subseteq G, $$


so ∣Hd ∣ = n/d.


Define the averaging kernel


$$ \mu_{H_d} := \tfrac{1}{|H_d|}\sum_{h\in H_d}\delta_h. $$


Symbol: Πd (in the blueprint: Πpr for prime powers)


Definition on signals:


$$ (\Pi_d x)(t) := (x * \mu_{H_d})(t) = \frac{1}{|H_d|}\sum_{h\in H_d} x(t-h). $$


Action on state:


$$ \Pi_d(x,H) := (\Pi_d x,\; H). $$


Properties (useful for pruning/normal forms):


      • Idempotent: Πd ∘ Πd = Πd .
      • Contractive in ℓ2 .

Prime-power specialization: Use d = pr whenever pr ∣ n.


Symbol: Δd (detail), Spd (spike)


Two common choices (pick one and keep it consistent):


(A) Residual-to-level:


$$ \Delta_d := I-\Pi_d,\quad \mathrm{Sp}_d := I-\Pi_d. $$


(B) Band-pass between nested levels when d1 ∣ d2 :


$$ \Delta_{d_1\to d_2} := \Pi_{d_2}-\Pi_{d_1}. $$




                                                        2
Action on state:


$$ \Delta_d(x,H):=(\Delta_d x,H),\quad \mathrm{Sp}_d(x,H):=((I-\Pi_d)x,H). $$


1.4 Level selection by CRT (optional but aligned with blueprint)
               a
Let n = ∏i pi i . You may define a multi-indexed projector


$$ \Pi_{\mathbf{r}} := \Pi_{p_1^{r_1}}\circ\cdots\circ\Pi_{p_k^{r_k}},\quad 0\le r_i\le a_i. $$


Even if the Π’s commute, this still provides a clean lattice of levels for search.




2) Group actions and “accent” operators on signals
Symbol: Rk


Definition:


$$ (R_k x)(t) := x(t+k). $$


Action on state:


$$ R_k(x,H) := (R_k x,\; H). $$


        If your hypergraph has time-indexed vertices (see §4.3), define a synchronized version Rk
        that also shifts those vertex IDs.


Symbol: A (parameterized)


Let χ : G → R (or S 1 if you keep complex scalars). Typical choices:


      • Fourier character: χm (t) = cos(2πmt/n) and/or sin(2πmt/n).
      • Learned gate: χ(t) = σ(u⊤ x(t) + b) (keep this fixed during operator definition; learning is outside
        the operator).

Definition:


$$ (A_\chi x)(t) := \chi(t)\,x(t)\quad\text{(scalar gate)} $$


or coordinate-wise gating (Aχ x)(t)j = χj (t)x(t)j .


Action on state: Aχ (x, H) = (Aχ x, H).


Symbol: W (parameterized)




                                                           3
Let φ : G → G be a bijection. A canonical family is multiplication by q with gcd(q, n) = 1: φq (t) =
qt mod n.

Definition:


$$ (W_\varphi x)(t) := x(\varphi^{-1}(t)). $$


Action on state: Wφ (x, H) = (Wφ x, H) unless coupled to time vertices (see §4.3).


       W is the main source of noncommutativity with Πd in practice: W changes the partition/
       cosets being averaged.




3) Hypergraph operators (typed rewrites)
All hypergraph operators are defined as functions on H with explicit preconditions. Extend to state by
leaving x unchanged unless stated.


Symbol: W (hypergraph-side)


Let σ : V → V be a bijection.


Definition:


      • V ′ = V , E′ = E
      • ι′ (e) = map(σ, ι(e))
      • a′V (σ(v)) = aV (v)
      • Edge roles/attrs unchanged.

State action: Wσ (x, H) = (x, Wσ (H)).


Symbol: Sv,P


Parameters:


      • vertex v ∈ V
      • predicate P on incident edge-positions: P : (e, i) ↦ {0, 1} for ι(e)[i] = v

Precondition: v ∈ V .


Definition: create two new vertices v0 , v1 with attributes derived from aV (v):


      • V ′ = (V ∖ {v}) ∪ {v0 , v1 }
      • For each incident position (e, i) where ι(e)[i] = v , set
      • ι′ (e)[i] = vP (e,i)




                                                        4
      • Set a′V (vb ) = SplitAttr(aV (v), b) (e.g., copy or learned affine maps).

State action: Sv,P (x, H) = (x, Sv,P (H)).


Symbol: Mu,v


Precondition: u  v ∈
                    =V .

Definition: merge u and v into w :


      • V ′ = (V ∖ {u, v}) ∪ {w}
      • Replace occurrences of u or v in ι by w
      • a′V (w) = MergeAttr(aV (u), aV (v)) (e.g., mean/concat+MLP).

State action: Mu,v (x, H) = (x, Mu,v (H)).


3.4 Edge split / merge (optional)

Often useful for n-ary relations.


Edge split Se,Q
            E
                : split an edge e into e0 , e1 based on predicate Q(i) over positions.


Edge merge MeE1 ,e2 : merge if they share schema/roles.


Symbol: F


Transforms hypergraph into bipartite incidence form (useful as a normal form / baseline):


      • Create a vertex ve for each edge e
      • Replace each hyperedge by ordinary edges (ve , ι(e)[i]) carrying role ρ(e)[i]

Denote F (H) as this factor graph. This is a deterministic compilation.


State action: F (x, H) = (x, F (H)).


Symbol: Relτ


Let τ be a schema transform mapping roles/edge-types.


Definition: re-map ρ and optionally partition edges by type.


Symbol: UfV ,fE


Functions:


      • fV : Rd V → Rd V




                                                        5
      • fE : Rd E → Rd E

Definition: a′V (v) = fV (aV (v)), a′E (e) = fE (aE (e)).


3.8 Add/remove edges (structural edits)
      +
Add: E(v ,…,v ),(r ,…,r ),α
         1    k   1    k



      • Adds new edge with incidence list and roles, edge attribute α.

Remove: Ee−


      • Removes edge e.

       These are powerful; in many experiments, restrict to typed templates to avoid combinatorial
       blowup.




4) Coupling operators between signal and hypergraph
These are the glue that makes (x, H) a single system rather than two disjoint objects.


Symbol: ROg


Produces a task output y (classification/regression/ranking) from state:


$$ \mathsf{RO}_g(x,H) := g\big(\mathsf{Pool}_G(x),\;\mathsf{Pool}_H(H)\big) $$


where pooling can be mean/max/attention, and g is a simple head (linear/MLP).


       Readout is not necessarily included in the operator word (you can treat it as the final
       evaluation stage).


Symbol: Liftψ


Given a map ψ : V → G (assign each vertex a time index), define a lifted signal


$$ (\mathsf{Lift}_\psi(H))(t) := \mathsf{Agg}{a_V(v): \psi(v)=t}\in\mathbb{R}^{d_V}. $$


Then combine with x via concatenation:


$$ \widetilde x(t) := \mathrm{concat}(x(t),\; \mathsf{Lift}_\psi(H)(t)). $$


State action: Liftψ (x, H) = (x, H).




                                                         6
If ψ : V → G is part of your state, define:


     • Rk shifts x by k and reindexes time-assigned vertices so ψ ′ (v) = ψ(v) + k .

This is often necessary to make Rk meaningful when H encodes events over time.




5) Operator words, typing, and normal forms

5.1 Words

An operator word is a composition


$$ W := \mathcal{O}_L\circ\cdots\circ\mathcal{O}_2\circ\mathcal{O}_1, $$


where each Oi is a parameterized operator from the dictionary.


5.2 Admissibility (lightweight refinement typing)

Each operator includes:


     • Precondition PreO (x, H)
     • Postcondition/invariants Inv(x, H)

A word is admissible if all preconditions hold along the execution trace and invariants are preserved.


5.3 Normal forms (for search pruning)

Use algebraic simplifications to reduce branching:


     • Πd Πd → Πd
     • (I − Πd )Πd → 0 (if you represent it explicitly)
     • Optional: collapse consecutive shifts Ra Rb → Ra+b
     • Optional: if you restrict Π to a commuting family, reorder them into canonical order.




(b) Experimental Protocol
6) Core experimental question
Does a prime-level operator word (noncommutative composition) produce measurable gains in:


    1. periodic anomaly detection,
    2. n-ary / hypergraph structure learning,
    3. retrieval interference reduction,




                                                      7
     4. interpretability stability, compared to commutative or unconstrained baselines?




7) Implementation skeleton
Pick n to have multiple primes (e.g., n = 2a 3b 5c ). Practical defaults:


      • n = 720 (24 ⋅ 32 ⋅ 5) for minute/hour/day structure
      • n = 840 (23 ⋅ 3 ⋅ 5 ⋅ 7) for richer prime mix

For a time series z1 , … , zT , create overlapping windows of length n:


      • Window w corresponds to xw (t) = feat(zw+t ) ∈ Rdx

Hypergraph Hw can be:


      • trivial (empty) for pure time-series tasks,
      • event-derived (edges = events within window),
      • knowledge-derived (edges = facts relevant to window).

7.2 Word search (beam)

      • Alphabet Σ: start small
      • signal: Πpr , Δpr , R±1 , Aχm , Wφq
      • hypergraph: S, M , F , U (optional in phase 1)
      • Max length L ∈ {6, 8, 10}
      • Beam width B ∈ {64, 128, 256}
      • Score = validation resonance (metric-specific) minus complexity penalty λ ⋅ L

Pruning:


      • Apply normal forms (§5.3)
      • Reject inadmissible words early (failed preconditions)

7.3 Resonance metrics by task

      • Anomaly detection: AUPRC / AUROC / F1 at fixed false-positive rate
      • Hyper-relational prediction: MRR, Hits\@K
      • Retrieval interference: accuracy vs load + latency; interference slope
      • Interpretability: stability metrics (edit distance, Jaccard over operator multiset, agreement of top-k
        attributions)




                                                         8
8) Experiment A — Periodic anomaly detection

8.1 Datasets

Use a mix of synthetic + real-world benchmarks:


     • NAB (streaming anomaly detection)
     • Yahoo S5 (A1–A4)
     • AIOps-style KPI datasets (multivariate seasonality)
     • Industrial control (SWaT / WADI) if available

8.2 Task

Given a window xw , predict whether it contains an anomaly (binary) or produce pointwise anomaly scores.


8.3 Multiplicity model (minimal)

     • Build features by applying word W to x: ϕW (x) = PoolG (W (x))
     • Classifier: logistic regression / small MLP
     • Search W with beam search; choose best on validation.

8.4 Baselines

Feature baselines:


     • FFT magnitude features + linear model
     • Wavelet features + linear model
     • Seasonal decomposition + residual threshold

Learning baselines:


     • Isolation Forest / One-Class SVM on standard features
     • LSTM/TCN autoencoder anomaly score
     • Transformer-based anomaly detection (where feasible)

8.5 Ablations (directly aligned to predictions)

    1. No prime levels: remove Πpr ; allow only shifts/accents.
    2. Commutative aggregation: compute features ∑i fi (x) from operator set, ignore order.
    3. Order-only: keep same multiset of operators but randomize order; compare.
    4. No permutation ***********************W ***********************: disallow index
       automorphisms.
    5. No accents ***********************A***********************: disallow modulation gates.
    6. Fixed hand-crafted word: e.g., Πp and Δp only.




                                                      9
8.6 Expected measurable outcome

      • Noncommutative word search should improve AUPRC/AUROC over (2) commutative aggregation,
        especially when multiple periodicities exist.




9) Experiment B — Hypergraph structure learning (n-ary / hyper-
relational)

9.1 Datasets

Choose datasets with explicit n-ary relations / qualifiers:


      • Hyper-relational knowledge graphs (statements with qualifiers)
      • N-ary relation corpora (entities + roles)

Concrete options commonly used in the literature:


      • WikiPeople (n-ary facts)
      • JF17K (n-ary)
      • WD50K variants (Wikidata statements)

9.2 Task variants

(i) Missing argument prediction: given edge e with one role missing, predict the missing entity.


(ii) Edge validation: classify whether a proposed n-ary fact is valid.


9.3 Multiplicity model (hypergraph-enabled)

State includes H for the window/document:


      • H nodes = entities; hyperedges = facts; roles = argument positions.
      • Optionally define x as an auxiliary signal (e.g., time ordering of facts or textual position indices).

Apply a word W consisting of:


      • structural rewrites S, M (restricted templates)
      • compilation F (optional)
      • attribute updates U

Readout for prediction:


      • Score candidates by RO over transformed H ′ (and x′ if used).




                                                        10
9.4 Baselines

     • Factor-graph/bipartite compilation (use F ) + standard GNN message passing
     • Hypergraph neural networks (HGNN-style / HyperGCN-style) on the incidence structure
     • Hyper-relational KG baselines (statement/qualifier models)

9.5 Ablations

    1. No rewrites: only U on attributes; structure fixed.
    2. No role awareness: drop ρ (treat incidence as unordered set).
    3. Only compilation ***********************F ***********************: reduce to factor graph;
       no higher-order ops.
    4. No prime-level coupling: disable Lift/time alignment if used.
    5. Rewrite-only vs attribute-only: isolate where gains come from.

9.6 Metrics

     • MRR, Hits\@1/3/10 for argument prediction
     • AUROC/AUPRC for edge validation
     • Constraint violation rate (typed schema errors) if you enforce invariants

9.7 Expected measurable outcome

     • Typed rewrites should reduce structural distortion/constraint violations vs unconstrained edits, while
       maintaining or improving MRR/Hits\@K.




10) Experiment C — Retrieval interference in memory/KG

10.1 Setup (controlled)

Create a memory of items {mi } as hyperedges and/or signal patterns.


     • Queries are partial patterns; retrieval returns top-k matches.

Increase load N and measure:


     • accuracy\@k vs N
     • latency vs N
     • interference slope (performance drop per doubling of N )

10.2 Multiplicity approach

Use prime-level projections as orthogonalizing/partitioning features:


     • Store each item with a signature across Πpr levels.
     • Query uses the same operator word for feature extraction.




                                                     11
10.3 Baselines

      • Dense embedding retrieval (vector search)
      • Hashing / LSH
      • Graph traversal / rule-based retrieval

10.4 Ablations

      • Remove prime-level decomposition
      • Replace Πpr with single-scale smoothing

10.5 Expected outcome

      • Prime-level signatures reduce cross-talk, improving accuracy under heavy load and/or improving
        latency via early pruning.




11) Experiment D — Interpretability and stability

11.1 What is “the explanation”?

Multiplicity’s explanation is the selected word W ∗ plus its intermediate states (xi , Hi ).


11.2 Stability protocol

Train/select W ∗ across S random seeds or folds. Compare:


      • edit distance between words
      • Jaccard similarity of operator multisets
      • agreement of top contributing operators (by ablation impact)

11.3 Baseline explanations

      • Feature attribution on FFT/wavelet features
      • Gradient/attention-based explanations (for neural baselines)

11.4 Expected outcome

      • Operator-level explanations should be more stable across runs than dense attribution maps,
        especially when you constrain words via admissibility.




12) Minimal “Phase 1” plan (fastest validation)
     1. Implement signal operators: Πpr , Δpr , R±1 , Aχm , Wφq .
     2. Run Experiment A (anomaly detection) with beam search over words up to length 8.
     3. Report: best word, ablation table, runtime, and whether ordering beats commutative aggregation.



                                                        12
    4. Only if successful: add hypergraph operators S, M , F , U and run Experiment B.




Appendix: Operator checklist (symbols → function)
Signal-side:


      • Πpr : coset averaging projector
      • Δpr : residual or band-pass
      • Rk : shift
      • Aχ : modulation/gating
      • Wφ : index permutation/automorphism

Hypergraph-side:


      • Sv,P : vertex split
      • Mu,v : vertex merge
      • F : edge-to-vertex fold (factorization)
      • Relτ : role/schema rewrite
      • UfV ,fE : attribute update
      • E + , E − : add/remove edges

Coupling:


      • Liftψ : hypergraph-to-signal lift
      • Rk : synchronized shift (signal + time-indexed vertices)
      • ROg : readout (task head)


References
    1. *Ryan Van Gelder “Multiplicity: Type-theoretic Kr Blueprint“ (unpublished manuscript / blueprint PDF).
    2. Alexander Lavin and Subutai Ahmad. “Evaluating Real-time Anomaly Detection Algorithms — The
       Numenta Anomaly Benchmark.” arXiv:1510.03336 (2015).
    3. Yahoo! Webscope. “S5 — A Labeled Anomaly Detection Dataset, Version 1.0 (16M).” (2015).
    4. Aditya P. Mathur and Nils Ole Tippenhauer. “SWaT: A Water Treatment Testbed for Research and
       Training on ICS Security.” Proceedings of the Workshop on Cyber-Physical Systems for Smart Water
       Networks (CySWater), April 2016.
    5. Chuadhry Mujeeb Ahmed, Venkata Reddy Palleti, and Aditya P. Mathur. “WADI: A Water Distribution
       Testbed for Research in the Design of Secure Cyber Physical Systems.” CySWater (2017).
    6. Jiehui Xu, Haixu Wu, Jianmin Wang, and Mingsheng Long. “Anomaly Transformer: Time Series
       Anomaly Detection with Association Discrepancy.” arXiv:2110.02642 (2021).
    7. Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. “Isolation Forest.” 2008 Eighth IEEE International
       Conference on Data Mining (ICDM), 413–422 (2008).
    8. Bernhard Schölkopf, John C. Platt, John Shawe-Taylor, Alex J. Smola, and Robert C. Williamson.
       “Estimating the Support of a High-Dimensional Distribution.” Neural Computation 13(7):1443–1471
       (2001).




                                                       13
    9. Sepp Hochreiter and Jürgen Schmidhuber. “Long Short-Term Memory.” Neural Computation 9(8):1735–
       1780 (1997).
   10. Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz
       Kaiser, and Illia Polosukhin. “Attention Is All You Need.” NeurIPS (2017).
   11. Jianfeng Wen, Jianxin Li, Yongyi Mao, Shini Chen, and Richong Zhang. “On the Representation and
       Embedding of Knowledge Bases Beyond Binary Relations.” IJCAI 2016, 1300–1307 (2016).
   12. Saiping Guan, Xiaolong Jin, Yuanzhuo Wang, and Xueqi Cheng. “Link Prediction on N-ary Relational
       Data.” Proceedings of the 28th International Conference on World Wide Web (WWW ’19), 583–593
       (2019).
   13. Saiping Guan, Xiaolong Jin, Jiafeng Guo, Yuanzhuo Wang, and Xueqi Cheng. “NeuInfer: Knowledge
       Inference on N-ary Facts.” ACL 2020, 6141–6151 (2020).
   14. Mikhail Galkin, Priyansh Trivedi, Gaurav Maheshwari, Ricardo Usbeck, and Jens Lehmann. “Message
       Passing for Hyper-Relational Knowledge Graphs.” EMNLP 2020, 7346–7359 (2020).
   15. Bahare Fatemi, Perouz Taslakian, David Vazquez, and David Poole. “Knowledge Hypergraphs:
       Prediction Beyond Binary Relations.” IJCAI 2020.
   16. Naganand Yadati, Madhav Nimishakavi, Prateek Yadav, Vikram Nitin, Anand Louis, and Partha
       Talukdar. “HyperGCN: A New Method of Training Graph Convolutional Networks on Hypergraphs.”
       NeurIPS 2018 / arXiv:1809.02589.
   17. Yifan Feng, Haoxuan You, Zizhao Zhang, Rongrong Ji, and Yue Gao. “Hypergraph Neural Networks.”
       AAAI 2019.
   18. Ingrid Daubechies. Ten Lectures on Wavelets. SIAM (1992).
   19. Stéphane G. Mallat. “A Theory for Multiresolution Signal Decomposition: The Wavelet
       Representation.” IEEE TPAMI 11(7):674–693 (1989).
   20. Patrick M. Rondon, Ming Kawaguchi, and Ranjit Jhala. “Liquid Types.” PLDI 2008.
   21. Nikhil Swamy, Juan Chen, Cédric Fournet, Pierre-Yves Strub, Karthikeyan Bhargavan, and Jean Yang.
       “Dependent Types and Multi-monadic Effects in F*.” POPL 2016.
   22. Hartmut Ehrig, Karsten Ehrig, Ulrike Prange, and Gabriele Taentzer. Fundamentals of Algebraic Graph
       Transformation. Springer (2006).
   23. Benjamin C. Pierce. Types and Programming Languages. MIT Press (2002).

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                   14
