#!/usr/bin/env python3
"""Fetch an arXiv paper's source and convert it with Epsilon into papers/<key>/ (the Epsilon document), keeping the
source in papers/<key>/source/. Uses Epsilon's own helpers; nothing in Epsilon's library is touched.

    python3 tools/fetch_arxiv.py 2608.21511
"""
import json
import sys
import time
from pathlib import Path

EPSILON = Path("/Users/urbach/IAS Dropbox/Erez Urbach/research/epsilon")
sys.path.insert(0, str(EPSILON))
import epsilon_library as L  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
aid = sys.argv[1]
key = L.arxiv_key(aid)
root = HERE / "papers" / key
src = root / "source"
meta = L.arxiv_meta(aid)
print("title:", meta["title"]); print("authors:", meta["authors"])
time.sleep(1)
if not (src / "src.bin").exists():
    raw = L.http_get("https://arxiv.org/e-print/" + aid)
    src.mkdir(parents=True, exist_ok=True)
    (src / "src.bin").write_bytes(raw)
    print("fetched %d KB" % (len(raw) // 1024))
unpacked = src / "unpacked"
if not unpacked.exists():
    L.unpack((src / "src.bin").read_bytes(), unpacked)
tex = L.main_tex(unpacked)
print("main file:", tex)
(root / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
ok, log = L.run_converter(tex, root / "doc", None, meta=meta)
print("converted:", ok)
print(log[-3000:])
