# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All commands run from `gndx.dev/`. Node 20+ is expected.

- `npm run dev` — Astro dev server at `http://localhost:4321`. The `predev` hook runs `scripts/youtube.cjs`, which requires `API_KEY` and `CHANNEL_ID` in `.env` (see `.env.example`). Without those vars the script will fail and block startup.
- `npm run build` — Static build to `dist/`. Also runs `prebuild` → `scripts/youtube.cjs`.
- `npm run preview` — Serve the built `dist/` locally.
- `npm run youtube` — Refresh `src/config/youtube.json` from the YouTube Data API.
- `npm run newpost` — Scaffold a blog post via `astro-md-generator`.
- `node scripts/translate-posts.mjs` — Bulk-translate posts from `src/content/blog/es` into `en` and `pt` (uses `js-yaml`; review output before committing).

There is no test suite or linter wired up. The validation step is `npm run build` and visual checks of `/`, `/blog`, `/categories`, `/tags`.

## Architecture

Astro 5 static site deployed to **Cloudflare Pages/Workers** (`@astrojs/cloudflare` adapter, `wrangler.jsonc` builds from `dist/_worker.js/index.js`). Tailwind 4 is wired through `@tailwindcss/vite`, not a PostCSS plugin — `tailwind.config.cjs` exists but the Vite plugin is the source of truth.

### Trilingual content model

The site is i18n-aware with locales `es` (default, unprefixed), `en`, `pt` defined in `astro.config.mjs` and mirrored in `src/i18n/config.ts`. Two things to remember:

1. **Three separate content collections**, not one. `src/content/config.ts` defines `blogEs`, `blogEn`, `blogPt`, each loading from `src/content/blog/{es,en,pt}/`. A post added to only `es/` will not exist in the other locales — use `scripts/translate-posts.mjs` or duplicate manually. Frontmatter schema is shared (`title`, `description`, `pubDate`, `categories`, `tags`, `authors`, optional `updatedDate`/`heroImage`).
2. **Routes are duplicated per locale.** Default-locale routes live at `src/pages/*` (e.g. `src/pages/blog/[...slug].astro`). Prefixed-locale routes live under `src/pages/[locale]/*` and must stay in sync. When adding a new page, add it in both places or the non-default locales lose it.

URL helpers (`withLocalePath`, `stripLocaleFromPath`, `parseAcceptLanguage`) live in `src/i18n/config.ts` and should be used whenever building cross-locale links so the default-locale-unprefixed convention is preserved.

### Build integrations

`astro.config.mjs` composes: `@astrojs/mdx` (with Shiki `dracula` theme), `@astrojs/sitemap`, `astro-robots-txt`, `astro-compress`, Tailwind Vite plugin, and `vite-plugin-pwa`. The PWA manifest is generated from `src/utils/manifest.ts` — edit there, not a static `manifest.json`. Workbox precaches everything matching `dist/**/*.{js,css,svg,png,jpg,jpeg,gif,webp,woff,woff2,ttf,eot,ico}` with `navigateFallback: null` (SPA fallback is intentionally off because every route is pre-rendered).

`markdown.drafts: true` is enabled both globally and on MDX, so draft posts render in builds.

### Taxonomy

Categories and tags are derived at build time from post frontmatter via `src/utils/getAllTags.ts` and slugged via `src/utils/slug.ts`. Pages under `src/pages/categories/` and `src/pages/tags/` use these helpers with `getStaticPaths`. When renaming a tag or category, update every affected post's frontmatter — there's no redirect layer.

### YouTube data flow

`scripts/youtube.cjs` runs as a `pre*` hook on `dev`/`start`/`build` and writes `src/config/youtube.json`, which `src/components/FeaturedVideos.astro` reads at build time. The cache file is committed; the script will overwrite it on every run. If working offline or without API credentials, comment out the `pre*` hooks in `package.json` or stub the JSON.

### Configuration surface

- `src/config/config.json` — site metadata (title, description, author, URL).
- `src/config/menu.json` — header/nav links.
- `src/config/social.js` — social profiles and inline SVG icons.
- `src/config/youtube.json` — generated; don't hand-edit.

## Conventions

- Components are `.astro` first; reach for TS only for utilities under `src/utils/`. There is no React/Vue/Svelte integration despite the `react` keyword in `package.json` (legacy from the EV0 template).
- Posts use frontmatter `authors: ["gndx"]` (array). Older posts may use a single-author shape — prefer the array form when editing.
- Hero images in posts are paths into `public/` (e.g. `/blog-placeholder.jpg`).
