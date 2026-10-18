"""The drafted layers of arXiv:2207.11980 (Onset of Quantum Chaos in Random Field Theories).

Drafted by an AI reader from the paper's text; nothing here has been checked by the authors yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs. <span data-covers="..."> marks what a sentence of a summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, figure and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2207.11980 · hep-th · July 2022"
DATE = "25 July 2022"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "Onset of quantum chaos"
# The headline (a discontinuous onset of chaos in disordered generalized free fields) is not a formula, so the equation
# is that of the key mechanism: (13), the conjectured equality that lets one core CFT decide the type of onset. The
# unlabelled (3), lambda_L = max(0, lambda_ker), would be the other choice but has no label. The figure is figure 4, the
# computed lambda_L(J) of the generalized free fields, which shows the discontinuous onset itself; figure 1 is its sketch.
KEY = {"equation": "eq-continuity", "figure": "fig-GFFchaos"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on SYK-like models, quantum chaos or disorder-averaged CFTs"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows CFT and large N, has heard of SYK and out-of-time-order correlators"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory and a first course on conformal field theory"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (introduction-p4 to p8).
# How they relate, from the paper's own words: the general equations (c-kernel) give the retarded kernel that exact
# marginality makes perturbative in J (c-marginal, "Importantly, if J is exactly marginal ..."); its expansion decides
# the type of onset and is conjectured to equal a core-CFT exponent (c-onset, "The expansion in J can also be used ...");
# the two examples are announced as "one example for each type of transition into chaos" of that criterion. Each step
# builds on the one before in the paper's words: one argument, one theme.
# c-onset and c-minimal are claimed only in the introduction: they are in the summary, and c-minimal also in the gist,
# where it fits, because the abstract's "interesting behaviors" are the two kinds of onset.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-kernel",
     "claim": r"At leading order in $1/N$ the averaged two- and four-point functions of any disordered CFT obey self-consistency equations generalizing those of SYK, with a ladder (kernel) structure that carries over, as a retarded kernel, to the double commutator and yields a putative chaos exponent $\lambda_L^{\text{ker}}$.",
     "quote": "We first derive self-consistency equations for the two- and four-point functions",
     "where": ["the-kernel-structure-of-the-four-point-function-p1", "the-kernel-structure-of-the-four-point-function-p3", "the-double-commutator-and-chaos-p2"],
     "theme": "A"},
    {"id": "c-marginal",
     "claim": r"When the disorder is exactly marginal the theory is conformal at every $J$, and the retarded kernel's eigenvalue can be computed order by order in $J$ from finitely many core-CFT correlators, so $\lambda_L$ can be followed from weak to strong coupling.",
     "quote": "in which the disorder coupling is an exactly marginal deformation",
     "where": ["the-double-commutator-and-chaos-p4", "the-kernel-structure-of-the-four-point-function-p4"],
     "theme": "A", "builds_on": "c-kernel",
     "link_quote": r"Importantly, if $J$ is exactly marginal, $k_R(\lambda_L)$ can be found perturbatively in $J$"},
    {"id": "c-onset",
     "claim": r"Since $\lambda_L=\max(0,\lambda_L^{\text{ker}})$, the onset of chaos is continuous or discontinuous according to the sign of $\lambda_L^{\text{ker}}$ as $J\to0^+$; the paper conjectures, and argues under reasonable assumptions in a companion paper, that this limit equals $\lambda_L^0$, a late-time exponent of a single core CFT.",
     "quote": "what a single core CFT should obey in order for the transition into chaos to be discontinuous",
     "where": ["the-double-commutator-and-chaos-p5", "the-double-commutator-and-chaos-p7"],
     "theme": "A", "builds_on": "c-marginal",
     "link_quote": "The expansion in $J$ can also be used to determine whether the transition into chaos would be continuous or discontinuous"},
    {"id": "c-gff", "headline": True,
     "claim": r"Disordered generalized free fields, the 1d cSYK model and its 2d $\mathcal N=2$ version, have $\lambda_L^{\text{ker}}\to-2\Delta$ at weak coupling, so there is no chaos below a finite coupling: a discontinuous transition into chaos, which the paper compares with classical KAM theory.",
     "quote": "including a discontinuous transition into chaos, mimicking classical KAM theory",
     "where": ["disordered-generalized-free-fields-p5", "disordered-generalized-free-fields-p6"],
     "theme": "A", "builds_on": "c-onset",
     "link_quote": "Below we give one example for each type of transition into chaos"},
    {"id": "c-minimal",
     "claim": r"In the disordered $\mathcal N=2$ $A_2$ minimal model $\lambda_L^{\text{ker}}$ tends to zero at weak coupling, so a continuous transition into chaos is expected; there, as for the generalized free fields, $\lambda_L^{\text{ker}}(0^+)=\lambda_L^0$, as conjectured.",
     "quote": "a continuous transition in the latter",
     "where": ["disordered-minimal-models-p2"],
     "theme": "A", "builds_on": "c-onset",
     "link_quote": "Below we give one example for each type of transition into chaos"},
]

# Every version states the three contributions the abstract claims (c-kernel, c-marginal, c-gff), and c-minimal, the
# other "interesting behavior"; c-onset, claimed only in the introduction, is in the specialist gist and the summary.
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="introduction-p1 introduction-p5">SYK-like disorder gives the chaos exponent $\lambda_L$, usually only at infinite coupling. How does chaos start?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-kernel"><span data-covers="the-kernel-structure-of-the-four-point-function-p1 the-kernel-structure-of-the-four-point-function-p3 the-double-commutator-and-chaos-p2">Randomly coupled copies of any CFT obey SYK-like large-$N$ equations; their ladder kernel gives a putative exponent.</span></li>
  <li data-claims="c-marginal"><span data-covers="the-double-commutator-and-chaos-p3 the-double-commutator-and-chaos-p4">Exactly marginal disorder keeps the theory conformal at every coupling, so $\lambda_L$ can be followed from weak to strong.</span></li>
  <li data-claims="c-gff"><span data-covers="disordered-generalized-free-fields-p5 disordered-generalized-free-fields-p6">Disordered generalized free fields have weak-coupling putative exponent $-2\Delta<0$: a discontinuous onset, at finite coupling.</span></li>
  <li data-claims="c-minimal"><span data-covers="disordered-minimal-models-p2">A disordered supersymmetric minimal model's putative exponent tends to zero at small coupling: a continuous onset is expected.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="introduction-p7">The paper calls the discontinuous transition into chaos surprising, comparing it with classical KAM theory.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="introduction-p1 introduction-p5">Relevant SYK-like disorder gives $\lambda_L$ only in the IR, at infinite coupling. How does chaos set in?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-kernel"><span data-covers="the-kernel-structure-of-the-four-point-function-p1 the-kernel-structure-of-the-four-point-function-p3 the-double-commutator-and-chaos-p2">Copies of any CFT with random $q$-body couplings obey large-$N$ Schwinger–Dyson and ladder equations; the retarded kernel $K_R$ gives $\lambda_L^{\text{ker}}$.</span></li>
  <li data-claims="c-marginal"><span data-covers="the-double-commutator-and-chaos-p4 the-kernel-structure-of-the-four-point-function-p4">For exactly marginal disorder the eigenvalues of $K_R$ are series in $J^2$, each order needing finitely many core correlators.</span></li>
  <li data-claims="c-onset"><span data-covers="the-double-commutator-and-chaos-p3 the-double-commutator-and-chaos-p5">With $\lambda_L=\max(0,\lambda_L^{\text{ker}})$, the sign of $\lambda_L^{\text{ker}}(0^+)$ sets a continuous or discontinuous onset;</span> <span data-covers="the-double-commutator-and-chaos-p7">the paper claims $\lambda_L^{\text{ker}}(0^+)=\lambda_L^0$, one core CFT's late-time exponent, shown under reasonable assumptions in a companion paper.</span></li>
  <li data-claims="c-gff"><span data-covers="disordered-generalized-free-fields-p5 disordered-generalized-free-fields-p6">Disordered generalized free fields, 1d and 2d supersymmetric, have $\lambda_L^{\text{ker}}\to-2\Delta$: a discontinuous onset, and SYK values at large $J$.</span></li>
  <li data-claims="c-minimal"><span data-covers="disordered-minimal-models-p2">The disordered supersymmetric $A_2$ minimal model ($c=1$ bosons) has $\lambda_L^{\text{ker}}\to0$: a continuous onset is expected. Both obey the claimed equality.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="introduction-p7">The paper calls the discontinuous transition into chaos surprising, comparing it with classical chaos, above all the KAM theorem.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="introduction-p1 introduction-p5">SYK-like random couplings usually give quantum chaos's growth rate $\lambda_L$ only at infinite coupling. How does it begin?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-kernel"><span data-covers="the-kernel-structure-of-the-four-point-function-p1 the-kernel-structure-of-the-four-point-function-p3 the-double-commutator-and-chaos-p2">Randomly coupled copies of any conformal theory obey SYK-like equations; a ladder kernel gives a putative exponent.</span></li>
  <li data-claims="c-marginal"><span data-covers="the-double-commutator-and-chaos-p3 the-double-commutator-and-chaos-p4">If the coupling never runs (exactly marginal), the theory stays conformal, so $\lambda_L$ can be followed from weak to strong.</span></li>
  <li data-claims="c-gff"><span data-covers="disordered-generalized-free-fields-p5 disordered-generalized-free-fields-p6">Disordered generalized free fields have a negative putative exponent at weak coupling: a discontinuous onset, at finite coupling.</span></li>
  <li data-claims="c-minimal"><span data-covers="disordered-minimal-models-p2">A disordered supersymmetric minimal model's exponent tends to zero at small coupling: chaos should start continuously.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="introduction-p7">The paper calls the discontinuous transition into chaos surprising, comparing it with classical KAM theory.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="introduction-p1">The chaos exponent $\lambda_L$ is the growth rate of a thermal double commutator, a quantum Lyapunov exponent. Averaging over random couplings, as in the SYK model, makes it computable at large $N$.</span> <span data-covers="introduction-p5">But such disorder is usually relevant, so $\lambda_L$ is found only in the infrared, at effectively infinite coupling.</span> <span data-covers="introduction-p3 introduction-p5">The paper couples $N$ copies of a core CFT by random, exactly marginal interactions of strength $J$, and follows $\lambda_L$ from weak to strong coupling.</span> <span data-covers="disordered-generalized-free-fields-p5 disordered-minimal-models-p2">Chaos then sets in either at once or only at a finite coupling: disordered generalized free fields show the second, a disordered minimal model the first.</span> <span data-covers="introduction-p7">The paper compares the delayed onset with classical chaos, above all the KAM theorem.</span></p>
<p><span data-covers="the-kernel-structure-of-the-four-point-function-p1 the-kernel-structure-of-the-four-point-function-p2">At leading order in $1/N$ the averaged two-point function obeys a Schwinger–Dyson equation like SYK's, but every correlator of the core CFT enters it, through theory-independent “subtracted” combinations.</span> <span data-covers="the-kernel-structure-of-the-four-point-function-p3">The four-point function is still a sum of ladders built from one kernel.</span> <span data-covers="the-double-commutator-and-chaos-p2 the-double-commutator-and-chaos-p3">So is the double commutator, with a retarded kernel. The largest $\lambda$ at which that kernel has eigenvalue one, $\lambda_L^{\text{ker}}$, is the chaos exponent when positive; otherwise there is no chaos, and $\lambda_L=\max(0,\lambda_L^{\text{ker}})$.</span></p>
<p><span data-covers="introduction-p5 the-double-commutator-and-chaos-p4">With exactly marginal disorder every realization is conformal, and the kernel's eigenvalue is a series in $J$, each order needing finitely many core correlators.</span> <span data-covers="the-double-commutator-and-chaos-p5">The leading order fixes $\lambda_L^{\text{ker}}(0^+)$, and its sign decides the onset: continuous if positive, discontinuous if negative.</span> <span data-covers="the-double-commutator-and-chaos-p6 the-double-commutator-and-chaos-p7">The paper conjectures $\lambda_L^{\text{ker}}(0^+)=\lambda_L^0$, the late-time exponent of the double commutator of one decoupled core CFT, never positive in unitary 2d theories. A single core CFT would then decide how chaos sets in.</span></p>
<p><span data-covers="disordered-generalized-free-fields-p2 disordered-generalized-free-fields-p3">In 1d the cSYK model couples generalized free fermions of dimension $\Delta=1/q$, and its kernel is known in closed form.</span> <span data-covers="disordered-generalized-free-fields-p5">The putative exponent rises to the maximal value 1 at strong coupling but tends to $-2\Delta$ at weak coupling. So there is no chaos below a finite coupling, and $\lambda_L^0=-2\Delta$ agrees with the conjecture.</span> <span data-covers="disordered-generalized-free-fields-p6">The 2d supersymmetric version, conformal even at finite $N$, behaves the same way.</span> <span data-covers="disordered-minimal-models-p1 disordered-minimal-models-p2">Copies of the supersymmetric $A_2$ minimal model, each a $c=1$ boson, are exactly marginally coupled. Their leading kernel gives an exponent tending to zero, so a continuous onset is expected, again with $\lambda_L^0$ matching.</span></p>
<p><span data-covers="the-double-commutator-and-chaos-p7">The equality of $\lambda_L^{\text{ker}}(0^+)$ and $\lambda_L^0$ is conjectured, argued in a companion paper under reasonable assumptions, and checked only in these examples.</span> <span data-covers="disordered-minimal-models-p2">For the minimal model only the leading weak-coupling kernel is computed, for $q=3$.</span> <span data-covers="footnotes">The classification assumes $\lambda_L$ grows monotonically with $J$, which the paper calls reasonable but not guaranteed.</span> <span data-covers="introduction-p7">The comparison with the KAM theorem stays a comparison: no quantum analogue of it is proved.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "introduction-p6", "note": r"With $\lambda_L=\max(0,\lambda_L^{\text{ker}})$ and a continuous $\lambda_L^{\text{ker}}(J)$, $\lambda_L$ itself is continuous in $J$; in the “discontinuous” case it has a kink at the finite coupling where $\lambda_L^{\text{ker}}$ crosses zero. Is “discontinuous” meant for this onset at finite coupling (as the layers describe it), rather than a jump in $\lambda_L$?"},
    {"node": "disordered-minimal-models-p2", "note": r"$\lambda_L^{\text{ker}}(0^+)=0$ is the borderline case: the-double-commutator-and-chaos-p5 classifies only a positive (continuous) or negative (discontinuous) limit, while introduction-p6 counts “non-negative” as continuous. Whether $\lambda_L^{\text{ker}}$ is positive just above $J=0$ seems to depend on the next order. Is a continuous onset expected for that reason? The layers say “expected”."},
    {"node": "the-double-commutator-and-chaos-p7", "note": r"The status of (13) varies: “it can be shown” (under reasonable assumptions, in the companion paper), “we claim”, and “our conjecture (13)”. The layers call it a conjecture argued under reasonable assumptions; is that the intended status?"},
    {"node": "disordered-generalized-free-fields-p1", "note": r"“our first class of examples with exactly marginal chaos”: presumably “exactly marginal disorder”."},
    {"node": "disordered-generalized-free-fields-p2", "note": r"(15) sums over $i=1,\dots,n$ while the variance below it, and (1)-(2), use $N$; and $S_\text{SYK}$ sums over all index values with $1/q!$, whereas (1) sums over distinct indices. Are the normalisations the same as in (2)?"},
    {"node": "the-double-commutator-and-chaos-p4", "note": r"(10)-(11) are written with $d^2x_3d^2x_4$ and a cylinder two-point function depending on $t$ and $x$, i.e. for a 2d core CFT, although the section is general and the first example is 1d. Is (10) meant for 2d, with the 1d form analogous?"},
    {"node": "the-double-commutator-and-chaos-p6", "note": r"$\lambda_L^0\le0$ is stated “for unitary theories in $2d$”, citing Caron-Huot (2017), whose argument is not specific to two dimensions as far as the drafter knows. Is the restriction to 2d intended? The layers keep “unitary 2d theories”."},
]
