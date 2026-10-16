#!/usr/bin/env python3
"""conifer build: a paper's skeleton + its drafted layers -> tree.json and a self-contained page.

    python3 tools/build_tree.py papers/2608.21511

Expects in the paper folder:
  doc/            the Epsilon document (paper.json, math.json, images/)
  skeleton.json   from tools/skeleton.py
  layers.py       the drafted layers: ROOT_GIST, ROOT_BRIEF, GIST, BRIEF, BACKGROUND, DEFS, QUESTIONS, KEY, AUDIENCES, VARIANTS
Writes:
  tree.json       the Conifer document (TeX intact in the layers; the paper's own markup in the bodies)
  tree.html       the page, self-contained (Epsilon's drawn math and images inside; the layers' math drawn the same way)
  tree.artifact.html   the same without the document skeleton, to publish as a Claude artifact

The layers refer to nodes by the ids in skeleton.json / outline.md. The build checks every id and every quote,
marks the mentions of defined terms in the text, and reports what is stale (a summary whose covered text changed).
"""
import base64
import html
import importlib.util
import json
import re
import subprocess
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
import loader  # noqa: E402
import tempfile
import urllib.parse
from pathlib import Path

EPSILON = Path("/Users/urbach/IAS Dropbox/Erez Urbach/research/epsilon")
HERE = Path(__file__).resolve().parent.parent
paper = Path(sys.argv[1]).resolve()
doc = paper / "doc"
D = json.loads((doc / "paper.json").read_text())
M = json.loads((doc / "math.json").read_text())
S = json.loads((paper / "skeleton.json").read_text())
if not S["meta"].get("arxiv") and (paper / "meta.json").exists():          # the arXiv number, from the fetch
    S["meta"]["arxiv"] = json.loads((paper / "meta.json").read_text()).get("id") or paper.name
sys.path.insert(0, str(paper))                 # the layers may be split over several files in the paper's folder
spec = importlib.util.spec_from_file_location("layers", paper / "layers.py")
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
problems = []

# ---------------------------------------------------------------- the tree, with the layers merged in
byid = {}


def index(n):
    byid[n["id"]] = n
    for c in n.get("children", []):
        index(c)


index(S["root"])


def rendition(x, status="ai-draft"):
    if x is None:
        return None
    if isinstance(x, str):
        return {"html": x, "status": status}
    r = dict(x)
    r.setdefault("status", status)
    if "variants" in r:
        r["variants"] = {k: rendition(v, status) for k, v in r["variants"].items()}
    return r


root = S["root"]
root["gist"] = rendition(L.ROOT_GIST, getattr(L, "ROOT_STATUS", "ai-draft"))
root["brief"] = rendition(L.ROOT_BRIEF, getattr(L, "ROOT_STATUS", "ai-draft"))
for table, key in ((L.GIST, "gist"), (L.BRIEF, "brief")):
    for nid, text in table.items():
        if nid not in byid:
            problems.append("%s for unknown node %s" % (key, nid))
            continue
        byid[nid][key] = rendition(text)
for nid, v in getattr(L, "VARIANTS", {}).items():
    for key, variants in v.items():
        target = root if nid == "root" else byid.get(nid)
        if not target or not target.get(key):
            problems.append("variants for missing %s of %s" % (key, nid))
            continue
        target[key]["variants"] = {k: rendition(t) for k, t in variants.items()}
for bg in getattr(L, "BACKGROUND", []):
    after = byid.get(bg["after"])
    if not after:
        problems.append("background %s after unknown node %s" % (bg["id"], bg["after"]))
        continue
    parent = next(p for p in byid.values() if after in p.get("children", []))
    node = {"id": bg["id"], "kind": "background", "title": bg["title"], "audience": bg["audience"], "fold": True, "body": bg["body"]}
    parent["children"].insert(parent["children"].index(after) + 1, node)
    byid[node["id"]] = node

# every grounding span must point at nodes that exist
for n in list(byid.values()) + [root]:
    for key in ("gist", "brief"):
        r = n.get(key)
        if not r:
            continue
        for cov in re.findall(r'data-covers="([^"]+)"', r["html"]):
            for cid in cov.split():
                if cid not in byid:
                    problems.append("%s of %s covers unknown node %s" % (key, n["id"], cid))
        for k, v in (r.get("variants") or {}).items():
            for cov in re.findall(r'data-covers="([^"]+)"', v["html"]):
                for cid in cov.split():
                    if cid not in byid:
                        problems.append("%s/%s of %s covers unknown node %s" % (key, k, n["id"], cid))

# the abstract becomes the first node of the paper
if S["meta"].get("abstractHtml"):
    root["children"].insert(0, {"id": "abstract", "kind": "abstract", "title": "Abstract", "body": S["meta"]["abstractHtml"]})
    byid["abstract"] = root["children"][0]

# ---------------------------------------------------------------- definitions: anchors and mentions
items = D["math"]["items"]


def plain_text(h):
    """The text of a node as a reader sees it, formulas as their TeX between $ signs (for quotes)."""
    t = re.sub(r'<l2m-math n="(\d+)"></l2m-math>', lambda m: "\x01%s\x01" % m.group(1), h)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub("\x01(\\d+)\x01", lambda m: "$" + items[int(m.group(1))]["tex"].strip() + "$", t)
    return html.unescape(re.sub(r"\s+", " ", t))


def mark_mentions(h, aliases, def_id, defining):
    """Wrap the first mention of any alias in the text segments of H (never inside a tag or a formula)."""
    parts = re.split(r"(<[^>]+>)", h)
    done = False
    skip = 0                                      # inside <a ...>...</a> or a heading, leave the text alone
    out = []
    for part in parts:
        if part.startswith("<"):
            if re.match(r"<(a|h\d|figcaption|span class=\"capname\")\b", part):
                skip += 1
            elif re.match(r"</(a|h\d|figcaption|span)>", part) and skip:
                skip -= 1
            out.append(part)
            continue
        if done or skip:
            out.append(part)
            continue
        for al in aliases:
            m = re.search(r"(?<![\w-])" + re.escape(al) + r"(?![\w-])", part)
            if m:
                tag = "dfn" if defining else "a"
                part = part[:m.start()] + '<%s data-def="%s">%s</%s>' % (tag, def_id, m.group(0), tag) + part[m.end():]
                done = True
                break
        out.append(part)
    return "".join(out)


defs = []
for d in getattr(L, "DEFS", []):
    d = dict(d)
    at = d.get("at") or {}
    if at.get("node") not in byid:
        problems.append("definition %s anchored to unknown node %s" % (d["id"], at.get("node")))
    elif at.get("quote") and at["quote"] not in plain_text(byid[at["node"]].get("body", "")):
        problems.append("definition %s: quote not found in %s: %r" % (d["id"], at["node"], at["quote"][:50]))
    aliases = sorted(set([d["term"]] + d.get("aliases", [])), key=len, reverse=True)
    for n in byid.values():
        if n.get("body") and n["kind"] not in ("references", "footnotes"):
            n["body"] = mark_mentions(n["body"], aliases, d["id"], n["id"] == at.get("node"))
    defs.append(d)

questions = []
for q in getattr(L, "QUESTIONS", []):
    if q["at"]["node"] not in byid:
        problems.append("question %s at unknown node %s" % (q["id"], q["at"]["node"]))
    for a in q.get("answeredBy", []):
        if a not in byid:
            problems.append("question %s answered by unknown node %s" % (q["id"], a))
    questions.append(q)

LEVELS = [
    {"key": "gist", "label": "Gist", "hint": "the trunk: the three things to know"},
    {"key": "brief", "label": "Summary", "hint": "the branches: one page, every sentence opens"},
    {"key": "paper", "label": "Paper", "hint": "the foliage: the full text, with the roots folded"},
]
cone = {
    "format": "conifer-doc", "version": 1,
    "meta": dict(S["meta"], key=getattr(L, "KEY", {}), defaultAudience=getattr(L, "DEFAULT_AUDIENCE", "physicist"),
                 kicker=getattr(L, "KICKER", S["meta"].get("kicker")), date=getattr(L, "DATE", ""), note=getattr(L, "NOTE", ""),
                 macros=D["math"].get("macros", {})),
    "levels": LEVELS, "audiences": getattr(L, "AUDIENCES", []),
    "root": root, "defs": defs, "questions": questions,
}
(paper / "tree.json").write_text(json.dumps(cone, indent=1, ensure_ascii=False) + "\n")
for p in problems:
    print("problem:", p, file=sys.stderr)
print("tree.json: %d nodes, %d definitions, %d questions" % (len(byid), len(defs), len(questions)))

# ---------------------------------------------------------------- drawing: the paper's formulas from Epsilon's cache, the layers' with MathJax
svgs = M["svg"] if M.get("key") == D["math"]["key"] and len(M.get("svg", [])) == len(items) else None
if svgs is None:
    sys.exit("math.json does not match paper.json; run Epsilon's converter again")
new_items = []
SKIP = {"id", "quote", "node", "covers", "answeredBy", "at", "key", "kind", "role", "status", "source", "number", "format", "generator", "term", "aliases", "audience", "after", "hash", "doc", "arxiv", "title"}


def mark(tex, display):
    new_items.append({"tex": tex, "display": display})
    return "\x00%d\x00" % (len(new_items) - 1)


def collect(s):
    def disp(m):
        tex = m.group(1)
        lab = re.search(r"\\label\{([^}]*)\}", tex)
        tex = re.sub(r"\\label\{[^}]*\}", "", tex)
        return '</p><div class="display"%s><div class="eqbody">%s</div></div><p class="cont">' % (' id="%s"' % lab.group(1) if lab else "", mark(tex.strip(), True))
    s = re.sub(r"\\\[(.+?)\\\]", disp, s, flags=re.S)
    s = re.sub(r"(?<!\\)\$(.+?)(?<!\\)\$", lambda m: mark(m.group(1), False), s, flags=re.S)
    return re.sub(r'<p(?: class="cont")?>\s*</p>', "", s)


def walk(o, key=None):
    if isinstance(o, dict):
        return {k: walk(v, k) for k, v in o.items()}
    if isinstance(o, list):
        return [walk(v, key) for v in o]
    if isinstance(o, str) and key not in SKIP and ("$" in o or "\\[" in o) and "<l2m-math" not in o:
        return collect(o)
    return o


page_doc = walk(cone)
if new_items:
    with tempfile.TemporaryDirectory() as td:
        job, res = Path(td) / "job.json", Path(td) / "res.json"
        job.write_text(json.dumps({"items": new_items, "macros": D["math"].get("macros", {}), "packages": D["math"].get("packages", ["base", "ams"])}))
        r = subprocess.run(["node", str(EPSILON / "render_math.js"), str(job), str(res)], capture_output=True, text=True)
        if r.returncode:
            sys.exit("render_math.js failed:\n" + r.stderr)
        out = json.loads(res.read_text())
    for e in out.get("errors", []):
        print("math error in the layers:", e["message"], "in", e["tex"][:70], file=sys.stderr)
    for k in out.get("undefined", []):
        print("undefined macro in the layers:", new_items[k]["tex"][:70], file=sys.stderr)
    new_svgs = out["out"]
else:
    new_svgs = []
print("layers' formulas drawn:", len(new_items))

images = {}
for f in (doc / "images").iterdir():
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "svg": "image/svg+xml", "gif": "image/gif", "webp": "image/webp"}.get(f.suffix[1:].lower(), "application/octet-stream")
    images[f.name] = "data:%s;base64,%s" % (mime, base64.b64encode(f.read_bytes()).decode())


HL = '<span class="mjx-hl" aria-hidden="true"></span>'


def with_band(svg):
    """Under the formula, an unseen picture as wide as its drawing (viewer.css .mjx-hl): a selection that takes the
    formula in is shaded there by the browser itself, at its line's whole height, as the words round it are."""
    m = re.search(r'<svg[^>]*?\swidth="([\d.]+ex)"', svg)
    a = svg.find(">")
    if not m or a < 0 or not svg.startswith("<mjx-container"):
        return svg
    return svg[:a] + ' style="--w:%s">' % m.group(1) + HL + svg[a + 1:]


def with_tex(svg, tex):
    return with_band(svg.replace("<mjx-container", '<mjx-container data-tex="%s"' % html.escape(tex.strip(), quote=True), 1))


def fill(o):
    if isinstance(o, dict):
        return {k: fill(v) for k, v in o.items()}
    if isinstance(o, list):
        return [fill(v) for v in o]
    if isinstance(o, str):
        o = re.sub(r'<l2m-math n="(\d+)"></l2m-math>', lambda m: with_tex(svgs[int(m.group(1))], items[int(m.group(1))]["tex"]), o)
        o = re.sub("\x00(\\d+)\x00", lambda m: with_tex(new_svgs[int(m.group(1))], new_items[int(m.group(1))]["tex"]), o)
        o = re.sub(r'src="images/([^"]+)"', lambda m: 'src="%s"' % images.get(m.group(1), "images/" + m.group(1)), o)
        return o
    return o


page_doc = fill(page_doc)

# ---------------------------------------------------------------- the page
css = (HERE / "viewer" / "viewer.css").read_text() + "\n" + M.get("css", "")
js = (HERE / "viewer" / "viewer.js").read_text()
js += "\n" + (HERE / "viewer" / "search.js").read_text()
js += "\n" + (HERE / "viewer" / "copy.js").read_text()
meta = page_doc["meta"]
data = json.dumps(page_doc, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\u0021--")
fonts = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;'
         '0,6..72,700;1,6..72,400;1,6..72,600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">')
ICON_TOC = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M4 6h16M4 12h16M4 18h10"/></svg>')
ICON_FIND = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>')
ICON_EXPAND = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6"/><path d="M20 4l-7 7"/><path d="M10 20H4v-6"/><path d="M4 20l7-7"/></svg>')
ICON_CLOSE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M7 7l10 10M17 7 7 17"/></svg>')
ICON_BACK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>')
ICON_UP = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 15 6-6 6 6"/></svg>')
ICON_DOWN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>')
ICON_SET = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M20 7h-9M14 17H5"/><circle cx="17" cy="17" r="3"/><circle cx="7" cy="7" r="3"/></svg>')
LOGO_BAR = (HERE / "logo" / "conifer-icon.svg").read_text().replace('width="64" height="64"', 'class="bar-logo"').replace('<svg xmlns="http://www.w3.org/2000/svg"', "<svg")
LOGO_BAR = re.sub(r"<!--.*?-->", "", LOGO_BAR, flags=re.S).strip()
LOGO = (HERE / "logo" / "conifer-icon.svg").read_text().replace('width="64" height="64"', 'class="logo"').replace('<svg xmlns="http://www.w3.org/2000/svg"', "<svg")
LOGO = re.sub(r"<!--.*?-->", "", LOGO, flags=re.S).strip()
title_html = fill(S["meta"].get("titleHtml") or html.escape(meta["title"]))
page_title = getattr(L, "PAGE_TITLE", meta["title"])
LOADER_HTML, LOADER_CSS = loader.build()
body = f"""<title>{html.escape(page_title)}</title>
{fonts}
<style>
{css}
{LOADER_CSS}
</style>
{LOADER_HTML}<div class="app">
<header class="bar" id="bar">
 <div class="bar-row" id="bar-row">
  <button type="button" class="bar-btn" data-open="contents" aria-label="Contents">{LOGO_BAR}</button>
  <button type="button" class="bar-pill" id="back" hidden title="Back to where you were"></button>
  <button type="button" class="bar-title" id="bar-title" data-open="contents" title="Contents"></button>
  <button type="button" class="bar-btn bar-search" data-open="search" aria-label="Search in the paper"><span class="i-find">{ICON_FIND}</span><span class="i-close">{ICON_CLOSE}</span></button>
  <button type="button" class="bar-btn" data-open="settings" aria-label="Settings">{ICON_SET}</button>
 </div>
 <div class="lane" id="lane">
  <div class="dial" role="radiogroup" aria-label="How much of the paper to show" id="dial"></div>
  <div id="find-row" hidden><input id="find-input" type="search" autocomplete="off" spellcheck="false" placeholder="Words, or TeX: phi, x^2, \\frac{{1}}{{2}}" aria-label="Search in the paper"><span id="find-count"></span><button type="button" class="bar-btn" data-find="prev" aria-label="Previous match">{ICON_UP}</button><button type="button" class="bar-btn" data-find="next" aria-label="Next match">{ICON_DOWN}</button></div>
  <svg class="dial-line" aria-hidden="true"><line class="track"/><line class="lit"/><g class="nodes"></g></svg>
 </div>
</header>
<main class="page">
 <header class="titleblock">
  <p class="kicker">{LOGO}{html.escape(meta.get("kicker") or "")}</p>
  <h1 class="title">{title_html}</h1>
  <p class="authors">{html.escape(", ".join(meta["authors"]))}{(" · " + html.escape(meta["date"])) if meta.get("date") else ""}</p>
 </header>
 <div id="paper"></div>
 <footer class="colophon">arXiv:{html.escape(meta.get("arxiv") or "")}, grown into a Conifer tree: the trunk is the gist, the branches the summary, the foliage the paper, the roots its appendices. The paper's text is the author's, converted with Epsilon; the summaries, definitions, background notes and questions were drafted by an AI reader and carry their status.</footer>
</main>
</div>
<div id="scrim" class="scrim" hidden></div>
<aside id="sheet" class="sheet" hidden aria-live="polite"><div class="sheet-head"><h2 id="sheet-title"></h2><button type="button" class="x-btn" data-close aria-label="Close"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 3l6 6M9 3l-6 6"/></svg></button></div><div id="sheet-body"></div></aside>
<section id="peek" class="peek" hidden aria-label="Peek"><div class="peek-head" title="Drag to resize"><span class="peek-grip" aria-hidden="true"></span><div class="peek-row"><button type="button" class="bar-btn peek-back" data-peekback aria-label="Back in the peek" hidden>{ICON_BACK}</button><div id="peek-title" class="peek-title"></div><button type="button" class="x-btn peek-go" data-peekgo aria-label="Read it in the page" title="Read it in the page">{ICON_EXPAND}</button><button type="button" class="x-btn" data-peekclose aria-label="Close the peek"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 3l6 6M9 3l-6 6"/></svg></button></div></div><div id="peek-body" class="peek-body"></div></section>
<div id="pop" class="pop" hidden></div>
<div id="toast" role="status" hidden></div>
{M.get("cache", "")}
<script type="application/json" id="conifer-doc">{data}</script>
<script>
{js}
</script>
"""
(paper / "tree.artifact.html").write_text(body)
head_end = body.index("</style>") + len("</style>")
favicon = ('<link rel="icon" href="../favicon.ico" sizes="any">\n<link rel="icon" href="../icons/favicon-32.png" type="image/png" sizes="32x32">\n<link rel="icon" href="../icons/favicon.svg" type="image/svg+xml">\n'
           '<link rel="apple-touch-icon" href="../icons/apple-touch-icon.png">\n<link rel="manifest" href="../manifest.webmanifest">\n'
           '<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">\n<meta name="theme-color" content="#0c0e11" media="(prefers-color-scheme: dark)">\n'
           '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="Conifer">\n<meta name="mobile-web-app-capable" content="yes">\n'
           '<meta name="description" content="' + html.escape(meta["title"]) + ', as a Conifer tree: read it at any depth.">\n')
SW = '<script>if ("serviceWorker" in navigator && /^https?:/.test(location.protocol)) navigator.serviceWorker.register("../sw.js").catch(function () {});</script>\n'
page = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n" + favicon
        + body[:head_end] + "\n</head>\n<body>\n" + body[head_end:] + SW + "\n</body>\n</html>\n")
(paper / "tree.html").write_text(page)
print("wrote tree.html (%d KB) and cone.artifact.html%s" % (len(page.encode()) // 1024, "; %d problems" % len(problems) if problems else ""))
