import { getCollection } from 'astro:content';
import type { Locale } from '@i18n/config';
import { slugify, deslugify } from './slug';

export type BlogCollection = 'blogEs' | 'blogEn' | 'blogPt';

export const collectionByLocale: Record<Locale, BlogCollection> = {
  es: 'blogEs',
  en: 'blogEn',
  pt: 'blogPt'
};

const getEntrySlug = (post: { slug?: string; id: string }) =>
  post.slug || post.id.replace(/\.(md|mdx)$/i, '');

export const getPostsByLocale = async (locale: Locale) => {
  const posts = await getCollection(collectionByLocale[locale]);
  for (const post of posts as Array<{ id: string; slug?: string }>) {
    if (!post.slug) post.slug = getEntrySlug(post);
  }
  return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
};

export const getTaxonomyByLocale = async (
  locale: Locale,
  key: 'tags' | 'categories'
): Promise<Array<{ name: string; slug: string }>> => {
  const posts = await getPostsByLocale(locale);
  const seen = new Set<string>();
  const terms: Array<{ name: string; slug: string }> = [];

  for (const post of posts) {
    for (const item of post.data[key]) {
      const slug = slugify(item);
      if (seen.has(slug)) continue;
      seen.add(slug);
      terms.push({ name: item, slug });
    }
  }

  return terms;
};

export const filterByTaxonomy = (
  posts: Awaited<ReturnType<typeof getPostsByLocale>>,
  key: 'tags' | 'categories',
  value: string
) => posts.filter((post) => post.data[key].map((item) => deslugify(item)).includes(deslugify(value)));
