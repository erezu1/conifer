"""The drafted layers of arXiv:2109.05512 (AdS from CFT for scalar QED).

Drafted by an AI reader from the paper's text; nothing here has been checked by the authors yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2109.05512 · hep-th · September 2021"
DATE = "12 September 2021"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the authors.")
PAGE_TITLE = "AdS from CFT for scalar QED"
# The equation is (4.8): the boundary conditions of the bulk vector for the free theory, QED and QED_3 with a
# Chern-Simons term, which is the headline in one line. No figure carries the result (the three figures are bubble
# chains and the contour of the conformal expansion), so none is named.
KEY = {"equation": "boundF"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on higher-spin holography, vector models or bi-local holography"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows AdS/CFT and large-N field theory in outline"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory and the basics of AdS/CFT"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (intro-p3, intro-p5, intro-p6).
# How they relate, from the paper's own words: the off-shell map of local operators (sec 3.2, theme A) is what
# "allows us to write down a simple action" for QED (theme B, sec 4); the Chern-Simons term is "translated into a
# modified boundary condition for the bulk vector field" of that construction (B); QCD is "As with QED" (sec 5, C);
# the critical vector model for d>4 follows "because we generalized the off-shell map" (sec 4, D). Every theme
# builds on another: one argument.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-qed", "headline": True,
     "claim": r"The $SU(N)$-singlet sector of scalar QED in $2<d<4$ has an explicit, non-local bulk dual in AdS with couplings of order $1/N$: the boundary photon becomes the boundary value of the bulk vector $\Phi_1$, so the low-energy ($\mathbb{CP}^{N-1}$) dual is the free-scalar dual with alternate boundary conditions for $\Phi_0$ and $\Phi_1$, argued to reproduce the theory to all orders in $1/N$.",
     "quote": "We construct an explicit bulk dual in anti-de Sitter space",
     "where": ["sec-action-p3", "sec-action-p4", "sec-correlations-p4"], "theme": "B",
     "builds_on": "c-offshell", "link_quote": "This allows us to write down a simple action for the"},
    {"id": "c-cs",
     "claim": r"In $d=3$ a Chern–Simons term at level $k$ (with $k/N$ fixed) turns the bulk vector's boundary condition into a mixed one, a family labelled by $k$; for $k\neq0$ the singlet sector so defined contains no monopole operators.",
     "quote": "we discuss also the addition of a Chern-Simons term for",
     "where": ["sec-action-p4", "sec-correlations-p3", "restrict-p3"], "theme": "B",
     "builds_on": "c-qed", "link_quote": "this coupling is translated into a modified boundary condition for the bulk vector field"},
    {"id": "c-qcd",
     "claim": r"For $U(N_c)$ scalar QCD with $N$ fundamental scalars at large $N$ and fixed $N_c$, the bulk fields become $U(N_c)$ adjoints and the dual is again the free dual with a changed boundary condition for the spin-one field.",
     "quote": "We also discuss the generalization to QCD",
     "where": ["sec-QCD_bulk-p2", "sec-QCD_bulk-p3"], "theme": "C",
     "builds_on": "c-qed", "link_quote": "As with QED, the resulting bulk theory is related to the bulk dual of the free theory by a simple change of boundary conditions"},
    {"id": "c-offshell",
     "claim": r"Local single-trace operators of every spin $J$, in every dimension $d>2$, map off-shell to the rescaled boundary limit of the bulk field $\Phi_J$, generalising the $J=0$, $d<4$ case of the earlier work.",
     "quote": "In this paper we show that the same is true also for",
     "where": ["sec-newmap-p4"], "theme": "A"},
    {"id": "c-critical",
     "claim": r"The off-shell map gives the bulk dual of the critical $U(N)$ or $O(N)$ vector model also for $4<d<6$; to all orders in $1/N$ it differs from the free dual only by the bulk scalar's boundary condition.",
     "quote": "our off-shell mapping allows us to construct the bulk dual for the critical",
     "where": ["sec-action-p2", "sec-correlations-p2"], "theme": "D",
     "builds_on": "c-offshell", "link_quote": "because we generalized the off-shell map"},
]

# Every version states the three contributions the abstract claims (c-qed, c-cs, c-qcd); c-offshell and c-critical,
# claimed only in the introduction, are in the summary, and in the specialist gist, which has room for them.
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="intro-p2 intro-p3">The authors had rewritten free scalars' singlet sector as gravity in AdS, deriving AdS/CFT there. Can a gauge field be added?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-qed"><span data-covers="sec-action-p3 sec-action-p4">For scalar QED in $2<d<4$ the photon becomes a bulk vector's boundary value;</span> <span data-covers="sec-action-p1 sec-correlations-p4">the explicit low-energy dual, non-local with $1/N$ couplings, is the free one with new boundary conditions.</span></li>
  <li data-claims="c-cs"><span data-covers="sec-action-p4">In three dimensions a Chern–Simons term makes the boundary condition mixed;</span> <span data-covers="restrict-p3">then no dressed monopole is gauge invariant, so monopole operators are excluded.</span></li>
  <li data-claims="c-qcd"><span data-covers="sec-QCD_bulk-p2 sec-QCD_bulk-p3">Scalar QCD with fixed colour number gets a very similar, adjoint-valued dual.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="intro-p2 intro-p3">It extends an explicit derivation of AdS/CFT beyond free fields;</span> <span data-covers="intro-p4">at zero Chern–Simons level, bulk solutions might describe monopoles.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="intro-p2 intro-p3">The authors' bi-local map rewrote singlet free scalars as an explicit non-local AdS theory, believed to be gauge-fixed Vasiliev gravity. Gauging needs local operators mapped off-shell.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-qed"><span data-covers="sec-action-p3 sec-action-p4">For scalar QED in $2<d<4$ at $e\to\infty$, the photon is $\Phi_1$'s boundary value: magnetic $\mathcal F_{zi}=0$ replaces the free electric $\mathcal F_{ij}=0$.</span> <span data-covers="sec-correlations-p4">With $\Phi_0$'s shadow condition this is the $\mathbb{CP}^{N-1}$ dual, argued to all orders in $1/N$.</span></li>
  <li data-claims="c-cs"><span data-covers="sec-action-p4 sec-correlations-p3">In $d=3$ a Chern–Simons level $k\propto N$ makes the condition mixed, labelled by $\kappa$;</span> <span data-covers="restrict-p3">for $k\neq0$ no dressed monopole is gauge invariant, so none are included.</span></li>
  <li data-claims="c-qcd"><span data-covers="sec-QCD_bulk-p2 sec-QCD_bulk-p3">$U(N_c)$ scalar QCD at fixed $N_c$: similar, with adjoint bulk fields.</span></li>
  <li data-claims="c-offshell"><span data-covers="sec-newmap-p4">The spin-$J$ single-trace operator $S^J$, any $J$ and $d>2$, equals off-shell $f_{d-2+J,J}^{-1}\lim\epsilon^{2-d}\Phi_J$, beyond the earlier $J=0$, $d<4$.</span></li>
  <li data-claims="c-critical"><span data-covers="sec-action-p2 sec-correlations-p2">The critical model's dual extends to $4<d<6$.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="intro-p2 intro-p3">It carries an explicit derivation of AdS/CFT from free scalars to an interacting gauge theory;</span> <span data-covers="intro-p4">for $k=0$, monopoles might be bulk solutions.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="intro-p1 intro-p2">AdS/CFT says some field theories are gravity in one more dimension; the authors had derived this for free scalars; can a gauge field be added?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-qed"><span data-covers="sec-action-p3 sec-action-p4">With many charged scalars, the photon becomes the boundary value of a vector field in AdS;</span> <span data-covers="sec-correlations-p4">at low energies only boundary conditions differ from the free case.</span></li>
  <li data-claims="c-cs"><span data-covers="sec-action-p4">In three dimensions a Chern–Simons term changes the vector's boundary condition again;</span> <span data-covers="restrict-p3">it also leaves no gauge-invariant monopole operators.</span></li>
  <li data-claims="c-qcd"><span data-covers="sec-QCD_bulk-p2 sec-QCD_bulk-p3">Scalar QCD with a fixed number of colours gets a very similar dual.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="intro-p2 intro-p3">It extends an explicit derivation of AdS/CFT beyond free fields;</span> <span data-covers="intro-p4">without a Chern–Simons term, it might also describe monopoles.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="intro-p1 intro-p2">AdS/CFT is taken to define quantum gravity in AdS through a CFT, but deriving it means rewriting a whole CFT, to all orders in $1/N$, as a gravitational theory.</span> <span data-covers="intro-p2">The authors had done this for the simplest case, the singlet sector of $N$ free complex scalars, dual to higher-spin gravity: through bi-local fields, an explicit non-local action on fixed AdS.</span> <span data-covers="intro-p3 sec-local_QED-p1">Here they gauge the scalars' $U(1)$, which gives scalar QED in $2<d<4$, and follow it to the CFT it reaches at low energies, the $\mathbb{CP}^{N-1}$ model.</span> <span data-covers="sec-action-p4 sec-correlations-p4">The answer is simple: the boundary photon becomes the boundary value of the bulk vector field, so the QED dual is the free dual with that field's boundary condition changed.</span></p>
<p><span data-covers="sec-action-p3 sec-newmap-p2">The difficulty is that gauging couples the photon to the current inside the path integral. The map from local operators to the bulk must then hold off-shell, as an operator identity, not only inside correlators.</span> <span data-covers="sec-review-p1 sec-review-p5">The map expands the bi-local and the bulk fields $\Phi_J$ of every spin $J$ in the same basis of conformal representations, and identifies the coefficients.</span> <span data-covers="sec-newmap-p3">The earlier work had an off-shell identity only for spin zero below four dimensions.</span> <span data-covers="sec-newmap-p4">The paper extends it to every spin and every $d>2$. A source for a spin-$J$ operator makes the bi-local singular as its points meet, at any $N$, and absorbing the singularity shifts the bulk field's boundary behaviour.</span> <span data-covers="sec-newmap-p4">Comparing with a bulk source term then gives $S^J(x)=f_{d-2+J,J}^{-1}\lim_{\epsilon\to0}\epsilon^{2-d}\Phi_J(x,\epsilon)$: each single-trace operator is a rescaled boundary limit of its bulk field.</span></p>
<p><span data-covers="sec-newmap-p2 sec-action-p3">For spin one that operator is the $U(1)$ current, so the photon's coupling becomes a coupling of a boundary field $A_i$ to the boundary limit of $\Phi_1$. Gauge-fixing and Chern–Simons terms do not involve the scalars and stay on the boundary.</span> <span data-covers="sec-action-p4">At infinite gauge coupling and without a Chern–Simons term, $A_i$ acts as a Lagrange multiplier: it sets the current to zero, and $\Phi_1$'s $z^0$ mode becomes dynamical, equal to $A_i$ up to normalisation.</span> <span data-covers="sec-action-p4">In terms of a boundary field strength, the free dual has electric boundary conditions, $\mathcal F_{ij}=0$, and QED magnetic ones, $\mathcal F_{zi}=0$.</span> <span data-covers="sec-correlations-p3">Correspondingly the vector's physical propagator is replaced by a shadow one, whose boundary condition also depends on the CFT's gauge-fixing parameter $\zeta$.</span> <span data-covers="sec-bilocal_QED-p2 sec-correlations-p4">After a field redefinition both $\sigma$ and the photon couple linearly, so the $\mathbb{CP}^{N-1}$ dual is the free dual with alternate boundary conditions for $\Phi_0$ and $\Phi_1$. The paper argues that this reproduces the model's correlators to all orders in $1/N$.</span></p>
<p><span data-covers="sec-local_QED-p1 sec-QED_bilocal-p1">In $d=3$ a Chern–Simons term for the photon can be added at level $k$, with $\kappa=k/N$ fixed at large $N$.</span> <span data-covers="sec-action-p4 sec-correlations-p3">It makes the boundary condition mixed, $\mathcal F_{ij}+\frac{2\pi i}{16\kappa}\varepsilon_{ijl}\mathcal F_{zl}=0$, so that the shadow propagator comes in an infinite family labelled by $k$.</span> <span data-covers="restrict-p2 restrict-p3">The singlet sector is defined rigorously by first gauging the scalars' $U(N)$ at infinite Chern–Simons level. For $k\neq0$ a monopole then carries $k$ units of gauge charge, and any dressing that cancels it is charged under that $U(N)$, so no monopole operators remain.</span></p>
<p><span data-covers="sec-action-p2">The off-shell map for spin zero, now valid above four dimensions, also gives the bulk dual of the critical $U(N)$ or $O(N)$ vector model wherever it exists at large $N$, for $2<d<6$.</span> <span data-covers="sec-action-p2 sec-correlations-p2">There the auxiliary field $\sigma$ removes the scalar's $z^{d-2}$ mode, so free and critical duals differ only in the bulk scalar's boundary condition, to all orders in $1/N$.</span> <span data-covers="sec-QCD_bulk-p2">For $U(N_c)$ scalar QCD with $N$ fundamental scalars at fixed $N_c$, bi-locals and bulk fields become $U(N_c)$ adjoints, and gauging adds self-interacting gauge fields and ghosts on the boundary.</span> <span data-covers="sec-QCD_bulk-p3">Again the dual is the free one with a changed boundary condition for the spin-one field.</span></p>
<p><span data-covers="sec-action-p1">The bulk dual is explicit but non-local: only its quadratic term can be made local, by a choice of normalisation.</span> <span data-covers="intro-p2">It is believed, not shown, to be a gauge-fixed form of Vasiliev's higher-spin gravity.</span> <span data-covers="sec-action-p4 sec-correlations-p3">The bulk vector has no gauge freedom of its own, and its propagator depends on how the CFT is gauge-fixed.</span> <span data-covers="sec-bilocal_QED-p1 sec-QCD_bulk-p3">The construction holds in the $1/N$ expansion, and not in the large-$N_c$ Chern–Simons-matter limit, which is expected to have a different dual.</span> <span data-covers="intro-p4 restrict-p3">Bulk solutions for monopole operators, which the formalism contains only without a Chern–Simons term, are left for future work.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "sec-action-p2", "note": r"“When $\lambda\to0$, this defines the bulk dual of the critical $U(N)$ theory”: the critical theory is $\lambda\to\infty$ in (2.4), (4.5) and (4.16), and only then does $\sigma$ act as a Lagrange multiplier. Is $\lambda\to\infty$ meant? The layers say the critical model."},
    {"node": "sec-correlations-p1", "note": r"“The particle with negative propagator and $\Delta=d+J-2$”: in (4.9) the negative term is $\Pi^{TT}_{d+J,J}$, and $\Delta=d+J-2$ is the physical one. Should it read $\Delta=d+J$?"},
    {"node": "sec-correlations-p3", "note": r"$\Pi^{\zeta,k}_{1,1}$ “satisfies the same differential equation (4.9)”: (4.9) is the free two-point function; the equation is (4.10). A slip?"},
    {"node": "sec-newmap-p4", "note": r"The bulk source term (3.34) is written with the bulk measure $d^dx\,dz/z^{d+1}$, but its integrand is a boundary limit and it is compared with (3.28), an integral over $d^dx$ only. Is $\int d^dx$ intended?"},
    {"node": "sec-action-p2", "note": r"After the critical deformation $\Phi_0$ “has the same small $z$ boundary condition as all other $J>0$ bulk fields, namely it scales as $z^{d/2}$”; sec-review-p6 gives the general fall-off as $z^{d/2-J}$. Is $z^{d/2}$ meant for the scalar only?"},
    {"node": "erez2-p1", "note": r"“the explicit momentum space photon 2-point function given in the first line of (2.15)”: (2.15) is in position space; the momentum-space propagator is (2.14). Which is meant? Also the last line of (B.17) is labelled $\Pi^\zeta_{d-1,1}$, presumably $\Pi^\zeta_{1,1}$."},
    {"node": "intro-p6", "note": r"“This CFT is not unitarity at finite $N$”: presumably “not unitary”."},
    {"node": "sec-newmap-p4", "note": r"(3.35) is stated “for all other $d>2$ and $J$”, while footnote 8 treats $d=4$ only as an expected analytic continuation. The layers say “every $d>2$” as the paper does; is $d=4$ covered by the argument of section 3.2?"},
]
