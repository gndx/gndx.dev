import type { APIRoute } from 'astro';
import { locales, withLocalePath } from '@i18n/config';
import { getPostsByLocale } from '@utils/i18nContent';
import { markdownToText } from '@utils/machineFeeds';

export const prerender = true;

export const GET: APIRoute = async () => {
  const postsByLocale = await Promise.all(locales.map(async (locale) => {
    const posts = await getPostsByLocale(locale);
    return posts.map(({ slug, id, data, body }) => ({
      url: withLocalePath(locale, `/blog/${slug || id.replace(/\.(md|mdx)$/i, '')}`),
      locale,
      title: data.title,
      description: data.description,
      keywords: [...data.tags, ...data.categories].join(' '),
      body: markdownToText(body ?? '')
    }));
  }));

  return Response.json(postsByLocale.flat());
};
