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

ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> Does a string-scale black hole become a self-gravitating “string star”? The supersymmetric index, at imaginary angular velocity $\beta\Omega=2\pi i$, gives a sharper test.</li>
<li><b>Result</b> Near the heterotic index the Hagedorn instability is Ambjørn–Olesen condensation of a W boson in a magnetic field, and string stars become “W stars”. Charged W stars approach the microscopic entropy $S_\text{micro}$ near the BPS bound, yet W stars and black holes all decouple at the index.</li>
<li><b>Why it matters</b> If the phases connect, only BPS strings remain, against a proposed small black hole.</li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> Near the half-BPS index $\beta\Omega=2\pi i$ the Atick–Witten EFT fails; for heterotic strings a Higgsed $SU(2)_L\times U(1)_R$ half-maximal supergravity takes over, written here to all orders in the fields at two derivatives.</li>
<li><b>Result</b> The winding mode is the W boson, tachyonic below $R_H(\nu)=1+\sqrt{\nu/2}+\dots$ by Ambjørn–Olesen condensation in the Melvin field. W stars exist in three to five spatial dimensions with $I\sim m^{6-d}/(G_N\nu\log(\nu/m^2))$, Horowitz–Polchinski up to the logarithm, and decouple at the index like Myers–Perry black holes. Charged, $S_\nu\approx2\pi\sqrt{M^2-Q_L^2}$ nears $S_\text{micro}$ close to BPS, but its reliable window closes at the index. For type II the zero-twist and large-mass limits do not commute, removing an apparent zero index.</li>
<li><b>Why it matters</b> If W stars and black holes connect, only BPS strings survive, against the small black hole saddles of Chowdhury–Sen–Shanmugapriya–Virmani and Chen–Murthy–Turiaci.</li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> Very heavy states in string theory are black holes or long excited strings. An old idea says a shrinking black hole becomes a ball of string held by its own gravity, a “string star”. The supersymmetric index, a temperature-independent count of special states, could test this.</li>
<li><b>Result</b> Near the index, a string wrapped around the imaginary-time circle acts like a W boson in a magnetic field. Its condensate, a “W star”, and the black hole both “decouple”: they grow without bound, so their contribution to the count falls to zero.</li>
<li><b>Why it matters</b> If the two are connected, only free strings remain, against a proposed small black hole.</li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="section-1-p1">In weakly coupled string theory, energies $1\ll l_sE\ll g_s^{-2}$ belong not to black holes but to highly excited strings with Hagedorn growth. Whether a black hole heated to the string scale becomes such a self-gravitating string, a “string star”, is an old question, hard to settle because the two descriptions are never reliable together.</span> <span data-covers="section-1-p2 subsec-setup-p1">The paper follows both to the half-BPS supersymmetric index, which an imaginary angular velocity $\beta\Omega=2\pi i$ reaches from the thermal ensemble. The index is exact and independent of temperature and coupling, so each phase can be compared with it.</span> <span data-covers="subsec-bh_w_trans-p7 subsec-charged_w_stars-p6">Weakly curved black holes and string stars, neutral or charged, all decouple there: their reliable regimes run off to infinite size or temperature.</span> <span data-covers="subsec-charged_w_stars-p8 sec-discussion-p3">So if the phases are connected, only BPS strings remain, against a recently proposed BPS small black hole.</span></p>
<p><span data-covers="subsec-worldsheet-p2 subsec-worldsheet-p3">The usual string star's effective theory fails at rotations of order one, because the twist opens string-scale gaps.</span> <span data-covers="subsec-worldsheet-p4 subsec-worldsheet-p5">Near the heterotic index the lightest winding state is instead a vector, massless at the self-dual radius: the W boson of an enhanced $SU(2)_L\times U(1)_R$, Higgsed by the circle's radius $R$.</span> <span data-covers="subsec-su2_sugra-p2 subsec-su2_sugra-p3">The paper writes this supergravity to all orders in the fields at two derivatives.</span> <span data-covers="subsec-setup-p3 subsec-mag_spectrum-p3">Off the index the twist $\nu$ acts as a magnetic field, which quantises the W's motion in the rotation plane into Landau levels spaced by order $\nu$.</span> <span data-covers="subsec-mag_spectrum-p4 subsec-worldsheet-p6">Through its spin one W mode drops below them, to $m^2=(R-1/R)^2-2\nu/R^2$, so it is tachyonic below $R_H(\nu)=1+\sqrt{\nu/2}+\dots$</span> <span data-covers="subsec-electroweak-p2">This Ambjørn–Olesen instability of electroweak W bosons is here the string's Hagedorn instability.</span></p>
<p><span data-covers="sec-w_stars-p3">Exactly at the index the effective action is positive, so no localised condensate exists.</span> <span data-covers="subsec-low_e_eft-p4 subsec-lower_E_EFT-p4">Slightly away, gravity and magnetic forces bind the W condensate into a “W star” in three to five spatial dimensions.</span> <span data-covers="sec-W_star_prop-p1">Its $S_\nu$ (the entropy at $\nu=1$, the exponent of the index at $\nu=0$) obeys $S_\nu=2\pi l_sE$: Hagedorn growth beside an index that has no Hagedorn temperature.</span> <span data-covers="sec-W_star_prop-p3">It scales like the Horowitz–Polchinski string star up to a logarithm, suggesting one family of string stars.</span> <span data-covers="sec-W_star_prop-p4 sec-W_star_prop-p5">Near the index it does not dissolve but decouples: at fixed temperature its size and action diverge, and at fixed energy its transition to free strings recedes to infinite energy.</span> <span data-covers="subsec-bh_w_trans-p4 subsec-bh_w_trans-p5">Rotating black holes decouple too, because their horizons diverge.</span></p>
<p><span data-covers="subsec-charged_setup-p1 subsec-charged_setup-p2 subsec-charged_setup-p4">Momentum and winding charges make the index non-trivial, with free-string entropy $S_\text{micro}=4\pi\sqrt{|Q_nQ_w|}$, and a classical duality adds them to any neutral saddle, exactly in $\alpha'$.</span> <span data-covers="subsec-charged_bh-p6 subsec-charged_bh-p7">Charged black holes reach the BPS bound only through string-scale curvature, and the reliable ones recede from it as the index nears.</span> <span data-covers="subsec-charged_w_stars-p1 subsec-charged_w_stars-p3">Charged W stars do better: near the heterotic index $S_\nu\approx2\pi\sqrt{M^2-Q_L^2}$, which approaches $S_\text{micro}$ close to the BPS bound.</span> <span data-covers="subsec-charged_w_stars-p5 subsec-charged_w_stars-p6">But only within a temperature window, between black-hole and free-string transitions, that closes at the index, so they decouple too.</span> <span data-covers="subsec-charged_w_stars-p7">At the free-string transition their size matches a typical BPS string's, suggesting a smooth passage to BPS strings.</span></p>
<p><span data-covers="subsec-ii_worldsheet-p1 subsec-ii_worldsheet-p2 subsec-ii_eft_etc-p2">For type II strings the winding mass vanishes only at zero radius, so near the index a tower of windings is light. T-dual, they are momentum modes in one more dimension, where a similar string star is argued to exist.</span> <span data-covers="subsec-ii_charged-p1 subsec-ii_charged-p2">Its charged entropy carries a factor $\sqrt\nu$ and seems to vanish at the index. That zero is an artifact of the order of limits: heavy strings at fixed twist are far from BPS, but those lighter than about $1/\nu$ are nearly BPS.</span> <span data-covers="sec-bosonic-p2 sec-bosonic-p3">For bosonic strings the black hole free energy has a kink in the rotation that the string star's lacks, an open tension.</span></p>
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
