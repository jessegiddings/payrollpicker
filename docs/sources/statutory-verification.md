# Statutory verification log — Builders Lien Act (BC)

**Status: NOT VERIFIED. Publication blocked on items below.**

Attempted 2026-08-12 from the build environment:

| Source | Result |
|---|---|
| `bclaws.gov.bc.ca` (official consolidated statutes) | **EGRESS BLOCKED** by the build sandbox's network policy |
| `canlii.org` | **EGRESS BLOCKED** |

Per REBUILD SPEC v4 §4, every number that could not be read in the statute this
session is rendered as `[VERIFY: …]` in the shipped pages rather than published
from secondary sources or memory. The affected claims:

| Claim | Where used | Status |
|---|---|---|
| Holdback percentage (10%) | Holdback service page H1 and body; home; insight post | Stated in the rebuild spec itself; **still confirm the exact statutory wording** (percentage and what it is calculated on — the spec of payment vs value of work matters) |
| Holdback period (days) and its trigger | Holdback page §1–2; insight post | **[VERIFY]** — spec notes secondary sources disagree (45 vs 55 days) and on the trigger event |
| Lien filing deadline (days) | Holdback page; insight post | **[VERIFY]** |
| Holdback trust account requirement and its contract-value threshold | Holdback page §4 | **[VERIFY]** — threshold amount not published |
| Definition of "owner" capturing a homeowner contracting with a GC | Holdback page §1 | **[VERIFY]** exact definition wording |
| Owner liability where holdback not retained (cap / personal exposure) | Holdback page §2 | **[VERIFY]** — describe qualitatively only until read in the statute |

## What must happen before these pages go public

1. Read the current consolidated Builders Lien Act, SBC 1997, c. 45 at
   bclaws.gov.bc.ca (any environment with normal web access — a Cowork session
   can). Record section numbers and exact wording here for each row above.
2. Replace every `[VERIFY: …]` token in:
   - `src/content/services/holdback-and-draw-compliance.md`
   - `src/content/insights/the-ten-percent-you-must-withhold.md`
3. **BC construction lawyer review of both pages** (rebuild spec §9.2) — required
   even after the statute is read. Verification by a non-lawyer is a floor, not
   the gate.

Until 1–3 complete, the site must stay on the private `*.vercel.app` URL (it is
already held there by the other launch gates).
