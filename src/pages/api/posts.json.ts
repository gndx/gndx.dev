import { getCollection } from 'astro:content';

export async function GET() {
  const posts = await getCollection('blog');
  const data = posts.map((post) => ({
    title: post.data.title,
    description: post.data.description,
    slug: post.slug,
    pubDate: post.data.pubDate,
  }));
  return new Response(JSON.stringify(data), {
    headers: {
      'Content-Type': 'application/json',
    },
  });
}
