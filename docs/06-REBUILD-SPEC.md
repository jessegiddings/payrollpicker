# REBUILD SPEC v4 — Site Repositioning

(Stored verbatim from the partner handoff, 2026-08-12.)

**For Claude Code.** This is a **rebuild of an existing site**, not a new build.
Repo: `jessegiddings/erskine-advisory`, branch `main`. Astro 5 + Tailwind 4,
static, Vercel auto-deploy.

Supersedes BUILD SPEC v3 §1 (positioning) and COPY DRAFT v3 wherever they
conflict. `03-ART-DIRECTION.md` still governs design and is unchanged.

⚠️ **`{{FIRM}}` is unresolved.** The name is still under review (Erskine, Maxwell,
Pender, Booth). Use the token; do not hardcode. Repo name is not the decision.

---

## 1. WHY THIS REBUILD

The site was built on an argument that competitive research has since weakened.

The old home page led with the conflict argument — *your contractor's project
manager works for your contractor, so you can't see where the money goes.* A West
Vancouver competitor now sells **open-book accounting** as a headline service:
detailed financial reports, cost breakdowns showing where every dollar goes, a
client login, and a staff financial controller. Against that, "you can't see the
numbers" simply isn't true anymore.

The replacement argument is narrower, harder, and cannot be copied:

> **Transparency is not verification.** Open books are the builder showing you the
> builder's records. Independent verification is a third party confirming the work
> exists before the money moves. Better bookkeeping never makes a party
> independent of itself.

And the proof case is statutory: under BC's Builders Lien Act an owner must retain
10% of every progress payment, and **a builder cannot discharge that obligation on
the owner's behalf — they are the party being held back from.** No competitor site
mentions it.

**Verification is also a genuine competitive hole.** The closest comparable firm
(Alpine Group, US) lists due diligence, permits, contract procurement, budgeting,
team selection, scheduling, insurance and closeout, estate turnover — and nothing
about payment application review, draw control, liens or holdback. Same for every
other firm surveyed.

---

## 2. THE NEW CORE

### 2.1 The three words

The strongest competitor organises its home page around three repeatable words
(Ease / Confidence / Control). Ours currently offers seven independence
commitments — correct, but nobody can repeat them. Keep the seven on
`/independence`. Put three words above them and on the home page.

**Use: INDEPENDENT · VERIFIED · DOCUMENTED**

| Word | One line beneath it |
|---|---|
| **Independent** | We are paid by you and by no one else on the project. |
| **Verified** | Nothing is approved for payment until someone has confirmed it exists. |
| **Documented** | Every decision, approval and release is written down and yours to keep. |

*Alternates if these are rejected: Independent / Verified / Accountable, or
Reviewed / Verified / Released. Do not use benefit-words (Ease, Peace of Mind,
Confidence) — the competitor owns that register and it undercuts the harder claim.*

### 2.2 The new one-sentence positioning

> {{FIRM}} represents owners on significant residential projects. We review the
> contract before it is signed, verify the work before payments are released, and
> administer the holdback the law requires you to retain.

### 2.3 Ranked argument order (this is the change)

1. **Verification** — nobody gets paid before someone independent confirms the work
2. **The statutory holdback** — the legal proof that a builder cannot do this for you
3. **The conflict** — demoted to supporting material, not the headline
4. **Independence commitments** — the trust layer
5. **Published fees** — the credibility layer

---

## 3. SITEMAP CHANGES

**New nav:** How It Works · Services · Fees · Independence · Who We Are · Contact

| Path | Action | Notes |
|---|---|---|
| `/` | **Rewrite** | New argument order, three words, new H1 |
| `/services/holdback-and-draw-compliance` | **NEW — P0** | Promote from a section to a top-level page. Lead Canadian offering |
| `/compare` | **NEW — P0** | Independent representation vs builder project management vs open-book accounting. Nobody has published an honest version |
| `/the-owners-position` | **Rewrite → `/how-it-works`** | Reframe from "why owners are disadvantaged" to "how verification actually works." Keep the essay, change the spine. Add a 301 redirect |
| `/services/owners-representation` | **Edit** | Add the verification and payment functions to the service list |
| `/services/remote-oversight` | **Edit** | Remove holdback content now living on its own page; cross-link |
| `/independence` | **Edit** | Three words above the seven commitments |
| `/fees` | **Edit** | Add holdback compliance pricing |
| `/who-we-are` | **Edit** | See §5.4 — two changes, both required |
| `/services/project-recovery`, `/services/prefab-and-modular` | Keep | Cross-link to `/compare` |
| `/insights/*` | Keep | Add the two new posts in §6 |
| `/projects`, `/testimonials` | Keep as stubs | noindex, unlinked, excluded from sitemap |

---

## 4. NEW PAGE: `/services/holdback-and-draw-compliance`

⚠️ **Every statutory claim on this page must be verified against the Builders Lien
Act on bclaws.gov.bc.ca before it ships, and the page must be reviewed by a BC
construction lawyer before public launch.** Secondary sources disagree on the
holdback period (45 vs 55 days) and on the trigger. Do not publish a number that
has not been read in the statute. If verification is not possible in this session,
build the page with the numbers replaced by `[VERIFY]` and flag it.

**H1:** The 10% the law requires you to hold back

**Structure:**
1. **What the obligation is.** Owner must retain 10% of every progress payment.
   Statutory, applies whether or not the contract mentions it. A homeowner
   contracting with a GC is an "owner" under the Act.
2. **What it protects you from.** Comply and exposure to downstream lien claimants
   is capped at the holdback pool. Fail to retain and the owner can become
   personally liable for lien claims up to the amount that should have been held.
3. **Why your builder can't do this for you.** Short, plain, and the most important
   paragraph on the site. The holdback exists to protect the owner *from* the
   contracting chain. The party being held back from cannot administer it.
4. **What we do.** Holdback calculation on every draw · trust account setup where
   the contract exceeds the statutory threshold · payment application review
   against work in place · lien period tracking · title search before release ·
   documented release approval.
5. **What we don't do.** We are not lawyers. We manage the obligation
   operationally; interpretation and disputes go to counsel, and we will tell you
   when it's time.
6. **Fee.** Monthly, quoted with the engagement.

**Tone:** flat and factual. The material is alarming enough without adjectives. No
fear-selling.

---

## 5. PAGE REWRITES

### 5.1 `/` — home

**H1:** Nothing gets paid until someone independent confirms it exists.

**Sub:** {{FIRM}} represents owners on significant residential projects. We review
the contract before you sign it, verify the work before money is released, and
administer the holdback the law requires you to retain. Paid by you, and by no one
else on the project.

**Section order — this is the change, follow it exactly:**

1. **Hero** + three words (Independent · Verified · Documented)
2. **"Transparency is not verification."** The central argument. Be explicitly fair:
   open-book accounting is a real improvement and a good builder offering it is
   doing something worth having. It is still the builder's own record of the
   builder's own work. Independence is structural, not a matter of goodwill.
3. **The holdback** — the statutory proof case. Short, links to the new service page.
4. **`RiskLadder`** — keep the existing component, retitle the section to "Where the
   leverage is."
5. **Services** — five cards, holdback compliance first.
6. **"Everyone on your project is paid by someone else"** — the old conflict
   argument, demoted to a supporting section here rather than the opening.
7. **Fees band** — we publish what we charge.
8. **Independence band** — three words plus link.
9. **"We are a new firm"** — keep this section unchanged. It is the best thing on
   the site.
10. **CTA** — project review.

### 5.2 `/compare` — NEW

**H1:** Independent representation, builder project management, and open books

Three-column comparison, scrupulously fair. Rows: who pays them · whose records
you see · who verifies completion · who administers the holdback · what happens in
a dispute · what it costs · when each is the right choice.

**Required:** a closing section titled **"When builder-provided management is
enough."** Genuinely argue it — small scopes, a long-standing builder
relationship, an owner who is on site daily, a fixed-price contract with a
performance bond. This section is what makes the whole page credible, and it is
the reason an architect will forward it.

**Do not name any competitor.** Compare models, never firms.

### 5.3 `/how-it-works` (was `/the-owners-position`)

Keep the essay, change the spine. Old frame: why owners are structurally
disadvantaged. New frame: what verification actually involves, in sequence —
contract, bid comparison, payment application review, change order interrogation,
holdback, lien period, release. Retain the incentive-map section as chapter one.
Add a 301 from the old path.

### 5.4 `/who-we-are` — two required changes

- **Remove the former employer's name** in all three places it appears (here,
  `/independence`, and the prefab service page). Replace with: *five years inside a
  prefab housing company, latterly as Vice President and Partner.* Same credibility,
  no name.
- **The specialists section must not imply a roster that doesn't exist.** Until
  someone is actually retained, the copy is: *we engage independent specialists —
  structural engineering, cost consulting, site inspection — and name them in the
  proposal for your project.* Not "our team includes."

### 5.5 `/services/owners-representation` — service list

The market-standard list is due diligence, permits, contract procurement,
budgeting, team selection, scheduling, insurance and closeout. Ours must contain
all of that **and visibly more.** Add and make prominent:

- Payment application review against work in place
- Independent draw verification and release approval
- Statutory holdback administration
- Change order interrogation and pricing challenge
- Lien period tracking and title search
- Documented decision log

A prospect comparing two service lists side by side should see the difference in
five seconds.

---

## 6. TWO NEW INSIGHT POSTS

Same collection and frontmatter as existing posts.

| Slug | Title | Words | Brief |
|---|---|---|---|
| `transparency-is-not-verification` | Transparency is not verification | 1,300 | The core argument, at length. Open with genuine credit to builders offering open books. Then the structural point. Never name a firm. |
| `the-ten-percent-you-must-withhold` | The 10% you are legally required to withhold | 1,400 | Highest-value piece on the site. Same verification gate as §4. |

---

## 7. WHAT TO KEEP — DO NOT UNDO

- **Art direction in full.** `<Plate>` duotone, Inter Tight 4:1 scale, `Inverse`
  bands, `Stat` components, `RiskLadder`, margin section numbers, once-only motion
  behind `prefers-reduced-motion`.
- **All honesty rails.** No fabricated proof · no guarantees or savings
  percentages · no licensure claims · no project-size floor · no legal advice · never
  imply the firm builds, hires subcontractors or contracts for construction work
  (permitted verbs: advise, review, verify, coordinate, represent, report) · never
  name a builder as a cautionary example · footer line "Photography is illustrative.
  We do not publish client projects."
- **Banned words:** bespoke, curated, seamless, luxury (self-applied), passionate,
  journey, dream home, turnkey, white-glove, elevate, unparalleled, world-class,
  innovative, exclusive, discerning. **Also now banned:** ease, peace of mind,
  stress-free — the competitor's register.
- **Banned as names** (trademark): Advocate, Owner's Advocate, Construction
  Advocate, Construction Advisor.
- **Published fees.** No competitor does this. It is the cheapest credibility we have.
- **The "we are a new firm" section.** Do not soften it.
- **Accessibility:** WCAG 2.2 AA, axe clean, 4.5:1 over plates, text equivalents for
  diagrams, keyboard nav, 320px, CSP in `vercel.json`.

---

## 8. BUILD SEQUENCE

1. Verify the statutory claims (§4). Log to `docs/sources/statutory-verification.md`.
   **If this fails, stop and report before writing the holdback page.**
2. `/services/holdback-and-draw-compliance` — new page, service collection entry.
3. `/` — rewrite to the section order in §5.1.
4. `/compare` — new page.
5. `/the-owners-position` → `/how-it-works`, with 301.
6. Edits: `/services/owners-representation`, `/services/remote-oversight`,
   `/independence`, `/fees`, `/who-we-are`.
7. Two new insight posts.
8. SEO pass — hand-written title and description on every new and changed page;
   `Service` schema on the holdback page; `FAQPage` on `/compare`; update sitemap;
   verify canonicals and the redirect.
9. Audit — axe, Lighthouse (Perf ≥95, A11y 100, SEO 100), keyboard-only, 320px.
10. Push to `main`. **Site stays on the `*.vercel.app` URL** — do not attach a
    public domain until the launch gates clear.

---

## 9. OPEN ITEMS — CANNOT BE RESOLVED IN CODE

| # | Item | Blocks |
|---|---|---|
| 1 | **Final name + domain**, with CIPO / USPTO / BC registry searches | All copy, public launch |
| 2 | **BC construction lawyer review** of the holdback page and its article | Publishing either |
| 3 | **E&O at $5M+ and CGL bound** | Honest capability claims sitewide |
| 4 | **Cost consultant retained and named** | `/who-we-are` credibility at this client level |
| 5 | Confirm holdback compliance pricing | `/fees` |
| 6 | Entity registration, business email, phone | Footer, `/terms`, schema |
| 7 | Formspree form ID | Lead capture (site captures nothing until set) |
| 8 | The 14 photographs and two headshots | Currently SVG placeholders |

---

## 10. SUGGESTED OPENING PROMPT

> Open `docs/06-REBUILD-SPEC.md` in this repo. Start with step 1: verify the
> Builders Lien Act holdback claims against bclaws.gov.bc.ca and log results to
> `docs/sources/statutory-verification.md`. Report what you find before writing the
> holdback page — if the numbers don't check out, stop. Then work steps 2–10 in
> order. Show me the new home page and `/compare` before moving to the SEO pass.
