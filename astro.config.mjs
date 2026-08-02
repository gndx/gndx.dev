import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwindcss from '@tailwindcss/vite';
import Compress from 'astro-compress';
import sitemap from '@astrojs/sitemap';
import robotsTxt from 'astro-robots-txt';
import { VitePWA } from 'vite-plugin-pwa';

import { manifest } from './src/utils/manifest';

import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
export default defineConfig({
  site: 'https://gndx.dev',

  i18n: {
    defaultLocale: 'es',
    locales: ['es', 'en', 'pt'],
    routing: {
      prefixDefaultLocale: false
    }
  },

  markdown: {
    shikiConfig: {
      theme: 'dracula',
      wrap: false
    }
  },

  integrations: [
    mdx({
      syntaxHighlight: 'shiki',
      shikiConfig: {
        theme: 'dracula',
        wrap: false
      }
    }),
    Compress(),
    sitemap({
      filter(page) {
        const pathname = new URL(page).pathname;
        return !/^\/(?:en\/|pt\/)?tags(?:\/|$)/.test(pathname);
      }
    }),
    robotsTxt({
      policy: [
        { userAgent: 'OAI-SearchBot', allow: '/' },
        { userAgent: 'PerplexityBot', allow: '/' },
        { userAgent: '*', allow: '/' }
      ]
    })
  ],

  vite: {
    plugins: [VitePWA({
      registerType: 'autoUpdate',
      outDir: 'dist/client',
      manifest,
      workbox: {
        globDirectory: 'dist/client',
        globPatterns: ['**/*.{js,css,svg,woff,woff2,ico}'],
        globIgnores: ['og/**', 'og-assets/**'],
        navigateFallback: null,
        cleanupOutdatedCaches: true
      }
    }), tailwindcss()]
  },

  adapter: cloudflare({
    cloudflareModules: true,
    imageService: 'passthrough'
  })
});
