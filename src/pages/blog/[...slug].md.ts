import type { APIRoute } from 'astro';
import { getPostsByLocale } from '@utils/i18nContent';
import { createArticleMarkdown } from '@utils/machineFeeds';

export const prerender = true;

const getSlug = (post: { slug?: string; id: string }) =>
  post.slug || post.id.replace(/\.(md|mdx)$/i, '');

export async function getStaticPaths() {
  const posts = await getPostsByLocale('es');
  return posts.map((post) => ({ params: { slug: getSlug(post) } }));
}

export const GET: APIRoute = async ({ params }) => {
  const slug = params.slug;
  const posts = await getPostsByLocale('es');
  const post = posts.find((item) => getSlug(item) === slug);

  if (!post || !slug) return new Response('Not found', { status: 404 });

  const canonical = `https://gndx.dev/blog/${slug}/`;
  return new Response(createArticleMarkdown(post, 'es', slug), {
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
      'Cache-Control': 'public, max-age=3600, stale-while-revalidate=86400',
      'Content-Signal': 'search=yes, ai-input=yes, ai-train=no, use=reference',
      Link: `<${canonical}>; rel="canonical"`,
      'X-Content-Type-Options': 'nosniff'
    }
  });
};
