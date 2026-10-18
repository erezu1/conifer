#!/usr/bin/env python3
"""Assemble the project's site that GitHub Pages serves (docs/, erezu1.github.io/conifer/): its page and the example.

    python3 example/build.py     # (after a change to the viewer or the example)
    python3 tools/site.py

docs/index.html              the project's page, with the example tree listed
docs/semicircle/index.html   the example tree (the Wigner semicircle, from random matrix theory)
docs/404.html                sends an old link to one of Erez's papers to where they now are
"""
import html
import json
import re
import shutil
import tempfile
import sys
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DOCS = HERE / "docs"
DOCS.mkdir(exist_ok=True)

# the project's page lists the example tree, the Wigner semicircle (example/); Erez's own papers are trees on his site
# (erezu1.github.io/papers/, built from his website's repository since 18 Oct 2026), and an old link to one of them
# here (/conifer/<arXiv id>/) is sent there by docs/404.html
PAPERS = "https://erezu1.github.io/papers/"
for d in DOCS.iterdir():                                       # the papers' folders, from before they moved
    if d.is_dir() and re.fullmatch(r"\d{4}\.\d{4,5}", d.name):
        shutil.rmtree(d)
cones = [{"key": "semicircle", "page": HERE / "example" / "semicircle.html", "data": HERE / "example" / "semicircle.tree.json", "doc": None}]

# THE INDEX DRAWS ITS FORMULAS (18 Oct, Erez): a title's and a gist's TeX is drawn here, at build time, with the paper's
# own macros by the renderer the trees use (Epsilon's render_math.js), slimmed, with one hidden set of glyphs for all
sys.path.insert(0, str(HERE / "tools"))
from paths import EPSILON  # noqa: E402
from slim import slim, merge_caches  # noqa: E402
caches = []


def draw_tex(texts, doc_json):
    """[TeX] -> [inline SVG markup], with the paper's macros; '' where a formula fails (its TeX is shown instead)."""
    if not texts:
        return []
    D = json.loads(doc_json.read_text())["math"] if doc_json and doc_json.exists() else {}
    with tempfile.TemporaryDirectory() as td:
        job, res = Path(td) / "job.json", Path(td) / "res.json"
        job.write_text(json.dumps({"items": [{"tex": t, "display": False} for t in texts], "macros": D.get("macros", {}), "packages": D.get("packages", ["base", "ams"])}))
        r = subprocess.run(["node", str(EPSILON / "render_math.js"), str(job), str(res)], capture_output=True, text=True)
        if r.returncode:
            return ["" for _ in texts]
        out = json.loads(res.read_text())
    caches.append(out.get("cache", ""))
    bad = {e["index"] for e in out.get("errors", [])}
    return ["" if k in bad else slim(svg) for k, svg in enumerate(out["out"])]


def with_math(text, doc_json):
    """Plain text with $TeX$ in it -> HTML, the formulas drawn."""
    parts = re.split(r"(\$[^$]+\$)", text)
    texs = [p[1:-1] for p in parts if p.startswith("$") and p.endswith("$") and len(p) > 1]
    drawn = iter(draw_tex(texs, doc_json))
    out = []
    for p in parts:
        if p.startswith("$") and p.endswith("$") and len(p) > 1:
            svg = next(drawn)
            f = svg if svg else html.escape(p)
            # a formula written onto a word (AdS$_3$, $N$-point) does not break from it
            w = re.search(r"\S+$", out[-1]) if out else None
            if w:
                out[-1] = out[-1][:w.start()]
                f = '<span class="nb">' + w.group(0) + f + "</span>"
            out.append(f)
        else:
            t = html.escape(p)
            m = re.match(r"\S+", t)
            if m and out and out[-1].endswith("</span>") and out[-1].startswith('<span class="nb">') and len(parts) > 1:
                out[-1] = out[-1][:-7] + m.group(0) + "</span>"
                t = t[m.end():]
            out.append(t)
    return "".join(out)


def context_of(gist_html):
    """The gist's Context, as text with its $TeX$ (the index shows it under the title)."""
    m = re.search(r"<li>\s*<b>Context</b>(.*?)</li>", gist_html, re.S)
    return text_of(m.group(1) if m else gist_html)


def text_of(h):
    """HTML -> text with its $TeX$; tags are removed only outside the formulas ($d<9$ is not a tag)."""
    t = "".join(p if p.startswith("$") and p.endswith("$") and len(p) > 1 else re.sub(r"<[^>]+>", " ", p)
                for p in re.split(r"(\$[^$]+\$)", h))
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def title_of(c, d):
    """The paper's title with its $TeX$: from the converted document, where the title's formulas are kept as TeX."""
    m = d["meta"]
    if c["doc"] and c["doc"].exists() and m.get("titleHtml"):
        items = json.loads(c["doc"].read_text())["math"]["items"]
        t = re.sub(r'<l2m-math n="(\d+)"></l2m-math>', lambda x: "$" + items[int(x.group(1))]["tex"].strip() + "$", m["titleHtml"])
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()
    return m["title"]


rows = []
for c in cones:
    if not c["data"].exists():                                  # a tree not built yet
        continue
    d = json.loads(c["data"].read_text())
    (DOCS / c["key"]).mkdir(exist_ok=True)
    shutil.copyfile(c["page"], DOCS / c["key"] / "index.html")
    if (c["page"].parent / "img").is_dir():
        shutil.rmtree(DOCS / c["key"] / "img", ignore_errors=True)
        shutil.copytree(c["page"].parent / "img", DOCS / c["key"] / "img")
    m = d["meta"]
    gh = (d["root"].get("gist") or {}).get("html", "")
    gist = context_of(gh)
    if len(gist) > 420:
        gist = gist[:420].rsplit(" ", 1)[0]
        if gist.count("$") % 2: gist = gist[:gist.rindex("$")].rstrip()   # (not inside a formula)
        gist += "…"
    rm = re.search(r"<b>Result</b>\s*<ul>(.*?)</ul>", gh, re.S)          # the gist's points: what the paper finds
    points = [text_of(p) for p in re.findall(r"<li[^>]*>(.*?)</li>", rm.group(1), re.S)] if rm else []
    if not points:                                             # (a Result written as prose is its one point)
        rp = re.search(r"<li>\s*<b>Result</b>(.*?)</li>", gh, re.S)
        points = [text_of(rp.group(1))] if rp else []
    parts = [x.strip() for x in (m.get("kicker") or "").split("·")]
    rows.append({"key": c["key"], "title": with_math(title_of(c, d), c["doc"]), "authors": m.get("authors", []),
                 "cat": parts[1] if len(parts) > 1 else "", "when": parts[2] if len(parts) > 2 else "",
                 "context": with_math(gist, c["doc"]), "points": [with_math(p, c["doc"]) for p in points],
                 "year": "20" + c["key"][:2] if re.fullmatch(r"\d{4}\.\d{4,5}", c["key"]) else "Example"})

# the app's files at the site's root: icons, the manifest, the service worker
(DOCS / "icons").mkdir(exist_ok=True)
for f in (HERE / "logo" / "icons").iterdir():
    shutil.copyfile(f, DOCS / "icons" / f.name)
shutil.copyfile(HERE / "logo" / "icons" / "favicon.ico", DOCS / "favicon.ico")
(DOCS / "icons" / "favicon.svg").write_text((HERE / "logo" / "conifer-icon.svg").read_text().replace("currentColor", "#1d5b98"))
shutil.copyfile(HERE / "viewer" / "manifest.webmanifest", DOCS / "manifest.webmanifest")
shutil.copyfile(HERE / "viewer" / "sw.js", DOCS / "sw.js")
HEAD = ('<link rel="icon" href="favicon.ico" sizes="any">\n<link rel="icon" href="icons/favicon-32.png" type="image/png" sizes="32x32">\n<link rel="icon" href="icons/favicon.svg" type="image/svg+xml">\n'
        '<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">\n<link rel="manifest" href="manifest.webmanifest">\n'
        '<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">\n<meta name="theme-color" content="#0c0e11" media="(prefers-color-scheme: dark)">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="Conifer">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="description" content="Conifer: papers you can read at any depth, from the gist to the full text.">')
css = (HERE / "viewer" / "viewer.css").read_text()
logo = (HERE / "logo" / "conifer-icon.svg").read_text().replace('width="64" height="64"', 'class="logo"').replace('<svg xmlns="http://www.w3.org/2000/svg"', "<svg")
logo = re.sub(r"<!--.*?-->", "", logo, flags=re.S).strip()
OWNER = "Erez Y. Urbach"                     # (bold in the author lines, as on erezu1.github.io)
PLUS = '<svg viewBox="0 0 12 12" aria-hidden="true"><path class="h" d="M2.5 6h7"/><path class="v" d="M6 2.5v7"/></svg>'


def entry(r):
    auth = "" if r["year"] == "Example" else ", ".join(('<b class="nb">%s</b>' if a == OWNER else '<span class="nb">%s</span>') % html.escape(a) for a in r["authors"])
    arx = ('<a href="https://arxiv.org/abs/%s">arXiv:%s</a>' % (r["key"], r["key"])) if r["year"] != "Example" else ""
    meta = "".join('<span>%s</span>' % x for x in (arx, html.escape(r["cat"]), html.escape(r["when"])) if x)
    finds = ('<details class="finds"><summary><span class="circ">%s</span>What it finds</summary><ul>%s</ul></details>'
             % (PLUS, "".join("<li>%s</li>" % p for p in r["points"]))) if r["points"] else ""
    return ('<li class="pub"><div class="pub-meta">%s</div><div class="pub-body"><h3 class="pub-title"><a href="%s/#gist">%s</a></h3>'
            '%s<p class="pub-context">%s</p>%s</div></li>' % (meta, r["key"], r["title"], ('<p class="pub-authors">%s</p>' % auth) if auth else "", r["context"], finds))


groups = []
for r in rows:
    if not groups or groups[-1][0] != r["year"]:
        groups.append((r["year"], []))
    groups[-1][1].append(r)
items = "\n".join('<section class="year"><h2 class="year-head">%s</h2><ul class="pub-list">%s</ul></section>'
                  % (html.escape(y), "".join(entry(r) for r in rs)) for y, rs in groups)
SUN = ('<svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2'
       'M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg>')
MOON = '<svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>'
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
<title>Conifer</title>
<script>/* the reader's theme, before anything is drawn (shared with the trees: conifer-reader) */
try {{ var t = JSON.parse(localStorage.getItem("conifer-reader") || "{{}}").theme; if (t === "light" || t === "dark") document.documentElement.dataset.theme = t; }} catch (e) {{}}</script>
{HEAD}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
{css}
body {{ background: var(--bg); color: var(--fg); }}
/* the bar with the project's name stays at the top as the list scrolls (as on erezu1.github.io); the year heads stick below it */
:root {{ --head-h: 3rem; }}
body {{ overflow-x: clip; }}
.site-head {{ position: sticky; top: 0; z-index: 5; display: flex; align-items: center; justify-content: space-between; gap: 1rem;
  height: var(--head-h); margin: -.6rem calc(50% - 50vw) 0; padding-inline: calc(50vw - 50%);
  background: color-mix(in srgb, var(--bg) 82%, transparent); backdrop-filter: saturate(1.3) blur(10px); -webkit-backdrop-filter: saturate(1.3) blur(10px); }}
.site-head .brand {{ margin: 0; color: var(--muted); white-space: nowrap; }}
.page .site-head a.brand {{ border-bottom: 0; background: none; }}
.page .site-head a.brand:hover {{ color: var(--fg); }}
.theme-btn {{ width: 2.25rem; height: 2.25rem; border: 0; background: none; color: var(--accent); cursor: pointer; display: grid; place-items: center; padding: 0; border-radius: 999px; }}
.theme-btn:hover {{ background: var(--accent-soft); }}
.theme-btn svg {{ width: 20px; height: 20px; grid-area: 1 / 1; fill: none; stroke: currentColor; stroke-linecap: round; stroke-linejoin: round; transition: opacity .25s, transform .35s var(--ease-out); }}
.theme-btn svg * {{ vector-effect: non-scaling-stroke; stroke-width: 1.25px; }}
.theme-btn .moon {{ opacity: 0; transform: rotate(-60deg) scale(.6); }}
:root[data-theme="dark"] .theme-btn .sun {{ opacity: 0; transform: rotate(60deg) scale(.6); }}
:root[data-theme="dark"] .theme-btn .moon {{ opacity: 1; transform: none; }}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) .theme-btn .sun {{ opacity: 0; transform: rotate(60deg) scale(.6); }}
  :root:not([data-theme="light"]) .theme-btn .moon {{ opacity: 1; transform: none; }}
}}
.page .intro {{ font: 400 1rem/1.55 var(--sans); color: var(--muted); max-width: 40rem; margin: .6rem 0 .3rem; text-align: left; hyphens: manual; }}
.depths {{ list-style: none; padding: 0; margin: .5rem 0 0; display: grid; gap: .35rem; font: 400 .95rem/1.5 var(--sans); color: var(--muted); max-width: 40rem; }}
.page .depths li {{ text-align: left; hyphens: manual; -webkit-hyphens: manual; }}
.depths b {{ font: 600 .74rem var(--sans); letter-spacing: .08em; text-transform: uppercase; color: var(--accent); margin-right: .5rem; }}
.year {{ margin-top: 1.6rem; }}
.year-head {{ position: sticky; top: var(--head-h); z-index: 2; margin: 0; padding: .45rem 0 .3rem; border-bottom: 1px solid var(--rule);
  font: 500 1.05rem var(--serif); color: var(--muted); background: color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); }}
.year-head::before {{ content: "§"; color: var(--accent); margin-right: .5rem; font-size: .9em; }}
.pub-list {{ list-style: none; margin: 0; padding: 0; }}
.pub {{ display: grid; grid-template-columns: 1fr; gap: .25rem 1rem; padding: 1.1rem 0; border-bottom: 1px solid color-mix(in srgb, var(--rule) 55%, transparent); }}
.pub:last-child {{ border-bottom: 0; }}
.pub-list li, .pub-list li * {{ text-align: left; hyphens: manual; -webkit-hyphens: manual; }}
.pub-meta {{ font: 400 .74rem/1.45 var(--sans); color: var(--muted); display: flex; flex-wrap: wrap; gap: .1rem .8rem; font-variant-numeric: tabular-nums; }}
.pub-meta a {{ color: var(--muted); text-decoration: none; }}
.pub-meta a:hover {{ color: var(--accent); }}
.pub-title {{ font: 500 1.24rem/1.3 var(--serif); margin: 0; text-wrap: pretty; }}
.pub-title a {{ color: var(--fg); text-decoration: none; background-image: linear-gradient(currentColor, currentColor); background-repeat: no-repeat; background-size: 0 1px; background-position: 0 100%; transition: background-size .3s var(--ease-out); }}
.pub-title a:hover {{ background-size: 100% 1px; }}
.pub-authors {{ font: 400 .88rem var(--sans); color: var(--muted); margin: .25rem 0 0; }}
.pub-authors b {{ color: var(--fg); font-weight: 600; }}
.pub .nb {{ white-space: nowrap; }}
.pub-context {{ font: 400 1rem/1.5 var(--serif); color: color-mix(in srgb, var(--fg) 82%, var(--muted)); margin: .5rem 0 0; max-width: 42rem; }}
.finds {{ margin-top: .45rem; max-width: 42rem; }}
.finds summary {{ list-style: none; cursor: pointer; display: inline-flex; align-items: center; gap: .45rem; font: 500 .72rem var(--sans); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }}
.finds summary::-webkit-details-marker {{ display: none; }}
.finds summary:hover {{ color: var(--accent); }}
.finds .circ {{ width: 1.15rem; height: 1.15rem; border-radius: 999px; border: 1px solid color-mix(in srgb, var(--muted) 45%, transparent); display: grid; place-items: center; }}
.finds summary:hover .circ {{ border-color: var(--accent); }}
.finds .circ svg {{ width: 9px; height: 9px; fill: none; stroke: currentColor; stroke-linecap: round; }}
.finds .circ svg * {{ vector-effect: non-scaling-stroke; stroke-width: 1.25px; }}
.finds[open] .circ .v {{ display: none; }}
.finds ul {{ list-style: none; margin: .5rem 0 0; padding: 0; display: grid; gap: .35rem; font: 400 .97rem/1.5 var(--serif); color: color-mix(in srgb, var(--fg) 85%, var(--muted)); }}
.finds li {{ position: relative; padding-left: 1.05rem; }}
.finds li::before {{ content: ""; position: absolute; left: .2rem; top: .62em; width: 5px; height: 5px; border-radius: 50%; background: var(--accent); }}
@media (min-width: 720px) {{
  .pub {{ grid-template-columns: 8.5rem 1fr; }}
  .pub-meta {{ flex-direction: column; gap: .15rem; padding-top: .35rem; }}
}}
</style>
</head>
<body>
<main class="page">
 <header class="site-head"><a class="brand kicker" href="./">{logo}Project Conifer</a><button type="button" class="theme-btn" id="theme-btn" aria-label="Switch between light and dark">{SUN}{MOON}</button></header>
 <header class="titleblock">
  <h1 class="title">From the gist down</h1>
  <p class="intro">Each paper opens on a short card and goes deeper when you want it to. Switch between the depths with the tabs at the top of a paper.</p>
  <ul class="depths">
   <li><b>Gist</b>the question, what the paper finds and why it matters: a minute.</li>
   <li><b>Summary</b>one page; tap a sentence to see the paragraphs it stands for.</li>
   <li><b>Paper</b>the full text, with a short summary under each section, definitions on dotted terms, background notes and questions.</li>
  </ul>
  <p class="intro">The text of each paper is its authors'. The gists, summaries, definitions, notes and questions are drafted by AI, marked as such, and not yet reviewed by the authors.</p>
 </header>
{items}
{merge_caches(*caches)}
 <footer class="colophon">Conifer turns a LaTeX paper into a tree like this one: <a href="https://github.com/erezu1/conifer">the code on GitHub</a>. The LaTeX is read by <a href="https://github.com/erezu1/epsilon">Epsilon</a>. Erez Y. Urbach's papers as trees: <a href="{PAPERS}">{PAPERS.split("//")[1]}</a>.</footer>
</main>
<script>
(function () {{
  var root = document.documentElement, btn = document.getElementById("theme-btn");
  var dark = function () {{ return root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches; }};
  btn.addEventListener("click", function () {{
    var t = dark() ? "light" : "dark"; root.dataset.theme = t;
    try {{ var s = JSON.parse(localStorage.getItem("conifer-reader") || "{{}}"); s.theme = t; localStorage.setItem("conifer-reader", JSON.stringify(s)); }} catch (e) {{}}
  }});
}})();
if ("serviceWorker" in navigator && /^https?:/.test(location.protocol)) navigator.serviceWorker.register("sw.js").catch(function () {{}});
</script>
</body>
</html>
"""
(DOCS / "index.html").write_text(page)
(DOCS / "404.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Conifer</title>
<script>
var m = location.pathname.match(/\\/conifer\\/(\\d{{4}}\\.\\d{{4,5}})\\/?/);
location.replace(m ? "{PAPERS}" + m[1] + "/" + location.hash : "./");
</script></head>
<body style="font: 1rem/1.5 system-ui, sans-serif; margin: 2rem;">Erez Y. Urbach's papers are at <a href="{PAPERS}">{PAPERS}</a>.</body></html>
""")
(DOCS / ".nojekyll").write_text("")
print("site:", ", ".join(r["key"] for r in rows), "->", DOCS)
