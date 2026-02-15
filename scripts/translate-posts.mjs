import fs from 'node:fs/promises';
import path from 'node:path';
import yaml from 'js-yaml';

const ROOT = process.cwd();
const BLOG_DIR = path.join(ROOT, 'src/content/blog');
const ES_DIR = path.join(BLOG_DIR, 'es');
const EN_DIR = path.join(BLOG_DIR, 'en');
const PT_DIR = path.join(BLOG_DIR, 'pt');

const TARGETS = [
  { locale: 'en', dir: EN_DIR, lang: 'en' },
  { locale: 'pt', dir: PT_DIR, lang: 'pt' }
];

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function ensureDirs() {
  await fs.mkdir(ES_DIR, { recursive: true });
  await fs.mkdir(EN_DIR, { recursive: true });
  await fs.mkdir(PT_DIR, { recursive: true });
}

async function moveSpanishPosts() {
  const entries = await fs.readdir(BLOG_DIR, { withFileTypes: true });
  for (const entry of entries) {
    if (!entry.isFile()) continue;
    if (!entry.name.endsWith('.md') && !entry.name.endsWith('.mdx')) continue;
    const from = path.join(BLOG_DIR, entry.name);
    const to = path.join(ES_DIR, entry.name);
    await fs.rename(from, to);
  }
}

function splitFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!match) return { data: {}, body: content };
  return { data: yaml.load(match[1]) || {}, body: match[2] };
}

function toFrontmatter(data) {
  const text = yaml.dump(data, {
    forceQuotes: true,
    quotingType: "'",
    lineWidth: 120,
    noRefs: true
  });
  return `---\n${text}---\n\n`;
}

function chunkText(text, maxSize = 1200) {
  if (text.length <= maxSize) return [text];
  const parts = [];
  let current = '';
  const chunks = text.split(/\n\n+/);
  for (const item of chunks) {
    const candidate = current ? `${current}\n\n${item}` : item;
    if (candidate.length > maxSize && current) {
      parts.push(current);
      current = item;
    } else {
      current = candidate;
    }
  }
  if (current) parts.push(current);
  return parts;
}

async function translateChunk(chunk, target, attempt = 1) {
  try {
    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=es&tl=${target}&dt=t&q=${encodeURIComponent(chunk)}`;
    const res = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    return Array.isArray(data?.[0]) ? data[0].map((part) => part[0]).join('') : chunk;
  } catch (error) {
    if (attempt >= 4) throw error;
    await sleep(400 * attempt);
    return translateChunk(chunk, target, attempt + 1);
  }
}

async function translateWithGoogle(text, target) {
  if (!text.trim()) return text;
  const chunks = chunkText(text);
  const translated = [];
  for (const chunk of chunks) {
    translated.push(await translateChunk(chunk, target));
    await sleep(70);
  }
  return translated.join('\n\n');
}

function protectSegments(text) {
  const tokens = [];
  let value = text;
  const patterns = [
    /```[\s\S]*?```/g,
    /~~~[\s\S]*?~~~/g,
    /<[^>]+>/g,
    /`[^`]+`/g,
    /\{[^{}]+\}/g,
    /https?:\/\/[^\s)\]]+/g
  ];

  for (const pattern of patterns) {
    value = value.replace(pattern, (match) => {
      const token = `__TOKEN_${tokens.length}__`;
      tokens.push(match);
      return token;
    });
  }
  return { value, tokens };
}

function unprotectSegments(text, tokens) {
  let value = text;
  tokens.forEach((original, index) => {
    value = value.replaceAll(`__TOKEN_${index}__`, original);
  });
  return value;
}

async function translateMarkdownBody(body, target) {
  const blocks = body.split(/\n{2,}/);
  const out = [];

  for (const block of blocks) {
    const trimmed = block.trim();
    if (!trimmed) {
      out.push(block);
      continue;
    }

    if (trimmed.startsWith('import ') || trimmed.startsWith('export ')) {
      out.push(block);
      continue;
    }

    const { value, tokens } = protectSegments(block);
    const translated = await translateWithGoogle(value, target);
    out.push(unprotectSegments(translated, tokens));
  }

  return out.join('\n\n');
}

async function translatePostFile(filename) {
  const sourcePath = path.join(ES_DIR, filename);
  const sourceContent = await fs.readFile(sourcePath, 'utf8');
  const { data, body } = splitFrontmatter(sourceContent);

  for (const target of TARGETS) {
    const outPath = path.join(target.dir, filename);

    let shouldSkip = false;
    try {
      await fs.access(outPath);
      shouldSkip = true;
    } catch {
      shouldSkip = false;
    }

    if (shouldSkip) {
      console.log(`Skip ${filename} -> ${target.locale}`);
      continue;
    }

    const outData = { ...data };
    if (typeof outData.title === 'string') outData.title = await translateWithGoogle(outData.title, target.lang);
    if (typeof outData.description === 'string') outData.description = await translateWithGoogle(outData.description, target.lang);

    if (Array.isArray(outData.categories)) {
      outData.categories = await Promise.all(outData.categories.map((item) => translateWithGoogle(String(item), target.lang)));
    }

    if (Array.isArray(outData.tags)) {
      outData.tags = await Promise.all(outData.tags.map((item) => translateWithGoogle(String(item), target.lang)));
    }

    const translatedBody = await translateMarkdownBody(body, target.lang);
    const finalContent = toFrontmatter(outData) + translatedBody + '\n';
    await fs.writeFile(outPath, finalContent, 'utf8');
    console.log(`Translated ${filename} -> ${target.locale}`);
  }
}

async function main() {
  await ensureDirs();
  await moveSpanishPosts();

  const files = (await fs.readdir(ES_DIR))
    .filter((name) => name.endsWith('.md') || name.endsWith('.mdx'))
    .sort();

  for (const file of files) {
    await translatePostFile(file);
  }

  console.log(`Done. Processed ${files.length} posts.`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
