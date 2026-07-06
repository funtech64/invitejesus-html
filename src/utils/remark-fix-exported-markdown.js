/**
 * Remark plugin: fix exported markdown where the first line is `text# Title`
 * instead of a proper `# Title` heading. Does not modify source files.
 */
import { visit } from 'unist-util-visit';

export function fixExportedMarkdown() {
  return function transform(tree) {
    let fixed = false;

    visit(tree, 'paragraph', (node, index, parent) => {
      if (fixed || index !== 0 || !parent || typeof index !== 'number') return;

      const first = node.children?.[0];
      if (first?.type !== 'text' || typeof first.value !== 'string') return;

      const match = first.value.match(/^text#\s+(.+)$/);
      if (!match) return;

      parent.children[index] = {
        type: 'heading',
        depth: 1,
        children: [{ type: 'text', value: match[1] }],
      };
      fixed = true;
    });
  };
}
