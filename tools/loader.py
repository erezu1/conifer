"""The loading animation: the Conifer icon growing, as the page loads.

The trunk is drawn from the ground up, then the boughs from the trunk outward, the gist's first and the deepest
last (the tree read from the top, as the reader reads it); then the nodes appear, the apex first and the leaves
last; it holds, fades, and grows again until the paper is drawn. Pure CSS (it runs before any script has been
read); viewer.js takes it away once the page is ready.
"""

CYCLE = 2.8  # seconds


def _stroke(name, d, start, end):
    return (f'<path class="ld-{name}" d="{d}" pathLength="1"/>',
            f"@keyframes ld-{name} {{ 0%, {start}% {{ stroke-dashoffset: 1; }} {end}%, 100% {{ stroke-dashoffset: 0; }} }}\n"
            f".ld-{name} {{ stroke-dasharray: 1; stroke-dashoffset: 1; animation: ld-{name} {CYCLE}s infinite; animation-timing-function: cubic-bezier(.3, .1, .3, 1); }}\n")


def _dot(name, cx, cy, r, start, end):
    return (f'<circle class="ld-{name}" cx="{cx}" cy="{cy}" r="{r}"/>',
            f"@keyframes ld-{name} {{ 0%, {start}% {{ transform: scale(0); }} {end}% {{ transform: scale(1.18); }} {end + 4}%, 100% {{ transform: scale(1); }} }}\n"
            f".ld-{name} {{ transform-box: fill-box; transform-origin: center; transform: scale(0); animation: ld-{name} {CYCLE}s infinite; animation-timing-function: ease-out; }}\n")


def build():
    parts, css = [], []
    def add(pair):
        parts.append(pair[0]); css.append(pair[1])
    add(_stroke("trunk", "M32 56 V 9", 2, 20))
    joints = [(20, 23, 41, 28), (32, 17.5, 46.5, 43), (44, 11, 53, 58)]
    for k, (y, xl, xr, y2) in enumerate(joints):
        s = 18 + 8 * k
        add(_stroke(f"bl{k}", f"M32 {y} L {xl} {y2}", s, s + 13))
        add(_stroke(f"br{k}", f"M32 {y} L {xr} {y2}", s, s + 13))
    add(_dot("apex", 32, 9, 4, 44, 52))
    for k, (y, xl, xr, y2) in enumerate(joints):
        s = 48 + 5 * k
        add(_dot(f"j{k}", 32, y, 2.6, s, s + 7))
        add(_dot(f"l{k}", xl, y2, 2.9, s + 3, s + 10))
        add(_dot(f"r{k}", xr, y2, 2.9, s + 3, s + 10))
    strokes = "".join(p for p in parts if p.startswith("<path"))
    dots = "".join(p for p in parts if p.startswith("<circle"))
    svg = ('<svg viewBox="0 0 64 64" aria-hidden="true">'
           '<g class="ld-tree">'
           f'<g fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round">{strokes}</g>'
           f'<g fill="currentColor">{dots}</g></g></svg>')
    html = f'<div id="loader" role="progressbar" aria-label="Loading the paper">{svg}</div>\n'
    style = ("#loader { position: fixed; inset: 0; z-index: 100; display: grid; place-items: center; background: var(--bg, #fff); color: var(--accent, #1d5b98); transition: opacity .35s ease; }\n"
             "#loader svg { width: 76px; height: 76px; overflow: visible; }\n"
             "#loader.done { opacity: 0; pointer-events: none; }\n"
             f"@keyframes ld-tree {{ 0%, 84% {{ opacity: 1; }} 96%, 100% {{ opacity: 0; }} }}\n"
             f".ld-tree {{ animation: ld-tree {CYCLE}s infinite ease-in-out; }}\n"
             + "".join(css)
             + "@media (prefers-reduced-motion: reduce) { #loader * { animation: none !important; stroke-dashoffset: 0 !important; transform: none !important; } "
               "#loader svg { animation: ld-calm 1.6s ease-in-out infinite alternate; } }\n"
               "@keyframes ld-calm { from { opacity: .45; } to { opacity: 1; } }\n")
    return html, style


if __name__ == "__main__":
    h, s = build()
    print(len(h), len(s))
