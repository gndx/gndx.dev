import type { APIRoute } from 'astro';
import { createLlmsText } from '@utils/machineFeeds';

export const prerender = true;

export const GET: APIRoute = async () =>
  new Response(await createLlmsText(false), {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
      'X-Content-Type-Options': 'nosniff'
    }
  });
