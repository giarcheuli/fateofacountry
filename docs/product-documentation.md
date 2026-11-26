# Product and software documentation convention

## Two persistent homes

Maintain product and software documentation in both this GitHub repository and the matching Google Drive project folder. GitHub is the version-controlled, coding-tool-accessible home for implementation-facing material. Google Drive remains the project knowledge and coordination home. Keep both current after meaningful decisions or artifact changes; link to the other copy where practical. A coding assistant should be able to understand the current approved solution from this repository without needing Drive access.

## What belongs in GitHub

- Vision, goals, users, and product principles: `docs/vision.md`
- Scope, non-goals, user needs, and acceptance criteria: `docs/scope.md`
- Functional and non-functional requirements: `docs/requirements.md`
- Architecture and interfaces: `docs/architecture.md` and focused contracts under `docs/`
- Approved decisions: `docs/decisions/NNNN-short-title.md` (one decision per file, including context, decision, consequences, date, and status)
- Current implementation state and next work: repository README and issue tracker
- Operational setup and contributor instructions: repository docs and `AGENTS.md`

Create only the documents that are useful for the current project stage. Do not invent requirements or mark proposals as approved.

## Change and consistency rules

1. Label material as **Proposed**, **Approved**, **Implemented**, or **Superseded**; include a date for decisions and distinguish implementation from intent.
2. When a product or technical decision changes, update the relevant GitHub document in the same change as the implementation when possible. Record material decisions in a focused decision note and link the associated issue, PR, commit, or artifact.
3. Update the corresponding Google Drive project knowledge after meaningful work, keeping a concise current summary and links to the GitHub source files and history.
4. Preserve useful decision history. Revise current requirements when needed, mark replaced decisions **Superseded**, and link their replacement rather than silently deleting the rationale.
5. Before editing either copy, inspect the existing content. Avoid contradictory duplicate versions; GitHub files are the detailed, versioned reference for coding work, while Drive is the persistent project overview and cross-project record.
6. When delivering work, state which documents changed and whether implementation and tests are complete.

## Current project

The project is the Georgia-first Country Monitoring System (repository name currently `fateofacountry`). These conventions apply to new product and technical work in this repository.
