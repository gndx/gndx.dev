import type { APIRoute } from 'astro';
import { createJsonFeed } from '@utils/machineFeeds';

export const prerender = true;

export const GET: APIRoute = async () => {
  const feed = await createJsonFeed('es');
  return new Response(JSON.stringify(feed), {
    headers: {
      'Content-Type': 'application/feed+json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
      'X-Content-Type-Options': 'nosniff'
    }
  });
};
