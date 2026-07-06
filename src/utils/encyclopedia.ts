import type { CollectionEntry } from 'astro:content';

export function slugToTitle(slug: string): string {
  return slug
    .split('-')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

export function getEntryTitle(entry: CollectionEntry<'encyclopedia'>): string {
  if (entry.data.title) return entry.data.title;
  return slugToTitle(entry.id);
}

export function getSortKey(entry: CollectionEntry<'encyclopedia'>): string {
  const key = entry.data.sortTitle ?? getEntryTitle(entry);
  return key.toLowerCase();
}

export function getEntryLetter(entry: CollectionEntry<'encyclopedia'>): string {
  const first = getSortKey(entry).charAt(0).toUpperCase();
  return /[A-Z]/.test(first) ? first : '#';
}

export function groupByLetter(entries: CollectionEntry<'encyclopedia'>[]) {
  const groups = new Map<string, CollectionEntry<'encyclopedia'>[]>();

  for (const entry of entries) {
    const letter = getEntryLetter(entry);
    const list = groups.get(letter) ?? [];
    list.push(entry);
    groups.set(letter, list);
  }

  for (const list of groups.values()) {
    list.sort((a, b) => getSortKey(a).localeCompare(getSortKey(b)));
  }

  return groups;
}

export const INDEX_LETTERS = [
  ...'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
  '#',
] as const;

export function getRelatedEntries(
  entry: CollectionEntry<'encyclopedia'>,
  allEntries: CollectionEntry<'encyclopedia'>[],
  limit = 6,
): CollectionEntry<'encyclopedia'>[] {
  const byId = new Map(allEntries.map((e) => [e.id, e]));
  const related: CollectionEntry<'encyclopedia'>[] = [];
  const seen = new Set<string>([entry.id]);

  const relatedSlugs = entry.data.related ?? [];
  for (const slug of relatedSlugs) {
    const match = byId.get(slug);
    if (match && !seen.has(match.id)) {
      related.push(match);
      seen.add(match.id);
    }
  }

  if (entry.data.category) {
    for (const candidate of allEntries) {
      if (related.length >= limit) break;
      if (candidate.id === entry.id || seen.has(candidate.id)) continue;
      if (candidate.data.category === entry.data.category) {
        related.push(candidate);
        seen.add(candidate.id);
      }
    }
  }

  if (related.length < limit) {
    const neighbors = allEntries
      .filter((e) => e.id !== entry.id && !seen.has(e.id))
      .sort((a, b) => getSortKey(a).localeCompare(getSortKey(b)));

    for (const neighbor of neighbors) {
      if (related.length >= limit) break;
      related.push(neighbor);
      seen.add(neighbor.id);
    }
  }

  return related.slice(0, limit);
}
