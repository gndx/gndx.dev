import rss from '@astrojs/rss';
import config from '@config/config.json';
import { prefixedLocales, isLocale } from '@i18n/config';
import { getPostsByLocale } from '@utils/i18nContent';

export async function getStaticPaths() {
  return prefixedLocales.map((locale) => ({ params: { locale } }));
}

export async function GET(context) {
  const locale = context.params.locale;
  if (!isLocale(locale)) {
    return new Response('Not found', { status: 404 });
  }
  const posts = await getPostsByLocale(locale);

  return rss({
    title: `${config.site.title} (${locale.toUpperCase()})`,
    description: config.site.description,
    site: context.site,
    items: posts.map((post) => ({
      ...post.data,
      link: `/${locale}/blog/${post.slug || post.id.replace(/\.(md|mdx)$/i, '')}/`
    }))
  });
}
