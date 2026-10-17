"""The drafted layers of arXiv:2406.14605 (Aharony and Urbach, On type II string theory on AdS3 x S3 x T4 and
symmetric orbifolds).

Drafted by an AI reader from the paper's text, following skill/conifer-draft.md; nothing here has been checked by
the authors yet, so every rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md.
Equations are not nodes in this paper's skeleton, so the grounding spans name paragraphs. Math is TeX between $
signs. <span data-covers="..."> marks the paragraphs that establish a sentence of a summary.
"""
from layers_gists import GIST          # one line per paragraph, figure and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2406.14605 · hep-th · June 2024"
DATE = "20 June 2024"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the author.")
PAGE_TITLE = "Strings on AdS3 and symmetric orbifolds"
# The headline result is the exponentiation (3.12). Figure 1 (the N=30 moduli slice) illustrates the review and
# section 5, not the genus expansion, so it is left out of KEY.
KEY = {"equation": "eq-grand_Z"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on AdS3/CFT2, the tensionless string or symmetric orbifolds"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist who knows AdS/CFT in outline"},
    {"key": "student", "label": "Student", "hint": "knows QFT, a first course on strings and the basics of AdS/CFT"},
]

ROOT_STATUS = "ai-draft"

ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> With one unit of NS5-brane flux, strings on $AdS_3\times S^3\times T^4$ match the free symmetric orbifold of $N$ tori, yet were suggested to describe an ensemble over $N$.</li>
<li><b>Result</b> Orbifold correlators are sums over covering surfaces, the worldsheets. Summed over $N$ with weight $p^N$, these exponentiate into connected covers: an exact all-genus string expansion, $g_s^{-2}\propto p$, unlike at fixed $N$.</li>
<li><b>Why it matters</b> It shows how strings compute a CFT ensemble. The orbifold also sees strong string coupling, and the CFT's extra torus is a decoupled Chern–Simons sector.</li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> For $Q_5=1$ the NS-NS string matches $\mathrm{Sym}_N(T^4)\times\hat T^4$, yet its worldsheet computes an ensemble over $Q_1$.</li>
<li><b>Result</b> With $\sigma_w$ counting each permutation once, $\log Z_p[J]$, for $Z_p=\sum_N p^N Z_N$, is exactly a sum over connected covers weighted by $p^{N_c}/N_c$. Rescaling $\sigma_w$ by $p^{-w/2}$ gives an exact genus expansion, $g_s^{-2}\propto p$, extending Eberhardt's partition-function result. Fixed $N$ with $g_s^2=1/N$ fails beyond leading order, and Kim–Porrati's Legendre transform is only leading-order, here and, conjecturally, at higher $Q_5$.</li>
<li><b>Why it matters</b> Genus-$g$ terms carry $(V/N)^g$, so the expansion fails at large volume, where the R-R dual is never weakly coupled. For all $Q_5$ the R-R currents seem to lack vertex operators. The $J\bar J$ deformations to other coprime $(Q_1,Q_5)$ are exact, with the free orbifold at vanishing R-R scalars, unlike Larsen–Martinec.</li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> Strings on $AdS_3\times S^3\times T^4$ with one unit of NS5-brane flux match $N$ copies of a free 2d theory on a four-torus, with their permutations gauged. Yet they may describe a weighted sum over $N$.</li>
<li><b>Result</b> The theory's correlators sum over ways of gluing copies into surfaces, the string worldsheets. Summed over $N$, the gluings split into connected pieces, giving exact sums over worldsheets of every genus (number of handles), with coupling $g_s^{-2}\propto p$ for weight $p$ per copy.</li>
<li><b>Why it matters</b> This shows how strings can be dual to an ensemble of CFTs. It also shows where strings become strongly coupled, and why an extra torus is invisible.</li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="sec-dual_cft-p1 sec-dual_cft-p4">Type IIB strings on $AdS_3\times S^3\times T^4$, with $Q_1$ strings and $Q_5$ five-branes, are dual to a 2d CFT with $N=Q_1Q_5$. For one unit of NS5-brane flux this CFT is believed to be a free symmetric orbifold, $N$ copies of $T^4$ permuted by $S_N$, times an extra torus $\hat T^4$.</span> <span data-covers="sec-string_ws-p4">The worldsheet with that flux reproduces the orbifold's spectrum and correlators.</span> <span data-covers="section-2.5-p1">Three puzzles remain: strings describe an ensemble over $N$, the orbifold stays free where strings are strongly coupled, and the extra torus never appears in strings.</span> <span data-covers="sec-grand-p6 section-4.1-p2 sec-q5_1_dec_sector-p9">The paper resolves each, with the orbifold's exact combinatorics, its $1/N$ expansion, and a bulk Chern–Simons theory.</span></p>
<p><span data-covers="sec-genus_exp-p3">An orbifold correlator is a sum over covering surfaces, gluings of the copies around the insertions, identified with string worldsheets.</span> <span data-covers="sec-genus_exp-p6 sec-genus_exp-p7">At fixed $N$ a genus-$g$ cover scales as $N^{1-g-n/2}$, suggesting $g_s^2=1/N$, but only at leading order, because its $1/N$ corrections mix with higher genus.</span> <span data-covers="sec-genus_exp-p8">Disconnected covers do not factorise exactly either, since copies used by one cannot be used by another.</span> <span data-covers="sec-grand-p2 sec-grand-p4">Summing over $N$, $Z_p[J]=\sum_N p^N Z_N[J]$, removes that constraint, so the sum exponentiates into connected covers.</span> <span data-covers="sec-grand-p6 sec-genus_exp-p2">With twist operators counting each permutation once, and rescaled by $p^{-w/2}$, every genus-$g$ cover then carries exactly the string weight, with $g_s^{-2}\propto p$.</span> <span data-covers="sec-grand-p4">This extends the known exponentiation of the partition function to correlators.</span></p>
<p><span data-covers="sec-grand-p7">String theory thus computes ratios of ensemble partition functions; fixed-$N$ correlators need separate inverse Laplace transforms of correlators and vacuum diagrams.</span> <span data-covers="sec-grand-p8 sec-grand-p10">The copy-counting operator should correspond to the worldsheet operator $I$, and its exchange spoils field-theory clustering.</span> <span data-covers="sec-higher_genus_CFT-p3">On a CFT surface of genus $G>1$ the worldsheet must cover the surface, so its genus is at least $G$ and $p\propto g_s^{2G-2}$: large $p$ is strong coupling.</span> <span data-covers="section-3.5-p3">On the sphere the exponentiated form is exact at finite $p$, so perturbative strings seem to capture the whole partition function.</span> <span data-covers="section-3.5-p1">For $Q_5>1$ the paper conjectures a Laplace transform over $Q_1$, refining an earlier Legendre transform.</span></p>
<p><span data-covers="section-4.1-p1">The NS-NS string's squared 10d coupling is $g_{10}^2=V/N$, with $V$ the torus volume, yet the orbifold is free for every $V$.</span> <span data-covers="section-4.1-p2">It still sees strong coupling, because genus-$g$ terms of its $1/N$ expansion carry $(V/N)^g$, from torus zero modes on loops around branch points. So the expansion breaks down once $V$ reaches $N$.</span> <span data-covers="section-4.1-p3 section-4.1-p4">The S-dual R-R string then looks weakly coupled, but its AdS radius is below the string scale. Newton's constant in AdS units, $G_N^{(10)}/R^8=V/N$, is large, so for one unit of flux it is never weakly coupled.</span> <span data-covers="sec-planck-p3 sec-planck-p4">Counting covers shows the expansion also fails at high energies, $E\sim N^{1/6}$ if single covers do not grow, a negative power of the string coupling.</span></p>
<p><span data-covers="sec-q5_1_dec_sector-p5 sec-q5_1_dec_sector-p6">The extra torus carries wrapped D1- and D3-brane charges, and matching the bulk BPS bound gives it the inverse volume, $\hat G=G/V$.</span> <span data-covers="sec-q5_1_dec_sector-p8">Its partition function is one overall factor, not one per string, suggesting that its currents have no local worldsheet vertex.</span> <span data-covers="sec-q5_1_dec_sector-p9">In the bulk it is a level-1 Chern–Simons theory, decoupled from all strings, so D-branes charged under it should not exist.</span> <span data-covers="sec-diffrent_back-p1 sec-diffrent_back-p2">U-duality relates all coprime $(Q_1,Q_5)$ with the same $N$, so each is an exactly marginal deformation of the free orbifold: a blow-up plus a $J\bar J$ deformation mixing the two tori's currents.</span> <span data-covers="section-5.2-p10">The paper finds the $J\bar J$ part exactly.</span> <span data-covers="section-5.3-p2 section-5.3-p3">For every $Q_5$ the R-R currents, now of level $Q_5$, seem to lack a worldsheet vertex.</span> <span data-covers="section-5.3-p4 section-5.3-p6">States whose charges are multiples of the levels are pure gauge modes, though they carry R-R charge.</span></p>
<p><span data-covers="section-5.2-p11">The blow-up part of the deformation is known only at leading order.</span> <span data-covers="section-3.5-p1">The ensemble for $Q_5>1$ is a conjecture, and whether it includes $Q_1$ not coprime to $Q_5$ is open.</span> <span data-covers="sec-planck-p4">How single covers grow with energy, and so the exact breakdown scale, is not known.</span> <span data-covers="section-5.2-p6 sec-intro-p7">The orbifold with vanishing theta angle is conjectured to sit at $\chi=\pm1/2$, and whether it has a controllable string description is open.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

FLAGS = [
    {"node": "sec-genus_exp-p4", "note": "(3.2) writes the two-point function as $1/|z|^{2\\Delta_w}$ with $\\Delta_w=\\frac{c}{24}(w-1/w)$. That $\\Delta_w$ is the holomorphic weight $h_w$; for a spinless operator the exponent should be $2(h+\\bar h)=4h_w$. Possibly a factor of 2 in the convention; not used in the layers."},
    {"node": "sec-genus_exp-p5", "note": "(3.4) labels the insertions $z_1\\dots z_s$, while (3.3) and (3.5) use $n$ for their number. Cosmetic."},
    {"node": "sec-grand-p5", "note": "(3.13): the summation index is written $w_n$ under the sum while the summand uses $J_w$. Cosmetic."},
    {"node": "sec-grand-p10", "note": "(3.19), second line: $\\partial_{J_{w_1}}^2\\partial_{J_{w_1}}^2$ and the second factor $\\partial_{J_{w_1}}^2$ presumably should involve $J_{w_2}$."},
    {"node": "sec-higher_genus_CFT-p3", "note": "Question for the author: 'Repeating the same redefinition (3.14)'. For $G>1$, (3.20) gives a connected diagram the weight $p^{N_c}$ with $N_c=[(1-g)+\\frac12\\sum_j(w_j-1)]/(1-G)$. With $\\sigma'_w=p^{-w/2}\\sigma_w$ the $g$-dependence gives $p\\propto g_s^{2G-2}$ as stated, but each insertion keeps an extra $p^{w_jG/(2-2G)}$ beyond the $g_s$ per insertion of (3.6); $\\sigma'_w=p^{w/(2G-2)}\\sigma_w$ removes it and reduces to (3.14) at $G=0$. Is 'the analogous redefinition' meant? (3.21) and the vacuum diagrams are unaffected; the layers state only $p\\propto g_s^{2G-2}$."},
    {"node": "section-4.1-p1", "note": "Sections 4-5 write the NS-NS frame quantities without primes ($g_6^2=1/N$, $g_{10}^2=V/N$) and call the torus volume $V$; section 2.1 calls them $g_6'$, $g_{10}'$, $v_4$. Section 5.2 then uses $v_4$ for the canonical-frame volume in (5.23), distinct from $V=Ng_{10}^2$. Consistent but easy to misread; the layers follow each section's usage and say 'torus volume'."},
    {"node": "section-3.5-p1", "note": "Section 3.1 says the ensemble is weighted by $p^{Q_1}$; (3.24) uses $p^{Q_5Q_1}$. A redefinition of $p$ (identical for $Q_5=1$), not a contradiction; the section 3.5 brief quotes (3.24) as written, the rest of the layers use $p^{Q_1}$."},
    {"node": "section-5.2-p7", "note": "'For the canonical background (5.12) the two are related by' presumably means the canonical background (5.17), with $\\tau,\\tilde\\tau$ related by the attractor equation (5.12)."},
    {"node": "fig-N30_moduli", "note": "The caption defines $\\tau_\\text{RR}=\\chi+i/g_{10}$ in R-R-frame variables, section 5.2 defines $\\tau_\\text{RR}=-1/\\tau$ from the NS-NS-frame $\\tau$. Consistent. Checked the arc endpoints in the caption ((15,2): 1/2 and 7/15; (10,3): 1/3 and 3/10; (6,5): 1/5 and 1/6) against $\\pm b/Q_5$, $\\pm a/Q_1$ with $aQ_5-bQ_1=1$: they agree for $(a,b)=(-7,-1),(-3,-1),(-1,-1)$. The figure is not in KEY because it does not carry the headline result; the author may prefer to add it."},
    {"node": "sec-intro-p5", "note": "The abstract says the strong-coupling limit of the NS-NS string 'arises (even at large N)' in the orbifold; section 4.1 shows this as a breakdown of the $1/N$ expansion at $V\\sim N$. The layers phrase it as a breakdown, not as the orbifold producing a new description."},
]
