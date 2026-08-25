// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://erskineadvisory.com',
  trailingSlash: 'never',
  integrations: [
    sitemap({
      // Stubs stay out of the sitemap until there is proof to put on them.
      filter: (page) =>
        !page.includes('/projects') &&
        !page.includes('/testimonials') &&
        !page.includes('/project-review/thank-you') &&
        !page.includes('/handbook/thank-you'),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
