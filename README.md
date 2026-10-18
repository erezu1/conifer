# Conifer

Turns a LaTeX paper into a tree that can be read at three depths: the **Gist** (the question, what the paper finds and why it matters), a one-page **Summary** in which every sentence shows the paragraphs it stands for, and the **Paper** itself, with a short summary under each section, definitions on dotted terms, background notes and questions. One page, for phones and the web, with the formulas drawn ahead of time.

An example, the Wigner semicircle from random matrix theory: <https://erezu1.github.io/conifer/>.

## From LaTeX to a tree

```bash
python3 tools/convert.py paper.tex -o my-paper      # or a folder, a .tar.gz, or an arXiv id
#   draft my-paper/layers*.py from my-paper/outline.md, following skill/conifer-draft.md
python3 tools/build_tree.py my-paper                # writes my-paper/tree.html (self-contained) and my-paper/web/
python3 tools/check_layers.py my-paper              # measures the draft against the skill's rules
```

1. **Convert.** `tools/convert.py` reads the LaTeX with [Epsilon](https://github.com/erezu1/epsilon)'s converter and writes the tree's folder: the converted document (`doc/`), `skeleton.json` (every section, paragraph, figure and reference, with a stable id) and `outline.md` (the same as text, to draft from).
2. **Draft.** The layers (the gist, the summary, the section briefs, the definitions, notes and questions) are written by an AI drafter into `layers*.py`, following `skill/conifer-draft.md`: the paper's contributions first, every sentence tied to the paragraphs it stands for, and a blind read of the gist (`tools/blind_gist.py`) by a second reader who sees only the abstract and the cited paragraphs. Give the skill to Claude Code with the folder, e.g. "draft the layers of my-paper following skill/conifer-draft.md".
3. **Build.** `tools/build_tree.py` merges the layers into the paper, checks every id and quotation, draws the formulas, and writes `tree.json`, `tree.html` (one self-contained file) and `web/index.html` (the same, with the figures as files beside it, for a website).

## Needs

- Python 3, and [Node.js](https://nodejs.org/) for drawing the formulas.
- Epsilon: `git clone https://github.com/erezu1/epsilon` and `npm install` inside it. Conifer finds it through the `EPSILON` environment variable, a path written in `epsilon.path` here, or a checkout named `epsilon` beside this folder.
- Optional: [Pillow](https://pypi.org/project/pillow/) in `.venv/` to shrink large figures.

## What is here

| | |
|---|---|
| `tools/` | `convert.py`, `skeleton.py`, `build_tree.py`, the checks (`check_layers.py`, `blind_gist.py`), figure and formula slimming, `site.py` (this repository's site) |
| `viewer/` | the reader every tree carries: `viewer.js`, `viewer.css`, search, copying, the service worker and app manifest |
| `skill/conifer-draft.md` | the drafting instructions |
| `example/` | the semicircle example: its document (`doc_semicircle.py`), `build.py`, and the page |
| `logo/` | the mark (a conifer drawn as a hierarchical graph), a wordmark and app icons |
| `DESIGN.md`, `PERFORMANCE.md` | how the format and the reader were designed, and how the reader was made fast |
| `docs/` | the site GitHub Pages serves: the example (`python3 tools/site.py`) |
