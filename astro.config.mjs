import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwindcss from '@tailwindcss/vite';
import Compress from 'astro-compress';
import sitemap from '@astrojs/sitemap';
import robotsTxt from 'astro-robots-txt';
import { VitePWA } from 'vite-plugin-pwa';

import { manifest } from './src/utils/manifest';

// https://astro.build/config
export default defineConfig({
  site: 'https://gndx.dev',
  image: {
    remotePatterns: [{ protocol: 'https' }]
  },
  markdown: {
    drafts: true,
    shikiConfig: {
      theme: 'material-theme-palenight',
      wrap: true
    }
  },
  integrations: [
    mdx({
      syntaxHighlight: 'shiki',
      shikiConfig: {
        theme: 'material-theme-palenight',
        wrap: true
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
  }
});