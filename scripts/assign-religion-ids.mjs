import { createHash } from 'node:crypto';
import { promises as fs } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve('src/content/encyclopedia');
const REGISTRY = path.resolve('src/data/religion-registry.json');
const ID_PATTERN = /^REL-(\d{3})$/;

async function walk(directory) {
  const entries = await fs.readdir(directory, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await walk(absolute));
    else if (entry.isFile() && entry.name.endsWith('.md')) files.push(absolute);
  }

  return files;
}

function relativePath(absolute) {
  return path.relative(ROOT, absolute).split(path.sep).join('/');
}

function setRelId(source, relId) {
  const newline = source.includes('\r\n') ? '\r\n' : '\n';
  const normalized = source.replace(/\r\n/g, '\n');
  let output;

  if (normalized.startsWith('---\n')) {
    const end = normalized.indexOf('\n---\n', 4);
    if (end === -1) throw new Error('Unclosed YAML frontmatter');

    const frontmatter = normalized.slice(4, end);
    const body = normalized.slice(end + 5);
    const lines = frontmatter.split('\n');
    const index = lines.findIndex((line) => /^relId\s*:/.test(line));

    if (index >= 0) lines[index] = `relId: ${relId}`;
    else lines.unshift(`relId: ${relId}`);

    output = `---\n${lines.join('\n')}\n---\n${body}`;
  } else {
    output = `---\nrelId: ${relId}\n---\n${normalized}`;
  }

  return newline === '\r\n' ? output.replace(/\n/g, '\r\n') : output;
}

function sha256(text) {
  return createHash('sha256').update(Buffer.from(text, 'utf8')).digest('hex');
}

async function readExistingRegistry() {
  try {
    const parsed = JSON.parse(await fs.readFile(REGISTRY, 'utf8'));
    return Array.isArray(parsed.entries) ? parsed.entries : [];
  } catch (error) {
    if (error.code === 'ENOENT') return [];
    throw error;
  }
}

const files = (await walk(ROOT)).sort((a, b) =>
  relativePath(a).localeCompare(relativePath(b), 'en', { sensitivity: 'base' })
);

const existingEntries = await readExistingRegistry();
const existingByPath = new Map(existingEntries.map((entry) => [entry.path, entry.id]));
const usedNumbers = new Set();

for (const id of existingByPath.values()) {
  const match = ID_PATTERN.exec(id);
  if (!match) throw new Error(`Invalid existing religion ID: ${id}`);
  usedNumbers.add(Number(match[1]));
}

function nextNumber() {
  for (let number = 1; number <= 999; number += 1) {
    if (!usedNumbers.has(number)) {
      usedNumbers.add(number);
      return number;
    }
  }
  throw new Error('REL namespace exhausted at REL-999');
}

const registryEntries = [];

for (const file of files) {
  const relative = relativePath(file);
  const existingId = existingByPath.get(relative);
  const relId = existingId ?? `REL-${String(nextNumber()).padStart(3, '0')}`;
  const original = await fs.readFile(file, 'utf8');
  const updated = setRelId(original, relId);

  if (updated !== original) await fs.writeFile(file, updated, 'utf8');

  registryEntries.push({
    id: relId,
    path: relative,
    sha256: sha256(updated),
  });
}

registryEntries.sort((a, b) => a.id.localeCompare(b.id));

const registry = {
  schemaVersion: 1,
  namespace: 'REL',
  hashAlgorithm: 'SHA-256',
  hashScope: 'Exact UTF-8 bytes of each canonical Markdown file after relId attribution',
  assignmentRule: 'Existing IDs are preserved. New IDs use the lowest unused number; the initial corpus is assigned by case-insensitive alphabetical path order.',
  sourceDirectory: 'src/content/encyclopedia',
  count: registryEntries.length,
  entries: registryEntries,
};

await fs.mkdir(path.dirname(REGISTRY), { recursive: true });
await fs.writeFile(REGISTRY, `${JSON.stringify(registry, null, 2)}\n`, 'utf8');

console.log(`Attributed and hashed ${registryEntries.length} religion Markdown files.`);
