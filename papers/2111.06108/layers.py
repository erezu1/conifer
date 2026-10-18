"""The drafted layers of arXiv:2111.06108 (The onset of quantum chaos in disordered CFTs).

Drafted by an AI reader from the paper's text; nothing here has been checked by the authors yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2111.06108 · hep-th · November 2021"
DATE = "11 November 2021"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "The onset of quantum chaos in disordered CFTs"
# The equation is the continuity relation (2.37), lambda_L(J->0+) = lambda_L^0: one line, readable with the notation
# question, and it is what decides between the two kinds of onset. The figure is figure 11, the computed lambda_L(J) of
# cSYK, zero up to J_c and rising to 1: the headline result itself. Figure 1 (the two kinds of onset, schematic) was
# considered; it carries no computed result.
KEY = {"equation": "eq-continuity", "figure": "fig-GRchaos"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on SYK-like models, quantum chaos or conformal manifolds"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy or condensed-matter theorist; knows CFT and has heard of SYK and OTOCs"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory and the basics of conformal field theory"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction's "two main results"
# (section-1.1-p1) and its conjecture (section-1.1-p2).
# How they relate, from the paper's own words: theme A is the general large-N machinery (section 2); theme B is chaos
# on exactly marginal lines (sections 3-5). The paper links them itself: the chaos computation uses the OTOC's ladder
# structure for general disordered CFTs (section-2.5.1-p1, the link_quote of c-continuity; also section-1-p7, "they
# still allow us to study a new phenomenon"). Within B, the generalized free field result is computed on the cSYK line
# (sec-cSYK_chaos-p1), and the minimal-model result uses the weak-coupling analysis of section 2.5 (section-5.1-p4).
# Every theme is linked, so: one argument. The abstract's "We also derive" lists the equations as a further
# deliverable, so the gist states them in their own point, without claiming more of a link than "ladder structure".
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-marginal", "headline": True,
     "claim": r"In families of disordered CFTs the disorder coupling is exactly marginal: generalized free fields of dimension $1/q$ (cSYK at leading order in $1/N$, and a $1+1$d supersymmetric version) and $N$ coupled $\mathcal N=(2,2)$ minimal models, conformal for every realization; so $\lambda_L$ can be followed from weak to strong coupling.",
     "quote": "families of theories in which the disorder coupling is an exactly marginal deformation",
     "where": ["sec-cSYK-p1", "section-3.2.1-p8", "sec-GFF_limit_of_MM-p6"], "theme": "B"},
    {"id": "c-discontinuous", "headline": True,
     "claim": r"For disordered generalized free fields in $0+1$d and $1+1$d, $\lambda_L$ vanishes below a finite critical coupling $J_c$ and rises above it, to the maximal value at strong coupling: a discontinuous transition into chaos.",
     "quote": "including a discontinuous transition into chaos",
     "where": ["sec-cSYK_chaos-p3", "sec-cSYK_chaos-p4", "section-4.2-p4"], "theme": "B",
     "builds_on": "c-marginal", "link_quote": "We can now compute the chaos exponent in this theory as a function of"},
    {"id": "c-continuous",
     "claim": r"For the disordered $\mathcal N=(2,2)$ $A_2$ minimal model, at leading order in $J$, $\lambda_L(J\to0^+)=0$, so the transition into chaos is continuous, assuming $\lambda_L$ grows with $J$.",
     "quote": "We find that there is a smooth transition into chaos in this case",
     "where": ["section-5.1-p4", "section-5.1-p8"], "theme": "B",
     "builds_on": "c-continuity", "link_quote": r"the value of $\lambda_L$ close to $J=0$ is found by looking for values of"},
    {"id": "c-continuity",
     "claim": r"A conjectured continuity relation, argued in general and verified in both examples: the chaos exponent from the retarded kernel as $J\to0^+$ equals the late-time exponent $\lambda_L^0$ of one core CFT, so one copy would decide whether the onset is continuous.",
     "quote": "we conjecture a continuity relation",
     "where": ["sec-chaos_J0-p6", "section-2.5.3-p4", "sec-validity_1-p2"], "theme": "B",
     "builds_on": "c-equations", "link_quote": "since in addition we saw that the OTOC has a ladder structure even for general disordered CFTs"},
    {"id": "c-equations",
     "claim": r"For $N$ copies of any CFT deformed by disorder, at leading order in $1/N$, the two-point function obeys a generalized Schwinger–Dyson equation, and the four-point function and the double commutator obey ladder equations, all expandable in $J$ with finitely many core correlators per order.",
     "quote": "We also derive self-consistency equations for the two- and four-point functions",
     "where": ["sec-2_pt_SD-p3", "sec-four_pt-p2", "section-2.4-p5"], "theme": "A"},
]

# Every version states the three contributions the abstract claims (c-marginal, c-discontinuous, c-equations), and the
# continuous onset (claimed in the introduction) that the paper sets against the discontinuous one; the specialist's also
# states the continuity relation.
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p9">The chaos exponent $\lambda_L$ is known mostly at isolated points; how chaos grows with coupling is open.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-marginal"><span data-covers="sec-cSYK-p1 sec-GFF_limit_of_MM-p6">Disorder is exactly marginal among generalized free fields (in cSYK at leading order in $1/N$)</span> <span data-covers="section-3.2.1-p8">and, for every realization, among supersymmetric minimal models.</span></li>
  <li data-claims="c-discontinuous"><span data-covers="sec-cSYK_chaos-p3 section-4.2-p4">For generalized free fields the kernel allows no positive exponent below a finite $J_c$, so chaos is absent: a discontinuous transition.</span></li>
  <li data-claims="c-continuous"><span data-covers="section-5.1-p4 section-5.1-p8">For the simplest supersymmetric minimal model, chaos should grow from zero coupling.</span></li>
  <li data-claims="c-equations"><span data-covers="sec-2_pt_SD-p3 sec-four_pt-p2 section-2.4-p5">Large-$N$ self-consistency equations give any disordered CFT's two- and four-point functions; OTOCs keep a ladder structure.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p10 section-1-p12">The threshold loosely parallels the classical KAM theorem, though the analogy is far from precise.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p3 section-1-p9">Disorder makes SYK-like models solvable at large $N$, but $\lambda_L$ is known mostly at isolated conformal points.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-marginal"><span data-covers="sec-cSYK-p1 sec-GFF_limit_of_MM-p6">Disorder is exactly marginal for generalized free fields of dimension $1/q$ (cSYK, at leading order in $1/N$)</span> <span data-covers="section-3.2.1-p7 section-3.2.1-p8">and, per realization, among $\mathcal N=2$ $A_{q-1}$ minimal models.</span></li>
  <li data-claims="c-discontinuous"><span data-covers="sec-cSYK_chaos-p4 section-4.2-p4 sec-chaos_summary-p3">For generalized free fields, in $0+1$d and supersymmetric in $1+1$d, the largest root of $k_R=1$ is negative below a finite $J_c$ ($-2\Delta$ at $J=0$ in $0+1$d): no chaos, a discontinuous onset.</span></li>
  <li data-claims="c-continuous"><span data-covers="sec-q3_Case-p2 section-5.1-p4 section-5.1-p8">For the $A_2$ model ($c=1$), $\lambda_L(J\to0^+)=0$: the onset should be continuous.</span></li>
  <li data-claims="c-continuity"><span data-covers="sec-chaos_J0-p6 sec-validity_1-p2 sec-validity_2-p2">A conjectured continuity relation, $\lambda_L(J\to0^+)=\lambda_L^0$ with $\lambda_L^0$ one copy's late-time exponent, is argued and checked in the paper's examples.</span></li>
  <li data-claims="c-equations"><span data-covers="sec-2_pt_SD-p3 sec-2_pt_SD-p4">For any core CFT the $G$–$\Sigma$ saddle gives a Schwinger–Dyson equation of subtracted correlators,</span> <span data-covers="sec-four_pt-p2 section-2.4-p5">and ladders for four-point functions and OTOCs.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p10 section-1-p12">The threshold loosely parallels the KAM theorem, though the analogy is far from precise.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p8 section-1-p9">The chaos exponent $\lambda_L$ measures quantum chaos; it is known mostly for isolated theories.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-marginal"><span data-covers="sec-cSYK-p1 section-3.2.1-p8 sec-GFF_limit_of_MM-p6">Random couplings among many copies of some conformal theories keep them conformal at any strength (for some, only at large $N$), so $\lambda_L$ can be tracked.</span></li>
  <li data-claims="c-discontinuous"><span data-covers="sec-cSYK_chaos-p3 section-4.2-p4">For generalized free fields chaos appears only above a finite coupling: a discontinuous transition.</span></li>
  <li data-claims="c-continuous"><span data-covers="section-5.1-p4 section-5.1-p8">For the simplest supersymmetric minimal model chaos should instead grow from zero coupling.</span></li>
  <li data-claims="c-equations"><span data-covers="sec-2_pt_SD-p3 sec-four_pt-p2 section-2.4-p5">For any disordered conformal theory, large-$N$ equations give its two- and four-point functions, as in the SYK model.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p10 section-1-p12">The threshold loosely resembles the KAM theorem, by which slightly deformed classical integrable systems stay largely regular.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="section-1-p8 section-1-p9">The chaos exponent $\lambda_L$ measures how fast out-of-time-order correlators grow, and is bounded by $2\pi/\beta$. Computing it usually needs scale invariance, so it is known mostly at isolated conformal points, and little is known about how chaos grows as a theory moves away from weak coupling.</span> <span data-covers="section-2.5.1-p1 sec-cSYK_chaos-p1">The paper couples $N$ copies of a conformal theory by random couplings that are exactly marginal, so every coupling strength $J$ is conformal and $\lambda_L(J)$ can be followed from $J=0$ upwards.</span> <span data-covers="sec-cSYK_chaos-p3 section-5.1-p8">For disordered generalized free fields chaos appears only above a finite coupling, which the paper calls a discontinuous transition. For a disordered supersymmetric minimal model it should appear continuously from $J=0$.</span> <span data-covers="section-1-p12">The first behaviour loosely parallels the KAM theorem of classical mechanics, though the analogy is far from precise.</span></p>
<p><span data-covers="sec-review_of_disordered_free_fields-p2 sec-review_of_disordered_free_fields-p5">In the SYK model, where the copies are free fermions, averaging over couplings makes the propagator obey a closed Schwinger–Dyson equation and the four-point function a sum of ladder diagrams.</span> <span data-covers="sec-2_pt_SD-p3 sec-2_pt_SD-p4">The paper shows that this survives for an interacting core CFT. Rewritten with bilocal fields $G$ and $\Sigma$, the theory sees the core CFT only through a generating functional of its correlators, and the large-$N$ saddle gives a generalized Schwinger–Dyson equation.</span> <span data-covers="sec-four_pt-p2 sec-four_pt-p4">Fluctuations about the saddle sum the four-point function as a ladder $F_0/(1-K)$, whose kernel is built from core correlators with their disconnected parts subtracted.</span> <span data-covers="sec-2_pt_SD-p6 sec-four_pt-p5">Exact solutions need every correlator of the core CFT, but each order in $J$ needs only finitely many.</span> <span data-covers="section-2.4-p5 section-2.5.1-p2">The double commutator obeys the same ladder with a retarded kernel, so $\lambda_L$ is the largest growth rate whose eigenvalue $k_R$ equals one.</span></p>
<p><span data-covers="sec-cSYK-p1 sec-cSYK-p2">In cSYK, Gross and Rosenhaus's model of generalized free fermions of dimension $1/q$, the coupling is exactly marginal at leading order in $1/N$, and the propagator is SYK's times a function of $J$.</span> <span data-covers="sec-2d_GFFs-p7 sec-2d_GFFs-p8">A $1+1$d supersymmetric version behaves alike.</span> <span data-covers="section-3.2.1-p7 section-3.2.1-p8">Among $N$ copies of the $\mathcal N=(2,2)$ $A_{q-1}$ minimal model, every random coupling of $q$ chiral fields is exactly marginal, because the copies have no continuous non-R global symmetry; so each realization is conformal.</span> <span data-covers="section-3.2.1-p3">The resulting conformal manifold has dimension about $N^q/q!$.</span> <span data-covers="sec-GFF_limit_of_MM-p5 sec-GFF_limit_of_MM-p6">With many flavours of minimal models, the theory reduces to the supersymmetric generalized free fields, which therefore have a conformal manifold even at finite $N$.</span></p>
<p><span data-covers="sec-chaos_J0-p2 sec-chaos_J0-p3">At $J=0$ the copies decouple, and the double commutator of one copy decays at late times with an exponent $\lambda_L^0$, expected to be non-positive. It describes the eventual decay, not chaos.</span> <span data-covers="sec-chaos_J0-p5 sec-chaos_J0-p6">Since the kernel's eigenvalue is of order $J^2$, a solution near $J=0$ sits where its integral diverges, which the paper argues happens from $\lambda=\lambda_L^0$ down.</span> <span data-covers="section-2.5.3-p3 section-2.5.3-p4">A toy model gives a double pole there and $\lambda_L=\lambda_L^0+O(J)$, so the paper conjectures the continuity relation $\lambda_L(J\to0^+)=\lambda_L^0$.</span> <span data-covers="sec-chaos_summary-p3">A negative root of $k_R=1$ means no exponentially growing solution, so the paper reads it as no chaos. A negative $\lambda_L^0$ thus predicts chaos only above a finite coupling, and a vanishing one an onset from zero.</span></p>
<p><span data-covers="sec-cSYK_chaos-p2 sec-cSYK_chaos-p3">For cSYK the retarded kernel is SYK's rescaled, so $\lambda_L(J)$ is found at every $J$. It reaches the maximal value 1 at strong coupling, but below a critical $J_c$ the root is negative, tending to $-2\Delta$.</span> <span data-covers="sec-cSYK_chaos-p4 section-4.2-p4">So for every finite $q$, and in the $1+1$d version for every $\Delta>0$, there is no chaos below $J_c$.</span> <span data-covers="section-5.1-p4 section-5.1-p8">For the $A_2$ minimal model, a $c=1$ compact boson whose correlators are all known, the integrals diverge only for $\lambda\le0$ at every order. So $\lambda_L(J\to0^+)=0$, and the onset should be continuous.</span> <span data-covers="sec-validity_1-p2 sec-validity_2-p2">Computed directly, $\lambda_L^0$ is $-2\Delta$ and 0 in the two families, so the continuity relation holds in both.</span></p>
<p><span data-covers="sec-chaos_J0-p6 sec-conclusions-p4">The continuity relation is argued, not proved: where the integrals diverge is expected rather than shown in general.</span> <span data-covers="section-5.1-p5 section-5.1-p7">For the minimal model only $q=3$ and the leading order in $J$ are computed; that $\lambda_L$ then grows with $J$ is assumed, and the higher-order argument skips the Euclidean integrals.</span> <span data-covers="section-5.1-p2 sec-cSYK-p1">The bosonic part of the kernel is assumed to dominate, and cSYK's marginality is established only at leading order in $1/N$.</span> <span data-covers="sec-conclusions-p4 sec-conclusions-p5">If continuity holds generally, one copy of a core CFT decides the kind of onset. The paper then expects non-supersymmetric minimal models and the $2+1$d Ising model to enter chaos discontinuously, if suitable conformal manifolds exist.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "section-1.1-p1", "note": r"“Discontinuous transition into chaos” for the generalized free fields: in figures 1b, 11a and 12a, $\max(0,\lambda_L)$ is continuous at $J_c$, with a kink. Is “discontinuous” meant for the onset needing a finite coupling (the KAM-like reading), or for $d\lambda_L/dJ$ at $J_c$? The layers describe it as “no chaos below a finite coupling” and call it discontinuous only as the paper's name."},
    {"node": "sec-chaos_summary-p3", "note": r"For $\lambda_L^0=0$ this paragraph expects $\lambda_L(J)\sim J^2+O(J^4)$, while the toy model (section-2.5.3-p3, p4), with a double pole $k_R\sim J^2/(\lambda-\lambda_L^0)^2$, gives $\lambda_L=\lambda_L^0+O(J)$, linear in $J$. Which is meant? The layers give only $\lambda_L^0+O(J)$ and no scaling for the continuous case."},
    {"node": "section-2.5.3-p4", "note": r"(2.45) has $(\lambda-\lambda_L)^2$ in the denominator; from (2.44) and the text it should presumably be $(\lambda-\lambda_L^0)^2$. Also (2.43) writes $|z_4-1|^{-\lambda_0}$ for $\lambda_L^0$."},
    {"node": "section-4.2-p2", "note": r"(4.2) rescales the retarded kernel by $b(J)/b(J=\infty)$, while (3.17) for the same model, and (3.8) and (4.1) for cSYK, have the $q$-th power $(b(J)/b(\infty))^q$. Is the power missing in (4.2)? The layers say only “rescaled”."},
    {"node": "sec-chaos_J0-p3", "note": r"Here $\lambda_L^0\le0$ is “expected”; sec-chaos_summary-p3 says it is “always non-positive … from unitarity”. The layers keep the weaker “expected to be non-positive”."},
    {"node": "sec-validity_1-p1", "note": r"“at large $t_3,t_4$ … $F_0\propto e^{\Delta(t_3+t_4)}$”: this decays only as $t_3,t_4\to-\infty$ (points 3, 4 in the far past of 1, 2), which is what gives $\lambda_L^0=-2\Delta$; “large” presumably means large and negative, or large separation $t_1-t_3$."},
    {"node": "sec-GFF_limit_of_MM-p6", "note": r"“find its two- and four-point functions using the results of 3.2”: the generalized free field results are in 3.1.2 (sec-2d_GFFs); 3.2 is the minimal models. A wrong cross-reference?"},
    {"node": "fig-nsp", "note": r"The caption of figure 15, “Decomposing the six-point function”, repeats that of figure 14; the text (app-nsprime-p1) says figure 15 inserts the decomposed four-point function into the kernel."},
    {"node": "sec-2_pt_SD-p5", "note": r"“plugged into the diagrams in figure B”: a broken figure reference, presumably figure 6 (or the appendix B figures)."},
    {"node": "sec-cSYK_chaos-p3", "note": r"Refers to “section 2.5.4” and “section 2.5.2”; the subsections of 2.5 are unnumbered in the converted text (Generalities, Chaos at $J\to0^+$, A toy model, Summary). The layers read 2.5.4 as the Summary (sec-chaos_summary)."},
]
