# Architecture

## Runtime Model

- Astro static site generation (`astro build`).
- Output is pre-rendered pages plus PWA assets.
- No server-side app runtime is required for core rendering.

## Main Data Sources

- Blog content collection: `src/content/blog/*.{md,mdx}`
- Content schema and validation: `src/content/config.ts`
- Site metadata and author info: `src/config/config.json`
- Navigation: `src/config/menu.json`
- Social links/icons: `src/config/social.js`
- YouTube feed cache: `src/config/youtube.json`

## Routing

- Home: `src/pages/index.astro`
- Blog listing (paginated): `src/pages/blog/[...page].astro`
- Blog post detail: `src/pages/blog/[...slug].astro`
- Categories:
  - index: `src/pages/categories/index.astro`
  - detail: `src/pages/categories/[category].astro`
- Tags:
  - index: `src/pages/tags/index.astro`
  - detail: `src/pages/tags/[tag].astro`
- RSS feed: `src/pages/rss.xml.js`

## UI Composition

- Base shell and metadata: `src/layouts/Base.astro`
- Post layout: `src/layouts/BlogPost.astro`
- Generic page wrapper: `src/layouts/Page.astro`
- Card grid for post lists: `src/layouts/Posts.astro`

Primary shared components include:

- `src/components/Header.astro`
- `src/components/Hero.astro`
- `src/components/FeaturedVideos.astro`
- `src/components/Pagination.astro`

## Taxonomy and Slug Helpers

- Category/tag extraction and filtering: `src/utils/getAllTags.ts`
- Slug helpers: `src/utils/slug.ts`

## Build Integrations

Configured in `astro.config.mjs`:

- `@astrojs/mdx`
- `@astrojs/sitemap`
- `astro-robots-txt`
- `astro-compress`
- Tailwind Vite plugin
- `vite-plugin-pwa` using `src/utils/manifest.ts`

## YouTube Data Flow

1. Set `API_KEY` and `CHANNEL_ID` in `.env`.
2. Run `npm run youtube`.
3. Script `scripts/youtube.cjs` fetches latest videos and writes to `src/config/youtube.json`.
4. UI consumes that file in `src/components/FeaturedVideos.astro`.
