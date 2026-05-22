---
slug: qahes-engineering-grade-roadmap-v1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/QAHES Engineering-grade roadmap v1.md
  last_synced: '2026-03-20T17:17:21.541835Z'
---

Below is a comprehensive, engineering-grade roadmap to take the Quantum-Assisted Hybrid
Encryption System (v1.0.1) from spec → reference implementation → interoperable products
→ production operations → future versions.




0) Program setup and governance
Deliverables

   ●​ Product requirements + target deployment profiles (datacenter link, metro fiber,
      satellite/FSO, lab demo)
   ●​ Threat model + security requirements traceability to spec MUSTs / tests 1–6
   ●​ Repository structure + CI policy + release process (semantic versions, signed releases)
   ●​ Cryptography policy: approved libraries, constant-time requirements, secure memory,
      key zeroization

Acceptance

   ●​ Every normative requirement maps to a test, a code module, and an owner.
   ●​ Reproducible builds + SBOM + dependency pinning.




1) Architecture and protocol implementation plan
1.1 Control plane vs data plane split

Control plane

   ●​ Bootstrap: ML-DSA cert validation + ML-KEM exchange + derive K_auth
   ●​ Per-sender transcript chains → context_hash
   ●​ Session state machine + strict per-sender message_sequence validation (bootstrap
      and secured)

Data plane

   ●​ Directional AEAD keys: K_enc_A2B, K_enc_B2A
   ●​ Deterministic nonce prefix derivation (v1.0.1)
   ●​ Strict per-direction seq64 replay protection

Deliverables
   ●​ State machine diagram + error/abort rules (what aborts session vs drop/log)
   ●​ Exact wire encoder/decoder library (big-endian, length checks, canonical bytes)
   ●​ Shared “transcript API” used by all message handlers

Acceptance

   ●​ Unit tests prove identical byte encoding across languages.




2) Build the reference implementation (v1.0.1 core)
2.1 Core modules

   ●​ Wire codec: BOOTSTRAP_MESSAGE + CLASSICAL_MESSAGE, strict bounds, no
      struct packing
   ●​ Sequence validation: per sender expected_next_sequence[sender]
   ●​   Transcript hash chains: per sender + role labels (8 bytes), final context_hash
   ●​   HKDF/HMAC: exact salt rule + exact HMAC input bytes (wire bytes)
   ●​   Directional AEAD: keys + deterministic prefix32 + per-direction seq64
   ●​   Replay persistence: atomic storage, corruption handling, restore behavior

2.2 Test suite automation (normative)

   ●​ Implement Tests 1–6 exactly (including your debug anchors)
   ●​ Provide a “known-answer test (KAT)” runner that prints all intermediate values:
         ○​ SESSION_ID, H_A0/H_B0, H_A1/H_B1, H_A2, context_hash
         ○​ HMAC input bytes + tag
         ○​ HKDF PRK + both directional keys
         ○​ prefix32s

Acceptance

   ●​ make test / python -m tests produces a single pass/fail summary and emits
      anchors on failure.




3) Cross-language ports + interoperability bakeoff
3.1 First ports (pick two)
  ●​ Go (service-friendly) and Rust (memory safety / crypto hygiene), or C++ for
     embedded/HSM integration.

3.2 Interop plan

  ●​ Golden test vectors repository (immutable tags)
  ●​ Matrix testing: A↔B across versions and platforms
  ●​ “Fuzz the codec” + “fault injection” for sequence violations, length corruption, replay, and
     partial frames

Acceptance

  ●​ Byte-exact agreement on Tests 1–6 across all implementations.
  ●​ Deterministic interop transcript equality across mixed-language peers.




4) Cryptographic hardening and implementation security
4.1 Side-channel & memory safety

  ●​ Constant-time checks for HMAC comparisons, ML-KEM/ML-DSA operations
  ●​ Key zeroization strategy (best-effort in managed runtimes; strict in Rust/C)
  ●​ Secure logging policy (no keying material, no raw payload dumps in prod)

4.2 Audit readiness

  ●​ Threat model review against:
        ○​ reflection risks (enable optional sender-label prefix in HMAC via negotiated flag)
        ○​ rollback/version negotiation handling
        ○​ transcript-binding completeness (every authenticated message updates chains)

Acceptance

  ●​ Security review checklist completed + static analysis + dependency auditing + fuzzing
     targets in CI.




5) QKD integration workstream (hardware + protocol
glue)
5.1 “QKD adapter” layer
   ●​ Abstract interface: basis exchange, sifting, error correction, privacy amplification
      (Toeplitz), finite-key parameters
   ●​ Plug-in backends:
         ○​ simulator backend (CI deterministic)
         ○​ vendor device backend (ETSI API integration if applicable)

5.2 Key lifecycle

   ●​ QKD key pool management: buffering, rate limiting, minimum key thresholds
   ●​ Key confirmation step tied to context_hash

Acceptance

   ●​ End-to-end run with simulator produces stable session keys and can encrypt/decrypt
      bidirectionally.




6) Operationalization for production
6.1 Observability

   ●​ Metrics: QBER, reconciliation success rate, key pool levels, sequence violations, replay
      drops, rekeys
   ●​ Tracing: session_id, role, direction, message type (no sensitive payloads)
   ●​ Alerts: persistent storage failures, counter nearing limits, repeated abort reasons

6.2 Deployment patterns

   ●​ Library mode (embedded in apps)
   ●​ Sidecar / daemon mode (local agent provides encryption service)
   ●​ Gateway mode (link encryption between sites)

Acceptance

   ●​ Runbooks for: restart recovery, state corruption, rekey triggers, incident response.




7) Compliance, certification, and release engineering
7.1 Conformance tooling

   ●​ “Compliance bundle” export: test logs + hashes + version info + build provenance
   ●​ Optional hosted interoperability service (your compliance endpoint concept)

7.2 Crypto compliance

   ●​ Document dependency posture (FIPS modules where required)
   ●​ PQ certificates profile strategy (experimental OIDs until standardized)

Acceptance

   ●​ Reproducible artifacts + signed tags + documented upgrade policy (v1.0 → v1.0.1).




8) Performance and scalability roadmap
8.1 Throughput optimization

   ●​ Zero-copy parsing, bounded allocations
   ●​ Batch AEAD processing, pipelined handshake steps
   ●​ Hardware acceleration hooks (AES-NI, ARMv8 crypto, HSM offload)

8.2 Load and soak testing

   ●​ Long-run seq64 monotonicity under restart/failover
   ●​ Fault injection: dropped frames, duplicated frames, storage I/O failures

Acceptance

   ●​ Defined SLOs for handshake rate, latency, and sustained encrypted throughput.




9) v2.0 evolution plan (based on your “planned” items)
Protocol features

   ●​ Sliding-window replay protection (reordering-tolerant networks)
   ●​ Fragmentation/reassembly for >64KB payloads
   ●​ Extended negotiation framework (capability flags: reflection-hardening HMAC prefix,
      window size, fragmentation)

Security engineering

   ●​ Formal verification targets (codec + state machine)
   ●​ Expanded test vectors (property tests, negative tests, transcript mismatch tests)




Suggested workstreams and owners (practical
structuring)
   1.​ Spec→Code Core: codec/state machine/transcript/HMAC/HKDF
   2.​ Interop & Test Infra: vector repo, KAT runner, CI, fuzzing
   3.​ Crypto Hardening: constant-time, memory, audits
   4.​ QKD Adapter: simulator + vendor integration
   5.​ Ops & Deployment: persistence, metrics, runbooks, packaging
   6.​ Compliance: conformance artifacts, certification process




“Definition of done” for v1.0.1 production readiness
   ●​ Pass Tests 1–6 byte-exact, plus negative tests (bad length, bad sequence, bad HMAC,
      replay)
   ●​ Two independent implementations interoperate end-to-end with deterministic session
      establishment
   ●​ Persistent replay state survives restart safely (atomic updates, corruption handling)
   ●​ Observability + runbooks exist for abort/rekey/storage failures
   ●​ Security review completed (reflection, downgrade, transcript-binding completeness)



If you want, I can also format this into:

   ●​ a milestone tracker (deliverables + acceptance criteria per phase), or
   ●​ a work breakdown structure suitable for Jira/Linear (epics → stories), or
   ●​ an architecture decision record (ADR) pack capturing all v1.0.1 “must not be
      ambiguous” decisions.
