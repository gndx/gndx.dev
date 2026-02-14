import type { Locale } from './config';

export const ui = {
  es: {
    nav: { home: 'Inicio', about: 'Acerca', stack: 'Stack', courses: 'Cursos', mentoring: 'Mentoria' },
    labels: {
      blog: 'Blog',
      tags: 'Tags',
      categories: 'Categorias',
      viewAll: 'Ver todos',
      scheduleSession: 'Agendar una sesion',
      tagPrefix: 'Tag',
      categoryPrefix: 'Categoria',
      postsWithTag: 'Ver posts con el tag',
      postsWithCategory: 'Ver posts con la categoria'
    }
  },
  en: {
    nav: { home: 'Home', about: 'About', stack: 'Stack', courses: 'Courses', mentoring: 'Mentoring' },
    labels: {
      blog: 'Blog',
      tags: 'Tags',
      categories: 'Categories',
      viewAll: 'View all',
      scheduleSession: 'Book a session',
      tagPrefix: 'Tag',
      categoryPrefix: 'Category',
      postsWithTag: 'View posts with tag',
      postsWithCategory: 'View posts with category'
    }
  },
  pt: {
    nav: { home: 'Inicio', about: 'Sobre', stack: 'Stack', courses: 'Cursos', mentoring: 'Mentoria' },
    labels: {
      blog: 'Blog',
      tags: 'Tags',
      categories: 'Categorias',
      viewAll: 'Ver todos',
      scheduleSession: 'Agendar sessao',
      tagPrefix: 'Tag',
      categoryPrefix: 'Categoria',
      postsWithTag: 'Ver posts com a tag',
      postsWithCategory: 'Ver posts com a categoria'
    }
  }
} as const;

export const getUi = (locale: Locale) => ui[locale];
