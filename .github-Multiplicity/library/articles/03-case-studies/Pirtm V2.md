---
slug: pirtm-v2
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Pirtm V2.md
  last_synced: '2026-03-20T17:17:20.979453Z'
---

PIRTM v2.9 — Witnessed Contraction Wrapper +
Auditable Identity
     Core idea: certify contractive update maps (stability) while keeping forcing as diagnostics
     (stress tests), and record witnessed identity/provenance artifacts for replayability.




0. Scope and non-goals

In scope (core)

    • Contractive recursion wrapper for iterative systems/optimizers.
    • Explicit separation of:
    • pure update map Φ (certified)
    • forcing/input Ft (diagnostics only)
    • Optional nonexpansive projection/clamp P (PSMC-style).
    • Additive perturbation budget composition.
    • Versioned identity/provenance with PETC-style signatures and witnessed transforms.
    • Deterministic audit log + independent verifier.

Out of scope (extensions)

    • Quantum/diamond norm/Hermitian-gap certification (allowed only via verified artifacts).
    • Byzantine fault tolerance / distributed ledgers.
    • Any claim of “unification” across physics/crypto/AI.




1. Formal objects

1.1 Normed state space and domain

    • State space: (X, ∥ ⋅ ∥) (Banach; in practice finite-dimensional tensors with a chosen norm).
    • Certified domain D ⊆ X : the set on which Lipschitz bounds are claimed.
    • Domain must be explicit and referenced by domain_id .

1.2 Update map and forcing

    • Dynamics: $$ T_{t+1} = \Phi_{\theta'}(T_t) + F_t. $$
    • Certification acts on Φθ′ only.
    • Forcing Ft is free, but its impact is bounded via input-to-state gain envelopes.




                                                     1
1.3 Nonexpansive safety projection

      • Optional clamp/projection P with witness of nonexpansiveness: $$ \mathrm{Lip}(P;D,|\cdot|) \le 1.
        $$
      • Wrapped update: $$ \Phi \leftarrow P \circ \Phi. $$

1.4 Additive perturbation budget

You may decompose the raw proposal map as:


$$ \Phi = P\circ (K + \Lambda\,\mathcal T + \kappa\,C) $$


and certify contractivity with a composable Lipschitz budget on the same (D, ∥ ⋅ ∥):


$$ \mathrm{Lip}(\Phi) \le \mathrm{Lip}(P)\left(\mathrm{Lip}(K)+|\Lambda|\,\mathrm{Lip}(\mathcal T)+|
\kappa|\,\mathrm{Lip}(C)\right). $$


1.5 Identity/provenance (PETC signatures)

      • Registry version pins a finite vocabulary slice Vk .
      • Signature space:
           +
      • Sig (Vk ) = {e : Vk → N finitely supported}
      • Operations are performed on signatures (sparse exponent maps), not prime products.
      • Witnessed transforms (reshape/coarsen/pushforward) are required for any lossy or structural
        change.




2. Theorem statements (spec-grade)
       All Lipschitz statements are on a certified domain D under the selected norm ∥ ⋅ ∥. Each
       theorem is checkable by an independent verifier given the emitted artifacts.


T1 — Banach contraction fixed point (constant forcing)

Assume Φ : D → D is contractive:


$$ |\Phi(x)-\Phi(y)|\le c|x-y|,\quad 0\le c<1. $$


If Ft ≡ F is constant, then the affine map x ↦ Φ(x) + F has a unique fixed point T ∗ ∈ D , and iterates
converge:


$$ |T_t - T^| \le c^t\,|T_0 - T^|. $$




                                                         2
T2 — BIBS stability and input-to-state gain envelope
                                ~         ~      ~
Let Tt+1 = Φ(Tt ) + Ft and Tt+1 = Φ(Tt ) + Ft with the same contractive Φ (constant c < 1). Then for all
t ≥ 0:

$$ |T_t-\tilde T_t|\le c^t|T_0-\tilde T_0|+\sum_{k=0}^{t-1}c^{t-1-k}\,|F_k-\tilde F_k|. $$


This is the certified gain envelope used for forcing-based diagnostics.


T3 — Neumann tail bound (affine/linear only)

For the affine recurrence Tt+1 = ATt + F with induced operator norm ∥A∥ ≤ c < 1, the fixed point is
T ∗ = (I − A)−1 F and the Neumann series converges:

$$ (I-A)^{-1}=\sum_{j=0}^\infty A^j. $$


Tail after n terms satisfies:


$$ \Big|\sum_{j=n+1}^\infty A^jF\Big|\le \frac{c^{n+1}}{1-c}\,|F|. $$


T4 — Picard convergence bound (general contractive map)

If Φ is contractive on D with constant c < 1, then the Picard iterates satisfy:


$$ |T_{t+1}-T_t|\le c\,|T_t-T_{t-1}|\Rightarrow|T_t-T^*|\le \frac{c^t}{1-c}\,|T_1-T_0|. $$


T5 — Nonexpansive composition safety

If P is nonexpansive on D : Lip(P ) ≤ 1, and Φ is contractive with Lip(Φ) ≤ c, then


$$ \mathrm{Lip}(P\circ\Phi)\le \mathrm{Lip}(P)\,\mathrm{Lip}(\Phi)\le c. $$


Thus adding a nonexpansive clamp cannot break an existing contraction guarantee.


T6 — Additive perturbation budget

Let Ψ = K + ΛT + κC and assume each component is Lipschitz on D under the same norm: Lip(K) =
cK , Lip(T ) = cT , Lip(C) = cC . Then

$$ \mathrm{Lip}(\Psi)\le c_K + |\Lambda|c_T + |\kappa|c_C. $$


If P is nonexpansive and


$$ c_K + |\Lambda|c_T + |\kappa|c_C \le 1-\delta, $$


then Φ = P ∘ Ψ is contractive with constant ≤ 1 − δ .



                                                        3
T7 — Multi-resolution weighted composition (optional module)

Let Ap be a finite family of operators on D with Lip(Ap ) ≤ cp and weights wp . Then


$$ \mathrm{Lip}\Big(\sum_p w_p A_p\Big)\le \sum_p |w_p|\,c_p. $$


Traceability requires an independent ladder witness for injective resolution mapping; it is not implied by
contractivity.




3. Artifact formats (JSON schemas)

3.1 Canonical IDs

      • registry_version : semantic atom → ID mapping version.
      • operator_version : implementation/version of map Φ or components.
      • norm_id : e.g., l2 , linf , weighted_l1:alpha=... .
      • domain_id : e.g., ball:l2:R=... , box:linf:B=... , trust_region:... .

3.2 Certificate artifact (core)


  {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "PIRTM.Certificate",
      "type": "object",
      "required": [
         "certificate_id",
         "level",
         "norm_id",
         "domain_id",
         "lipschitz_upper",
         "delta",
         "status",
         "artifact",
         "created_at"
      ],
      "properties": {
        "certificate_id": {"type": "string"},
        "level": {
          "type": "string",
          "enum": [
            "L0_heuristic",
            "L1_norm_bound",
            "L2_power_iter",
            "L3_nonexpansive_clamp",
            "L4_perturbation_budget",




                                                    4
               "L5_external_verified"
           ]
         },
         "norm_id": {"type": "string"},
         "domain_id": {"type": "string"},
         "lipschitz_upper": {"type": "number", "minimum": 0},
         "delta": {"type": "number", "minimum": 0, "maximum": 1},
         "status": {"type": "string", "enum": ["ACCEPT", "REJECT"]},
         "artifact": {"type": "object"},
         "created_at": {"type": "string"}
     }
 }


3.3 Domain witness


 {
   "$schema": "https://json-schema.org/draft/2020-12/schema",
   "title": "PIRTM.DomainWitness",
   "type": "object",
   "required": ["domain_id", "norm_id", "kind", "params", "assumptions"],
   "properties": {
     "domain_id": {"type": "string"},
     "norm_id": {"type": "string"},
     "kind": {"type": "string", "enum": ["ball", "box", "trust_region",
 "custom"]},
     "params": {"type": "object"},
     "assumptions": {"type": "array", "items": {"type": "string"}}
   }
 }


3.4 Perturbation budget artifact


 {
     "$schema": "https://json-schema.org/draft/2020-12/schema",
     "title": "PIRTM.PerturbationBudget",
     "type": "object",
     "required": ["norm_id", "domain_id", "terms", "total_bound"],
     "properties": {
       "norm_id": {"type": "string"},
       "domain_id": {"type": "string"},
       "terms": {
         "type": "array",
         "items": {
           "type": "object",
           "required": ["name", "weight", "lip"],




                                            5
               "properties": {
                 "name": {"type": "string"},
                 "weight": {"type": "number"},
                 "lip": {"type": "number", "minimum": 0},
                 "witness": {"type": "object"}
               }
           }
         },
         "total_bound": {"type": "number", "minimum": 0}
     }
 }


3.5 Forcing diagnostic artifact


 {
     "$schema": "https://json-schema.org/draft/2020-12/schema",
     "title": "PIRTM.ForcingDiagnostic",
     "type": "object",
     "required": [
        "norm_id",
        "domain_id",
        "certified_c",
        "window",
        "envelope_violations",
        "gain_stats"
     ],
     "properties": {
        "norm_id": {"type": "string"},
        "domain_id": {"type": "string"},
        "certified_c": {"type": "number", "minimum": 0, "maximum": 1},
        "window": {"type": "integer", "minimum": 1},
        "envelope_violations": {"type": "integer", "minimum": 0},
        "gain_stats": {
          "type": "object",
          "required": ["p50", "p95", "max"],
          "properties": {
            "p50": {"type": "number"},
            "p95": {"type": "number"},
            "max": {"type": "number"}
          }
        }
     }
 }




                                              6
3.6 Audit log entry (hash-chained)


 {
     "$schema": "https://json-schema.org/draft/2020-12/schema",
     "title": "PIRTM.AuditLogEntry",
     "type": "object",
     "required": [
       "seq",
       "prev_hash",
       "entry_hash",
       "registry_version",
       "operator_version",
       "determinism",
       "seed",
       "theta_raw_hash",
       "theta_cert_hash",
       "certificate",
       "inputs_hash",
       "outputs_hash",
       "timestamp"
     ],
     "properties": {
       "seq": {"type": "integer", "minimum": 0},
       "prev_hash": {"type": "string"},
       "entry_hash": {"type": "string"},
       "registry_version": {"type": "string"},
       "operator_version": {"type": "string"},
       "determinism": {"type": "string", "enum": ["best_effort", "strict"]},
       "seed": {"type": "integer"},
       "theta_raw_hash": {"type": "string"},
       "theta_cert_hash": {"type": "string"},
       "certificate": {"$ref": "#/definitions/Certificate"},
       "inputs_hash": {"type": "string"},
       "outputs_hash": {"type": "string"},
       "timestamp": {"type": "string"}
   },
   "definitions": {
      "Certificate": {
        "type": "object",
        "required": ["level", "norm_id", "domain_id", "lipschitz_upper", "delta",
 "status", "artifact"],
        "properties": {
          "level": {"type": "string"},
          "norm_id": {"type": "string"},
          "domain_id": {"type": "string"},
          "lipschitz_upper": {"type": "number"},
          "delta": {"type": "number"},




                                          7
                  "status": {"type": "string"},
                  "artifact": {"type": "object"}
              }
          }
      }
  }


3.7 PETC signature + witness artifacts (minimal)

Signature (sparse exponent map):



  {
      "registry_version": "vX.Y",
      "sig": {"token:A": 2, "token:B": 1, "axis:time": 1}
  }


Reshape witness (example skeleton):



  {
      "kind": "reshape",
      "from": {"axes": ["batch", "time", "feat"], "shape": [32, 128, 64]},
      "to": {"axes": ["batch", "feat", "time"], "shape": [32, 64, 128]},
      "bijection": "permute",
      "proof": {"perm": [0, 2, 1]}
  }




4. Minimal reference implementation skeleton (pure Python +
NumPy + optional PyTorch)
          This is intentionally minimal: a runnable scaffold that demonstrates (i) certification on Φ, (ii)
          optional nonexpansive clamp P , (iii) forcing diagnostics and (iv) independent verification.



  # pirtm_v29_skeleton.py
  from __future__ import annotations

  from dataclasses import dataclass
  from typing import Any, Dict, Optional, Tuple, Protocol, Literal
  import hashlib
  import json
  import time




                                                         8
import numpy as np

try:
       import torch
       TORCH_OK = True
except Exception:
    TORCH_OK = False



# -----------------------------
# Utilities
# -----------------------------

def sha256_json(obj: Any) -> str:
    """Stable hash of JSON-serializable objects."""
    s = json.dumps(obj, sort_keys=True, separators=(",", ":"),
ensure_ascii=False)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()



def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())



def norm(x: np.ndarray, norm_id: str) -> float:
    if norm_id == "l2":
        return float(np.linalg.norm(x.ravel(), ord=2))
    if norm_id == "linf":
        return float(np.linalg.norm(x.ravel(), ord=np.inf))
    raise ValueError(f"unknown norm_id={norm_id}")



# -----------------------------
# Domain
# -----------------------------

class Domain(Protocol):
       domain_id: str
       norm_id: str

       def contains(self, x: np.ndarray) -> bool:
           ...

       def witness(self) -> Dict[str, Any]:
           ...



@dataclass(frozen=True)



                                          9
class BallDomain:
    domain_id: str
    norm_id: str
    radius: float


    def contains(self, x: np.ndarray) -> bool:
        return norm(x, self.norm_id) <= self.radius + 1e-12

    def witness(self) -> Dict[str, Any]:
        return {
             "domain_id": self.domain_id,
             "norm_id": self.norm_id,
             "kind": "ball",
             "params": {"radius": self.radius},
             "assumptions": ["State is kept within the ball by construction/
clamping."],
        }



# -----------------------------
# Map interface
# -----------------------------

LipResult = Tuple[Optional[float], Dict[str, Any]]     # (bound, artifact) ;
bound=None => unknown



class Map(Protocol):
    operator_version: str

    def apply(self, x: np.ndarray, theta: Any) -> np.ndarray:
        ...

    def lipschitz_upper(self, theta: Any, domain: Domain) -> LipResult:
        ...

    def project(self, theta: Any, domain: Domain, delta: float) -> Tuple[Any,
Dict[str, Any]]:
        """Return theta' and projection artifact."""
        ...



# -----------------------------
# Example: linear map Phi(x)=A x
# -----------------------------

@dataclass
class LinearMap:



                                       10
    operator_version: str = "LinearMap@v0"

    def apply(self, x: np.ndarray, theta: Dict[str, Any]) -> np.ndarray:
        A = theta["A"]
        return A @ x


    def lipschitz_upper(self, theta: Dict[str, Any], domain: Domain) ->
LipResult:
        A = theta["A"]
           # Use induced norm upper bounds. For l2: spectral norm; for linf: max
row sum.
        if domain.norm_id == "l2":
            # spectral norm is exact for matrices but may be expensive; ok for
skeleton.
            s = float(np.linalg.norm(A, ord=2))
            art = {"method": "matrix_spectral_norm", "value": s}
            return s, art
        if domain.norm_id == "linf":
            s = float(np.linalg.norm(A, ord=np.inf))
            art = {"method": "matrix_linf_row_sum", "value": s}
            return s, art
        return None, {"method": "unknown_norm"}

    def project(self, theta: Dict[str, Any], domain: Domain, delta: float) ->
Tuple[Dict[str, Any], Dict[str, Any]]:
        # Simple projection: scale A down so ||A|| <= 1-delta.
        A = theta["A"].copy()
        bound, art = self.lipschitz_upper({"A": A}, domain)
        if bound is None:
            raise ValueError("cannot project without a bound")
        target = 1.0 - delta
        if bound <= target:
            return {"A": A}, {"projected": False, "scale": 1.0, "pre_bound":
bound, "target": target}
        scale = target / (bound + 1e-12)
        A2 = A * scale
        return {"A": A2}, {"projected": True, "scale": scale, "pre_bound":
bound, "target": target}



# -----------------------------
# Nonexpansive clamp P (PSMC-style)
# -----------------------------

class Clamp(Protocol):
    clamp_version: str

    def apply(self, x: np.ndarray, domain: Domain) -> np.ndarray:



                                          11
        ...

    def lip_witness(self, domain: Domain) -> Dict[str, Any]:
        """Return a witness that Lip(P)<=1 on the domain."""
        ...



@dataclass
class BallProjectClamp:
    clamp_version: str = "BallProjectClamp@v0"

    def apply(self, x: np.ndarray, domain: Domain) -> np.ndarray:
        if not isinstance(domain, BallDomain):
            return x # noop
        r = domain.radius
        n = norm(x, domain.norm_id)
        if n <= r:
            return x
        return x * (r / (n + 1e-12))

    def lip_witness(self, domain: Domain) -> Dict[str, Any]:
        return {
            "kind": "nonexpansive_projection",
            "claim": "Lip<=1",
            "domain_id": domain.domain_id,
            "norm_id": domain.norm_id,
            "note":
"Metric projection onto a closed convex ball is nonexpansive in Hilbert spaces
(l2).",
        }



# -----------------------------
# Certification
# -----------------------------

CertLevel = Literal[
    "L0_heuristic",
    "L1_norm_bound",
    "L2_power_iter",
    "L3_nonexpansive_clamp",
    "L4_perturbation_budget",
    "L5_external_verified",
]



@dataclass(frozen=True)
class Certificate:



                                       12
    certificate_id: str
    level: CertLevel
    norm_id: str
    domain_id: str
    lipschitz_upper: float
    delta: float
    status: Literal["ACCEPT", "REJECT"]
    artifact: Dict[str, Any]
    created_at: str



@dataclass(frozen=True)
class CertResult:
    status: Literal["ACCEPT", "REJECT"]
    theta_cert: Optional[Any]
    certificate: Certificate
    reason: Optional[str] = None



def certify(
    phi: Map,
    theta_raw: Any,
    domain: Domain,
    delta: float,
    clamp: Optional[Clamp] = None,
) -> CertResult:
    bound, art = phi.lipschitz_upper(theta_raw, domain)

    cert_id = sha256_json({"theta": str(type(theta_raw)), "t": now_iso(), "op":
phi.operator_version})

    if bound is not None and bound <= 1.0 - delta:
        cert = Certificate(
            certificate_id=cert_id,
            level="L1_norm_bound",
            norm_id=domain.norm_id,
            domain_id=domain.domain_id,
            lipschitz_upper=float(bound),
            delta=float(delta),
            status="ACCEPT",
            artifact={"lip": art, "domain": domain.witness()},
            created_at=now_iso(),
        )
        return CertResult("ACCEPT", theta_raw, cert)

    # Optional clamp path: if clamp exists, we can wrap the map by clamping
state each step.
    if clamp is not None:



                                          13
          # Clamp itself must be nonexpansive (witnessed). This is a safety
module.
        clamp_w = clamp.lip_witness(domain)
        # We do not change the Lipschitz bound of phi, but we ensure the
trajectory remains in domain.
        # In a full implementation, you may require the domain to be invariant
under clamp.
        # If we still can't certify phi, proceed to projection.


    # Projection to certified theta'
    try:
         theta_proj, proj_art = phi.project(theta_raw, domain, delta)
         b2, art2 = phi.lipschitz_upper(theta_proj, domain)
    except Exception as e:
         cert = Certificate(
             certificate_id=cert_id,
             level="L0_heuristic",
             norm_id=domain.norm_id,
             domain_id=domain.domain_id,
             lipschitz_upper=float("inf"),
             delta=float(delta),
             status="REJECT",
             artifact={"error": str(e), "domain": domain.witness()},
             created_at=now_iso(),
         )
         return CertResult("REJECT", None, cert, reason="projection_failed")

    if b2 is not None and b2 <= 1.0 - delta:
        cert = Certificate(
            certificate_id=cert_id,
            level="L1_norm_bound",
            norm_id=domain.norm_id,
            domain_id=domain.domain_id,
            lipschitz_upper=float(b2),
            delta=float(delta),
            status="ACCEPT",
            artifact={"lip": art2, "projection": proj_art, "domain":
domain.witness()},
            created_at=now_iso(),
        )
        return CertResult("ACCEPT", theta_proj, cert)

    cert = Certificate(
        certificate_id=cert_id,
        level="L1_norm_bound" if b2 is not None else "L0_heuristic",
        norm_id=domain.norm_id,
        domain_id=domain.domain_id,
        lipschitz_upper=float(b2) if b2 is not None else float("inf"),



                                         14
        delta=float(delta),
        status="REJECT",
        artifact={"lip": art2, "projection": proj_art, "domain":
domain.witness()},
        created_at=now_iso(),
    )
    return CertResult("REJECT", None, cert, reason="could_not_certify")



# -----------------------------
# Forcing diagnostics (gain envelope)
# -----------------------------

def gain_envelope(c: float, dF_norms: np.ndarray) -> float:
    # returns sum_{k=0}^{t-1} c^{t-1-k} ||dF_k||, assuming dF_norms ordered
oldest->newest
    t = len(dF_norms)
    weights = np.array([c ** (t - 1 - k) for k in range(t)], dtype=np.float64)
    return float(np.sum(weights * dF_norms))



# -----------------------------
# Audit logging (hash chained)
# -----------------------------

@dataclass
class AuditLog:
    registry_version: str
    determinism: Literal["best_effort", "strict"] = "best_effort"
    seed: int = 0
    entries: list = None

    def __post_init__(self):
        if self.entries is None:
            self.entries = []

    def append(self, operator_version: str, theta_raw: Any, theta_cert: Any,
cert: Certificate,
               inputs: Any, outputs: Any):
        prev_hash = self.entries[-1]["entry_hash"] if self.entries else "0" * 64
        entry = {
            "seq": len(self.entries),
            "prev_hash": prev_hash,
            "registry_version": self.registry_version,
            "operator_version": operator_version,
            "determinism": self.determinism,
            "seed": self.seed,
            "theta_raw_hash": sha256_json(theta_raw),



                                        15
            "theta_cert_hash": sha256_json(theta_cert),
            "certificate": {
                "certificate_id": cert.certificate_id,
                "level": cert.level,
                "norm_id": cert.norm_id,
                "domain_id": cert.domain_id,
                "lipschitz_upper": cert.lipschitz_upper,
                "delta": cert.delta,
                "status": cert.status,
                "artifact": cert.artifact,
                "created_at": cert.created_at,
            },
            "inputs_hash": sha256_json(inputs),
            "outputs_hash": sha256_json(outputs),
            "timestamp": now_iso(),
        }
        entry_hash = sha256_json(entry)
        entry["entry_hash"] = entry_hash
        self.entries.append(entry)



# -----------------------------
# Verifier (independent recomputation)
# -----------------------------

def verify_certificate(phi: Map, theta_cert: Any, cert: Certificate, domain:
Domain) -> bool:
    # Recompute bound and check it matches certificate claims (within
tolerance).
    b, _ = phi.lipschitz_upper(theta_cert, domain)
    if b is None:
        return False
    # Allow small floating tolerance
    return (b <= cert.lipschitz_upper + 1e-9) and (cert.lipschitz_upper <= 1.0 -
cert.delta + 1e-9)



# -----------------------------
# Example run
# -----------------------------

def demo():
    np.random.seed(0)
    domain = BallDomain(domain_id="ball:l2:R=10", norm_id="l2", radius=10.0)

    # Create a raw A that may be non-contractive
    A = np.array([[1.2, 0.0], [0.1, 0.9]], dtype=np.float64)
    phi = LinearMap()



                                         16
       theta_raw = {"A": A}

       res = certify(phi, theta_raw, domain, delta=0.05, clamp=BallProjectClamp())
       print("CERT:", res.status, res.certificate.lipschitz_upper)


       if res.status != "ACCEPT":
           return

       # Dynamics with forcing
       T = np.array([1.0, 0.0], dtype=np.float64)
       F_base = np.array([0.1, 0.0], dtype=np.float64)
       c = res.certificate.lipschitz_upper

       log = AuditLog(registry_version="v0", determinism="best_effort", seed=0)

       traj = [T.copy()]
       for t in range(50):
           forcing = 0.05 * np.sin(2 * np.pi * t / 10.0)
           F_t = F_base + np.array([forcing, 0.0])
           T_next = phi.apply(T, res.theta_cert) + F_t
           traj.append(T_next.copy())

          log.append(phi.operator_version, theta_raw, res.theta_cert,
  res.certificate,
                     inputs={"t": t, "T": T.tolist(), "F": F_t.tolist()},
                     outputs={"T_next": T_next.tolist()})

             T = T_next

       ok = verify_certificate(phi, res.theta_cert, res.certificate, domain)
       print("VERIFIED:", ok)
       print("AUDIT last hash:", log.entries[-1]["entry_hash"])



  if __name__ == "__main__":
      demo()




5. Minimal “structured budget network” (optional, DAG-only)
       This is an extension module. It must include a DAG witness; cycles are rejected.


Idea: represent budgets as a DAG where each edge contributes an additive Lipschitz budget; fold budgets
in topological order.


Artifact sketch:




                                                    17
 {
     "kind": "SBN_DAG",
     "norm_id": "l2",
     "domain_id": "ball:l2:R=10",
     "nodes": ["K", "T", "C"],
     "edges": [
       {"from": "K", "to": "OUT", "lip": 0.6},
       {"from": "T", "to": "OUT", "lip": 0.2, "weight": 1.0},
       {"from": "C", "to": "OUT", "lip": 0.1, "weight": 1.0}
     ],
     "topo_order": ["K", "T", "C", "OUT"],
     "fold": {"total_bound": 0.9}
 }




6. External references (relevant, stable)

Core analysis / fixed points

     • Banach Fixed-Point Theorem (contraction mappings) — standard in functional analysis texts.
     • e.g., Rudin, Functional Analysis; Kreyszig, Introductory Functional Analysis with Applications.

Input-to-state stability style bounds

     • Discrete-time ISS/BIBS bounds — standard in systems/control texts.
     • e.g., Khalil, Nonlinear Systems (ISS concepts).

Nonexpansive projections

     • Metric projection onto closed convex sets is nonexpansive in Hilbert spaces.
     • Standard convex analysis references: Bauschke & Combettes, Convex Analysis and Monotone Operator
       Theory.

Lipschitz bounds for linear maps

     • Induced operator norms and submultiplicativity (matrix analysis).
     • Horn & Johnson, Matrix Analysis.

Verified numerics (for extensions)

     • Interval arithmetic / verified eigenvalue bounds (for Hermitian-gap plug-ins).
     • Moore, Interval Analysis; Higham, Accuracy and Stability of Numerical Algorithms.

Cryptographic audit logs

     • Hash chaining / Merkle trees.
     • Merkle, “Protocols for Public Key Cryptosystems” (foundational Merkle tree idea).




                                                      18
7. Notes for implementers
     • Always report acceptance rate vs performance (prevents “win by rejecting”).
     • Always publish the domain definition used for Lipschitz claims.
     • Keep forcing strictly in diagnostics; do not fold it into certification.
     • Treat GPU nondeterminism as “best_effort” unless you can guarantee deterministic kernels.



Citizen Gardens © 2025 CC-NC-ND 4.0




                                                   19
