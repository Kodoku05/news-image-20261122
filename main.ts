// news-image-20261122 entry (Node 22, standard library only).
//
// The image is entry.png beside this file: a one-page newspaper front
// page summing up the world news of Sunday 22 November 2026, drawn by
// draw.py (PIL) from the verified stories in stories.py. The program
// copies it to /output/entry.png. Run locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// Verified 22 Nov 2026: two runs of main.ts produce byte-identical
// output matching entry.png (sha256 d04ffb16...).

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(
  new URL('./entry.png', import.meta.url),
  join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'),
);
