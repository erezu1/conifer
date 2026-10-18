#!/usr/bin/env python3
"""conifer check: measure a paper's drafted layers against the drafting rules (skill/conifer-draft.md).
    python3 tools/check_layers.py papers/2406.14605            # a report
    python3 tools/check_layers.py papers/2406.14605 --json     # the numbers, for comparing two drafts
It reads layers.py (and the files it imports), skeleton.json and doc/paper.json; it changes nothing.
"""
import html, importlib.util, json, re, sys
from pathlib import Path

paper = Path(sys.argv[1]).resolve()
AS_JSON = "--json" in sys.argv
D = json.loads((paper / "doc" / "paper.json").read_text())
S = json.loads((paper / "skeleton.json").read_text())
items = D["math"]["items"]
sys.path.insert(0, str(paper))
for m in ("layers", "layers_gists", "layers_briefs", "layers_side"):
    sys.modules.pop(m, None)
spec = importlib.util.spec_from_file_location("layers", paper / "layers.py")
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

def html_of(x):
    return x if isinstance(x, str) else (x or {}).get("html", "")
def plain(h):                                # the text as read, each formula as $TeX$ (kept out of the tag stripping)
    keep = []
    def stash(tex):
        keep.append(tex); return "\x01%d\x01" % (len(keep) - 1)
    t = re.sub(r'<l2m-math n="(\d+)"></l2m-math>', lambda m: " " + stash(items[int(m.group(1))]["tex"].strip()) + " ", h)
    t = re.sub(r"\$\$(.+?)\$\$|\$(.+?)\$", lambda m: stash(m.group(1) or m.group(2)), t, flags=re.S)
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))).strip()
    return re.sub("\x01(\\d+)\x01", lambda m: "$" + keep[int(m.group(1))].replace("$", "") + "$", t)
def words(h):                                # (a formula is one word, with the punctuation that follows it)
    return len(re.sub(r"\$[^$]*\$", " F", plain(h)).split())
REL = re.compile(r"=|\\sim|\\approx|\\propto|\\le|\\ge|<|>|\\to|\\gg|\\ll")
_SYM, _CMP = r"\\?[A-Za-z]+(_\{?[\w]+\}?)?", r"(=|<|>|\\[lg]eq?|\\[lg]{2}|\\neq?)"
REGIME = re.compile(r"^\s*(-?\d+\s*%s\s*)?%s\s*%s\s*-?\d+\s*$" % (_CMP, _SYM, _CMP))   # Q_5=1, G>1, 2<d<6
def formulas(h):                             # relations (an equation or a scaling); a bare symbol, or a regime such as
    return len([f for f in re.findall(r"\$[^$]+\$", plain(h)) if REL.search(f) and not REGIME.match(f.strip("$"))])   # Q_5=1, does not count
def sentences(h):
    t = re.sub(r"\$[^$]*\$", "F", plain(h))
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(“\"])", t) if s.strip()]
def long_sentences(h, n=35):                 # the rule says about 30
    return [s for s in sentences(h) if len(s.split()) > n]

# the paper in reading order, as plain text per node
order, kids, kind = [], {}, {}
def walk(n, parent=None):
    kind[n["id"]] = n.get("kind")
    if "body" in n:
        order.append((n["id"], plain(n["body"])))
    kids[n["id"]] = [c["id"] for c in n.get("children", [])]
    for c in n.get("children", []):
        walk(c, n["id"])
walk(S["root"])
pos = {nid: k for k, (nid, _) in enumerate(order)}
def first_pos(nid):                          # a section's position is its first leaf's
    if nid in pos: return pos[nid]
    for c in kids.get(nid, []):
        p = first_pos(c)
        if p is not None: return p
    return None

R = {"issues": []}
def issue(where, what):
    R["issues"].append("%s: %s" % (where, what))

# ---- root gist
rg = L.ROOT_GIST
gv = {"default": html_of(rg)}
gv.update({k: html_of(v) for k, v in (rg.get("variants") or {}).items()} if isinstance(rg, dict) else {})
R["root_gist_words"] = {k: words(v) for k, v in gv.items()}
for k, v in gv.items():
    w, f = words(v), formulas(v)
    many = len(getattr(L, "CONTRIBUTIONS", None) or []) > 2
    lim = {"student": 110, "specialist": 150 if many else 135}.get(k, 110 if many else 90)
    if w > lim: issue("root gist/" + k, "%d words (limit %d)" % (w, lim))
    if f > (4 if k == "specialist" else 1): issue("root gist/" + k, "%d formulas (limit %d)" % (f, 4 if k == "specialist" else 1))
    if re.search(r"\(\d+\.\d+\)|§|appendix [A-Z]|section \d", plain(v), re.I): issue("root gist/" + k, "cites an equation, section or appendix")

# ---- the paper's contributions, and the gist's three jobs (skill sections 2 and 3)
C = getattr(L, "CONTRIBUTIONS", None) or []
R["contributions"] = len(C)
top = [c for c in S["root"].get("children", [])]
def below(nid):
    out = {nid}
    for c in kids.get(nid, []): out |= below(c)
    return out
framing = {"abstract"}                       # where Context and Why it matters may stand: the introduction, the discussion
if top and not any(kids.get(t["id"]) for t in top):    # a letter without sections: its whole text frames itself
    framing |= set(kind)
if top: framing |= below(top[0]["id"])
for t in top:
    if re.search(r"discussion|conclusion|summary|outlook", t.get("title") or "", re.I): framing |= below(t["id"])
claimed_text = " ".join([plain(S["meta"].get("abstractHtml") or "")] + [txt for nid, txt in order if nid in framing])
norm = lambda t: re.sub(r"\s+", " ", t).strip().lower()
ids_c = {c["id"] for c in C}
if not C: issue("contributions", "no CONTRIBUTIONS: list the paper's own results first (skill section 2)")
elif not 2 <= len(C) <= 6: issue("contributions", "%d items (2-6)" % len(C))
for c in C:
    if norm(c.get("quote", "")) not in norm(claimed_text): issue("contribution " + c["id"], "its quote is not in the abstract or the introduction")
    for w in c.get("where", []):
        if w not in kind: issue("contribution " + c["id"], "unknown node %s" % w)
    if not c.get("where"): issue("contribution " + c["id"], "no 'where'")
abstract_text = norm(plain(S["meta"].get("abstractHtml") or ""))
in_abstract = {c["id"] for c in C if norm(c.get("quote", "")) in abstract_text}   # these every version of the gist states
R["contributions_in_abstract"] = len(in_abstract)
VAGUE = re.compile(r"\b(poses? (a |an )?(possible )?(issue|problem|question|puzzle)s?|has implications|have implications|sheds? light|is discussed|are discussed|is also studied|are also studied|interesting)\b", re.I)
# how the results relate: from the paper (skill section 2), never supplied
SHAPE = getattr(L, "SHAPE", None)
by_id = {c["id"]: c for c in C}
whole_text = norm(" ".join(t for _, t in order) + " " + plain(S["meta"].get("abstractHtml") or ""))
for c in C:
    if not c.get("theme"): issue("contribution " + c["id"], "no theme (skill section 2)")
    b = c.get("builds_on")
    if b:
        if b not in by_id: issue("contribution " + c["id"], "builds on unknown %s" % b)
        if not c.get("link_quote") or norm(c["link_quote"]) not in whole_text: issue("contribution " + c["id"], "builds_on without the paper's own words for the link (link_quote)")
themes = sorted({c.get("theme") for c in C if c.get("theme")})
R["themes"] = len(themes); R["shape"] = SHAPE
if C and SHAPE not in ("one argument", "several findings"): issue("contributions", "SHAPE is not set to 'one argument' or 'several findings'")
if SHAPE == "one argument" and len(themes) > 1:
    linked = {c["theme"] for c in C if c.get("builds_on")}
    if len(themes) - len(linked) > 1: issue("contributions", "SHAPE 'one argument' with %d themes the paper does not link" % len(themes))
ANAPHOR = re.compile(r"^\s*(It|Its|This|These|That|Those|So|Thus|Hence|Such|Together|Therefore)\b")
GATHER = re.compile(r"^\s*(This|These|So|Thus|Hence|Together|Therefore|In all|All this)\b")
def list_items(h, level=1):                  # (opening tag, inner html) of each <li> at this depth of nested lists
    out, depth, start = [], 0, None
    for m in re.finditer(r"<(/?)(ul|ol|li)\b[^>]*>", h):
        close, tag = m.group(1), m.group(2)
        if tag in ("ul", "ol"):
            depth += -1 if close else 1
        elif depth == level and not close and start is None:
            start = m
        elif depth == level and close and start is not None:
            out.append((start.group(0), h[start.end():m.start()])); start = None
    return out
claims_of = lambda h: set(" ".join(re.findall(r'data-claims="([^"]+)"', h)).split())
covers_of = lambda h: set(" ".join(re.findall(r'data-covers="([^"]+)"', h)).split())
R["gist_points"] = {}
for k, v in gv.items():
    parts = {}
    for tag, inner in list_items(v):
        lab = re.search(r"<b>(.*?)</b>", inner)
        if lab: parts[re.sub(r"\s+", " ", lab.group(1)).strip().lower()] = (tag, inner)
    if set(parts) != {"context", "result", "why it matters"}:
        issue("root gist/" + k, "needs exactly the bullets Context, Result, Why it matters"); continue
    points = list_items(parts["result"][1])
    R["gist_points"][k] = len(points)
    if not points: issue("root gist/" + k, "Result is not a list of points, one per contribution")
    got = set(); seen_themes = []
    for tag, inner in points:
        c = claims_of(tag + inner)
        cid = sorted(c, key=lambda x: [i for i, cc in enumerate(C) if cc["id"] == x] or [0])[0] if c else None
        if cid and ANAPHOR.match(plain(inner)) and not (by_id.get(cid, {}).get("builds_on") and by_id[cid]["builds_on"] in got):
            issue("root gist/" + k, "a point leans on the one before ('%s…') without a link the paper states: name its subject" % plain(inner)[:24])
        th = by_id.get(cid, {}).get("theme")
        if th and seen_themes and th != seen_themes[-1] and th in seen_themes: issue("root gist/" + k, "the points of theme %s are not together" % th)
        if th: seen_themes.append(th)
        one_theme = len({by_id.get(x, {}).get("theme") for x in c}) == 1
        if not c or (len(c) > 1 and not (SHAPE == "several findings" and one_theme)):
            issue("root gist/" + k, "a point claims %s; a point states one contribution (several findings: one finding's)" % (", ".join(sorted(c)) or "nothing"))
        if c & got: issue("root gist/" + k, "%s has two points" % ", ".join(sorted(c & got)))
        got |= c
        n = words(inner); lim_p = (40 if k == "specialist" else 30) + (25 if len(c) > 1 else 0)
        if n > lim_p: issue("root gist/" + k, "a point of %d words (about 25, at most %d): %s…" % (n, lim_p, plain(inner)[:50]))
        for m in VAGUE.finditer(plain(inner)): issue("root gist/" + k, "a point says only that something was found: '%s'" % m.group(0))
    need = in_abstract
    if need - got: issue("root gist/" + k, "Result does not state %s" % ", ".join(sorted(need - got)))
    if got - ids_c: issue("root gist/" + k, "Result claims unknown %s" % ", ".join(sorted(got - ids_c)))
    why_text = plain(re.sub(r"<b>.*?</b>", "", parts["why it matters"][1]))
    if SHAPE == "several findings" and GATHER.match(why_text):
        issue("root gist/" + k, "Why it matters gathers several findings into one conclusion ('%s…')" % why_text[:20])
    for lab in ("context", "why it matters"):
        inner = parts[lab][1]
        if claims_of(inner): issue("root gist/" + k, "%s states a result (%s): it belongs under Result" % (lab.capitalize(), ", ".join(sorted(claims_of(inner)))))
        cv = covers_of(inner)
        if not cv: issue("root gist/" + k, "%s is not grounded (data-covers)" % lab.capitalize())
        elif cv - framing: issue("root gist/" + k, "%s is grounded outside the introduction and discussion: %s" % (lab.capitalize(), ", ".join(sorted(cv - framing))))
R["gist_claims"] = {k: len(set(" ".join(re.findall(r'data-claims="([^"]+)"', v)).split())) for k, v in gv.items()}

# ---- root brief
rb = html_of(L.ROOT_BRIEF)
paras = re.findall(r"<p[ >].*?</p>", rb, re.S) or [rb]
R["root_brief_words"] = words(rb); R["root_brief_paragraphs"] = len(paras)
R["root_brief_long_sentences"] = len(long_sentences(rb))
R["root_brief_formulas"] = formulas(rb)
paper_words = sum(len(t.split()) for _, t in order)
lo = 450 if paper_words >= 8000 else 250                  # (a short paper, a letter or proceedings, has a shorter summary)
R["paper_words"] = paper_words
if not lo <= words(rb) <= 700: issue("root brief", "%d words (%d-700)" % (words(rb), lo))
if not 4 <= len(paras) <= 7: issue("root brief", "%d paragraphs (4-7)" % len(paras))
for k, p in enumerate(paras, 1):          # (one relation per paragraph)
    if formulas(p) > 3: issue("root brief ¶%d" % k, "%d formulas (at most 3)" % formulas(p))
for s in long_sentences(rb): issue("root brief", "long sentence (%d words): %s…" % (len(s.split()), s[:70]))
if re.search(r"\bthe (discussion|paper|section) (summari[sz]es|concludes)", plain(rb), re.I): issue("root brief", "meta sentence")

rb_cov = set(" ".join(re.findall(r'data-covers="([^"]+)"', rb)).split())
if SHAPE == "several findings" and len(themes) > 1:
    where_theme = {w: c.get("theme") for c in C for w in c.get("where", [])}
    para_themes = [{where_theme[w] for w in set(" ".join(re.findall(r'data-covers="([^"]+)"', p)).split()) if w in where_theme} for p in paras]
    for th in themes:
        if not any(pt == {th} for pt in para_themes): issue("root brief", "finding %s has no paragraph of its own" % th)
for c in C:
    if not set(c.get("where", [])) & rb_cov: issue("root brief", "does not ground contribution %s in any of its paragraphs" % c["id"])
# ---- grounding: a span should cover paragraphs, not whole sections
coarse = 0
for h in [rb] + [html_of(v) for v in L.BRIEF.values()]:
    for cov in re.findall(r'data-covers="([^"]+)"', h):
        ids = cov.split()
        if any(kids.get(i) for i in ids) or len(ids) > 3: coarse += 1
R["coarse_spans"] = coarse

# ---- section briefs and paragraph gists
bw = {}
for nid, v in L.BRIEF.items():
    w = words(html_of(v)); bw[nid] = w
    parent = any(kids.get(c) for c in kids.get(nid, []))
    hi = 110 if parent else 90
    if not 40 <= w <= hi and kind.get(nid) != "appendix": issue("brief " + nid, "%d words (40-%d)" % (w, hi))
    for s in long_sentences(html_of(v)): issue("brief " + nid, "long sentence (%d words)" % len(s.split()))
R["brief_words_mean"] = round(sum(bw.values()) / max(1, len(bw)), 1); R["brief_words_max"] = max(bw.values() or [0])
R["briefs"] = len(bw)
gw = {nid: words(html_of(v)) for nid, v in L.GIST.items()}
R["gists"] = len(gw); R["gist_words_mean"] = round(sum(gw.values()) / max(1, len(gw)), 1)
R["gists_over_20"] = sum(1 for nid, w in gw.items() if w > 20 and kind.get(nid) == "paragraph")
for nid, v in L.GIST.items():
    if re.match(r"\s*(Thanks|Acknowledg|Conventions|Recap|Summary)\b", plain(html_of(v))): issue("gist " + nid, "filler")

# ---- definitions: length, anchor at the first mention, aliases that hit too often
R["defs"] = len(L.DEFS); late, noisy = [], []
for d in L.DEFS:
    w = words(d["html"])
    if not 25 <= w <= 60: issue("def " + d["id"], "%d words (25-60)" % w)
    names = [d["term"]] + list(d.get("aliases", []))
    pat = re.compile("|".join(r"(?<![\w-])" + re.escape(a) + r"(?![\w-])" for a in names), re.I)
    first = next((nid for nid, t in order if pat.search(t)), None)
    at = d["at"]["node"]
    if first and first_pos(at) is not None and first_pos(first) < first_pos(at) - 0:
        late.append(d["id"]); issue("def " + d["id"], "anchored at %s, first met at %s" % (at, first))
    for a in d.get("aliases", []):
        n = sum(len(re.findall(r"(?<![\w-])" + re.escape(a) + r"(?![\w-])", t, re.I)) for _, t in order)
        if n > 15: noisy.append(a); issue("def " + d["id"], "alias '%s' occurs %d times" % (a, n))
R["defs_anchored_late"] = len(late); R["noisy_aliases"] = len(noisy)

# ---- background notes and questions
R["background"] = len(L.BACKGROUND)
R["background_words"] = [words(b["body"]) for b in L.BACKGROUND]
STOP = set("the and with from into that this their what when where which about between under over without of for".split())
def nouns(t):
    return {w.lower().rstrip("s") for w in re.findall(r"[A-Za-z][A-Za-z–-]{3,}", t) if w.lower() not in STOP}
for b in L.BACKGROUND:
    w = words(b["body"])
    tn, bn = nouns(b["title"]), nouns(plain(b["body"]))
    if tn and len(tn & bn) <= len(tn) / 2: issue("background " + b["id"], "its body hardly mentions its title's words: %s" % ", ".join(sorted(tn - bn)))
    if not 100 <= w <= 180: issue("background " + b["id"], "%d words (100-180)" % w)
R["questions"] = len(L.QUESTIONS)
R["question_answer_words_mean"] = round(sum(words(q["a"]) for q in L.QUESTIONS) / max(1, len(L.QUESTIONS)), 1)
for q in L.QUESTIONS:
    w = words(q["a"])
    if not 35 <= w <= 90: issue("question " + q["id"], "answer %d words (about 40-90)" % w)
R["issue_count"] = len(R["issues"])

if AS_JSON:
    print(json.dumps({k: v for k, v in R.items() if k != "issues"}, indent=1))
else:
    for k, v in R.items():
        if k != "issues": print("%-28s %s" % (k, v))
    print("\n%d issues" % len(R["issues"]))
    for i in R["issues"]: print("  " + i)
