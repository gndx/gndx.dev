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
  const descriptions = {
    es: config.site.description,
    en: 'Articles by Oscar Barajas about JavaScript, React, artificial intelligence, AI agents, web development and tech careers.',
    pt: 'Artigos de Oscar Barajas sobre JavaScript, React, inteligência artificial, agentes de IA, desenvolvimento web e carreira.'
  };

  return rss({
    title: `${config.site.title} (${locale.toUpperCase()})`,
    description: descriptions[locale],
    site: context.site,
    customData: `<language>${locale === 'pt' ? 'pt-BR' : locale}</language>`,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.pubDate,
      categories: [...post.data.categories, ...post.data.tags],
      link: `/${locale}/blog/${post.slug || post.id.replace(/\.(md|mdx)$/i, '')}/`
    }))
  });
}
