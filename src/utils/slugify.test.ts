import { describe, expect, it } from 'vitest';
import { slugify } from './slugify';

describe('slugify', () => {
  it('lowercases and replaces spaces with hyphens', () => {
    expect(slugify('Hola Mundo')).toBe('hola-mundo');
  });

  it('removes punctuation and collapses hyphens', () => {
    expect(slugify('  Hello,   world!!!  ')).toBe('hello-world');
  });

  it('trims hyphens', () => {
    expect(slugify('---A---B---')).toBe('a-b');
  });
});
