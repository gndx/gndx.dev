import config from '@config/config.json';
import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';
import { generateBlogOgPng } from '@utils/generateBlogOgSvg';

export const prerender = true;

const getPostSlug = (slug: string | undefined, id: string): string =>
  slug || id.replace(/\.(md|mdx)$/i, '');

export async function getStaticPaths() {
  const posts = await getCollection('blogEs');
  return posts.map((post) => ({
    params: { slug: getPostSlug(post.slug, post.id) },
    props: { title: post.data.title }
  }));
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
