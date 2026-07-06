import { defineConfig } from 'astro/config';
import pagefind from 'astro-pagefind';
import { fixExportedMarkdown } from './src/utils/remark-fix-exported-markdown.js';

export default defineConfig({
  site: 'https://invitejesus.org',
  integrations: [pagefind()],
  markdown: {
    remarkPlugins: [fixExportedMarkdown],
  },
});
