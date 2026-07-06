import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const encyclopedia = defineCollection({
  loader: glob({ base: './src/content/encyclopedia', pattern: '**/*.md' }),
  schema: z
    .object({
      title: z.string().optional(),
      description: z.string().optional(),
      category: z.string().optional(),
      tags: z.array(z.string()).optional(),
      related: z.array(z.string()).optional(),
      sortTitle: z.string().optional(),
      draft: z.boolean().optional(),
    })
    .passthrough(),
});

export const collections = { encyclopedia };
