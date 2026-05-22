---
slug: prime-layered-recursion-tyler-ace-integration-spec-v0
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "02-implementations/q-calculator/Prime\u2011layered Recursion \u2014 Tyler_ace\
    \ Integration (spec V0.md"
  last_synced: '2026-03-20T17:17:15.352713Z'
---

Prime‑Layered Recursion — Tyler/ACE Integration
(Spec v0.1)
Purpose
Translate Tyler’s “layered prime recursion” notes into a concrete, implementable addendum to the ΛProof ×
Q‑ARI/Q‑Calculator architecture, including runtime model, crypto, logging anchors, and schemas. This doc
is implementation‑ready and procurement‑length; legal/IP terms are out‑of‑scope.




1) Executive Summary
     • Replace any single linear timeline with many prime‑keyed timelines (per‑prime append‑only logs
       + root‑of‑roots).
     • Treat each prime node as a dormant CPU that activates on demand; cross‑node work is a DAG of
       lawful sub‑requests.
     • “Truth” is a verifiable handshake: lawfulness token signature + (optional) ZK proof + inclusion in
       anchored Merkle roots.
     • Public transparency publishes commitments, not payloads; salts + envelope encryption prevent
       preimage and linkage.




2) Model — Prime‑Layered Runtime (Many Timelines)

2.1 Names & Timelines

     • Node ID: N = ⟨prime p : /scope/subscope/...⟩
     • Per‑prime ledger: append‑only local log for node p .
     • Daily root: per‑prime Merkle root → aggregated root‑of‑roots (day), externally anchored.

2.2 Activation & Concurrency

     • CPU per node (worker shard): nodes are off by default; activate when targeted and {C, η, q}
      tuple verifies.
     • Cross‑node calls: represented as a DAG; each edge carries its own lawfulness tuple and produces its
       own trace atom.
     • Budget composition: if a transition touches primes {p1..pk} , enforce Ση_i ≤ η_max and track
       g(η) subadditivity.

2.3 Lawfulness Loop (per node)

1) Intake typed proposal u_t → compute FP‑independent certificate C_t (may include prime‑signature/
multiplicity).
2) Apply policy projector P : commute with Ξ_p or stay within budget η (margin degrades via g(η) ).
3) Compute contraction witness q ; if needed, run projection Π (weighted‑ℓ1/ℓ2/ℓ∞/Bregman), emit




                                                     1
dual/KKT.
4) Scheduler admits only if q′ ≤ 1−ε and η ≤ η_max .
5) Assemble trace atom, verify, actuate Ξ_p , else silence and append a negative atom.




3) Cryptography — Keys, Derivation, AEAD

3.1 Key Hierarchy & Roles

     • KEK_root (offline, HSM) → derives per‑prime keys.
     • KEK_prime[p] → derives per‑node daily DEK_node[p,x].
     • Sign keys (TPM/HSM) → sign lawfulness tokens & atom acknowledgments.
     • ZK verification keys (public) → verify optional SNARK/STARK proofs.

3.2 HKDF Derivation (labels fixed)


  KEK_prime[p]     = HKDF( IKM = KEK_root,
                           salt = "ΛProof.QARI.hkdf.v1",
                           info = "prime" || be_u64(p) || policy_version )

  DEK_node[p,x] = HKDF( IKM = KEK_prime[p],
                             salt = "ΛProof.QARI.hkdf.v1",
                             info = "node" || H(path_x) || be_u64(epoch_day) )


Notes:
- H = SHA‑256; be_u64 = big‑endian 64‑bit.
- Rotate policy_version on CSL/invariant changes.
- epoch_day = UTC YYYYMMDD integer.


3.3 AEAD Parameters (envelope encryption)

     • Algorithms: AES‑256‑GCM (HW AES) or ChaCha20‑Poly1305.
     • Nonce: 96‑bit random or counter‑based per DEK; never reuse.
     • AAD: stable IDs {prime_id, node_path_hash, atom_id} .
     • Wrap: Store payloads with per‑day DEKs; DEKs wrapped by KEK_prime in HSM.
     • Do not use RSA per digit/field; use AEAD with derived keys.

3.4 Lawfulness Token (anti‑replay, prime‑aware)


  token_payload = req_hash || cert_hash || prime_id || monotonic_counter || ts ||
  audience
  signature     = Sign_TPM( token_payload )


- Verification: public key; require counter monotonicity & clock skew bounds; bind prime_id .




                                                    2
3.5 Optional ZK (bounds without disclosure)

      • Circuits attest: q ≤ 1−ε and ‖ΞPu − PΞu‖ ≤ η .
      • Publish only proof and verification key; never witnesses.




4) DNS‑TXT Anchor — Formats & Rotation

4.1 Per‑Prime Anchor (daily)


  _eiu.<p>.<YYYYMMDD>.yourdomain           TXT   "ts=YYYY-MM-DD root=<BASE64_MERKLE_ROOT>
  v=1"


- One record per p per day. Use DNSSEC if available.


4.2 Root‑of‑Roots Anchor (daily)


  _eiu.root.<YYYYMMDD>.yourdomain TXT            "ts=YYYY-MM-DD root=<BASE64_ROOT_OF_ROOTS>
  v=1"


4.3 Verifier Inputs

      • Export leaf commitments for day+prime, salts (under audit NDA), and linkage file (prime → leaves).
      • Verifier recomputes per‑prime root and compares to DNS; repeats for root‑of‑roots.




5) Trace Atom — Canonical Schema & Commitments

5.1 Canonical JSON (fields)


  {
    "atom_id": "uuid",
    "prime_id": "p-00000023",
    "node_path": "/scope/subscope",
    "ts": "2025-12-16T11:20:03Z",
    "decision_id": "ux-2025-12-16-001",
    "lawfulness_tuple": {"C_hash": "…", "eta": 0.07, "q": 0.86, "q_prime": 0.81},
    "projection": {"used": true, "metric": "weighted-l1", "dual_kkt": "…"},
    "policy": {"predicates": ["privacy:consent_ok","no_dark_patterns"], "g_eta":
  "affine@v1"},
    "actuation": {"operator": "Xi_p@1.3.0", "result": "allow"},
    "build": {"service": "ux-svc@1.4.2", "config": "cfg-2a9"},




                                                       3
      "scope": "ui.adapt.pricing.mobile"
  }


5.2 Deterministic Serialization

      • Canonical JSON: UTF‑8, sorted keys, no whitespace beyond single commas/colons.
      • Binary option: Canonical CBOR (CTAP2 profile).
      • Compute commitments before encryption/signature.

5.3 Commitment & Salting


  leaf_commitment = H( salt_128 || canonical(atom) )


- salt_128 : 16 random bytes (stored encrypted with the atom).
- Store leaf, build Merkle tree; keep salt_128 out of public anchors.


5.4 Atom Sign/Ack (optional)


  ack = Sign_TPM( H(canonical(atom)) || prime_id || ts )


- Ack can be used to non‑repudiably confirm gate authorization.




6) Operational Flows (Happy‑Path)
1) Client sends u_t → node p .
2) Structure checker computes FP‑independent C_t ; projector P applies CSL with budget η .
3) Stability module computes q ; if q > 1−ε run Π → q' .
4) Scheduler checks    q'   and   η ; if pass, assemble atom, compute leaf_commitment, append to
per‑prime log, gate actuates Ξ_p .
5) End of day: compute per‑prime roots; compute root‑of‑roots; publish DNS‑TXT anchors.




7) Privacy & Pseudonymization
      • Domain separation for user IDs: pseudo_id = HMAC(context_key, stable_id) per product/
        region.
      • Keep raw features in a sealed store; atoms carry only hashes/IDs or bucketed values.




                                                     4
8) SLAs, Metrics, and Safety
     • P95 veto decision ≤ 48h; max hold 7d; 100% overrides logged with liability sign‑off.
     • Anchor cadence: daily per prime + root‑of‑roots; log gap rate = 0.
     • Replay: periodic bit‑exact regeneration of C and atom across fp16/bf16/fp32/fp64.




9) Implementation Checklist (cut‑and‑paste)
     • [ ] HKDF labels & parameters implemented exactly as 3.2.
     • [ ] AEAD envelope encryption with per‑day DEKs; KEK in HSM; nonce policy enforced.
     • [ ] Lawfulness token signature verified; counter monotonicity enforced; clock skew bounded.
     • [ ] Canonical JSON/CBOR serializer; commitments salted; Merkle builder.
     • [ ] DNS‑TXT anchors emitted (per‑prime + root‑of‑roots) and verifier script operational.
     • [ ] CI gates reject atoms missing {C_hash, eta, q} or required projection witnesses.
     • [ ] Domain‑separated pseudonyms; sensitive fields redacted or bucketed.
     • [ ] Replay tests across FP formats pass; anchor/audit scripts pass.




10) Open Questions (for ADRs)
     • Target ZK system (transparent vs trusted setup), and which bounds are proven in ZK vs recomputed.
     • Exact form for g(η) (affine vs logistic) per domain.
     • Complexity‑band estimator for cross‑prime DAGs and deadlock policies.

End — Spec v0.1




                                                    5
