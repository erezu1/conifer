"""Where Epsilon is (Conifer converts LaTeX and draws formulas with it: https://github.com/erezu1/epsilon).

Looked up in this order: the EPSILON environment variable; the path written in epsilon.path at the repository's
root (git-ignored, for one machine); a checkout named epsilon beside this repository.
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _find():
    cands = [os.environ.get("EPSILON")]
    f = ROOT / "epsilon.path"
    if f.exists():
        cands.append(f.read_text().strip())
    cands.append(str(ROOT.parent / "epsilon"))
    for c in cands:
        if c and (Path(c).expanduser() / "render_math.js").exists():
            return Path(c).expanduser().resolve()
    sys.exit("Conifer needs Epsilon: clone https://github.com/erezu1/epsilon (and run npm install there), "
             "then set EPSILON=/path/to/epsilon or write that path into epsilon.path")


EPSILON = _find()
