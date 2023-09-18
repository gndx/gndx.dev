import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
	site: 'https://gndx.dev',
	markdown: {
		drafts: true,
		shikiConfig: {
			theme: 'material-theme-palenight',
			wrap: true
		}
	},
	integrations: [mdx({
		syntaxHighlight: 'shiki',
		shikiConfig: {
			theme: 'material-theme-palenight',
			wrap: true
		},
		drafts: true
	}), , sitemap(), tailwind()],

});
