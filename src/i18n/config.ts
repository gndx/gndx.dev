export const locales = ['es', 'en', 'pt'] as const;

export type Locale = (typeof locales)[number];

export const defaultLocale: Locale = 'es';
export const localeCookieName = 'lang';
export const prefixedLocales = locales.filter((locale) => locale !== defaultLocale);

const localeSet = new Set(locales);

export const isLocale = (value: string | undefined): value is Locale =>
  Boolean(value && localeSet.has(value as Locale));

export const stripLocaleFromPath = (pathname: string): string => {
  const segments = pathname.split('/').filter(Boolean);
  if (segments.length === 0) return '/';
  if (!isLocale(segments[0])) return pathname;
  const nextPath = `/${segments.slice(1).join('/')}`;
  return nextPath === '/' ? '/' : nextPath.replace(/\/$/, '') + '/';
};

export const withLocalePath = (locale: Locale, pathname = '/'): string => {
  const barePath = stripLocaleFromPath(pathname).replace(/^\//, '').replace(/\/$/, '');
  if (locale === defaultLocale) {
    return barePath ? `/${barePath}/` : '/';
  }
  return barePath ? `/${locale}/${barePath}/` : `/${locale}/`;
};

export const parseAcceptLanguage = (header: string | null): Locale => {
  if (!header) return defaultLocale;

  const ordered = header
    .split(',')
    .map((item) => {
      const [lang, quality = 'q=1'] = item.trim().split(';');
      const q = Number(quality.replace('q=', ''));
      return { lang: lang.toLowerCase(), q: Number.isNaN(q) ? 1 : q };
    })
    .sort((a, b) => b.q - a.q)
    .map((item) => item.lang);

  for (const lang of ordered) {
    if (lang.startsWith('es')) return 'es';
    if (lang.startsWith('en')) return 'en';
    if (lang.startsWith('pt')) return 'pt';
  }

  return defaultLocale;
};
