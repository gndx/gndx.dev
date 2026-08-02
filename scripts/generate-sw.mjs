import { generateSW } from 'workbox-build';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');

const result = await generateSW({
  swDest: resolve(root, 'dist/client/sw.js'),
  globDirectory: resolve(root, 'dist/client'),
  globPatterns: ['**/*.{js,css,svg,woff,woff2,ico}'],
  globIgnores: ['og/**', 'og-assets/**'],
  navigateFallback: null,
  runtimeCaching: [],
  cleanupOutdatedCaches: true,
  skipWaiting: true,
  clientsClaim: true,
});

console.log(`[generate-sw] ${result.count} files precached (${Math.round(result.size / 1024)} KB)`);
