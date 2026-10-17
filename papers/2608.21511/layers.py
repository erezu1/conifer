"""The drafted layers of arXiv:2608.21511 (String stars, small black holes, and the supersymmetric index).

Drafted by an AI reader from the paper's text; nothing here has been checked by the author yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2608.21511 · hep-th · August 2026"
DATE = "21 August 2026"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "String stars and the supersymmetric index"
# The equation carries the paper's mechanism in one line (the W mass lowered by the twist, tachyonic below R_H(nu)),
# readable with R and nu alone. The charged entropy (4.18) was considered: it is the closer match to the headline,
# but its line also carries the seed temperature and the boosts, which cannot be read without section 4.
KEY = {"equation": "eq-W_gs_mass", "figure": "fig-transition"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on string stars, black hole microstates or the index"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows string theory and black hole thermodynamics in outline"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory and a first course on strings"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction's list (section-1-p4 to p7).
# The tension with a BPS small black hole (abstract's last sentence, section-1-p6 "Thus, we argue") is drawn from the
# decoupling results, so it is listed as why they matter, not as a contribution.
CONTRIBUTIONS = [
    {"id": "c-eft", "headline": True,
     "claim": r"Near the heterotic index the Atick–Witten effective theory is replaced by a Higgsed $SU(2)_L\times U(1)_R$ supergravity in which the winding mode is the W boson, and the Hagedorn instability appears as Ambjørn–Olesen condensation of that W boson in the magnetic field set by the rotation.",
     "quote": "a new high-temperature description emerges near the index",
     "where": ["subsec-worldsheet-p5", "subsec-mag_spectrum-p4", "subsec-electroweak-p2"]},
    {"id": "c-wstar", "headline": True,
     "claim": r"Slightly off the index the W boson forms a self-gravitating condensate, the “W star”, similar to the Horowitz–Polchinski string star and very likely on the same family; it decouples at the index, as the weakly curved (rotating) black hole does.",
     "quote": "a string star solution is found, similar to the Horowitz-Polchinski solution, but decouples at the index",
     "where": ["sec-W_star_prop-p3", "sec-W_star_prop-p4", "subsec-bh_w_trans-p7"]},
    {"id": "c-charged",
     "claim": r"Charged W stars appear to interpolate between charged rotating black holes and the free string phase and approach the microscopic index, unlike a naive continuation of the charged black hole; exactly at the index both the charged black hole and the charged W star decouple.",
     "quote": "the string star appears to interpolate between charged black holes and the free string phase",
     "where": ["subsec-charged_w_stars-p3", "subsec-charged_w_stars-p6", "subsec-charged_w_stars-p7"]},
    {"id": "c-typeii",
     "claim": r"For type II a tower of winding strings becomes light near the index, opening a dimension in the T-dual picture, and the paper argues that string stars with properties similar to the W star exist there and likewise decouple at the index.",
     "quote": "a tower of winding strings becomes light near the index",
     "where": ["subsec-ii_worldsheet-p2", "subsec-ii_eft_etc-p4", "subsec-ii_charged-p3"]},
    {"id": "c-bosonic",
     "claim": r"For bosonic strings the black hole free energy has a kink in the imaginary rotation that the string star's lacks: a possible issue for the black hole/string transition, which the paper leaves open.",
     "quote": "explain a possible issue with the black hole/string transition",
     "where": ["sec-bosonic-p2", "sec-bosonic-p3"]},
]

# Every version states the four contributions the abstract claims (c-eft, c-wstar, c-typeii, c-charged); c-bosonic,
# claimed only in the introduction, is in the summary and not in the gist (skill section 3).
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">Do string-scale black holes become self-gravitating “string stars”? The exact supersymmetric index $\beta\Omega=2\pi i$ could tell.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-eft"><span data-covers="subsec-worldsheet-p5 subsec-worldsheet-p7">Near the heterotic index a Higgsed $SU(2)_L\times U(1)_R$ supergravity replaces Atick–Witten;</span> <span data-covers="subsec-mag_spectrum-p4 subsec-electroweak-p2">the Hagedorn instability is its winding W boson's Ambjørn–Olesen condensation in a magnetic field.</span></li>
  <li data-claims="c-wstar"><span data-covers="sec-W_star_prop-p3">W-boson condensates, “W stars”, resemble Horowitz–Polchinski stars</span> <span data-covers="sec-W_star_prop-p4 subsec-bh_w_trans-p7">but decouple at the index, growing until no reliable regime remains.</span></li>
  <li data-claims="c-typeii"><span data-covers="subsec-ii_worldsheet-p2 subsec-ii_eft_etc-p2">Type II's light winding tower opens a T-dual dimension;</span> <span data-covers="subsec-ii_eft_etc-p4 subsec-ii_charged-p3">its similar string star also decouples.</span></li>
  <li data-claims="c-charged"><span data-covers="subsec-charged_w_stars-p2 subsec-charged_w_stars-p5">Charged string stars appear to link charged black holes to free strings;</span> <span data-covers="subsec-charged_w_stars-p6">at the index both decouple.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p6 sec-discussion-p3">This suggests tension between a smooth black hole/string transition and a proposed BPS small black hole.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">Do string-scale black holes become Horowitz–Polchinski stars? The two are never reliable together; the half-BPS index $\beta\Omega=2\pi i$ is known exactly.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-eft"><span data-covers="subsec-worldsheet-p5 subsec-worldsheet-p7">Near the heterotic index Atick–Witten fails and a Higgsed $SU(2)_L\times U(1)_R$ supergravity takes over, its W boson the winding mode;</span> <span data-covers="subsec-mag_spectrum-p4 subsec-electroweak-p2 subsec-electroweak-p3">in the Melvin field its mass $m^2=(R-1/R)^2-2\nu/R^2$ turns tachyonic near $R=1$: Ambjørn–Olesen condensation.</span></li>
  <li data-claims="c-wstar"><span data-covers="sec-W_star_prop-p1 sec-W_star_prop-p3">W stars exist for $2<d<6$ with $I\sim m^{6-d}/(G_N\nu\log(\nu/m^2))$, Horowitz–Polchinski up to the logarithm,</span> <span data-covers="subsec-bh_w_trans-p7">and, like weakly curved black holes, decouple at the index.</span></li>
  <li data-claims="c-typeii"><span data-covers="subsec-ii_worldsheet-p2 subsec-ii_eft_etc-p2">For type II a light winding tower opens a T-dual dimension</span> <span data-covers="subsec-ii_eft_etc-p4 subsec-ii_charged-p3">with a similar string star that also decouples.</span></li>
  <li data-claims="c-charged"><span data-covers="subsec-charged_w_stars-p1 subsec-charged_w_stars-p3">Charged W stars have $S_\nu\approx2\pi\sqrt{M^2-Q_L^2}$, reaching $S_\text{micro}$ near BPS;</span> <span data-covers="subsec-charged_w_stars-p2 subsec-charged_w_stars-p5">they appear to interpolate between charged black holes and free strings,</span> <span data-covers="subsec-charged_w_stars-p6">and, like charged black holes, decouple at the index.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p6 sec-discussion-p3">This suggests a tension between a smooth black hole/string transition and the BPS small black hole of Chowdhury–Sen–Shanmugapriya–Virmani and Chen–Murthy–Turiaci.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">Do very hot black holes become self-gravitating “string stars”? The exact supersymmetric index could tell.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-eft"><span data-covers="subsec-worldsheet-p5 subsec-worldsheet-p7">Near the heterotic index Atick–Witten fails: the wound string becomes the W boson of a Higgsed $SU(2)$ supergravity,</span> <span data-covers="subsec-mag_spectrum-p4 subsec-electroweak-p2">condensing in a magnetic field (the Hagedorn instability).</span></li>
  <li data-claims="c-wstar"><span data-covers="sec-W_star_prop-p3">W-boson condensates, “W stars”, resemble Horowitz–Polchinski string stars</span> <span data-covers="sec-W_star_prop-p4 subsec-bh_w_trans-p7">but decouple at the index, growing arbitrarily large.</span></li>
  <li data-claims="c-typeii"><span data-covers="subsec-ii_worldsheet-p2 subsec-ii_eft_etc-p2">Type II's light wound strings open a T-dual dimension;</span> <span data-covers="subsec-ii_eft_etc-p4 subsec-ii_charged-p3">its similar string star also decouples.</span></li>
  <li data-claims="c-charged"><span data-covers="subsec-charged_w_stars-p2 subsec-charged_w_stars-p5">Charged stars appear to interpolate between charged black holes and free strings;</span> <span data-covers="subsec-charged_w_stars-p6">at the index both decouple.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p6 sec-discussion-p3">This suggests tension between a smooth black hole–string transition and a stringy two-charge BPS black hole.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="section-1-p1">In weakly coupled string theory, energies $1\ll l_sE\ll g_s^{-2}$ belong not to black holes but to highly excited strings with Hagedorn growth. Whether a black hole heated to the string scale becomes such a self-gravitating string, a “string star”, is an old question, hard to settle because the two descriptions are never reliable together.</span> <span data-covers="section-1-p2 subsec-setup-p1">The paper follows both to the half-BPS supersymmetric index, which an imaginary angular velocity $\beta\Omega=2\pi i$ reaches from the thermal ensemble. The index is exact and independent of temperature and coupling, so each phase can be compared with it.</span> <span data-covers="subsec-bh_w_trans-p7 subsec-charged_w_stars-p6">Weakly curved black holes and string stars, neutral or charged, all decouple there: their reliable regimes run off to infinite size or temperature.</span> <span data-covers="subsec-charged_w_stars-p8 sec-discussion-p3">So if the phases are connected, only BPS strings remain, against a recently proposed BPS small black hole.</span></p>
<p><span data-covers="subsec-worldsheet-p2 subsec-worldsheet-p3">The usual string star's effective theory fails at rotations of order one, because the twist opens string-scale gaps.</span> <span data-covers="subsec-worldsheet-p4 subsec-worldsheet-p5">Near the heterotic index the lightest winding state is instead a vector, massless at the self-dual radius: the W boson of an enhanced $SU(2)_L\times U(1)_R$, Higgsed by the circle's radius $R$.</span> <span data-covers="subsec-su2_sugra-p2 subsec-su2_sugra-p3">The paper writes this supergravity to all orders in the fields at two derivatives.</span> <span data-covers="subsec-setup-p3 subsec-mag_spectrum-p3">Off the index the twist $\nu$ acts as a magnetic field, which quantises the W's motion in the rotation plane into Landau levels spaced by order $\nu$.</span> <span data-covers="subsec-mag_spectrum-p4 subsec-worldsheet-p6">Through its spin one W mode drops below them, to $m^2=(R-1/R)^2-2\nu/R^2$, so it is tachyonic below $R_H(\nu)=1+\sqrt{\nu/2}+\dots$</span> <span data-covers="subsec-electroweak-p2">This Ambjørn–Olesen instability of electroweak W bosons is here the string's Hagedorn instability.</span></p>
<p><span data-covers="sec-w_stars-p3">Exactly at the index the effective action is positive, so no localised condensate exists.</span> <span data-covers="subsec-low_e_eft-p4 subsec-lower_E_EFT-p4">Slightly away, gravity and magnetic forces bind the W condensate into a “W star” in three to five spatial dimensions.</span> <span data-covers="sec-W_star_prop-p1">Its $S_\nu$ (the entropy at $\nu=1$, the exponent of the index at $\nu=0$) obeys $S_\nu=2\pi l_sE$: Hagedorn growth beside an index that has no Hagedorn temperature.</span> <span data-covers="sec-W_star_prop-p3">It scales like the Horowitz–Polchinski string star up to a logarithm, suggesting one family of string stars.</span> <span data-covers="sec-W_star_prop-p4 sec-W_star_prop-p5">Near the index it does not dissolve but decouples: at fixed temperature its size and action diverge, and at fixed energy its transition to free strings recedes to infinite energy.</span> <span data-covers="subsec-bh_w_trans-p4 subsec-bh_w_trans-p5">Rotating black holes decouple too, because their horizons diverge.</span></p>
<p><span data-covers="subsec-charged_setup-p1 subsec-charged_setup-p2 subsec-charged_setup-p4">Momentum and winding charges make the index non-trivial, with free-string entropy $S_\text{micro}=4\pi\sqrt{|Q_nQ_w|}$, and a classical duality adds them to any neutral saddle, exactly in $\alpha'$.</span> <span data-covers="subsec-charged_bh-p6 subsec-charged_bh-p7">Charged black holes reach the BPS bound only through string-scale curvature, and the reliable ones recede from it as the index nears.</span> <span data-covers="subsec-charged_w_stars-p1 subsec-charged_w_stars-p3">Charged W stars do better: near the heterotic index $S_\nu\approx2\pi\sqrt{M^2-Q_L^2}$, which approaches $S_\text{micro}$ close to the BPS bound.</span> <span data-covers="subsec-charged_w_stars-p5 subsec-charged_w_stars-p6">But only within a temperature window, between black-hole and free-string transitions, that closes at the index, so they decouple too.</span> <span data-covers="subsec-charged_w_stars-p7">At the free-string transition their size matches a typical BPS string's, suggesting a smooth passage to BPS strings.</span></p>
<p><span data-covers="subsec-ii_worldsheet-p2 subsec-ii_eft_etc-p2 subsec-ii_eft_etc-p4">For type II strings the winding mass vanishes only at zero radius, so near the index a tower of windings is light. T-dual, they are momentum modes in one more dimension, where a similar string star is argued to exist.</span> <span data-covers="subsec-ii_charged-p1 subsec-ii_charged-p2">Its charged entropy carries a factor $\sqrt\nu$ and seems to vanish at the index. That zero is an artifact of the order of limits: heavy strings at fixed twist are far from BPS, but those lighter than about $1/\nu$ are nearly BPS.</span> <span data-covers="sec-bosonic-p2 sec-bosonic-p3">For bosonic strings the black hole free energy has a kink in the rotation that the string star's lacks, an open tension.</span></p>
<p><span data-covers="subsec-lower_E_EFT-p1 sec-discussion-p5 subsec-ii_eft_etc-p4">The W star is built only far below the Landau spacing, and for type II its couplings are assumed, not derived.</span> <span data-covers="subsec-bh_w_trans-p6">The black hole comparison extrapolates both saddles to the string scale, where their divergences carry different powers of $\nu$.</span> <span data-covers="subsec-charged_w_stars-p8">Above all, the paper does not show that W stars and black holes are connected; if they are not, a small black hole could still contribute.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the author; not shown to readers).
FLAGS = [
    {"node": "subsec-lower_E_EFT-p3", "note": r"The text says the kernel is dominated at large distance by the Newtonian fall-off $G(r)\sim C_d/r^d$ and calls it marginal in $d-2$ dimensions; (3.18) gives $C_d/r^{d-2}$ at large $r$, which is the marginal fall-off in $d-2$ dimensions. The layers use $1/r^{d-2}$ (question q-d-minus-2); $r^d$ looks like a typo."},
    {"node": "subsec-worldsheet-p2", "note": r"“slightly above the Hagedorn temperature $R-R_H\ll1$” (also sec-w_stars-p1): $R>R_H$ is slightly below the Hagedorn temperature, as section-1-p3 says. The layers say “just below”."},
    {"node": "subsec-bh_w_trans-p1", "note": r"“extended for small zero angular velocity ($\beta\Omega 1$)” is garbled; presumably “small angular velocity ($\beta\Omega\ll1$)”."},
    {"node": "subsec-charged_bh-p5", "note": r"$\upbeta\sim\frac{D-2}{D-3}G_NQ_R/\tilde M$ lacks the prime that the parallel expression for $\upalpha$ has ($\tilde M'$)."},
    {"node": "fig-bps_limit", "note": r"The caption takes fixed and large charge $Q_R\gg\sqrt\nu$, while subsec-charged_w_stars-p5 needs $|Q|\gg1/\nu$ for the free-string end of the window. Unsure which is intended."},
    {"node": "fig-type_ii_spectrum", "note": r"The caption says the type II spectrum is tachyonic for any $\nu\ne1$ mod 2, but (5.2)-(5.3) make it tachyonic at small $R$ for $\nu\ne0$ (the index) and tachyonic at the thermal point $\nu=1$; compare the heterotic caption, “$\nu\ne0$ mod 2”. Probably a typo."},
    {"node": "fig-potential", "note": r"The caption puts the metastable W star at $\chi^2\sim1/\nu$; sec-W_star_prop-p4 has $\chi_0^2\sim m^2/\nu$. Consistent only at $m\sim1$; not used in the layers."},
    {"node": "subsec-charged_setup-p1", "note": r"Footnote 17: strictly the trace (2.1) vanishes at $\nu=0$ and the index is a helicity supertrace. The layers call it the index throughout and mention this once (definition of the index, question q-notation)."},
    {"node": "sec-W_star_prop-p1", "note": r"The paper gives no name to $S_\nu\equiv S+\beta\Omega J$; the layers write $S_\nu$ and describe it (the entropy at $\nu=1$, the exponent of the index at $\nu=0$) rather than invent one."},
]
