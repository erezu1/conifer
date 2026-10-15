# Conifer

A way to publish a paper as a tree that can be read at any depth, by readers of any background: the trunk is the gist, the branches a one-page summary in which every sentence shows the part of the paper it stands for, the foliage the paper itself, and the roots its proofs and appendices, folded until wanted. Definitions anchored to the sentence that defines them; questions anchored to the part they are about; the provenance of every generated sentence visible. One data file serves phones, the web and language models.

- [DESIGN.md](DESIGN.md): prior art, the product, the proposed data structure, the pipeline from a LaTeX draft, how it fits [Epsilon](../../research/epsilon), open questions.
- `mockup/conifer-mockup.html`: a working mockup, self-contained; open it in any browser. `python3 mockup/build.py` rebuilds it (needs node and Epsilon's `node_modules`).
- `mockup/semicircle.tree.json`: the sample document in the proposed format.
- `logo/`: the mark (a conifer drawn as a hierarchical graph), a wordmark and an app icon.
- `viewer/`: the viewer shared by every tree (`viewer.js`, `viewer.css`).
- `tools/`: the pipeline. `fetch_arxiv.py` fetches and converts an arXiv paper with Epsilon; `skeleton.py` turns the Epsilon document into the tree and an outline to draft from; `build_tree.py` merges the drafted layers, checks them, draws the math and packs the page.
- `papers/2608.21511/`: the first real tree, of *String stars, small black holes, and the supersymmetric index*: the Epsilon document (`doc/`), the skeleton and outline, the drafted layers (`layers*.py`), `tree.json` and the page `tree.html`. Rebuild with `python3 tools/build_tree.py papers/2608.21511`.
