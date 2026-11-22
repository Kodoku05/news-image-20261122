#!/usr/bin/env python3
"""Draw the 22 November 2026 world-news broadsheet (1024x1024 PNG).

Deterministic: fixed palette, fixed fonts, no timestamps, no randomness.
Run:  python3 draw.py            -> writes entry.png next to this file.
The graded program (main.ts) only copies entry.png; this generator is the
human-readable record of how the image was drawn, run locally in-session.
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import stories

W, H = 1024, 1024
MARGIN = 22
CREAM = (246, 241, 231)
INK = (26, 26, 26)
RED = (179, 27, 27)
NAVY = (31, 42, 68)
GREY = (110, 108, 100)
RULE = (60, 60, 60)

FONT_DIR = "/usr/share/fonts/truetype"


def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


SERIF_B = "liberation/LiberationSerif-Bold.ttf"
SERIF = "liberation/LiberationSerif-Regular.ttf"
SANS_B = "liberation/LiberationSans-Bold.ttf"
SANS = "liberation/LiberationSans-Regular.ttf"
SANS_I = "liberation/LiberationSans-Italic.ttf"

F_KICKER = font(SANS_B, 13)
F_TITLE = font(SERIF_B, 57)
F_SUB = font(SERIF, 15)
F_STAT_N = font(SANS_B, 25)
F_STAT_L = font(SANS, 10)
F_REGION = font(SANS_B, 10)
F_TAG = font(SANS_B, 11)
F_TAG_S = font(SANS_B, 9)
F_PLACE = font(SANS_B, 10)
F_PLACE_S = font(SANS_B, 9)
F_HEAD = font(SANS_B, 17)
F_HEAD_S = font(SANS_B, 12)
F_DEK = font(SANS, 11)
F_DEK_S = font(SANS, 10)
F_WHY_T = font(SANS_B, 13)
F_WHY = font(SANS, 11)
F_ALSO_H = font(SANS_B, 13)
F_ALSO = font(SANS, 11)
F_ALSO_N = font(SANS_B, 11)
F_MAP_T = font(SANS_B, 11)
F_DC_T = font(SANS_B, 11)
F_DC = font(SANS, 10)
F_FOOT = font(SANS, 10)
F_PIN = font(SANS_B, 8)


def clean(text):
    """Swap glyphs the Liberation fonts lack for safe equivalents."""
    return text.replace("\u2212", "-").replace("\u00a0", " ")


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = clean(text).split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text(draw, xy, s, fnt, fill=INK, anchor="la"):
    draw.text(xy, clean(s), font=fnt, fill=fill, anchor=anchor)


# --------------------------------------------------------------------------
# Dotted world map: rough continent polygons (lon, lat), sampled on a grid.
# --------------------------------------------------------------------------

CONTINENTS = [
    # North America
    [(-168, 66), (-150, 70), (-130, 71), (-115, 73), (-100, 72), (-90, 70),
     (-82, 72), (-70, 62), (-60, 55), (-55, 52), (-62, 45), (-70, 42),
     (-76, 36), (-80, 26), (-86, 30), (-90, 21), (-97, 26), (-105, 22),
     (-110, 28), (-116, 32), (-122, 40), (-126, 48), (-132, 56),
     (-150, 60), (-162, 58)],
    # South America
    [(-80, 10), (-72, 12), (-62, 9), (-52, 4), (-44, -3), (-35, -8),
     (-39, -16), (-42, -23), (-48, -28), (-54, -34), (-60, -39),
     (-66, -47), (-69, -53), (-72, -44), (-73, -32), (-70, -20),
     (-76, -13), (-80, -5)],
    # Europe
    [(-10, 36), (-9, 43), (-3, 48), (-5, 50), (0, 51), (4, 53), (7, 57),
     (10, 59), (18, 56), (21, 55), (24, 59), (28, 61), (31, 69), (40, 68),
     (45, 60), (42, 52), (38, 47), (31, 45), (28, 41), (24, 36), (20, 40),
     (16, 44), (12, 45), (8, 44), (3, 42), (-2, 37)],
    # Africa
    [(-6, 35), (10, 37), (20, 32), (32, 31), (35, 28), (39, 21), (43, 12),
     (48, 11), (51, 12), (45, 2), (40, -8), (36, -18), (33, -26), (28, -33),
     (20, -35), (16, -29), (12, -18), (13, -8), (9, 4), (2, 6), (-8, 5),
     (-13, 8), (-17, 15), (-16, 22), (-10, 30)],
    # Asia (mainland)
    [(30, 70), (45, 68), (60, 70), (75, 73), (90, 75), (110, 74), (130, 72),
     (150, 70), (170, 67), (178, 65), (170, 60), (160, 55), (150, 45),
     (142, 40), (140, 35), (130, 33), (127, 40), (122, 38), (120, 30),
     (110, 20), (108, 12), (105, 8), (100, 7), (98, 12), (95, 16), (92, 22),
     (88, 22), (85, 18), (80, 15), (77, 8), (75, 12), (72, 20), (68, 23),
     (65, 25), (60, 25), (55, 26), (50, 29), (48, 30), (44, 29), (40, 32),
     (36, 36), (32, 38), (30, 42), (28, 45), (30, 50), (35, 55), (40, 60),
     (35, 65)],
    # Australia
    [(113, -22), (114, -30), (118, -35), (125, -33), (130, -32), (135, -35),
     (140, -38), (145, -38), (150, -37), (153, -30), (153, -25), (150, -22),
     (146, -19), (142, -15), (142, -11), (137, -12), (132, -12), (126, -14),
     (122, -17), (118, -20)],
    # Indonesia / New Guinea blobs
    [(95, 6), (100, 2), (105, -4), (106, -6), (102, -6), (98, 0), (95, 4)],
    [(106, -6), (112, -7), (114, -8), (110, -8), (106, -7)],
    [(109, 1), (114, 3), (118, 0), (117, -3), (112, -3), (109, -1)],
    [(131, -1), (137, -2), (141, -3), (146, -6), (147, -9), (141, -8),
     (136, -7), (131, -4)],
    # Japan
    [(130, 31), (133, 34), (137, 35), (140, 38), (141, 42), (144, 44),
     (142, 40), (139, 36), (135, 33), (131, 32)],
    # New Zealand
    [(167, -45), (170, -43), (173, -39), (176, -38), (178, -38), (175, -41),
     (171, -44), (168, -47)],
    # United Kingdom
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (1, 52), (0, 50)],
    # Madagascar
    [(44, -16), (47, -15), (50, -16), (48, -22), (45, -25), (44, -21)],
]


def inside_poly(lon, lat, poly):
    """Ray-casting point-in-polygon test."""
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > lat) != (yj > lat):
            x_at = (xj - xi) * (lat - yi) / (yj - yi) + xi
            if lon < x_at:
                inside = not inside
        j = i
    return inside


def draw_dot_map(draw, x0, y0, w, h):
    """Dotted continents in a box; returns a lon/lat -> pixel projector."""
    lon_min, lon_max = -180.0, 180.0
    lat_min, lat_max = -60.0, 82.0

    def proj(lon, lat):
        px = x0 + (lon - lon_min) / (lon_max - lon_min) * w
        py = y0 + (lat_max - lat) / (lat_max - lat_min) * h
        return px, py

    step = 2.6
    lon = lon_min
    while lon <= lon_max:
        lat = lat_min
        while lat <= lat_max:
            for poly in CONTINENTS:
                if inside_poly(lon, lat, poly):
                    px, py = proj(lon, lat)
                    draw.ellipse([px - 1.5, py - 1.5, px + 1.5, py + 1.5],
                                 fill=(70, 110, 150))
                    break
            lat += step
        lon += step
    return proj


def draw_pin(draw, proj, lon, lat, num):
    px, py = proj(lon, lat)
    r = 7
    draw.ellipse([px - r, py - r, px + r, py + r], fill=RED,
                 outline=(255, 255, 255), width=1)
    label = str(num)
    tw = draw.textlength(label, font=F_PIN)
    draw.text((px - tw / 2, py - 5), label, font=F_PIN, fill=(255, 255, 255))


# --------------------------------------------------------------------------
# Flat-vector illustrations, one per lead/grid story. Each draws inside
# the box (x, y, w, h) given to it.
# --------------------------------------------------------------------------

def ill_cop31(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(198, 226, 216))
    cx, cy, r = x + w * 0.38, y + h * 0.52, min(w, h) * 0.36
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 130, 200))
    d.ellipse([cx - r * 0.55, cy - r * 0.5, cx + r * 0.1, cy + r * 0.05],
              fill=(110, 190, 110))
    d.ellipse([cx + r * 0.05, cy + r * 0.25, cx + r * 0.6, cy + r * 0.7],
              fill=(110, 190, 110))
    # Thermometer, mercury high.
    tx = x + w * 0.78
    d.rectangle([tx - 7, y + h * 0.16, tx + 7, y + h * 0.80], fill=(255, 255, 255),
                outline=INK, width=2)
    d.rectangle([tx - 5, y + h * 0.24, tx + 5, y + h * 0.78], fill=RED)
    d.ellipse([tx - 13, y + h * 0.74, tx + 13, y + h * 0.94], fill=RED,
              outline=INK, width=2)
    # Big red zero: fossil fuels mentioned zero times.
    d.ellipse([x + w * 0.60, y + h * 0.06, x + w * 0.60 + 34, y + h * 0.06 + 34],
              fill=RED)
    d.text((x + w * 0.60 + 10, y + h * 0.06 + 5), "0", font=font(SANS_B, 22),
           fill=(255, 255, 255))


def ill_hormuz(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 32, 64))
    for i in range(14):  # stars
        sx = x + (i * 37) % w
        sy = y + (i * 23) % int(h * 0.4)
        d.ellipse([sx, sy, sx + 2, sy + 2], fill=(255, 255, 220))
    d.rectangle([x, y + h * 0.62, x + w, y + h], fill=(20, 70, 120))
    for i in range(6):  # waves
        wx = x + i * (w // 6) + 8
        d.arc([wx, y + h * 0.78, wx + 26, y + h * 0.92], 180, 360,
              fill=(150, 200, 240), width=2)
    # Tanker hull and fire.
    hx, hy = x + w * 0.12, y + h * 0.50
    d.polygon([(hx, hy), (hx + w * 0.72, hy), (hx + w * 0.66, hy + h * 0.18),
               (hx + w * 0.06, hy + h * 0.18)], fill=(40, 40, 40))
    d.rectangle([hx + w * 0.55, hy - h * 0.14, hx + w * 0.66, hy],
                fill=(220, 220, 220))
    fx = hx + w * 0.30
    d.polygon([(fx, hy - h * 0.30), (fx + 14, hy - h * 0.05),
               (fx + 28, hy - h * 0.30), (fx + 22, hy), (fx + 6, hy)],
              fill=(255, 140, 0))
    d.polygon([(fx + 8, hy - h * 0.18), (fx + 16, hy - h * 0.02),
               (fx + 24, hy - h * 0.18), (fx + 20, hy), (fx + 12, hy)],
              fill=(255, 220, 60))
    d.ellipse([fx + 2, hy - h * 0.40, fx + 14, hy - h * 0.30], fill=(90, 90, 90))
    d.ellipse([fx + 12, hy - h * 0.48, fx + 26, hy - h * 0.36],
              fill=(110, 110, 110))


def ill_bahrain(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(12, 16, 40))
    d.ellipse([x + w * 0.78, y + h * 0.08, x + w * 0.78 + 22, y + h * 0.08 + 22],
              fill=(240, 240, 200))
    # Skyline.
    heights = [0.42, 0.55, 0.36, 0.62, 0.48, 0.58, 0.40]
    bw = w / len(heights)
    for i, hh in enumerate(heights):
        bx = x + i * bw
        by = y + h * (1 - hh)
        d.rectangle([bx + 2, by, bx + bw - 2, y + h], fill=(45, 55, 85))
        for wy in range(3):
            d.rectangle([bx + 6, by + 8 + wy * 12, bx + 12, by + 14 + wy * 12],
                        fill=(255, 220, 120))
    # Interceptor arcs and a burst.
    d.arc([x + w * 0.10, y - h * 0.30, x + w * 0.70, y + h * 0.55], 200, 330,
          fill=(255, 180, 60), width=3)
    d.arc([x + w * 0.30, y - h * 0.10, x + w * 0.95, y + h * 0.60], 210, 320,
          fill=(255, 220, 120), width=2)
    bx, by = x + w * 0.55, y + h * 0.18
    for dx, dy in [(0, -12), (0, 12), (-12, 0), (12, 0), (-9, -9), (9, -9),
                   (-9, 9), (9, 9)]:
        d.line([bx, by, bx + dx, by + dy], fill=(255, 200, 80), width=3)
    d.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(255, 240, 180))


def ill_mexico(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 200, 140))
    d.polygon([(x, y + h * 0.55), (x + w * 0.25, y + h * 0.25),
               (x + w * 0.5, y + h * 0.55)], fill=(170, 120, 70))
    d.polygon([(x + w * 0.4, y + h * 0.55), (x + w * 0.65, y + h * 0.18),
               (x + w * 0.9, y + h * 0.55)], fill=(150, 105, 60))
    d.rectangle([x, y + h * 0.55, x + w, y + h], fill=(210, 170, 100))
    d.rectangle([x, y + h * 0.72, x + w, y + h * 0.82], fill=(90, 90, 90))
    # Police star badge.
    cx, cy = x + w * 0.72, y + h * 0.38
    r = max(9.0, min(20.0, h * 0.30))
    pts = []
    for i in range(10):
        ang = -90 + i * 36
        rr = r if i % 2 == 0 else r * 0.45
        import math
        pts.append((cx + rr * math.cos(math.radians(ang)),
                    cy + rr * math.sin(math.radians(ang))))
    d.polygon(pts, fill=(255, 215, 0), outline=(120, 90, 0))
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(30, 60, 140))


def ill_iraq(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(215, 205, 185))
    # Cooling towers.
    for tx in (0.18, 0.48):
        bx = x + w * tx
        d.polygon([(bx, y + h * 0.85), (bx + 8, y + h * 0.30),
                   (bx + 34, y + h * 0.30), (bx + 42, y + h * 0.85)],
                  fill=(170, 165, 150), outline=(90, 85, 75))
        d.ellipse([bx - 4, y + h * 0.14, bx + 14, y + h * 0.30], fill=(140, 140, 140))
        d.ellipse([bx + 8, y + h * 0.06, bx + 28, y + h * 0.22], fill=(160, 160, 160))
    # Flames at the base of the second tower.
    fx = x + w * 0.62
    d.polygon([(fx, y + h * 0.85), (fx + 10, y + h * 0.55),
               (fx + 20, y + h * 0.85)], fill=(255, 140, 0))
    d.polygon([(fx + 6, y + h * 0.85), (fx + 13, y + h * 0.66),
               (fx + 20, y + h * 0.85)], fill=(255, 220, 60))
    d.rectangle([x, y + h * 0.85, x + w, y + h], fill=(120, 110, 95))


def ill_peru(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 220, 235))
    d.polygon([(x, y + h), (x + w * 0.3, y + h * 0.25), (x + w * 0.55, y + h)],
              fill=(110, 130, 150))
    d.polygon([(x + w * 0.3, y + h * 0.25), (x + w * 0.4, y + h * 0.38),
               (x + w * 0.2, y + h * 0.38)], fill=(255, 255, 255))
    d.polygon([(x + w * 0.45, y + h), (x + w * 0.72, y + h * 0.15),
               (x + w, y + h)], fill=(90, 110, 135))
    d.polygon([(x + w * 0.72, y + h * 0.15), (x + w * 0.8, y + h * 0.30),
               (x + w * 0.64, y + h * 0.30)], fill=(255, 255, 255))
    # Seismograph strip.
    d.rectangle([x + w * 0.06, y + h * 0.66, x + w * 0.94, y + h * 0.90],
                fill=(255, 255, 255), outline=INK, width=1)
    pts = []
    import math
    for i in range(40):
        px = x + w * 0.08 + i * (w * 0.84 / 39)
        amp = 2 + (9 if 14 <= i <= 24 else 0)
        py = y + h * 0.78 + amp * math.sin(i * 1.7)
        pts.append((px, py))
    d.line(pts, fill=RED, width=2)


def ill_maluku(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(170, 215, 230))
    # Island.
    d.ellipse([x + w * 0.18, y + h * 0.42, x + w * 0.82, y + h * 0.72],
              fill=(90, 160, 90))
    d.polygon([(x + w * 0.42, y + h * 0.48), (x + w * 0.52, y + h * 0.22),
               (x + w * 0.62, y + h * 0.48)], fill=(70, 130, 70))
    # Sea + seismic rings.
    d.rectangle([x, y + h * 0.72, x + w, y + h], fill=(40, 110, 170))
    cx, cy = x + w * 0.5, y + h * 0.80
    for r in (h * 0.14, h * 0.28, h * 0.42):
        d.ellipse([cx - r, cy - r * 0.45, cx + r, cy + r * 0.45],
                  outline=(255, 255, 255), width=2)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)


def ill_ebola(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(225, 240, 235))
    s = h / 60.0
    # Microscope-ish: slide + virus circles.
    d.rectangle([x + w * 0.12, y + h * 0.62, x + w * 0.88, y + h * 0.70],
                fill=(200, 200, 200), outline=INK, width=1)
    for (vx, vy, vr) in [(0.28, 0.38, 13), (0.55, 0.30, 10), (0.72, 0.45, 8)]:
        vr = vr * s
        cx, cy = x + w * vx, y + h * vy
        for ang in range(0, 360, 45):
            import math
            ex = cx + (vr + 4) * math.cos(math.radians(ang))
            ey = cy + (vr + 4) * math.sin(math.radians(ang))
            d.line([cx, cy, ex, ey], fill=(160, 40, 40), width=2)
        d.ellipse([cx - vr, cy - vr, cx + vr, cy + vr], fill=(200, 80, 80),
                  outline=(140, 30, 30), width=2)
    # Medical cross.
    cx, cy = x + w * 0.80, y + h * 0.78
    d.rectangle([cx - 3, cy - 9, cx + 3, cy + 9], fill=(30, 140, 70))
    d.rectangle([cx - 9, cy - 3, cx + 9, cy + 3], fill=(30, 140, 70))


def ill_manipur(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 220, 200))
    # Bottle, all heights proportional to the box.
    bx, by = x + w * 0.30, y + h * 0.12
    neck = h * 0.18
    d.rectangle([bx + 12, by, bx + 24, by + neck], fill=(60, 120, 60))
    d.polygon([(bx + 12, by + neck), (bx + 24, by + neck),
               (bx + 30, by + neck + h * 0.14), (bx + 6, by + neck + h * 0.14)],
              fill=(90, 150, 90))
    body_top = by + neck + h * 0.14
    d.rectangle([bx + 2, body_top, bx + 34, y + h * 0.82], fill=(110, 170, 110),
                outline=(40, 90, 40), width=2)
    d.rectangle([bx + 2, y + h * 0.60, bx + 34, y + h * 0.82], fill=(70, 120, 70))
    # Skull-and-crossbones sign.
    cx, cy = x + w * 0.72, y + h * 0.45
    r = max(8.0, h * 0.22)
    d.ellipse([cx - r, cy - r, cx + r, cy + r * 0.7], fill=(255, 255, 255),
              outline=INK, width=2)
    d.ellipse([cx - r * 0.55, cy - r * 0.4, cx - r * 0.15, cy + r * 0.05],
              fill=INK)
    d.ellipse([cx + r * 0.15, cy - r * 0.4, cx + r * 0.55, cy + r * 0.05],
              fill=INK)
    d.line([cx - r, cy + r * 0.95, cx + r, cy + r * 1.35], fill=INK, width=3)
    d.line([cx - r, cy + r * 1.35, cx + r, cy + r * 0.95], fill=INK, width=3)


def ill_myanmar(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 225, 170))
    # Pagoda silhouette, scaled to the box.
    cx = x + w * 0.5
    base = y + h * 0.88
    d.rectangle([cx - w * 0.17, base - h * 0.08, cx + w * 0.17, base],
                fill=(150, 110, 50))
    for i, ww in enumerate((0.28, 0.22, 0.16, 0.10)):
        ty = base - h * 0.14 - i * h * 0.14
        half = w * ww / 2
        d.polygon([(cx - half, ty), (cx + half, ty),
                   (cx + half - 5, ty - h * 0.09),
                   (cx - half + 5, ty - h * 0.09)], fill=(180, 135, 60))
    d.polygon([(cx - 2, base - h * 0.62), (cx + 2, base - h * 0.62),
               (cx, base - h * 0.78)], fill=(200, 160, 70))
    # Red "unfair" stamp: circle + slash.
    sx, sy = x + w * 0.80, y + h * 0.26
    r = max(8.0, h * 0.22)
    d.ellipse([sx - r, sy - r, sx + r, sy + r], outline=RED, width=3)
    d.line([sx - r * 0.7, sy + r * 0.7, sx + r * 0.7, sy - r * 0.7],
           fill=RED, width=3)


def ill_aukus(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 90, 140))
    for i in range(5):  # bubbles
        bx = x + w * (0.15 + i * 0.18)
        by = y + h * (0.25 + (i % 2) * 0.12)
        d.ellipse([bx - 3, by - 3, bx + 3, by + 3], outline=(200, 230, 255),
                  width=1)
    # Submarine, scaled to the box.
    cx, cy = x + w * 0.5, y + h * 0.55
    hh = h * 0.28
    d.ellipse([cx - w * 0.30, cy - hh, cx + w * 0.30, cy + hh],
              fill=(50, 60, 70))
    d.rectangle([cx - w * 0.09, cy - hh - h * 0.18, cx + w * 0.05, cy - hh + 2],
                fill=(50, 60, 70))
    d.rectangle([cx + w * 0.27, cy - hh * 0.7, cx + w * 0.33, cy - hh * 0.1],
                fill=(50, 60, 70))
    for fx in (-0.20, -0.11, -0.02, 0.07, 0.16):
        px = cx + w * fx
        d.ellipse([px - 3, cy - 3, px + 3, cy + 3], fill=(180, 220, 240))
    d.rectangle([x, y + h * 0.85, x + w, y + h], fill=(150, 130, 90))


def ill_geneva(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(220, 225, 235))
    # Robot, scaled to the box.
    cx, cy = x + w * 0.42, y + h * 0.52
    u = h / 46.0
    d.rectangle([cx - 18 * u, cy - 26 * u, cx + 18 * u, cy - 6 * u],
                fill=(120, 130, 145), outline=INK, width=1)
    d.ellipse([cx - 10 * u, cy - 20 * u, cx - 4 * u, cy - 14 * u],
              fill=(255, 80, 80))
    d.ellipse([cx + 4 * u, cy - 20 * u, cx + 10 * u, cy - 14 * u],
              fill=(255, 80, 80))
    d.rectangle([cx - 24 * u, cy - 2 * u, cx + 24 * u, cy + 26 * u],
                fill=(150, 160, 175), outline=INK, width=1)
    d.rectangle([cx - 30 * u, cy - 2 * u, cx - 24 * u, cy + 18 * u],
                fill=(120, 130, 145))
    d.rectangle([cx + 24 * u, cy - 2 * u, cx + 30 * u, cy + 18 * u],
                fill=(120, 130, 145))
    d.rectangle([cx - 14 * u, cy + 26 * u, cx - 4 * u, cy + 40 * u],
                fill=(120, 130, 145))
    d.rectangle([cx + 4 * u, cy + 26 * u, cx + 14 * u, cy + 40 * u],
                fill=(120, 130, 145))
    # Prohibition sign over it.
    px, py = x + w * 0.76, y + h * 0.30
    r = max(9.0, h * 0.28)
    d.ellipse([px - r, py - r, px + r, py + r], outline=RED, width=4)
    d.line([px - r * 0.7, py + r * 0.7, px + r * 0.7, py - r * 0.7],
           fill=RED, width=4)


def ill_atp(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(40, 110, 70))
    # Court lines (top view, skewed).
    d.rectangle([x + w * 0.14, y + h * 0.12, x + w * 0.86, y + h * 0.88],
                outline=(255, 255, 255), width=2)
    d.line([x + w * 0.14, y + h * 0.50, x + w * 0.86, y + h * 0.50],
           fill=(255, 255, 255), width=2)
    d.line([x + w * 0.50, y + h * 0.12, x + w * 0.50, y + h * 0.88],
           fill=(255, 255, 255), width=1)
    # Net.
    d.rectangle([x + w * 0.12, y + h * 0.47, x + w * 0.88, y + h * 0.53],
                fill=(20, 60, 35))
    # Ball + racket, scaled to the box.
    br = max(5.0, h * 0.16)
    bx, by = x + w * 0.70, y + h * 0.24
    d.ellipse([bx - br, by - br, bx + br, by + br], fill=(220, 230, 60),
              outline=(255, 255, 255), width=1)
    rx, ry = x + w * 0.24, y + h * 0.58
    rw, rh = max(6.0, w * 0.06), max(8.0, h * 0.28)
    d.ellipse([rx - rw, ry - rh, rx + rw, ry + rh], outline=(200, 170, 120),
              width=3)
    d.line([rx, ry + rh, rx - 6, ry + rh + h * 0.22], fill=(200, 170, 120),
           width=3)


ILLUSTRATIONS = {
    "cop31": ill_cop31,
    "hormuz": ill_hormuz,
    "bahrain": ill_bahrain,
    "mexico": ill_mexico,
    "iraq": ill_iraq,
    "peru": ill_peru,
    "maluku": ill_maluku,
    "ebola": ill_ebola,
    "manipur": ill_manipur,
    "myanmar": ill_myanmar,
    "aukus": ill_aukus,
    "geneva": ill_geneva,
    "atp": ill_atp,
}


# --------------------------------------------------------------------------
# Layout.
# --------------------------------------------------------------------------

def rule(d, x0, x1, y, width=1, fill=RULE):
    d.line([x0, y, x1, y], fill=fill, width=width)


def tag_bar(d, x, y, w, s, fnt=F_TAG):
    """Red tag bar sized to its text."""
    tw = d.textlength(clean(s), font=fnt) + 12
    d.rectangle([x, y, x + tw, y + fnt.size + 6], fill=RED)
    d.text((x + 6, y + 3), clean(s), font=fnt, fill=(255, 255, 255))
    return tw


def paste_illustration(img, key, x, y, w, h):
    """Render one illustration onto its own layer, then paste it clipped
    to its box, so no drawing can spill into neighbouring sections."""
    tmp = Image.new("RGB", (int(round(w)), int(round(h))), CREAM)
    td = ImageDraw.Draw(tmp)
    ILLUSTRATIONS[key](td, 0, 0, w, h)
    img.paste(tmp, (int(round(x)), int(round(y))))


def build():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    x0, x1 = MARGIN, W - MARGIN
    content_w = x1 - x0
    y = 12

    # Kicker row.
    text(d, (x0, y), stories.KICKER_LEFT, F_KICKER, fill=RED)
    tw = d.textlength(clean(stories.KICKER_RIGHT), font=F_KICKER)
    text(d, (x1 - tw, y), stories.KICKER_RIGHT, F_KICKER, fill=INK)
    y += 20
    rule(d, x0, x1, y, width=2)
    y += 6

    # Title.
    text(d, (x0, y), stories.DAY_TITLE, F_TITLE, fill=(20, 20, 40))
    y += 60
    # Sub-headline strip.
    sub = " \u00b7 ".join(stories.SUBHEAD)
    text(d, (x0, y), sub, F_SUB, fill=INK)
    y += 22
    rule(d, x0, x1, y, width=1)
    y += 6

    # Stats strip: 6 boxes.
    box_w = content_w / 6
    stats_top = y
    for i, (big, label) in enumerate(stories.STATS):
        bx = x0 + i * box_w
        if i:
            d.line([bx, y, bx, y + 46], fill=(200, 195, 180), width=1)
        text(d, (bx + 8, y), big, F_STAT_N, fill=INK)
        for j, line in enumerate(wrap(d, label, F_STAT_L, box_w - 16)):
            text(d, (bx + 8, y + 27 + j * 11), line, F_STAT_L, fill=GREY)
    y = stats_top + 50

    # Region strip.
    seg_w = content_w / len(stories.REGIONS)
    for i, (name, count, color) in enumerate(stories.REGIONS):
        sx = x0 + i * seg_w
        d.rectangle([sx, y, sx + seg_w - 2, y + 20], fill=color)
        label = f"{name} {count}"
        lw = d.textlength(label, font=F_REGION)
        d.text((sx + (seg_w - 2 - lw) / 2, y + 4), label, font=F_REGION,
               fill=(255, 255, 255))
    y += 26

    # Three leads.
    gap = 10
    lead_w = (content_w - 2 * gap) / 3
    lead_img_h = 108
    lead_bottom = y
    for i, lead in enumerate(stories.LEADS):
        lx = x0 + i * (lead_w + gap)
        paste_illustration(img, lead["ill"], lx, y, lead_w, lead_img_h)
        tag_bar(d, lx, y + lead_img_h - 17, lead_w, lead["tag"])
        ly = y + lead_img_h + 5
        text(d, (lx, ly), f"{lead['n']}  {lead['place']} \u00b7 {lead['beat']}",
             F_PLACE, fill=RED)
        ly += 14
        for line in wrap(d, lead["headline"], F_HEAD, lead_w)[:2]:
            text(d, (lx, ly), line, F_HEAD, fill=INK)
            ly += 20
        ly += 1
        for line in wrap(d, lead["dek"], F_DEK, lead_w)[:2]:
            text(d, (lx, ly), line, F_DEK, fill=(60, 60, 60))
            ly += 13
        lead_bottom = max(lead_bottom, ly)
    y = lead_bottom + 6

    # Grid: 5 columns x 2 rows.
    grid_gap = 8
    cell_w = (content_w - 4 * grid_gap) / 5
    grid_img_h = 46
    for row in range(2):
        row_bottom = y
        for col in range(5):
            item = stories.GRID[row * 5 + col]
            cx = x0 + col * (cell_w + grid_gap)
            paste_illustration(img, item["ill"], cx, y, cell_w, grid_img_h)
            tag_bar(d, cx, y + grid_img_h - 14, cell_w, item["tag"], F_TAG_S)
            cy = y + grid_img_h + 4
            text(d, (cx, cy), f"{item['n']}  {item['place']} \u00b7 {item['beat']}",
                 F_PLACE_S, fill=RED)
            cy += 12
            for line in wrap(d, item["headline"], F_HEAD_S, cell_w)[:2]:
                text(d, (cx, cy), line, F_HEAD_S, fill=INK)
                cy += 14
            cy += 1
            for line in wrap(d, item["dek"], F_DEK_S, cell_w)[:2]:
                text(d, (cx, cy), line, F_DEK_S, fill=(60, 60, 60))
                cy += 12
            row_bottom = max(row_bottom, cy)
        y = row_bottom + 6

    # WHY box.
    why_top = y
    d.rectangle([x0, y, x1, y + 60], outline=RED, width=2)
    text(d, (x0 + 8, y + 5), stories.WHY_TITLE, F_WHY_T, fill=RED)
    col_w = (content_w - 16) / 5
    for i, item in enumerate(stories.WHY):
        wx = x0 + 8 + i * col_w
        lines = wrap(d, f"\u2022 {item}", F_WHY, col_w - 10)
        for j, line in enumerate(lines[:3]):
            text(d, (wx, y + 24 + j * 13), line, F_WHY, fill=INK)
    y = why_top + 66

    # ALSO header + 37 items in 3 columns.
    d.rectangle([x0, y, x1, y + 19], fill=NAVY)
    text(d, (x0 + 8, y + 3), "ALSO ON SUNDAY 22 NOVEMBER \u2014 37 MORE STORIES",
         F_ALSO_H, fill=(255, 255, 255))
    y += 23
    cols = [stories.ALSO[:13], stories.ALSO[13:25], stories.ALSO[25:]]
    col_w = content_w / 3
    also_top = y
    for ci, col in enumerate(cols):
        cx = x0 + ci * col_w
        cy = also_top
        for n, place, item_text in col:
            num = f"{n} "
            text(d, (cx, cy), num, F_ALSO_N, fill=RED)
            nw = d.textlength(num, font=F_ALSO_N)
            line = f"{place} \u2014 {item_text}"
            lines = wrap(d, line, F_ALSO, col_w - nw - 8)
            if len(lines) > 1:
                print(f"WARNING: ALSO item {n} wraps to 2 lines: {line}",
                      file=sys.stderr)
            text(d, (cx + nw, cy), lines[0], F_ALSO, fill=INK)
            cy += 12
    y = also_top + 13 * 12 + 4

    # Bottom row: dotted map (left) + date check (right).
    rule(d, x0, x1, y, width=1)
    y += 5
    map_x1 = x0 + 560
    dc_x = map_x1 + 14
    text(d, (x0, y), "WHERE IT HAPPENED", F_MAP_T, fill=INK)
    text(d, (dc_x, y), stories.DATECHECK_TITLE, F_DC_T, fill=RED)
    y += 16
    proj = draw_dot_map(d, x0, y, 560, 72)
    for i, (label, lon, lat) in enumerate(stories.PINS):
        draw_pin(d, proj, lon, lat, i + 1)
    dcy = y
    for item in stories.DATECHECK:
        text(d, (dc_x, dcy), f"\u00d7 {item}", F_DC, fill=(70, 70, 70))
        dcy += 11
    y += 76

    # Footer.
    rule(d, x0, x1, y, width=1)
    y += 4
    fw = d.textlength(clean(stories.FOOTER_SOURCES), font=F_FOOT)
    text(d, ((W - fw) / 2, y), stories.FOOTER_SOURCES, F_FOOT, fill=GREY)
    y += 13
    text(d, (x0, y), stories.FOOTER_MARKETS, F_FOOT, fill=GREY)
    tw = d.textlength(clean(stories.FOOTER_TRENDING), font=F_FOOT)
    text(d, (x1 - tw, y), stories.FOOTER_TRENDING, F_FOOT, fill=GREY)
    y += 12
    assert y <= H, f"layout overflow: final y={y}"
    return img


def main():
    out = Path(__file__).resolve().parent / "entry.png"
    img = build()
    img.save(out, format="PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
