"""Genera los recursos SVG del perfil Alpaber/Alpaber — estilo B (gaming / tech).

Uso:  python3 assets/_build_assets.py   (desde la raíz del repo)
Cambia textos o colores aquí y vuelve a ejecutarlo.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent

BG = "#07020F"
SURFACE = "#0E0820"
GRID = "#1C1235"
CYAN = "#00F0FF"
MAGENTA = "#FF2BD6"
TEXT = "#F2F0FF"
MUTED = "#8A7FA8"
MONO = "'JetBrains Mono', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
SCAN = '<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" fill-opacity=".035"/></pattern>'


def save(name, svg):
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hud_corners(w, h, pad=10, size=22, color=CYAN):
    """Esquinas tipo HUD."""
    p = pad
    s = size
    d = (f"M{p},{p + s} V{p} H{p + s} "
         f"M{w - p - s},{p} H{w - p} V{p + s} "
         f"M{w - p},{h - p - s} V{h - p} H{w - p - s} "
         f"M{p + s},{h - p} H{p} V{h - p - s}")
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5" stroke-opacity=".9"/>'


def glitch_text(x, y, text, size, weight=800, anim=True):
    cls_c = ' class="gc"' if anim else ""
    cls_m = ' class="gm"' if anim else ""
    t = esc(text)
    common = f'font-family="{MONO}" font-size="{size}" font-weight="{weight}" letter-spacing="2"'
    return (f'<text x="{x - 3}" y="{y}" {common} fill="{MAGENTA}"{cls_m}>{t}</text>'
            f'<text x="{x + 3}" y="{y}" {common} fill="{CYAN}"{cls_c}>{t}</text>'
            f'<text x="{x}" y="{y}" {common} fill="{TEXT}" filter="url(#glow)">{t}</text>')


GLITCH_CSS = """
    .gc { animation: gc 4s steps(1) infinite; }
    .gm { animation: gm 4s steps(1) infinite; }
    @keyframes gc { 0%,90%,100% { transform: translate(0,0); } 92% { transform: translate(5px,-2px); } 95% { transform: translate(-4px,1px); } }
    @keyframes gm { 0%,90%,100% { transform: translate(0,0); } 92% { transform: translate(-5px,2px); } 95% { transform: translate(4px,-1px); } }
"""

GLOW = '<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feFlood flood-color="#00F0FF" flood-opacity=".55"/><feComposite in2="b" operator="in"/><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>'


# ---------- BANNER (1200x400) ----------
save("banner.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-label="PABLO.RDZ — Full Stack Developer. Próximo nivel: IA y Big Data">
  <style>{GLITCH_CSS}
    .xp {{ animation: xp 3.5s ease-out forwards; }}
    @keyframes xp {{ from {{ width: 0; }} to {{ width: 186px; }} }}
    .cursor {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
  </style>
  <defs>
    {SCAN}{GLOW}
    <clipPath id="r"><rect width="1200" height="400" rx="16"/></clipPath>
    <radialGradient id="mg" cx="88%" cy="15%" r="50%"><stop offset="0" stop-color="{MAGENTA}" stop-opacity=".22"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity="0"/></radialGradient>
    <radialGradient id="cg" cx="0%" cy="100%" r="55%"><stop offset="0" stop-color="{CYAN}" stop-opacity=".14"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
    <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{MAGENTA}" stop-opacity="0"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity=".35"/></linearGradient>
  </defs>
  <g clip-path="url(#r)">
    <rect width="1200" height="400" fill="{BG}"/>
    <rect width="1200" height="400" fill="url(#mg)"/>
    <rect width="1200" height="400" fill="url(#cg)"/>
    <!-- suelo en perspectiva tipo synthwave -->
    <g stroke="url(#floor)" stroke-width="1.2">
      {''.join(f'<line x1="{960 + (i - 6) * 18}" y1="270" x2="{960 + (i - 6) * 70}" y2="400"/>' for i in range(13))}
      {''.join(f'<line x1="760" y1="{y}" x2="1200" y2="{y}"/>' for y in (278, 292, 312, 340, 378))}
    </g>
    <!-- sol retro -->
    <clipPath id="sky"><rect x="760" y="0" width="440" height="268"/></clipPath>
    <g clip-path="url(#sky)"><g transform="translate(960 250)">
      <circle r="92" fill="{MAGENTA}" fill-opacity=".85"/>
      <g fill="{BG}">{''.join(f'<rect x="-100" y="{y}" width="200" height="{h}"/>' for y, h in ((-30, 3), (-12, 5), (4, 7)))}</g>
    </g></g>
    <rect width="1200" height="400" fill="url(#scan)"/>
  </g>
  {hud_corners(1200, 400, pad=16, size=30)}
  <text x="64" y="92" font-family="{MONO}" font-size="18" fill="{MUTED}" letter-spacing="3">[ @ALPABER ] · PLAYER_1 · ONLINE<tspan fill="{CYAN}" class="cursor"> ▌</tspan></text>
  {glitch_text(60, 190, "PABLO.RDZ", 96)}
  <text x="64" y="244" font-family="{MONO}" font-size="24" fill="{CYAN}">&gt; FULL STACK DEV // PYTHON · DJANGO · REACT</text>
  <text x="64" y="300" font-family="{MONO}" font-size="16" fill="{MUTED}" letter-spacing="2">NEXT LEVEL: IA &amp; BIG DATA</text>
  <rect x="64" y="314" width="300" height="14" fill="none" stroke="{MAGENTA}" stroke-width="1.5"/>
  <rect x="67" y="317" width="186" height="8" fill="{MAGENTA}" class="xp"/>
  <text x="378" y="327" font-family="{MONO}" font-size="16" fill="{MAGENTA}">LOADING…</text>
</svg>
""")


# ---------- SEPARADOR ----------
save("divider.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="24" viewBox="0 0 1200 24" role="presentation">
  <defs><linearGradient id="d" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}" stop-opacity=".8"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity="0"/>
  </linearGradient></defs>
  <rect x="0" y="11" width="1200" height="2" fill="url(#d)"/>
  {''.join(f'<rect x="{570 + i * 22}" y="6" width="12" height="12" fill="{MAGENTA if i == 1 else CYAN}"/>' for i in range(3))}
</svg>
""")


# ---------- CABECERAS DE SECCIÓN ----------
def header(num, title, tag, file):
    save(file, f"""
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="64" viewBox="0 0 800 64" role="img" aria-label="{num} {esc(title)}">
  <defs><linearGradient id="h" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{CYAN}"/><stop offset=".6" stop-color="{MAGENTA}" stop-opacity=".5"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity="0"/>
  </linearGradient></defs>
  <rect x="2" y="14" width="44" height="32" fill="{MAGENTA}"/>
  <text x="24" y="38" text-anchor="middle" font-family="{MONO}" font-size="20" font-weight="800" fill="{BG}">{num}</text>
  <text x="62" y="40" font-family="{MONO}" font-size="26" font-weight="800" fill="{TEXT}" letter-spacing="3">{esc(title)}</text>
  <text x="798" y="40" text-anchor="end" font-family="{MONO}" font-size="16" fill="{MUTED}" letter-spacing="2">// {esc(tag)}</text>
  <rect x="2" y="56" width="796" height="2" fill="url(#h)"/>
</svg>
""")



# ---------- PANEL DE CHIPS (stack y "en cola") ----------
def chip_panel(file, rows, queued=False):
    CHAR, LINE = 13.6, 52
    chip = MAGENTA if queued else CYAN
    dash = ' stroke-dasharray="6 5"' if queued else ""
    body, y = "", 40
    for i, (label, chips) in enumerate(rows):
        body += (f'<text x="44" y="{y + 30}" font-family="{MONO}" font-size="17" font-weight="700" '
                 f'fill="{CYAN if queued else MAGENTA}" letter-spacing="2">{esc(label)}</text>')
        x, line_y = 220, y
        for c in chips:
            w = int(len(c) * CHAR + 36)
            if x + w > 860:
                x, line_y = 220, line_y + LINE
            body += (f'<rect x="{x}" y="{line_y + 4}" width="{w}" height="40" '
                     f'fill="{chip}" fill-opacity=".06" stroke="{chip}" stroke-opacity=".6"{dash}/>'
                     + ("" if queued else f'<rect x="{x}" y="{line_y + 4}" width="4" height="40" fill="{chip}"/>')
                     + f'<text x="{x + w / 2 + (0 if queued else 2)}" y="{line_y + 31}" text-anchor="middle" font-family="{MONO}" '
                     f'font-size="22" fill="{TEXT}" fill-opacity="{.8 if queued else 1}">{esc(c)}</text>')
            x += w + 12
        y = line_y + LINE + 22
        if i < len(rows) - 1:
            body += f'<rect x="44" y="{y - 14}" width="812" height="1" fill="{GRID}"/>'
    H = y + 10
    save(file, f"""
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{H}" viewBox="0 0 900 {H}" role="img" aria-label="{esc(', '.join(c for _, cs in rows for c in cs))}">
  <defs>{SCAN}</defs>
  <rect width="900" height="{H}" rx="10" fill="{SURFACE}"/>
  <rect width="900" height="{H}" rx="10" fill="url(#scan)"/>
  {hud_corners(900, H, pad=6, size=20, color=MAGENTA if queued else CYAN)}
  {body}
</svg>
""")


# ---------- CARDS DE PROYECTO ----------
def project_card(file, eyebrow, title, desc_lines, tags, status, status_color, locked=False):
    desc = "".join(
        f'<text x="44" y="{156 + i * 32}" font-family="{MONO}" font-size="20" fill="{MUTED}">{esc(l)}</text>'
        for i, l in enumerate(desc_lines))
    x, tag_svg = 44, ""
    for t in tags:
        w = int(len(t) * 11 + 28)
        tag_svg += (f'<rect x="{x}" y="256" width="{w}" height="32" fill="{MAGENTA}" fill-opacity=".12" stroke="{MAGENTA}" stroke-opacity=".6"/>'
                    f'<text x="{x + w / 2}" y="278" text-anchor="middle" font-family="{MONO}" font-size="17" fill="{MAGENTA}">{esc(t)}</text>')
        x += w + 10
    title_svg = (f'<text x="44" y="112" font-family="{MONO}" font-size="38" font-weight="800" fill="{MUTED if locked else TEXT}" letter-spacing="1">{esc(title)}</text>')
    save(file, f"""
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="320" viewBox="0 0 900 320" role="img" aria-label="{esc(title)}">
  <style>.dot {{ animation: p 1.6s ease-in-out infinite; }} @keyframes p {{ 50% {{ opacity: .25; }} }}</style>
  <defs>{SCAN}
    <radialGradient id="cg" cx="100%" cy="0%" r="70%"><stop offset="0" stop-color="{MAGENTA}" stop-opacity="{'.06' if locked else '.18'}"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="900" height="320" rx="10" fill="{SURFACE}"/>
  <rect width="900" height="320" rx="10" fill="url(#cg)"/>
  <rect width="900" height="320" rx="10" fill="url(#scan)"/>
  {hud_corners(900, 320, pad=6, size=20, color=MUTED if locked else CYAN)}
  <text x="44" y="62" font-family="{MONO}" font-size="17" fill="{CYAN}" letter-spacing="3">{esc(eyebrow)}</text>
  <circle cx="{856 - len(status) * 12.4 - 14}" cy="56" r="5" fill="{status_color}" class="dot"/>
  <text x="856" y="62" text-anchor="end" font-family="{MONO}" font-size="17" fill="{status_color}" letter-spacing="2">{esc(status)}</text>
  {title_svg}
  {desc}
  {tag_svg}
</svg>
""")



# ---------- TEXTOS POR IDIOMA ----------
L = {
    "": {  # español (README.md)
        "headers": [("01", "STACK", "loadout"), ("02", "PROYECTOS", "misiones"),
                    ("03", "SUBIENDO DE NIVEL", "ia & big data"), ("04", "ACTIVIDAD", "contribuciones"),
                    ("05", "CONTACTO", "multiplayer")],
        "data": "DATOS",
        "q": [("IA / ML", ["TensorFlow", "Keras"]),
              ("BIG DATA", ["Apache Spark", "Hadoop", "MongoDB"]),
              ("BI", ["Power BI"])],
        "agro": ("MISIÓN 01 · ANÁLISIS DE DATOS",
                 ["Datos reales de 8 sensores de suelo: limpieza,",
                  "EDA, alertas y predicción a 24 h. Web en Django."]),
        "locked": ("MISIÓN 02", "[ BLOQUEADA ]", ["Próximo proyecto en desarrollo.", "Se desbloquea pronto."], "PRÓXIMAMENTE"),
        "tpl": ("MISIÓN 0X · CATEGORÍA", "Nombre del proyecto",
                ["Qué problema resuelve, en una línea.", "Qué has hecho tú y qué lo hace interesante."]),
    },
    "-en": {
        "headers": [("01", "STACK", "loadout"), ("02", "PROJECTS", "quests"),
                    ("03", "LEVELLING UP", "ai & big data"), ("04", "ACTIVITY", "contributions"),
                    ("05", "CONTACT", "multiplayer")],
        "data": "DATA",
        "q": [("AI / ML", ["TensorFlow", "Keras"]),
              ("BIG DATA", ["Apache Spark", "Hadoop", "MongoDB"]),
              ("BI", ["Power BI"])],
        "agro": ("QUEST 01 · DATA ANALYSIS",
                 ["Real data from 8 soil sensors: cleaning, EDA,",
                  "alerts and a 24 h forecast. Django web app."]),
        "locked": ("QUEST 02", "[ LOCKED ]", ["Next project in progress.", "Unlocking soon."], "COMING SOON"),
        "tpl": ("QUEST 0X · CATEGORY", "Project name",
                ["What problem it solves, in one line.", "What you built and why it's interesting."]),
    },
}

files = ["h-stack", "h-projects", "h-learning", "h-activity", "h-contact"]
for sfx, t in L.items():
    for (n, title, tag), f in zip(t["headers"], files):
        header(n, title, tag, f"{f}{sfx}.svg")
    chip_panel(f"stack{sfx}.svg", [
        ("FRONTEND", ["HTML5", "CSS3", "JavaScript", "React", "Bootstrap", "Tailwind CSS"]),
        ("BACKEND", ["Python", "Django", "PHP"]),
        (t["data"], ["SQL", "MySQL", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn", "Jupyter"]),
        ("TOOLS", ["Git", "GitHub"]),
    ])
    chip_panel(f"queue{sfx}.svg", t["q"], queued=True)
    project_card(f"project-agrodatalab{sfx}.svg", t["agro"][0], "AgroDataLab EnviroPro", t["agro"][1],
                 ["Python", "Django", "Pandas", "Scikit-learn", "Jupyter"], "ONLINE", "#3DFF9A")
    e, ti, d, st = t["locked"]
    project_card(f"project-locked{sfx}.svg", e, ti, d, ["build in public"], st, MUTED, locked=True)
    project_card(f"project-card-template{sfx}.svg", t["tpl"][0], t["tpl"][1], t["tpl"][2],
                 ["Django", "Tailwind CSS", "SQL"], "ONLINE", "#3DFF9A")

print("ok", len(list(OUT.glob("*.svg"))), "svg")
