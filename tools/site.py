#!/usr/bin/env python3
"""Assemble the site that GitHub Pages serves (docs/): a small index and one folder per cone.

    python3 tools/site.py

docs/index.html              the index: every tree, with its gist
docs/<key>/index.html        the tree page (a copy of its built page)
"""
import html
import json
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DOCS = HERE / "docs"
DOCS.mkdir(exist_ok=True)

cones = [
    {"key": "2608.21511", "page": HERE / "papers" / "2608.21511" / "tree.html", "data": HERE / "papers" / "2608.21511" / "tree.json"},
    {"key": "semicircle", "page": HERE / "mockup" / "conifer-mockup.html", "data": HERE / "mockup" / "semicircle.tree.json"},
]
rows = []
for c in cones:
    d = json.loads(c["data"].read_text())
    (DOCS / c["key"]).mkdir(exist_ok=True)
    shutil.copyfile(c["page"], DOCS / c["key"] / "index.html")
    m = d["meta"]
    gist = re.sub(r"<[^>]+>", " ", (d["root"].get("gist") or {}).get("html", ""))
    gist = re.sub(r"\$[^$]*\$", "", gist)                       # (the index shows no formulas)
    gist = re.sub(r"\s+", " ", gist).strip()
    first = re.split(r"(?<=[.!?])\s+(?=Result)", gist)[0].replace("Context ", "", 1)
    rows.append((c["key"], m["title"], ", ".join(m.get("authors", [])), m.get("kicker") or "", first))

# the app's files at the site's root: icons, the manifest, the service worker
(DOCS / "icons").mkdir(exist_ok=True)
for f in (HERE / "logo" / "icons").iterdir():
    shutil.copyfile(f, DOCS / "icons" / f.name)
shutil.copyfile(HERE / "logo" / "icons" / "favicon.ico", DOCS / "favicon.ico")
(DOCS / "icons" / "favicon.svg").write_text((HERE / "logo" / "conifer-icon.svg").read_text().replace("currentColor", "#1d5b98"))
shutil.copyfile(HERE / "viewer" / "manifest.webmanifest", DOCS / "manifest.webmanifest")
shutil.copyfile(HERE / "viewer" / "sw.js", DOCS / "sw.js")
HEAD = ('<link rel="icon" href="favicon.ico" sizes="32x32">\n<link rel="icon" href="icons/favicon.svg" type="image/svg+xml">\n'
        '<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">\n<link rel="manifest" href="manifest.webmanifest">\n'
        '<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">\n<meta name="theme-color" content="#0c0e11" media="(prefers-color-scheme: dark)">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="Conifer">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="description" content="Project Conifer: papers grown into trees, read at any depth.">')
css = (HERE / "viewer" / "viewer.css").read_text()
logo = (HERE / "logo" / "conifer-icon.svg").read_text().replace('width="64" height="64"', 'class="logo"').replace('<svg xmlns="http://www.w3.org/2000/svg"', "<svg")
logo = re.sub(r"<!--.*?-->", "", logo, flags=re.S).strip()
items = "\n".join(
    f'<li class="cone"><a href="{k}/"><span class="cone-title">{html.escape(t)}</span><span class="cone-by">{html.escape(a)}{(" · " + html.escape(kk)) if kk else ""}</span><span class="cone-gist">{html.escape(g[:360])}{"…" if len(g) > 360 else ""}</span></a></li>'
    for k, t, a, kk, g in rows)
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Conifer</title>
{HEAD}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
{css}
.cones {{ list-style: none; padding: 0; margin: 1.5rem 0; display: grid; gap: 1rem; }}
.cone a {{ display: block; border: 1px solid var(--rule); border-radius: 14px; padding: 1rem 1.2rem; color: var(--fg); text-decoration: none; transition: background .15s, border-color .15s; }}
.cone a:hover {{ background: var(--surface); border-color: color-mix(in srgb, var(--accent) 40%, transparent); text-decoration: none; }}
.cone-title {{ display: block; font: 600 1.25rem/1.25 var(--serif); text-wrap: balance; }}
.cone-by {{ display: block; font: .8rem var(--sans); color: var(--muted); margin: .3rem 0 .6rem; }}
.cone-gist {{ display: block; font-size: .95em; color: color-mix(in srgb, var(--fg) 85%, var(--muted)); }}
.intro {{ font-size: 1.02em; }}
</style>
</head>
<body>
<main class="page">
 <header class="titleblock">
  <p class="kicker">{logo}Project Conifer</p>
  <h1 class="title">Papers grown into trees</h1>
  <p class="intro">Every paper here is a tree you can read at any depth. The trunk is the gist: the context, the result, why it matters. The branches are a one-page summary whose sentences show the part of the paper they stand for. The foliage is the paper itself, and the roots are its appendices and proofs, folded until you want them. Definitions, background notes and anticipated questions hang off the text, and a dial sets how much is shown.</p>
 </header>
 <ul class="cones">
{items}
 </ul>
 <footer class="colophon">Summaries, definitions and questions are drafted by an AI reader and carry their status; the paper's text is the author's. Made with Epsilon.</footer>
</main>
<script>if ("serviceWorker" in navigator && /^https?:/.test(location.protocol)) navigator.serviceWorker.register("sw.js").catch(function () {{}});</script>
</body>
</html>
"""
(DOCS / "index.html").write_text(page)
(DOCS / ".nojekyll").write_text("")
print("site:", ", ".join(k for k, *_ in rows), "->", DOCS)
