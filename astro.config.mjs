import { defineConfig, fontProviders } from 'astro/config';
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

  build: {
    // The complete stylesheet is small enough to inline, removing a
    // render-blocking request on the critical path.
    inlineStylesheets: 'always'
  },

  image: {
    domains: ['i.ytimg.com']
  },

  fonts: [
    {
      provider: fontProviders.google(),
      name: 'Space Grotesk',
      cssVariable: '--font-space-grotesk',
      weights: [400, 500, 600],
      styles: ['normal'],
      subsets: ['latin'],
      fallbacks: ['system-ui', 'sans-serif']
    },
    {
      provider: fontProviders.google(),
      name: 'Space Mono',
      cssVariable: '--font-space-mono',
      weights: [400, 700],
      styles: ['normal'],
      subsets: ['latin'],
      fallbacks: ['monospace']
    },
    {
      provider: fontProviders.google(),
      name: 'JetBrains Mono',
      cssVariable: '--font-jetbrains-mono',
      weights: [400, 500, 600],
      styles: ['normal'],
      subsets: ['latin'],
      fallbacks: ['monospace']
    }
  ],

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
      ],
      transform(content) {
        return content.replace(
          'User-agent: *\nAllow: /',
          'User-agent: *\nContent-Signal: search=yes, ai-input=yes, ai-train=no, use=reference\nAllow: /'
        );
      }
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
    imageService: 'compile'
  })
});
