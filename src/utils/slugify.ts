export function slugify(input: string): string {
  return input
    .trim()
    .toLowerCase()
    // replace whitespace with hyphens
    .replace(/\s+/g, '-')
    // remove non-url-safe chars (keep letters, numbers, hyphens)
    .replace(/[^a-z0-9-]/g, '')
    // collapse multiple hyphens
    .replace(/-+/g, '-')
    // trim hyphens
    .replace(/^-+|-+$/g, '');
}
