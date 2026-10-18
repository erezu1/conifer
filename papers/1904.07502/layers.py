"""The drafted layers of arXiv:1904.07502 (Generalized Hawking-Page transitions).

Drafted by an AI reader from the paper's text; nothing here has been checked by the author yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:1904.07502 · hep-th · April 2019"
DATE = "16 April 2019"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "Hawking-Page on two spheres"
# The headline (a first order transition between two topologies) is not a formula, so the equation is the closed form
# that organises the phase diagram: the critical ratio (3.3) of the singular solution, readable with d_1, d_2 alone.
# The oscillation law (3.15) carries the multiplying solutions but has no label. The figure is the computed action
# I(beta) for S^3 x S^2, which shows the two branches, the singular ratio and the transition at beta_c = 0.720.
KEY = {"equation": "eq-singular_temp", "figure": "fig-S3S2_Fb_1"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on holography, Euclidean gravity saddles or phase transitions in AdS/CFT"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy or gravitational theorist; knows AdS/CFT and the Hawking–Page transition in outline"},
    {"key": "student", "label": "Student", "hint": "knows general relativity and quantum field theory, and has met AdS/CFT"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and sec-introduction-p3.
# The universality of the solutions (sec-introduction-p7) and the possible link to de Sitter (p3) are why they matter;
# the numerical method (section 4) is a means, and the agreement with Blackman-McDermott-Van Raamsdonk a check.
# How they relate: the paper makes one argument about one phase diagram. The singular solution and its deformations
# (section 3) predict the oscillations and the picture of the transition near beta_s, which the numerics (section 5)
# confirm: "From the analysis above we can draw a schematic picture of the phase map" (sec-sing_sol_pert-p8), and
# the small-r0 solutions are deformations of the cone (sec-sing_sol_pert-p3). One theme: one argument.
# c-d9 is claimed only in the introduction (sec-introduction-p3), so it is in the summary and not in the gist.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-transition", "headline": True,
     "claim": r"On $S^{d_1}\times S^{d_2}$ with $d_1,d_2\ge2$ the bulk solutions have two topologies, in which one sphere or the other shrinks smoothly; unlike Hawking–Page only one exists at very small or very large ratio of radii, and for $d<9$ the numerics show a single first order transition between them, close to $\beta_s$.",
     "quote": "between solutions of two different topologies as the relative radius changes",
     "where": ["sec-sing_sol_pert-p1", "section-5.2-p1", "section-5.2-p2"], "theme": "A",
     "builds_on": "c-singular", "link_quote": "From the analysis above we can draw a schematic picture of the phase map"},
    {"id": "c-singular",
     "claim": r"At the critical ratio $\beta_s=\sqrt{(d_2-1)/(d_1-1)}$ there is an exact, sub-dominant singular solution in which both spheres shrink together to a cone; its traceless deformation leaves the action unchanged at first order.",
     "quote": "singular solution where both spheres shrink",
     "where": ["sec-sing_sol_pert-p2", "sec-sing_sol_pert-p6"], "theme": "A"},
    {"id": "c-oscill",
     "claim": r"For $d<9$ deformations of the singular solution have a complex exponent, so the ratio of radii approaches $\beta_s$ in oscillations damped as $r_0^{(d-1)/2}$ and the number of solutions grows without bound as $\beta\to\beta_s$; numerical fits confirm the exponent.",
     "quote": "the number of solutions grows to infinity as the critical ratio is approached",
     "where": ["sec-sing_sol_pert-p7", "section-5.1-p2"], "theme": "A",
     "builds_on": "c-singular", "link_quote": "they will be small perturbations of the singular metric"},
    {"id": "c-d9",
     "claim": r"For $d\ge9$, a case the paper calls unphysical, the classical analysis gives one solution for every ratio and a second order transition at $\beta_s$.",
     "quote": "leads to a second order phase transition",
     "where": ["sec-sing_sol_pert-p9", "section-5.1-p2"], "theme": "A"},
]

# Every version states the three contributions the abstract claims (c-transition, c-singular, c-oscill).
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sec-introduction-p2 sec-introduction-p3">Hawking and Page found two bulk geometries competing for a holographic CFT on a sphere at finite temperature. What if the time circle becomes a second sphere?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-transition"><span data-covers="sec-sing_sol_pert-p1 section-5.2-p1">Either sphere can shrink smoothly in the bulk; numerically, for CFT dimension $d<9$, a first order transition separates these topologies as the ratio varies.</span></li>
  <li data-claims="c-singular"><span data-covers="sec-sing_sol_pert-p2">At a critical ratio of radii, an exact singular solution, both spheres shrinking to a cone, is sub-dominant.</span></li>
  <li data-claims="c-oscill"><span data-covers="sec-sing_sol_pert-p7 section-5.1-p2">Near it, for $d<9$, the cone's deformations oscillate, so solutions multiply without bound.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sec-introduction-p7">With only the metric on, this phase structure is universal for CFTs with classical Einstein duals, unless other fields lower the action.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sec-introduction-p2 sec-introduction-p3">Hawking and Page found thermal AdS and the black hole competing for boundary $S^{d-1}\times S^1$. For $S^{d_1}\times S^{d_2}$ the symmetric Einstein equations reduce to ODEs, but no analytic solution is found at a general ratio.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-transition"><span data-covers="sec-sing_sol_pert-p1 section-5.2-p1 section-5.2-p2">Either sphere caps off smoothly at a closing radius $r_0$, with one solution at extreme ratios; for $d<9$ a first order transition lies near $\beta_s$, at $\beta_c=0.720$ for $S^3\times S^2$,</span> <span data-covers="section-5.2-p1 refs">agreeing with Blackman, McDermott and Van Raamsdonk.</span></li>
  <li data-claims="c-singular"><span data-covers="sec-sing_sol_pert-p2 sec-sing_sol_pert-p6">The cone $f,h\propto\sinh z$ at $\beta_s=\sqrt{(d_2-1)/(d_1-1)}$ is exact and sub-dominant; its traceless deformation leaves the action unchanged at leading order, so both branches are expected to arrive with zero slope.</span></li>
  <li data-claims="c-oscill"><span data-covers="sec-sing_sol_pert-p7 section-5.1-p2">For $d<9$ the deformation exponent is complex: $\beta-\beta_s\propto r_0^{(d-1)/2}\cos(\omega\log r_0+\phi)$, confirmed by fits, so solutions multiply without bound near $\beta_s$.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sec-introduction-p3 sec-introduction-p7">The two-sphere partition function is a non-thermal observable, possibly continued to de Sitter times a sphere, and these Einstein-only saddles are universal, though possibly sub-leading where other fields condense.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sec-introduction-p2 sec-introduction-p3">In holography, Hawking and Page found two spacetimes competing for a field theory on a hot sphere. What if time's circle becomes a second sphere?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-transition"><span data-covers="sec-sing_sol_pert-p1 section-5.2-p1">Numerically, either sphere can shrink smoothly to a point; if the two dimensions sum to under nine, a sudden (first order) transition separates the shapes.</span></li>
  <li data-claims="c-singular"><span data-covers="sec-sing_sol_pert-p2">At one critical size ratio, an exact solution has both spheres shrinking together to a singular cone; it never dominates.</span></li>
  <li data-claims="c-oscill"><span data-covers="sec-sing_sol_pert-p7 section-5.1-p2">Near that ratio, in the same dimensions, the cone's deformations oscillate, so ever more solutions appear.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sec-introduction-p7">Only gravity enters, so this holds for theories well described by classical Einstein gravity, unless other fields interfere.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="sec-introduction-p2">For a holographic CFT on a sphere at finite temperature, Hawking and Page found two competing bulk geometries. In thermal AdS the sphere shrinks to zero inside; in the Euclidean black hole the time circle does.</span> <span data-covers="sec-introduction-p3 sec-setup-p1">The paper replaces the circle by a second sphere, for CFTs dual to classical Einstein gravity. The partition function on $S^{d_1}\times S^{d_2}$ is no longer thermal but is still an observable, and the answer is universal, because only the metric is turned on.</span> <span data-covers="section-5.2-p1 sec-sing_sol_pert-p7">Again two topologies compete, with a first order transition for CFT dimension $d<9$, and near a critical ratio of radii the number of solutions grows without bound.</span></p>
<p><span data-covers="sec-setup-p1 sec-setup-p3">Symmetry reduces the Einstein equations to ODEs along one radial direction. Space ends smoothly where one sphere shrinks, and the other sphere's radius there, the closing radius $r_0$, fixes the solution and its boundary ratio of radii $\beta$.</span> <span data-covers="sec-sing_sol_pert-p1">At extreme ratios the smaller sphere shrinks first, so each extreme has a single solution of its own topology, with diverging action. Unlike thermal AdS, neither topology exists at every ratio, so the two must exchange dominance.</span></p>
<p><span data-covers="sec-sing_sol_pert-p2">At $r_0=0$ both spheres shrink together to a cone. This singular solution is exact and sits at the critical ratio $\beta_s=\sqrt{(d_2-1)/(d_1-1)}$.</span> <span data-covers="sec-sing_sol_pert-p3 sec-sing_sol_pert-p7">Smooth solutions with small $r_0$ are small deformations of the cone, whose exponent is complex for $d<9$. So $\beta$ approaches $\beta_s$ in damped oscillations, $\beta-\beta_s\propto r_0^{(d-1)/2}\cos(\tfrac12\sqrt{(d-1)(9-d)}\log r_0+\phi)$, and solutions multiply near $\beta_s$.</span> <span data-covers="sec-sing_sol_pert-p6 sec-sing_sol_pert-p8">The action is stationary under this deformation, so both branches reach $\beta_s$ with zero slope.</span> <span data-covers="sec-sing_sol_pert-p9">For $d\ge9$ the approach is monotonic, with one solution per ratio and, classically, a second order transition at $\beta_s$.</span></p>
<p><span data-covers="sec-hybrid_method_calc_energy-p4 sec-hybrid_method_calc_energy-p5">The renormalized action is computed by fitting the near-boundary expansion and integrating that region analytically, the interior numerically, at fixed CFT volume.</span> <span data-covers="section-5.1-p2 tb-temp_exponent">Fits recover the predicted exponents, less precisely as $d$ nears 9.</span> <span data-covers="section-5.2-p1 section-5.2-p2">The action turns out to decrease away from the cone, so the extra solutions should never dominate. The numerics show the simplest scenario, a single first order transition near $\beta_s$: for $S^3\times S^2$ at $\beta_c=0.720$, against $\beta_s\approx0.707$, agreeing with earlier work.</span> <span data-covers="section-5.3-p1 section-6.1-p1 section-6.2-p1">The stress tensor spirals into its singular value, and equal spheres and $S^4\times S^2$ behave alike.</span></p>
<p><span data-covers="sec-introduction-p7 sec-introduction-p8 sec-setup-p1">Only the metric is turned on and both spheres' symmetry is assumed, so in specific theories other solutions could dominate.</span> <span data-covers="sec-introduction-p4">Quantum effects, which should turn the transition into a crossover at finite $N$, are not studied.</span> <span data-covers="sec-sing_sol_pert-p7 section-5.2-p1">The oscillations' amplitude and phase are only fitted, and why the action decreases away from the cone has no analytic explanation.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the author; not shown to readers).
FLAGS = [
    {"node": "sec-sing_sol_pert-p7", "note": r"With $\alpha=-\tfrac12\big(d-1+\sqrt{(d-1)(d-9)}\big)$, ${\rm Im}(\alpha)$ is $\pm\tfrac12\sqrt{(d-1)(9-d)}$, not $\sqrt{(d-1)(9-d)}$, and (3.15) and section-5.1-p2 then need $\omega=\tfrac12\sqrt{(d-1)(9-d)}$; Table 1's expected $\omega$ (2 for $d=5$, 1.936 for $d=6$) uses the half. Is the factor $\tfrac12$ missing in the text? The layers use $\tfrac12\sqrt{(d-1)(9-d)}$."},
    {"node": "section-5.2-p1", "note": r"“the action decreases at second order in the expansion around the singular solution” reads against sec-sing_sol_pert-p8, where a decreasing action “as the solution becomes singular” gives infinitely many transitions. Consistent if 5.2 means decreasing away from the cone (the singular solution a local maximum along the branch); is that the intended reading? The layers say “decreases away from the cone”."},
    {"node": "tb-temp_exponent", "note": r"The text says the fitted exponents agree “to high precision”, but for $d=8$ the fitted frequencies (0.48 for $(6,2)$, 0.91 for $(5,3)$, 1.03 for $(4,4)$) are far from 1.32. Should the claim be limited to smaller $d$? The layers say the agreement worsens as $d$ nears 9, as the paper explains."},
    {"node": "section-5.3-p1", "note": r"$g^s_{(d)}=0$ (3.4) holds only for $d>4$, since $r_{1,2}^2$ are quartic in $\rho$; for $S^2\times S^2$ ($d=4$), does the spiral in figure 7 close on zero or on a non-zero value? The section speaks of “the singular value $g_{(d)}(\beta_s)=0$” for all cases."},
    {"node": "sec-introduction-p3", "note": r"The abstract calls the singular solution “sub-dominant” without restriction, while footnote 4 says that for $d\ge9$ it dominates at one ratio. Should the abstract say “for $d_1+d_2<9$”? The layers follow the abstract in the gist and say “for $d<9$” in the definition."},
    {"node": "section-5.3-p1", "note": r"“As we mentioned above (see section 3)”: the stress tensor relation is stated in section 2 (sec-setup-p8). Should it read section 2?"},
]
