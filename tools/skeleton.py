#!/usr/bin/env python3
"""conifer skeleton: an Epsilon document (paper.json) -> the cone's tree with empty layers, and an outline to draft from.

    python3 tools/skeleton.py papers/2608.21511/doc  [-o papers/2608.21511]

Writes <out>/skeleton.json (the tree: sections, paragraphs grouped with their displays, figures, boxes, footnotes,
references; stable ids; a hash of each node's text) and <out>/outline.md (every node's id and text, math as TeX),
which is what the layers are drafted from.
"""
import argparse
import hashlib
import json
import re
import textwrap
from html.parser import HTMLParser
from pathlib import Path

VOID = {"img", "br", "hr", "l2m-math", "l2m-slot", "input", "meta", "link", "wbr", "source", "col"}


class Top(HTMLParser):
    """Splits a flat HTML body into its top-level elements, with their raw markup."""

    def __init__(self, raw):
        super().__init__(convert_charrefs=False)
        self.raw = raw
        self.lines = [0] + [i + 1 for i, ch in enumerate(raw) if ch == "\n"]
        self.depth = 0
        self.items = []
        self.cur = None

    def off(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            if self.depth == 0:
                s = self.off()
                self.items.append({"tag": tag, "attrs": dict(attrs), "html": self.raw[s:s + len(self.get_starttag_text())]})
            return
        if self.depth == 0:
            self.cur = {"tag": tag, "attrs": dict(attrs), "start": self.off()}
        self.depth += 1

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        self.depth -= 1
        if self.depth == 0 and self.cur:
            end = self.raw.index(">", self.off()) + 1
            self.cur["html"] = self.raw[self.cur["start"]:end]
            self.items.append(self.cur)
            self.cur = None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    doc = Path(a.doc)
    out = Path(a.out) if a.out else doc.parent
    d = json.loads((doc / "paper.json").read_text())
    items = d["math"]["items"]
    heads = {h["id"]: h for h in d["headings"]}

    def tex_of(html):
        """Markup -> readable text with the formulas as TeX."""
        def m(mo):
            it = items[int(mo.group(1))]
            return ("\n\\[ %s \\]\n" if it["display"] else "$%s$") % it["tex"].strip()
        t = re.sub(r'<l2m-math n="(\d+)"></l2m-math>', lambda mo: "\x01%s\x01" % mo.group(1), html)
        t = re.sub(r'<a class="fnref"[^>]*>([^<]*)</a>', r" [fn \1]", t)
        t = re.sub(r"<(/p|/div|/li|/figcaption|br)[^>]*>", "\n", t)
        t = re.sub(r"<[^>]+>", "", t)
        t = re.sub("\x01(\\d+)\x01", lambda mo: m(mo), t)
        t = t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#8217;", "’")
        return re.sub(r"\n{3,}", "\n\n", t).strip()

    def plain(html):
        return re.sub(r"\s+", " ", tex_of(html)).strip()

    def digest(html):
        return hashlib.sha1(plain(html).encode()).hexdigest()[:12]

    def node(**kw):
        n = {"id": kw["id"], "kind": kw["kind"]}
        for k in ("number", "title", "titleHtml", "body", "children", "fold"):
            if kw.get(k) not in (None, "", False):
                n[k] = kw[k]
        if n.get("body"):
            n["hash"] = digest(n["body"])
        return n

    top = Top(d["body"])
    top.feed(d["body"])
    root = {"id": "root", "kind": "paper", "children": []}
    stack = [(0, root)]
    meta = {"title": d["title"], "authors": d["authors"], "arxiv": None, "abstractHtml": "", "kicker": d.get("kicker")}
    counters = {}
    cur_par = None

    def section_id():
        return stack[-1][1]["id"]

    def next_id(prefix):
        counters[prefix] = counters.get(prefix, 0) + 1
        return "%s-%s%d" % (section_id(), prefix, counters[prefix])

    def add(n):
        stack[-1][1]["children"].append(n)

    for it in top.items:
        tag, attrs, html = it["tag"], it["attrs"], it["html"]
        cls = attrs.get("class", "")
        if tag == "header":
            ab = re.search(r'<section class="abstract"[^>]*>(.*?)</section>', html, re.S)
            if ab:
                meta["abstractHtml"] = re.sub(r"<h2[^>]*>.*?</h2>", "", ab.group(1), flags=re.S).strip()
            t = re.search(r"<h1>(.*?)</h1>", html, re.S)
            if t:
                meta["titleHtml"] = t.group(1)
            continue
        if tag in ("h2", "h3", "h4", "h5"):
            level = int(tag[1]) - 1
            h = heads.get(attrs.get("id"), {})
            number = h.get("number", "")
            title_html = re.sub(r'<span class="secnum">.*?</span>\s*', "", html)
            title_html = re.sub(r"^<h\d[^>]*>|</h\d>$", "", title_html).strip()
            kind = "appendix" if re.match(r"^[A-Z](\.\d+)*$", number or "") else "section"
            n = node(id=attrs.get("id") or next_id("sec"), kind=kind, number=number, title=plain(title_html), titleHtml=title_html,
                     children=[], fold=(kind == "appendix" and "." not in number))
            n["children"] = []
            while stack[-1][0] >= level:
                stack.pop()
            add(n)
            stack.append((level, n))
            counters.clear()
            cur_par = None
            continue
        if tag == "section" and "footnotes" in cls:
            add(node(id="footnotes", kind="footnotes", title="Footnotes", body=html))
            continue
        if tag == "section" and "references" in cls:
            add(node(id="refs", kind="references", title="References", body=html))
            continue
        if tag == "figure":
            cap = re.search(r'<span class="capname">(.*?)</span>', html)
            kind = "table" if "table" in cls else "figure"
            add(node(id=attrs.get("id") or next_id("fig"), kind=kind, title=plain(cap.group(1)).rstrip(".:") if cap else kind.title(), body=html))
            cur_par = None
            continue
        if tag == "div" and re.search(r"\b(thm|defn|remark|proof)\b", cls):
            kind = {"thm": "theorem", "defn": "definition", "remark": "remark", "proof": "proof"}[re.search(r"\b(thm|defn|remark|proof)\b", cls).group(1)]
            name = re.search(r'<span class="(?:thm-name|proof-head)">(.*?)</span>', html)
            add(node(id=attrs.get("id") or next_id(kind), kind=kind, title=plain(name.group(1)).rstrip(".") if name else kind.title(), body=html, fold=(kind == "proof")))
            cur_par = None
            continue
        if tag == "p" and "cont" not in cls:
            n = node(id=next_id("p"), kind="paragraph", body=html)
            add(n)
            cur_par = n
            continue
        # a continuation: a display, a list, a continued paragraph, a quote
        if cur_par is not None:
            cur_par["body"] += "\n" + html
            cur_par["hash"] = digest(cur_par["body"])
        else:
            n = node(id=next_id("p"), kind="paragraph", body=html)
            add(n)
            cur_par = n

    skeleton = {
        "format": "conifer-doc", "version": 1,
        "meta": dict(meta, key={}, defaultAudience="physicist", source={"kind": "epsilon", "doc": str(doc)}),
        "levels": [
            {"key": "gist", "label": "Gist", "hint": "the three things to know"},
            {"key": "brief", "label": "Summary", "hint": "one page, every sentence opens"},
            {"key": "paper", "label": "Paper", "hint": "the full text, appendices folded"},
            {"key": "full", "label": "Everything", "hint": "appendices and proofs open"},
        ],
        "audiences": [],
        "root": root, "defs": [], "questions": [],
    }
    out.mkdir(parents=True, exist_ok=True)
    (out / "skeleton.json").write_text(json.dumps(skeleton, indent=1, ensure_ascii=False) + "\n")

    lines = ["# Outline of: " + d["title"], "", "Abstract:", "", tex_of(meta["abstractHtml"]), ""]
    count = {"nodes": 0, "words": 0}

    def walk(n, depth):
        count["nodes"] += 1
        head = "#" * min(depth + 1, 6)
        label = " ".join(x for x in (n.get("number"), n.get("title")) if x)
        lines.append("%s [%s] %s%s" % (head, n["id"], n["kind"], (": " + label) if label else ""))
        if n.get("body"):
            t = tex_of(n["body"])
            count["words"] += len(t.split())
            lines.append("")
            for para in t.split("\n"):
                lines.append(textwrap.fill(para, 110) if not para.startswith("\\[") else para)
            lines.append("")
        for c in n.get("children", []):
            walk(c, depth + 1)

    walk(root, 0)
    (out / "outline.md").write_text("\n".join(lines))
    print("skeleton: %d nodes, %d words; written to %s" % (count["nodes"], count["words"], out))


if __name__ == "__main__":
    main()
