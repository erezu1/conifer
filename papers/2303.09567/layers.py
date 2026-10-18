"""The drafted layers of arXiv:2303.09567 (The black hole/string transition in AdS3 and confining backgrounds).

Drafted by an AI reader from the paper's text; nothing here has been checked by the author yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2303.09567 · hep-th · March 2023"
DATE = "16 March 2023"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "String stars in AdS₃ and confining backgrounds"
# The equation is the general curvature correction to the holographic Hagedorn temperature (3.11), the formula the
# abstract's second finding names and that every confining example (and AdS3 with finite RR flux) evaluates; it reads
# with T_st, d and l alone. The figure is the conjectured AdS3 phase diagram (Figure 1), the first finding's picture
# of the BTZ/string transition. The two belong to different findings; no single figure or equation carries both.
KEY = {"equation": "eq-conf_hag", "figure": "fig-ads3_phase_diagram"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on string stars, the Hagedorn transition or strings in AdS₃"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows holography and black hole thermodynamics in outline"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory, general relativity and a first course on strings"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract ("First, ... Second, ...") and the introduction
# (section-1-p3 to p6). How they relate, from the paper's own words: theme A is AdS3 (the string stars for mixed flux;
# the BTZ/string transition, whose BTZ end is the string star with the circles exchanged, sec-thermo-p5); theme B is
# the confining backgrounds (the winding-string gas; the Hagedorn correction its analysis gives, sec-gen_disc-p1; the
# black brane/string transition and the Yang-Mills relation, conditioned on the gas, sec-d4_back-p7). The paper says
# the Witten phase diagram is "very similar" to AdS3's (section-1-p6, sec-d4_back-p5), an analogy, not a step of one
# argument, and the abstract presents the two as "First" and "Second": several findings.
# The pure NS-NS Hagedorn temperature matching the exact worldsheet value (section-4.2-p1) and the vanishing of the
# curvature correction to the winding mass (sec-higher_curv-p1) are claimed in neither the abstract nor the
# introduction: they are nice observations in the summary, not contributions.
SHAPE = "several findings"
CONTRIBUTIONS = [
    {"id": "c-ads3", "headline": True,
     "claim": r"AdS$_3$ curvature stabilises the thermal winding condensate, so string stars exist near the AdS$_3$ Hagedorn temperature although none exist on flat $\mathbb R^2\times S^1$; with finite RR flux they resemble the higher-dimensional AdS string stars, of size $\sqrt{l_sl_{ads}}(1-\lambda^2)^{-1/4}$, and for small RR flux or pure NS-NS flux they grow to the AdS scale, with the back-reacted NS-NS flux at leading order.",
     "quote": "with mixed RR and NS-NS fluxes (including the pure NS-NS system)",
     "where": ["sec-finite_RR-p2", "sec-small_RR_anal-p2", "sec-small_RR_num-p4"], "theme": "A"},
    {"id": "c-btz",
     "claim": r"Small BTZ black holes are cold, so the AdS$_3$ string star cannot meet them; exchanging the boundary circles gives a winding condensate on the BTZ near $R_c'=1/R_c$, and the paper conjectures a line of saddles joining the two, a BTZ/string transition unique to AdS$_3$, on evidence it calls much weaker than in higher dimensions.",
     "quote": "comment on a possible BTZ/string transition unique to",
     "where": ["sec-thermo-p4", "sec-thermo-p5", "fig-ads3_phase_diagram"], "theme": "A",
     "builds_on": "c-ads3", "link_quote": "string star saddle after switching the circles we get a new saddle"},
    {"id": "c-gas", "headline": True,
     "claim": r"Confining holographic backgrounds in which a non-thermal cycle shrinks in the infrared (the D4 and D3 Witten models, Maldacena–Nuñez, Klebanov–Strassler) admit a new near-Hagedorn saddle, the “winding-string gas”: a thermal winding condensate homogeneous along the boundary directions, localised at the tip with size $\sqrt{l_sl}$, and highly subdominant.",
     "quote": "saddles for confining holographic backgrounds such as the Witten model",
     "where": ["sec-gen_disc-p4", "sec-d4_back-p4", "sec-mn_back-p3"], "theme": "B"},
    {"id": "c-hag",
     "claim": r"The leading curvature correction to the Hagedorn temperature of these confining theories is $\beta_c=\sqrt{4\pi/T_{st}}\,\bigl(1-\tfrac{d}{2\sqrt2}\,l_s/l\bigr)$, set by the confining string tension and the curvature radius $l$ at the tip, and evaluated for each model.",
     "quote": "determine the subleading correction to their Hagedorn temperature",
     "where": ["sec-gen_disc-p5", "sec-gen_disc-p6", "sec-d4_back-p3"], "theme": "B",
     "builds_on": "c-gas", "link_quote": "The analysis allows us to find the characteristic behavior of the solution and the leading correction to the Hagedorn temperature"},
    {"id": "c-ym",
     "claim": r"The paper speculates a black brane/string transition in these models, a line of metastable saddles joining the black brane's $x^4$-winding condensate to the winding-string gas, and argues that the gas, invariant under exchanging $\beta$ and $2\pi R$, may continue at weak coupling to the deconfined phase of pure 3+1 Yang–Mills.",
     "quote": "argue for a possible relation to the deconfined phase of 3+1 dimensional pure Yang-Mills",
     "where": ["sec-d4_back-p5", "sec-d4_back-p7", "fig-witten_model"], "theme": "B",
     "builds_on": "c-gas", "link_quote": "If indeed the winding-string gas saddle is the one that connects the two saddles between"},
]

# Every version states the five contributions, all claimed in the abstract: one point per finding (theme A: c-ads3
# and c-btz; theme B: c-gas, c-hag and c-ym). Why it matters gives each finding its own clause, as the introduction
# frames it (section-1-p3 for AdS3; section-1-p7 for the confining predictions); the paper has no discussion section.
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1">String stars, thermal winding condensates, may describe string-scale black holes;</span> <span data-covers="section-1-p3 section-1-p6">the paper studies AdS$_3$ and confining backgrounds.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-ads3 c-btz"><span data-covers="sec-finite_RR-p1 sec-finite_RR-p5">AdS$_3$ curvature binds string stars, unlike flat $\mathbb R^2\times S^1$;</span> <span data-covers="sec-finite_RR-p4 sec-small_RR_anal-p2">they grow to AdS size as NS-NS flux replaces RR.</span> <span data-covers="sec-thermo-p4 sec-thermo-p5">A possible BTZ/string transition could link them to a winding condensate on the BTZ.</span></li>
  <li data-claims="c-gas c-hag c-ym"><span data-covers="sec-gen_disc-p4 sec-d4_back-p4">Confining backgrounds host a new “winding-string gas”,</span> <span data-covers="sec-gen_disc-p5 sec-gen_disc-p6">and curvature slightly raises their Hagedorn temperature;</span> <span data-covers="sec-d4_back-p5 sec-d4_back-p7">a black brane/string transition through the gas, and a link to deconfined 3+1 Yang–Mills, are speculated.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p3">AdS$_3$ suggests a black hole/string correspondence may exist wherever weakly coupled black holes do;</span> <span data-covers="section-1-p7">the confining saddles give predictions for their gauge duals.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">String stars may continue string-scale black holes to the Hagedorn point; earlier work built them in AdS$_{d+1}$, $d>2$.</span> <span data-covers="section-1-p3 section-1-p6">Here: AdS$_3$ and confining backgrounds.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-ads3 c-btz"><span data-covers="sec-finite_RR-p2 sec-finite_RR-p4 sec-finite_RR-p5">Curvature stabilises AdS$_3$ string stars, absent on flat $\mathbb R^2\times S^1$; near Hagedorn, for non-small RR flux, $L\sim\sqrt{l_sl_{ads}}(1-\lambda^2)^{-1/4}$, $\lambda$ the NS-NS fraction;</span> <span data-covers="sec-small_RR_anal-p2 sec-small_RR_num-p4">AdS-sized for small RR flux.</span> <span data-covers="sec-thermo-p4 sec-thermo-p5">A possible BTZ/string transition, unique to AdS$_3$, would link the star to the BTZ's angular winding condensate, born at $R_c'$, the branches speculated to meet near $R_0\sim l_{ads}$.</span></li>
  <li data-claims="c-gas c-hag c-ym"><span data-covers="sec-gen_disc-p4 sec-d4_back-p4">In the IR of confining backgrounds a subdominant “winding-string gas” of size $\sqrt{l_sl}$ exists, $l$ the IR curvature radius,</span> <span data-covers="sec-gen_disc-p5 sec-gen_disc-p6">with $\beta_c=\sqrt{4\pi/T_{st}}\,\bigl(1-\tfrac{d}{2\sqrt2}\,l_s/l\bigr)$ for a shrinking $S^{d-1}$;</span> <span data-covers="sec-d4_back-p5 sec-d4_back-p7">a black brane/string transition through it is speculated, and a link to deconfined 3+1 Yang–Mills argued possible.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p3">AdS$_3$ suggests a black hole/string correspondence wherever weakly coupled black holes exist;</span> <span data-covers="section-1-p7">the confining saddles give predictions for their gauge duals.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1">String-scale black holes may become “string stars”, clumps of wound strings;</span> <span data-covers="section-1-p3 section-1-p6">the paper studies them in AdS$_3$ and confining backgrounds.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-ads3 c-btz"><span data-covers="sec-finite_RR-p1 sec-finite_RR-p5">AdS$_3$ curvature holds string stars together, unlike flat space of that dimension;</span> <span data-covers="sec-finite_RR-p4 sec-small_RR_anal-p2">they grow as NS-NS flux replaces RR.</span> <span data-covers="sec-thermo-p4 sec-thermo-p5">A possible transition could link them to wound strings on BTZ black holes.</span></li>
  <li data-claims="c-gas c-hag c-ym"><span data-covers="sec-gen_disc-p4 sec-d4_back-p4">Confining backgrounds host a new “winding-string gas”,</span> <span data-covers="sec-gen_disc-p5 sec-gen_disc-p6">and curvature slightly raises their Hagedorn temperature;</span> <span data-covers="sec-d4_back-p5 sec-d4_back-p7">the gas may link to black branes, and to deconfined Yang–Mills.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p3">AdS$_3$ suggests black holes and string stars may be linked wherever weakly coupled black holes exist;</span> <span data-covers="section-1-p7">the confining saddles give predictions for gauge theories.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="section-1-p1">A black hole shrunk to the string scale may become a hot, self-gravitating bound state of strings: the black hole/string transition. Its Euclidean candidate is the string star, a condensate of strings wound around the thermal circle, reliable just below the Hagedorn temperature.</span> <span data-covers="section-1-p2">Earlier work built such string stars in AdS$_{d+1}$ for $d>2$.</span> <span data-covers="section-1-p3 section-1-p6">This paper continues with two separate findings: string stars in AdS$_3$ with mixed RR and NS-NS flux, with a possible BTZ/string transition, and new “winding-string gas” saddles in confining holographic backgrounds.</span></p>
<p><span data-covers="sec-eft-p3 sec-eft-p7">An effective theory couples the wound string's field $\chi$ to supergravity. The winding mass depends on the local size of the thermal circle, which the condensate itself shrinks, so gravity binds it.</span> <span data-covers="sec-finite_RR-p1 sec-finite_RR-p5">Flat space with two spatial dimensions has no string star, but in thermal AdS$_3$ the thermal circle grows away from the centre, so the winding mass rises and confines the condensate.</span> <span data-covers="sec-finite_RR-p2">With finite RR flux the star resembles its higher-dimensional cousins, with size $L\sim\sqrt{l_sl_{ads}}\,(1-\lambda^2)^{-1/4}$, where $\lambda$ is the NS-NS fraction of the flux.</span> <span data-covers="sec-thermo-p2 sec-finite_RR-p3">Its free energy is positive, so it is subdominant to thermal AdS$_3$ and to the BTZ black hole.</span></p>
<p><span data-covers="sec-finite_RR-p4 sec-small_RR_anal-p1">As the RR flux decreases the star grows, reaching the AdS radius when $1-\lambda^2\sim\alpha'/l_{ads}^2$; its back-reaction on the metric, dilaton and NS-NS flux then enters at leading order.</span> <span data-covers="sec-small_RR_anal-p3">For pure NS-NS flux the winding mass is constant out to the boundary, because the flux's electric repulsion cancels the growing thermal circle, as for long strings.</span> <span data-covers="section-4.2-p1 sec-higher_curv-p1">The Hagedorn temperature, $R_c^2=2/k-1/k^2$ with $k=l_{ads}^2/\alpha'$, then matches the exact worldsheet result, and curvature corrections to the winding mass, naively as large, vanish.</span> <span data-covers="fig-lengthscale fig-free_energy sec-small_RR_num-p5">Numerically, these AdS-sized stars grow with temperature, and their positive free energy falls to zero at the Hagedorn temperature.</span></p>
<p><span data-covers="sec-thermo-p3 sec-thermo-p4">In higher dimensions the AdS string star can be matched to small AdS black holes, which heat up as they shrink. Small BTZ black holes instead grow colder, so the AdS$_3$ string star cannot meet them.</span> <span data-covers="sec-thermo-p4">The clue is symmetry: thermal AdS$_3$ breaks the winding symmetry of the angular circle, the BTZ that of the thermal circle, and the string star both.</span> <span data-covers="sec-thermo-p5 fig-ads3_phase_diagram">Exchanging the circles maps the string star to an angular winding condensate on the BTZ near its own instability, $R_c'=1/R_c$, and the paper conjectures a line of saddles joining the two.</span> <span data-covers="section-1-p4">It admits that the evidence for this BTZ/string transition is much weaker than in higher dimensions.</span></p>
<p><span data-covers="sec-gen_disc-p1 sec-gen_disc-p2">Separately, the paper turns to confining backgrounds in which a non-thermal circle or sphere shrinks smoothly in the bulk: the D4 and D3 Witten models, Maldacena–Nuñez and Klebanov–Strassler.</span> <span data-covers="sec-gen_disc-p3 sec-gen_disc-p4">Just below the Hagedorn temperature a winding condensate forms at the tip, homogeneous along the boundary directions, with size $L\sim\sqrt{l_sl}$ set by the local curvature radius $l$: the “winding-string gas”.</span> <span data-covers="sec-gen_disc-p5 sec-gen_disc-p6">Its linear mode gives the Hagedorn temperature with its first curvature correction, $\beta_c=\sqrt{4\pi/T_{st}}\,\bigl(1-\tfrac{d}{2\sqrt2}\,l_s/l\bigr)$, where $T_{st}$ is the confining string tension and $S^{d-1}$ the shrinking sphere.</span> <span data-covers="sec-d4_back-p3 sec-mn_back-p2 sec-ks_back-p2">The correction raises the temperature, and the paper evaluates it for each model.</span></p>
<p><span data-covers="sec-d4_back-p5">The gas is highly metastable. The Witten models' phase diagram is very similar to that of AdS$_3$: exchanging $\beta$ and $2\pi R$ maps the thermal saddle to the black brane, which has its own winding instability.</span> <span data-covers="sec-d4_back-p5 fig-witten_model">The paper speculates a black brane/string transition, a line of metastable saddles from the black brane's winding condensate to the gas.</span> <span data-covers="sec-d4_back-p6">At weak coupling the D4 model is pure 3+1 Yang–Mills at low energies, and the simplest scenario has a single phase above its deconfinement transition that the exchange maps to itself.</span> <span data-covers="sec-d4_back-p7">The gas breaks both winding symmetries, so it is invariant under the exchange, and the paper argues it may continue into that deconfined phase.</span></p>
<p><span data-covers="section-1-p7 sec-eft-p5">All solutions are at leading order in $\alpha'$ and in the condensate, so they hold only near the Hagedorn temperature. Neither conjectured line of saddles is constructed: that would need the whole string spectrum.</span> <span data-covers="fig-ads3_phase_diagram">At small but finite $g_s$, one-loop effects take over close enough to the Hagedorn temperature.</span> <span data-covers="sec-small_RR_num-p1">The pure NS-NS numerics use a small RR flux as a regulator.</span> <span data-covers="section-1-p7 sec-finite_RR-p2">Open are the string star exact in $\alpha'$ for pure NS-NS flux, a comparison with integrability for pure RR flux, and tests of the confining predictions at weak coupling.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the author; not shown to readers).
FLAGS = [
    {"node": "sec-d4_back-p3", "note": r"(3.20): the second term is written $-\frac{27\pi^2}{\sqrt2\,(\lambda_5/R)^{-1}}$, i.e. growing as $(\lambda_5/R)^{+1}$. From (3.19) with $M_{gb}=1/R$ and $T_{st}=\lambda_5/(27\pi^2R^3)$ I get $-\frac{27\pi^2}{\sqrt2}(\lambda_5/R)^{-1}$, which also fits the stated $O((\lambda_5/R)^{-3/2})$ remainder. Is the exponent's sign a typo?"},
    {"node": "sec-d4_back-p5", "note": r"(3.21): the two forms of $\beta_c'$ do not seem to agree. With $T_{st}=\frac{4}{27\pi\alpha'}(R_{D4}/R)^3$ and $M_{gb}=1/R$, $2^{4/3}\pi(T_{st}M_{gb}^{-5})^{1/3}=\frac{4\pi^{2/3}}{3}R_{D4}(R^2/\alpha')^{1/3}$, not $\frac{4\pi}{3}R_{D4}(R^2/\alpha')^{1/3}$. Also, (3.22)'s $\beta_c'/R=\frac23(\pi^2\lambda_5/R)^{1/3}$ follows from a tip circle of radius $R_H=\sqrt{2\alpha'}$, i.e. $\frac{4\pi}{3}R_{D4}(R^2/2\alpha')^{1/3}$, a factor $2^{-1/3}$ from the first form. Which is intended? The layers quote neither."},
    {"node": "sec-higher_curv-p1", "note": r"The change of variables reads $-4m^2=s^2+\frac14$, but going from (4.18) to (4.19) needs $s^2+\frac14=-m^2/4$ (also the usual AdS$_3$ relation $m^2=4j(j-1)$). Typo? The conclusion $\Delta m^2=0$ does not depend on it."},
    {"node": "sec-finite_RR-p1", "note": r"“the winding mass of order $m^2\sim l_{ads}/l_s^3$”: in the near-Hagedorn regime $m^2\sim(R_0^2-R_H^2)/\alpha'^2\sim1/(l_sl_{ads})$ (which is $1/L^2$). The conclusion, that the $O(l_{ads}^{-2})$ curvature shift is subleading, holds either way. Also the sentence “Following the previous section we will when small solutions $L\ll l_{ads}$ exist” has lost a word."},
    {"node": "sec-finite_RR-p3", "note": r"“$\zeta$ is negligible in (7)”: which equation is meant? Presumably (2.17)/(2.18) at $\rho\ll l_{ads}$, as argued in sec-finite_RR-p1."},
    {"node": "sec-mn_back-p2", "note": r"Footnote 12 says “in the case we are considering $g_sN\ll1$”, but sec-mn_back-p1 requires $1\ll g_sN\ll N$ for the weakly curved solution. With $\beta_c\approx2\pi\sqrt{2\alpha'/g_s}$, $\beta_{H,LST}\ll\beta_c$ needs $g_sN\ll1$, so the footnote's comparison seems to hold only outside the regime of the section. Which is intended? The layers do not mention little string theory."},
    {"node": "fig-example", "note": r"The caption labels both panels “(left)”; the second is presumably “(right)”. The caption of fig-free_energy calls $a=0.1$ “the pure NS-NS theory”; per sec-small_RR_num-p1, $a=0.1$ stands in for it as a regulator. The layers say so."},
    {"node": "sec-small_RR_anal-p2", "note": r"(4.6) has “$m^2_\text{eff}\rho\,|\hat\chi|^2$”, presumably $m^2_\text{eff}(\rho)|\hat\chi|^2$. And sec-small_RR_num-p3 calls $\hat\chi_\text{lin}$ “found numerically above”, while for $a=0$ it was found analytically (4.13). Minor."},
    {"node": "section-1-p4", "note": r"The summary grounds “the evidence is much weaker than in higher dimensions” on the introduction, the only place the paper says it; the body (fig-ads3_phase_diagram, “hypothetical line”) is consistent. Drafter's choice, flagged for the author."},
]
