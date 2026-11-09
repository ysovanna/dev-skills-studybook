# -*- coding: utf-8 -*-
"""Flat 2D object drawings for the git-basics unit. Run: python git-basics/draw.py"""
import io
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
NAVY, INK, WHITE, LINE = '#1C2A4A', '#23262D', '#FFFFFF', '#C9CED8'
GREEN, YELLOW, RED = '#00A84D', '#F5B700', '#D7372B'
ORANGE, PURPLE, BROWN, BLUE = '#EF7C1C', '#996CAC', '#CD7C2F', '#0052A4'
PAPER, GREY = '#EEF0F4', '#9AA3B2'
MONO = 'Consolas, Menlo, monospace'
SANS = 'Gothic A1, Segoe UI, sans-serif'


def svg(name, body, vb='0 0 160 100'):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>\n'
    io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(s)


def file_page(x, y, w=34, h=44, fill=WHITE):
    """A sheet of paper with a folded corner, top-left at x,y."""
    f = 10
    return (f'<path d="M{x} {y} H{x + w - f} L{x + w} {y + f} V{y + h} H{x} Z" fill="{fill}" stroke="{LINE}" stroke-width="2"/>'
            f'<path d="M{x + w - f} {y} V{y + f} H{x + w}" fill="{GREY}" opacity=".35"/>')


os.makedirs(OUT, exist_ok=True)

# c1. terminal running git init
svg('c1-terminal.svg',
    f'<rect x="18" y="10" width="124" height="80" rx="9" fill="{NAVY}"/>'
    f'<circle cx="32" cy="22" r="3.4" fill="{RED}"/><circle cx="43" cy="22" r="3.4" fill="{YELLOW}"/><circle cx="54" cy="22" r="3.4" fill="{GREEN}"/>'
    f'<rect x="26" y="32" width="108" height="50" rx="4" fill="{INK}"/>'
    f'<text x="34" y="52" font-family="{MONO}" font-size="11" fill="{YELLOW}">$</text>'
    f'<text x="46" y="52" font-family="{MONO}" font-size="11" fill="{WHITE}">git init</text>'
    f'<rect x="98" y="43" width="7" height="11" fill="{GREEN}" opacity=".9"/>'
    f'<path d="M35 66 l4 4 7 -8" stroke="{GREEN}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<rect x="50" y="64" width="60" height="5" rx="2.5" fill="{GREY}"/>')

# c2. folder with a hidden .git tag
svg('c2-folder.svg',
    f'<path d="M30 26 h34 l8 10 h58 a8 8 0 0 1 8 8 v34 a8 8 0 0 1 -8 8 H30 a8 8 0 0 1 -8 -8 V34 a8 8 0 0 1 8 -8Z" fill="{YELLOW}"/>'
    f'<path d="M22 46 h116 v32 a8 8 0 0 1 -8 8 H30 a8 8 0 0 1 -8 -8Z" fill="#F7C948"/>'
    f'<g transform="translate(80 58) rotate(-6)">'
    f'<rect x="-26" y="-11" width="52" height="22" rx="5" fill="{NAVY}"/>'
    f'<circle cx="-17" cy="0" r="3" fill="{WHITE}"/>'
    f'<text x="4" y="4.5" font-family="{MONO}" font-size="12" font-weight="bold" fill="{WHITE}" text-anchor="middle">.git</text></g>')

# c3. magnifier over a list of changed files
svg('c3-status.svg',
    f'<rect x="20" y="8" width="96" height="84" rx="7" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    + ''.join(
        f'<circle cx="36" cy="{26 + i * 22}" r="4.5" fill="{[GREEN, ORANGE, GREY][i]}"/>'
        f'<rect x="48" y="{23 + i * 22}" width="{[50, 42, 46][i]}" height="6" rx="3" fill="{LINE}"/>' for i in range(3))
    + ''.join(
        f'<circle cx="36" cy="{70 + i * 16}" r="4.5" fill="{[GREY, GREEN][i]}"/>'
        f'<rect x="48" y="{67 + i * 16}" width="{[38, 44][i]}" height="6" rx="3" fill="{LINE}"/>' for i in range(2))
    + f'<circle cx="106" cy="58" r="24" fill="{BLUE}" opacity=".14"/><circle cx="106" cy="58" r="24" fill="none" stroke="{NAVY}" stroke-width="5"/>'
    f'<line x1="123" y1="75" x2="142" y2="94" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>')

# c4. diff: removed red line, added green line on two pages
svg('c4-diff.svg',
    file_page(20, 14, 56, 74) + file_page(84, 14, 56, 74)
    + f'<rect x="28" y="26" width="40" height="6" rx="3" fill="{LINE}"/>'
    f'<rect x="28" y="40" width="34" height="6" rx="3" fill="{LINE}"/>'
    f'<rect x="92" y="26" width="40" height="6" rx="3" fill="{LINE}"/>'
    f'<rect x="92" y="40" width="34" height="6" rx="3" fill="{LINE}"/>'
    + f'<rect x="28" y="54" width="40" height="12" rx="3" fill="{RED}" opacity=".2"/><line x1="30" y1="60" x2="66" y2="60" stroke="{RED}" stroke-width="2.6"/>'
    f'<rect x="92" y="54" width="40" height="12" rx="3" fill="{GREEN}" opacity=".2"/><line x1="106" y1="60" x2="118" y2="60" stroke="{GREEN}" stroke-width="2.6"/><line x1="112" y1="54" x2="112" y2="66" stroke="{GREEN}" stroke-width="2.6"/>'
    + f'<rect x="28" y="72" width="30" height="6" rx="3" fill="{LINE}"/><rect x="92" y="72" width="42" height="6" rx="3" fill="{LINE}"/>')

# c5. staging tray: a file dropping into an inbox tray
svg('c5-tray.svg',
    f'<g transform="translate(58 10) rotate(-8)">{file_page(0, 0, 30, 38)}</g>'
    + f'<path d="M73 46 q4 12 -1 22" stroke="{GREEN}" stroke-width="3.4" fill="none" stroke-dasharray="1 7" stroke-linecap="round"/>'
    f'<path d="M68 64 l4 9 5 -8" stroke="{GREEN}" stroke-width="3.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    + f'<path d="M26 60 v26 a8 8 0 0 0 8 8 h92 a8 8 0 0 0 8 -8 V60 h-16 v14 h-76 V60Z" fill="{NAVY}"/>'
    f'<rect x="34" y="52" width="92" height="10" rx="5" fill="#3B4A6E"/>')

# c6. polaroid snapshot with a check badge
svg('c6-snapshot.svg',
    f'<g transform="translate(80 50) rotate(-4) translate(-80 -50)">'
    f'<rect x="42" y="10" width="76" height="82" rx="5" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="50" y="18" width="60" height="52" rx="3" fill="{NAVY}"/>'
    f'<circle cx="66" cy="34" r="7" fill="{YELLOW}"/>'
    f'<path d="M50 62 L70 44 L84 56 L96 46 L110 62Z" fill="#3B4A6E"/>'
    f'<rect x="50" y="76" width="44" height="5" rx="2.5" fill="{LINE}"/></g>'
    + f'<circle cx="118" cy="80" r="13" fill="{GREEN}"/>'
    f'<path d="M111 80 l5 5 9 -10" stroke="{WHITE}" stroke-width="3.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# c7. commit timeline (log)
svg('c7-log.svg',
    f'<line x1="46" y1="12" x2="46" y2="90" stroke="{NAVY}" stroke-width="4"/>'
    + ''.join(
        f'<circle cx="46" cy="{cy}" r="{r}" fill="{col}"/><rect x="62" y="{cy - 4}" width="{w}" height="8" rx="4" fill="{LINE}"/>'
        for (cy, r, col, w) in [(18, 9, PURPLE, 58), (42, 7.5, NAVY, 46), (64, 7.5, NAVY, 54), (86, 6, GREY, 38)])
    + f'<rect x="124" y="10" width="26" height="16" rx="4" fill="{PURPLE}"/>'
    f'<text x="137" y="21.5" font-family="{MONO}" font-size="9" fill="{WHITE}" text-anchor="middle">a3f9c2</text>')

# c8. undo: circular back arrow around a file
svg('c8-undo.svg',
    f'<g transform="translate(80 50)">{file_page(-17, -24, 34, 46)}</g>'
    + ''.join(f'<rect x="{70}" y="{y}" width="20" height="4.5" rx="2.25" fill="{LINE}"/>' for y in (-8, 1, 10))
    + f'<path d="M36 30 a46 40 0 1 1 -6 34" fill="none" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M22 52 L31 68 L44 56Z" fill="{NAVY}"/>')

# c9. branch: main line forking into an orange side line
svg('c9-fork.svg',
    f'<line x1="14" y1="70" x2="146" y2="70" stroke="{NAVY}" stroke-width="5"/>'
    + f'<path d="M58 70 C74 70 70 30 92 30 H132" fill="none" stroke="{ORANGE}" stroke-width="5"/>'
    + ''.join(f'<circle cx="{x}" cy="70" r="8" fill="{NAVY}"/><circle cx="{x}" cy="70" r="3.4" fill="{WHITE}"/>' for x in (26, 140))
    + f'<circle cx="58" cy="70" r="9" fill="{BLUE}"/><circle cx="58" cy="70" r="3.6" fill="{WHITE}"/>'
    + ''.join(f'<circle cx="{x}" cy="30" r="7.5" fill="{ORANGE}"/><circle cx="{x}" cy="30" r="3.2" fill="{WHITE}"/>' for x in (98, 126))
    + f'<text x="24" y="94" font-family="{MONO}" font-size="10" fill="{NAVY}">main</text>'
    f'<text x="96" y="16" font-family="{MONO}" font-size="10" fill="{ORANGE}">new-feature</text>')

# c10. merge: two lines joining into one dot
svg('c10-merge.svg',
    f'<line x1="14" y1="70" x2="118" y2="70" stroke="{NAVY}" stroke-width="5"/>'
    + f'<path d="M46 70 C64 70 66 30 88 30 H104" fill="none" stroke="{ORANGE}" stroke-width="5"/>'
    + f'<path d="M104 30 C122 30 120 70 132 70" fill="none" stroke="{ORANGE}" stroke-width="5"/>'
    + ''.join(f'<circle cx="{x}" cy="70" r="8" fill="{NAVY}"/><circle cx="{x}" cy="70" r="3.4" fill="{WHITE}"/>' for x in (26, 140))
    + f'<circle cx="46" cy="70" r="8" fill="{BLUE}"/><circle cx="46" cy="70" r="3.4" fill="{WHITE}"/>'
    + f'<circle cx="92" cy="30" r="7.5" fill="{ORANGE}"/><circle cx="92" cy="30" r="3.2" fill="{WHITE}"/>'
    + f'<circle cx="132" cy="70" r="10" fill="{GREEN}"/><path d="M127 70 l3.4 3.6 6 -7" stroke="{WHITE}" stroke-width="2.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

# c11. cloud holding a repo folder
svg('c11-cloud.svg',
    f'<path d="M45 74 a20 20 0 0 1 -3 -39 a26 26 0 0 1 50 -8 a19 19 0 0 1 24 18 a17 17 0 0 1 -6 29Z" fill="{WHITE}" stroke="{LINE}" stroke-width="2.5"/>'
    + f'<g transform="translate(80 55)">'
    f'<path d="M-24 -13 h14 l5 6 h25 a4 4 0 0 1 4 4 v16 a4 4 0 0 1 -4 4 H-24 a4 4 0 0 1 -4 -4 V-9 a4 4 0 0 1 4 -4Z" fill="{BROWN}"/>'
    f'<rect x="-28" y="-3" width="56" height="20" rx="4" fill="#DD9A55"/></g>')

# c12. laptop syncing with a cloud (push up / pull down)
svg('c12-sync.svg',
    f'<path d="M118 34 a13 13 0 0 1 -2 -25 a17 17 0 0 1 32 -5 a12.5 12.5 0 0 1 16 12 a11 11 0 0 1 -4 18Z" fill="{WHITE}" stroke="{LINE}" stroke-width="2.5"/>'
    + f'<rect x="16" y="34" width="56" height="38" rx="4" fill="{NAVY}"/><rect x="21" y="39" width="46" height="28" rx="2" fill="{INK}"/>'
    f'<path d="M8 76 h72 l-6 10 H14Z" fill="#3B4A6E"/>'
    + f'<line x1="92" y1="66" x2="92" y2="34" stroke="{GREEN}" stroke-width="5" stroke-linecap="round"/><path d="M84 40 l8 -10 8 10Z" fill="{GREEN}"/>'
    f'<line x1="106" y1="34" x2="106" y2="66" stroke="{YELLOW}" stroke-width="5" stroke-linecap="round"/><path d="M98 60 l8 10 8 -10Z" fill="{YELLOW}"/>')

# x-clock. time machine: clock with a counter-clockwise arrow
svg('x-clock.svg',
    f'<circle cx="80" cy="52" r="34" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/>'
    + f'<line x1="80" y1="52" x2="80" y2="32" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>'
    f'<line x1="80" y1="52" x2="94" y2="58" stroke="{BLUE}" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="80" cy="52" r="3.6" fill="{NAVY}"/>'
    + ''.join(f'<circle cx="{80 + 27 * __import__("math").cos(a)}" cy="{52 - 27 * __import__("math").sin(a)}" r="1.8" fill="{LINE}" />' for a in (0, 1.5708, 3.1416))
    + f'<path d="M40 22 A44 44 0 0 1 122 26" fill="none" stroke="{GREEN}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M30 30 L38 17 L47 29Z" fill="{GREEN}"/>')

# x-conflict. two edits, one line: file with red/green pair and a question badge
svg('x-conflict.svg',
    file_page(52, 10, 60, 80)
    + f'<rect x="60" y="22" width="44" height="6" rx="3" fill="{LINE}"/>'
    + f'<text x="60" y="43" font-family="{MONO}" font-size="9" fill="{RED}">&lt;&lt; HEAD</text>'
    + f'<rect x="60" y="52" width="44" height="8" rx="3" fill="{RED}" opacity=".25"/>'
    + f'<line x1="60" y1="63" x2="104" y2="63" stroke="{LINE}" stroke-width="2"/>'
    + f'<rect x="60" y="70" width="44" height="8" rx="3" fill="{GREEN}" opacity=".25"/>'
    + f'<circle cx="46" cy="76" r="15" fill="{RED}"/>'
    f'<text x="46" y="82.5" font-family="{SANS}" font-size="19" font-weight="bold" fill="{WHITE}" text-anchor="middle">?</text>')

print('drawn:', sorted(os.listdir(OUT)))
