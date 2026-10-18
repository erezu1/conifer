"""The drafted layers of arXiv:1711.09491 (Delayed instabilities in viscoelastic solids through a metric description).

Drafted by an AI reader from the paper's text; nothing here has been checked by the author yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs. <span data-covers="..."> marks what a sentence of a summary stands for.

The paper is a letter with no section nodes: its run-in headings (Introduction, Linear viscoelastic continua, The
quasi static approximation, Metastable configuration-stationarity, Acquired elastic stability and delayed
instability, Experimental results, Discussion) sit inside paragraphs, so there are no section briefs (BRIEF = {}).
"""
from layers_gists import GIST          # one line per paragraph and figure
from layers_briefs import BRIEF        # none: the paper has no sections
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:1711.09491 · cond-mat.soft · November 2017"
DATE = "26 November 2017"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summary, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "Delayed instabilities in viscoelastic solids"
# The headline (which structures snap late) is not a formula, so the equation is the key mechanism: the stationary
# reference metric (6), readable alone, carries the collinearity of g, gbar and gbar^0 behind the stationarity property
# and shows beta as the fraction relaxed. The figure is the experimental phase diagram that tests the headline.
KEY = {"equation": "eq-gbar_stationary_condition", "figure": "fig-hopper_popper"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on elasticity, viscoelasticity or incompatible (non-Euclidean) elasticity"},
    {"key": "physicist", "label": "Physicist", "hint": "a physicist from another area; knows continuum mechanics in outline"},
    {"key": "student", "label": "Student", "hint": "knows undergraduate mechanics and some differential geometry"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract's four claims. The introduction (root-p3) states the
# chain that links them: the rest lengths as a state variable "allows us to analyze the notion of stability ... and
# discover a new stationarity property", which "elucidates the subtle nature of delayed instabilities ... as we
# demonstrate through experiment". Each link has the paper's own words (link_quote), so the shape is one argument.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-metric", "headline": True,
     "claim": r"Any linear viscoelastic material can be described exactly as an elastic body whose reference metric (its local rest lengths) evolves slowly towards the metric of its present configuration.",
     "quote": "a metric description of viscoelasticity in which the continua is characterized by temporally evolving reference lengths",
     "where": ["root-p5", "root-p7", "fig-1d_illustration"], "theme": "A"},
    {"id": "c-stationary",
     "claim": r"A body brought abruptly from rest into a locally stable elastic configuration shows no motion, although its reference metric evolves and its stress relaxes; conversely a body that settles into a fixed stable state is extremal with respect to its rest reference metric.",
     "quote": "including cases where the relaxation leads to no apparent motion",
     "where": ["root-p9", "fig-metric_space"], "theme": "A",
     "builds_on": "c-metric", "link_quote": "In particular it allows us to analyze the notion of stability in viscoelastic materials and discover a new stationarity property"},
    {"id": "c-predict", "headline": True,
     "claim": r"Which structures show delayed instability reduces to the purely elastic stability of the rest state: only configurations unstable at rest can snap late, after creep has given them a stability that, for configurations not initially extremal, is eventually lost.",
     "quote": "predict which structures will exhibit delayed instability due to viscoelastic flow",
     "where": ["root-p8", "root-p10", "root-p11"], "theme": "A",
     "builds_on": "c-stationary", "link_quote": "A particular corollary of the configuration stationarity property is that instability could be observed only for initially unstable configurations"},
    {"id": "c-poppers",
     "claim": r"For about 50 silicone-rubber conical poppers, the stability phases predicted from the separately measured $\beta$ agree very well with those observed.",
     "quote": "showing quantitative agreement with experimental measurements",
     "where": ["root-p12", "root-p13", "fig-hopper_popper"], "theme": "A",
     "builds_on": "c-predict", "link_quote": "We next come to test these predictions by examining experimentally the response of silicone-rubber poppers"},
]

ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="root-p1 root-p2">Viscoelastic structures, like elastomer shells, can creep, then snap; standard models give little intuition about which will.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-metric"><span data-covers="root-p5 fig-1d_illustration">Viscoelasticity is recast exactly as elasticity about a “reference metric”, local rest lengths that creep towards the present shape.</span></li>
  <li data-claims="c-stationary"><span data-covers="root-p9 fig-metric_space">A body brought abruptly from rest into a stable shape never moves, though its stress relaxes.</span></li>
  <li data-claims="c-predict"><span data-covers="root-p8 root-p10 root-p11">So late snaps need shapes unstable at rest that creep stabilised while held; that stability is eventually lost if not initially extremal.</span></li>
  <li data-claims="c-poppers"><span data-covers="root-p13 fig-hopper_popper">For about 50 rubber poppers, predicted stability phases match experiment, given one measured constant.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="root-p1 root-p2 root-p3">Delayed instabilities were poorly understood, and evolving-stiffness models only qualitative; this allows a quantitative understanding.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="root-p2">Delayed instability is hard to predict: hereditary-integral models are rarely solvable, and evolving-stiffness models agree with experiment only qualitatively and miss creep at zero load.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-metric"><span data-covers="root-p5">An isotropic, incompressible linear viscoelastic law is exactly elasticity about a reference metric, $S^{ij}=\tfrac12C^{ijkl}(g_{kl}-\bar g_{kl})$, relaxing towards $\bar g^\text{stat}_{ij}=\beta g_{ij}+(1-\beta)\bar g^0_{ij}$.</span></li>
  <li data-claims="c-stationary"><span data-covers="root-p9 fig-metric_space">Loaded instantly from rest into a local minimum, a body does not move while its stress relaxes, for any memory kernel: $g$, $\bar g$ and $\bar g^0$ stay collinear.</span></li>
  <li data-claims="c-predict"><span data-covers="root-p8 root-p10">So delayed instability reduces to elastic stability of the rest system, $\bar g=\bar g^0$: it needs stability acquired by creep, which is eventually lost for initially non-extremal states.</span></li>
  <li data-claims="c-poppers"><span data-covers="root-p12 root-p13">For about 50 conical silicone poppers, with $\beta=0.0928\pm0.0077$ from stress relaxation, the predicted bistable, delayed-snap and unstable phases agree very well with experiment.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="root-p3">Stationarity elucidates the subtle nature of delayed instabilities and allows their quantitative understanding;</span> <span data-covers="root-p17">the paper suggests it may also apply to creeping athermal systems.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="root-p1 root-p2">Rubber shells can creep slowly, then snap suddenly; standard models give little intuition about which will.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-metric"><span data-covers="root-p5 fig-1d_illustration">Each piece of material has preferred “reference lengths”, drifting towards its present lengths while held, back to rest once released.</span></li>
  <li data-claims="c-stationary"><span data-covers="root-p9 fig-metric_space">A shell pushed suddenly from rest into an elastically stable shape never moves, though its stresses relax.</span></li>
  <li data-claims="c-predict"><span data-covers="root-p8 root-p10 root-p11">So only shapes unstable at first can snap late, after creep stabilised them while held; it is lost if they started out of equilibrium.</span></li>
  <li data-claims="c-poppers"><span data-covers="root-p13 fig-hopper_popper">Tests on about 50 cone-shaped rubber “poppers” match predictions using one measured number.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="root-p1 root-p3">Delayed snapping, from Venus flytraps to poppers, was poorly understood; this picture explains it quantitatively.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="root-p1 root-p2">Jumping poppers, thin elastomer shells, creep slowly and then snap in a fraction of a second, as does the Venus flytrap leaf. Standard viscoelastic models simulate this well but are rarely solvable, so they say little about which structures will snap.</span> <span data-covers="root-p5 fig-1d_illustration">The paper rewrites viscoelasticity as fast elasticity measured from reference lengths that slowly creep towards the present shape.</span> <span data-covers="root-p8 root-p10">Whether a structure can snap late then reduces to its purely elastic stability at rest,</span> <span data-covers="root-p13">and the predicted phases of conical poppers match experiment.</span></p>
<p><span data-covers="root-p4">A body's shape is described by its metric $g_{ij}$, which measures lengths in the material, and strain is measured from a rest reference metric $\bar g^0_{ij}$.</span> <span data-covers="root-p5">Any linear viscoelastic law is then exactly elasticity about a reference metric $\bar g_{ij}$, which a sudden deformation leaves unchanged and which creeps towards $g_{ij}$.</span> <span data-covers="root-p5">Held fixed, it approaches $\bar g^\text{stat}_{ij}=\beta g_{ij}+(1-\beta)\bar g^0_{ij}$, so the material constant $\beta$, from 0 (elastic) to 1 (fluid), is the fraction of stress that relaxes.</span> <span data-covers="root-p6">Because elasticity acts much faster than creep, the shape at each moment minimises the elastic energy measured from $\bar g_{ij}$.</span></p>
<p><span data-covers="root-p9">This yields a stationarity property. A body brought abruptly from rest into an elastically stable configuration shows no motion, even though its reference metric evolves and its stress relaxes.</span> <span data-covers="fig-metric_space">The actual, reference and rest metrics stay collinear, so the present shape remains the admissible one closest to the drifting reference metric.</span> <span data-covers="root-p9">Conversely, a body that settles into a fixed stable state must be extremal with respect to its rest reference metric. Neither result depends on the memory kernel.</span></p>
<p><span data-covers="root-p10">A cone flipped inside out creeps for seconds and then snaps back, which seems to contradict this but is explained by it. A shape stable from the start stays a local energy minimum, so a delayed snap needs stability acquired by creep.</span> <span data-covers="root-p10 root-p11">Stability acquired while held in a shape that was not initially extremal cannot persist, and is eventually lost.</span></p>
<p><span data-covers="root-p12">Conical silicone-rubber poppers test this: thin ones are bistable, thick ones snap back at once, and in between a held popper should gain stability and later lose it.</span> <span data-covers="root-p13 fig-hopper_popper">The authors measured $\beta=0.0928\pm0.0077$ by stress relaxation, computed the phase boundaries, and found very good agreement for about 50 poppers of different shapes.</span></p>
<p><span data-covers="root-p15">The stationarity result assumes equal Poisson ratios for the elastic and viscoelastic responses, and instantaneous loading, which no experiment achieves. The paper argues that small deviations cause little motion; none was seen.</span> <span data-covers="root-p9">Its proofs are deferred to a companion paper.</span> <span data-covers="root-p16">How the snapping time depends on the holding time, and diverges near the stable phase, is anticipated but not computed.</span> <span data-covers="root-p14 root-p17">Letting the rest metric evolve would add plasticity and growth, and the paper suggests links to creeping athermal systems.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the author; not shown to readers).
FLAGS = [
    {"node": "root-p5", "note": r"“deduced from 2, 3, ??, 4”: the source's \cref list has an empty entry (a double comma), which prints as ??. Should it read Eqs. (2)–(4)?"},
    {"node": "root-p4", "note": r"Eq. (2) is introduced for an “isotropic and incompressible” material, but footnote 1 gives a general $\lambda,\mu$ stiffness, Fig. 3 uses Poisson ratio $\nu=0.47$, and root-p15 states the assumption as equal Poisson ratios of the elastic and viscoelastic responses. Which is the assumption the stationarity result needs: incompressibility, or one stiffness tensor $C^{ijkl}$ for both responses? The layers use the root-p15 wording."},
    {"node": "root-p11", "note": r"“These results hold for all incompressible linear viscoelastic bodies regardless of the form of the stress relaxation kernel”, while root-p15 adds that stationarity also assumes instantaneous loading from rest. Should root-p11 state that condition? The layers keep it."},
    {"node": "root-p13", "note": r"“The boundaries between the different stability phases of FIG. 3c depend on these geometric parameters”: the plane of the two geometric ratios is Fig. 3b; 3c varies the thickness only. Is 3b meant?"},
    {"node": "root-p14", "note": r"The additive split of strains is attributed to Lee (1969), which is usually cited for the multiplicative decomposition $F=F^eF^p$. Is the additive metric split meant as its analogue, or is another reference intended? The layers say only that the split resembles elasto-plastic decompositions."},
    {"node": "root-p17", "note": r"“The analysis below ties this creeping evolution ...” in the paper's last paragraph: presumably “above”."},
]
