# Erskine Advisory — website

Static site for Erskine Advisory, an independent owner's representation practice for
private clients building significant residences. Built per **BUILD SPEC v3**, with all
page copy reconciled to **COPY DRAFT v3**.

Astro 5 · Tailwind CSS 4 · content collections · Formspree · Plausible · self-hosted fonts.
No CMS, no client-side framework — the only JS on the site is the mobile nav toggle.

```bash
npm install
npm run dev       # local dev at :4321
npm run build     # static build to dist/
npm run preview   # serve dist/
```

## Structure

- `src/lib/site.ts` — single source of truth for firm name, contact, nav. **Provisional values are flagged here.**
- `src/content/services/` — five service pages (schema in `src/content.config.ts`)
- `src/content/insights/` — six launch posts targeting the spec §7 SEO clusters
- `src/components/RiskLadder.astro` — the signature diagram (spec §6), inline SVG with text alternative
- `src/pages/projects.astro`, `src/pages/testimonials.astro` — **stubs**: noindex, unlinked, excluded from sitemap. Activate only with real, permissioned content.

## Launch gates (from spec §10 — do not deploy publicly before these)

1. **Geordie's name is on `/who-we-are` and referenced on `/services/prefab-and-modular`.**
   Spec §8.1 requires employment-lawyer review of his prior-employment agreement *before his name
   appears publicly*. Remove or anonymize those passages if launching earlier.
2. **E&O ($5M+) and CGL bound** (§8.2) before the site implies engagement capability.
3. Provisional values in `src/lib/site.ts`: home base city, business email. Update once
   entity/registrations exist (open items #6, #10).
4. **Fees on `/fees`** are from COPY DRAFT v3 (audit $25,000–60,000; recovery/advisory
   $300–450/hr). Confirm before launch (open item #7).
5. Jesse's bio on `/who-we-are` is a minimal draft pending his confirmation (open item #8).
6. Domain: confirm `erskineadvisory.com` (set in `astro.config.mjs` and `src/lib/site.ts`),
   plus CIPO/USPTO/BC registry searches (open item #1).

## Deploying

Deployed on Vercel as a static Astro build; `vercel.json` carries the security headers
and immutable caching for fonts and hashed assets. The project review form posts to
Formspree with a `_gotcha` honeypot and redirects to `/project-review/thank-you`:
create a free form at formspree.io and replace `YOUR_FORM_ID` in `src/lib/site.ts` —
**the form does not deliver until that ID is set.** (The `_next` redirect to the
thank-you page requires a paid Formspree plan; on the free tier submitters see
Formspree's confirmation page instead, which is fine for launch.)

Analytics: Plausible script is in `src/layouts/Base.astro`; register the domain in
Plausible before launch or remove the script tag.
