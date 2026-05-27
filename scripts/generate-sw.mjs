import { generateSW } from 'workbox-build';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');

const result = await generateSW({
  swDest: resolve(root, 'dist/client/sw.js'),
  globDirectory: resolve(root, 'dist/client'),
  globPatterns: ['**/*.{js,css,svg,png,jpg,jpeg,gif,webp,woff,woff2,ttf,eot,ico}'],
  navigateFallback: null,
  runtimeCaching: [],
  skipWaiting: true,
  clientsClaim: true,
});

console.log(`[generate-sw] ${result.count} files precached (${Math.round(result.size / 1024)} KB)`);
