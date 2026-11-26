# Publication synchronization v0.1

The local reviewer changes a pending revision to approved in the same transaction as their final edits. SQLite queues that revision atomically. Every worker connection must enable PRAGMA foreign_keys=ON. Generate stable UUIDs for claims, source snapshots and runs. A claim version is identified by (claim UUID, positive version number). Capture event dates in events. Cite a source locator for each evidence link. Categories belong to each revision. Treat category IDs as stable and resolve their labels separately.

## Write endpoint (contract, awaiting implementation)

PUT /v1/claims/{claim_uuid}/versions/{version} over HTTPS with a publisher credential. Only the local publisher holds that credential. Public reads are anonymous. Use a JSON object with action (publish or retract), statement (the reason for a retraction), uncertainty, entities and events arrays, category_ids (UUID array) and evidence (array). Each evidence item includes stance, locator and a source object with id, url, title, publisher, author, published_at, retrieved_at and content_sha256. Optional source metadata may be null. Use ISO 8601 UTC timestamps on the wire. Keep reviewer identities, credentials and raw source bodies local.

The cloud validates the envelope, UUIDs and evidence. In one PostgreSQL transaction, serialize writes per claim, insert an immutable revision and advance the public head. The path is the idempotency key. New revision: 201. Same revision and identical normalized content: 200, including after a lost response. Different content at the same key or a previously unseen older revision: 409. A first retraction is invalid. Gaps are valid because rejected drafts stay local. Sort unordered evidence and category lists deterministically before comparing payloads. Return the claim ID and version on success.

Deliver the lowest outstanding version per claim first. Mark delivered only after 200/201 with the matching key. Retry network failures, 429 and 5xx with bounded exponential backoff and jitter, respecting Retry-After. Stop and surface 400/401/403/409/422 for operator resolution. One blocked claim must not stall others.

GET /v1/claims/{claim_uuid} returns the latest approved public version and evidence or 404 for an unknown claim. A retraction remains visible with a retracted status, reason and version. Historical versions remain addressable through GET /v1/claims/{claim_uuid}/versions/{version}. Exceptional privacy deletion requires coordinated removal from local and cloud stores.

## Local execution

Run python db/migrate.py country.sqlite twice to verify repeatability. Run python -m unittest discover -s tests. Each scheduled worker must commit its running row before ingestion. The unique active-run constraint prevents overlap. After a crash confirm the previous process is dead before marking its run failed and restarting.
