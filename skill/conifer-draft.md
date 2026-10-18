# Drafting a Conifer tree

These are the instructions an AI drafter follows to turn a converted paper into the layers of a Conifer tree: the gist, the one-page summary, the section briefs, the paragraph gists, the definitions, the background notes and the questions. They were written on 17 October 2026 from a review of the first draft (arXiv:2608.21511), whose main faults were length and voice: every layer paraphrased the one below in the paper's own dense style, and definitions and notes were anchored where the paper treats a term formally rather than where a reader first meets it.

## 0. The pipeline

```
python3 tools/convert.py <paper.tex | folder | archive | arXiv id> -o DIR   # DIR/doc (Epsilon's converter), skeleton.json, outline.md
#   ...the drafter reads DIR/outline.md and writes DIR/layers*.py (this document)...
python3 tools/build_tree.py DIR                   # checks ids and quotes, writes tree.json and tree.html
python3 tools/check_layers.py DIR                 # measures the draft against the rules below
python3 tools/blind_gist.py DIR                   # the abstract and the gist alone, for a blind reader (section 3)
```

Read the whole of `outline.md` before writing anything. First list the paper's contributions (section 2). Then write bottom-up: paragraph gists, section briefs, then the root summary and gist, then the side tables. Then run the build and the checker and fix every problem and every issue the checker reports, unless the issue is one the rules below allow (say so in a comment).

## 1. The reader and the voice

- **Three audiences.** `specialist` works on this paper's subject; `physicist` (or the field's equivalent) is a researcher from a neighbouring area and is the default; `student` has the field's first graduate courses. Name them in `AUDIENCES` with a one-line hint that says what each knows.
- **Plain, short, and an argument.** Sentences of at most about 30 words. Explain every technical term the first time a layer uses it, in a few words, unless the audience surely knows it; a term the summary needs late ("Landau spacing") is introduced where it first appears. Short is not choppy: join a claim to its reason with "so" or "because", and let one grounding span cover two sentences that make one point, so that the prose reads as an argument and not an inventory of claims.
- **Formulas only when they are results.** Write a formula only when it is itself a result the reader should take away: a closed form, a scaling, a bound, a critical value. Up to three such relations per summary paragraph; none that is a step of a derivation. Bare symbols ($\nu$, $SU(2)$) are fine when named. Leave out intermediate scalings, ansätze, regime conditions and equation numbers, except a regime that is the paper's subject (a symbol set against a number, such as $Q_5=1$; the checker does not count these).
- **Keep the paper's confidence, in both directions.** "argues", "suggests", "is in tension with", "presumably" stay as they are, and what the paper states as found is not hedged ("arguably" for what the abstract says it finds); never make a claim stronger than the paper does ("can test this exactly" for what the paper calls "a sharper test"), never turn the paper's question into its claim ("echoes an older puzzle" for "we ask whether it is related"), and never add a claim the paper does not make, even in a definition.
- **No salesmanship and no meta.** No "this paper elegantly", no "the discussion summarises", no "in this section we".
- **The paper's own names.** Use the paper's terms. If a layer needs a name the paper does not give, mark it as yours ("what we call here…").
- **Check, don't copy.** Check every number, scaling and formula against its node. If the paper contradicts itself (a fall-off written two ways, a factor that differs between sections), do not copy one version: write the consistent one if it is clear, and record the conflict in `FLAGS` (section 8).

## 2. The paper's contributions (`CONTRIBUTIONS`), first

Before any layer, list what the paper itself claims as its results. Every later layer is checked against this list, so that no result is lost and none is misfiled (a first draft of arXiv:2406.14605 put one result under Result and two others under Why it matters).

- **2 to 6 items, taken from the paper, not chosen by the drafter**: the abstract's claims and the introduction's own list ("we show", "we argue", "our main result is", "we also find"). One item per independent result; a step towards a result is not one.
- Each item: `id` ("c-…"), `claim` (one plain sentence, with the paper's own hedge), `quote` (a few words, verbatim, from the abstract or the introduction where the paper claims it; the checker finds them), `where` (the 1 to 3 body paragraphs that establish it), and `headline: True` for the one or two the paper puts first.
- **Not a contribution**: the setup, a review, the motivation, or a consequence the paper draws from a result (that is why it matters).
- **How the results relate, decided from the paper, not supplied.** Some papers make one argument whose steps build on each other; others report several findings with no stated relation between them (arXiv:2406.14605 has three: the genus expansion of the grand-canonical orbifold, the breakdown of string perturbation theory, and the decoupled extra torus with its deformations; a draft tied them into one story and was wrong, Erez, 18 Oct). Give each item a `theme` (one letter; items of one finding share it, usually one section of the paper each), and give an item that builds on another `builds_on` (that item's id) with `link_quote`, the paper's own words stating the link (the checker finds them in the paper). No quote, no link: two results the paper does not connect are written as separate, however naturally they could be connected. A link may cross themes (a finding that reuses another's result, as type II strings reuse the W-star analysis in arXiv:2608.21511): the themes stay separate findings, and the point may say what it reuses.
- Set `SHAPE` in layers.py: `"one argument"` when every theme is one (or each builds on another), `"several findings"` otherwise.

## 3. The gist (`ROOT_GIST`)

The card a reader sees first, read in thirty seconds. Its three bullets have three different jobs, and each is grounded:

- **Context**: the question or puzzle the paper starts from. Grounded (`data-covers`) in the introduction. For **several findings**, the setting they share (the system the paper studies, and what it sets out to do, in its own words), not the question of one of them.
- **Result**: **points, one per contribution** (Erez, 17 Oct: a reader scans points faster than a sentence that lists), for every contribution the abstract claims (its `quote` is from the abstract), the headline first. Each point is one short sentence, at most about 25 words (35 for the specialist; a finding's point with two results, 45 and 60), and claims exactly one contribution (or, for several findings, the contributions of one finding). **A point stands on its own**: it names its subject rather than opening with "It", "Its", "This", "So" or "Thus" pointing to the point before, unless its contribution `builds_on` that one (the checker flags it). For **several findings, one point per finding** (theme): the paper's grouping is the reader's (three issues, three points; five points under "three issues" read as five), and a finding with two linked results states both in its point, in up to two sentences (`data-claims` names both); nothing in a point suggests a link to another finding. A contribution claimed only in the introduction goes in the summary, and in the gist only if it can be stated specifically in the space left. **Each is stated as what was found**, never only that something was found: "bosonic strings pose a possible issue" says nothing; "for bosonic strings the black hole's free energy has a kink that the string star's lacks" does (the checker flags such empty phrases). Each point names its contribution and where it is established: `<li data-claims="c-genus"><span data-covers="sec-grand-p3">…</span></li>`. Name the mechanism of the headline result, not only its consequence.
- **Why it matters**: what the results mean beyond this paper, for the field's open questions, as the paper itself frames it in its introduction or its discussion, and **first of all the significance the paper gives its headline result** (what the introduction says it explains, resolves or makes possible). A remark the paper makes about a secondary result ("usually string theory does not allow decoupled sectors, but here…") is not why the paper matters; it can go in that result's point. For **several findings**, Why it matters does not present one finding's significance as the paper's: it says what the paper as a whole is for (its stated aim), or gives each finding its own short clause; never a "This shows…" that gathers them into one conclusion the paper does not draw. When the paper itself draws one conclusion from some of its findings (its abstract ends on it), that conclusion is Why it matters, naming the findings it rests on. It claims **no** contribution and is grounded in paragraphs of the introduction, the discussion or the conclusion. The test: a sentence that could be followed by "the paper shows this in §n" is a result and belongs under Result.
- The shape:

```html
<ul class="gist-list">
<li><b>Context</b> <span data-covers="…">…</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-…"><span data-covers="…">…</span></li>
  <li data-claims="c-…"><span data-covers="…">…</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="…">…</span></li>
</ul>
```
- **At most 90 words** for the default audience (110 when the paper has more than two contributions), never longer than the abstract. At most **one formula** in the default and student gists. No equation numbers, section or appendix references.
- **Variants differ in vocabulary and in what they state, not in which results they report.** Every version, the student's too, states every contribution the abstract claims, and its Why it matters builds only on results its own Result states. The specialist version may run to about 130 words (150 with more than two contributions) with up to four formulas: it states the results a specialist would check (the critical values, the scalings, what is computed exactly), and names prior work only in Context, for the result the paper builds on, and where a result agrees with earlier work or contradicts it. State results, not citations.
- **A blind read.** When the gist is written, give a fresh reader (another agent) only what `python3 tools/blind_gist.py DIR` prints: the abstract, every version of the gist, and the paragraphs each of the gist's sentences cites. Ask: does the abstract present one argument or several findings, and does the gist (its order, its "this", "so", "thus", its Context and Why it matters) claim links between results that the abstract does not make; does Result state, point by point, each result the abstract claims; is every sentence under Why it matters the paper's own framing of its headline result, rather than another result or a side remark; is every sentence supported by the paragraphs it cites, at the abstract's confidence? Fix what it finds and read again.

## 4. The summary (`ROOT_BRIEF`)

The one-page version, read in a few minutes.

- **450 to 700 words in 4 to 7 paragraphs** (250 to 450 for a paper under 8 000 words, a letter or proceedings); the long end for a paper with many contributions or several findings. The closing paragraph on what the paper does not show stays, whatever the shape.
- **Complete.** Every item of `CONTRIBUTIONS` appears in the summary, grounded in one of its `where` paragraphs (the checker tests this), and so does each result the paper singles out as a nice observation.
- **For several findings, one part per finding** (a finding claimed only in the introduction too: it has no point in the gist, but it has its part here). Open with the setting they share, then give each finding its own paragraph (or two), each opening with its own question and closing on its own result; between them a plain turn ("Separately, the paper…"), never a frame the paper does not use (the paper's own "three confusing issues" is fine; "three puzzles that together show…" is not). The closing paragraph on limits may take the findings in turn. The rule of joining claims with "so" and "because" holds within a finding, not across findings.
- **Ordered by logic, not by section.** Paragraph one gives the question, the answer and why it matters (for several findings: the setting they share and the findings it holds, by name, in the paper's own framing, such as "three confusing issues"). The middle paragraphs give the argument: the idea that makes it work, then the main results, each with the reason it holds. The last paragraph gives the limitations, what the paper does not show, and the open questions.
- **Grounding.** Every sentence sits in a `<span data-covers="…">` naming the **1 to 3 paragraph ids** (or a figure or box id, when the skeleton has it as a node) of the body that *establish* the claim: not the introduction's announcement of it, and not a whole section. Equations are not nodes: they live inside paragraphs, so ground on the paragraph that holds the equation. A sentence that cannot be grounded is not written. The introduction's own brief is the exception: it grounds on the introduction.
- The rules of section 1 apply in full: short sentences joined into an argument, terms explained, up to three result formulas per paragraph.

## 5. Section briefs (`BRIEF`) and paragraph gists (`GIST`)

The brief is the "In brief" fold under a section's title, read before deciding whether to read the section.

- **40 to 90 words** for a leaf section, up to **110** for a section with subsections; appendices 40 to 70. Acknowledgements get no brief.
- Say what the section **establishes and how**, as a short paragraph of its own, **with its main result as the paper states it**: when that result is a formula (a scaling, a critical value), the brief gives it. Never one sentence per paragraph of the section, never a repeat of a child's brief or of the root summary. A parent's brief says what its subsections add up to.
- Up to two result formulas in a brief, one in a gist; regimes ($2<d<6$, $Q_5=1$) do not count.
- Ground its sentences as in section 4.
- A **paragraph gist** (also boxes, figures, sections) is one line of **at most 20 words** stating the paragraph's claim. A section's gist always states the section's claim, never its topic ("Why the index can test…" is a table of contents, not a gist); a "role" line ("Sets up…", "Defines…") is allowed only for a setup paragraph. Keep the one contrast that makes a paragraph's point ("…unlike the thermal Sen limit, its area does not vanish"). Appendix gists state claims too. Write none for acknowledgements, convention-only or recap paragraphs: a node can lack a gist. Do not copy the gist's words into the brief; the two are written for different moments.

## 6. Definitions (`DEFS`)

A definition opens when a reader taps a dotted term, anywhere in the tree.

- **What to define.** Every term central to the result that is not standard for the default audience: always the paper's main object (the thing the title is about), its notation conventions (dimensions such as $d$ versus $D=d+1$, units, the meaning of a parameter's ends), and ordinary words used in a technical sense ("decouple", "saddle", "dominates"). Usually 15 to 30 entries.
- **Anchor at the first mention.** `at.node` and `at.quote` are the **first sentence in reading order that uses the term** (the checker enforces this), usually in the introduction ("…or a 'string star'"; "We call those solutions 'W stars'"); not a later formal treatment. The reader taps the term where they first meet it, so the definition itself must say what the term is, whether or not that sentence does.
- **A term the paper names late.** If the layers need a word earlier than the paper first uses it (the paper says "twist" only in §3), anchor the definition at the paper's first plain use, and have each layer explain the word in passing where it first uses it.
- **Only terms with a word name.** A notion written only as a symbol ($J\bar J$, $\Gamma_0(N)$, $p$) has no word in the text to dot: carry it in a background note or in the notation question. The quote is a few words that occur verbatim in the node's text as `outline.md` prints it (formulas as their TeX), and it should contain the term or an alias in plain words: a term the paper first writes only inside a formula or a compound ("½-BPS") is anchored at its first plain-word occurrence.
- **Length and order.** 25 to 60 words. Say what the term is before its role in this paper.
- **Aliases are true synonyms only**: inflections, plurals, the paper's abbreviations and spellings ("Atick-Witten" for "Atick–Witten"). Never a broader word ("BPS" for "BPS bound"), a related but distinct concept ("small black hole" for "Sen limit": give it its own entry), or a phrase the paper also uses with another meaning ("winding mode" when it sometimes means another mode). The checker reports any alias that occurs more than 15 times: such an alias is almost always too broad.
- **A term with two senses.** If the paper itself uses the term in two senses ("decouple" for a saddle and for a sector of the theory), say so in the definition, since every mention is dotted.
- Record the term's symbol, if it has one, as `symbol`.

## 7. Background notes (`BACKGROUND`)

A folded box placed in the paper, after a paragraph, holding what that paragraph assumes.

- **When.** Only for a prerequisite that the paper assumes, the stated audience plausibly lacks, and the next paragraph needs. Typically 3 to 7 shown to the default audience; notes for students alone may add a few more. If the paper's key mechanism is non-standard (a twisted identification acting as a magnetic field, an unusual limit), it gets a note.
- **Never a paraphrase of the paragraph it follows.** Supply what the paragraph takes for granted, not what it says.
- **Where.** Right after the **first** paragraph whose argument uses it (not one that merely names it), unless that paragraph itself explains the idea: then the note supplies what that explanation assumes, or is not written. An introduction that names every prerequisite in passing does not get all the notes: no more than two or three in it, and the others where the body works with the idea. One note per concept; notes must not overlap. Several notes after one paragraph appear in the order they are listed.
- **Length and content.** 100 to 180 words of textbook content, standard results only, ending with one sentence that connects it to the paper.
- **It names its subject.** The body uses the words of its title (the checker tests that most of them occur), so that a note cannot be filed under the wrong title.
- **Audience.** Tag only the audiences that need it, usually `["student"]`, and `["student", "physicist"]` only when a researcher from a neighbouring area would also lack it. The fold's head names them ("for students").

## 8. Questions (`QUESTIONS`), the key figure and equation, flags

- **5 to 15 questions** a careful reader would ask, each anchored at the region it is about (`at.node`), each answered in **about 40 to 90 words**, with `answeredBy` naming the paragraphs that answer it.
- Include at least one on **notation or regimes** (what the parameters mean, which limit is which) and at least one on **what the paper does not show**, answered honestly.
- `KEY`: the ids (the `\label`s, as `eq-…` and `fig-…`; the build checks they exist) of the equation and the figure that **carry the headline result** and can be read without the section around them. If the headline is not a formula, choose the equation of the key mechanism.
- `FLAGS` (optional, for the author, not shown to readers): a list of `{"node": id, "note": "…"}` for every inconsistency found in the paper and every place the drafter was unsure.

## 9. The files

`DIR/layers.py` holds the metadata and the root, and imports the rest:

```python
from layers_gists import GIST          # {node id: html}  one line per paragraph, box and section
from layers_briefs import BRIEF        # {section id: html}  one paragraph each, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND
KICKER = "arXiv:<id> · <category> · <Month Year>"
DATE = "<day Month Year>"
NOTE = "The paper as a Conifer tree. … drafted by an AI reader and have not yet been checked by the author."
PAGE_TITLE = "<a short title>"
KEY = {"equation": "<eq id>", "figure": "<fig id>"}           # either may be omitted
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [{"key": "specialist", "label": "Specialist", "hint": "…"}, …]
ROOT_STATUS = "ai-draft"
ROOT_GIST = {"html": r"""<ul class="gist-list">…</ul>""", "status": "ai-draft",
             "variants": {"specialist": {"html": r"""…""", "status": "ai-draft"}, "student": {…}}}
ROOT_BRIEF = {"html": r"""<p><span data-covers="…">…</span> …</p> …""", "status": "ai-draft"}
VARIANTS = {}                          # {node id: {"brief": {audience: html}}}  optional
FLAGS = []
SHAPE = "several findings"             # or "one argument" (section 2)
CONTRIBUTIONS = [{"id": "c-…", "claim": "…", "quote": "<words from the abstract or introduction>", "where": ["<para id>", …],
                  "headline": True, "theme": "A", "builds_on": "c-…", "link_quote": "<the paper's words linking them>"}, …]
```

- `DEFS`: `{"id", "term", "symbol"?, "aliases": [...], "html", "at": {"node", "quote"}}`.
- `QUESTIONS`: `{"id", "at": {"node"}, "source": "ai", "status": "draft", "q", "a", "answeredBy": [...]}`.
- `BACKGROUND`: `{"id", "after": <paragraph id>, "title", "audience": [...], "body": "<p>…</p>"}`.
- Math is TeX between `$` signs, in raw strings; the paper's own macros may be used. HTML is plain: `<p>`, `<b>`, `<i>`, `<span data-covers>`.
- Everything drafted is `ai-draft` (renditions) or `"status": "draft"` (questions) until the author approves it.

## 10. Before handing over

1. `python3 tools/build_tree.py DIR` reports no problems (unknown ids, quotes not found).
2. `python3 tools/check_layers.py DIR` reports no issues except ones you have justified in a comment.
3. Read the gist and the summary once as each audience, start to finish, and cut anything that reader would skip.
