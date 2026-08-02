export const truncateSeoText = (value: string, maxLength: number): string => {
  const normalized = value.replace(/\s+/g, ' ').trim();
  if (normalized.length <= maxLength) return normalized;

  const candidate = normalized.slice(0, maxLength - 1);
  const lastSpace = candidate.lastIndexOf(' ');
  const safeCut = lastSpace >= Math.floor(maxLength * 0.65) ? lastSpace : candidate.length;
  return `${candidate.slice(0, safeCut).replace(/[,:;.!?\-–—]+$/u, '')}…`;
};
