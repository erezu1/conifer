"""The drafted layers of arXiv:2510.17951 (A spin on Hagedorn temperatures and string stars).

Drafted by an AI reader from the paper's text; nothing here has been checked by the authors yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs. <span data-covers="..."> marks what a sentence of a summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2510.17951 · hep-th · October 2025"
DATE = "20 October 2025"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "Hagedorn temperatures and rotating string stars"
# The headline is the exact Hagedorn temperature (1.2) for all three string theories, readable with nu alone.
# Figure 1 is the paper's own summary of the rotating black hole/string star correspondence.
KEY = {"equation": "eq-hag_flat_final", "figure": "fig-schem_intro"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on string stars, Hagedorn physics or the black hole/string transition"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows string theory and black hole thermodynamics in outline"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory, general relativity and a first course on strings"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (section-1-p2 to p5).
# The interpretation of the star as a bound state of rotating strings (abstract) and the hope that it describes the
# rotating black hole at string size (section-1-p2) are why the results matter, not further results.
# How they relate, from the paper's own words: the Hagedorn temperature (A) is re-derived from a target-space EFT
# (subsec-Atick_W-p1), the string star is a saddle of that EFT with gravity (sec-sss-p2), the correspondence is
# argued for that saddle (sec-corr-p3), and the AdS section generalises the analysis (sec-ads-p1). Every step
# builds on another, so the paper is one argument; the AdS comments are a separate section, kept in the same theme
# because the paper presents them as the extension of the same analysis.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-hagedorn", "headline": True,
     "claim": r"At fixed imaginary angular velocity $\nu$ free strings still have a Hagedorn instability, because the lightest winding mode on the twisted thermal circle turns tachyonic; this gives the exact $\beta_H(\nu)$ for bosonic, type II and heterotic strings, confirmed by counting states.",
     "quote": "we show that free strings exhibit a Hagedorn instability due to a thermal-winding mode turning tachyonic",
     "where": ["subsec-euc_hag-p5", "subsec-euc_hag-p9", "subsec-euc_hag-p11"], "theme": "A"},
    {"id": "c-eft",
     "claim": r"Reduced on the thermal circle, the twisted background is a Melvin flux tube, and a novel $\nu$-dependent effective theory of the winding mode, with a universal confining mass term, reproduces the $O(\nu)$ shift of the Hagedorn temperature.",
     "quote": "effective field theory (EFT) for the thermal winding mode",
     "where": ["subsec-Atick_W-p4", "subsec-Atick_W-p6"], "theme": "A",
     "builds_on": "c-hagedorn", "link_quote": "We would like to explain the results of the previous section also from a target space perspective"},
    {"id": "c-star", "headline": True,
     "claim": r"Perturbatively in $\nu$, that effective theory coupled to gravity has a normalizable winding condensate for $3\le d\le5$, a rotating string star: squashed by the rotation, with no intrinsic spin but an $O(G_N^{-1})$ angular momentum $J=\mathcal I\Omega$ given by the rigid-body moment of inertia, and Hagedorn entropy $S=\beta_HM$.",
     "quote": "we find a novel ‘rotating string star’ saddle",
     "where": ["subsec-eom_ss-p9", "subsec-grand_ss-p4", "subsec-micro_ss-p1"], "theme": "A",
     "builds_on": "c-eft", "link_quote": "we can look for saddles of the EFT derived in the previous section, together with gravity"},
    {"id": "c-corr",
     "claim": r"Extrapolated to their crossover regimes, the rotating string star qualitatively matches rotating black holes and rotating free strings: at leading order in the rotation their angular momentum and eccentricity agree in scaling and sign; subleading differences are scheme dependent.",
     "quote": "the saddle is qualitatively shown to interpolate between the rotating strings phase and a rotating black hole",
     "where": ["subsec-black-hole-string-star-corr-p4", "subsec-black-hole-string-star-corr-p5", "subsec-corr_free_strings-p2"], "theme": "A",
     "builds_on": "c-star", "link_quote": "we discuss the extension of the correspondence arguments to the rotating string star saddle"},
    {"id": "c-ads",
     "claim": r"In AdS the winding mode stays stable at real angular velocity below the unitarity bound, the leading $l_s/l_{ads}$ correction to the Hagedorn temperature is computed at real and imaginary rotation, type II strings in pure NS-NS AdS$_3$ have an exact $R_H(\nu)$ equal to flat space's for $k|\nu|>1$, and the rotating AdS string star is estimated.",
     "quote": "We also comment on the implications of these results for anti-de Sitter space",
     "where": ["section-5.1-p4", "section-5.1-p8", "section-5.2-p3"], "theme": "A",
     "builds_on": "c-hagedorn", "link_quote": "we generalize the analysis from flat space to anti-de Sitter space"},
]

# Every version states the four contributions the abstract claims (c-hagedorn, c-star, c-corr, c-ads); c-eft,
# claimed only in the introduction, is in the summary and not in the gist (skill section 3).
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">Does a string-size black hole become a self-gravitating “string star” when it rotates?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-hagedorn"><span data-covers="subsec-euc_hag-p5 subsec-euc_hag-p9 subsec-euc_hag-p11">At imaginary angular velocity $\nu$, a thermal winding mode turns tachyonic, giving exact Hagedorn temperatures $\beta_H(\nu)$ for bosonic, type II and heterotic strings.</span></li>
  <li data-claims="c-star"><span data-covers="subsec-eom_ss-p5 subsec-eom_ss-p9 subsec-grand_ss-p4">A “rotating string star” saddle, found numerically to order $\nu^2$ for $3\le d\le5$, rotates rigidly with $O(1/G_N)$ angular momentum.</span></li>
  <li data-claims="c-corr"><span data-covers="subsec-black-hole-string-star-corr-p4 subsec-corr_free_strings-p2">Extrapolated, its angular momentum and eccentricity match rotating black holes' and free strings' up to $O(1)$ factors: a qualitative interpolation.</span></li>
  <li data-claims="c-ads"><span data-covers="section-5.1-p4 section-5.1-p5">In AdS, the Hagedorn temperature's leading $l_s/l_{ads}$ shift is computed at real or imaginary rotation.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p2">The rotating star is offered as what a rotating black hole becomes at string size.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">Horowitz–Polchinski string stars qualitatively match black holes at the string scale; does this survive a twist $\nu$ of the thermal circle (imaginary angular velocity)?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-hagedorn"><span data-covers="subsec-euc_hag-p5 subsec-euc_hag-p9 subsec-euc_hag-p11">The lightest winding mode turns tachyonic at an exact $R_H(\nu)$: $R_H^2/\alpha'=4-2|\nu|+2\nu^2$ (bosonic), $2-2|\nu|$ (type II), heterotic the average of the two radii.</span></li>
  <li data-claims="c-star"><span data-covers="subsec-eom_ss-p5 subsec-eom_ss-p7 subsec-eom_ss-p9">To order $\nu^2$ the Horowitz–Polchinski star, found numerically for $3\le d\le5$, gains a quadrupole that squashes it,</span> <span data-covers="subsec-grand_ss-p4">and rotates rigidly, $J=\mathcal I\Omega$.</span></li>
  <li data-claims="c-corr"><span data-covers="subsec-black-hole-string-star-corr-p1 subsec-black-hole-string-star-corr-p4 subsec-corr_free_strings-p2">Extrapolated, its $J$ and eccentricity match Myers–Perry black holes and rotating free strings at leading order, up to $O(1)$ factors;</span> <span data-covers="subsec-black-hole-string-star-corr-p5">its mass and entropy shifts have the opposite sign to the black hole's, which the paper argues is scheme dependent.</span></li>
  <li data-claims="c-ads"><span data-covers="section-5.1-p4">In AdS at real angular velocity $\Omega$, $R_H/l_s=\sqrt2-\frac{l_s}{2l_{ads}}(d-2+2\sqrt{1-\Omega^2})+O(\alpha'/l_{ads}^2)$.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p2">The rotating string star is proposed as the string-scale rotating Euclidean black hole, extending the correspondence's evidence to angular momentum.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">Very hot, string-size black holes may turn into “string stars”, balls of strings held by their own gravity. Does this work when they spin?</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-hagedorn"><span data-covers="subsec-euc_hag-p5 subsec-euc_hag-p9 subsec-euc_hag-p11">With an imaginary rotation $\nu$, strings wrapped around Euclidean time become unstable above an exact maximal (Hagedorn) temperature, for bosonic, type II and heterotic strings.</span></li>
  <li data-claims="c-star"><span data-covers="subsec-ss_eft-p1 subsec-eom_ss-p9 subsec-grand_ss-p4">A slowly rotating string star is found numerically, spinning like a rigid body.</span></li>
  <li data-claims="c-corr"><span data-covers="subsec-black-hole-string-star-corr-p4 subsec-corr_free_strings-p2">The star's rotation and flattening roughly match rotating black holes and free strings, linking the two.</span></li>
  <li data-claims="c-ads"><span data-covers="section-5.1-p4 section-5.1-p5">In anti-de Sitter space, the curvature's leading correction to that temperature is computed.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p2">The rotating star could be what a rotating black hole becomes at string size.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="sec-sss-p1 sec-corr-p1">A Euclidean black hole is described by Einstein gravity only while its inverse temperature $\beta$ is much larger than the string length $l_s$. Near the Hagedorn temperature, Horowitz and Polchinski proposed that it becomes a “string star”, a self-gravitating condensate of strings wound on the thermal circle, whose thermodynamics qualitatively matches the black hole's.</span> <span data-covers="section-1-p2 subsec-grand_can-p2">The paper adds angular momentum. It fixes an imaginary angular velocity $\nu$, with $\beta\Omega=2\pi i\nu$, the ensemble in which the rotating Euclidean black hole is real.</span> <span data-covers="subsec-euc_hag-p9 subsec-eom_ss-p9 subsec-black-hole-string-star-corr-p4">Free strings then still have a Hagedorn temperature, now depending on $\nu$; a rotating string star exists; and it qualitatively matches rotating black holes and rotating strings.</span> <span data-covers="section-1-p2">So the string star remains a candidate description of the rotating black hole at string size.</span></p>
<p><span data-covers="subsec-grand_can-p1 subsec-grand_can-p3">Real angular velocity makes a flat-space ensemble diverge, as low-energy states can carry any angular momentum; imaginary $\nu$ turns that weight into a phase.</span> <span data-covers="subsec-euc_hag-p2 subsec-euc_hag-p3">In Euclidean time the ensemble is flat space in which going once around the thermal circle rotates a plane by $2\pi\nu$, a Melvin space.</span> <span data-covers="subsec-euc_hag-p5 subsec-euc_hag-p9">The twist shifts the oscillator frequencies of strings wound on the circle, and the lightest wound string turns massless at $R_H^2/\alpha'=4-2|\nu|+2\nu^2$ (bosonic) or $2-2|\nu|$ (type II), with $R_H=\beta_H/2\pi$.</span> <span data-covers="subsec-euc_hag-p11">For heterotic strings $R_H$ is the average of these two radii.</span> <span data-covers="subsec-grand_can-p4 app-hagedorn_temps-p5">Counting free-string states gives the same temperatures.</span> <span data-covers="subsec-euc_hag-p9">At $\nu=1$ the superstring trace becomes the supersymmetric index, where no instability is expected.</span></p>
<p><span data-covers="subsec-Atick_W-p2 subsec-Atick_W-p4">Reduced on the thermal circle, the twist becomes a Kaluza–Klein magnetic flux tube, and the winding mode gains a universal mass term growing as $\nu^2\rho^2$ away from the rotation axis.</span> <span data-covers="subsec-Atick_W-p6">Its lowest state is a Gaussian in the rotation plane, whose energy reproduces the $O(\nu)$ shift of the Hagedorn temperature in all three theories.</span> <span data-covers="subsec-Atick_W-p4">At real angular velocity the same term is negative: the Euclidean face of the flat-space divergence.</span> <span data-covers="subsec-Atick_W-p7">The effective theory holds only for $|\nu|\ll1$, where the Gaussian's width $\sqrt{\alpha'/|\nu|}$ exceeds the string length.</span></p>
<p><span data-covers="sec-sss-p2 subsec-ss_eft-p5">Close to $R_H(\nu)$ the winding mode is light, so the paper couples it to gravity and the dilaton and seeks a normalizable condensate.</span> <span data-covers="subsec-eom_ss-p4 subsec-eom_ss-p5">Treating $\nu$ as a perturbation of the Horowitz–Polchinski solution, which exists for $3\le d\le5$ spatial dimensions, it solves the equations numerically to order $\nu^2$.</span> <span data-covers="subsec-eom_ss-p9 subsec-eom_ss-p10">Rotation adds a quadrupole, making the star prolate at imaginary $\nu$ and oblate once continued to real $\Omega$, like a slowly rotating Newtonian gas.</span> <span data-covers="subsec-ss_eft-p1 subsec-grand_ss-p4">The profile keeps the background's rotational symmetry and so has no intrinsic spin. Yet the star carries angular momentum of order $1/G_N$, $J=\mathcal I\Omega$, with $\mathcal I$ the Newtonian moment of inertia of its mass density.</span> <span data-covers="subsec-grand_ss-p3 subsec-micro_ss-p1">The Hagedorn relation $S=\beta_HM$ still holds, and at fixed mass angular momentum lowers the entropy, since energy is spent on rotation.</span></p>
<p><span data-covers="subsec-black-hole-string-star-corr-p3 subsec-black-hole-string-star-corr-p4">Slowly rotating Myers–Perry black holes and the star, both extrapolated to $\beta\sim l_s$, are expanded in $l_s\Omega$. Their angular momentum and eccentricity, the only quantities shifted at leading order, agree up to order-one factors and in sign: both rotate along $\Omega$ and flatten.</span> <span data-covers="subsec-black-hole-string-star-corr-p5">At subleading order mass and entropy rise with $\Omega$ for the star but fall for the black hole; moving the crossover point reverses this, so the paper calls such effects scheme dependent.</span> <span data-covers="subsec-corr_free_strings-p1 subsec-corr_free_strings-p2">On the other side, rotating free strings become self-gravitating at a breakdown mass, and there their angular velocity and eccentricity match the star's in $g_s$-scaling and sign.</span></p>
<p><span data-covers="section-5.1-p2 section-5.1-p4">In AdS the curvature confines the winding mode, so real angular velocities below the unitarity bound are stable, and the leading $l_s/l_{ads}$ shift of the Hagedorn temperature follows at real or imaginary rotation.</span> <span data-covers="section-5.1-p8">For type II strings in pure NS-NS AdS$_3$, an exact $R_H(\nu)$ agrees with flat space for $k|\nu|>1$, where the paper reads a switch from long to short strings.</span> <span data-covers="section-5.2-p1 section-5.2-p3">Small AdS string stars and black holes look like flat-space ones, so the rotating correspondence is expected to carry over; the rotating AdS star is estimated, not solved.</span></p>
<p><span data-covers="subsec-eom_ss-p4 subsec-black-hole-string-star-corr-p6">Everything is perturbative in the rotation, so the regime $l_s\Omega\sim1$, where the crossover point itself moves, is out of reach.</span> <span data-covers="sec-sss-p5">Only bosonic and type II stars are constructed; heterotic ones are believed similar.</span> <span data-covers="sec-corr-p1 subsec-black-hole-string-star-corr-p3">The matches extrapolate both saddles to where neither is reliable, so they are qualitative.</span> <span data-covers="section-4.3-p2 section-4.3-p3">Large angular momentum, up to the Regge bound, is left to speculation, such as a “stringy pancake” of near-extremal strings.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "subsec-eom_ss-p12", "note": r"(3.21) gives $e=\sqrt{2(c_\perp-c_{||})}\,|\nu|/(\alpha'm_0^2)$, imaginary for real $\nu$ since Table 1 has $c_\perp<c_{||}$; is it meant after continuing $\nu=-iR\Omega$? Continuing it and using (3.30) gives $\sqrt{2(c_{||}-c_\perp)}$ in (3.36), where the paper has $\sqrt{\kappa(c_{||}-c_\perp)}$, an extra factor $R_H/l_s$. Which is intended?"},
    {"node": "subsec-corr_free_strings-p2", "note": r"In (4.12) and (4.13) the entropy correction is written $g_s^{8/(d-6)}J^2$ but the size corrections $g_s^{8/(6-d)}J^2$, and the text calls the perturbative parameter $g_s^{4/(d-6)}J$, while $e\sim g_s^{-4/(d-6)}J$. At $l_sM\sim g_s^{4/(d-6)}$, $J/(l_sM)\sim g_s^{4/(6-d)}J$; are the exponents in the entropy and in the stated parameter sign-flipped?"},
    {"node": "subsec-black-hole-string-star-corr-p5", "note": r"Setting $r_h=l_s$ in (4.5) gives $\beta_{corr}=\frac{4\pi l_s}{d-2}(1+\dots)$; the text has $\frac{4l_s}{d-2}$. Is a $\pi$ missing?"},
    {"node": "app-J-M-free-string-p6", "note": r"(A.39) is a correction to $L_{||}^2$; with (A.41) and (A.42) it gives $L_{||}^2\propto1+\frac{12J^2}{5(l_sM)^2}$, so $L_{||}\propto1+\frac{6J^2}{5(l_sM)^2}$, while (A.43) and (2.9) put $12/5$ in $L_{||}$ itself (and (2.10) follows from it). Also the $L_\perp$ correction is $O(J^2/M)$ in (A.43) but $O(J^2/M^3)$ in (2.9). The layers quote neither coefficient."},
    {"node": "subsec-grand_can-p4", "note": r"(2.16) writes $Z(b,\nu)=\exp(-\frac{2\pi^2}{b}a(\nu)+\dots)$, which decays at small $b$; (A.2) has the growing $+\frac{2\pi^2}{b}a(\nu)$. Also the text uses $\alpha'M^2=N/4$ (and $M^2\approx N/4$ in (A.40)), while the mass shell (2.25) gives $\alpha'M^2\approx4N$ and A.2 uses $N\sim M^2/4$. Typos?"},
    {"node": "sec-sss-p4", "note": r"The first line of (3.1) has $(d\phi+\nu dt)^2$, the second line and (2.43) $(d\phi-\nu dt)^2$."},
    {"node": "app-hagedorn_temps-p6", "note": r"Appendix A.1 calls the supersymmetric heterotic side the right-movers and the bosonic side the left-movers; subsec-euc_hag-p10 has them the other way round. The layers say “bosonic side” and “supersymmetric side”."},
]
