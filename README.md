# Conifer

A way to publish a paper so that it can be read at any depth, by readers of any background: a gist at the tip, a one-page summary in which every sentence opens into the part of the paper it stands for, the paper itself with its proofs and appendices folded, and everything. Definitions anchored to the sentence that defines them; questions anchored to the part they are about; the provenance of every generated sentence visible. One data file serves phones, the web and language models.

- [DESIGN.md](DESIGN.md): prior art, the product, the proposed data structure, the pipeline from a LaTeX draft, how it fits [Epsilon](../../research/epsilon), open questions.
- `mockup/conifer-mockup.html`: a working mockup, self-contained; open it in any browser. `python3 mockup/build.py` rebuilds it (needs node and Epsilon's `node_modules`).
- `mockup/semicircle.cone.json`: the sample document in the proposed format.
- `logo/`: the mark (a conifer drawn as a hierarchical graph), a wordmark and an app icon.
- `viewer/`: the viewer shared by every cone (`viewer.js`, `viewer.css`).
- `tools/`: the pipeline. `fetch_arxiv.py` fetches and converts an arXiv paper with Epsilon; `skeleton.py` turns the Epsilon document into the cone's tree and an outline to draft from; `build_cone.py` merges the drafted layers, checks them, draws the math and packs the page.
- `papers/2608.21511/`: the first real cone, of *String stars, small black holes, and the supersymmetric index*: the Epsilon document (`doc/`), the skeleton and outline, the drafted layers (`layers*.py`), `cone.json` and the page `cone.html`. Rebuild with `python3 tools/build_cone.py papers/2608.21511`.
