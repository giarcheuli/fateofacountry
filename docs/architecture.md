# Country Monitoring System: MVP Architecture

**Status:** Local-first architecture approved; provider and framework choices open.  
**Last updated:** 2026-11-26

## Data path

1. A scheduled Python worker runs on the maintainer's computer approximately every 30 minutes and collects a small number of Georgian sources (RSS, official pages, or manually supplied URLs).
2. The worker deduplicates material and uses a local open-weight model through Ollama to propose structured claims, dates, entities, and categories.
3. Candidate records, source metadata, evidence links, review state, and research-run history are stored in local SQLite. Human review and approval gate publication.
4. Approval creates a publication outbox item in the same local transaction. A publisher process synchronizes approved versions incrementally through an authenticated API to cloud PostgreSQL. Failed deliveries are retained and retried idempotently.
5. A public web frontend reads published records from the cloud API. It never connects directly to the local SQLite database, so the public site remains available while the local computer is offline.

## Claim lifecycle

Source snapshot → candidate claim → evidence and uncertainty → human review → approval/rejection → publication outbox → cloud publication → public display → new version or visible retraction when facts change.

A claim has a stable ID. Each version has a version number and its own content, evidence, and category links. Do not silently overwrite published versions. A retraction indicates that a finding should no longer be relied on; deletion is reserved for separate privacy, legal, or retention needs.

## Current data model

The SQLite v0.1 migration provides eight tables: `categories`, `sources`, `claims`, `claim_versions`, `evidence`, `claim_categories`, `publication_outbox`, and `research_runs`. IDs are UUID strings. Foreign keys are enabled by the migration runner. Approval requires evidence and category links and enqueues publication atomically. A partial unique index prevents overlapping active research runs.

See `db/migrations/001_initial.sql`, `db/migrate.py`, and `docs/publication-sync.md` for implemented schema and proposed API behavior.

## Implementation status

- **Implemented in repository:** SQLite migration, migration runner, publication synchronization contract, and schema tests on `feature/database-schema-v0.1`.
- **Prototype evidence:** Drive contains a sample SQLite database with one manually captured Geostat CPI candidate and no publication queue entry; it is a review-ready example, not an automated ingestion pipeline or public publication.
- **Not yet implemented:** scheduled source collection, Ollama extraction, reviewer UI, cloud API/PostgreSQL, synchronization worker, and public frontend.

## Open architecture choices

Model, web frameworks, cloud/PostgreSQL host, credential provisioning, scheduler mechanism, and production hosting remain undecided. Do not infer reuse of another project's cloud resources.
