#!/usr/bin/env python3
"""Build the Conifer mockup.

    python3 build.py

Writes
  semicircle.tree.json       the sample document as data (TeX intact): the proposed format
  conifer-mockup.html        the page, self-contained (formulas drawn once as SVG with Epsilon's MathJax)
  conifer-mockup.artifact.html   the same without the document skeleton, to publish as a Claude artifact

The formulas are drawn with Epsilon's render_math.js (node + mathjax-full), so nothing is fetched by the page
except the fonts.
"""
import html
import json
import re
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
EPSILON = Path("/Users/urbach/IAS Dropbox/Erez Urbach/research/epsilon")
sys.path.insert(0, str(HERE))
from doc_semicircle import DOC  # noqa: E402

(HERE / "semicircle.tree.json").write_text(json.dumps(DOC, indent=1, ensure_ascii=False) + "\n")

# ---------------------------------------------------------------- collect the formulas
items = []
SKIP = {"id", "quote", "node", "covers", "answeredBy", "at", "key", "kind", "role", "status", "source", "number", "format", "generator", "term", "aliases"}


def mark(tex, display):
    items.append({"tex": tex, "display": display})
    return "\x00%d\x00" % (len(items) - 1)


def collect(s):
    def disp(m):
        tex = m.group(1)
        lab = re.search(r"\\label\{([^}]*)\}", tex)
        tex = re.sub(r"\\label\{[^}]*\}", "", tex)
        idattr = ' id="%s"' % lab.group(1) if lab else ""
        # a display inside a paragraph closes it, as Epsilon's converter does; empty paragraphs are removed below
        return '</p><div class="display"%s><div class="eqbody">%s</div></div><p class="cont">' % (idattr, mark(tex.strip(), True))
    s = re.sub(r"\\\[(.+?)\\\]", disp, s, flags=re.S)
    s = re.sub(r"\$(.+?)\$", lambda m: mark(m.group(1), False), s, flags=re.S)
    s = re.sub(r'<p(?: class="cont")?>\s*</p>', "", s)
    return s


def walk(o, key=None):
    if isinstance(o, dict):
        return {k: walk(v, k) for k, v in o.items()}
    if isinstance(o, list):
        return [walk(v, key) for v in o]
    if isinstance(o, str) and key not in SKIP and ("$" in o or "\\[" in o):
        return collect(o)
    return o


doc = walk(DOC)

# ---------------------------------------------------------------- draw them with MathJax (Epsilon's renderer)
with tempfile.TemporaryDirectory() as td:
    job = Path(td) / "job.json"
    res = Path(td) / "res.json"
    job.write_text(json.dumps({"items": items, "macros": {}, "packages": ["base", "ams", "boldsymbol", "newcommand", "mathtools"]}))
    r = subprocess.run(["node", str(EPSILON / "render_math.js"), str(job), str(res)], capture_output=True, text=True)
    if r.returncode:
        sys.exit("render_math.js failed:\n" + r.stderr)
    out = json.loads(res.read_text())
for e in out.get("errors", []):
    print("math error:", e["message"], "in", e["tex"][:60], file=sys.stderr)
for k in out.get("undefined", []):
    print("undefined macro in:", items[k]["tex"][:60], file=sys.stderr)
svgs = out["out"]


def fill(o):
    if isinstance(o, dict):
        return {k: fill(v) for k, v in o.items()}
    if isinstance(o, list):
        return [fill(v) for v in o]
    if isinstance(o, str) and "\x00" in o:
        return re.sub("\x00(\\d+)\x00", lambda m: svgs[int(m.group(1))].replace("<mjx-container", '<mjx-container data-tex="%s"' % html.escape(items[int(m.group(1))]["tex"].strip(), quote=True), 1), o)
    return o


doc = fill(doc)
print("formulas drawn:", len(items))

# ---------------------------------------------------------------- the page
css = (HERE.parent / "viewer" / "viewer.css").read_text()
js = (HERE.parent / "viewer" / "viewer.js").read_text()
js += "\n" + (HERE.parent / "viewer" / "search.js").read_text()
meta = doc["meta"]
data = json.dumps(doc, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\u0021--")
fonts = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;'
         '0,6..72,700;1,6..72,400;1,6..72,600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">')
ICON_TOC = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M4 6h16M4 12h16M4 18h10"/></svg>')
ICON_FIND = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>')
ICON_BACK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>')
ICON_UP = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 15 6-6 6 6"/></svg>')
ICON_DOWN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>')
ICON_SET = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M20 7h-9M14 17H5"/><circle cx="17" cy="17" r="3"/><circle cx="7" cy="7" r="3"/></svg>')
LOGO = (HERE.parent / "logo" / "conifer-icon.svg").read_text().replace('width="64" height="64"', 'class="logo"').replace("<svg xmlns=\"http://www.w3.org/2000/svg\"", "<svg")
LOGO = re.sub(r"<!--.*?-->", "", LOGO, flags=re.S).strip()
body = f"""<title>Conifer Reader Mockup</title>
{fonts}
<style>
{css}
{out["css"]}
</style>
<div class="app">
<header class="bar" id="bar">
 <div class="bar-row" id="bar-row">
  <button type="button" class="bar-btn" data-open="contents" aria-label="Contents">{ICON_TOC}</button>
  <button type="button" class="bar-pill" id="back" hidden title="Back to where you were"></button>
  <button type="button" class="bar-title" id="bar-title" data-open="contents" title="Contents"></button>
  <button type="button" class="bar-pill" data-open="settings" id="who" title="Who you are reading as"></button>
  <button type="button" class="bar-btn" data-open="search" aria-label="Search in the paper">{ICON_FIND}</button>
  <button type="button" class="bar-btn" data-open="settings" aria-label="Settings">{ICON_SET}</button>
 </div>
 <div id="find-row" hidden><button type="button" class="bar-btn" data-find="close" aria-label="Close the search">{ICON_BACK}</button><input id="find-input" type="search" autocomplete="off" spellcheck="false" placeholder="Words, or TeX: phi, x^2, \\frac{{1}}{{2}}"><span id="find-count"></span><button type="button" class="bar-btn" data-find="prev" aria-label="Previous match">{ICON_UP}</button><button type="button" class="bar-btn" data-find="next" aria-label="Next match">{ICON_DOWN}</button></div>
 <div class="dial" role="radiogroup" aria-label="How much of the paper to show" id="dial"></div>
</header>
<main class="page">
 <header class="titleblock">
  <p class="kicker">{LOGO}{html.escape(meta["kicker"])}</p>
  <h1 class="title">{html.escape(meta["title"])}</h1>
  <p class="authors">{html.escape(", ".join(meta["authors"]))} · {html.escape(meta["date"])}</p>
  <p class="note">{html.escape(meta["note"])} The dial above sets how much of the paper is shown, and the pill who you are reading as; every summary opens in place, dotted terms carry definitions, and ? marks the parts with questions.</p>
 </header>
 <div id="paper"></div>
 <footer class="colophon">A mockup for project Conifer: one document, four depths. The text is drawn from <code>semicircle.tree.json</code>; formulas were drawn once with MathJax through Epsilon.</footer>
</main>
</div>
<div id="scrim" class="scrim" hidden></div>
<aside id="sheet" class="sheet" hidden aria-live="polite"><div class="sheet-head"><h2 id="sheet-title"></h2><button type="button" class="x-btn" data-close aria-label="Close">&times;</button></div><div id="sheet-body"></div></aside>
<div id="pop" class="pop" hidden></div>
<div id="toast" role="status" hidden></div>
{out["cache"]}
<script type="application/json" id="conifer-doc">{data}</script>
<script>
{js}
</script>
"""
(HERE / "conifer-mockup.artifact.html").write_text(body)
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{body}
</head>
<body></body>
</html>
"""
# the full page: the fragment's title/style/link belong in <head>; everything else in <body>
head_end = body.index("</style>") + len("</style>")
page = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        + '<link rel="icon" href="data:image/svg+xml,' + urllib.parse.quote((HERE.parent / "logo" / "conifer-icon.svg").read_text().replace("currentColor", "#1d5b98")) + '">\n'
        + body[:head_end] + "\n</head>\n<body>\n" + body[head_end:] + "\n</body>\n</html>\n")
(HERE / "conifer-mockup.html").write_text(page)
print("wrote conifer-mockup.html (%d KB) and conifer-mockup.artifact.html" % (len(page.encode()) // 1024))
