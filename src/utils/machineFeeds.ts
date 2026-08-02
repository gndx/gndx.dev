import config from '@config/config.json';
import type { Locale } from '@i18n/config';
import { getPostsByLocale } from '@utils/i18nContent';
import { truncateSeoText } from '@utils/seo';

const localeMetadata: Record<Locale, { language: string; label: string; description: string }> = {
  es: {
    language: 'es',
    label: 'Español',
    description: 'Artículos de Oscar Barajas sobre JavaScript, React, inteligencia artificial, agentes de IA, desarrollo web y carrera profesional.'
  },
  en: {
    language: 'en',
    label: 'English',
    description: 'Articles by Oscar Barajas about JavaScript, React, artificial intelligence, AI agents, web development and tech careers.'
  },
  pt: {
    language: 'pt-BR',
    label: 'Português',
    description: 'Artigos de Oscar Barajas sobre JavaScript, React, inteligência artificial, agentes de IA, desenvolvimento web e carreira.'
  }
};

const getPostSlug = (post: { slug?: string; id: string }) =>
  post.slug || post.id.replace(/\.(md|mdx)$/i, '');

const getLocalePrefix = (locale: Locale) => (locale === 'es' ? '' : `/${locale}`);

const getPostUrl = (locale: Locale, slug: string) =>
  `${config.site.base_url}${getLocalePrefix(locale)}/blog/${slug}/`;

const getPostMarkdownUrl = (locale: Locale, slug: string) =>
  `${config.site.base_url}${getLocalePrefix(locale)}/blog/${slug}.md`;

const getAuthorUrl = (locale: Locale) =>
  `${config.site.base_url}${getLocalePrefix(locale)}/about/`;

const markdownToText = (markdown: string): string =>
  markdown
    .replace(/^\s*(?:import|export)\s.+$/gm, '')
    .replace(/```[^\n]*\n?/g, '')
    .replace(/!\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/<iframe[\s\S]*?<\/iframe>/gi, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/^\s{0,3}(?:#{1,6}|>|[-+*])\s+/gm, '')
    .replace(/[*_~`]/g, '')
    .replace(/[ \t]+/g, ' ')
    .replace(/\n{3,}/g, '\n\n')
    .trim();

export const createJsonFeed = async (locale: Locale) => {
  const posts = await getPostsByLocale(locale);
  const metadata = localeMetadata[locale];
  const prefix = getLocalePrefix(locale);

  return {
    version: 'https://jsonfeed.org/version/1.1',
    title: `${config.site.name} — ${metadata.label}`,
    home_page_url: `${config.site.base_url}${prefix}/`,
    feed_url: `${config.site.base_url}${prefix}/feed.json`,
    description: metadata.description,
    language: metadata.language,
    authors: [
      {
        name: config.author.name,
        url: getAuthorUrl(locale),
        avatar: new URL(config.author.avatar, config.site.base_url).toString()
      }
    ],
    items: posts.map((post) => {
      const slug = getPostSlug(post);
      const url = getPostUrl(locale, slug);
      const body = 'body' in post && typeof post.body === 'string' ? post.body : post.data.description;

      return {
        id: url,
        url,
        title: post.data.title,
        summary: post.data.description,
        content_text: markdownToText(body),
        date_published: post.data.pubDate.toISOString(),
        ...(post.data.updatedDate ? { date_modified: post.data.updatedDate.toISOString() } : {}),
        authors: [{ name: config.author.name, url: getAuthorUrl(locale) }],
        tags: [...new Set([...post.data.categories, ...post.data.tags])],
        image: `${config.site.base_url}/og${prefix}/blog/${slug}.png`,
        language: metadata.language,
        _markdown_url: getPostMarkdownUrl(locale, slug)
      };
    })
  };
};

const createArticleList = async (locale: Locale, limit?: number) => {
  const posts = await getPostsByLocale(locale);
  const selectedPosts = typeof limit === 'number' ? posts.slice(0, limit) : posts;

  return selectedPosts.map((post) => {
    const slug = getPostSlug(post);
    const summary = truncateSeoText(post.data.description, 180);
    return `- [${post.data.title}](${getPostUrl(locale, slug)}): ${summary} — [Markdown](${getPostMarkdownUrl(locale, slug)})`;
  });
};

type LocalizedPost = Awaited<ReturnType<typeof getPostsByLocale>>[number];

const yamlString = (value: string) => JSON.stringify(value);

export const createArticleMarkdown = (
  post: LocalizedPost,
  locale: Locale,
  slug: string
): string => {
  const canonical = getPostUrl(locale, slug);
  const body = 'body' in post && typeof post.body === 'string'
    ? post.body.trim()
    : post.data.description;
  const metadata = [
    '---',
    `title: ${yamlString(post.data.title)}`,
    `description: ${yamlString(post.data.description)}`,
    `author: ${yamlString(config.author.name)}`,
    `language: ${yamlString(localeMetadata[locale].language)}`,
    `canonical: ${yamlString(canonical)}`,
    `datePublished: ${yamlString(post.data.pubDate.toISOString())}`,
    `dateModified: ${yamlString((post.data.updatedDate || post.data.pubDate).toISOString())}`,
    `categories: ${JSON.stringify(post.data.categories)}`,
    `tags: ${JSON.stringify(post.data.tags)}`,
    '---'
  ];

  return [
    ...metadata,
    '',
    `# ${post.data.title}`,
    '',
    `> ${post.data.description}`,
    '',
    body,
    '',
    '---',
    '',
    `Fuente canónica: [${canonical}](${canonical})`,
    `Autor: [${config.author.name}](${getAuthorUrl(locale)})`
  ].join('\n');
};

export const createLlmsText = async (full = false): Promise<string> => {
  const articleLimit = full ? undefined : 12;
  const sections = await Promise.all(
    (['es', 'en', 'pt'] as Locale[]).map(async (locale) => {
      const articles = await createArticleList(locale, articleLimit);
      return [`## ${localeMetadata[locale].label}`, ...articles].join('\n');
    })
  );

  return [
    '# GNDX',
    '',
    '> Sitio oficial y blog personal de Oscar Barajas Tavares (@gndx), Software AI Engineer y educador tecnológico. Publica contenido en español, inglés y portugués sobre JavaScript, React, inteligencia artificial, agentes de IA y desarrollo web.',
    '',
    'Usa la URL canónica de cada artículo al citar información y atribuye la autoría a Oscar Barajas Tavares. Las fechas, títulos y resúmenes de los feeds son la referencia estructurada del sitio.',
    '',
    '## Fuentes estructuradas',
    '- [Sitemap XML](https://gndx.dev/sitemap-index.xml): URLs canónicas que el sitio recomienda indexar.',
    '- [RSS en español](https://gndx.dev/rss.xml): artículos y fechas de publicación.',
    '- [JSON Feed en español](https://gndx.dev/feed.json): contenido completo en formato legible por máquinas.',
    '- [RSS in English](https://gndx.dev/en/rss.xml): English articles and publication dates.',
    '- [JSON Feed in English](https://gndx.dev/en/feed.json): complete English content.',
    '- [RSS em português](https://gndx.dev/pt/rss.xml): artigos e datas de publicação.',
    '- [JSON Feed em português](https://gndx.dev/pt/feed.json): conteúdo completo em português.',
    ...(full
      ? []
      : ['- [Catálogo completo para agentes](https://gndx.dev/llms-full.txt): índice de todos los artículos en los tres idiomas.']),
    '',
    ...sections.flatMap((section) => [section, '']),
    '## Autor',
    '- [Perfil y trayectoria](https://gndx.dev/about/): biografía, experiencia, reconocimientos y áreas de trabajo.',
    '- [GitHub](https://github.com/gndx): proyectos y código público.',
    '- [YouTube](https://www.youtube.com/@gndx): contenido educativo en video.'
  ].join('\n');
};
