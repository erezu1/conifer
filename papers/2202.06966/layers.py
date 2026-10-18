"""The drafted layers of arXiv:2202.06966 (String Stars in Anti de Sitter Space).

Drafted by an AI reader from the paper's text; nothing here has been checked by the author yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, figure and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2202.06966 · hep-th · February 2022"
DATE = "14 February 2022"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "String stars in AdS"
# The introduction says the main results are drawn in figures 2 and 1; figure 2 (the star's size against the
# temperature, flat-space agreement when cold, bounded size and merger at beta_c when hot) carries both headline
# results. The equation is the AdS Hagedorn temperature (5.6), readable with R_H, kappa and l_s/l_ads alone.
KEY = {"equation": "eq-R_c", "figure": "fig-length_scale"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on string stars, the Hagedorn transition or small AdS black holes"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows AdS/CFT and black hole thermodynamics in outline"},
    {"key": "student", "label": "Student", "hint": "knows general relativity, quantum field theory and a first course on strings"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (sec-intro-p4 to p7).
# The hypothetical connection to the small AdS black hole (abstract's third sentence, sec-intro-p5 "Therefore the
# extrapolation ... follows exactly the flat space analysis") is drawn from the flat-space agreement, so it is why
# the results matter, not a contribution. The holographic entanglement entropy (section 8) is claimed in neither the
# abstract nor the introduction: it is in the summary, not here (see FLAGS).
# How they relate, from the paper's own words: the paper follows one saddle in temperature (figure 2). Theme A is
# the cold, flat-space-like star (section 3); theme B the hot star (sections 4-5), whose branch the paper states is
# "connected continuously" to the colder solutions, with the AdS Hagedorn temperature and the every-d existence
# both drawn from the merger; theme C the instabilities (section 6), whose negative mode near R_c uses the entropy
# scaling of theme B. Every theme but the first builds on another: one argument.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-flat", "headline": True,
     "claim": r"For $l_s/l_{ads}\ll(R_0-R_H)/R_H\ll1$ the AdS string star is too small to feel the curvature and coincides with the flat-space Horowitz–Polchinski solution, which exists for $3\le d\le5$.",
     "quote": "a regime of temperatures in which the saddle is very similar to the flat space solution found by Horowitz and Polchinski",
     "where": ["sec-small_sol-p1", "sec-small_sol-p2", "sec-small_sol-p3"], "theme": "A"},
    {"id": "c-gas", "headline": True,
     "claim": r"At higher temperatures the AdS string star's size stays of order $\sqrt{l_sl_{ads}}$ instead of diverging, and at a critical temperature $\beta_c<\beta_H$ its amplitude vanishes and it joins the thermal gas, with free energy $F\sim(\beta-\beta_c)^2$ (assuming the simplest scenario, supported by numerics).",
     "quote": "we describe how the solution joins with the thermal gas phase",
     "where": ["sec-at_hagedorn-p1", "sec-gas_transition-p1", "sec-gas_transition-p7"], "theme": "B",
     "builds_on": "c-flat", "link_quote": "as it is connected continuously to the solutions we found for higher"},
    {"id": "c-hagedorn",
     "claim": r"The merger point is the AdS Hagedorn temperature, $R_c/R_H=1-\frac{d}{\sqrt{2\kappa}}\frac{l_s}{l_{ads}}$ at leading order; for $\mathcal N=4$ super Yang–Mills its constant term $1/2\pi$ agrees with integrability numerics.",
     "quote": "find the leading correction to the Hagedorn temperature due to the AdS curvature",
     "where": ["sec-gas_transition-p2", "sec-gas_transition-p3"], "theme": "B",
     "builds_on": "c-gas", "link_quote": "it means that at that point the trivial solution has a zero mode"},
    {"id": "c-alld",
     "claim": r"Close to $\beta_c$ AdS string stars exist for every $d$, also $d\ge6$ where flat-space ones do not; there, numerically, they become string-sized near $\beta_H$ with the entropy of a string-sized black hole, a correspondence principle that exists only in AdS.",
     "quote": "In AdS on the other hand string star solutions exist close to",
     "where": ["sec-gas_transition-p8", "sec-numerical_res-p3"], "theme": "B",
     "builds_on": "c-gas", "link_quote": "The results of this section are valid for any spatial dimension"},
    {"id": "c-gl",
     "claim": r"The string star is argued to have a negative mode (near $\beta_c$ from its negative specific heat), and away from $\beta_c$ any such mode implies Gregory–Laflamme-like negative modes when extra dimensions are present at the AdS curvature scale.",
     "quote": "argue for a Gregory-Laflamme-like instability whenever extra dimensions are present at the AdS curvature scale",
     "where": ["sec-therm_inst-p4", "sec-therm_inst-p8", "sec-therm_inst-p9"], "theme": "C",
     "builds_on": "c-gas", "link_quote": "Close to $R_c$ we found the entropy scales like"},
]

# Every version states the four contributions the abstract claims (c-flat, c-gas, c-hagedorn, c-gl); c-alld,
# claimed only in the introduction, is in the specialist's gist, where there is room, and in the summary.
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sec-intro-p1 sec-intro-p2">A black hole naively extrapolated to the string scale roughly agrees with a “string star” of hot strings; here, in AdS.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-flat"><span data-covers="sec-small_sol-p1 sec-small_sol-p2">Somewhat below the Hagedorn temperature, the AdS star is the flat-space Horowitz–Polchinski solution.</span></li>
  <li data-claims="c-gas"><span data-covers="sec-at_hagedorn-p1 sec-gas_transition-p1">Hotter, its size stays bounded; it fades into the thermal gas.</span></li>
  <li data-claims="c-hagedorn"><span data-covers="sec-gas_transition-p2 sec-gas_transition-p3">That is the AdS Hagedorn temperature, hotter than flat space's by a fraction $\sim l_s/l_{ads}$.</span></li>
  <li data-claims="c-gl"><span data-covers="sec-therm_inst-p4 sec-therm_inst-p9">Near it a negative mode is argued for; farther away, AdS-sized extra dimensions should make such modes Gregory–Laflamme-like.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sec-intro-p5 sec-intro-p7">If, as speculated, the small black hole turns into this star when heated, the star predicts how the dual CFT's metastable phase meets the confined one.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sec-intro-p1 sec-intro-p3">Extrapolated, the flat-space Horowitz–Polchinski star agrees qualitatively with a string-sized black hole; here it sits in thermal $AdS_{d+1}$.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-flat"><span data-covers="sec-small_sol-p1 sec-small_sol-p2">For $l_s/l_{ads}\ll(R_0-R_H)/R_H\ll1$ the AdS star is the flat-space solution, for $3\le d\le5$.</span></li>
  <li data-claims="c-gas"><span data-covers="sec-at_hagedorn-p1 sec-gas_transition-p4">Hotter, $L$ grows only up to $L_c\sim\sqrt{l_sl_{ads}}$;</span> <span data-covers="sec-gas_transition-p1 sec-gas_transition-p7">its amplitude vanishes at $R_c$, where it joins thermal AdS with $F\sim(R_0-R_c)^2$, as in the weakly coupled CFT.</span></li>
  <li data-claims="c-hagedorn"><span data-covers="sec-gas_transition-p2 sec-gas_transition-p3">That is the AdS Hagedorn temperature, $R_c/R_H=1-\frac{d}{\sqrt{2\kappa}}\frac{l_s}{l_{ads}}$; for N=4 SYM its $\lambda^0$ term, $1/2\pi$, agrees with integrability.</span></li>
  <li data-claims="c-alld"><span data-covers="sec-gas_transition-p8 sec-numerical_res-p3">Near $R_c$ stars exist for every $d$; for $d\ge6$ they turn string-sized near $R_H$, qualitatively like a small black hole.</span></li>
  <li data-claims="c-gl"><span data-covers="sec-therm_inst-p4 sec-therm_inst-p9">Negative specific heat near $R_c$ argues for a negative mode; farther away, where it is expected to fit in compact dimensions of AdS size, it becomes Gregory–Laflamme-like.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sec-intro-p5 sec-intro-p7">The qualitative small-black-hole correspondence carries over; if, as speculated, that phase becomes this star, the CFT gets strong-coupling predictions for how it meets the confined phase.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sec-intro-p1 sec-intro-p2">A string-sized black hole behaves roughly like a “string star” of self-bound hot strings, here in AdS space.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-flat"><span data-covers="sec-small_sol-p1 sec-small_sol-p2">Somewhat colder than the Hagedorn temperature the star cannot notice the curvature: it is the flat-space solution.</span></li>
  <li data-claims="c-gas"><span data-covers="sec-at_hagedorn-p1 sec-gas_transition-p1">Hotter, its size stays bounded; it fades into a gas of strings.</span></li>
  <li data-claims="c-hagedorn"><span data-covers="sec-gas_transition-p2 sec-gas_transition-p3">That marks AdS's Hagedorn temperature, slightly above flat space's, where string gas turns unstable.</span></li>
  <li data-claims="c-gl"><span data-covers="sec-therm_inst-p4 sec-therm_inst-p9">Near it the star is argued to have an unstable mode; farther away, AdS-sized extra dimensions should add Gregory–Laflamme-like ones.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sec-intro-p5 sec-intro-p7">If, as speculated, small black holes turn into this star when heated, it predicts how that dual field-theory phase joins the confined one.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="sec-intro-p1">A black hole shrunk to the string scale has roughly the thermodynamics of a string state of the same energy: the “correspondence principle”. In Horowitz and Polchinski's canonical version, the string wound around the Euclidean time circle, light just below the Hagedorn temperature, binds with gravity into a “string star”.</span> <span data-covers="sec-intro-p2 sec-intro-p3">The paper places this star at the centre of thermal anti de Sitter space, where the partition function is well defined and equals that of a dual CFT.</span> <span data-covers="sec-small_sol-p3 sec-gas_transition-p1">When cold, the AdS star is the flat-space one, so its rough agreement with a string-sized black hole carries over; when hotter, it fades into the thermal gas.</span> <span data-covers="sec-gas_transition-p2 sec-gas_transition-p7">It does so at the AdS Hagedorn temperature, which the paper computes, with scalings that give the dual CFT strong-coupling predictions.</span></p>
<p><span data-covers="sec-action-p1">In thermal AdS the time circle widens away from the centre. The winding string's mass is set by the local radius, so it is light only near the centre, and near the flat-space Hagedorn radius $R_H$.</span> <span data-covers="sec-action-p3 sec-EOM-p1">Reducing on the circle gives an effective theory in $d$ spatial dimensions for the winding mode $\chi$ and the circle's size $\varphi$; its bound states are the AdS string stars.</span> <span data-covers="sec-small_sol-p1 sec-small_sol-p2">A star much smaller than $\sqrt{l_sl_{ads}}$ does not feel the curvature and solves exactly the Horowitz–Polchinski equations. With $R_0$ the circle's radius at the centre (larger is colder), this holds for $l_s/l_{ads}\ll(R_0-R_H)/R_H\ll1$, and only for $3\le d\le5$.</span> <span data-covers="sec-small_sol-p3">At the cold end of this window the star is string-sized, with entropy $S\sim l_s^{d-1}/G_N$, like a string-sized small AdS black hole. Both are far smaller than the AdS radius, so the flat-space comparison carries over.</span> <span data-covers="sec-ee-p4 sec-ee-p6">Their holographic entanglement entropies agree in the same way.</span></p>
<p><span data-covers="sec-at_hagedorn-p1">Hotter, at $R_H$, the winding mass vanishes at the centre but grows as $\rho^2$ away from it, a confining potential, so the star keeps a size of order $\sqrt{l_sl_{ads}}$ instead of diverging.</span> <span data-covers="sec-gas_transition-p1 sec-numerical_res-p3">Hotter still, the paper assumes, and its numerics support, that the star loses amplitude until it merges with thermal AdS at a critical radius $R_c$, below $R_H$.</span> <span data-covers="sec-gas_transition-p6 sec-gas_transition-p7">Near the merger the amplitude grows as $(R_0-R_c)^{1/2}$ and the free energy as $(R_0-R_c)^2$, the scaling found in the weakly coupled dual gauge theory.</span> <span data-covers="sec-gas_transition-p8 sec-numerical_res-p3">Since this analysis holds in any dimension, AdS string stars exist near $R_c$ for every $d$. For $d\ge6$ numerics show them shrinking to string size near $R_H$, with the entropy of a string-sized black hole: a correspondence that exists only in AdS.</span></p>
<p><span data-covers="sec-gas_transition-p2">At the merger thermal AdS has a normalizable zero mode, so $R_c$ is where the string gas turns tachyonic: the AdS Hagedorn temperature.</span> <span data-covers="sec-gas_transition-p3 sec-gas_transition-p5">Near the centre the linearized equation is a harmonic oscillator, and the zero mode is its ground state. Its zero-point energy must be paid by a negative mass squared at the centre, so the gas becomes unstable hotter than in flat space.</span> <span data-covers="sec-gas_transition-p3">To leading order $R_c/R_H=1-\frac{d}{\sqrt{2\kappa}}\frac{l_s}{l_{ads}}$, with $\kappa$ a constant of the string theory.</span> <span data-covers="sec-gas_transition-p3">For type IIB on $AdS_5\times S^5$ this gives N=4 super Yang–Mills a Hagedorn temperature $T_c=\lambda^{1/4}/\sqrt{8\pi^2}+1/2\pi$ at strong coupling. Its constant agrees with integrability numerics.</span></p>
<p><span data-covers="sec-therm_inst-p1">With positive free energy, the star is subdominant to the gas and the large black hole.</span> <span data-covers="sec-therm_inst-p3 sec-therm_inst-p4">It also appears to have a negative mode, a fluctuation that lowers its Euclidean action. It is inherited from flat space in the cold window, and near $R_c$ follows from the star's negative specific heat.</span> <span data-covers="sec-therm_inst-p5">For $3\le d\le5$ the paper suggests the two are one mode, present throughout.</span> <span data-covers="sec-therm_inst-p8 sec-therm_inst-p9">When the compact part of space has the AdS size, such a mode, modulated along it, stays negative, except too close to $R_c$. This is the string star's analogue of the Gregory–Laflamme instability that turns small AdS black holes ten-dimensional.</span></p>
<p><span data-covers="sec-thermo-p5 sec-small_sol-p3">The link to the small AdS black hole remains a qualitative extrapolation: neither saddle is reliable near $\beta\sim l_s$, and whether they connect is open, as in flat space.</span> <span data-covers="sec-at_hagedorn-p1 sec-gas_transition-p1">Between $R_H$ and $R_c$ no analytic solution is known, and the smooth merger with the gas is the simplest scenario, checked numerically.</span> <span data-covers="sec-gas_transition-p9">Too close to $R_c$ one-loop effects dominate the tree-level free energy.</span> <span data-covers="sec-therm_inst-p5 sec-therm_inst-p10">The negative mode is shown only near the two ends of the temperature range, and what the star decays into is open.</span> <span data-covers="sec-ee-p1">Nor are the star's states identified in the dual CFT.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the author; not shown to readers).
FLAGS = [
    {"node": "sec-action-p2", "note": r"(2.2) writes $\sinh^2(\rho/l_{ads})\,d\Omega_{d-1}^2$ without the factor $l_{ads}^2$ that (2.1) has. A typo?"},
    {"node": "sec-thermo-p5", "note": r"(2.22) gives $S_\text{Large}=\frac{\omega_{d-1}}{G_N}(\dots)$, but the area law (2.21), $S=\frac{\omega_{d-1}}{4G_N}r_h^{d-1}$, with $r_h=(4\pi/d)l_{ads}^2/\beta$ gives $\frac{\omega_{d-1}}{4G_N}(\dots)$. Is a factor $1/4$ missing?"},
    {"node": "sec-thermo-p6", "note": r"(2.24) has $S_\text{10d}=\frac{\omega_8}{4\pi G_N^{(10)}}(\dots)^8$; the area law gives $4G_N^{(10)}$, not $4\pi G_N^{(10)}$. Intended?"},
    {"node": "sec-numerical_res-p3", "note": r"“In figures 4, 8 the critical length scale $L_c$ is drawn as a green horizontal line”: by the captions $L_c$ is drawn in the length-scale figures 5 and 7. Should it read 5, 7?"},
    {"node": "sec-numerical_res-p2", "note": r"“Figure 6 shows the power-law behavior of the free energy and the amplitude”: the caption of figure 6 has the amplitude and the normalized entropy. Similarly sec-gas_transition-p7 cites figure 4 for the scaling (5.13), which figure 6 shows. Which is meant?"},
    {"node": "sec-therm_inst-p8", "note": r"“Comparing to (6.5)” presumably means (6.4), the $d$-dimensional eigen-equation; and the second line of (6.6) has $\partial_z^2\chi$ where $\partial_z^2\delta\chi$ seems meant."},
    {"node": "sec-ee-p6", "note": r"“from zero at $\theta_A=0$ to its full value (8.1) at $\theta_A=\pi$”: (8.1) is the replica formula; the full value is presumably the star's entropy (2.17)/(2.19). Which is meant?"},
    {"node": "sec-ee", "note": r"The holographic entanglement entropy of section 8 is mentioned in neither the abstract nor the introduction, so the layers list it in the summary and section brief but not among the contributions. Is it meant as a result of the paper?"},
    {"node": "sec-intro-p4", "note": r"The drafter read the paper as one argument (one saddle followed in temperature, figure 2; the instability argument near $R_c$ using the entropy scaling of section 5) rather than three separate studies, as the abstract's “We also study … Finally” might suggest. Is that the intended reading?"},
]
