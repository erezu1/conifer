#!/usr/bin/env python3
"""conifer blind read: the abstract, every version of the gist and the paragraphs the gist cites, as plain text, for a fresh
reader who sees nothing else.
    python3 tools/blind_gist.py papers/2406.14605 > blind.txt
The reader is asked (skill/conifer-draft.md, section 3) whether the Result bullet states each result the abstract claims,
and whether anything under Why it matters is really another result.
"""
import sys, json, re, html, importlib.util
paper = sys.argv[1].rstrip("/")
sys.path.insert(0, paper)
for m in ("layers", "layers_gists", "layers_briefs", "layers_side"): sys.modules.pop(m, None)
spec = importlib.util.spec_from_file_location("layers", paper + "/layers.py"); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
S = json.load(open(paper + "/skeleton.json")); D = json.load(open(paper + "/doc/paper.json")); items = D["math"]["items"]
def txt(h):
    keep = []
    def stash(t): keep.append(t); return "\x01%d\x01" % (len(keep) - 1)
    h = re.sub(r'<l2m-math n="(\d+)"></l2m-math>', lambda m: stash("$" + items[int(m.group(1))]["tex"].strip() + "$"), h)
    h = re.sub(r"\$[^$]+\$", lambda m: stash(m.group(0)), h)
    h = re.sub(r"<ul[^>]*>\s*<li", "<ul>\n<li", h)
    depth, out, pos = 0, [], 0                   # a point of the Result is set as "  - …"
    for m in re.finditer(r"<(/?)(ul|li)\b[^>]*>", h):
        out.append(h[pos:m.start()]); pos = m.end()
        if m.group(2) == "ul": depth += -1 if m.group(1) else 1
        elif not m.group(1) and depth >= 2: out.append("\n  - ")
        elif m.group(1) and depth == 1: out.append("\n")
    h = "".join(out) + h[pos:]
    h = re.sub(r"<b>(.*?)</b>", r"\1:", h); h = re.sub(r"\n\s*\n", "\n", h)
    h = html.unescape(re.sub(r"<[^>]+>", "", h)).strip()
    return re.sub("\x01(\\d+)\x01", lambda m: keep[int(m.group(1))], h)
g = L.ROOT_GIST
parts = ["ABSTRACT\n" + txt(S["meta"]["abstractHtml"]), "GIST (default reader: a physicist from a neighbouring area)\n" + txt(g["html"])]
for k, v in g.get("variants", {}).items(): parts.append("GIST (%s)\n" % k + txt(v["html"]))
# the paragraphs the gist cites, so that the reader can tell a claim the paper supports from one it does not
byid = {}
def walk(n):
    byid[n["id"]] = n
    for c in n.get("children", []): walk(c)
walk(S["root"])
cited = []
for h in [g["html"]] + [v["html"] for v in g.get("variants", {}).values()]:
    for cov in re.findall(r'data-covers="([^"]+)"', h):
        for i in cov.split():
            if i not in cited and i in byid and byid[i].get("body"): cited.append(i)
parts.append("THE PARAGRAPHS THE GIST CITES\n" + "\n\n".join("[%s] %s" % (i, txt(byid[i]["body"])) for i in cited))
print("\n\n".join(parts))
