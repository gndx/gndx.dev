import config from '@config/config.json';
import { prefixedLocales } from '@i18n/config';
import { getPostsByLocale } from '@utils/i18nContent';
import { generateBlogOgPng } from '@utils/generateBlogOgSvg';
import type { APIRoute } from 'astro';

export const prerender = true;

const getPostSlug = (slug: string | undefined, id: string): string =>
  slug || id.replace(/\.(md|mdx)$/i, '');

export async function getStaticPaths() {
  const paths: Array<{ params: { locale: string; slug: string }; props: { title: string } }> = [];

  for (const locale of prefixedLocales) {
    const posts = await getPostsByLocale(locale);
    paths.push(
      ...posts.map((post) => ({
        params: { locale, slug: getPostSlug(post.slug, post.id) },
        props: { title: post.data.title }
      }))
    );
  }

  return paths;
}

export const GET: APIRoute = async ({ props }) => {
  const title = String(props?.title || config.site.title);
  const png = await generateBlogOgPng(title);

  return new Response(png, {
    headers: {
      'Content-Type': 'image/png',
      'Cache-Control': 'public, max-age=31536000, immutable'
    }
  });
};
