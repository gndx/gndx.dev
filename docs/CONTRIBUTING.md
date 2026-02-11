# Contributing

## Prerequisites

- Node.js 20+ recommended
- npm (project currently uses `package-lock.json`)

## Local Development

```bash
npm install
npm run dev
```

Build and preview:

```bash
npm run build
npm run preview
```

## Project Conventions

## 1) Content and Frontmatter

- Add posts in `src/content/blog`.
- Use `.md` or `.mdx`.
- Frontmatter must satisfy `src/content/config.ts`:
  - Required: `title`, `description`, `pubDate`, `categories`, `tags`
  - Optional: `updatedDate`, `heroImage`, `authors`
- Prefer `authors` (array) over legacy single-author patterns in older posts.

Example:

```yaml
---
title: "My post"
description: "Summary"
pubDate: "2026-02-11T00:00:00.000Z"
heroImage: "/blog-placeholder.jpg"
categories: ["javascript"]
tags: ["astro"]
authors: ["gndx"]
---
```

## 2) Routing and Taxonomy

- Blog list uses static pagination (`src/pages/blog/[...page].astro`).
- Blog details resolve by collection slug (`src/pages/blog/[...slug].astro`).
- Categories and tags are generated from post frontmatter via:
  - `src/utils/getAllTags.ts`
  - `src/utils/slug.ts`

## 3) Configuration

- Site-wide metadata: `src/config/config.json`
- Menu links: `src/config/menu.json`
- Social links/SVG icons: `src/config/social.js`
- Cached YouTube data: `src/config/youtube.json`

## 4) Styling and Components

- Global styles: `src/styles/global.css`
- Tailwind configuration: `tailwind.config.cjs`
- Shared layouts/components are Astro-first (`.astro`) with TypeScript where useful.

## 5) Scripts

- `npm run youtube` updates `src/config/youtube.json` from YouTube Data API.
  - Requires `.env` values:
    - `API_KEY`
    - `CHANNEL_ID`
- `npm run newpost` runs `astro-md-generator`.

## Validation Checklist

- `npm run build` passes.
- New/updated content renders correctly in:
  - `/`
  - `/blog`
  - `/categories`
  - `/tags`
- If taxonomy values changed, verify generated pages still resolve.
