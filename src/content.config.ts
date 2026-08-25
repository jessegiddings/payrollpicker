import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const services = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/services' }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    summary: z.string(),
    feeShape: z.string(),
    whoItsFor: z.string(),
    order: z.number(),
  }),
});

const insights = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/insights' }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    description: z.string(),
    publishDate: z.coerce.date(),
    keywords: z.array(z.string()),
  }),
});

// Long-form guides. Source of record for the gated PDF at
// public/downloads/ — the PDF is generated from this markdown, so edit here
// and rebuild rather than editing the PDF.
const guides = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/guides' }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    description: z.string(),
    publishDate: z.coerce.date(),
    keywords: z.array(z.string()),
  }),
});

export const collections = { services, insights, guides };
