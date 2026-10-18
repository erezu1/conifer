#!/usr/bin/env python3
"""LaTeX -> a tree's folder, ready to draft: the Epsilon document, the skeleton and the outline.

    python3 tools/convert.py paper.tex            [-o DIR]
    python3 tools/convert.py my-paper/            [-o DIR]   (a folder: its main .tex is found)
    python3 tools/convert.py source.tar.gz        [-o DIR]   (an archive as arXiv serves it)
    python3 tools/convert.py 2406.14605           [-o DIR]   (an arXiv paper: its source is downloaded)

DIR (by default <name>-conifer in the current folder, or the arXiv number) receives
    doc/             the Epsilon document (paper.json, images/)
    meta.json        title and authors (from arXiv for an arXiv paper; the converter's otherwise)
    skeleton.json    the tree with empty layers
    outline.md       every node's id and text: what the layers are drafted from (skill/conifer-draft.md)
    source/          the unpacked LaTeX (an archive's or arXiv's)

Then the layers are drafted into DIR/layers*.py, and python3 tools/build_tree.py DIR builds the page.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import EPSILON  # noqa: E402
sys.path.insert(0, str(EPSILON))
import epsilon_library as L  # noqa: E402

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
ap.add_argument("source", help="a .tex file, a folder, a .tar.gz, or an arXiv id")
ap.add_argument("-o", "--out", help="the tree's folder")
a = ap.parse_args()

src = Path(a.source).expanduser()
meta = {}
ARXIV = re.fullmatch(r"(\d{4}\.\d{4,5}|[a-z-]+(\.[A-Z]{2})?/\d{7})(v\d+)?", a.source) and not src.exists()
if ARXIV:
    key = L.arxiv_key(a.source)
    out = Path(a.out or key).resolve()
    meta = L.arxiv_meta(a.source)
    raw_file = out / "source" / "src.bin"
    if not raw_file.exists():
        time.sleep(1)                                          # (arXiv asks for a pause between requests)
        raw = L.http_get("https://arxiv.org/e-print/" + a.source)
        raw_file.parent.mkdir(parents=True, exist_ok=True)
        raw_file.write_bytes(raw)
    folder = out / "source" / "unpacked"
    if not folder.exists():
        L.unpack(raw_file.read_bytes(), folder)
elif src.is_file() and src.suffix == ".tex":
    out = Path(a.out or src.stem + "-conifer").resolve()
    folder = src.parent
elif src.is_dir():
    out = Path(a.out or src.resolve().name + "-conifer").resolve()
    folder = src
elif src.is_file():                                            # an archive
    out = Path(a.out or re.sub(r"(\.tar)?\.(gz|tgz|tar|zip)$", "", src.name) + "-conifer").resolve()
    folder = out / "source" / "unpacked"
    if not folder.exists():
        if src.suffix == ".zip":
            shutil.unpack_archive(str(src), str(folder))
        else:
            L.unpack(src.read_bytes(), folder)
else:
    sys.exit("not a .tex file, a folder, an archive or an arXiv id: %s" % a.source)

tex = src if src.suffix == ".tex" and src.is_file() else L.main_tex(folder)
if not tex:
    sys.exit("no main .tex file (one with \\documentclass and \\begin{document}) in %s" % folder)
print("main file:", tex)
out.mkdir(parents=True, exist_ok=True)
ok, log = L.run_converter(tex, out / "doc", None, meta=meta or None)
if not ok:
    print(log[-3000:])
    sys.exit("Epsilon could not convert %s" % tex)

doc = json.loads((out / "doc" / "paper.json").read_text())
if not meta:                                                   # a local paper: its title and authors as converted
    meta = {"title": L.page_text(doc.get("title")) or tex.stem, "authors": doc.get("authors") or []}
(out / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
r = subprocess.run([sys.executable, str(HERE / "skeleton.py"), str(out / "doc"), "-o", str(out)], capture_output=True, text=True)
print((r.stdout + r.stderr).strip())
if r.returncode:
    sys.exit(r.returncode)
print("\nnext: draft %s/layers*.py from %s/outline.md (skill/conifer-draft.md), then\n  python3 %s %s"
      % (out, out, HERE / "build_tree.py", out))
