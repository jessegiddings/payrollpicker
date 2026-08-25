// Single source of truth for firm identity and contact details.
// Items marked PROVISIONAL await partner confirmation (spec §10) —
// update here and they change everywhere.

export const SITE = {
  name: 'Erskine Advisory',
  domain: 'erskineadvisory.com',
  url: 'https://erskineadvisory.com',
  // PROVISIONAL — open item #6: home base city to name publicly.
  homeBase: 'Salt Spring Island, British Columbia',
  serviceArea: 'Engagements across Canada and the United States, delivered remote-first.',
  // PROVISIONAL — open item #10: business email and phone.
  email: 'enquiries@erskineadvisory.com',
  // PROVISIONAL — create a free Formspree form (formspree.io), then replace
  // YOUR_FORM_ID with the real ID. The form will not deliver until this is set.
  formEndpoint: 'https://formspree.io/f/YOUR_FORM_ID',
  tagline: 'Independent owner’s representation for significant private residences.',
} as const;

export const NAV = [
  { label: 'How It Works', href: '/how-it-works' },
  { label: 'Services', href: '/services' },
  { label: 'Fees', href: '/fees' },
  { label: 'Independence', href: '/independence' },
  { label: 'Who We Are', href: '/who-we-are' },
  { label: 'Contact', href: '/contact' },
] as const;

export const FOOTER_LINKS = [
  { label: 'How We Work', href: '/how-we-work' },
  { label: 'Compare the Models', href: '/compare' },
  { label: 'Insights', href: '/insights' },
  // LAUNCH GATE: hold until the handbook clears BC construction-lawyer review.
  { label: 'The BC Owner’s Handbook', href: '/handbook' },
  { label: 'Request a Project Review', href: '/project-review' },
  { label: 'Privacy', href: '/privacy' },
  { label: 'Terms', href: '/terms' },
] as const;

// The three words (rebuild spec §2.1) — used on / and /independence.
export const THREE_WORDS = [
  { word: 'Independent', line: 'We are paid by you and by no one else on the project.' },
  { word: 'Verified', line: 'Nothing is approved for payment until someone has confirmed it exists.' },
  { word: 'Documented', line: 'Every decision, approval and release is written down and yours to keep.' },
] as const;
