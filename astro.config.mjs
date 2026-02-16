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

  image: {
    remotePatterns: [{ protocol: 'https' }]
  },

  markdown: {
    drafts: true,
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
      },
      drafts: true
    }),
    Compress(),
    sitemap(),
    tailwindcss(),
    robotsTxt()
  ],

  vite: {
    plugins: [VitePWA({
      registerType: 'autoUpdate',
      manifest,
      workbox: {
        globDirectory: 'dist',
        globPatterns: [
          '**/*.{js,css,svg,png,jpg,jpeg,gif,webp,woff,woff2,ttf,eot,ico}'
        ],
        navigateFallback: null
      }
    }), tailwindcss()]
  },

  adapter: cloudflare()
});
