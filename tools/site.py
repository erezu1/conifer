#!/usr/bin/env python3
"""Assemble the site that GitHub Pages serves from docs/ (erezu1.github.io/conifer/): the example tree, nothing else.

    python3 example/build.py     # (after a change to the viewer or the example)
    python3 tools/site.py

docs/index.html      the example tree (the Wigner semicircle), with the site's icons
docs/404.html        sends an old link to a paper (/conifer/<arXiv id>/...) to where the papers now are
"""
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DOCS = HERE / "docs"
PAPERS = "https://erezu1.github.io/papers/"           # Erez's papers as trees, published with his site (18 Oct 2026)

for d in DOCS.iterdir() if DOCS.exists() else []:      # whatever an earlier site left
    shutil.rmtree(d) if d.is_dir() else d.unlink()
DOCS.mkdir(exist_ok=True)

(DOCS / "icons").mkdir()
for f in (HERE / "logo" / "icons").iterdir():
    shutil.copyfile(f, DOCS / "icons" / f.name)
shutil.copyfile(HERE / "logo" / "icons" / "favicon.ico", DOCS / "favicon.ico")
(DOCS / "icons" / "favicon.svg").write_text((HERE / "logo" / "conifer-icon.svg").read_text().replace("currentColor", "#1d5b98"))
ICONS = ('<link rel="icon" href="favicon.ico" sizes="any">\n<link rel="icon" href="icons/favicon-32.png" type="image/png" sizes="32x32">\n'
         '<link rel="icon" href="icons/favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">\n')

page = (HERE / "example" / "semicircle.html").read_text()
page = page.replace("</title>", "</title>\n" + ICONS, 1)
(DOCS / "index.html").write_text(page)

(DOCS / "404.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Conifer</title>
<script>
var m = location.pathname.match(/\\/conifer\\/(\\d{{4}}\\.\\d{{4,5}})\\/?/);
location.replace(m ? "{PAPERS}" + m[1] + "/" + location.hash : "{PAPERS}");
</script></head>
<body style="font: 1rem/1.5 system-ui, sans-serif; margin: 2rem;">The papers have moved to <a href="{PAPERS}">{PAPERS}</a>.</body></html>
""")
(DOCS / ".nojekyll").write_text("")
print("site: the example ->", DOCS)
