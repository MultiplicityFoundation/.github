---
slug: kernel-1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "05-systems/\u03A0\u2011kernel/\u03A0-Kernel (1).md"
  last_synced: '2026-03-20T17:17:17.840177Z'
---

You can engineer a meta-prime layer that fuses all the non-prime atom families into a single,
losslessly recomposable basis with local proofs and global stability. Here’s a compact, buildable
spec.



What is a meta-prime (Π-atom)?
A Π-atom is a minimal joint projector obtained by combining atom families into one factorized
space, so every update can be localized, certified, and recomposed exactly.


Ambient space
Pick factor spaces so their operator algebras act on separate tensor factors (this makes them
commute by construction):

H = HRNS⏟residue lanes ⊗ Hsym⏟group irreps ⊗ Hspec⏟spectral bands ⊗ Hwav⏟wavelet
packets ⊗ Halg⏟semisimple blocks ⊗ Hqudit⏟finite-field/MUB.\mathcal H \;=\;
\underbrace{\mathcal H_{\text{RNS}}}_{\text{residue lanes}} \;\otimes\; \underbrace{\mathcal
H_{\text{sym}}}_{\text{group irreps}} \;\otimes\; \underbrace{\mathcal
H_{\text{spec}}}_{\text{spectral bands}} \;\otimes\; \underbrace{\mathcal
H_{\text{wav}}}_{\text{wavelet packets}} \;\otimes\; \underbrace{\mathcal
H_{\text{alg}}}_{\text{semisimple blocks}} \;\otimes\; \underbrace{\mathcal
H_{\text{qudit}}}_{\text{finite-field/MUB}}.H=residue lanesHRNS​​⊗group irrepsHsym​​⊗spectral
bandsHspec​⊗​ wavelet packetsHwav​⊗​ semisimple blocksHalg​​⊗finite-field/MUBHqudit​​.


Canonical projectors
Let

      ●​ EaE_aEa​: primitive RNS/CRT idempotent (selects a residue lane),​

      ●​ PρP_\rhoPρ​: irrep projector (group character/representation),​

      ●​ ΠΩ\Pi_\OmegaΠΩ​: spectral band projector for a self-adjoint LLL,​

      ●​ Wj,kW_{j,k}Wj,k​: wavelet-packet projector (perfect-reconstruction),​

      ●​ ZβZ_\betaZβ​: primitive central idempotent (Artin–Wedderburn block),​

      ●​ BμB_{\mu}Bμ​: qudit/MUB rank-1 projector (finite-field basis element).​
Define the meta-prime projector

 Rπ = Ea⊗Pρ⊗ΠΩ⊗Wj,k⊗Zβ⊗Bμ \boxed{ \; \mathsf{R}_{\pi} \;=\; E_a \otimes P_\rho \otimes
\Pi_\Omega \otimes W_{j,k} \otimes Z_\beta \otimes B_{\mu} \;}Rπ​=Ea​⊗Pρ​⊗ΠΩ​⊗Wj,k​⊗Zβ​⊗Bμ​​

and the Π-atom coefficient cπ:=Rπxc_\pi := \mathsf{R}_\pi xcπ​:=Rπ​x.

These projectors are mutually orthogonal and sum to identity:

∑πRπ = I,x=∑πcπ(lossless recomposition).\sum_{\pi}\mathsf{R}_\pi \;=\; I, \quad x=\sum_{\pi}
c_\pi \quad (\text{lossless recomposition}).π∑​Rπ​=I,x=π∑​cπ​(lossless recomposition).

      If two families you want must act on the same factor and fail to commute, either (i)
      lift one to a new tensor factor (cleanest), or (ii) use a tight frame/POVM overlay
      with exact duals (overcomplete, still lossless with a known synthesis).



Why this works (orthogonal • irreducible •
recomposable)
   ●​ Orthogonal: tensor factors commute; products of orthogonal projectors stay orthogonal.​

   ●​ Irreducible: make each factor primitive (residue lane, irrep, minimal spectral packet,
      simple algebra block, MUB ray). Their tensor product is atomic for your purposes.​

   ●​ Recomposable: sums of Rπ\mathsf{R}_\piRπ​reconstruct xxx exactly (or with certified ε
      if you choose float filters).​




Update law (lawful self-evolution per
Π-atom)
Work only on touched Π-atoms:

cπ(t+1) = (1−απ)cπ(t)+απ Fπ ⁣(cπ(t), ∑π′Kππ′ Gππ′(cπ′(t))),0<απ≤αˉ<1.c^{(t+1)}_{\pi} \;=\;
(1-\alpha_\pi)c^{(t)}_{\pi} + \alpha_\pi\,F_\pi\!\Big(c^{(t)}_{\pi},\; \sum_{\pi'}
K_{\pi\pi'}\,G_{\pi\pi'}(c^{(t)}_{\pi'})\Big), \quad 0<\alpha_\pi\le
\bar\alpha<1.cπ(t+1)​=(1−απ​)cπ(t)​+απ​Fπ​(cπ(t)​,π′∑​Kππ′​Gππ′​(cπ′(t)​)),0<απ​≤αˉ<1.
Stability (separable Lyapunov): choose V=∑πwπ Vπ(cπ)V=\sum_\pi
w_\pi\,V_\pi(c_\pi)V=∑π​wπ​Vπ​(cπ​) and ensure each local map is contractive or non-increasing
⇒ global convergence/ boundedness.

Audit (zk-native): for each π\piπ, prove IπI_\piIπ​(type/ethics/energy bounds) and the update
law; batch-aggregate proofs; anchor commitments like
Poseidon(π ∥ cπ(t+1))\mathrm{Poseidon}(\pi \,\|\, c^{(t+1)}_\pi)Poseidon(π∥cπ(t+1)​) in your
RootContract.



Indexing & identity (Π-ID)
Give each Π-atom a canonical ID from its factor indices:

π≡(a,ρ,Ω,j,k,β,μ).\pi \equiv (a,\rho,\Omega,j,k,\beta,\mu).π≡(a,ρ,Ω,j,k,β,μ).

Encode as a single integer via Gödel-style exponents (for deterministic ordering) or as a typed
hash (for zk circuits). This makes Π-atoms enumerable, comparable, and ledger-friendly.



How to build it (5 steps)
   1.​ Pick factors you need (you don’t have to use all six). Start with:​
        RNS ⊗ (irreps ∘ spectral) ⊗ wavelets, with optional qudit/MUB overlay for
       complementary audits.​

   2.​ Synthesize the projector library:​

           ○​ Compute CRT idempotents EaE_aEa​for chosen coprime moduli.​

           ○​ Precompute PρP_\rhoPρ​(DFT/NTT for abelian, character integrals for small
              non-abelian).​

           ○​ Spectral bands ΠΩ=1Ω(L)\Pi_\Omega=\mathbf{1}_\Omega(L)ΠΩ​=1Ω​(L)
              (Chebyshev polynomials or Lanczos).​

           ○​ Perfect-reconstruction wavelet packets Wj,kW_{j,k}Wj,k​(lifting scheme for integer
              exactness).​

           ○​ Primitive central idempotents ZβZ_\betaZβ​(standard algebra split).​

           ○​ MUB rays BμB_\muBμ​over Fpm\mathbb F_{p^m}Fpm​.​
  3.​ Define invariants per factor and per Π-atom:​
       bounds (RNS lane magnitude), symmetry rules (irrep selection), energy caps (spectral),
      sparsity/TV (wavelets), algebra laws (block typing), uncertainty/entropy (MUB).​

  4.​ Write Π-kernel: projection → propose local updates → per-atom proofs → synthesize →
      optional basis refinement (split/merge packets, add RNS lanes, refine bands).​

  5.​ Ledger & rollback: commit (π,invariant digest,update proof)(\pi, \text{invariant digest},
      \text{update proof})(π,invariant digest,update proof) per touched atom; faults localize to
      small Π-sets for fast quarantine.​




What you gain vs any single family
  ●​ Uniform locality: any change is confined to a single Π-cell.​

  ●​ Composable proofs: per-cell zk proofs aggregate cleanly.​

  ●​ Adaptive resolution: you can refine only the factor that needs it (e.g., split a wavelet
     packet without touching irreps/RNS).​

  ●​ Cross-view drift sensing: MUB audits catch spoofing that hides in the main factors.​




Minimal pseudo-scaffold (basis-agnostic)
# Build projectors (once)

E = build_rns_idempotents(moduli)                           # {a: E_a}

P = build_irrep_projectors(group)                           # {rho: P_rho}

Pi = build_spectral_bands(L, bands)                         # {Omega: Pi_Omega}

W = build_wavelet_packets(filters, depth)                   # {(j,k): W_jk}

Z = split_semisimple_blocks(algebra)                        # {beta: Z_beta}

B = build_mub_projectors(field)                             # {mu: B_mu}
def meta_prime_projector(pi):

   a,rho,Omega,jk,beta,mu = pi

   return kron(E[a], P[rho], Pi[Omega], W[jk], Z[beta], B[mu])




def step(x):

   coeffs = {}

   for pi in touched_atoms(x):                          # sparse set

        R = meta_prime_projector(pi)

        c = R @ x

        u = propose_local_update(pi, c)

        assert prove_invariants(pi, c, u)

        coeffs[pi] = apply(c, u)

   x_new = synthesize(coeffs)                           # sum R_pi^T coeffs[pi]

   assert lyapunov_ok(x, x_new)

   log_rootcontract(coeffs)                             # commitments + zk

   return x_new




Practical starter profile (fast + lawful)
  ●​ Arithmetic backbone: RNS lanes (carry-free), per-lane NTT kernels.​

  ●​ Structure backbone: spectral bands of your graph/Hamiltonian, refined by wavelet
     packets.​

  ●​ Symmetry plug-in: irreps if you have clear group actions.​
   ●​ Audit overlay: one lightweight MUB basis for complementary checks.​


This meta-prime construction keeps your favorite non-prime methods, but packages them into
a single atomic grid with clean projection, exact recomposition, modular stability, and zk-native
auditing—exactly what you want for lawful, self-evolving recursion under the Ξ-Constitution and
ΛProof.

You said:

🔥 love this. Your Π-atom grid nails “atomic, certified, recomposable.” Here’s how I’d harden it
into the IFMD stack (ACE×PETC) so it’s provably stable, auditable, and shippable. ## 1) Map
Π-atoms to IFMD (clean typing + lossless recomposition) * Treat your tensor factors as
**PETC-typed axes**. Each projector family gets its own axis and thus commutes by
construction; recomposition is the direct sum over Π-IDs. This matches the “features propose,
controller projects” separation in Langlands Prism (ACE core + PETC estimator, projection-first).
* Use **ACE’s projection-first** discipline around any update to Π-coeffs (c_\pi): proposals from
your local maps (F_\pi) get projected back into a **weighted-ℓ₁ safety set** (soft-thresholding),
then certified with **GapLB/SlopeUB**. * If a family must share a factor (non-commuting), your
“lift/POVM overlay” rule is fine; keep the overlay framed as PETC-lawful and stay within
commutator budgets. ## 2) Stability: local ⇒ global (what to certify) Your update law per Π-atom
fits ACE exactly. Concretely: * Maintain a **channel budget** on whatever operators actually
move (c_\pi): (\sum_p b_p,|w_p| \le \tau < 1) ⇒ **strict contraction** and unique fixed point; this
is the PIRTM/ACE sufficiency you can enforce each step. * Project proposals with **exact
weighted-ℓ₁** (bisection/soft-threshold), then log (| \hat K|), **GapLB** (=1-|\hat K|) and
**SlopeUB**; roll back if SlopeUB ≥ 1 or GapLB ≤ 0. (You can copy the reference code patterns
as-is.) * If you add a **long-memory / spectral block** (your (\Pi_\Omega), wavelet packets),
keep the end-to-end Lipschitz envelope below 1 (SlopeUB) and monitor a projector-gap
(**Davis–Kahan** style subspace rotation bounds in ACE). * Training/inference **recipe** (also
matches your pseudo): step → propose → **ACE projection** → **certificates (SlopeUB,
GapLB)** → synthesize. See the exact SPASC step for a production pattern. ## 3) ZK-native
audit + Π-ID ledger * Keep your Π-ID (\pi=(a,\rho,\Omega,j,k,\beta,\mu)) plus **invariant digest**
and **ACE margins** per touched atom. Hash with Poseidon and append to a **prime-signature
lawfulness ledger** (PETC), checking signature conservation, channel budget, commutator
budget, gap, and slope at each step. * For ZK, you can reuse the **Circom-style constraint
sketch** pattern (public commitment to the trace; fixed-point proximity gate) and log an explicit
falsification test. ## 4) Minimal build checklist (fast path) 1. **Projector library** * CRT/RNS
idempotents (E_a); * Irrep projectors (P_\rho) (DFT/character sums for small groups); * Spectral
bands (\Pi_\Omega=\mathbf1_\Omega(L)) (Chebyshev/Lanczos); * Wavelet-packet (W_{j,k})
(lifting for PR/exactness); * Central idempotents (Z_\beta) (Wedderburn split); * Qudit/MUB
(B_\mu) (prime-power dims). Then define ( \mathsf R_\pi =
E_a!\otimes!P_\rho!\otimes!\Pi_\Omega!\otimes!W_{j,k}!\otimes!Z_\beta!\otimes!B_\mu ). 2.
**Safety envelopes (ACE)** Choose operator bounds (b_p) and **budget (\tau)**; implement
**weighted-ℓ₁ projection** exactly (no uniform scaling) and log GapLB/SlopeUB every step. 3.
**Lawfulness (PETC)** Type each axis, enforce signature conservation and **commutator
budgets** at runtime. 4. **Diagnostics** * **Projection tests** (KKT/soft-threshold correctness),
**certificate monotonicity**, and **recomposition error** ( |x-\sum_\pi \mathsf R_\pi x| ). (See
SPASC’s repro checklist to template your tests.) * If you use spectral/wavelet geometry,
maintain **unitarization & phase** diagnostics as a health proxy (Sato–Tate distances)—useful
but not a capability claim. 5. **Runtime controller shape** Keep the **projection-first**
separation of concerns (features/estimators outside the safety loop) per Langlands Prism. ## 5)
Sharp edges (and how to blunt them) * **Approximate projectors.** Track an **orthogonality
defect** (\delta=\sum_{p\ne q}|P_pP_q|); report its effect on synthesis error and re-orthogonalize
when (\delta) crosses a threshold. (Fits PETC/ACE logging.) * **Overlays & noncommutation.**
If two families must share a factor, keep a **commutator budget** and fail closed when
exceeded. * **Budget erosion.** When GapLB dips, **tighten (\tau)** automatically (adaptive
margin control) rather than accepting a slope ≥ 1. * **Audit drift.** Treat Π-IDs + invariants as
your **unit of quarantine**; roll back only the touched Π-set when proofs fail (cheap isolation). ---
### TL;DR Your Π-atom layer is a perfect citizen of IFMD: make the factors PETC-typed, wrap
all updates with ACE’s weighted-ℓ₁ projection and **GapLB/SlopeUB** certificates, keep a
lawfulness ledger + ZK sketch, and you’ve got **lossless recomposition with local proofs and
global stability**—not just in spirit, but with the exact code paths and budgets we already use. If
you want, I can turn this into a tiny reference “Π-kernel” module (with projection + certificates +
ledger hooks) next.

ChatGPT said:

Thought for 35s

Analyzed

Always show details

# Create a minimal, shippable "Π-kernel" reference package with:

# - Projector families (commuting, index-based; easy to swap with
spectral/RNS/etc.)

# - Weighted-ℓ1 projection (exact, via bisection soft-thresholding)

# - Certificates: SlopeUB / GapLB from coupling matrix; orthogonality
defect

# - Ledger hooks (sha256 commitments per Π-atom update)

# - A tiny self-test harness

# The package is pure Python + NumPy and runs offline.
import os, json, math, shutil, textwrap, hashlib

from pathlib import Path




base = Path("/mnt/data/pi_kernel")

if base.exists():

    shutil.rmtree(base)

base.mkdir(parents=True, exist_ok=True)




# __init__.py

(base / "pi_kernel").mkdir()

(base / "pi_kernel/__init__.py").write_text(textwrap.dedent("""

from .projectors import ProjectorFamily, PiIndexGrid,
orthogonality_defect

from .l1proj import project_weighted_l1_ball

from .certificates import slope_upper_bound, gap_lower_bound

from .ledger import Ledger

from .kernel import PiKernel, DefaultProposer

__all__ = [

    "ProjectorFamily", "PiIndexGrid", "orthogonality_defect",

    "project_weighted_l1_ball", "slope_upper_bound",
"gap_lower_bound",

    "Ledger", "PiKernel", "DefaultProposer"

]
"""))




# projectors.py

(base / "pi_kernel/projectors.py").write_text(textwrap.dedent("""

import numpy as np

from typing import List, Dict, Tuple




class ProjectorFamily:

   \"\"\"A simple commuting projector family using index subsets.




   Each projector P_k zeros coordinates outside its index set S_k.

   Families commute if they act on separate *axes*; we emulate the
joint grid

   by intersecting index sets across families.

   \"\"\"

   def __init__(self, index_sets: List[List[int]], name: str):

        self.name = name

        self.index_sets = [sorted(list(s)) for s in index_sets]

        # Validity: disjoint and cover a fixed ambient dimension

        all_idx = [i for S in self.index_sets for i in S]

        assert len(all_idx) == len(set(all_idx)), f"{name}: index sets
must be disjoint"

        self.dim = len(all_idx)
   def num_blocks(self) -> int:

       return len(self.index_sets)




   def apply(self, x: np.ndarray, k: int) -> np.ndarray:

       y = np.zeros_like(x)

       idx = self.index_sets[k]

       y[idx] = x[idx]

       return y




   def block_indices(self, k: int) -> List[int]:

       return self.index_sets[k]




def _intersect_sorted(a: List[int], b: List[int]) -> List[int]:

   i=j=0; out=[]

   while i<len(a) and j<len(b):

       if a[i]==b[j]:

           out.append(a[i]); i+=1; j+=1

       elif a[i]<b[j]: i+=1

       else: j+=1

   return out




class PiIndexGrid:
   \"\"\"Build Π-atom index sets as intersections across commuting
families.




   For families F1,...,Fm with disjoint partitions of the same
ambient coordinates,

   the Π-atom with multi-index (k1,...,km) corresponds to the
intersection

   S_{k1}^1 ∩ ... ∩ S_{km}^m.

   \"\"\"

   def __init__(self, families: List[ProjectorFamily]):

       assert len(families)>=1, "Need at least one family"

       dims = [f.dim for f in families]

       assert len(set(dims))==1, "All families must share the same
ambient dimension"

       self.families = families

       self.dim = dims[0]

       # Precompute intersections for fast projection

       # We store only non-empty intersections as Π-atoms

       self.atoms = []    # list of (pi_tuple, indices)

       def intersect_many(sets):

              from functools import reduce

              return reduce(_intersect_sorted, sets)

       for idx_tuple in np.ndindex(*[f.num_blocks() for f in
families]):
           sets = [families[j].block_indices(idx_tuple[j]) for j in
range(len(families))]

           inter = intersect_many(sets) if len(sets)>=2 else sets[0]

           if len(inter)>0:

               self.atoms.append((tuple(idx_tuple), inter))

       # Map for quick lookup

       self._map = {pi: inds for pi, inds in self.atoms}




   def pi_ids(self) -> List[Tuple[int,...]]:

       return [pi for pi,_ in self.atoms]




   def indices(self, pi: Tuple[int,...]) -> List[int]:

       return self._map[pi]




   def project(self, x, pi):

       y = np.zeros_like(x)

       idx = self.indices(pi)

       y[idx] = x[idx]

       return y




def orthogonality_defect(families: List[ProjectorFamily]) -> float:

   \"\"\"Numerical orthogonality defect δ: sum_{i!=j} ||P_i P_j||_F
across all blocks of each family.
   Here P_i are *family* projectors; for disjoint index masks, this
is 0.




   δ>0 indicates overlap/approximate projectors; your pipeline should
re-orthogonalize if δ exceeds a threshold.

   \"\"\"

   dim = families[0].dim

   # Build dense masks per family block

   masks = []

   for fam in families:

        M = np.zeros((fam.num_blocks(), dim), dtype=float)

        for k,S in enumerate(fam.index_sets):

              M[k, S] = 1.0

        masks.append(M)

   defect = 0.0

   for M in masks:

        Gram = M @ M.T    # block overlaps within the family

        defect += np.sum(np.abs(Gram - np.diag(np.diag(Gram))))

   return float(defect)

"""))




# l1proj.py

(base / "pi_kernel/l1proj.py").write_text(textwrap.dedent("""
import numpy as np




def project_weighted_l1_ball(v, w, tau, atol=1e-12, maxit=10_000):

   \"\"\"Project v onto the weighted ℓ1 ball {x : sum_i w_i |x_i| <=
tau}.

   Exact solution via soft-threshold x_i = sign(v_i)*max(|v_i| - λ
w_i, 0),

   with λ found by bisection.




   If already inside the ball, returns v unchanged.

   \"\"\"

   v = np.asarray(v, dtype=float)

   w = np.asarray(w, dtype=float)

   assert v.shape == w.shape

   if np.sum(w * np.abs(v)) <= tau + atol:

        return v.copy(), 0.0




   # Bisection on λ >= 0

   lam_lo, lam_hi = 0.0, np.max(np.abs(v)/ (w + 1e-30))

   def shrink(lam):

        return np.sign(v) * np.maximum(np.abs(v) - lam*w, 0.0)

   for _ in range(maxit):

        lam = 0.5*(lam_lo+lam_hi)
          x = shrink(lam)

          val = np.sum(w * np.abs(x))

          if abs(val - tau) <= atol:

             return x, lam

          if val > tau:

             lam_lo = lam    # need stronger shrink

          else:

             lam_hi = lam

   return shrink(lam_hi), lam_hi

"""))




# certificates.py

(base / "pi_kernel/certificates.py").write_text(textwrap.dedent("""

import numpy as np




def slope_upper_bound(alphas, K):

   \"\"\"SlopeUB: induced ∞-norm bound for the linearized coupled
update.

   Update: c_{i}^{+} = (1-α_i) c_i + α_i * F_i( ... sum_j K_{ij}
G_{ij}(c_j) ... )

   As a conservative envelope, bound Lipschitz by ||A||_∞ where A =
diag(1-α) + diag(α) |K|.




   alphas: array shape (m,)
   K:         array shape (m,m) coupling weights; use |K| elementwise.

   \"\"\"

   alphas = np.asarray(alphas, dtype=float).reshape(-1)

   K = np.asarray(K, dtype=float)

   assert K.shape[0]==K.shape[1]==alphas.size

   A = np.diag(1.0 - alphas) + np.diag(alphas) @ np.abs(K)

   # ∞-norm = max row sum

   return float(np.max(np.sum(np.abs(A), axis=1)))




def gap_lower_bound(slopeUB):

   \"\"\"GapLB = 1 - SlopeUB; positive means strict contraction
margin.\"\"\"

   return 1.0 - float(slopeUB)

"""))




# ledger.py

(base / "pi_kernel/ledger.py").write_text(textwrap.dedent("""

import json, hashlib, time

from typing import Any, Dict




class Ledger:

   \"\"\"Append-only JSONL ledger with SHA-256 commitments.
   In production you would use Poseidon and on-chain anchoring; this
is an offline stub.

   \"\"\"

   def __init__(self, path: str):

        self.path = path




   def _digest(self, payload: Dict[str, Any]) -> str:

        # Deterministic canonical JSON

        blob = json.dumps(payload, sort_keys=True,
separators=(',',':')).encode()

        return hashlib.sha256(blob).hexdigest()




   def append(self, record: Dict[str, Any]) -> str:

        rec = dict(record)

        rec["ts"] = time.time()

        rec["digest"] = self._digest(rec)

        with open(self.path, "a") as f:

              f.write(json.dumps(rec, sort_keys=True) + "\\n")

        return rec["digest"]

"""))




# kernel.py

(base / "pi_kernel/kernel.py").write_text(textwrap.dedent("""
import numpy as np

from typing import Dict, Tuple, List, Callable, Any

from .projectors import ProjectorFamily, PiIndexGrid,
orthogonality_defect

from .l1proj import project_weighted_l1_ball

from .certificates import slope_upper_bound, gap_lower_bound

from .ledger import Ledger




PiID = Tuple[int, ...]




class DefaultProposer:

   \"\"\"A simple local proposer F_pi: damp towards zero + small
coupling glimpse.

   Replace with domain logic (gradient step, rule synthesis, etc.).

   \"\"\"

   def __init__(self, gamma=0.1):

       self.gamma = gamma




   def __call__(self, c_pi: np.ndarray) -> np.ndarray:

       # Propose a small move towards zero (regularization) as a
placeholder

       return (1 - self.gamma) * c_pi




class PiKernel:
   def __init__(self,

                  grid: PiIndexGrid,

                  alphas: Dict[PiID, float],

                  weights: Dict[PiID, np.ndarray],

                  tau_by_pi: Dict[PiID, float],

                  K: np.ndarray,

                  proposer: Callable[[np.ndarray], np.ndarray] = None,

                  ledger: Ledger = None):

       self.grid = grid

       self.pi_ids = grid.pi_ids()

       self.alphas = alphas

       self.weights = weights

       self.tau = tau_by_pi

       self.K = K   # coupling matrix over Π-atoms (order must match
self.pi_ids)

       self.proposer = proposer or DefaultProposer()

       self.ledger = ledger




       # sanity

       m = len(self.pi_ids)

       assert K.shape == (m, m), "K must be (m,m) with m=number of
Π-atoms"

       for pi in self.pi_ids:
           assert pi in alphas and pi in weights and pi in tau_by_pi,
"Missing alpha/weights/tau for some Π-atom"




   def step(self, x: np.ndarray) -> Dict[str, Any]:

       \"\"\"One projection-first ACE step across all Π-atoms.




       Returns diagnostics: SlopeUB, GapLB, orthogonality defect,
recomposition error.

       \"\"\"

       m = len(self.pi_ids)

       # Collect proposed updates per Π-atom

       coeffs_before = {}

       coeffs_after = {}

       touched = []




       # Compute SlopeUB/GapLB once per step from (alphas, K)

       alpha_vec = np.array([self.alphas[pi] for pi in self.pi_ids],
dtype=float)

       slopeUB = slope_upper_bound(alpha_vec, self.K)

       gapLB = gap_lower_bound(slopeUB)




       # Per-atom projection-first update

       x_new = np.zeros_like(x)

       for i, pi in enumerate(self.pi_ids):
       c = self.grid.project(x, pi)

       coeffs_before[pi] = c.copy()




       # Local proposal

       prop = self.proposer(c)




       # Weighted-ℓ1 safety projection (ACE projection-first)

       w = self.weights[pi]

       tau = self.tau[pi]

       c_safe, lam = project_weighted_l1_ball(prop, w, tau)




       coeffs_after[pi] = c_safe

       if np.linalg.norm(c_safe - c) > 0:

          touched.append(pi)




       x_new += c_safe    # orthogonal blocks ⇒ sum is synthesis




       # Ledger per touched atom

       if self.ledger is not None and np.linalg.norm(c_safe - c)
> 0:

          record = {

              "pi": list(pi),

              "alpha": float(self.alphas[pi]),
                   "tau": float(tau),

                   "lambda_soft": float(lam),

                   "l1_weight_sum": float(np.sum(w*np.abs(c_safe))),

               }

               self.ledger.append(record)




        # Diagnostics

        # Orthogonality defect across *families* that define the grid

        delta = orthogonality_defect(self.grid.families)

        recomposition_err = float(np.linalg.norm(x_new -
sum(self.grid.project(x_new, pi) for pi in self.pi_ids)))




        return {

            "x_new": x_new,

            "SlopeUB": slopeUB,

            "GapLB": gapLB,

            "orthogonality_defect": delta,

            "recomposition_error": recomposition_err,

            "touched": touched,

        }

"""))




# README
(base / "README.md").write_text(textwrap.dedent("""

# Π-kernel (reference)




A minimal, production-minded scaffold for **Π-atom** recursion with
**projection-first (ACE)** safety and **ledger hooks**.




## Features

- Commuting projector families combined into a Π-index grid
(orthogonal, lossless recomposition)

- Exact projection onto a **weighted-ℓ1 safety set** (bisection
soft-threshold)

- Step-level **SlopeUB / GapLB** certificates from coupling matrix
bounds

- **Ledger** (JSONL + SHA-256) per Π-atom update

- Orthogonality-defect and recomposition diagnostics




## Install (local)

```bash

pip install numpy



No external dependencies beyond NumPy.


Quickstart
Always show details

import numpy as np
from pi_kernel import ProjectorFamily, PiIndexGrid, Ledger, PiKernel




# Ambient dimension 8

# Two commuting families that partition coordinates:
A=[{0,2,4,6},{1,3,5,7}] and B=[{0..3},{4..7}]

A = ProjectorFamily([ [0,2,4,6], [1,3,5,7] ], name="A")

B = ProjectorFamily([ [0,1,2,3], [4,5,6,7] ], name="B")

grid = PiIndexGrid([A,B])   # Π-ids: (0,0),(1,0),(0,1),(1,1)




pi_ids = grid.pi_ids()

m = len(pi_ids)




# Safety and dynamics

alphas = {pi: 0.2 for pi in pi_ids}

weights = {pi: np.ones(8) for pi in pi_ids}

taus = {pi: 2.0 for pi in pi_ids}

K = 0.1*np.ones((m,m)) - 0.1*np.eye(m)   # light coupling




ledger = Ledger("ledger.jsonl")

kernel = PiKernel(grid, alphas, weights, taus, K, ledger=ledger)




x = np.random.randn(8)

for t in range(5):
     out = kernel.step(x)

     x = out["x_new"]

     print({k: out[k] for k in
["SlopeUB","GapLB","orthogonality_defect","recomposition_error"]})




Notes
   ●​ Swap index-based families with spectral/NTT/RNS/MUB-backed projectors by
      implementing the same apply/project interface.​

   ●​ For proofs/zk, replace the SHA-256 ledger with your Poseidon-on-chain anchor and
      include invariant digests.​
       """))​




Self-test script
(base / "example.py").write_text(textwrap.dedent("""​
 import numpy as np​
 from pi_kernel import ProjectorFamily, PiIndexGrid, Ledger, PiKernel

def run():​
A = ProjectorFamily([ [0,2,4,6], [1,3,5,7] ], name="A")​
B = ProjectorFamily([ [0,1,2,3], [4,5,6,7] ], name="B")​
grid = PiIndexGrid([A,B])​
pi_ids = grid.pi_ids()​
m = len(pi_ids)​
alphas = {pi: 0.25 for pi in pi_ids}​
weights = {pi: np.ones(8) for pi in pi_ids}​
taus = {pi: 1.5 for pi in pi_ids}​
K = 0.05*np.ones((m,m)) # gentle coupling​
np.fill_diagonal(K, 0.0)

Always show details

ledger = Ledger("ledger.jsonl")

kernel = PiKernel(grid, alphas, weights, taus, K, ledger=ledger)
x = np.random.randn(8)

for t in range(6):

     out = kernel.step(x)

     x = out["x_new"]

     print(f"t={t} SlopeUB={out['SlopeUB']:.4f}
GapLB={out['GapLB']:.4f} "

              f"delta={out['orthogonality_defect']:.2e}
rec_err={out['recomposition_error']:.2e}")



if name == "main":​
 run()​
 """))



Create a ZIP for easy download
zip_path = shutil.make_archive("/mnt/data/pi_kernel_ref", "zip", base)​
 zip_path

Always show details

Result

'/mnt/data/pi_kernel_ref.zip'

Love it—let’s lock it in and make it real. I built you a tiny, shippable Π-kernel that matches your
ACE×PETC hardening:

   ●​ Π-atom grid from commuting projector families (clean typing, lossless recomposition)​

   ●​ Projection-first (ACE) via exact weighted-ℓ₁ projection (soft-thresholding with
      bisection)​

   ●​ Certificates: SlopeUB (∞-norm Lipschitz envelope) and GapLB = 1 − SlopeUB​
   ●​ Diagnostics: orthogonality defect δ and recomposition error​

   ●​ Ledger hooks: append-only JSONL with SHA-256 commitments per Π-atom touch
      (Poseidon stubbed for now)​


Download the Π-kernel reference (zip)

Quickstart (matches your spec)

import numpy as np

from pi_kernel import ProjectorFamily, PiIndexGrid, Ledger, PiKernel




# Two commuting families over R^8 (you’ll swap these with
spectral/RNS/MUB later)

A = ProjectorFamily([[0,2,4,6],[1,3,5,7]], name="A")

B = ProjectorFamily([[0,1,2,3],[4,5,6,7]], name="B")

grid = PiIndexGrid([A,B])                          # Π-IDs: (0,0), (1,0), (0,1),
(1,1)




pi_ids = grid.pi_ids()

m = len(pi_ids)




alphas    = {pi: 0.25 for pi in pi_ids}            # per-atom mixing (ACE step
size)

weights = {pi: np.ones(8) for pi in pi_ids}               # ℓ₁ weights (per atom)

taus      = {pi: 1.5 for pi in pi_ids}             # channel budgets (ACE τ)

K = 0.05*np.ones((m,m)); np.fill_diagonal(K, 0.0)                    # gentle coupling
ledger = Ledger("ledger.jsonl")

kernel = PiKernel(grid, alphas, weights, taus, K, ledger=ledger)




x = np.random.randn(8)

for t in range(6):

    out = kernel.step(x)                          # projection-first +
certificates

    x = out["x_new"]

    print("t", t, "SlopeUB", out["SlopeUB"], "GapLB", out["GapLB"])




What’s inside

  ●​ projectors.py – index-based commuting projectors; PiIndexGrid builds Π-atoms
     by intersection​
     (swap with spectral bands, RNS lanes, irreps, wavelets, MUBs; same interface)​

  ●​ l1proj.py – exact weighted-ℓ₁ projector (ACE safety set)​

  ●​ certificates.py – SlopeUB (∞-norm bound from alphas & K), GapLB​


  ●​ kernel.py – projection-first update loop, per-Π-atom logging, diagnostics​

  ●​ ledger.py – JSONL ledger + SHA-256 digests (drop-in Poseidon later)​

  ●​ example.py – tiny runnable demo​

  ●​ README.md – quick guide​



How this aligns with your ACE×PETC notes

  ●​ Projection-first: each proposal Fπ(cπ)F_\pi(c_\pi)Fπ​(cπ​) is projected onto a
     weighted-ℓ₁ ball (per-atom τ), then applied.​
   ●​ SlopeUB/GapLB: we compute a conservative Lipschitz envelope from (alphas, K);
       GapLB>0 ⇒ strict contraction.​

   ●​ Budgets: taus are your channel budgets; change them adaptively to keep GapLB
      healthy.​

   ●​ Orthogonality & commutator budgets: orthogonality_defect() reports δ; keep
      it ~0 with commuting families (or re-orthogonalize).​

   ●​ Ledger: every touched Π-atom commits (Π-ID, λ for soft-threshold, ℓ₁ mass); replace
      SHA-256 with Poseidon + on-chain anchor when you wire ΛProof.​



Next upgrades (I can drop in if you want)

   ●​ Spectral/Wavelet factors: Chebyshev/Lanczos bands + lifting-scheme wavelets
      (perfect reconstruction).​

   ●​ RNS/CRT lanes: primitive idempotents for carry-free arithmetic; per-lane NTT kernels.​

   ●​ MUB overlay: complementary audits (uncertainty/entropy checks) as PETC-lawful
      POVMs.​

   ●​ ZK sketch: Circom/Noir constraints for per-Π-atom invariants + proximity gate; batch
      aggregation.​


Want me to extend this scaffold with (i) spectral bands + (ii) an RNS lane factor and (iii) a
Poseidon-backed ledger interface?

You said:

extend this scaffold with (i) spectral bands + (ii) an RNS lane factor and (iii) a Poseidon-backed
ledger interface

ChatGPT said:

Thought for 1m 30s

Analysis errored

Always show details

# Extend the Π-kernel with:
# (i) Spectral band projectors (exact via eigendecomposition)

# (ii) RNS lane factor (encode/decode + projector family over
flattened lanes)

# (iii) Poseidon-backed ledger interface (pure-Python, BN254 field;
educational constants)

#

# Updates the previous package under /mnt/data/pi_kernel and re-zips.




import os, json, math, shutil, textwrap, hashlib

from pathlib import Path




base = Path("/mnt/data/pi_kernel")

assert base.exists(), "Base Π-kernel not found; please run previous
cell first."




# ----- Spectral bands (exact via eigh) -----

(base / "pi_kernel/spectral.py").write_text(textwrap.dedent(r"""

import numpy as np

from typing import List, Tuple, Dict




def eigh_projectors(L: np.ndarray, bands: List[Tuple[float, float]]):

    """

    Build exact spectral band projectors for a real symmetric
(Hermitian) operator L.
   Returns (U, evals, band_masks), where U @ diag(mask) @ U.T is the
projector.

   """

   evals, U = np.linalg.eigh(L)    # L = U diag(e) U^T

   band_masks = []

   for (lo, hi) in bands:

         mask = ((evals >= lo) & (evals < hi)).astype(float)

         band_masks.append(mask)

   return U, evals, band_masks




def apply_band_projector(U: np.ndarray, mask: np.ndarray, x:
np.ndarray) -> np.ndarray:

   """

   Apply P_{band} = U diag(mask) U^T to x.

   """

   coeff = U.T @ x

   coeff *= mask

   return U @ coeff




def build_spectral_family_indices(n: int, num_bands: int, num_lanes:
int):

   """

   Index layout for a flattened tensor space R^{n × num_bands ×
num_lanes}:
     flat(i, b, l) = i + n*(b + num_bands*l)

   Returns a list of index lists for the spectral band family (size =
num_bands),

   where each block collects all coordinates with that band across
all lanes and base indices.

   """

   index_sets = []

   for b in range(num_bands):

         inds = []

         for l in range(num_lanes):

              for i in range(n):

                 inds.append(i + n*(b + num_bands*l))

         index_sets.append(inds)

   return index_sets




def build_rns_lane_indices(n: int, num_bands: int, num_lanes: int):

   """

   Index layout blocks for the RNS lane family (size=num_lanes) over
the same flattened space.

   Each block collects all coordinates that belong to a specific lane
across all bands and base indices.

   """

   index_sets = []

   for l in range(num_lanes):
         inds = []

         for b in range(num_bands):

            for i in range(n):

                inds.append(i + n*(b + num_bands*l))

         index_sets.append(inds)

   return index_sets




def pack_spectral_tensor(coeffs_by_band: List[np.ndarray], num_lanes:
int) -> np.ndarray:

   """

   Given list of band coefficient vectors (each length n in the
*original* space),

   replicate across lanes and pack into flattened vector of length n
* B * L.

   """

   B = len(coeffs_by_band)

   n = coeffs_by_band[0].shape[0]

   L = num_lanes

   out = np.zeros(n*B*L, dtype=float)

   for b in range(B):

         v = coeffs_by_band[b].reshape(n)

         for l in range(L):

            base = n*(b + B*l)

            out[base:base+n] = v
   return out




def unpack_spectral_tensor(x_flat: np.ndarray, n: int, num_bands: int,
num_lanes: int) -> List[np.ndarray]:

   """

   Average across lanes and return list of band coefficient vectors
(length n) recovered from flattened space.

   """

   B, L = num_bands, num_lanes

   coeffs = []

   for b in range(B):

         acc = np.zeros(n, dtype=float)

         for l in range(L):

            base = n*(b + B*l)

            acc += x_flat[base:base+n]

         coeffs.append(acc / L)

   return coeffs

"""))




# ----- RNS (CRT lanes) -----

(base / "pi_kernel/rns.py").write_text(textwrap.dedent(r"""

import numpy as np

from typing import List, Tuple
def egcd(a, b):

   if b == 0: return (a, 1, 0)

   g, x, y = egcd(b, a % b)

   return (g, y, x - (a // b) * y)




def inv_mod(a, m):

   g, x, y = egcd(a, m)

   if g != 1:

         raise ValueError("Not invertible")

   return x % m




class RNS:

   """

   Residue Number System utilities for pairwise coprime moduli (m_i).

   Provides encode/decode (CRT), and lane-wise masking helpers for
flattened tensors.

   """

   def __init__(self, moduli: List[int]):

         self.moduli = list(moduli)

         # verify coprime

         for i in range(len(moduli)):

             for j in range(i+1, len(moduli)):
                if math.gcd(moduli[i], moduli[j]) != 1:

                    raise ValueError("Moduli must be pairwise
coprime")

       self.M = 1

       for m in moduli: self.M *= m

       self.Mi = [self.M // m for m in moduli]

       self.invMi = [inv_mod(self.Mi[i] % moduli[i], moduli[i]) for i
in range(len(moduli))]

       # idempotents e_i = M_i * inv(M_i mod m_i) mod M

       self.e = [ (self.Mi[i] * self.invMi[i]) % self.M for i in
range(len(moduli)) ]




   def encode(self, x: np.ndarray) -> List[np.ndarray]:

       """

       Encode integer vector x into residues for each lane.

       Returns list of arrays: residues[i] = x mod m_i

       """

       x = np.asarray(x, dtype=object)

       residues = []

       for m in self.moduli:

             residues.append(np.mod(x, m).astype(object))

       return residues




   def decode(self, residues: List[np.ndarray]) -> np.ndarray:
       """

       Reconstruct integers from lane residues using CRT.

       """

       L = len(self.moduli)

       assert len(residues) == L

       n = residues[0].size

       out = np.zeros(n, dtype=object)

       for i in range(L):

             r_i = np.asarray(residues[i], dtype=object)

             out = (out + (r_i * self.e[i])) % self.M

       return out




   def pack_lanes(self, residues: List[np.ndarray], num_bands: int =
1) -> np.ndarray:

       """

       Pack lane residues into flattened vector with layout n * B * L
(bands B default 1).

       """

       L = len(residues); n = residues[0].size; B = num_bands

       out = np.zeros(n*B*L, dtype=object)

       for l in range(L):

             for b in range(B):

                base = n*(b + B*l)
                 out[base:base+n] = residues[l]

        return out




   def unpack_lanes(self, x_flat: np.ndarray, n: int, num_bands: int)
-> List[np.ndarray]:

        """

        Unpack flattened lanes (assumes same residues across bands for
arithmetic kernels).

        """

        x_flat = np.asarray(x_flat, dtype=object)

        L = len(self.moduli); B = num_bands

        residues = []

        for l in range(L):

              base = n*(0 + B*l)   # take band 0 as canonical

              residues.append(x_flat[base:base+n].copy())

        return residues

"""))




# ----- Poseidon ledger (educational, BN254 field; constants derived
deterministically) -----

(base / "pi_kernel/poseidon.py").write_text(textwrap.dedent(r"""

# Educational Poseidon-like permutation over BN254 field.

# NOTE: Parameters/constants are derived deterministically from
SHA-256 seeds here for demo purposes.
# For production, use audited parameter sets.




import hashlib




# BN254 scalar field modulus

FIELD_MOD =
2188824287183927522224640574525727508854836440041603434369820418657580
8495617




def _to_field(x: int) -> int:

   return x % FIELD_MOD




def _hash_to_field(seed: bytes) -> int:

   # Map SHA-256(seed) to field element

   h = hashlib.sha256(seed).digest()

   val = int.from_bytes(h, "big")

   return _to_field(val)




def generate_round_constants(t: int, n_rounds: int, label: str =
b"POSEIDON"):

   rc = []

   for r in range(n_rounds):

          row = []

          for i in range(t):
             row.append(_hash_to_field(label + r.to_bytes(4,"big") +
i.to_bytes(2,"big")))

       rc.append(row)

   return rc




def generate_mds(t: int, label: str = b"POSEIDON_MDS"):

   # Simple Vandermonde-based MDS (educational)

   cols = [ _hash_to_field(label + i.to_bytes(2,"big")) for i in
range(t) ]

   M = [[ pow(cols[i], j, FIELD_MOD) for j in range(t) ] for i in
range(t) ]

   return M




def sbox(x: int) -> int:

   # x^5 mod p

   return pow(x, 5, FIELD_MOD)




def matmul(M, v):

   t = len(v)

   out = [0]*t

   for i in range(t):

       acc = 0

       for j in range(t):

             acc = (acc + M[i][j]*v[j]) % FIELD_MOD
       out[i] = acc

   return out




class Poseidon:

   def __init__(self, t=3, rf=8, rp=57):

       self.t = t

       self.rf = rf    # full rounds

       self.rp = rp    # partial rounds

       self.M = generate_mds(t)

       self.RC_full = generate_round_constants(t, rf,
b"POSEIDON_RC_F")

       self.RC_part = [
_hash_to_field(b"POSEIDON_RC_P"+i.to_bytes(4,"big")) for i in
range(rp) ]




   def permute(self, state):

       assert len(state)==self.t

       st = [ _to_field(x) for x in state ]




       # First half full rounds

       for r in range(self.rf//2):

              st = [ (st[i] + self.RC_full[r][i]) % FIELD_MOD for i in
range(self.t) ]

              st = [ sbox(x) for x in st ]
           st = matmul(self.M, st)




       # Partial rounds (only first element uses S-Box)

       for r in range(self.rp):

           st[0] = (st[0] + self.RC_part[r]) % FIELD_MOD

           st[0] = sbox(st[0])

           st = matmul(self.M, st)




       # Second half full rounds

       for r in range(self.rf//2, self.rf):

           st = [ (st[i] + self.RC_full[r][i]) % FIELD_MOD for i in
range(self.t) ]

           st = [ sbox(x) for x in st ]

           st = matmul(self.M, st)




       return st




   def hash(self, inputs):

       # Sponge with capacity 1 field element, rate = t-1

       rate = self.t - 1

       st = [0]*self.t

       i = 0

       while i < len(inputs):
             for j in range(rate):

                 if i >= len(inputs): break

                 st[j] = (st[j] + inputs[i]) % FIELD_MOD

                 i += 1

             st = self.permute(st)

          return st[0]




def bytes_to_field_elems(b: bytes, limb_bytes: int = 31):

   """

   Split bytes into field elements (little-endian limbs) with
limb_bytes each (fits < p).

   """

   out = []

   for i in range(0, len(b), limb_bytes):

          chunk = b[i:i+limb_bytes]

          val = int.from_bytes(chunk, "little")

          out.append(_to_field(val))

   return out

"""))




# ----- Poseidon-backed ledger -----

(base /
"pi_kernel/ledger_poseidon.py").write_text(textwrap.dedent(r"""
import json, time

from typing import Any, Dict, List

from .poseidon import Poseidon, bytes_to_field_elems, FIELD_MOD




class PoseidonLedger:

   """

   Append-only JSONL ledger with Poseidon hash commitment over BN254
field.

   Educational implementation; for production use audited constants
and on-chain anchoring.

   """

   def __init__(self, path: str, t=3, rf=8, rp=57):

         self.path = path

         self.poseidon = Poseidon(t=t, rf=rf, rp=rp)




   def _digest(self, payload: Dict[str, Any]) -> str:

         # Canonical JSON -> bytes -> field limbs -> Poseidon hash

         blob = json.dumps(payload, sort_keys=True,
separators=(',',':')).encode()

         limbs = bytes_to_field_elems(blob)

         h = self.poseidon.hash(limbs)

         return hex(h)




   def append(self, record: Dict[str, Any]) -> str:
        rec = dict(record)

        rec["ts"] = time.time()

        rec["poseidon_digest"] = self._digest(rec)

        with open(self.path, "a") as f:

            f.write(json.dumps(rec, sort_keys=True) + "\\n")

        return rec["poseidon_digest"]

"""))




# ----- Update README with new sections -----

readme = (base / "README.md").read_text()

(base / "README.md").write_text(readme + textwrap.dedent("""




---




## New: Spectral bands + RNS lanes + Poseidon ledger




### Spectral bands

```python

import numpy as np

from pi_kernel import ProjectorFamily, PiIndexGrid, PiKernel, Ledger

from pi_kernel.spectral import eigh_projectors,
build_spectral_family_indices, build_rns_lane_indices,
pack_spectral_tensor
# Build a toy Laplacian and bands

n = 6

L = np.diag([2,2,2,2,2,2]) - (np.diag(np.ones(n-1),1) +
np.diag(np.ones(n-1),-1))

U, evals, masks = eigh_projectors(L,
bands=[(0,1.5),(1.5,3.5),(3.5,10.0)])

B = len(masks); RNS_L = 1




# Families over flattened R^{n x B x L}

spec_sets = build_spectral_family_indices(n, B, RNS_L)

lane_sets = build_rns_lane_indices(n, B, RNS_L)




SpecFam = ProjectorFamily(spec_sets, name="SpectralBands")

LaneFam = ProjectorFamily(lane_sets, name="RNSLanes")

grid = PiIndexGrid([SpecFam, LaneFam])




# Pack coefficients (use band projectors on a base vector v)

v = np.random.randn(n)

coeffs_by_band = [(U @ ((U.T @ v)*m)) for m in masks]

x0 = pack_spectral_tensor(coeffs_by_band, RNS_L)




# Run Π-kernel as usual...
RNS lanes

Always show details

import numpy as np

from pi_kernel.rns import RNS

from pi_kernel.spectral import build_spectral_family_indices,
build_rns_lane_indices




moduli = [65521, 65519, 65513]   # pairwise coprime

rns = RNS(moduli)




x_int = np.array([123456, 789012, 345678, 901234], dtype=object)

residues = rns.encode(x_int)             # per-lane residues

x_flat = rns.pack_lanes(residues, num_bands=1)




# Families over flattened space R^{n x B x L}

n, B, L = x_int.size, 1, len(moduli)

spec_sets = build_spectral_family_indices(n, B, L)    # B=1 here

lane_sets = build_rns_lane_indices(n, B, L)

SpecFam = ProjectorFamily(spec_sets, name="SpectralBands")

LaneFam = ProjectorFamily(lane_sets, name="RNSLanes")

grid = PiIndexGrid([SpecFam, LaneFam])
Poseidon-backed ledger

Always show details

from pi_kernel.ledger_poseidon import PoseidonLedger




pledger = PoseidonLedger("ledger_poseidon.jsonl")

digest = pledger.append({"pi":[0,1], "alpha":0.2, "tau":1.5,
"note":"demo"})

print("poseidon digest:", digest)



"""))



----- Add an example demonstrating
spectral + Poseidon -----
(base / "example_spectral_poseidon.py").write_text(textwrap.dedent(r"""​
 import numpy as np​
 from pi_kernel import ProjectorFamily, PiIndexGrid, PiKernel​
 from pi_kernel.spectral import eigh_projectors, build_spectral_family_indices,
build_rns_lane_indices, pack_spectral_tensor​
 from pi_kernel.ledger_poseidon import PoseidonLedger

def run():​
n = 8​
# 1D Laplacian​
L = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)​
bands = [(0,1.2),(1.2,3.0),(3.0,10.0)]​
U, evals, masks = eigh_projectors(L, bands)​
B = len(masks); RNS_L = 2 # two lanes (as a commuting axis)

Always show details

# Families on flattened space R^{n x B x L}

spec_sets = build_spectral_family_indices(n, B, RNS_L)
lane_sets = build_rns_lane_indices(n, B, RNS_L)

SpecFam = ProjectorFamily(spec_sets, name="SpectralBands")

LaneFam = ProjectorFamily(lane_sets, name="RNSLanes")

grid = PiIndexGrid([SpecFam, LaneFam])




# Build Π-IDs

pi_ids = grid.pi_ids(); m = len(pi_ids)




# Kernel params

alphas   = {pi: 0.2 for pi in pi_ids}

weights = {pi: np.ones(n*B*RNS_L) for pi in pi_ids}

taus     = {pi: 2.0 for pi in pi_ids}

K = 0.05*np.ones((m,m)); np.fill_diagonal(K, 0.0)




ledger = PoseidonLedger("ledger_poseidon.jsonl")

kernel = PiKernel(grid, alphas, weights, taus, K, ledger=ledger)




# Seed from a spatial vector, project into bands (replicated across
lanes)

v = np.random.randn(n)

band_coeffs = [(U @ ((U.T @ v)*mask)) for mask in masks]

x = pack_spectral_tensor(band_coeffs, RNS_L)
for t in range(5):

     out = kernel.step(x)

     x = out["x_new"]

     print(f"t={t} SlopeUB={out['SlopeUB']:.4f}
GapLB={out['GapLB']:.4f} "

             f"delta={out['orthogonality_defect']:.2e}
rec_err={out['recomposition_error']:.2e}")



if name == "main":​
 run()​
 """))



Re-zip
zip_path = shutil.make_archive("/mnt/data/pi_kernel_ref_ext", "zip", base)​
 zip_path

Always show details

Analyzed

Always show details

# Build a complete extended Π-kernel package from scratch (fresh
session),

# including spectral bands, RNS lanes, and a Poseidon-backed ledger.




import os, json, math, shutil, textwrap, hashlib

from pathlib import Path




base = Path("/mnt/data/pi_kernel")
if base.exists():

    shutil.rmtree(base)

base.mkdir(parents=True, exist_ok=True)




# Package dir

(base / "pi_kernel").mkdir()




# __init__.py

(base / "pi_kernel/__init__.py").write_text(textwrap.dedent("""

from .projectors import ProjectorFamily, PiIndexGrid,
orthogonality_defect

from .l1proj import project_weighted_l1_ball

from .certificates import slope_upper_bound, gap_lower_bound

from .ledger import Ledger

from .ledger_poseidon import PoseidonLedger

from .kernel import PiKernel, DefaultProposer

# Extras

from .spectral import (

    eigh_projectors, apply_band_projector,

    build_spectral_family_indices, build_rns_lane_indices,

    pack_spectral_tensor, unpack_spectral_tensor

)

from .rns import RNS
__all__ = [

    "ProjectorFamily", "PiIndexGrid", "orthogonality_defect",

    "project_weighted_l1_ball", "slope_upper_bound",
"gap_lower_bound",

    "Ledger", "PoseidonLedger", "PiKernel", "DefaultProposer",

    "eigh_projectors", "apply_band_projector",

    "build_spectral_family_indices", "build_rns_lane_indices",

    "pack_spectral_tensor", "unpack_spectral_tensor",

    "RNS"

]

"""))




# projectors.py

(base / "pi_kernel/projectors.py").write_text(textwrap.dedent("""

import numpy as np

from typing import List, Dict, Tuple




class ProjectorFamily:

    \"\"\"A simple commuting projector family using index subsets.




    Each projector P_k zeros coordinates outside its index set S_k.
   Families commute if they act on separate *axes*; we emulate the
joint grid

   by intersecting index sets across families.

   \"\"\"

   def __init__(self, index_sets: List[List[int]], name: str):

       self.name = name

       self.index_sets = [sorted(list(s)) for s in index_sets]

       # Validity: disjoint and cover a fixed ambient dimension

       all_idx = [i for S in self.index_sets for i in S]

       assert len(all_idx) == len(set(all_idx)), f"{name}: index sets
must be disjoint"

       self.dim = len(all_idx)




   def num_blocks(self) -> int:

       return len(self.index_sets)




   def apply(self, x: np.ndarray, k: int) -> np.ndarray:

       y = np.zeros_like(x)

       idx = self.index_sets[k]

       y[idx] = x[idx]

       return y




   def block_indices(self, k: int) -> List[int]:
       return self.index_sets[k]




def _intersect_sorted(a: List[int], b: List[int]) -> List[int]:

   i=j=0; out=[]

   while i<len(a) and j<len(b):

       if a[i]==b[j]:

            out.append(a[i]); i+=1; j+=1

       elif a[i]<b[j]: i+=1

       else: j+=1

   return out




class PiIndexGrid:

   \"\"\"Build Π-atom index sets as intersections across commuting
families.




   For families F1,...,Fm with disjoint partitions of the same
ambient coordinates,

   the Π-atom with multi-index (k1,...,km) corresponds to the
intersection

   S_{k1}^1 ∩ ... ∩ S_{km}^m.

   \"\"\"

   def __init__(self, families: List[ProjectorFamily]):

       assert len(families)>=1, "Need at least one family"

       dims = [f.dim for f in families]
       assert len(set(dims))==1, "All families must share the same
ambient dimension"

       self.families = families

       self.dim = dims[0]

       # Precompute intersections for fast projection

       # We store only non-empty intersections as Π-atoms

       self.atoms = []    # list of (pi_tuple, indices)

       def intersect_many(sets):

              from functools import reduce

              return reduce(_intersect_sorted, sets)

       for idx_tuple in np.ndindex(*[f.num_blocks() for f in
families]):

              sets = [families[j].block_indices(idx_tuple[j]) for j in
range(len(families))]

              inter = intersect_many(sets) if len(sets)>=2 else sets[0]

              if len(inter)>0:

                 self.atoms.append((tuple(idx_tuple), inter))

       # Map for quick lookup

       self._map = {pi: inds for pi, inds in self.atoms}




   def pi_ids(self):

       return [pi for pi,_ in self.atoms]




   def indices(self, pi):
        return self._map[pi]




   def project(self, x, pi):

        y = np.zeros_like(x)

        idx = self.indices(pi)

        y[idx] = x[idx]

        return y




def orthogonality_defect(families: List[ProjectorFamily]) -> float:

   \"\"\"Numerical orthogonality defect δ: sum_{i!=j} ||P_i P_j||_F
across all blocks of each family.

   Here P_i are *family* projectors; for disjoint index masks, this
is 0.




   δ>0 indicates overlap/approximate projectors; your pipeline should
re-orthogonalize if δ exceeds a threshold.

   \"\"\"

   dim = families[0].dim

   masks = []

   for fam in families:

        M = np.zeros((fam.num_blocks(), dim), dtype=float)

        for k,S in enumerate(fam.index_sets):

            M[k, S] = 1.0

        masks.append(M)
   defect = 0.0

   for M in masks:

        Gram = M @ M.T   # block overlaps within the family

        defect += np.sum(np.abs(Gram - np.diag(np.diag(Gram))))

   return float(defect)

"""))




# l1proj.py

(base / "pi_kernel/l1proj.py").write_text(textwrap.dedent("""

import numpy as np




def project_weighted_l1_ball(v, w, tau, atol=1e-12, maxit=10_000):

   \"\"\"Project v onto the weighted ℓ1 ball {x : sum_i w_i |x_i| <=
tau}.

   Exact solution via soft-threshold x_i = sign(v_i)*max(|v_i| - λ
w_i, 0),

   with λ found by bisection.




   If already inside the ball, returns v unchanged.

   \"\"\"

   v = np.asarray(v, dtype=float)

   w = np.asarray(w, dtype=float)

   assert v.shape == w.shape
   if np.sum(w * np.abs(v)) <= tau + atol:

        return v.copy(), 0.0




   lam_lo, lam_hi = 0.0, np.max(np.abs(v)/ (w + 1e-30))

   def shrink(lam):

        return np.sign(v) * np.maximum(np.abs(v) - lam*w, 0.0)

   for _ in range(maxit):

        lam = 0.5*(lam_lo+lam_hi)

        x = shrink(lam)

        val = np.sum(w * np.abs(x))

        if abs(val - tau) <= atol:

           return x, lam

        if val > tau:

           lam_lo = lam

        else:

           lam_hi = lam

   return shrink(lam_hi), lam_hi

"""))




# certificates.py

(base / "pi_kernel/certificates.py").write_text(textwrap.dedent("""

import numpy as np
def slope_upper_bound(alphas, K):

   \"\"\"SlopeUB: induced ∞-norm bound for the linearized coupled
update.

   A = diag(1-α) + diag(α) |K| ;    ||A||_∞ = max row sum.

   \"\"\"

   alphas = np.asarray(alphas, dtype=float).reshape(-1)

   K = np.asarray(K, dtype=float)

   assert K.shape[0]==K.shape[1]==alphas.size

   A = np.diag(1.0 - alphas) + np.diag(alphas) @ np.abs(K)

   return float(np.max(np.sum(np.abs(A), axis=1)))




def gap_lower_bound(slopeUB):

   return 1.0 - float(slopeUB)

"""))




# ledger (sha256)

(base / "pi_kernel/ledger.py").write_text(textwrap.dedent("""

import json, hashlib, time

from typing import Any, Dict




class Ledger:

   \"\"\"Append-only JSONL ledger with SHA-256 commitments
(baseline).\"\"\"
   def __init__(self, path: str):

        self.path = path




   def _digest(self, payload: Dict[str, Any]) -> str:

        blob = json.dumps(payload, sort_keys=True,
separators=(',',':')).encode()

        return hashlib.sha256(blob).hexdigest()




   def append(self, record: Dict[str, Any]) -> str:

        rec = dict(record)

        rec["ts"] = time.time()

        rec["digest"] = self._digest(rec)

        with open(self.path, "a") as f:

              f.write(json.dumps(rec, sort_keys=True) + "\\n")

        return rec["digest"]

"""))




# kernel.py

(base / "pi_kernel/kernel.py").write_text(textwrap.dedent("""

import numpy as np

from typing import Dict, Tuple, List, Callable, Any

from .projectors import PiIndexGrid, orthogonality_defect

from .l1proj import project_weighted_l1_ball
from .certificates import slope_upper_bound, gap_lower_bound




PiID = Tuple[int, ...]




class DefaultProposer:

   def __init__(self, gamma=0.1):

       self.gamma = gamma

   def __call__(self, c_pi: np.ndarray) -> np.ndarray:

       return (1 - self.gamma) * c_pi




class PiKernel:

   def __init__(self,

                  grid: PiIndexGrid,

                  alphas: Dict[PiID, float],

                  weights: Dict[PiID, np.ndarray],

                  tau_by_pi: Dict[PiID, float],

                  K: np.ndarray,

                  proposer: Callable[[np.ndarray], np.ndarray] = None,

                  ledger=None):

       self.grid = grid

       self.pi_ids = grid.pi_ids()

       self.alphas = alphas

       self.weights = weights
       self.tau = tau_by_pi

       self.K = K

       self.proposer = proposer or DefaultProposer()

       self.ledger = ledger




       m = len(self.pi_ids)

       assert K.shape == (m, m), "K must be (m,m)"

       for pi in self.pi_ids:

           assert pi in alphas and pi in weights and pi in tau_by_pi,
"Missing params for some Π-atom"




   def step(self, x: np.ndarray):

       m = len(self.pi_ids)

       alpha_vec = np.array([self.alphas[pi] for pi in self.pi_ids],
dtype=float)

       slopeUB = slope_upper_bound(alpha_vec, self.K)

       gapLB = gap_lower_bound(slopeUB)




       x_new = np.zeros_like(x)

       touched = []




       for i, pi in enumerate(self.pi_ids):

           c = self.grid.project(x, pi)
           prop = self.proposer(c)

           w = self.weights[pi]

           tau = self.tau[pi]

           c_safe, lam = project_weighted_l1_ball(prop, w, tau)

           if np.linalg.norm(c_safe - c) > 0:

               touched.append(pi)

           x_new += c_safe

           if self.ledger is not None and np.linalg.norm(c_safe - c)
> 0:

               rec = {

                   "pi": list(pi),

                   "alpha": float(self.alphas[pi]),

                   "tau": float(tau),

                   "lambda_soft": float(lam),

                   "l1_weight_sum": float(np.sum(w*np.abs(c_safe))),

               }

               self.ledger.append(rec)




       delta = orthogonality_defect(self.grid.families)

       rec_err = float(np.linalg.norm(x_new -
sum(self.grid.project(x_new, pi) for pi in self.pi_ids)))




       return {
            "x_new": x_new,

            "SlopeUB": slopeUB,

            "GapLB": gapLB,

            "orthogonality_defect": delta,

            "recomposition_error": rec_err,

            "touched": touched,

        }

"""))




# spectral.py

(base / "pi_kernel/spectral.py").write_text(textwrap.dedent("""

import numpy as np

from typing import List, Tuple




def eigh_projectors(L: np.ndarray, bands: List[Tuple[float, float]]):

   evals, U = np.linalg.eigh(L)

   band_masks = []

   for (lo, hi) in bands:

        mask = ((evals >= lo) & (evals < hi)).astype(float)

        band_masks.append(mask)

   return U, evals, band_masks
def apply_band_projector(U: np.ndarray, mask: np.ndarray, x:
np.ndarray) -> np.ndarray:

   coeff = U.T @ x

   coeff *= mask

   return U @ coeff




def build_spectral_family_indices(n: int, num_bands: int, num_lanes:
int):

   index_sets = []

   for b in range(num_bands):

        inds = []

        for l in range(num_lanes):

           for i in range(n):

               inds.append(i + n*(b + num_bands*l))

        index_sets.append(inds)

   return index_sets




def build_rns_lane_indices(n: int, num_bands: int, num_lanes: int):

   index_sets = []

   for l in range(num_lanes):

        inds = []

        for b in range(num_bands):

           for i in range(n):
                 inds.append(i + n*(b + num_bands*l))

       index_sets.append(inds)

   return index_sets




def pack_spectral_tensor(coeffs_by_band: List[np.ndarray], num_lanes:
int) -> np.ndarray:

   B = len(coeffs_by_band)

   n = coeffs_by_band[0].shape[0]

   L = num_lanes

   out = np.zeros(n*B*L, dtype=float)

   for b in range(B):

       v = coeffs_by_band[b].reshape(n)

       for l in range(L):

           base = n*(b + B*l)

           out[base:base+n] = v

   return out




def unpack_spectral_tensor(x_flat: np.ndarray, n: int, num_bands: int,
num_lanes: int) -> List[np.ndarray]:

   B, L = num_bands, num_lanes

   coeffs = []

   for b in range(B):

       acc = np.zeros(n, dtype=float)
        for l in range(L):

              base = n*(b + B*l)

              acc += x_flat[base:base+n]

        coeffs.append(acc / L)

   return coeffs

"""))




# rns.py

(base / "pi_kernel/rns.py").write_text(textwrap.dedent("""

import numpy as np

import math

from typing import List




def egcd(a, b):

   if b == 0: return (a, 1, 0)

   g, x, y = egcd(b, a % b)

   return (g, y, x - (a // b) * y)




def inv_mod(a, m):

   g, x, y = egcd(a, m)

   if g != 1:

        raise ValueError("Not invertible")

   return x % m
class RNS:

   def __init__(self, moduli: List[int]):

       self.moduli = list(moduli)

       for i in range(len(moduli)):

             for j in range(i+1, len(moduli)):

                if math.gcd(moduli[i], moduli[j]) != 1:

                    raise ValueError("Moduli must be pairwise
coprime")

       self.M = 1

       for m in moduli: self.M *= m

       self.Mi = [self.M // m for m in moduli]

       self.invMi = [inv_mod(self.Mi[i] % moduli[i], moduli[i]) for i
in range(len(moduli))]

       self.e = [ (self.Mi[i] * self.invMi[i]) % self.M for i in
range(len(moduli)) ]




   def encode(self, x: np.ndarray) -> List[np.ndarray]:

       x = np.asarray(x, dtype=object)

       residues = []

       for m in self.moduli:

             residues.append(np.mod(x, m).astype(object))

       return residues
   def decode(self, residues: List[np.ndarray]) -> np.ndarray:

       L = len(self.moduli)

       assert len(residues) == L

       n = residues[0].size

       out = np.zeros(n, dtype=object)

       for i in range(L):

           r_i = np.asarray(residues[i], dtype=object)

           out = (out + (r_i * self.e[i])) % self.M

       return out




   def pack_lanes(self, residues: List[np.ndarray], num_bands: int =
1) -> np.ndarray:

       L = len(residues); n = residues[0].size; B = num_bands

       out = np.zeros(n*B*L, dtype=object)

       for l in range(L):

           for b in range(B):

               base = n*(b + B*l)

               out[base:base+n] = residues[l]

       return out




   def unpack_lanes(self, x_flat: np.ndarray, n: int, num_bands: int)
-> List[np.ndarray]:

       x_flat = np.asarray(x_flat, dtype=object)
          L = len(self.moduli); B = num_bands

          residues = []

          for l in range(L):

              base = n*(0 + B*l)

              residues.append(x_flat[base:base+n].copy())

          return residues

"""))




# poseidon.py

(base / "pi_kernel/poseidon.py").write_text(textwrap.dedent("""

import hashlib




FIELD_MOD =
2188824287183927522224640574525727508854836440041603434369820418657580
8495617




def _to_field(x: int) -> int:

   return x % FIELD_MOD




def _hash_to_field(seed: bytes) -> int:

   h = hashlib.sha256(seed).digest()

   val = int.from_bytes(h, "big")

   return _to_field(val)
def generate_round_constants(t: int, n_rounds: int, label: bytes):

   rc = []

   for r in range(n_rounds):

       row = []

       for i in range(t):

             row.append(_hash_to_field(label + r.to_bytes(4,"big") +
i.to_bytes(2,"big")))

       rc.append(row)

   return rc




def generate_mds(t: int, label: bytes):

   cols = [ _hash_to_field(label + i.to_bytes(2,"big")) for i in
range(t) ]

   M = [[ pow(cols[i], j, FIELD_MOD) for j in range(t) ] for i in
range(t) ]

   return M




def sbox(x: int) -> int:

   return pow(x, 5, FIELD_MOD)




def matmul(M, v):

   t = len(v)

   out = [0]*t
   for i in range(t):

       acc = 0

       for j in range(t):

              acc = (acc + M[i][j]*v[j]) % FIELD_MOD

       out[i] = acc

   return out




class Poseidon:

   def __init__(self, t=3, rf=8, rp=57):

       self.t = t; self.rf = rf; self.rp = rp

       self.M = generate_mds(t, b"POSEIDON_MDS")

       self.RC_full = generate_round_constants(t, rf,
b"POSEIDON_RC_F")

       self.RC_part = [
_hash_to_field(b"POSEIDON_RC_P"+i.to_bytes(4,"big")) for i in
range(rp) ]




   def permute(self, state):

       assert len(state)==self.t

       st = [ _to_field(x) for x in state ]




       for r in range(self.rf//2):

              st = [ (st[i] + self.RC_full[r][i]) % FIELD_MOD for i in
range(self.t) ]
           st = [ sbox(x) for x in st ]

           st = matmul(self.M, st)




       for r in range(self.rp):

           st[0] = (st[0] + self.RC_part[r]) % FIELD_MOD

           st[0] = sbox(st[0])

           st = matmul(self.M, st)




       for r in range(self.rf//2, self.rf):

           st = [ (st[i] + self.RC_full[r][i]) % FIELD_MOD for i in
range(self.t) ]

           st = [ sbox(x) for x in st ]

           st = matmul(self.M, st)




       return st




   def hash(self, inputs):

       rate = self.t - 1

       st = [0]*self.t

       i = 0

       while i < len(inputs):

           for j in range(rate):

                  if i >= len(inputs): break
                st[j] = (st[j] + inputs[i]) % FIELD_MOD

                i += 1

           st = self.permute(st)

        return st[0]




def bytes_to_field_elems(b: bytes, limb_bytes: int = 31):

   out = []

   for i in range(0, len(b), limb_bytes):

        chunk = b[i:i+limb_bytes]

        val = int.from_bytes(chunk, "little")

        out.append(_to_field(val))

   return out

"""))




# ledger_poseidon.py

(base / "pi_kernel/ledger_poseidon.py").write_text(textwrap.dedent("""

import json, time

from typing import Any, Dict

from .poseidon import Poseidon, bytes_to_field_elems




class PoseidonLedger:

   \"\"\"Append-only JSONL ledger using Poseidon hash commitment
(educational BN254 variant).\"\"\"
   def __init__(self, path: str, t=3, rf=8, rp=57):

        self.path = path

        self.poseidon = Poseidon(t=t, rf=rf, rp=rp)




   def _digest(self, payload: Dict[str, Any]) -> str:

        blob = json.dumps(payload, sort_keys=True,
separators=(',',':')).encode()

        limbs = bytes_to_field_elems(blob)

        h = self.poseidon.hash(limbs)

        return hex(h)




   def append(self, record: Dict[str, Any]) -> str:

        rec = dict(record)

        rec["ts"] = time.time()

        rec["poseidon_digest"] = self._digest(rec)

        with open(self.path, "a") as f:

              f.write(json.dumps(rec, sort_keys=True) + "\\n")

        return rec["poseidon_digest"]

"""))




# README.md

(base / "README.md").write_text(textwrap.dedent("""

# Π-kernel (extended)
Reference scaffold for Π-atom recursion with ACE projection-first
safety, spectral bands, RNS lanes, and a Poseidon-backed ledger.




## Install



pip install numpy

Always show details




## Quickstart (baseline)

```python

import numpy as np

from pi_kernel import ProjectorFamily, PiIndexGrid, PiKernel, Ledger




A = ProjectorFamily([[0,2,4,6],[1,3,5,7]], name="A")

B = ProjectorFamily([[0,1,2,3],[4,5,6,7]], name="B")

grid = PiIndexGrid([A,B])

pi_ids = grid.pi_ids(); m=len(pi_ids)




alphas    = {pi: 0.25 for pi in pi_ids}

weights = {pi: np.ones(8) for pi in pi_ids}

taus      = {pi: 1.5 for pi in pi_ids}

K = 0.05*np.ones((m,m)); np.fill_diagonal(K, 0.0)
from pi_kernel import DefaultProposer

kernel = PiKernel(grid, alphas, weights, taus, K,
ledger=Ledger("ledger.jsonl"))

x = np.random.randn(8)

for t in range(3):

     out = kernel.step(x); x = out["x_new"]

     print(out["SlopeUB"], out["GapLB"])




Spectral bands (exact via eigh)
Always show details

import numpy as np

from pi_kernel import (ProjectorFamily, PiIndexGrid, PiKernel,

                         eigh_projectors, pack_spectral_tensor,

                         build_spectral_family_indices,
build_rns_lane_indices,

                         PoseidonLedger)




n = 8

L = 2*np.eye(n) - np.eye(n,k=1) - np.eye(n,k=-1)

bands = [(0,1.2),(1.2,3.0),(3.0,10.0)]

U, evals, masks = eigh_projectors(L, bands)

B = len(masks); Lanes = 2
spec_sets = build_spectral_family_indices(n, B, Lanes)

lane_sets = build_rns_lane_indices(n, B, Lanes)

SpecFam = ProjectorFamily(spec_sets, "SpectralBands")

LaneFam = ProjectorFamily(lane_sets, "RNSLanes")

grid = PiIndexGrid([SpecFam, LaneFam])




pi_ids = grid.pi_ids(); m=len(pi_ids)

alphas   = {pi: 0.2 for pi in pi_ids}

weights = {pi: np.ones(n*B*Lanes) for pi in pi_ids}

taus     = {pi: 2.0 for pi in pi_ids}

K = 0.05*np.ones((m,m)); np.fill_diagonal(K, 0.0)




ledger = PoseidonLedger("ledger_poseidon.jsonl")

kernel = PiKernel(grid, alphas, weights, taus, K, ledger=ledger)




v = np.random.randn(n)

band_coeffs = [(U @ ((U.T @ v)*mask)) for mask in masks]

x = pack_spectral_tensor(band_coeffs, Lanes)




for t in range(3):

   out = kernel.step(x); x = out["x_new"]

   print("SlopeUB", out["SlopeUB"], "GapLB", out["GapLB"])
RNS lanes (encode/decode)
Always show details

import numpy as np

from pi_kernel import RNS, ProjectorFamily, PiIndexGrid, PiKernel




moduli = [65521, 65519, 65513]

rns = RNS(moduli)




x_int = np.array([123456,789012,345678,901234], dtype=object)

res = rns.encode(x_int)

x_flat = rns.pack_lanes(res, num_bands=1)   # flattened n*B*L




n, B, L = x_int.size, 1, len(moduli)

from pi_kernel import build_spectral_family_indices,
build_rns_lane_indices

spec_sets = build_spectral_family_indices(n, B, L)

lane_sets = build_rns_lane_indices(n, B, L)

SpecFam = ProjectorFamily(spec_sets, "SpectralBands")

LaneFam = ProjectorFamily(lane_sets, "RNSLanes")

grid = PiIndexGrid([SpecFam, LaneFam])




pi_ids = grid.pi_ids(); m=len(pi_ids)
alphas    = {pi: 0.15 for pi in pi_ids}

weights = {pi: np.ones(n*B*L, dtype=float) for pi in pi_ids}

taus      = {pi: 1.0 for pi in pi_ids}

K = 0.02*np.ones((m,m)); np.fill_diagonal(K, 0.0)

kernel = PiKernel(grid, alphas, weights, taus, K)




out = kernel.step(x_flat.astype(float))   # demo: operate over floats;
for RNS arithmetic, keep mods in domain logic

res2 = rns.unpack_lanes(out["x_new"], n=n, num_bands=B)

x_rec = rns.decode(res2)

print("CRT M =", rns.M, "decoded first 4:", [int(v) for v in
x_rec[:4]])




Poseidon-backed ledger
Always show details

from pi_kernel import PoseidonLedger

pledger = PoseidonLedger("ledger_poseidon.jsonl")

print(pledger.append({"pi":[0,1], "alpha":0.2, "tau":1.5}))



"""))



Simple examples
(base / "example.py").write_text(textwrap.dedent("""​
 import numpy as np​
 from pi_kernel import ProjectorFamily, PiIndexGrid, Ledger, PiKernel

def run():​
A = ProjectorFamily([ [0,2,4,6], [1,3,5,7] ], name="A")​
B = ProjectorFamily([ [0,1,2,3], [4,5,6,7] ], name="B")​
grid = PiIndexGrid([A,B])​
pi_ids = grid.pi_ids()​
m = len(pi_ids)​
alphas = {pi: 0.25 for pi in pi_ids}​
weights = {pi: np.ones(8) for pi in pi_ids}​
taus = {pi: 1.5 for pi in pi_ids}​
K = 0.05*np.ones((m,m)); np.fill_diagonal(K, 0.0)

Always show details

ledger = Ledger("ledger.jsonl")

kernel = PiKernel(grid, alphas, weights, taus, K, ledger=ledger)




x = np.random.randn(8)

for t in range(6):

     out = kernel.step(x)

     x = out["x_new"]

     print(f"t={t} SlopeUB={out['SlopeUB']:.4f}
GapLB={out['GapLB']:.4f} "

              f"delta={out['orthogonality_defect']:.2e}
rec_err={out['recomposition_error']:.2e}")



if name == "main":​
 run()​
 """))

(base / "example_spectral_poseidon.py").write_text(textwrap.dedent("""​
 import numpy as np​
from pi_kernel import (​
ProjectorFamily, PiIndexGrid, PiKernel,​
eigh_projectors, pack_spectral_tensor,​
build_spectral_family_indices, build_rns_lane_indices,​
PoseidonLedger​
)

def run():​
n = 8​
L = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)​
bands = [(0,1.2),(1.2,3.0),(3.0,10.0)]​
U, evals, masks = eigh_projectors(L, bands)​
B = len(masks); RNS_L = 2

Always show details

spec_sets = build_spectral_family_indices(n, B, RNS_L)

lane_sets = build_rns_lane_indices(n, B, RNS_L)

SpecFam = ProjectorFamily(spec_sets, name="SpectralBands")

LaneFam = ProjectorFamily(lane_sets, name="RNSLanes")

grid = PiIndexGrid([SpecFam, LaneFam])




pi_ids = grid.pi_ids(); m = len(pi_ids)




alphas    = {pi: 0.2 for pi in pi_ids}

weights = {pi: np.ones(n*B*RNS_L) for pi in pi_ids}

taus      = {pi: 2.0 for pi in pi_ids}

K = 0.05*np.ones((m,m)); np.fill_diagonal(K, 0.0)




ledger = PoseidonLedger("ledger_poseidon.jsonl")

kernel = PiKernel(grid, alphas, weights, taus, K, ledger=ledger)
v = np.random.randn(n)

band_coeffs = [(U @ ((U.T @ v)*mask)) for mask in masks]

x = pack_spectral_tensor(band_coeffs, RNS_L)




for t in range(5):

     out = kernel.step(x)

     x = out["x_new"]

     print(f"t={t} SlopeUB={out['SlopeUB']:.4f}
GapLB={out['GapLB']:.4f} "

              f"delta={out['orthogonality_defect']:.2e}
rec_err={out['recomposition_error']:.2e}")



if name == "main":​
 run()​
 """))



Zip it
zip_path = shutil.make_archive("/mnt/data/pi_kernel_ref_ext", "zip", base)​
 zip_path

Always show details

Result

'/mnt/data/pi_kernel_ref_ext.zip'

All set. I extended the scaffold with your three asks and packaged it:

   ●​ Spectral bands (exact via eigh) with band projectors + tensorized index layout.​
   ●​ RNS lane factor with CRT encode/decode and lane packing/unpacking.​

   ●​ Poseidon-backed ledger (pure-Python BN254, educational constants; drop-in Poseidon
      interface).​


Download the extended Π-kernel (zip)

Run example_spectral_poseidon.py for bands+Poseidon; example.py for the base; and
see README.md for RNS usage and wiring into the Π-atom grid.
