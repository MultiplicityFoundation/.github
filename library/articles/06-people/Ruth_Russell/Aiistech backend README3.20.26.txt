Aiistech backend README implementation

The README has been fully rewritten and pushed. Here's what changed:

Segments 1–6 (existing code — now documented):

Segment 1 — Site scaffolding: GET /sites, GET /sites/{site_id}
Segment 2 — Events: POST/GET /events, GET /events/{filename}
Segment 3 — Audit trail: automatic audit middleware behavior, audit entry schema, GET /audit, GET /audit/{filename}
Segment 4 — Artifacts: POST/GET /artifacts, GET/DELETE /artifacts/{filename}
Segment 5 — Config: per-site config file format, GET /sites/{site_id}/config
Segment 6 — Observability: GET /healthz, /healthz/live, /healthz/ready, /sites/{site_id}/healthz, /metrics with expvar counter table
Segments 7–10 (roadmap):

Segment 7 — Embedded database persistence (bbolt/SQLite)
Segment 8 — API-key / HMAC authentication
Segment 9 — Pagination (?limit= / ?cursor=) on list endpoints
Segment 10 — Dockerfile + GitHub Actions CI/CD
Also added: a Table of Contents, the AIISTECH_LOG_LEVEL env var (was missing), corrected project structure, site registry rules, and per-site config format with example YAML.
===============================================================================
==============================================================

The project has completed all 10 planned segments. The README roadmap currently states: "There are no further planned segments at this time."

Here's a brief summary of where the project stands and what a natural next phase would look like:

What's been built (Segments 1–10)
The backend is a fully operational, multi-site Go HTTP server with:

Site scaffolding, events, artifacts, and audit trail verticals
Persistent bbolt storage, structured logging/healthcheck, per-site API-key auth, cursor-based pagination
A production Dockerfile (distroless) and GitHub Actions CI pipeline
Natural next phase candidates
Segment 11 — Search / Filtering — Add query-parameter filtering on list endpoints (e.g. ?event=deploy, date ranges), which is the most obvious missing API capability now that pagination exists.

Segment 12 — Event / Webhook Notifications — Push outbound webhooks or SSE streams when events are written, turning the server from a passive store into an active notifier.

Segment 13 — OpenAPI / Contract Generation — Auto-generate an OpenAPI 3.x spec from the existing routes, enabling client SDK generation and API documentation.

Segment 14 — Multi-tenancy & RBAC — Extend the auth model beyond a single API key to support roles (read-only vs. write) or OAuth2/JWT tokens.

Segment 15 — Kubernetes / Helm — Add a helm/ chart and a docker-compose.yml to complement the existing Dockerfile and make deployment straightforward.