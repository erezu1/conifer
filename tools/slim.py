"""Slimming MathJax's SVG output before it goes into a page (measured on arXiv:2608.21511, 17 Oct 2026: a third of
the formulas' bytes was markup the reader never uses, and the browser reads every byte of it when the Paper is drawn).

Kept: what draws (paths, uses, texts, transforms, sizes), data-c on each glyph (the search finds symbols by it),
data-tex on the container (copying gives TeX), jax and display (the stylesheet selects on them), and data-mml-node
only where MathJax's own stylesheet looks at it (maction, merror, mtable).
Dropped: the other data-mml-node marks, data-mjx-texclass, xmlns and xmlns:xlink (an SVG inside HTML needs none),
role and focusable, the stroke/fill/stroke-width of the outer group (viewer.css sets them once on every formula),
xlink:href for href, a translate's zero second argument, a bare <g> around a single glyph, and a\ngroup that only places one glyph (the glyph takes x and y instead).
"""
import re

KEEP_MML = {"maction", "merror", "mtable"}
_MML = re.compile(r' data-mml-node="([^"]+)"')
_TR = re.compile(r'transform="translate\(([-\d.]+),0\)"')
_POS = re.compile(r'<g transform="translate\(([-\d.]+)(?:,([-\d.]+))?\)">(<use [^>]*></use>)</g>')
_BARE = re.compile(r"<g>(<use [^>]*></use>|<text [^>]*>[^<]*</text>|<rect [^>]*></rect>|<path [^>]*></path>)</g>")


def slim(svg):
    svg = _MML.sub(lambda m: m.group(0) if m.group(1) in KEEP_MML else "", svg)
    svg = svg.replace(' data-mjx-texclass="ORD"', "").replace(' data-mjx-texclass="OP"', "")
    svg = re.sub(r' data-mjx-texclass="[A-Z]+"', "", svg)
    svg = svg.replace(' xmlns="http://www.w3.org/2000/svg"', "").replace(' xmlns:xlink="http://www.w3.org/1999/xlink"', "")
    svg = svg.replace(' role="img"', "").replace(' focusable="false"', "")
    svg = svg.replace('<g stroke="currentColor" fill="currentColor" stroke-width="0"', "<g")
    svg = svg.replace(" xlink:href=", " href=")
    svg = _TR.sub(r'transform="translate(\1)"', svg)
    prev = None
    while prev != svg:                                # a group with no attributes around one glyph draws the same without it
        prev, svg = svg, _BARE.sub(r"\1", svg)
    # a group that only places one glyph: the glyph is placed by its own x and y (the same translation)
    return _POS.sub(lambda m: m.group(3).replace("<use ", '<use x="%s"%s ' % (m.group(1), ' y="%s"' % m.group(2) if m.group(2) else ""), 1), svg)
