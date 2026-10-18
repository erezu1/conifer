"""The drafted layers of arXiv:2609.29859 (The cosmological necklace problem).

Drafted by an AI reader from the paper's text; nothing here has been checked by the authors yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.

Note on ids: the converter gives the two pairs of subsections "Standard solutions" / "Tunneling solutions" of
sections 2.3 and 2.4 the same ids (standard-solutions, tunneling-solutions and their -pN). The build keeps the
later ones, so every gist, brief and grounding span using these ids means the section 2.4 nodes; the section 2.3
copies get no layers and are grounded through sec-pure_grav_3d-p1..p3 instead (see FLAGS).
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2609.29859 · hep-th · September 2026"
DATE = "24 September 2026"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "The cosmological necklace problem"
# The equation is the headline in one line: the k=1 saddle picked by the shifted Lorentzian contour has action
# -pi/2G whatever the flux q. The figure shows the same contour deforming onto the k=1 thimble (real G, q=0.1).
KEY = {"equation": "action237", "figure": "fig-plot_minus_degenerate"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on the gravitational path integral, de Sitter entropy or quantum cosmology"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy or gravity theorist; knows Euclidean saddles and de Sitter space in outline"},
    {"key": "student", "label": "Student", "hint": "knows general relativity, quantum mechanics and path integrals from first graduate courses"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (sect1.1unentropicsols, sect1.2proposal,
# section-1.3-p2). "Summing over all Euclidean solutions is not a reasonable definition of the path integral" and "the
# Lorentzian contour is the appropriate one from an observer's perspective" are conclusions the paper draws from the
# necklaces and from their resolution, so they are why it matters, not contributions.
# How they relate (skill section 2), from the paper's own words: one argument. The necklaces (A) are the problem; the
# Lorentzian contour (B) is introduced "To remedy this" (abstract); the non-Euclidean dominant solution and its
# flux-independent entropy are properties of the saddle that dominates, linked by the paper ("the dominant contribution
# ... is the solution a_-"; "this Lorentzian detour ... is essential to obtain a q-independent on-shell action"); the
# higher-dimensional necklaces (C) are "further evidence for the generality of our claim". The other contour
# N=-eps+iR is part of the same steepest-descent analysis (theme B) and needs no link of its own.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-necklace", "headline": True,
     "claim": r"Gluing $k$ copies of a 3d de Sitter axion wormhole gives an infinite series of closed Euclidean saddles, “cosmological necklaces”, with entropy growing linearly in $k$, so no saddle dominates and the Euclidean path integral diverges.",
     "quote": "an infinite series of Euclidean saddles corresponding with repeated bounces",
     "where": ["sect1.1unentropicsols-p4", "gauged-quantum-mechanics-p2"], "theme": "A"},
    {"id": "c-single", "headline": True,
     "claim": r"In a minisuperspace steepest-descent analysis, the (mostly) Lorentzian lapse contour $N=\varepsilon+i\mathbb R$ is dominated by a single necklace, the Gibbons–Hawking saddle, so the entropy is finite; the crucial element is treating $a\to-a$ as a gauge redundancy, whose sector has a pole at zero lapse.",
     "quote": "we find that a single necklace dominates, leading to a finite entropy",
     "where": ["tunneling-sector-p1", "walls-p1", "subsect2.5.4gen-p1"], "theme": "B",
     "builds_on": "c-necklace", "link_quote": "To remedy this, we study the gravitational path integral using a (mostly) Lorentzian lapse contour"},
    {"id": "c-lorentzian",
     "claim": r"The dominant solution is not purely Euclidean: it reaches $-a$ only by winding once around the big-crunch singularity of its Lorentzian continuation, a bra-ket wormhole, which adds a flux-dependent term to its action.",
     "quote": "the dominant solution is not purely Euclidean",
     "where": ["tunneling-solutions-p2", "tunneling-solutions-p3"], "theme": "B",
     "builds_on": "c-single", "link_quote": "a steepest descent analysis now reveals that the dominant contribution to the gravitational path integral is the solution"},
    {"id": "c-flux",
     "claim": r"The dominant necklace's entropy is $S=\pi/2G$ for every axion flux $q$, equal to the entropy of empty de Sitter space; the paper finds this puzzling and traces it to deforming the time contour to late times, where the universe approaches empty de Sitter.",
     "quote": "Its entropy turns out to be independent of the axion flux",
     "where": ["tunneling-sector-p1", "tunneling-solutions-p4", "sect-3.3-p2"], "theme": "B",
     "builds_on": "c-lorentzian", "link_quote": "We stress that this Lorentzian detour, and the associated correction"},
    {"id": "c-higherd",
     "claim": r"For 4d and 5d axion necklaces, and for necklaces sourced by SO$(d-1)$ Yang–Mills fields, the paper argues, mainly numerically within minisuperspace, that the single necklace again dominates along $N=\varepsilon+i\mathbb R$.",
     "quote": "argue for qualitatively similar results",
     "where": ["sect3.3kineticnum-p6", "sect4-magnetic-p5", "app-contours-p4"], "theme": "C",
     "builds_on": "c-single", "link_quote": "In this section, we will provide further evidence for the generality of our claim"},
    {"id": "c-vilenkin",
     "claim": r"The other regularisation, $N=-\varepsilon+i\mathbb R$ (a Vilenkin-type contour), picks up only $k\le0$, is dominated by the trivial $k=0$ “saddle”, and predicts no entropy at order $1/G$.",
     "quote": "These contours only pick up the saddles with",
     "where": ["tunneling-sector-p1", "app-contours-p5", "sect5-concl-p2"], "theme": "B"},
]

# Every version states the five contributions the abstract claims; c-vilenkin, claimed only in the introduction
# (conclusion-p2, section-1.3-p2), is in the summary and not in the gist (skill section 3).
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sect-1.intro-p3 sect1.1unentropicsols-p3">Euclidean axion wormholes were proposed to give cosmological observers an entropy.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-necklace"><span data-covers="sect1.1unentropicsols-p4 gauged-quantum-mechanics-p2">Gluing copies of a 3d axion wormhole makes “necklace” saddles of unbounded entropy: the Euclidean sum diverges.</span></li>
  <li data-claims="c-single"><span data-covers="tunneling-sector-p1 walls-p1">In minisuperspace a (mostly) Lorentzian lapse contour lets one necklace dominate, finite in entropy,</span> <span data-covers="gauged-quantum-mechanics-p1 subsect2.5.4gen-p1">through a zero-lapse pole from identifying scale factors $a$ and $-a$.</span></li>
  <li data-claims="c-lorentzian"><span data-covers="tunneling-solutions-p2 tunneling-solutions-p3">The dominant necklace is partly Lorentzian, not purely Euclidean.</span></li>
  <li data-claims="c-flux"><span data-covers="tunneling-sector-p1 sect-3.3-p3">Its candidate entropy, $S=\pi/2G$, is puzzlingly empty de Sitter's, whatever the axion flux.</span></li>
  <li data-claims="c-higherd"><span data-covers="sect3.3kineticnum-p6 sect4-magnetic-p3 sect4-magnetic-p5">Axion numerics in 4d and 5d, and Yang–Mills magnetic necklaces, again give one dominant necklace.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sect1.1unentropicsols-p4 conclusion-p1">So summing Euclidean solutions cannot define the path integral; a Lorentzian lapse contour may.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sect-1.intro-p4 sect1.1unentropicsols-p3">Euclidean axion-dS wormholes were proposed to give an FLRW observer's entropy, $-I_0$.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-necklace"><span data-covers="gauged-quantum-mechanics-p2 sect1.1unentropicsols-p4">Their $k$-fold covers, necklaces with $I=-k\pi(1-q)/2G$, make the Euclidean lapse contour diverge.</span></li>
  <li data-claims="c-single"><span data-covers="gauged-quantum-mechanics-p1 subsect2.5.4gen-p1">Gauging $a\to-a$ adds $\mathcal G_N(a|-a)$, with a pole at zero lapse;</span> <span data-covers="tunneling-sector-p1 walls-p1">in minisuperspace $N=\varepsilon+i\mathbb R$ then picks the $k=1$ saddle, a finite entropy; constant-$\text{Re}\,I$ lines through the poles exclude $k\ge2$.</span></li>
  <li data-claims="c-lorentzian"><span data-covers="tunneling-solutions-p2 tunneling-solutions-p3">That saddle is partly Lorentzian: its scale factor winds around the big crunch, a bra-ket wormhole.</span></li>
  <li data-claims="c-flux"><span data-covers="tunneling-sector-p1 sect-3.3-p2">Its action, $-\pi/2G$, would give empty dS's entropy for every $q$, as deforming the time contour to late times, where the solution is empty dS, shows.</span></li>
  <li data-claims="c-higherd"><span data-covers="sect3.2kinetic-p1 sect3.3kineticnum-p6">4d and 5d numerics, in a gauge giving $a$ a standard kinetic term, agree;</span> <span data-covers="sect4-magnetic-p3 sect4-magnetic-p5">applied to SO$(d-1)$ Yang–Mills necklaces, it agrees too.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sect1.1unentropicsols-p4 conclusion-p1 section-1.3-p2">Summing Euclidean solutions cannot define the path integral; the shifted contour is suggested instead, and flux independence offered to Lorentzian algebraic calculations to reproduce or disprove.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sect-1.intro-p3 sect1.1unentropicsols-p3">A sphere gives de Sitter's entropy; Euclidean “wormholes” were proposed to do so for closed axion-filled universes.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-necklace"><span data-covers="sect1.1unentropicsols-p4 gauged-quantum-mechanics-p2">Gluing copies of a 3d wormhole gives “necklaces” of ever larger entropy: the Euclidean sum diverges.</span></li>
  <li data-claims="c-single"><span data-covers="tunneling-sector-p1 walls-p1">Integrating over Lorentzian time instead picks one necklace, with finite entropy,</span> <span data-covers="gauged-quantum-mechanics-p1 subsect2.5.4gen-p1">once sizes $a$ and $-a$ count as the same.</span></li>
  <li data-claims="c-lorentzian"><span data-covers="tunneling-solutions-p2 tunneling-solutions-p3">The winning necklace is partly Lorentzian, not purely Euclidean.</span></li>
  <li data-claims="c-flux"><span data-covers="tunneling-sector-p1 sect-3.3-p3">Its candidate entropy, $S=\pi/2G$, is puzzlingly empty de Sitter's, whatever the axion flux.</span></li>
  <li data-claims="c-higherd"><span data-covers="sect3.3kineticnum-p6 sect4-magnetic-p3 sect4-magnetic-p5">In 4d and 5d, and with Yang–Mills fields, mostly numerical evidence suggests the same.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sect1.1unentropicsols-p4 conclusion-p1">So summing all Euclidean solutions cannot define the path integral; a Lorentzian time contour may.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="sect-1.intro-p3 sect-1.intro-p4">The Euclidean sphere, the Wick rotation of de Sitter space, gives the Gibbons–Hawking entropy $A/4G$ of an observer's static patch. The paper takes this entropy as a requirement on the gravitational path integral.</span> <span data-covers="sect1.1unentropicsols-p3">Euclidean axion wormholes, closed universes whose two ends are glued, were proposed to give an observer's entropy in the same way.</span> <span data-covers="sect1.1unentropicsols-p4">The paper finds that any number of them glue into a “necklace” of larger entropy, so a sum over Euclidean solutions diverges and cannot define the path integral.</span> <span data-covers="tunneling-sector-p1 conclusion-p1">Instead it integrates the lapse, the elapsed time between two slices, along a (mostly) Lorentzian contour. Within minisuperspace a single necklace then dominates and the entropy is finite.</span></p>
<p><span data-covers="sect2.1setup-p1 sect2.1setup-p2">In three dimensions, with an axion flux $q$ through the spatial sphere, a closed homogeneous universe reduces to a particle, the scale factor $a$, in a potential. A wall near zero size makes Euclidean solutions bounce between two sizes.</span> <span data-covers="gauged-quantum-mechanics-p2">Gluing at the largest size gives necklaces of $k$ bounces at lapse $N=k\pi$, with action $I=-k\pi(1-q)/2G$.</span> <span data-covers="gauged-quantum-mechanics-p2 sect1.1unentropicsols-p4">A Euclidean contour, over positive real lapse, sums them all, so the entropy is unbounded and the integral diverges. Since each necklace covers the single wormhole, no local rule can exclude it.</span></p>
<p><span data-covers="gauged-quantum-mechanics-p1 sect1.2proposal-p2">The metric depends only on $a^2$, so the paper treats $a\to-a$ as a gauge redundancy, and the trace sums the propagators from $a$ to $a$ and from $a$ to $-a$.</span> <span data-covers="sect2.2exact-p2 sect2.2exact-p4">In three dimensions both are known exactly, and their semiclassical limits are effective actions $I(N)$ whose saddles are the even and the odd necklaces respectively.</span> <span data-covers="subsect2.5.4gen-p1 tunneling-sector-p1">Reaching $-a$ in no time costs infinite energy, so the sign-flipping action has a pole at $N=0$, which the contour $N=\varepsilon+i\mathbb R$ passes on the right.</span> <span data-covers="tunneling-sector-p1">A Lorentzian contour normally cannot reach a saddle of negative action, since Lorentzian actions are imaginary. The pole evades this, so the $k=1$ saddle contributes, with positive entropy $S=-I$.</span> <span data-covers="walls-p1 standard-sector-p2">Lines of constant height through the poles wall off the higher necklaces, and the standard sector keeps only suppressed saddles with $k\le0$.</span></p>
<p><span data-covers="tunneling-solutions-p1 tunneling-solutions-p2">That saddle keeps one sign in Euclidean time and reaches $-a$ only by winding once around the big-crunch singularity of its Lorentzian continuation.</span> <span data-covers="tunneling-solutions-p3">This detour, a bra-ket wormhole, adds a flux-dependent term to the action and reproduces the exact propagator.</span> <span data-covers="tunneling-sector-p1 tunneling-solutions-p4">The dominant saddle therefore has $S=\pi/2G$ for every flux, the entropy of empty de Sitter space.</span> <span data-covers="sect-3.3-p2">The paper traces this to deforming the time contour to late times, where any such universe is empty de Sitter, as the cosmic no-hair theorem demands.</span> <span data-covers="sect-3.3-p3 dominant-solution-p1">The authors find it puzzling but hard to avoid in three dimensions, and offer it as a target for Lorentzian algebraic calculations.</span></p>
<p><span data-covers="sect3.2kinetic-p1 sect3.2kinetic-p2">In higher dimensions no exact propagator is known, so the paper assumes the same two sectors, in a “kinetic gauge” where $a$ has an ordinary kinetic term.</span> <span data-covers="sect3.3kineticnum-p5 sect3.3kineticnum-p6">Numerically, in four and five dimensions, every ascent line reaching the contour drops below a height from which no necklace with $k\ge2$ could descend, so one necklace dominates.</span> <span data-covers="app-contours-p4 sect4-magnetic-p5">An analytic five-dimensional treatment of empty de Sitter, and necklaces made of Yang–Mills fields, give the same outcome.</span></p>
<p><span data-covers="tunneling-sector-p1 conclusion-p2">Passing the pole on the left, $N=-\varepsilon+i\mathbb R$, keeps only $k\le0$, so the trivial $k=0$ “saddle” dominates, as for a Vilenkin-type contour.</span> <span data-covers="sect5-concl-p2 app-contours-p5 plan-for-the-remainder-of-this-section-p1">It predicts no entropy at order $1/G$, as if horizon area were not entropy; the paper keeps it as a possible answer for the global Hilbert space.</span> <span data-covers="conclusion-p3">Neither contour is free of trouble: on the first the conformal mode keeps its wrong-sign fluctuations, on the second all matter fluctuations are unstable.</span></p>
<p><span data-covers="sect5-concl-p3">Everything is done in minisuperspace, and the steepest-descent picture may change beyond it.</span> <span data-covers="on-shell-action-p4">Only in three dimensions is the tunneling solution shown to govern the quantum mechanics. Elsewhere it is assumed, and then flux independence would hold only in three dimensions.</span> <span data-covers="on-shell-action-p3 on-shell-action-p4">Above three dimensions it would also give the Einstein static universe more entropy than empty de Sitter, against the second law, unless it is not the right solution there.</span> <span data-covers="sect3.3kineticnum-p3">The numerical exclusion of higher necklaces is not fully airtight.</span> <span data-covers="sect5-concl-p5 sect5-concl-p4">The detour violates the KSW allowability criterion, though perhaps not a weaker spectral version, and no static-patch quantum mechanics counts the entropy directly.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "sect1.1unentropicsols-p4", "note": r"The introduction gives each $k$-cover entropy $k|I_0|$, with $I_0$ the Euclidean wormhole action, which (2.19) makes $-\pi(1-q)/2G$; but the saddles the contour selects have $-I=k\pi/2G$ for every $q$ ((2.36), (2.37)), the difference being the Lorentzian detour's $\pi q/2G$. walls-p1 and sect3.3kineticnum then write $|I_0|$ for the $q$-independent value. Is $I_0$ meant to include the detour? The layers give (2.19) for the Euclidean necklaces and $\pi/2G$ for the dominant saddle."},
    {"node": "sect-1.intro-p2", "note": r"“their entropy is greater than the Gibbons-Hawking entropy”: with (2.19) a $k$-necklace has $k\pi(1-q)/2G$, which exceeds $\pi/2G$ only for $k(1-q)>1$, so not every $k>1$ necklace at large $q$. Is the comparison meant with the $q$-independent saddle actions, or for large enough $k$? The layers say only that the entropy grows without bound."},
    {"node": "sect-3.3-p2", "note": r"(2.80) is labelled $GI_{a\to-a}(2\pi)$, but the Gibbons–Hawking saddle studied there is at $N=\pi$; and the text says the second line “is exact and gives $\pi/2$” while the result is $-\pi/2$ (the second-line integrand also looks positive). Presumably $I_{a\to-a}(\pi)$ and $-\pi/2$."},
    {"node": "app-contours-p5", "note": r"“choosing the contour $N=-\varepsilon+i\mathbb R$, the leading contribution is $k=-1$”: within the bouncing ($a\to-a$) sector; overall the standard sector's $k=0$, with $I=0$, dominates, as conclusion-p2 and sect5-concl-p2 say. Worth saying “in this sector”."},
    {"node": "sect4-magnetic-p2", "note": r"The abstract speaks of necklaces “sourced by … Yang-Mills instantons”, while section 4 builds a purely magnetic configuration, the gauge field equal to the spin connection (the meron in $d=4$, footnote 22), and calls them magnetic wormholes. The layers use “Yang–Mills fields” and “magnetic necklaces”; is “instantons” intended?"},
    {"node": "fig-app2", "note": r"Caption: “$a_0\to a_\text{mas}$”, presumably $a_\text{max}$."},
    {"node": "appa1-p1", "note": r"In 5d proper-time gauge (A.13) has saddles at $N=k\pi$, including $N=\pi$ with the same action as the $a\to-a$ saddle (A.17) at $N=\pi$; so here the single sphere seems to appear in both sectors, unlike in 3d (standard-solutions of section 2.3: “the single Euclidean sphere does not arise in this $a\to a$ sector”). Harmless for the conclusion, since app-contours-p2 shows $N=\pm\varepsilon+i\mathbb R$ picks only $k\le0$ there, but the drafter was unsure the parity rule is meant to hold in this gauge."},
    {"node": "sec-pure_grav_3d", "note": r"Not the paper's: the converter gives the subsections “Standard solutions” and “Tunneling solutions” of sections 2.3 and 2.4 the same ids, so only the section 2.4 copies carry layers. The section 2.3 copies (the $q\to0$ trajectories, the single sphere arising only for $a\to-a$) are covered through the section 2.3 brief and sec-pure_grav_3d-p1..p3."},
]
