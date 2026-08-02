import type { APIRoute } from 'astro';
import { isLocale, prefixedLocales } from '@i18n/config';
import { createJsonFeed } from '@utils/machineFeeds';

export const prerender = true;

export const getStaticPaths = () => prefixedLocales.map((locale) => ({ params: { locale } }));

export const GET: APIRoute = async ({ params }) => {
  const { locale } = params;
  if (!isLocale(locale)) return new Response('Not found', { status: 404 });

  const feed = await createJsonFeed(locale);
  return new Response(JSON.stringify(feed), {
    headers: {
      'Content-Type': 'application/feed+json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
      'X-Content-Type-Options': 'nosniff'
    }
  });
};
