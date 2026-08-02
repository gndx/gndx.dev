import type { APIRoute } from 'astro';
import { isLocale, prefixedLocales, type Locale } from '@i18n/config';
import { getPostsByLocale } from '@utils/i18nContent';
import { createArticleMarkdown } from '@utils/machineFeeds';

export const prerender = true;

const getSlug = (post: { slug?: string; id: string }) =>
  post.slug || post.id.replace(/\.(md|mdx)$/i, '');

export async function getStaticPaths() {
  const paths = [];
  for (const locale of prefixedLocales) {
    const posts = await getPostsByLocale(locale);
    paths.push(
      ...posts.map((post) => ({
        params: { locale, slug: getSlug(post) }
      }))
    );
  }
  return paths;
}

export const GET: APIRoute = async ({ params }) => {
  const { locale, slug } = params;
  if (!isLocale(locale) || locale === 'es' || !slug) {
    return new Response('Not found', { status: 404 });
  }

  const posts = await getPostsByLocale(locale as Locale);
  const post = posts.find((item) => getSlug(item) === slug);
  if (!post) return new Response('Not found', { status: 404 });

  const canonical = `https://gndx.dev/${locale}/blog/${slug}/`;
  return new Response(createArticleMarkdown(post, locale as Locale, slug), {
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
      'Cache-Control': 'public, max-age=3600, stale-while-revalidate=86400',
      'Content-Signal': 'search=yes, ai-input=yes, ai-train=no, use=reference',
      Link: `<${canonical}>; rel="canonical"`,
      'X-Content-Type-Options': 'nosniff'
    }
  });
};
