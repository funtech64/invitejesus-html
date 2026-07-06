import type { CollectionEntry } from 'astro:content';
import positionsData from '../data/positions.json';

export type PositionMeta = (typeof positionsData.positions)[number];

export const POSITION_COUNT = 12;
export const POSITION_IDS = positionsData.positions.map((p) => p.id);

export function positionTag(id: string): string {
  return `position-${id.padStart(2, '0')}`;
}

export function getPositionMeta(id: string): PositionMeta | undefined {
  return positionsData.positions.find((p) => p.id === id);
}

export function getLogicIntro() {
  return positionsData.logic;
}

export function getEntriesForPosition(
  entries: CollectionEntry<'encyclopedia'>[],
  positionId: string,
): CollectionEntry<'encyclopedia'>[] {
  const tag = positionTag(positionId);
  return entries
    .filter((entry) => !entry.data.draft && entry.data.tags?.includes(tag))
    .sort((a, b) => {
      const titleA = a.data.sortTitle ?? a.data.title ?? a.id;
      const titleB = b.data.sortTitle ?? b.data.title ?? b.id;
      return titleA.localeCompare(titleB);
    });
}

export function countEntriesByPosition(
  entries: CollectionEntry<'encyclopedia'>[],
): Map<string, number> {
  const counts = new Map<string, number>();
  for (const id of POSITION_IDS) {
    counts.set(id, getEntriesForPosition(entries, id).length);
  }
  return counts;
}
