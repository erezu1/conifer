"""The drafted layers of arXiv:1806.01237 (The metric description of viscoelasticity and instabilities in viscoelastic
solids, Urbach and Efrati).

Drafted by an AI reader from the paper's text; nothing here has been checked by the author yet, so every rendition
carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between $ signs.
<span data-covers="..."> marks what a sentence of a summary stands for.

Node ids: those of the reconversion with numbered sections (section-I, section-II-A, section-III-D, section-IV-A,
section-V for the unlabelled sections).
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:1806.01237 · cond-mat.soft · June 2018"
DATE = "4 June 2018"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "The metric description of viscoelasticity"
# The equation is the mechanism of the stability claims in one line: the reference metric relaxes towards a fixed mix
# of the present and rest metrics, so stationary forces are (1-beta) times the rest system's. The Hessian relation
# (eq-Hessians_static_rest) carries more of the result but needs the generalized coordinates to be read. The figure
# shows the three phases of the truss, the paper's worked demonstration, readable from its caption.
KEY = {"equation": "eq-gbar_stationary_condition", "figure": "fig-sls_von_mises_truss_lengths_space"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on elasticity, viscoelasticity or incompatible (non-Euclidean) elasticity"},
    {"key": "physicist", "label": "Physicist", "hint": "a physicist from another area; knows continuum mechanics in outline"},
    {"key": "student", "label": "Student", "hint": "knows undergraduate mechanics and some differential geometry"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (section-I-p3 to p5) and the
# summary's own list (section-V-p1, section-V-p2). The abstract's "robust claims" are two results that the summary states
# separately: stable states reached from rest never evolve (c-stationary), and only acquired stability is lost
# (c-loss, claimed in this form only in the introduction).
# How they relate, in the paper's words: the metric description "allows" the claims (abstract); the loss rules are "a
# general corollary of the previous section" (sec-transient_stability_loss-p2); the truss "demonstrates these claims"
# (abstract); the popper is the corollary applied (sec-transient_stability_loss-p2). One theme: one argument.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-metric", "headline": True,
     "claim": r"Viscoelasticity is described as elasticity about a temporally evolving reference length (for a continuum, a reference metric $\bar g_{ij}(t)$), which fast deformations leave unchanged and which relaxes from the rest reference metric towards recent configurations; it is the slow state variable of the material.",
     "quote": "we put forward a metric description of viscoelasticity",
     "where": ["section-II-A-p1", "sec-viscoelastic_continuum-p2", "sec-quasi_static_approximation-p2"], "theme": "A"},
    {"id": "c-stationary", "headline": True,
     "claim": r"For isotropic incompressible linearly viscoelastic bodies, a configuration that is stable with respect to the rest reference metric and is reached abruptly from rest never evolves and never loses stability, whatever the memory kernel.",
     "quote": "robust claims regarding stability of incompressible isotropic viscoelastic media",
     "where": ["sec-stationary_states-p3", "sec-stationary_states-p2", "sec-stationary_states-p5"], "theme": "A",
     "builds_on": "c-metric", "link_quote": "allows us to provide robust claims regarding stability"},
    {"id": "c-loss",
     "claim": r"Stationary configurations are extremals of the rest elastic system, so stability can be lost only if it was acquired through relaxation, and stability acquired by a configuration that is not such an extremal must eventually be lost.",
     "quote": "Several claims regarding the elastic stability and stationary states of such bodies are shown",
     "where": ["sec-stationary_states-p1", "sec-transient_stability_loss-p2", "sec-transient_stability_loss-p3"], "theme": "A",
     "builds_on": "c-stationary", "link_quote": "One general corollary of the previous section is that stability loss can occur only from configurations that were"},
    {"id": "c-truss",
     "claim": r"A von Mises truss of three standard linear solids displays, depending on its stiffness ratio, no bistability, lasting bistability, or bistability acquired by relaxation and lost after release, all read off a plane of lengths; the rules are proved for any assembly of SLS elements on a line sharing $\beta$ and $\tau$.",
     "quote": "We demonstrate these claims for a simple bistable systems of three standard-linear-solid spring dashpot assemblies",
     "where": ["sec-sls_von_Mises_truss-p6", "sec-sls_von_Mises_truss-p7", "app-1d_sls_systems-p3"], "theme": "A",
     "builds_on": "c-stationary", "link_quote": "We demonstrate these claims for a simple bistable systems of three standard-linear-solid spring dashpot assemblies"},
    {"id": "c-popper",
     "claim": r"For jumping poppers, rubber shells that creep and then snap back after inversion, a popper that snaps a finite time after inversion had acquired its stability, and one unstable at rest cannot be stabilized indefinitely. A simulated cone gives the flip time against thickness.",
     "quote": "viscoelastic silicone rubber shells that display delayed stability loss",
     "where": ["sec-transient_stability_loss-p1", "sec-transient_stability_loss-p3", "fig-hopper_popper"], "theme": "A",
     "builds_on": "c-loss", "link_quote": "Therefore if a popper snap a finite time after being inverted, its stability (prior to the snap) was necessarily acquired"},
]

# Every version states the five contributions; c-loss is claimed in this form only in the introduction but is the
# paper's account of the instabilities in its title, and fits.
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-I-p2 section-I-p3">Rubbery solids can creep, then snap, though relaxation should only stabilize them.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-metric"><span data-covers="section-II-A-p1 sec-viscoelastic_continuum-p2 sec-quasi_static_approximation-p2">Viscoelasticity becomes elasticity about a reference metric drifting from rest towards recent shapes.</span></li>
  <li data-claims="c-stationary"><span data-covers="sec-stationary_states-p2 sec-stationary_states-p3">In incompressible isotropic solids, a stable shape reached suddenly from rest never moves or destabilizes.</span></li>
  <li data-claims="c-loss"><span data-covers="sec-stationary_states-p1 sec-transient_stability_loss-p2 sec-transient_stability_loss-p3">In incompressible isotropic solids only acquired stability can be lost, and it always is unless the shape is a rest equilibrium.</span></li>
  <li data-claims="c-truss"><span data-covers="sec-sls_von_Mises_truss-p3 sec-sls_von_Mises_truss-p4 sec-sls_von_Mises_truss-p6">A spring–dashpot truss illustrates the rules: bistability absent, lasting, or acquired then lost.</span></li>
  <li data-claims="c-popper"><span data-covers="sec-transient_stability_loss-p1 sec-transient_stability_loss-p2 sec-transient_stability_loss-p3">Rubber “jumping poppers” that snap back late had acquired their inverted stability.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-I-p3 section-V-p1 section-V-p3">Rules expected to hold for any memory kernel give insight into stability over time, where simulations were relied on.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-I-p2 section-I-p3">Linear relaxation lowers stresses, so should never destabilize a metastable state; yet viscoelastic solids creep, then snap.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-metric"><span data-covers="sec-viscoelastic_continuum-p2 sec-quasi_static_approximation-p2">Viscoelasticity becomes elasticity about a reference metric $\bar g_{ij}(t)$, untouched by fast deformations, relaxing from the rest metric $\bar g^0_{ij}$ towards past configurations.</span></li>
  <li data-claims="c-stationary"><span data-covers="sec-stationary_states-p3 sec-stationary_states-p5">For isotropic incompressible media, a rest-stable configuration imposed abruptly from rest stays static and stable for any scalar kernel, its elastic strain shrinking by $1-\beta+\beta\phi(t)$.</span></li>
  <li data-claims="c-loss"><span data-covers="section-IV-A-p1 sec-stationary_states-p1 sec-transient_stability_loss-p3">As $\bar g^{\rm stat}=\beta g+(1-\beta)\bar g^0$, stationary configurations are rest extremals: only acquired stability can be lost, and non-extremals lose it,</span> <span data-covers="sec-stationary_states-p2">while rest saddles may stabilize permanently.</span></li>
  <li data-claims="c-truss"><span data-covers="sec-sls_von_Mises_truss-p6 sec-sls_von_Mises_truss-p7">A three-SLS von Mises truss illustrates the rules in three phases,</span> <span data-covers="app-1d_sls_systems-p4 app-1d_sls_systems-p6">proved for any mass on a line tied by equally relaxing SLS elements.</span></li>
  <li data-claims="c-popper"><span data-covers="sec-transient_stability_loss-p2 sec-transient_stability_loss-p3">Jumping poppers that snap late had acquired their stability; inverted non-extremal shapes cannot be kept.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-I-p3 section-V-p1 section-V-p3">Rules expected to hold for any memory kernel give insight where simulations were relied on, elucidating subtle viscoelastic instabilities.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-I-p2 section-I-p3">Rubbery materials can creep slowly, then snap, though relaxing stresses should only stabilize them.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-metric"><span data-covers="section-II-A-p1 sec-viscoelastic_continuum-p2 sec-quasi_static_approximation-p2">A viscoelastic solid acts as an elastic one whose preferred lengths drift towards recent shapes.</span></li>
  <li data-claims="c-stationary"><span data-covers="sec-stationary_states-p2 sec-stationary_states-p3">Pushed quickly from rest into another stable shape, an incompressible solid stays put.</span></li>
  <li data-claims="c-loss"><span data-covers="sec-stationary_states-p1 sec-transient_stability_loss-p2 sec-transient_stability_loss-p3">Only stability created by relaxation can be lost, and a shape not balanced at rest always loses it.</span></li>
  <li data-claims="c-truss"><span data-covers="sec-sls_von_Mises_truss-p3 sec-sls_von_Mises_truss-p4 sec-sls_von_Mises_truss-p6">In a spring–dashpot truss, relaxation leaves one stable state, keeps two, or briefly adds one.</span></li>
  <li data-claims="c-popper"><span data-covers="sec-transient_stability_loss-p1 sec-transient_stability_loss-p2 sec-transient_stability_loss-p3">“Jumping poppers” that snap back late had gained their inverted stability by relaxing.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-I-p3 section-V-p3">Simple rules, not simulations alone, may tell when rubber-like structures snap over time.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="section-I-p1 section-I-p2">Rubber-like solids relax stress and creep, yet keep part of their stress indefinitely. Some creep slowly and then snap, as jumping poppers, rubber shells turned inside out, do: delayed stability loss.</span> <span data-covers="section-I-p3">Laws tying stress to the whole strain history through a memory kernel simulate this well but explain little, and relaxation, which lowers stresses, seems bound to stabilize.</span> <span data-covers="section-V-p1 section-V-p2">The paper finds that intuition right for states reached abruptly from rest, and traces viscoelastic instabilities to stability that relaxation itself created.</span></p>
<p><span data-covers="section-II-A-p1">A standard linear solid, a spring in parallel with a spring and a dashpot in series, acts at every instant as one spring, $F=-k(L-\bar L)$, about a reference length $\bar L$. Viscous flow moves $\bar L$ towards both the current length and the rest length $\bar L^0$, weighted by $\beta$, the fraction of force relaxed at long times.</span> <span data-covers="sec-viscoelastic_continuum-p1 sec-viscoelastic_continuum-p2">For a continuum the stress is likewise elastic in the difference between the actual metric $g_{ij}$ and a reference metric $\bar g_{ij}(t)$. Fast deformations leave $\bar g_{ij}$ unchanged, so it is the slow state variable, drifting from the rest metric $\bar g^0_{ij}$ towards recent shapes.</span> <span data-covers="sec-quasi_static_approximation-p1 sec-quasi_static_approximation-p2">Because elasticity is fast, the body always takes the admissible shape closest to $\bar g_{ij}$ in elastic energy.</span></p>
<p><span data-covers="sec-sls_von_Mises_truss-p1 sec-sls_von_Mises_truss-p2">In a von Mises truss of three such elements, the energy is the squared distance from the reference point to the curve of lengths the truss can take. Stable states are therefore feet of normals to that curve.</span> <span data-covers="sec-sls_von_Mises_truss-p3 sec-sls_von_Mises_truss-p4">Held inverted, the truss is never bistable when its symmetry-breaking spring is stiff, and always bistable when it is soft.</span> <span data-covers="sec-sls_von_Mises_truss-p6">In between, relaxation creates an inverted stable state that is lost some time after release: a delayed instability.</span> <span data-covers="app-1d_sls_systems-p3 app-1d_sls_systems-p6">An appendix proves the rules for any such assembly on a line sharing $\beta$ and the relaxation time.</span></p>
<p><span data-covers="section-IV-A-p1">For isotropic incompressible solids the reference metric relaxes towards $\bar g^{\rm stat}_{ij}=\beta g_{ij}+(1-\beta)\bar g^0_{ij}$, whatever the memory kernel.</span> <span data-covers="sec-stationary_states-p1 sec-stationary_states-p2">So stationary forces are $(1-\beta)$ times those of the rest elastic system: every stationary configuration is an equilibrium of the body at rest, and relaxation adds a positive term to its stiffness.</span> <span data-covers="sec-stationary_states-p3 sec-stationary_states-p5">A body brought suddenly from rest into a stable shape therefore never moves or loses stability, because its reference metric slides straight towards that shape.</span> <span data-covers="sec-transient_stability_loss-p2 sec-transient_stability_loss-p3">Only acquired stability can be lost, and stability acquired away from rest equilibria always is. A popper that snaps late had acquired its stability, and one unstable at rest cannot be kept inverted indefinitely.</span></p>
<p><span data-covers="sec-stationary_states-p4">The proofs need a scalar memory kernel, so they hold exactly for incompressible solids and approximately near incompressibility.</span> <span data-covers="section-V-p3">Instabilities also need a curved set of admissible shapes, which a single element lacks; in continua relaxation can instead leave a non-Euclidean reference metric and residual stress.</span> <span data-covers="sec-transient_stability_loss-p1 fig-hopper_popper">For poppers the text applies the rules qualitatively and gives simulated flip times; the comparison with experiments that the abstract mentions is not shown here.</span> <span data-covers="section-V-p4">A rest metric that itself evolves, for growth or plasticity, is left open.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "fig-hopper_popper", "note": r"The abstract says the paper shows “quantitative agreement with recent experiments in viscoelastic silicone rubber shells”. This version has no experimental data or comparison: the popper section applies the rules qualitatively, the figure shows simulated flip times ($\beta=0.3$, $\nu=0.47$) and cites a similar phase plot in [12] and [8], sec-transient_stability_loss-p4 is empty, and the source has an “Experimental results” section commented out. Is the comparison meant to be here, or in the companion letter [8]? The layers do not claim it."},
    {"node": "sec-viscoelastic_continuum-p2", "note": r"The abstract says the rest reference metric “serves as a state variable describing the result of the viscoelastic flow”. In the body the rest metric $\bar g^0_{ij}$ is fixed, and the time-dependent reference metric $\bar g_{ij}(t)$ is the slow state variable. Is “rest” in the abstract meant to be “reference”? The layers follow the body."},
    {"node": "section-V-p2", "note": r"“Every instance of such an acquired stability cannot persist indefinitely” (also sec-sls_von_Mises_truss-p7, “every acquired stable point … must become unstable”). But sec-stationary_states-p2 lets a saddle of the rest system stabilize indefinitely, sec-transient_stability_loss-p3 and app-1d_sls_systems-p4 restrict the claim to configurations that were not extremal, and footnote 2 allows a continuous drift to a rest extremum. Should the summary carry that restriction? The layers do."},
    {"node": "sec-transient_stability_loss-p3", "note": r"“acquired stability from configurations that were not extremal initially (e.g. saddle points)”: a saddle point is an extremal, and sec-stationary_states-p2 says rest saddles may stabilize indefinitely. Is “e.g. saddle points” meant to illustrate the opposite case? The layers leave the example out."},
    {"node": "section-III-D-p2", "note": r"“isotropic with respect to any linear combination of $\bar g^0_{ij}$ and $\bar g^0_{ij}$”: presumably $\bar g^0_{ij}$ and $\bar g_{ij}$?"},
    {"node": "sec-sls_von_Mises_truss-p5", "note": r"“Stationary state” is used in two senses: here a configuration that stays fixed while the reference lengths still evolve; in sec-stationary_states-p1 and app-1d_sls_systems-p4 a state in which both the configuration and the reference metric have stopped. Is this intended? The definition of the term mentions both."},
    {"node": "sec-quasi_static_approximation-p1", "note": r"$\alpha$ denotes the truss stiffness ratio, the index of the generalized coordinates $\lambda_\alpha$, and the mixing term $\alpha(x,t)$ of section-III-D-p4; $\beta$ is both the relaxed fraction and a second Hessian index. A reader could stumble in sec-stationary_states-p2, where $\beta$ appears in both roles in one equation. Covered by the notation question."},
]
