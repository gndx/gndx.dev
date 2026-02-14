import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blogSchema = z.object({
  title: z.string(),
  description: z.string(),
  pubDate: z.coerce.date(),
  updatedDate: z.coerce.date().optional(),
  heroImage: z.string().optional(),
  categories: z.array(z.string()).default(['others']),
  tags: z.array(z.string()).default(['others']),
  authors: z.array(z.string()).default(['gndx'])
});

const blogEs = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: 'src/content/blog/es' }),
  schema: z.object({
    ...blogSchema.shape
  })
});

const blogEn = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: 'src/content/blog/en' }),
  schema: z.object({
    ...blogSchema.shape
  })
});

const blogPt = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: 'src/content/blog/pt' }),
  schema: z.object({
    ...blogSchema.shape
  })
});

export const collections = { blogEs, blogEn, blogPt };
