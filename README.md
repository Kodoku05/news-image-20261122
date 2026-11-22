# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Kodoku05/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Kodoku05/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

The World Today — 22 November 2026: a program that sums up the world news
of Sunday 22 November 2026 as a one-page newspaper front page (a 1024×1024
PNG). Lead stories: COP31's final draft drops every mention of fossil fuels;
a third tanker burns at anchor off Khasab as Hormuz attacks mount; Bahrain
says an Iranian attack set an industrial site ablaze; Mexico captures
'El Chapo Isidro'; and a M7.2 quake strikes deep under Maluku. 50 stories
across 8 regions, every one dated 22 November 2026.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out node main.ts
```

Writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`). Node 22,
standard library only — the program just copies the image.

## How the image was made

`draw.py` (Python + Pillow, run locally) draws the front page from the
verified story data in `stories.py`: three illustrated leads, ten more
illustrated stories, a 37-story "Also" column, a "Why the strait is
burning" explainer, a dotted world map with story pins, and a date-check
box listing the big stories deliberately left out because they belong to
earlier days. The output is deterministic — two runs produce byte-identical
PNGs.

## Sources

Reuters, AP, AFP, UKMTO, BBC and Sunday round-ups, checked on 22 November
2026. Every story happened, or was first reported, on Sunday 22 November
2026. Illustrations are original flat-vector drawings, not photographs.
