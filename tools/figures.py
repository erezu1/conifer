#!/usr/bin/env python3
"""A paper's figure, made light for the page (run by tools/build_tree.py with the project's .venv, which has Pillow):
    .venv/bin/python tools/figures.py SRC OUT MAXWIDTH        prints the width and height written

No wider than MAXWIDTH pixels (a page shows a figure at most ~700px wide: twice that is sharp on any screen), and, when
128 colours reproduce it to within the eye (line plots, diagrams: their antialiased edges need no more), stored with a
palette, which makes such a PNG about a quarter of its size. A photograph keeps its colours.
"""
import sys

from PIL import Image, ImageChops, ImageStat

src, out, maxw = sys.argv[1], sys.argv[2], int(sys.argv[3])
im = Image.open(src)
im.load()
if im.mode not in ("RGB", "RGBA"):
    im = im.convert("RGBA" if "A" in im.mode or im.info.get("transparency") is not None else "RGB")
if im.width > maxw:
    im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
q = im.quantize(colors=128, method=Image.Quantize.FASTOCTREE if im.mode == "RGBA" else Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
diff = ImageChops.difference(q.convert(im.mode), im)
rms = max(ImageStat.Stat(diff).rms[:3])
(q if rms < 3.0 else im).save(out, optimize=True)
print(im.width, im.height)
