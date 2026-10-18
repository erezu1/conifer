"""The drafted layers of arXiv:2011.06328 (A Derivation of AdS/CFT for Vector Models).

Drafted by an AI reader from the paper's text; nothing here has been checked by the authors yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2011.06328 · hep-th · November 2020"
DATE = "12 November 2020"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the authors.")
PAGE_TITLE = "AdS/CFT derived for vector models"
# The headline is a map, not a formula; (1.3) is the one equation that shows its outcome, the local quadratic action
# with its two particles per spin, and it can be read with M^2 defined beside it. The map itself, (1.2) (unlabelled)
# or (4.15), cannot be read without sections 3 and 4. No figure carries a headline result (Figure 1 is a contour,
# Figure 2 the mass-deformed profile), so none is chosen.
KEY = {"equation": "eq-bulk_S2_local_schematic"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on higher-spin holography, bi-local holography or large-N vector models"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows AdS/CFT and large-N field theory in outline"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory, path integrals and a first course on AdS/CFT"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (intro-p3 to intro-p9).
# How they relate, from the paper's own words: one construction. The map (c-map) is used to build the action
# (sec-quadratic_action-p1), whose higher terms give the loop rules (sec-bulk_theory-p1); the finite-N constraints are
# the bi-local rank constraints carried through the same map (intro-p5). Theme B, the two deformations, applies "our
# formalism" (intro-p9): the mass deformation reuses the map, and the critical model reuses the free bulk Feynman
# rules (critUNbulk-p3). Every theme builds on another: one argument.
# c-critical's quote is the abstract's "free or critical", so every gist states it; c-mass is claimed only in the
# introduction and appears in the summary, not in the gist.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-map", "headline": True, "theme": "A",
     "claim": r"The path integral of the $U(N)$ or $O(N)$ free vector model is rewritten explicitly, within the $1/N$ expansion, as a path integral over fields of all integer spins on a fixed AdS$_{d+1}$: bi-local fields are expanded in conformal eigenmodes, which are identified, up to a normalization $f_{\Delta,J}$, with the bulk-to-boundary modes of transverse traceless bulk fields; the map is linear, invertible and finite.",
     "quote": "as a path integral over fields (including massless high-spin fields)",
     "where": ["sec-cft_to_ads-p1", "sec-ads_to_cft-p3", "sec-cft_to_ads-p10"]},
    {"id": "c-action", "headline": True, "theme": "A",
     "claim": r"The map gives an explicit bulk action, non-local in general; for one normalization its quadratic part is local with four derivatives, giving a physical field of each spin (massless for $J>0$) and a wrong-sign ghost. For $U(N)$ this is Vasiliev's spectrum, the ghosts matching Faddeev–Popov ghosts; the action is presumably Vasiliev's theory in a specific gauge (for $O(N)$ the ghost spins do not match).",
     "quote": "an explicit (non-local) action for a high-spin theory on anti-de Sitter space",
     "where": ["section-5.1-p2", "section-5.3-p2", "section-5.3-p4"],
     "builds_on": "c-map", "link_quote": "we can use it to construct the bulk action by mapping the bilocal action"},
    {"id": "c-loops", "theme": "A",
     "claim": r"The bulk action comes with Feynman rules and explicit counter-terms that cancel the loop divergences: shown at one loop, argued to all orders in $1/N$, so the action can be used for loop computations.",
     "quote": "can be used also for loop computations",
     "where": ["section-6.3-p3", "section-6.3-p4", "section-6.3-p5"],
     "builds_on": "c-action", "link_quote": "We will now construct all the higher order bulk interaction and counter terms from the CFT"},
    {"id": "c-finiteN", "theme": "A",
     "claim": r"At finite $N$ the same rewriting holds in principle, but the bulk fields obey non-local constraints on products of $N+1$ of them, inherited from the rank bound on the bi-local field, which exclude most configurations, empty AdS among them.",
     "quote": "extra constraints on products of bulk fields",
     "where": ["sec-local_to_bilocal-p5", "sec-local_to_bilocal-p6", "section-5.3-p4"],
     "builds_on": "c-map", "link_quote": "obey complicated constraints, that will map in our formalism to complicated constraints on the bulk fields"},
    {"id": "c-critical", "theme": "B",
     "claim": r"The critical model in $2<d<4$ has the same bulk action as the free one; only the bulk scalar's propagator changes, from $\Pi^{TT}_{d-2,0}$ to $\Pi^{TT}_{2,0}$, a change of boundary condition, which gives the critical correlators at all orders in $1/N$.",
     "quote": "path integral for the free or critical",
     "where": ["critUNbulk-p2", "critUNbulk-p3"],
     "builds_on": "c-loops", "link_quote": "since we already showed that the free bulk dual gave the expected bulk diagrams dual to the free CFT"},
    {"id": "c-mass", "theme": "B",
     "claim": r"The mass deformation corresponds to a classical bulk solution on AdS with only the scalar turned on, depending on $mz$ alone ($\propto m^2z^2$ for small mass, computed numerically for finite mass in $d=3$), found with a separate map for non-decaying configurations.",
     "quote": "there is a corresponding classical solution of the bulk equations of motion",
     "where": ["sec-smallmass-p2", "sec-finmass-p2"],
     "builds_on": "c-map", "link_quote": "we apply our formalism to two interesting deformations of the CFT"},
]

# Every version states the five contributions the abstract claims (c-map, c-action, c-loops, c-finiteN, c-critical);
# c-mass, claimed only in the introduction, is in the summary. Why it matters is the introduction's own framing of the
# headline (intro-p3, intro-p4): the bulk is fields on one fixed AdS with no sign of a topology sum, and the action is
# a quantum completion of high-spin gravity.
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="intro-p2 intro-p3">What bulk does a CFT define beyond $1/N$? Simplest case: vector models, dual to high-spin gravity.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-map"><span data-covers="sec-cft_to_ads-p1 sec-ads_to_cft-p3">Matching conformal eigenmodes of $\phi^*(x_1)\phi(x_2)$ with AdS modes gives a path integral over all-spin AdS fields.</span></li>
  <li data-claims="c-action"><span data-covers="sec-bulk_theory-p1 section-5.3-p4">The non-local bulk action is presumably Vasiliev's classical theory, gauge-fixed;</span> <span data-covers="section-5.1-p2 section-5.3-p2">its quadratic part can be made local, with Vasiliev's $U(N)$ spectrum.</span></li>
  <li data-claims="c-loops"><span data-covers="section-6.3-p3 section-6.3-p4">Loops are computable: counter-terms are argued to cancel all divergences.</span></li>
  <li data-claims="c-finiteN"><span data-covers="sec-local_to_bilocal-p5 section-5.3-p4">In principle finite $N$ works: products of $N+1$ bulk fields obey constraints excluding even empty AdS.</span></li>
  <li data-claims="c-critical"><span data-covers="critUNbulk-p2 critUNbulk-p3">The critical model keeps the action; only the scalar's boundary condition changes.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="intro-p3 intro-p4">No sign of a topology sum appears; high-spin gravity presumably gains a quantum completion.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="intro-p4 intro-p5">Vasiliev's theory has no action. Bi-local holography, notably de Mello Koch–Jevicki–Suzuki–Yoon, proposes building the bulk from $G(x_1,x_2)=\frac1N\sum_I\phi_I^*(x_1)\phi_I(x_2)$.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-map"><span data-covers="sec-cft_to_ads-p1 sec-ads_to_cft-p3 sec-ads_to_cft-p4">Identifying conformal partial-wave coefficients of $G$'s fluctuation $\eta$, up to $f_{\Delta,J}$, with bulk-to-boundary coefficients of transverse traceless $\Phi_J$ gives an invertible map (modified for the $d<4$ scalar),</span> <span data-covers="sec-cft_to_ads-p10 sec-ads_to_cft-p8">finite if $f$ is a power times a phase at large $s$.</span></li>
  <li data-claims="c-action"><span data-covers="section-5.1-p2 section-5.3-p2 section-5.3-p3">If $f_{\Delta,J}f_{d-\Delta,J}=(-1)^J$ the quadratic action is $\Phi_J(\nabla^2-M^2_{d+J-2,J})(\nabla^2-M^2_{d+J,J})\Phi_J$, with Faddeev–Popov-like ghosts for $U(N)$, not $O(N)$;</span> <span data-covers="sec-bulk_theory-p1 section-5.3-p4">the non-local whole is presumably Vasiliev's, gauge-fixed.</span></li>
  <li data-claims="c-loops"><span data-covers="section-6.3-p3 section-6.3-p5">Counter-terms $\propto V\sim L^d/\varepsilon^d$ cancel the one-loop tadpole exactly; all loops are argued to cancel.</span></li>
  <li data-claims="c-finiteN"><span data-covers="sec-local_to_bilocal-p5 section-5.3-p4">In principle, at finite $N$ the rank bound on $G$ becomes constraints on products of $N+1$ bulk fields, excluding empty AdS.</span></li>
  <li data-claims="c-critical"><span data-covers="critUNbulk-p2 critUNbulk-p3">The critical model keeps the action, with $\Pi^{TT}_{d-2,0}\to\Pi^{TT}_{2,0}$ for the scalar.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="intro-p3 intro-p4">No sign of a topology sum, only fields on fixed AdS; high-spin gravity presumably gains an off-shell quantum completion.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="intro-p2 intro-p3">What bulk does a CFT define beyond $1/N$? Simplest case: $N$ free scalars, dual to all-spin fields.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-map"><span data-covers="sec-cft_to_ads-p1 sec-ads_to_cft-p3">Expanding the bi-local field $\phi^*(x_1)\phi(x_2)$ in conformal modes, matched to AdS modes, gives a path integral over all-spin AdS fields.</span></li>
  <li data-claims="c-action"><span data-covers="sec-bulk_theory-p1 section-5.3-p4">The non-local bulk action is presumably Vasiliev's high-spin gravity;</span> <span data-covers="section-5.1-p2 section-5.3-p2">for $U(N)$ its particles match, plus unphysical ghosts.</span></li>
  <li data-claims="c-loops"><span data-covers="section-6.3-p3 section-6.3-p4">Loops are computable: counter-terms are argued to cancel their divergences.</span></li>
  <li data-claims="c-finiteN"><span data-covers="sec-local_to_bilocal-p5 section-5.3-p4">In principle finite $N$ works too, with constraints that even empty AdS violates.</span></li>
  <li data-claims="c-critical"><span data-covers="critUNbulk-p2 critUNbulk-p3">The critical model keeps the action; only the scalar's boundary condition changes.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="intro-p3 intro-p4">No sign of a topology sum appears; high-spin gravity presumably gets a quantum theory.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="intro-p1 intro-p2">Holography defines the bulk through the CFT, but only within the $1/N$ expansion is it understood as fields around a classical solution; beyond it, even whether the bulk is a sum over configurations is open.</span> <span data-covers="intro-p3">The paper suggests answers in the simplest example: $N$ free scalars restricted to $U(N)$ or $O(N)$ singlets, dual to high-spin gravity.</span> <span data-covers="sec-cft_to_ads-p1 sec-ads_to_cft-p3">It rewrites their path integral, explicitly within the $1/N$ expansion, as one over fields of all integer spins on a fixed AdS space, through an invertible map.</span> <span data-covers="section-5.1-p2 section-5.3-p4">This gives an explicit, if non-local, action for high-spin gravity, which until now had only equations of motion, and it shows no sign of a sum over topologies.</span></p>
<p><span data-covers="sec-local_to_bilocal-p2 sec-local_to_bilocal-p5">All singlet information sits in the bi-local field $G(x_1,x_2)=\frac1N\sum_I\phi_I^*(x_1)\phi_I(x_2)$. On a lattice of $V$ points it is a non-negative matrix of rank at most $N$.</span> <span data-covers="section-2.1-p1 section-2.1-p3">For $N\ge V$ the rank bound is empty, and changing variables to $G$ only adds the Jacobian term $(N-V)\,\mathrm{Tr}\log G$, which is highly non-local.</span> <span data-covers="section-2.1-p4 sec-pert_bilocal-p3">The whole action is then of order $N$, so expanding $G$ around the free propagator gives Feynman rules in $1/N$, with counter-terms proportional to $V$.</span></p>
<p><span data-covers="sec-conformal_basis-p1 sec-conformal_basis-p3">The fluctuation of $G$ is then expanded in eigenmodes of the conformal group: three-point functions with an operator of spin $J$ and dimension $\Delta=\frac d2+is$ on the principal series.</span> <span data-covers="section-4.1-p3 sec-cft_to_ads-p1">Transverse traceless spin-$J$ fields on AdS, expanded in bulk-to-boundary propagators, carry the same labels. So the two sets of coefficients are identified, up to a factor $f_{\Delta,J}$ that conformal symmetry leaves free.</span> <span data-covers="sec-cft_to_ads-p10 sec-ads_to_cft-p8">The map and its inverse are linear integrals, finite as long as $f_{\Delta,J}$ grows at most like a power along the principal series.</span> <span data-covers="sec-single_trace_dual-p4 sec-single_trace_dual-p5">On-shell, the boundary limit of each spin-$J$ field gives the corresponding single-trace operator.</span></p>
<p><span data-covers="section-5.1-p1 section-5.1-p2">Substituted into the quadratic bi-local action, the map gives a non-local bulk kernel. For the choice $f_{\Delta,J}f_{d-\Delta,J}=(-1)^J$ it becomes local but has four derivatives, $\Phi_J(\nabla^2-M^2_{d+J-2,J})(\nabla^2-M^2_{d+J,J})\Phi_J$, where $M^2_{\Delta,J}=\Delta(\Delta-d)-J$.</span> <span data-covers="section-5.3-p1">Each spin therefore carries two particles: one of dimension $d-2+J$ with a positive propagator, massless for $J>0$, and one of dimension $d+J$ with a negative propagator.</span> <span data-covers="section-5.3-p2">For $U(N)$ the physical particles are exactly Vasiliev's, and the wrong-sign ones have the quantum numbers of the Faddeev–Popov ghosts that gauge-fixing Vasiliev's fields produces.</span> <span data-covers="section-5.3-p3">For $O(N)$ the ghosts come out with even spin where Vasiliev's would be odd, a mismatch the paper leaves open.</span> <span data-covers="section-5.3-p4">The paper claims its action as the off-shell definition of Vasiliev's theory in this gauge, perturbatively in $1/N$.</span></p>
<p><span data-covers="sec-bulk_theory-p1 section-6.2-p3">The higher terms map to bulk vertices, non-local for any $f$, with the bi-local theory's powers of $N$ and counter-terms.</span> <span data-covers="section-6.1-p3 section-6.3-p3">Two diagram identities, inherited from the conformal completeness relation, reduce a bulk loop to a tree diagram times a factor $V$, so the one-loop tadpole cancels its counter-term exactly.</span> <span data-covers="section-6.3-p4 section-6.3-p5">Every diagram reduces this way, so the bi-local cancellations should carry over; with radial and infrared cutoffs, divergences appear only through $V\propto L^d/\varepsilon^d$, and they cancel.</span></p>
<p><span data-covers="sec-smallmass-p1 sec-smallmass-p2">The formalism also maps deformations. A mass for the scalars acts only at the boundary of AdS. At leading order it turns on the bulk scalar alone, as a function of $mz$ that breaks the AdS isometries, $\langle\Phi_0\rangle\propto m^2z^2$ for small mass.</span> <span data-covers="sec-NDbasisCFT-p5 sec-finmass-p2">For a finite mass, a separate map for configurations that do not decay gives the profile numerically in $d=3$.</span> <span data-covers="critUN-p3 critUNbulk-p2">The quartic double-trace interaction flows, for $2<d<4$, to the critical model, where $\phi^*\phi$ is replaced by a field of dimension 2. In the bulk this changes only the scalar propagator, from $\Pi^{TT}_{d-2,0}$ to its shadow $\Pi^{TT}_{2,0}$, that is, the boundary condition.</span> <span data-covers="critUNbulk-p3">Since the change is free of short-distance singularities, the same action with this boundary condition gives the critical model at all orders in $1/N$.</span></p>
<p><span data-covers="sec-local_to_bilocal-p6 section-5.3-p4">At finite $N$ ($N<V$) the rank constraints are not known explicitly. In the bulk they constrain products of $N+1$ fields and exclude even empty AdS, so the finite-$N$ bulk theory is defined but not written down.</span> <span data-covers="section-2.3.3-p2 section-6.3-p4">Loop cancellation is shown at one loop and argued in general, without an all-orders proof.</span> <span data-covers="intro-p4 section-1.1-p3">Equivalence with Vasiliev's equations is expected, not shown, and whether the non-local action is local on scales much larger than the AdS radius is open.</span> <span data-covers="section-1.1-p2">The construction is for flat $\mathbb R^d$; on spaces with circles, where vector models have phase transitions, it is likely to need modification.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "sec-NDbasisCFT-p5", "note": r"The first line of (7.14) is written with the decaying part, $\nabla^2_1\eta_D\,\nabla^2_2\eta_D$, but the section computes the quadratic term of the non-decaying modes and the next line uses $d_\Delta$ only. Should it read $\eta_{ND}$?"},
    {"node": "sec-NDbasisCFT-p3", "note": r"The text says $\eta_{ND}$ is expanded in scalar two-point functions $|x_{12}|^{-2\Delta}$, but (7.11) expands it in $|x_{12}|^{2-\Delta}$, which is what integrating the three-point basis over $y$ gives for $2\Delta_0=d-2$. Is $|x_{12}|^{-2\Delta}$ meant only loosely? The layers say “powers of $|x_1-x_2|$”."},
    {"node": "sec-finmass-p2", "note": r"The pole term of (7.30) at $\Delta=1$ is proportional to $(mz)^{3-\Delta}=(mz)^2$, and it reproduces the small-mass result (7.5) exactly, $-f_{2,0}(mz)^2/(8\pi)$. If the integral term tends to a constant at large $mz$, as the text says, the profile should grow quadratically, yet the text says Figure 2 shows linear growth. Which is right? The layers state neither."},
    {"node": "section-2.1-p1", "note": r"“the Jacobian for the change of variables from $\Phi$ to $G$”: $\Phi$ elsewhere denotes the bulk fields; presumably $\phi_I$."},
    {"node": "sec-pert_bilocal-p3", "note": r"(2.11) writes the second term as $(N-V)\log(1+G_0^{-1}\eta/\sqrt N)$ without the trace that (2.8) and the expansion (2.12)-(2.13) carry; presumably ${\rm Tr}\log$."},
    {"node": "sec-massDef-p1", "note": r"“the deformation of the bulk theory by a finite scalar mass $m$”: the mass is given to the boundary scalars $\phi_I$ (as intro-p9 says), and its bulk image is a scalar profile, not a bulk mass. Presumably “the CFT”."},
    {"node": "section-5.3-p2", "note": r"Not an error, but easy to misread: the Faddeev–Popov ghost of the spin-$J$ field has spin $J-1$ and $M_{d+J-1,J-1}$, while the wrong-sign mode found at spin $J$ has $M_{d+J,J}$. They match as sets (the ghost of the spin-$(J+1)$ field), which is how the layers phrase it; a sentence saying so would help."},
]
