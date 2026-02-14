# gndx.dev

Personal website and blog for [gndx.dev](https://gndx.dev), built with Astro 5, Tailwind CSS 4, and TypeScript.

## Overview

- Static site generated with Astro.
- Blog content sourced from `src/content/blog` (`.md` and `.mdx`).
- Taxonomy pages for categories and tags.
- RSS, sitemap, robots.txt, and PWA manifest/service worker integration.
- Optional YouTube feed data generation into `src/config/youtube.json`.

## Tech Stack

- Astro 5 (`astro`)
- Tailwind CSS 4 (`@tailwindcss/vite`)
- MDX (`@astrojs/mdx`)
- PWA (`vite-plugin-pwa`)
- Compression, sitemap, robots (`astro-compress`, `@astrojs/sitemap`, `astro-robots-txt`)

## Quick Start

```bash
git clone https://github.com/gndx/gndx.dev.git
cd gndx.dev
npm install
npm run dev
```

App runs at `http://localhost:4321`.

## Scripts

| Command | Purpose |
|---|---|
| `npm run dev` | Start Astro dev server |
| `npm run start` | Alias of `dev` |
| `npm run build` | Build production output to `dist/` |
| `npm run preview` | Preview production build |
| `npm run astro` | Run Astro CLI directly |
| `npm run youtube` | Fetch latest channel videos into `src/config/youtube.json` |
| `npm run newpost` | Run `astro-md-generator` post scaffold |

## Configuration

- Site metadata: `src/config/config.json`
- Navigation: `src/config/menu.json`
- Social networks: `src/config/social.js`
- YouTube video cache: `src/config/youtube.json`
- Content schema: `src/content/config.ts`
- PWA manifest source: `src/utils/manifest.ts`

## Content Conventions

Blog entries live in `src/content/blog` and must follow the schema in `src/content/config.ts`.

Required frontmatter:

```yaml
title: "Post title"
description: "Short description"
pubDate: "2026-02-11T00:00:00.000Z"
categories: ["category"]
tags: ["tag"]
authors: ["gndx"]
```

Optional frontmatter:

```yaml
updatedDate: "2026-02-11T00:00:00.000Z"
heroImage: "/blog-placeholder.jpg"
```

## Project Structure

```text
.
├── public/               # Static assets
├── scripts/              # Utility scripts (YouTube + legacy post script)
├── src/
│   ├── components/       # Reusable Astro components
│   ├── config/           # Site/menu/social/youtube config
│   ├── content/          # Astro content collections
│   ├── layouts/          # Shared page and post layouts
│   ├── pages/            # File-based routes
│   ├── styles/           # Global CSS
│   └── utils/            # Helpers (slug, taxonomy, PWA manifest)
├── astro.config.mjs
├── tailwind.config.cjs
└── tsconfig.json
```

## Contributor Docs

- `docs/ARCHITECTURE.md`
- `docs/CONTRIBUTING.md`

## License

MIT.
