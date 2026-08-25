# LAUNCH HANDOFF — Erskine Advisory

**Purpose:** the single working document for finishing the site. Take this into a
Claude Cowork session (or hand it to a person) and work top to bottom. Everything
built so far is described at the end so context never has to be reconstructed.

Repo: `jessegiddings/erskine-advisory`, branch `main` · Hosting: Vercel (static
Astro build, auto-deploys on push) · Specs live in the project history:
BUILD SPEC v3 → 01-COPY-DRAFT v3 → 02-COMPETITIVE-TEARDOWN → 03-ART-DIRECTION
(03 supersedes the build spec's §6 design direction).

---

## PART 1 — Work a Cowork session can do now

### 1.1 Source the 14 photographs (the main job)

The site currently runs on generated SVG placeholder plates in `public/plates/`.
Replace them with real photography per the shot list below. The build sandbox that
made the site could not reach stock libraries; a Cowork session with normal web
access can.

**Sources, in order:** Unsplash (`unsplash.com`) → Pexels (`pexels.com`) →
Pixabay. Budget **one paid frame** (Adobe Stock / Stocksy, ~$80–200) for the home
hero if the free options don't deliver — it sets the tone for everything.

**Reject any image containing:** a recognisable person or face · a readable
company logo · a visible address or identifiable private property · a finished
styled interior · a sunset.

**Licence discipline (non-negotiable):** before an image ships, open its
individual photo page, confirm the licence, and save a screenshot of that licence
page into `docs/image-licences/`, named to match the asset (e.g.
`plate-01-rebar.licence.png`). One screenshot per image, no exceptions.

**The shot list:**

| # | Replaces | Placement | Search terms | Selection criteria |
|---|---|---|---|---|
| 1 | `plate-01-rebar` | Home hero | `concrete formwork`, `building under construction detail`, `rebar grid` | Abstract, geometric, no sky, no identifiable building. Must work ~2000px wide with type over the left third. This is the one worth paying for. |
| 2 | *(new — optional)* | Home, conflict section | `construction site meeting drawings table` | Hands and drawings only; crop out faces. Currently the conflict section is a dark type band and works without an image — add only if a frame is genuinely strong. |
| 3 | `plate-03-crane` | Home divider | `tower crane underside`, `crane rigging` | Looking up. Structural, stark. |
| 4 | `plate-04-framing` | Home, new-firm section | `wood framing interior daylight` | Skeletal, honest, unfinished. |
| 5 | `plate-05-linework` | `/the-owners-position` | `architectural blueprint detail`, `technical drawing close up` | Tight crop of linework; doubles as texture. |
| 6 | *(new — optional)* | `/the-owners-position` second texture | same | Only if it earns its place. |
| 7 | `plate-07-rule` | `/fees` | `measuring tape steel`, `calipers` | One object, one shadow, lots of negative space. |
| 8 | `plate-08-scaffold` | `/independence` | `scaffolding pattern`, `structural steel joint` | Repetition and structure. |
| 9 | `plate-09-excavation` | `/how-we-work` | `construction site excavation foundation` | Early-stage. Mud. Reality. |
| 10 | `plate-10-forest` | `/who-we-are` | `pacific northwest coastal forest fog` | Place, not project. |
| 11 | `plate-11-aerial` | `/services/remote-oversight` | `aerial construction site` | Drone perspective. |
| 12 | `plate-12-shell` | `/services/project-recovery` | `abandoned construction site`, `stalled building shell` | Bleak — this page is read at midnight by someone in trouble. |
| 13 | `plate-13-module` | `/services/prefab-and-modular` | `modular building crane lift`, `prefab module transport truck` | The delivery moment. |
| 14 | `plate-14-timber` | `/insights` index | `stacked timber`, `material yard` | Neutral texture. |

**Import mechanics — read before touching code:**

- Export each photo **≤1800px wide** (hero: target <180KB after AVIF). Don't bake
  any treatment into the files — the duotone/grain is applied live by the
  `<Plate>` component (`src/components/Plate.astro`).
- Drop files in `public/plates/` using the same base names (`plate-01-rebar.jpg`
  etc.) and update the `src=` paths at each usage site (grep for
  `/plates/plate-` — every usage is explicit). Keep `width`/`height` props
  accurate to the real file to avoid layout shift.
- Keep every existing `alt` and `caption` unless the new image genuinely needs a
  different description. **Captions are statements about the work — never a
  location, never a project.** The one rule (art direction §1): no image may ever
  be captioned, positioned or implied as a project of the firm.
- After swapping: rebuild, and re-check type-over-plate contrast on the home hero
  (axe + eyeball). If a plate fails 4.5:1 under type, darken the scrim in
  `index.astro` — never add a text shadow.

### 1.2 Process and add the two headshots (received 2026-08-12)

Both principals' headshots exist — Jesse Giddings (studio, cream background) and
Geordie Flanagan (wood-slat background). Whoever holds the originals attaches
them to the Cowork session.

- Crop both to **4:5 portrait**, matched framing: eye line ~40% from the top,
  similar head size in frame. Export ≤1200px wide, JPG.
- Save as `public/plates/headshot-jesse.jpg` and
  `public/plates/headshot-geordie.jpg`.
- Add each to `/who-we-are` (`src/pages/who-we-are.astro`) beside the respective
  bio using the existing `<Plate>` component with `class="aspect-[4/5]"` — the
  duotone treatment is what makes the two mismatched backgrounds read as a set.
  Alt text: "Portrait of Jesse Giddings" / "Portrait of Geordie Flanagan". No
  caption needed.
- The two source photos differ in background, lighting and expression. The
  treatment papers over most of it; a matched reshoot with one photographer
  remains the art direction's recommendation when convenient, not a blocker.
- **Gate:** Geordie's photo ships only when his name does — see item 2.1.

### 1.3 Wire the enquiry form (site is not capturing leads until this is done)

- Create a free form at `formspree.io`, pointed at the enquiries inbox.
- Replace `YOUR_FORM_ID` in `src/lib/site.ts` (`formEndpoint`).
- Submit a test through `/project-review` on the deployed site and confirm
  delivery. (Free tier shows Formspree's confirmation page instead of the site's
  thank-you redirect — acceptable at launch.)

### 1.4 Small finishing items

- **OG image**: if the hero plate changes the site's look materially, re-render
  `public/og/default.png` (1200×630) to match. Current one uses the H1 + palette
  and remains fine.
- **Plausible**: the analytics script in `src/layouts/Base.astro` points at
  `erskineadvisory.com`. Register the domain at plausible.io (paid) before
  launch, or comment the script out until then — it 404s harmlessly meanwhile.
- **`src/lib/site.ts` placeholders**: business email (`enquiries@…`) and home
  base line are provisional — update when the real ones exist (see 2.4).

---

## PART 2 — Work only the partners can do (launch gates)

The site must stay on the private `*.vercel.app` URL — do not attach the public
domain — until these clear:

| # | Gate | Blocks | Status |
|---|---|---|---|
| 2.1 | **Employment-lawyer review of Geordie's prior-employment agreement** (spec §8.1 — non-compete, non-solicit, fiduciary duties as VP & Partner) | His name and photo, currently drafted on `/who-we-are`, `/independence`, and the prefab service page | Open |
| 2.2 | **E&O at $5M+ and CGL bound** (spec §8.2) | Honest capability claims sitewide | Open |
| 2.3 | **Fees confirmed by both partners** — audit $25,000–60,000; recovery/advisory $300–450/hr (both from COPY DRAFT v3, published on `/fees`) | `/fees` | Open |
| 2.4 | **Entity registration, business email, phone** | Footer, `/terms`, contact, schema | Open |
| 2.5 | **Jesse's bio content** — current copy is the minimal draft; he adds concrete achievements | `/who-we-are` | Open |
| 2.6 | **Domain**: buy `erskineadvisory.com` (+ `.ca`), CIPO/USPTO/BC registry searches on the wordmark, then attach domain in Vercel + DNS | Public launch | Open |
| 2.7 | **Technical bench retained and named** (spec §2.3 — cost consultant first) | `/who-we-are` credibility; roles are described, names say "confirmed in the proposal" until real | Open |
| 2.8 | Decision on the prior-employer conversation (referral source vs quiet exit) — names held off-repo | Launch sequencing | Open |

---

## PART 3 — What is already done (context for any new session)

- **Site**: Astro 5 + Tailwind 4 static build, 27 pages. All copy reconciled to
  COPY DRAFT v3: home, the-owners-position (cornerstone essay), fees (published
  fixed-scope table + FAQ schema), independence (seven commitments + the
  industry-background answer), who-we-are, how-we-work (assess / commit / hold /
  verify / close), five service pages (problem / included / who / fee / what it
  isn't), six insight posts, project-review form + thank-you, privacy, terms,
  404. `/projects` and `/testimonials` are noindex, unlinked stubs by design.
- **Design**: 03-ART-DIRECTION implemented — Plate duotone treatment + grain,
  Inter Tight display scale (4:1), dark Inverse bands, oversized Stats (real
  numbers only), RiskLadder v2 (filled risk area vs attention line, draws in
  once), margin section numbers, designed fee table, once-only motion fully
  gated behind `prefers-reduced-motion` and a no-JS fallback.
- **Honesty rails** (do not undo): no project-size floor, no licensure claims,
  no guarantees or savings percentages, no "Advocate/Construction Advisor" as
  names, no fabricated proof, banned-word list respected, footer carries
  "Photography is illustrative. We do not publish client projects."
- **SEO**: hand-written titles/descriptions, JSON-LD (Organization,
  ProfessionalService, Service, Article, FAQPage), canonicals, robots.txt,
  sitemap excluding stubs, OG image.
- **Quality**: axe-core 0 violations (WCAG 2.2 AA) across key pages, no
  horizontal overflow at 320px, strict CSP in `vercel.json` (no inline scripts).
- **Infrastructure**: repo `jessegiddings/erskine-advisory` (`main`), Vercel
  auto-deploy, `vercel.json` security headers, Formspree form pending ID.
- **Old location**: the site was first built on branch
  `claude/erskine-advisory-site-xeryfw` of `jessegiddings/payrollpicker` — that
  branch is a backup and must never merge into payrollpicker's main.

### Suggested opening prompt for the Cowork session

> Open `docs/04-LAUNCH-HANDOFF.md` in the `jessegiddings/erskine-advisory` repo
> and work through Part 1: source the 14 photographs per the shot list (saving a
> licence screenshot per image into `docs/image-licences/`), process the two
> attached headshots per §1.2, swap everything into the `<Plate>` usages, set the
> Formspree form ID I give you, rebuild, re-run the accessibility and contrast
> checks, and push to main.
