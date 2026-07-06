#!/usr/bin/env node
/**
 * Prepends minimal YAML frontmatter to encyclopedia files that lack it.
 * Does not alter article body lines — only inserts a header block when missing.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const ENC_DIR = path.join(ROOT, 'src', 'content', 'encyclopedia');

function slugToTitle(slug) {
  return slug
    .split('-')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function extractTitle(content, slug) {
  const firstLine = content.split('\n')[0] ?? '';
  const match = firstLine.match(/^text#\s+(.+)$/) || firstLine.match(/^#\s+(.+)$/);
  return match ? match[1].trim() : slugToTitle(slug);
}

function yamlString(value) {
  return JSON.stringify(value);
}

let updated = 0;
let skipped = 0;

for (const file of fs.readdirSync(ENC_DIR).sort()) {
  if (!file.endsWith('.md')) continue;

  const filePath = path.join(ENC_DIR, file);
  const content = fs.readFileSync(filePath, 'utf8');

  if (content.startsWith('---')) {
    skipped += 1;
    continue;
  }

  const slug = file.replace(/\.md$/, '');
  const title = extractTitle(content, slug);
  const frontmatter = [
    '---',
    `title: ${yamlString(title)}`,
    `slug: ${yamlString(slug)}`,
    '---',
    '',
  ].join('\n');

  fs.writeFileSync(filePath, frontmatter + content, 'utf8');
  updated += 1;
}

console.log(`ensure-frontmatter: ${updated} updated, ${skipped} already had frontmatter`);
