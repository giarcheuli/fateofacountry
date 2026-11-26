# Country Monitoring System: MVP Requirements

**Status:** Approved direction and acceptance criteria; unresolved implementation choices are marked open.  
**Last updated:** 2026-11-26

## Users and operating model

- Initial country: Georgia.
- Maintainer/reviewer: project volunteer who checks candidate claims and decides whether to approve, revise, or reject them.
- Public reader: can inspect published claims, their status, evidence, and version history.
- The project is open-source, noncommercial, and community-maintained.

## Functional requirements

1. **Research directions:** support configurable categories, initially Internal politics, Foreign politics, Economics, Social and public life, Human rights, Science and arts, and Infrastructure. A claim version may have multiple categories.
2. **Source records:** retain source URL, title, publisher/author when available, publication and retrieval timestamps, and a content hash. Preserve evidence locators such as paragraph references.
3. **Candidate extraction:** capture a candidate statement, event/date information, entities, categories, uncertainty, and links to supporting or contradicting sources. Structured entities and events may be JSON in the MVP.
4. **Review gate:** allow a human to approve, revise, or reject candidates. Model extraction is not independent verification. Unreviewed records must not be publicly published.
5. **Version history:** assign a stable claim ID and immutable sequential versions. New evidence leads to a new version and review. A retraction remains visible as a status and reason; it is not deletion. Handle legally or privacy-required deletion separately.
6. **Publication queue:** enqueue approved versions atomically; retry failed synchronization idempotently using stable IDs and versions.
7. **Public access:** public web clients read published data through a cloud API, never directly from a local database. The public site remains available when the local research computer is offline.
8. **Research worker:** schedule collection approximately every 30 minutes; prevent overlapping runs. Start with a small set of roughly 3–5 reputable Georgian sources, using RSS, official pages, or manually supplied URLs. Deduplicate source material.

## Non-functional requirements

- Open-source-compatible and low-cost components are preferred.
- Preserve source traceability, contradictions, uncertainty, and publication history.
- Keep publisher credentials out of public clients and source material that should not be published out of the public API.
- Use stable identifiers, referential integrity, and idempotent synchronization.
- Label the public prototype Experimental and communicate limitations.

## MVP acceptance scenario

Using a real Georgian source, demonstrate: collect source → extract candidate claim → save locally → human review and approval → synchronize and publish → display claim with evidence → create a reviewed update version → retract and show retraction history.

## Open choices

Exact Ollama model; initial vetted source roster; backend and frontend frameworks; PostgreSQL host; API authentication; reviewer UI; source licensing/retention rules; and procedures for corrections or unavailable sources.
