import { initWasm, Resvg } from '@resvg/resvg-wasm';
// @ts-expect-error – WASM module, handled by @cloudflare/vite-plugin
import resvgWasm from '@resvg/resvg-wasm/index_bg.wasm';

const WIDTH = 1200;
const HEIGHT = 630;
const TITLE_MAX_CHARS_PER_LINE = 32;
const TITLE_MAX_LINES = 3;
const TITLE_FONT_SIZE = 62;
const TITLE_LINE_HEIGHT = 66;

const escapeXml = (value: string): string =>
  value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&apos;');

const wrapText = (text: string, maxCharsPerLine: number, maxLines: number): string[] => {
  const words = text.trim().split(/\s+/).filter(Boolean);
  const lines: string[] = [];
  let line = '';

  for (const word of words) {
    const candidate = line ? `${line} ${word}` : word;
    if (candidate.length <= maxCharsPerLine) {
      line = candidate;
      continue;
    }

    if (line) lines.push(line);
    line = word;

    if (lines.length >= maxLines) break;
  }

  if (line && lines.length < maxLines) {
    lines.push(line);
  }

  if (lines.length === 0) return ['Blog Post'];

  if (words.join(' ').length > lines.join(' ').length) {
    lines[lines.length - 1] = `${lines[lines.length - 1].slice(0, Math.max(0, maxCharsPerLine - 1))}...`;
  }

  return lines;
};

export const generateBlogOgSvg = (title: string): string => {
  const titleLines = wrapText(title, TITLE_MAX_CHARS_PER_LINE, TITLE_MAX_LINES);
  const titleStartY = 338 - ((titleLines.length - 1) * TITLE_LINE_HEIGHT) / 2;
  const lastTitleY = titleStartY + (titleLines.length - 1) * TITLE_LINE_HEIGHT;
  const subtitleY = lastTitleY + 68;

  const titleTspans = titleLines
    .map(
      (line, index) =>
        `<tspan x="600" y="${titleStartY + index * TITLE_LINE_HEIGHT}" text-anchor="middle">${escapeXml(line)}</tspan>`
    )
    .join('');

  return `
<svg width="${WIDTH}" height="${HEIGHT}" viewBox="0 0 ${WIDTH} ${HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="glowLeft" cx="0%" cy="100%" r="80%">
      <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#7c3aed" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="glowRight" cx="100%" cy="0%" r="80%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.68" />
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0" />
    </radialGradient>
    <pattern id="grid" width="64" height="64" patternUnits="userSpaceOnUse">
      <path d="M 64 0 L 0 0 0 64" fill="none" stroke="#cbd5e1" stroke-opacity="0.14" stroke-width="1" />
    </pattern>
  </defs>

  <rect x="0" y="0" width="${WIDTH}" height="${HEIGHT}" fill="#020205" />
  <rect x="0" y="0" width="${WIDTH}" height="${HEIGHT}" fill="url(#glowLeft)" />
  <rect x="0" y="0" width="${WIDTH}" height="${HEIGHT}" fill="url(#glowRight)" />
  <rect x="0" y="0" width="${WIDTH}" height="${HEIGHT}" fill="url(#grid)" />
  <rect x="0" y="0" width="${WIDTH}" height="${HEIGHT}" fill="#00000066" />

  <text x="600" fill="#f8fafc" font-size="${TITLE_FONT_SIZE}" font-weight="700" font-family="Arial, Helvetica, sans-serif" letter-spacing="0.05">
    ${titleTspans}
  </text>

  <text x="600" y="${subtitleY}" fill="#e2e8f0" font-size="34" font-family="Arial, Helvetica, sans-serif" font-weight="300" text-anchor="middle">
    Oscar Barajas @gndx
  </text>
</svg>`;
};

let wasmInitialized = false;

export const generateBlogOgPng = async (title: string): Promise<Uint8Array> => {
  if (!wasmInitialized) {
    await initWasm(resvgWasm as WebAssembly.Module);
    wasmInitialized = true;
  }
  const svg = generateBlogOgSvg(title);
  const resvg = new Resvg(svg);
  return resvg.render().asPng();
};
