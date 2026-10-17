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
def words(h):
    return len(re.sub(r"\$[^$]*\$", " F ", plain(h)).split())
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
    lim = {"student": 110, "specialist": 135}.get(k, 90)
    if w > lim: issue("root gist/" + k, "%d words (limit %d)" % (w, lim))
    if f > (4 if k == "specialist" else 1): issue("root gist/" + k, "%d formulas (limit %d)" % (f, 4 if k == "specialist" else 1))
    if re.search(r"\(\d+\.\d+\)|§|appendix [A-Z]|section \d", plain(v), re.I): issue("root gist/" + k, "cites an equation, section or appendix")

# ---- root brief
rb = html_of(L.ROOT_BRIEF)
paras = re.findall(r"<p[ >].*?</p>", rb, re.S) or [rb]
R["root_brief_words"] = words(rb); R["root_brief_paragraphs"] = len(paras)
R["root_brief_long_sentences"] = len(long_sentences(rb))
R["root_brief_formulas"] = formulas(rb)
if not 450 <= words(rb) <= 700: issue("root brief", "%d words (450-700)" % words(rb))
if not 4 <= len(paras) <= 6: issue("root brief", "%d paragraphs (4-6)" % len(paras))
for k, p in enumerate(paras, 1):          # (one relation per paragraph)
    if formulas(p) > 3: issue("root brief ¶%d" % k, "%d formulas (at most 3)" % formulas(p))
for s in long_sentences(rb): issue("root brief", "long sentence (%d words): %s…" % (len(s.split()), s[:70]))
if re.search(r"\bthe (discussion|paper|section) (summari[sz]es|concludes)", plain(rb), re.I): issue("root brief", "meta sentence")

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
    if not 40 <= w <= 90: issue("question " + q["id"], "answer %d words (40-90)" % w)
R["issue_count"] = len(R["issues"])

if AS_JSON:
    print(json.dumps({k: v for k, v in R.items() if k != "issues"}, indent=1))
else:
    for k, v in R.items():
        if k != "issues": print("%-28s %s" % (k, v))
    print("\n%d issues" % len(R["issues"]))
    for i in R["issues"]: print("  " + i)
