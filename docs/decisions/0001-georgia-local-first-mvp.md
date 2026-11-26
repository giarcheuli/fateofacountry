# Decision 0001: Georgia-first local-first MVP

**Status:** Approved  
**Date:** 2026-11-26  
**Source:** HND-0001 and project decisions recorded in Google Drive Project Knowledge

## Context

The project needs an affordable, open-source-compatible volunteer workflow that can preserve evidence and keep a public information site online even when the maintainer's personal computer is offline.

## Decision

Build the initial MVP for Georgia. Run scheduled Python research locally, use a local open-weight model through Ollama for candidate extraction, and store research and review records in SQLite. Require human review before publication. Synchronize approved versions one-way through an authenticated API to cloud PostgreSQL; serve the public frontend from the cloud API, never from the local database. Queue and retry failed publication events idempotently. Start with approximately 3–5 vetted Georgian sources and prevent overlapping worker runs. Use seven broad configurable research directions: Internal politics, Foreign politics, Economics, Social and public life, Human rights, Science and arts, and Infrastructure.

Represent the independently reviewable item as a versioned claim with stable identity, version-specific evidence and categories, and visible uncertainty. Retractions remain visible; deletion is separate. An LLM extraction is not independent verification.

## Consequences

The system can keep its public site available while local research is offline and can preserve review/history. The first release needs both local worker/reviewer capability and a cloud publishing/read path. Exact model, implementation frameworks, provider, authentication mechanism, and source roster remain open decisions.

## Implementation status

The SQLite v0.1 schema, migration runner, tests, and proposed synchronization contract are committed on `feature/database-schema-v0.1`. Source automation, cloud API, cloud database, reviewer UI, and public frontend are not yet implemented. See [architecture](../architecture.md), [requirements](../requirements.md), and [publication sync contract](../publication-sync.md).
