"""The drafted layers of arXiv:2105.15059 (The entanglement entropy of typical pure states and replica wormholes).

Drafted by an AI reader from the paper's text; nothing here has been checked by the author yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2105.15059 · hep-th · May 2021"
DATE = "31 May 2021"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "Typical pure states and replica wormholes"
# The equation is the headline in one line: the averaged entropy as the smaller of the thermal entropies of A and of
# its complement, (4.7), readable with phi, beta and c alone. The figure shows the switch of RT surface at phi = pi,
# the mechanism of the Page curve; figure 1 only sketches the expected curve.
KEY = {"equation": "eq-pure_entropy_holo", "figure": "fig-phase_transition"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on holographic entanglement, replica wormholes or black hole microstates"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows AdS/CFT and the Ryu–Takayanagi formula in outline"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory, density matrices and a first course on AdS/CFT"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (section-1-p2, p4 to p7).
# How they relate, from the paper's own words: the averaged Rényi entropy as a path integral on a singular geometry
# (QFT side, section 4.1) is what the holographic calculation then evaluates ("Writing the averaged entropy as a path
# integral, we can employ the holographic dictionary", section-1-p5); the Page curve is that evaluation (section 4.2);
# the refined RT formula is the same calculation for a general region ("The final result is a refinement of the RT
# formula", section-1-p6). One theme, each item building on the one before: one argument.
# Not contributions: the review of the thermal case (section 3); the extension of the island conjecture and the
# purity origin of the connected saddle, which are what the results mean (Why it matters); the one-loop formula
# (4.10), a proposal made in the body only; the free-field checks of appendix B, which support c-pathint.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-pathint",
     "claim": r"For any field theory, the Rényi entropy averaged over an ensemble of Euclidean-evolved pure states is a path integral on a singular replicated geometry, which different smoothness assumptions turn into equivalent geometries: $n$ thermal-like tori, or one torus connecting all replicas.",
     "quote": "as a path integral on a singular replicated geometry",
     "where": ["section-4.1-p3", "section-4.1-p6", "section-4.1-p7"], "theme": "A"},
    {"id": "c-page", "headline": True,
     "claim": r"For a CFT with a gravity dual, the two geometries give different bulk saddles: the thermal saddle dominates for intervals shorter than half the circle, and the saddle connecting the replicas beyond, so the averaged entropy follows a Page curve.",
     "quote": "the dominant saddle connects the replicas in a non-trivial way",
     "where": ["section-4.2-p3", "section-4.2-p4"], "theme": "A",
     "builds_on": "c-pathint", "link_quote": "Writing the averaged entropy as a path integral, we can employ the holographic dictionary to find its value"},
    {"id": "c-rt",
     "claim": r"The result is a refinement of the RT formula for typical pure states, in which the RT surface may be homologous to either the region or its complement: a weaker homology constraint.",
     "quote": "where now the RT surface has a weaker homology constraint",
     "where": ["section-4.2-p5"], "theme": "A",
     "builds_on": "c-page", "link_quote": "The final result is a refinement of the RT formula for the case of typical pure states"},
]

# Every version states c-pathint and c-page, which the abstract claims; c-rt, claimed in the introduction, fits in
# a short point and is stated too. Why it matters is the abstract's closing sentence and the introduction's framing
# of the headline (section-1-p2: replica-connecting saddles "imposed by the field theory calculation, from the purity").
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p2 section-1-p3">A typical pure state on a circle should show a Page curve in an interval's entanglement entropy, but lacks a thermal state's simple path integral.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-pathint"><span data-covers="section-4.1-p3 section-4.1-p4">Averaging the Rényi entropy over an ensemble of pure states writes it as a path integral on replicas identified at $\tau=\pm\beta/2$: a singular geometry.</span></li>
  <li data-claims="c-page"><span data-covers="section-4.2-p3 section-4.2-p4">At high temperature the bulk's thermal saddle dominates short intervals and a replica-joining saddle, allowed by that geometry, past half the circle: a Page curve, absent at low temperature.</span></li>
  <li data-claims="c-rt"><span data-covers="section-4.2-p5">The RT surface may then be homologous to the interval or its complement.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p2">Purity, not conjecture, imposes these saddles, extending the island conjecture to a non-evaporating setting.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p2 section-1-p3">A typical high-energy microstate of a holographic CFT on a circle should follow Page's curve; unlike the thermal state, whose entropy is a Euclidean path integral with an RT dual, it needs $O(1/G_N)$ insertions.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-pathint"><span data-covers="sec-ensemble-p2 section-4.1-p3 section-4.1-p6">For an ensemble of Euclidean-evolved basis states, $\overline{S_n}$ is the thermal replica integral with all replicas identified at $\tau=\pm\beta/2$; it equals both $n$ separate tori and one connected torus.</span></li>
  <li data-claims="c-page"><span data-covers="section-4.2-p3 section-4.2-p4">Each topology has its own bulk saddle; for $\beta\ll\varphi$, $\overline{S_{vN}}\approx\frac{c}{6\beta}\min\{\varphi,2\pi-\varphi\}$, thermal below half the circle and replica-connected above, with no transition in the low-temperature phase.</span></li>
  <li data-claims="c-rt"><span data-covers="section-4.2-p5">In general $\overline{S_{vN}(A)}=\text{Area}(X^*)/4G_N+O(G_N^0)$, with $X^*$ homologous to $A$ or to $A^c$.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p2">Saddles like replica wormholes are imposed here by the purity of the ensemble states rather than conjectured, extending the island conjecture to a non-evaporating setting.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p2 section-1-p3">For a typical pure state on a circle, an interval's entanglement entropy should follow a Page curve; no simple path integral computes it.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-pathint"><span data-covers="section-4.1-p3 section-4.1-p4">Averaging over many pure states gives a path integral over copies (replicas) of spacetime with fields set equal at one time: a singular geometry.</span></li>
  <li data-claims="c-page"><span data-covers="section-4.2-p3 section-4.2-p4">At high temperature gravity's thermal saddle wins for short intervals, a replica-joining one past half the circle: a Page curve, absent at low temperature.</span></li>
  <li data-claims="c-rt"><span data-covers="section-4.2-p5">The entropy's minimal surface may then enclose a bulk region with either the interval or its complement.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p2">Here purity, not assumption, forces replica-joining saddles, extending the island conjecture beyond evaporating black holes.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="section-1-p2">Take a typical high-energy pure state of a field theory on a circle, and ask for the entanglement entropy of an interval $A=[0,\varphi]$.</span> <span data-covers="section-1-p2 fig-page_curv">Because the state is pure, the entropy should follow a Page curve: thermal for short intervals, then falling back symmetrically past half the circle.</span> <span data-covers="section-1-p3">A thermal state is easy, since its entropy is a Euclidean path integral, but one microstate needs of order $1/G_N$ operator insertions.</span> <span data-covers="section-4.2-p4">The paper averages over an ensemble of pure states instead, and finds the Page curve with the standard holographic dictionary.</span> <span data-covers="section-4.1-p3 section-4.2-p5">Saddles joining the replicas, like replica wormholes, appear without being conjectured: the purity of the states imposes them.</span></p>
<p><span data-covers="sec-ensemble-p2">Each ensemble state is a basis state, such as a field configuration on the circle, evolved by $e^{-\beta H/2}$; for a generic basis it resembles a typical state at energy set by $\beta$.</span> <span data-covers="section-3.1-p1">Averaging the density matrices first would give the thermal state.</span> <span data-covers="sec-termal_GR-p2 sec-termal_GR-p3">Its holographic entropy is a BTZ geodesic homologous to the interval, which keeps growing with $\varphi$.</span> <span data-covers="section-4.1-p2 section-4.1-p3">Averaging the Rényi entropies instead gives the thermal replica integral with one change: the field at $\tau=\pm\beta/2$ is identified across all replicas, because each carries the same state.</span> <span data-covers="section-4.1-p3">This identification makes $\varphi\to2\pi-\varphi$ a symmetry, as purity requires.</span> <span data-covers="app-another_replica-p4">The average is taken inside the logarithm, which a second replica trick shows to be exact at leading order in $G_N$.</span></p>
<p><span data-covers="section-4.1-p6">The identified integral is singular, so where the field is taken smooth is a choice that changes the topology but not the integral.</span> <span data-covers="section-4.1-p6 section-4.1-p7">One choice gives $n$ separate tori, as in the thermal case; another gives one long torus connecting all replicas, and moving the cut to $2\pi-\varphi$ exchanges the two.</span> <span data-covers="section-B.1.2-p5 section-B.1.2-p6">For the harmonic oscillator with two replicas the equality is checked explicitly.</span> <span data-covers="section-4.1-p4 section-B.2.2-p4">The identification also brings UV divergences, cancelled by local counter-terms on the identified circles and absent in the energy basis.</span></p>
<p><span data-covers="section-4.2-p1">In gravity the two geometries are filled by different saddles, which are summed.</span> <span data-covers="section-4.2-p3">The separate tori give the thermal entropy, a geodesic homologous to $A$.</span> <span data-covers="section-4.2-p4">In the connected saddle the bulk surface also ends on the identified circle, so its geodesic is homologous to $A^c$ and gives the thermal entropy of the complement.</span> <span data-covers="section-4.2-p4 fig-phase_transition">The smaller wins, $\overline{S_{vN}}\approx\frac{c}{6\beta}\min\{\varphi,2\pi-\varphi\}$ at high temperature: past half the circle the surface swallows the black hole, an island covering the horizon.</span> <span data-covers="section-4.2-p2">The identification touches bulk fields only at one loop, so this leading result does not depend on the ensemble.</span> <span data-covers="section-4.2-p5">For a general region, the RT formula for typical states lets the surface be homologous to $A$ or to $A^c$.</span></p>
<p><span data-covers="app-another_replica-p3 app-another_replica-p4">Replica-symmetric saddles are assumed to dominate, which the paper argues only away from $\varphi=\pi$.</span> <span data-covers="section-4.2-p6">The one-loop correction is a proposal.</span> <span data-covers="section-4.1-p4 section-4.2-p7">Those divergences have no clear bulk meaning, and in string theory the identification allows new strings whose consistency is left open.</span> <span data-covers="sec-discussion-p3">A Lorentzian version is also open.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the author; not shown to readers).
FLAGS = [
    {"node": "fig-pure_replica", "note": r"The caption says the topology ensures $S_{vN}(\rho_\alpha(\varphi))=S_{vN}(\rho_\alpha(\varphi))$; presumably the right-hand side should be $S_{vN}(\rho_\alpha(2\pi-\varphi))$?"},
    {"node": "section-3.1-p3", "note": r"“we don’t expect $S_{vN}(\overline\rho(\varphi))\ne S_{vN}(\overline\rho(2\pi-\varphi))$” reads as a double negative; is “we don’t expect … $=$ …” meant? The layers say the thermal entropy is not symmetric."},
    {"node": "section-4.2-p6", "note": r"(4.10) ends in $+O(G_N^{-1})$, which is the order of the leading area term; after the $O(G_N^0)$ bulk entropy, should it be $O(G_N)$? (4.9) has $+O(G_N^0)$."},
    {"node": "app-another_replica-p3", "note": r"“Any other partition … has free energy $(\sum_i n_i^{1-d})\cdot\frac{a_d}{G_N\beta^{d-1}}$” lacks the minus sign of $I(\beta)=-\frac{a_d}{G_N\beta^{d-1}}$; with it, the fully disconnected saddle is the most negative, as concluded."},
    {"node": "sec-ensemble-p2", "note": r"The ensemble selects “states with energy $E\sim1/\beta$” (also section-1-p4, section-4.1-p1, (4.9)). For a CFT$_2$ on a circle at high temperature the energy grows as $c/\beta^2$; is “temperature $1/\beta$” meant? The layers say “energy set by $\beta$”."},
    {"node": "app-ident-p2", "note": r"(B.2) sums $\log(an^2)$ while (B.1) and the result are for general $an^\alpha$; presumably $\log(an^\alpha)$."},
    {"node": "section-B.2.2-p3", "note": r"(B.53) is stated “at $m=0$ (and removing the zero mode)” but keeps $\frac{2\pi\sinh(mL/2)}{m}$, which tends to $\pi L$; unsure whether the massive zero-mode factor is meant to stay."},
    {"node": "section-4.2-p4", "note": r"(4.8) is stated for $\beta\ll\varphi$; near $\varphi\to2\pi$ it also needs $\beta\ll2\pi-\varphi$. Minor."},
]
