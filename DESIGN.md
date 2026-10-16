# Project Conifer: a paper grown into a tree

*Brainstorm, prior art and a proposed data structure. First draft, 15 October 2026. Companion to the mockup in `mockup/`.*

## 0. The idea in one paragraph

A paper is published as a **tree**. The trunk is the gist, three things every reader passes through: the context, the result, why it matters. The branches are a one-page summary in which every sentence can be opened into the part of the paper it stands for. The foliage is the paper itself, each section led by its own summary; the roots are its proofs and appendices, folded until asked for. The full text is the ground truth and is never lost; every coarser layer is *grounded* in it (each summary sentence knows what it summarises), so a reader can always check. Two cross-cutting layers hang off the tree: **definitions** anchored to the sentence that defines a term or symbol, and **questions** anchored to the region they are about. A third axis, the reader's **background**, picks which summaries they see and which background notes open for them. The author writes the paper as usual; an AI skill drafts the layers from the draft; the author approves and edits them, and the provenance of every piece of generated text stays visible. Because the tree is data, the same file serves readers, phones, and language models.

## 1. What exists already

I looked for prior art in four places: hypertext theory, reading interfaces from the HCI community, publishing formats, and document toolchains. The short version: every piece of Conifer has been tried somewhere, usually on its own and usually at read time rather than at publication time. Nobody seems to have combined author-owned layered text, grounding, definitions, anchored questions and an audience axis into one publishable document format, and the LLM-era systems all generate on demand instead of shipping a reviewed artefact.

| Idea | Who | What it shows |
| --- | --- | --- |
| **Stretchtext** (1967/1970) | Ted Nelson | Text that expands and contracts *in place*, with a global "throttle" for detail. Never took off on the web. Gwern calls the same thing "semantic zoom" and runs his site on it (collapsible sections, popups, a ladder from title to source). |
| **Telescopic text** | Joe Davis, then the `telescopic-text` library | Word-by-word expansion, authored as nested bullets. Charming, too fine-grained for papers. |
| **Qlarify** (UIST 2024) | Fok, Chang, August, Zhang, Weld | "Recursively expandable abstracts": select any span of an abstract, pick Define / Expand / Why, get an LLM expansion threaded in place with a quote button to the source passage. Readers mostly used the suggested spans; 87.5 % of expansions accurate; worries: verbosity, steering, discouraging full reads. Expansions are generated at read time, not authored. |
| **TreeReader** (2025) | Aspuru-Guzik group, Toronto | A paper as a tree (sections, paragraphs, figures); each node a 2–5 point LLM summary with an `evidence` quote per point; summaries built bottom-up; three-column UI that *navigates into* subtrees. Small study: better skimming, lower load. Code on GitHub. |
| **Paper Plain** (2022) | August et al. | For non-expert readers of medical papers: per-passage plain-language gists, definitions, section summaries and a list of *key questions* that lead to the passages answering them. Easier reading without loss of comprehension. The closest thing to the "questions on regions" idea. |
| **Scim**, **ScholarPhi**, **Semantic Reader** | Allen AI / Berkeley | Scim: faceted *extractive* highlights with adjustable density. ScholarPhi: position-sensitive definitions of terms and symbols, "defined in §2". Semantic Reader productised parts of both on arXiv PDFs. |
| **DocVoyager** (CHI 2025) | Adobe Research | LLM anticipates the reader's questions and guides a personal reading path. |
| **Nota** | Will Crichton | A document language for the browser with `@Definition` / `@Ref` and definition tooltips. Immature, but the right instinct: definitions are document structure. |
| **Lean blueprint** / plasTeX | Patrick Massot | LaTeX macros (`\uses`, `\lean`) on theorem environments compile both to the normal PDF and to a web view with a dependency graph. The one proof in the wild that mathematicians will annotate `.tex` files if the payoff is a better web artefact. |
| **Article of the Future** (2009) | Elsevier / Cell | Graphical abstract + bulleted highlights + hierarchical navigation. Highlights and graphical abstracts survived; the rest did not. Physics World's reaction, worth remembering: theorists will say their arguments do not reduce to bullets. |
| **Octopus** | Jisc / UKRI | A paper split into eight typed, separately citable units (problem, hypothesis, method, results, analysis, interpretation, application, review). Typed nodes with rhetorical roles. |
| **MyST / Pandoc / JATS** | Executable Books etc. | Documents already have JSON ASTs and round-trip to JATS and LaTeX. Conifer should sit *on top of* a document AST, not replace one. |
| **Zoomable hierarchical texts** | a 2022 US patent (11,321,416) | Click a sentence to see the next finer level down to the original. Worth knowing it exists; this is the general idea, patented in a narrow form. |

Takeaways that shaped the design below:

1. **Publish the layers, don't generate them at read time.** Qlarify and TreeReader are read-time tools: fast to build, unreviewed, and every reader gets a different paper. The scientific value is in the author owning a *fixed* set of layers that referees and readers share. Read-time AI can still exist on top, as an optional "ask" that proposes new questions to the author.
2. **Expand in place, keep the context.** Nelson was right and TreeReader's "navigate into the subtree" loses the reader's place. The mockup keeps the summary above the text it opens (a thread) and lets you switch to pure replacement to compare.
3. **Grounding is what makes summaries trustworthy.** Every one of TreeReader's points carries an evidence quote; Qlarify's attribution button was used by 15 % of readers but valued by all. In Conifer every summary sentence declares which nodes it covers.
4. **Definitions and questions are the two layers non-experts ask for first** (Paper Plain, ScholarPhi). They are cheap for the AI skill to draft and easy for the author to check.
5. **Extractive and abstractive layers are both useful.** Scim's highlights never hallucinate; a rewritten gist reads better. The format should allow a rendition to be either text or a selection of sentences.
6. **Authoring must stay in LaTeX** or nobody will use it. The Lean blueprint shows the way: a few macros, or a sidecar file, and a compiler.

## 2. The product

### 2.1 Three readers, two axes

Readers differ along two independent axes, and the product has to serve both:

- **Depth**: how much of the paper they want right now. The skimmer deciding whether to read (30 seconds), the colleague who wants the ideas but not the derivations (10 minutes), the student or referee who needs everything (hours). The same person moves along this axis during one sitting.
- **Background**: what they already know. A specialist in the subfield, a physicist from another area, a student. A specialist wants the terse version and no explanations of Wick's theorem; a student needs the opposite. Your point that the paper should be readable by people of different backgrounds is this axis, and it changes the data structure (see 3.2), not just the viewer.

There is a fourth reader: a language model. An agent that must "read" a hundred papers wants exactly the tree: load every gist, open the summaries of the relevant ones, expand only what it needs. The format is as much for machines as for people, and that is a strong argument for Conifer being a *data format* rather than a web page.

### 2.2 The reading experience

The mockup implements the whole ladder, so the quickest way to read this section is to open `mockup/conifer-mockup.html` on a phone. In words:

1. **The gist** (depth 0). Context / Result / Why it matters, three short paragraphs, plus the one equation and the one figure to remember. A reading time for each deeper level, so the choice to go on is informed.
2. **The summary** (depth 1). One page that reads as a standalone piece, like a Nature Research Briefing or an extended abstract. Every sentence is a *grounded span*: tap it and the part of the paper it stands for opens underneath as a thread, with its own summary, its own text and its own questions. Threads nest.
3. **The paper** (depth 2). The full text in order. Each section opens with its summary ("In brief"), which can be collapsed back into; proofs, appendices and derivations are folded to one line with their word count. Every paragraph can be folded to its one-line gist and opened again.
4. **Everything** (depth 3). All folds open, in the linear order of the PDF. This level *is* the paper; nothing in the source is lost at any level above it, only hidden.

Plus, at every depth:

- **Local depth control.** The dial sets the default depth for every node; any node can be pushed deeper or shallower on its own ("more", "less", "fold", "collapse to this summary"). Nelson's two throttles.
- **Definitions.** Terms and symbols carry a dotted underline. Tapping one shows the definition, where it is defined, and a "Show" that opens the paper there and highlights the defining words. Definitions can be audience-dependent: a student sees "Hermitian matrix" underlined, a physicist does not.
- **Questions on regions.** A `?3` badge on a section or paragraph lists the questions about it: anticipated by the AI skill, written by the author (referee reports and talk Q&A are an excellent source), or sent in by readers; each answer links to the parts of the paper that answer it. At coarse depths the questions of everything hidden below bubble up to the badge. An "Ask" box shows where a read-time model would plug in; in the mockup it copies the question with its context to the clipboard.
- **Provenance.** Every generated text carries a chip: *author*, *AI draft · approved*, *AI draft · unreviewed*. This is a scientific document; the reader must know which words the author stands behind.
- **Background notes.** Short boxes ("Why a random matrix?", "Euler's formula and the genus") that are open for the readers who need them and folded to a line for the others, never part of the summaries.
- **Working links.** Equation, section and citation references open the target in place (switching depth if needed) and flash it; links from outside the paper address nodes, equations and definitions, as Epsilon's links already address equations.

### 2.3 Principles

- **The paper is the ground truth.** Leaves hold the verbatim text; layers above are derived. "Everything" renders the paper in its original order.
- **Grounded, or it does not ship.** A summary sentence without `covers` is a bug; the skill should refuse to emit one.
- **The author owns the layers.** The skill drafts; the author approves, edits or rewrites; provenance is always visible. Unreviewed drafts may be published but are marked.
- **Two axes, one document.** Depth and audience are both in the data; the viewer only chooses.
- **Static and small.** One HTML file (or a JSON file plus a shared viewer), no server, readable offline on a phone. Epsilon's constraints, which have served well.
- **Also a machine interface.** The JSON is the API; a tiny "expand this node" tool for agents falls out of it for free.

### 2.4 Things the mockup lets you compare

- Thread versus replace: Settings → "When a summary opens". Stretchtext replaces; a thread keeps the summary as context above the text. I find threads better for the one-page summary and replacement acceptable inside sections; worth deciding per level.
- Section summaries in the Paper view on or off.
- Reading as specialist / physicist / student, which changes the gist, opens or folds the background notes, and decides which terms are underlined.
- The provenance chips on or off (to feel how much they cost in visual noise).

## 3. The data structure

### 3.1 Shape

A Conifer document is a **tree of nodes** plus a few **side tables** that point into the tree by id. Nothing in the side tables duplicates text from the tree. The mockup's `mockup/semicircle.tree.json` is a complete instance; the Python that generates it, `mockup/doc_semicircle.py`, is easier to read.

```
Document
  format, version
  meta        title, authors, date, key (the equation and figure to show in the gist),
              defaultAudience, source (which LaTeX file and converter version)
  levels      the depth ladder: [gist, brief, paper, full], each with a label and hint
  audiences   [{key, label, hint}]
  root        Node
  defs        [Definition]
  questions   [Question]
```

### 3.2 Nodes and renditions

```
Node
  id          stable id (see 3.4)
  kind        paper | section | appendix | paragraph | equation | figure | table |
              theorem | lemma | definition | proof | remark | background | references
  role        optional rhetorical role: context | background | method | derivation |
              result | discussion | caveat | example
  number      "3.2", "A", "Theorem 1" (as LaTeX printed it)
  title       for sections, boxes, figures
  gist        Rendition: one line (≈ 25 words; the root's gist is the three-part card)
  brief       Rendition: one paragraph (≈ 100–250 words)
  body        HTML of the verbatim text (a leaf), with Epsilon's markup for math,
              displays, figures; a node has body or children, not both
  children    [Node]
  fold        true for nodes shown as one line at the Paper depth (proofs, appendices,
              long derivations)
  audience    for background nodes: the audiences it opens for

Rendition
  html        the text, with grounding spans:  <span data-covers="id id ...">…</span>
  status      author | ai-approved | ai-draft
  variants    { audienceKey: Rendition }  the same level for a different reader
  extract     alternative to html: a list of sentence ids to show (extractive summary)
  hash        fingerprint of the covered text when this was written (staleness, 3.5)
  model, date optional provenance of a draft
```

Why renditions per node rather than one global tree of summaries: a node can lack a level (then the viewer falls through to its children at that level, or to its text), and the author can write the one-page summary as flowing prose *or* let it be composed from the sections' briefs. Both are the same structure; the difference is whether `root.brief` exists.

Why `data-covers` inside the HTML rather than offsets: it is what `\ref` is to a LaTeX author and what an LLM produces reliably; offsets break on every edit. The viewer indexes spans by position in the rendition, so a thread remembers which sentence opened it.

Why `variants` on the rendition and `audience` on background nodes, rather than a whole second document per audience: most of a paper does not change with the reader. What changes is a handful of summaries, a few explanatory boxes, and which terms need underlining. Keeping variants local keeps the author's review small.

### 3.3 The side tables

```
Definition
  id, term, aliases, symbol (TeX)
  html        the definition, in the paper's own words where possible
  at          { node, quote }   the sentence that defines it, by node id and quoted words
  audience    optional: who needs the underline (others see plain text)

Question
  id
  at          { node }          the region it is about (a section or a paragraph)
  q, a        HTML
  answeredBy  [node ids]        where the paper answers it
  source      author | ai | reader
  status      approved | draft
  audience    optional
```

Mentions of a term are marked in the text (`<a data-def="gue">GUE</a>`; the defining occurrence as `<dfn>`), by the skill, so that the viewer never has to guess at word boundaries inside math. Anchors use *quoted words* inside a node, exactly as Epsilon's marks do: they survive re-conversion and small edits, and the viewer finds and highlights them at run time.

### 3.4 Ids

Sections, equations, figures, theorems: the LaTeX label when there is one (Epsilon already normalises `eq:shock` to `eq-shock`), else the number (`section-2.3`, `eq-2.18`). Paragraphs: `<section id>-p<k>`, numbered within the section, plus a short content hash in the sidecar so a tool can tell "the paragraph moved" from "the paragraph changed". Sentences are not nodes; they are addressed by quote (3.3). This keeps the tree small and the ids readable in URLs (`paper.html#genus-p2`).

### 3.5 Provenance and staleness

Each rendition records who wrote it and, for drafts, with what. Each rendition also stores a hash of the text it covers. When the draft changes, `conifer check` lists the summaries whose covered text changed since they were written, so the author (or the skill) re-reads exactly those. A rendition whose `covers` point to ids that no longer exist is an error.

### 3.6 The rendering rule

The viewer needs one rule, and it is short. Let `L` be the depth requested for a node (the dial, unless the node or an ancestor was pushed to another depth):

- `L = 0`: show `gist` if it exists; else fall through to `L = 1`.
- `L = 1`: show `brief` if it exists; else `gist`; else the children at `L = 1`; else the text.
- `L = 2`: a folded node (proof, appendix) shows its brief or gist with an "open" control; otherwise heading + lede (its brief) + children at `L = 2`; a leaf shows its text.
- `L = 3`: as 2 with every fold open.
- Background nodes: hidden at `L ≤ 1`; open at `L = 2` for their audiences and folded for everyone else; open at `L = 3`.
- A grounded span, when opened, renders the nodes it covers at `L = 2` underneath its paragraph (a thread); inside the Paper view it instead scrolls to them.

The root is special only in that its gist is drawn as the card with the key equation and figure, and its brief as the one-page summary.

### 3.7 Left out on purpose, for now

- Sentence-level nodes. Quotes do the job for definitions and questions; if we need sentence ids for the machine interface we can add them without changing anything else.
- A DAG (one summary covering parts of two sections). `data-covers` already takes several ids; what I left out is *transclusion* of a node into a second place in the main text. The thread mechanism is a transclusion, so the viewer can do it; the format just does not ask for it yet.
- Versions, comments, reader marks. Epsilon has marks; a Conifer document can carry them unchanged.
- The "claims" layer (each claim typed as new / known / conjecture, with dependencies, like the Lean blueprint's graph). The `role` field is the hook for it.

## 4. From a draft to a tree

The pipeline I have in mind, each step a small tool:

1. **`epsilon_convert.py paper.tex`** (exists). LaTeX to a document with numbering that matches the PDF, drawn math, figures, labels. The body already carries the markup Conifer needs; the converter would additionally wrap paragraphs with ids (today it emits `<p>` and `<p class="cont">` after a display; a paragraph node groups those).
2. **`conifer skeleton paper.l2m`** (new, mechanical). Builds the tree from the body: sections from `h2`–`h5`, boxes from `.thm/.proof/...`, figures, paragraphs; assigns ids; writes `paper.tree.yaml` with empty renditions, and prints an outline with the text of every node, which is what the skill reads.
3. **The skill** (new, the AI part). Given the outline, it writes, bottom-up: a gist for every paragraph and box; a brief and gist for every section; the root's gist and the one-page summary with grounding spans; the definitions and their anchors; the term mentions; 5–15 anticipated questions with answers and `answeredBy`; background notes and variants for the audiences the author named. Everything it writes is `ai-draft`. It is told to refuse to write a summary sentence it cannot ground. For your own papers it should also read the referee reports and the talk notes if you give them to it, because the best questions are the ones people actually asked.
4. **The author** edits the YAML (or, if we go the LaTeX route, the macros), marks what they approve, rewrites what they want in their own voice.
5. **`conifer build paper.tree.yaml`** (new). Merges the layers with the Epsilon document, checks every id and quote, computes hashes and reading times, writes `paper.conifer.json`, and packs it with the viewer into one HTML file, exactly as `epsilon_render.py` does today. `conifer check` alone reports stale and broken pieces.

**Sidecar or macros?** I propose the sidecar (`paper.tree.yaml`) as the canonical form: the `.tex` stays pristine and compiles as before, the skill's output is a reviewable diff of one file, and the same file can describe *someone else's* arXiv paper, which turns Epsilon's library into a library of trees. LaTeX macros (`\gist{…}` at the top of a section, `\begin{background}[student]…`) can be offered as sugar for authors who want the layers in the source, compiled into the same YAML. The YAML is friendlier than JSON for humans only because of multi-line strings; the JSON is what the viewer reads.

## 5. Relation to Epsilon

Epsilon already solves the hard, unglamorous half: faithful LaTeX conversion with the PDF's numbering, math drawn once, figures, TikZ, footnotes, a phone-first viewer with a reading bar, contents panel, links that remember where you were, marks and notes with quote anchors, a library and a converter that runs on GitHub. Conifer should not duplicate any of it.

What Conifer adds on top:

- the converter emits paragraph ids (small change in `epsilon_convert.py`);
- a `conifer` module in the viewer that takes `paper.json` plus `tree.json` and does what `mockup/viewer.js` does: the dial, renditions, threads, folds, definitions, questions, audiences. The mockup viewer is 350 lines and written against the same document conventions (`.display`, `.thm`, `h2` ids, `cite-`, `eq-`), so it should port rather than be rewritten;
- the bar gets the dial and the audience pill; the contents panel gets the question counts;
- a `tree` tab beside *Notes* in the contents panel, perhaps, listing the questions;
- the library marks papers that have a tree, and the skill can make one for any paper in it.

Two ways to ship: a mode of the Epsilon app ("any paper, with a tree when it has one"), or a separate Conifer site that reuses the converter and the theme. I lean to the first, because the library, offline copies and marks are already there, and because a reader should not have to know which of the two they are opening.

## 6. The mockup

`mockup/conifer-mockup.html` is a self-contained page (open it anywhere; no server needed) and the same page is published as a Claude artifact for phones. It shows a short expository note, *Wigner's semicircle law by the moment method*, written for the purpose so that its three layers could be made faithful (five sections, two appendices, two figures, thirteen numbered equations, a theorem with a folded proof, twelve definitions, twelve questions, four background notes, three audiences). I wrote it rather than use a real paper of yours so that errors in the layering would be mine and not distract from the interface; running the pipeline on your draft "A classification of supersymmetric random matrices" (285 paragraphs, 33 headings in the library) is the natural next step.

Files:

| file | what |
| --- | --- |
| `mockup/doc_semicircle.py` | the sample document in the proposed structure, as Python for the multi-line strings |
| `mockup/semicircle.tree.json` | the same as data, TeX intact: the format |
| `mockup/viewer.js`, `mockup/viewer.css` | the viewer |
| `mockup/build.py` | draws the math with Epsilon's `render_math.js`, packs the page (full page and artifact fragment) |
| `mockup/fig_semicircle.py` | Figure 1: one GUE spectrum at N = 1000 by Sturm counts on the tridiagonal model, no numpy |
| `logo/` | the icon, a wordmark and an app icon |

Rebuild with `python3 mockup/build.py` (needs node and Epsilon's `node_modules`).

## 6b. The first real tree: arXiv:2608.21511

Built on 15 October 2026 from the arXiv source of *String stars, small black holes, and the supersymmetric index*, with the pipeline of section 4 as it now exists:

| step | tool | what it did here |
| --- | --- | --- |
| fetch and convert | `tools/fetch_arxiv.py` | downloads the e-print, finds the main file, runs Epsilon's converter into `papers/2608.21511/doc/` (1220 formulas, 7 figures, 27 footnotes, no warnings) |
| skeleton | `tools/skeleton.py` | reads Epsilon's `paper.json` into the tree tree: 27 sections, 112 paragraphs (each with its displays and continuations), 7 figures, footnotes, references; stable ids from the LaTeX labels; an `outline.md` with the text and TeX of every node, which is what the layers are drafted from |
| layers | `papers/2608.21511/layers*.py` | drafted by the AI reader: the three-part gist in three audience versions, a one-page summary of six grounded paragraphs, a gist for every paragraph and section, a grounded brief for every section, 19 definitions anchored to their defining sentence, 17 questions with the places that answer them, 5 background notes for non-specialists; all marked `ai-draft` |
| build | `tools/build_tree.py` | merges, checks every id and every quoted anchor, marks the mentions of defined terms in the text, draws the layers' TeX with the paper's own macros, embeds Epsilon's pre-drawn formulas and figures, and packs `tree.html` (6.5 MB, self-contained) |

Decisions taken while doing it, in response to reading the first version:

- **Quiet folds.** A folded background note or proof is one muted line (`+ Background · title · for students`), not a box; section summaries in the Paper view are a left-ruled paragraph without fill; chips are muted unless they warn (*AI draft · unreviewed*); the per-paragraph controls appear on hover. The Paper view should read as the paper, with the features reachable but not in the way.
- **Every quoted place leads to the paper.** A thread (the part of the paper a summary sentence stands for) has *Open in the paper*; so do definitions (at the defining sentence, highlighted) and the places that answer a question. The jump pushes a browser history entry and shows a *↩ Summary* pill, so the phone's back gesture returns to the summary with the thread still open.
- **Back and forward follow the structure.** Changing the depth, opening a thread and jumping to a place are history entries; local expansions are folded into the current entry. The address bar carries `#summary` / `#paper` or the id of the current place.
- **A copiable link for every location.** Section headings (¶ on hover), paragraphs, threads, definitions, questions and equation numbers all offer *Copy link*; `page.html#eq-W_gs_mass` opens the paper at that equation and flashes it, `#genus-p2` at a paragraph, `#summary` at the summary. Inside an artifact only bare `#token` links survive, so the depth is not encoded in a link to a place: a link to a place always opens the paper there.
- **Wide formulas** scroll sideways inside their own box under an edge shadow while their number stays put, as in Epsilon.

What the format could not express, or that the skeleton got wrong, in this paper:

- Figure 7 is two sub-figures with one caption; Epsilon keeps the sub-captions as `(7a)`, `(7b)` and the skeleton named the node after the first of them.
- The abstract is a node of its own at the top of the Paper view; the summary layer does not reuse it, although the author's abstract is itself a rendition and the format could treat it as one.
- Equations without labels have no id and so no link; Epsilon numbers them, and the skeleton could give them `eq-2.16`-style ids from the number, as Epsilon's links do.
- The gists of paragraphs in the appendices are present but nothing folds a single paragraph by default; the appendix as a whole folds to its brief.
- The reading-time estimate counts the paper's words only; a specialist reads the derivations much faster than the dial suggests.

## 6c. The reader, rethought (15 October, evening)

After reading the first tree of his own paper, Erez asked for a calmer reader and for the question of what expands where to be settled. The answer now built into the viewer:

- **The dial chooses which document you read**: gist, summary, paper, everything. Each is a clean, linear text with nothing expandable inside it, and nothing in it is marked as tappable: a sentence of the summary, a defined term, a citation, a footnote marker and an equation number look like text until hovered or tapped.
- **A tap never rearranges the text; it opens a peek.** A peek is Epsilon's sheet: from the bottom on a phone, from the side on a desktop. A summary sentence peeks at the paragraphs it stands for; a term at its definition; a footnote marker at its note; a citation at its reference; an equation reference (in the summary) at the equation with its paragraph. The peek's header, *From §3.2 …* or *Defined in §2.1 …*, is the link that travels into the paper, and the long press on a link in the paper peeks instead of travelling, as in Epsilon.
- **Travelling leaves a way back.** A jump from the summary into the paper, or from one place in the paper to another, shows a pill in the bar (*↩ Summary*, *↩ Back*) that returns to the exact place, and is a browser history step as well. The target is marked for a few seconds once the scroll has settled.
- **The only inline expansion is the fold**, for what is optional in the Paper view: appendices, proofs and background notes. Closed, a fold is one quiet line with a circled + on the left; open, a circled − on the same spot. "Fold to one line" and "collapse to summary" are gone: they duplicated the dial.
- **The address is the link.** As you read, the hash follows the section (`#subsec-worldsheet`), or the document (`#summary`), so the address bar can be shared at any moment; the ¶ on a heading copies a link to that section. The *Copy link* buttons are gone.
- **One motion language**: everything that opens rises in, everything that closes falls out, with the same curve; tapping the title opens the contents; sheets close with a circled × at the top right.

## 6d. The tree, the app and the search (15 October, late)

- **Tree, not cone.** The paper is a tree: the trunk is the gist, the branches the summary, the foliage the paper, the roots its appendices and proofs. The files are `tree.json` and `tree.html`, the build is `tools/build_tree.py`, and the dial's hints use the tree's words.
- **An installable app.** The site carries a web app manifest, icons at every size a launcher asks for (16 and 32 for tabs, 180 for iOS, 192 and 512 plus a maskable 512 for Android, all drawn from the mark), theme colours for both appearances, and a service worker that keeps every page you have opened readable offline and refreshes it behind you. The pages are self-contained, so installing the index is enough.
- **Search, after Epsilon's rules.** The magnifier in the bar takes the bar, as Epsilon's does. Words are found in the text; a query with TeX in it is found in the formulas, each of which carries its TeX on its drawing; a symbol by name or typed (`phi`, `\phi`, `φ`) is found in every formula; spellings that mean the same are one (`\le` and `\leq`, `<=`, `\to` and `\rightarrow`, `\epsilon` and `\varepsilon`); `\left`, `\right` and sizes do not count; a letter asked for plainly is found in any font, accent or prime; `?` is any one symbol and `{?}` anything in braces; `$...$` searches the formulas only. Enter and the arrows step through the matches, Escape closes. It is a port of the rules in `viewer/search.js`, not Epsilon's code: Epsilon's search lives inside its page's script and cannot be loaded on its own. If it were factored out into a module of its own, both apps could share one file, and an update to Epsilon would reach Conifer at its next build.
- **Copying, as Epsilon does it.** A selection copied from the paper carries each formula as its TeX (`$…$` in a line, `\[…\]` on its own line), with the paper's own macros written out so that the TeX works anywhere; plain text copies as the browser does. Ctrl+F and Cmd+F open the paper's own search.
- **Links in the text** keep the text's colour and carry the faint dotted line; the accent is reserved for the chrome and the peek headers. Equation numbers are plain again.
- **The chosen tab glides** to its place in the dial and in every segmented setting, instead of snapping.
- **Motion rule.** Nothing shrinks or scales when pressed, anywhere. Feedback is colour, an underline, or a fade in or out; a sheet slides in from the edge it belongs to; the dial's pill glides; a place landed on is tinted and haloed for a few seconds.

## 6e. What a reader-test agent found (15 October, night)

An agent read and used the live site for a quarter of an hour, at desktop and phone widths, as the three readers. Real findings, all fixed: on a phone the leading between the lines of a summary sentence did not take a tap (now the whole line box does); the back pill crushed the section title in the bar on a phone (the reader pill now yields to it); Escape left the keyboard focus in the hidden search field. It also led to three changes of taste: a specialist starts with no section summaries and no chips (the settings' "By reader" default); the back pill names the section it returns to ("↩ §2.1") rather than "Back"; the disclaimer moved from above the gist to the foot of the page, so that the gist is the first thing on a phone. A fold now opens and closes where it stands, its height easing, so the text below slides rather than jumps. Its second pass judged the Skim level and the defaults. Skim: it earns its place for the specialist (headings plus topic sentences is how one scans a paper for where to start) and for the physicist (the bridge between the Summary and the Paper), but not for the student, who should not be offered lines written at the paper's level; and a tap on a line should go straight into the paper rather than through a peek. Applied: Skim is hidden for a student, and a tap on a skim line opens the paper at the paragraph with a *↩ Skim* pill (a long press still peeks). Defaults, as applied: section summaries at Paper depth only, for everyone but a specialist, with a quiet head ("In brief · AI draft · 2 questions") instead of a chip and a badge; no question badges in headings, the words in the lede head and a line on the gist card and the summary page instead; background notes open by default only for a student, folded to their line for everyone else, all open at Everything; the reader pill leaves the bar on a phone once you are in the paper (Settings keeps the choice); a one-line hint for students on the gist card that dotted words have definitions. Not applied, by Erez's rule: terms stay dotted for every reader. Erez then dropped the Skim level altogether: the dial has four positions again, and the one-line gists of the paragraphs stay in the data (they name folded proofs, and a tree may declare a skim level if it wants one).

**Formulas in a selection, and a symbol found inside a formula (15 Oct, after Epsilon).** The build puts under each drawn formula an unseen picture as wide as its drawing (`.mjx-hl` with `--w`), so a selection that crosses a formula is shaded by the browser at the line's whole height, inline and display alike; a formula is selected whole and copies as its TeX. The search finds a single symbol, or a short run of TeX, glyph by glyph in each formula's drawing (MathJax's `data-c` codes, with Epsilon's tables of what a command draws, letters in any font, accents and primes passed over unless asked for) and lays a soft box behind just those glyphs, inside the formula's own SVG; longer TeX still marks the formula whole.

**A section's brief is a fold (15 Oct).** At Paper depth the "In brief" block under a section title is a fold like every other: a circled +/− at the left of the title, and the whole title folds or opens it (the ¶, the question words and the badge keep their own taps). Folded by default for every reader (Erez, 15 Oct), with a setting to open them all, and each one remembers being folded or opened by hand for the visit. In a peek, and inside an appendix (whose title's circle is the appendix's own), the brief stands as it is.

**Three tabs, no minutes (16 Oct).** The Everything tab is gone: it was the Paper with the appendices, proofs and background notes unfolded, and each of those opens from its own circle. The dial is Gist, Summary, Paper. The minute estimates under the tabs and on the buttons are gone too. A saved Everything position or brief setting from an older visit is ignored.

**Design guideline: the fold pattern (16 Oct).** Everything that folds is built the same way, by one function in the viewer (`foldBlock`, with `secHead` for the folds that are sections). A fold is a **head that never moves** and a **body under it**. The head is identical open or closed: a circled +/− at the left and the title beside it, and the whole head is the control (a tap anywhere on it, except on a link, a defined word or the ¶, toggles). Only the body changes: its grid track eases from nothing to its size, and it wears the fold's box (a rule at its left for a background note). The head is a real heading when the fold is a section: a section's brief hangs under the section's own title, and an appendix's title is its head. So a closed fold is its head alone, and opening one adds the box below without moving anything above or the head itself. A new kind of fold (a proof, a derivation, a remark) must use this pattern: give it a head and a body, never a separate "closed line". In a peek the fold is open and has no circle.

**Why opening a fold was slow, and the fix (16 Oct).** The page is about 50 000 elements with 1 500 drawn formulas. Opening a fold shifts everything below it, and laying out and painting all of that took 200 to 500 ms in one frame (measured with a frame timer; the animation itself added 40 ms frames on top). Hiding the content below the fold removed the hitch, so the cost was the rest of the page, not the fold. The fix: the paper's blocks (paragraphs, equations, figures, list items, leaf nodes) use `content-visibility: auto`, so only what is near the screen is laid out and painted. A fold now opens in frames of 9 to 18 ms with the same animation. The price: unseen blocks stand at an estimated height until seen, so the page's total height grows as one reads, and where a far place is changes while the page scrolls towards it. `landAt` (viewer.js, also used by the search) therefore takes a long way in one jump and re-aims frame by frame until the place stays where it was aimed; the reader's own wheel, touch or key ends it. Headings and fold heads are never skipped. Anything new that scrolls to a place must go through `ConiferScroll.land`, not `window.scrollTo`.

**The search row in the bar's language (16 Oct).** No rounded box and no focus glow: a magnifier in the bar's deep blue, the words, and one line under them in that blue (fainter at rest, full while typing); its icons and its underline are drawn fine (1.5 and 1 px), as the logo and the circled controls are. The row has the bar row's exact edges and height, with the back arrow where the logo is and the arrows where the bar's buttons are, so swapping between the two rows moves nothing.

**The peek, after Epsilon's (16 Oct).** Peeks are no longer a modal sheet. The peek is a panel rising from the bottom at every width, with no veil, so the page stays readable and usable above it. Its head is a grip: dragged, the peek follows the pointer; let go, it settles at a third, a half or two thirds of the screen and remembers that size (`conifer-peek` in local storage); let go low, it closes; pulled up to the bar, it becomes the page. Its title's link (↗) takes the page there. Opening it: a long press on a link in the page, or a right click on a wide screen, opens the peek without moving the page; a tap on a summary's sentence, a note or a citation peeks as before. Inside the peek a link moves the peek, and its back arrow steps back; a long press or a right click on a link inside the peek takes the page there. Contents, Settings, Questions and definitions on a phone remain sheets. Also fixed: a block the page has just travelled to keeps its whole halo (blocks far from the screen clip their painting, so a flashed block, a found formula and a peeked sentence are painted whole), and an equation's edge covers no longer show as patches over a flash.

**Citations and the peek's motion, after Epsilon (16 Oct).** A tap on a citation opens the peek on the whole list of references, scrolled to the one cited and flashed, so its neighbours are there too ("Reference 12 in the references ↗"); a long press, or a right click, on a citation takes the page to the reference instead. Notes keep a peek of the note alone. The reference list shows its own numbers only (the list's numbers beside them are gone). The grip no longer re-lays out the peek while it moves: on a press the peek becomes as tall as it can be and only slides (a transform); let go, it springs to its size (Epsilon's spring curve) and only then takes that height. Opening and closing slide it from the bottom edge. Becoming the page (the title's link, or the grip pulled to the bar) is Epsilon's too: the peek grows up to the bar by a transform while its text fades, the page fades out, goes to the place halfway and fades back in, and the peek fades away; transforms and fades run on the compositor, so the page's jump does not stall them.

**The peek becoming the page, checked frame by frame (16 Oct).** Stepping through the expand with every animation and timer paused and sought showed four faults: the peek's text faded out before the page was there (an empty panel with only its header), the page's jump showed above the peek, the page came in at the wrong place and then scrolled in sight, and the place flashed off screen. Now the peek grows to the bar with its text as it is and its header fading away at once (only the text rises into place); grown, it covers the page, and the page goes to the place behind it in one jump, set so that the first block of lines the peek shows (a paragraph, an equation, a reference) stands at exactly the same height; the peek fades only after the page has held that place for two frames, and nothing flashes. For the two texts to be the same, line for line, the peek's blocks are contained as the page's are (content-visibility contains them there) and its list items take the page's margins and justification. Measured during the crossfade: equations and references within half a pixel, a summary sentence's paragraphs within about three.

**Swiping between the documents (16 Oct).** A sideways swipe on the page goes to the next document of the dial (to the left, deeper; to the right, back); the dial's pill follows the finger all the way, and can itself be dragged along the dial. A trackpad's sideways swipe is not taken (Erez, 16 Oct): on a desktop it stays the browser's back and forward. While it is held only the pill and the page's one layer move, by transforms against positions read once at the start, so nothing is laid out or drawn (the worst frame measured while swiping on the Paper was 11 ms). Let go past a third of the way, or flicked, the page slides on and out, the next document is drawn once and slides in from the other side; otherwise both spring back. Past either end the pill leans and gives. A swipe that starts in a wide equation, a table or anything else that scrolls sideways scrolls it instead, a vertical move scrolls the page as always, and a swipe is never taken for a tap on a link. A tap on a tab (or a card's "Read the summary" / "Open the paper") moves the same way: the pill glides and the page slides out and the next one in from the side it lies on.

**Loading: the tree grows (16 Oct).** While the page downloads and is read (it is several megabytes), a full-screen veil in the page's colour shows the Conifer icon growing: the trunk is drawn from the ground up, then the boughs from the trunk outward, the gist's pair first and the deepest last, then the nodes appear (the apex, then each joint with its two leaves), the tree holds, fades, and grows again. It is pure CSS, generated by `tools/loader.py` from the icon's own geometry and placed at the very start of the page, so it shows before any script is read; the viewer fades it out once the paper is drawn. With reduced motion it is the still icon, breathing.

**Travelling to a place, and the words it points to (16 Oct).** Following a link into the paper ("Defined in §1", a summary's "From §2.1", the contents) no longer redraws the paper when the place is already in it (a redraw cost a 200 ms freeze); a closed fold on the way opens where it stands. A short way is a glide that re-reads where it is going every frame, so it never lurches at the end; a long way is a quick fade of the page, the jump unseen, and the page fading back in at the place. The words a definition's link points to are marked by a soft band laid under them that rises and fades (the paragraph flash's language), replacing a highlight in the selection's own colour that Erez took for a stray selection.

**Layers, notes and the peek's expand button (16 Oct).** A note is a small layer of its own, as a definition is (a popover by its mark on a wide screen, a sheet on a phone), over the page or over the peek, which stays as it is. Closing goes one layer at a time: Escape, a click outside, the × or the veil close the popover, then a sheet, then the peek; the search closes only when nothing lies over the page. The peek has an expand button (as Epsilon's peek has), a circled control like the × beside it and the folds' +/−, which grows it into the page; its title's link does the same. The hand-over aligns on a paragraph, an equation or an entry (not a heading, which the peek draws smaller), and when the peek goes the room under the page it still stands on is kept (a place near the paper's end would else be pulled up), and the bar's title and the address are brought up to date at once.

**One icon system (17 Oct).** An audit found five line weights (the logo 0.9px, the bar's icons 1.8px, the search row's 1.25px, the expand 1px, and the x and +/- typed characters) and two rings. Now every icon is drawn in one line, 1.25px whatever its size, with round ends: the bar's (the logo too), the search row's, the peek's. The bar's icons are deep blue. The small circled controls (a fold's +/-, the x of a sheet, a popover or the peek, the peek's expand) are one control: the same thin grey ring and grey glyph drawn as lines (no typed characters), and on hover the deep blue with its soft ground; two sizes only, in the text (a fold's) and in a header. Anything new follows this (viewer.css, "ONE ICON SYSTEM").

**The dial as a depth line (17 Oct).** The pill (a grey track and a raised white button) took too much focus, so the dial is now three quiet small-caps labels over a thin line, the icon's trunk laid on its side, with a dot under each tab. The line is lit in deep blue from the first dot up to how deep one reads (Gist: one dot; Paper: the whole line); a dot turns blue and grows only once the line has reached it, and shrinks back as the line leaves it; the dots never move. A swipe or a drag moves the line with the finger, a tap glides it; the current label is deep blue and bold. Line and dots follow the icon system (one 1.25px line). Prototypes of the alternatives (the pill, an underline, the depth line with a sliding dot) are in `mockup/tab-bars.html`; Erez chose the quiet depth line with dots that only grow.

**The bar, balanced, with one blue line at a time (17 Oct).** The title stands on the page's axis, over the dial's middle dot (it was 75px to the left, the right end being heavier); with the back pill it yields and stands between. The reader pill ("Physicist") left the bar, the last boxed and bold thing in it; who one reads as is chosen in Settings. The gaps from the bar's edge to the icons, to the labels, to the line and to the bar's edge are even (8 to 12px). The bar casts the peek's shadow. The rule for focus: the bar shows one deep-blue line at a time. Reading, it is the depth line; searching, it is the search's underline, and the dial goes grey where it stands (its place and size kept). The search's underline is drawn as the dial's line is (a 1.25px vector line with round ends; a border would round to 1px), so the two are the same line. The mockups are in `mockup/bar-balance.html`; Erez chose A.

**One line for the tabs and the search (17 Oct).** Erez chose the order kept (the title row on top: the logo, the title on the axis, search and settings; the tabs below), with the search taking the tab row. The bar has one line. Reading, it is the depth line under the tabs; searching, the labels give way to the field (your words, the count, the arrows; no magnifier and no back arrow in it) and the same line stays where it is and only changes its length, from its lit part to the field's whole width, the dots shrinking away; closing, back, and the dot where one reads grows again. The line never fades or changes colour. The title row's magnifier fades into an x while searching, which closes it (as Escape does). No swipe between the tabs while searching. The mockups of the other orders (the tabs on top; the search at the end of the tab row in the Paper only; the tabs between the logo and settings) are in `mockup/bar-order.html`.

**Searching what is selected (17 Oct).** With text selected, opening the search (its button or Ctrl/Cmd+F) searches the selection at once: words as they are, each formula as its TeX as written (as the search reads formulas). A passage of words and formulas is found as Epsilon finds it: the paper read as one stream, each formula as its normalised TeX between two marks, the words in any case and spacing, so a hit is that passage in order (its formulas boxed), not every place one of its parts occurs.

**A fold reveals, it does not move (17 Oct).** Opening a box (a background note, an appendix, a brief), its text is laid out at its final place from the start and the edge of its body slides down over it, uncovering it line by line; no fade, nothing shifts; closing, the edge slides back up. For that, a note's rule, indent and size are the same open or closed (they changed at the moment of opening, reflowing the text), the gap under a head is inside the part that opens, and the blocks inside an opening box take their true sizes at once (content-visibility would have them at an estimate first). The fold rules are on the fold itself (child combinators), so a closed fold inside an open appendix keeps its state.

**Search sees only what is open; formulas in the words' colours (17 Oct).** Text inside a closed box is left out of the search (its head is not); opening or closing a box searches again where the reader is, without moving. A formula found is marked in exactly the words' two colours, and a passage's formulas take the colour of the match one is on.

**References and notes (17 Oct).** The notes and the references end the paper at its top level (the converter had hung them on the last appendix, where a closed fold hid them); the converter's own heading inside them is hidden (the page heads them); an arXiv number is set in the text's face with lining figures (the browser's monospace was larger than the text around it); a note's number stands beside its text.

## 7. Open questions for you

1. **Whose papers first?** Your own (author-owned trees published next to the arXiv version) or any paper in the Epsilon library (reader-made trees, unreviewed by the author)? Both fit the format; they set different priorities for the skill's quality bar and for the provenance chips.
2. **The tip.** Context / Result / Why it matters, or Nature's Problem / Solution / Implications, or free? A fixed template makes trees comparable across papers and lets a library list them; I would fix it.
3. **The one-page summary.** Flowing prose written as one piece (what the mockup does) or composed from the sections' briefs? Prose reads better and is harder to keep in sync; composition is automatic. The format allows both; the skill needs a default.
4. **Thread or replace** when a summary opens, and should it differ between the summary page and the Paper view?
5. **Authoring surface.** Sidecar YAML (my proposal), LaTeX macros, or both? Would you want the layers to appear in the PDF too (a "Summary" page after the abstract, say)?
6. **Audiences.** Which three (or two, or four)? Who is the default? Should the audience change the *paper* text as well, or only summaries, background notes and underlines, as in the mockup?
7. **Questions layer.** Author-anticipated, AI-anticipated, reader-submitted, all three? Do you want a live "ask" in the viewer (needs a key or a small server) or the static layer plus "copy with context" to your own chatbot, as in the mockup?
8. **Extractive mode.** Scim-style highlights (show the key sentences of the original and elide the rest) as a fifth position on the dial, or as the paragraph-level fold instead of a rewritten gist?
9. **Where it lives.** Inside the Epsilon app, or a separate viewer that reuses Epsilon's converter and theme?
10. **The machine interface.** Is "a paper that is an API" (JSON + an expand tool for agents) in scope for the first version, or later?
11. **First real example.** Your SUSY random matrices draft, or one of the shorter papers in the library?

## 8. Name and logo

Conifer: a tree, evergreen, and the tree with the gist at its tip. The logo in `logo/` is a conifer drawn as a hierarchical graph: a trunk of nodes from the apex (the gist) down, with boughs at each level reaching wider the deeper they go. One colour, round strokes, reads at 16 px. `conifer-icon.svg` is the mark, `conifer-wordmark.svg` adds the name, `conifer-app-icon.svg` puts it on a blue tile for a home screen.

## Sources

- Stretchtext: [Wikipedia](https://en.wikipedia.org/wiki/Stretchtext); Nate Matias's [Stretchtext authoring system](https://natematias.com/portfolio/2006-03-27-stretchtext-authoring-system/); Andy Matuschak's [note](https://notes.andymatuschak.org/zPLUdgxrXo5z24ccuyz8YQ4).
- Telescopic text: [I Made Tea](https://elmcip.net/creative-work/i-made-tea) (Joe Davis); [telescopic-text](https://npmjs.com/package/telescopic-text).
- Gwern, [Design of This Website](https://gwern.net/design) (collapsible sections, popups, "semantic zoom").
- Qlarify: [arXiv 2310.07581](https://arxiv.org/html/2310.07581v2), [UIST 2024](https://doi.org/10.1145/3654777.3676397).
- TreeReader: [arXiv 2507.18945](https://arxiv.org/abs/2507.18945), [code](https://github.com/aspuru-guzik-group/TreeReader).
- Paper Plain: [arXiv 2203.00130](https://arxiv.org/pdf/2203.00130), [demo](https://openreader.semanticscholar.org/PaperPlain).
- Scim: [arXiv 2205.04561](https://arxiv.org/abs/2205.04561). ScholarPhi: [project page](https://www.infodocket.com/2021/05/11/new-from-the-uc-berkeley-school-of-information-scholarphi-a-novel-interface-for-reading-scientific-papers/). Semantic Reader: [arXiv 2303.14334](https://www.arxiv.org/pdf/2303.14334).
- DocVoyager: [Adobe Research, CHI 2025](https://research.adobe.com/publication/docvoyager-anticipating-users-information-needs-and-guiding-document-reading-through-question-answering).
- Nota: [nota-lang.org](https://nota-lang.org/).
- Lean blueprint: [leanblueprint on PyPI](https://pypi.org/project/leanblueprint/); KnowTeX: [arXiv 2601.15294](https://arxiv.org/abs/2601.15294).
- Article of the Future: [Physics World](https://physicsworld.com/a/is-this-the-article-of-the-fut/), [Research Information](https://www.researchinformation.info/?p=1845).
- Octopus: [Jisc project page](https://www.jisc.ac.uk/rd/projects/octopus-creating-a-new-primary-research-record-for-science).
- MyST: [AST primer](https://mystmd.org/spec/ast-primer), [overview](https://mystmd.org/guide/overview).
- Zoomable hierarchical texts: [US patent 11,321,416](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11321416); elision-based text zooming: [Sam Davis, UBC](https://www.cs.ubc.ca/~tmm/courses/old533/projects/sam/report.pdf).
- SciZoom (hierarchical summarisation benchmark): [arXiv 2603.16131](https://arxiv.org/abs/2603.16131). InsightGUIDE: [arXiv 2509.20493](https://arxiv.org/html/2509.20493v1).
