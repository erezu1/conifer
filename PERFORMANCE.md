# Making the reader faster and lighter (17 October 2026)

A report on where the reader spent its bytes and its time, what was changed, and what is left. All numbers are for the
string-star tree (arXiv:2608.21511), the heaviest, measured in Chrome on a MacBook with the startup marks now in the
viewer (`conifer:start`, `parsed`, `indexed`, `drawn`, `ready`, and the measures `conifer:draw` and
`conifer:paper-complete`) and the browser's long-animation-frame timings. A phone was not measured; a mid-range one is
typically four to six times slower at script and layout, and its network is the bigger cost.

## 1. What was measured

**Weight.** The page was 6.3 MB (2.26 MB gzipped, as GitHub Pages sends it), of which:

| Part | Size | Why |
|---|---|---|
| Formula drawings (1 635 SVGs) | 3.0 MB | a third of each drawing was markup the reader never uses |
| Figures (8 PNGs, inside the page as base64) | 2.5 MB | three plots at 2400 px, 0.6 MB each, shown at ~700 px |
| Text, layers, viewer, styles | 0.8 MB | |

**Time.** Opening at Paper depth: the 6 MB JSON parsed in 12 ms; drawing the Paper (one 5.5 MB HTML string,
47 899 elements) took 122 ms in one long frame of 170 ms. Style and layout cost only 8 ms (the earlier
content-visibility change). Switching from the Gist to the Paper froze the page for **183 ms** each time, because the
whole Paper was built again. At Gist depth the page was ready in 7 ms.

**Interactions that were already fine:** scrolling (median frame 8 ms, worst 19 ms), opening a fold (11 ms), search
(no frame over 50 ms; the count appears after the 180 ms typing pause), a citation's peek (35 to 55 ms).

## 2. What was changed

1. **Slimmer formulas** (`tools/slim.py`, used by both builds). Removed: MathJax's per-group `data-mml-node` marks
   (kept only the three its stylesheet uses), `data-mjx-texclass`, `xmlns`, `role`, `focusable`, the outer group's
   stroke and fill (one CSS rule now), `xlink:` on every glyph reference, a translate's zero argument, bare groups
   around single glyphs, and groups that only place one glyph (the glyph takes `x`/`y`). The formulas are 40% smaller
   and the Paper has a quarter fewer elements. Checked: every one of the paper's 1 345 formulas has the same size and
   every glyph the same position to half a pixel; the search still finds the same 479 occurrences of ν.
2. **Lighter figures** (`tools/figures.py`, run with the project's `.venv`, which has Pillow). No wider than 1400 px,
   and stored with a 128-colour palette when that is within the eye of the original (line plots are; photographs keep
   their colours). 1.9 MB of figures became 0.43 MB. Each figure now carries its width and height (its room is known
   before it loads) and loads lazily.
3. **Figures as files on the site.** The build writes `web/index.html` beside `tree.html`: the same page with each
   figure a file of its own, fetched only when it comes near the screen. The site serves that; `tree.html` and the
   artifact stay self-contained.
4. **The Paper is kept.** Leaving the Paper no longer destroys it: its container hands its id to another and is hidden
   with `content-visibility: hidden`, so coming back costs 1 ms instead of a rebuild, and the folds are as they were.
   (A first try moved the Paper's elements out and back in; that cost 25 ms out and 74 ms in, as much as a rebuild.)
5. **A fresh Paper is drawn in slices**: a section's head, then its paragraphs, as pieces of a few milliseconds, the
   first ones at once and the rest in later tasks, so the page never locks. A link to a place, the search, or the peek
   growing into the page finishes the drawing first. Checked: the Paper drawn in slices has the same 228 nodes in the
   same order and states, and the same text, as the Paper drawn in one piece.
6. **A closed fold holds nothing until opened.** The appendices (folded by default) and the background notes were a
   third of the Paper's elements; their bodies are now built on first opening (an appendix: 27 ms), or when a link or a
   jump needs a place inside them.
7. **Fonts no longer block the first paint** (a non-blocking stylesheet switched on by the viewer, with preconnect to
   Google Fonts), so the growing-tree loader shows at once on a slow network.
8. **The service worker** still asks the network first, but shows the kept copy if the network has not answered within
   3 seconds (and refreshes it in the background); figures, named by their content, are used from the cache as they are.

## 3. The result

| | Before | After |
|---|---|---|
| String-star page sent over the network | 2.26 MB | **0.35 MB** (+ figures 0.43 MB, only when seen) |
| 2406.14605 page sent | 0.81 MB | **0.28 MB** (+ 0.06 MB) |
| Self-contained page / artifact | 6.3 MB | 3.1 MB |
| Viewer's startup work at Paper depth | 139 ms | **30 ms** |
| Longest frame while opening at Paper | 170 ms | **none over 50 ms** |
| Switching into the Paper | 183 ms freeze | **1 ms** (kept), 20 ms first slice (fresh) |
| Elements in the Paper | 47 899 | **26 556** |
| Script memory | 34 MB | **19 MB** |

## 4. Afterwards: scrolling after a link

Erez saw the place jump when he scrolled after following a link. Measured: the far landing's hold did not yield to the
reader, and blocks drawn for the first time at the screen's edge sometimes moved the text despite scroll anchoring
(3 of 25 small steps off by up to 157 px). Fixed by yielding, and by drawing blocks within two screens ahead
(`near`, viewer.js `watch`); after, 0 of 75 steps were off. Startup is unchanged (34 ms).

## 5. What is left

- **A real phone.** These are laptop numbers; the next step is to open the site on a phone with remote debugging and
  read the same marks.
- **WebP or AVIF figures.** No encoder is installed (`sips` cannot write WebP); a palette PNG is already close for
  line plots, but a photograph would gain.
- **Self-hosted, subset fonts.** Two Google font families in several weights; serving only the glyphs used from the
  site would remove a third-party round trip.
- **The citation peek** (35 to 55 ms) re-inserts the whole list of references each time; it could keep one.
- **The search** walks the whole text on every query (fast here, under 50 ms); a prepared index would matter for
  much longer papers.
