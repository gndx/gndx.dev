import { getCollection } from "astro:content";

export async function GET() {
  const posts = await getCollection("blog");

  const payload = posts.map((post) => ({
    title: post.data.title,
    description: post.data.description,
    url: `/blog/${post.slug}/`,
    tags: post.data.tags ?? [],
    categories: post.data.categories ?? [],
    pubDate: post.data.pubDate,
  }));

  return new Response(JSON.stringify(payload), {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
    },
  });
}
