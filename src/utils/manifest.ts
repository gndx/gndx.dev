import type { ManifestOptions } from "vite-plugin-pwa";
import config from "../config/config.json";

export const manifest: Partial<ManifestOptions> = {
  name: config.site.title,
  short_name: config.site.title,
  description: config.site.description,
  theme_color: "#30E130",
  background_color: "#ffffff",
  display: "minimal-ui",
  icons: [
    {
      src: "/favicons/favicon-192x192.png",
      sizes: "192x192",
      type: "image/png",
    },
    {
      src: "/favicons/favicon-512x512.png",
      sizes: "512x512",
      type: "image/png",
    },
    {
      src: "/favicons/favicon-512x512.png",
      sizes: "512x512",
      type: "image/png",
      purpose: "any maskable",
    },
  ],
};
