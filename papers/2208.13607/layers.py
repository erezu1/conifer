"""The drafted layers of arXiv:2208.13607 (Explicit holography for vector models at finite N, volume and temperature).

Drafted by an AI reader from the paper's text; nothing here has been checked by the authors yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2208.13607 · hep-th · August 2022"
DATE = "29 August 2022"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the authors.")
PAGE_TITLE = "Vector-model holography at finite N"
# The headline is the exact finite-N bulk theory; (2.42) is its partition function in one line, the two towers
# Phi_J and tilde-Phi_J coupled locally plus N W, readable with the gist alone. The paper has no figure that carries
# a result (its only images are Feynman-rule diagrams), so no key figure.
KEY = {"equation": "eq-bulk_Z"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on higher-spin holography, vector models or bilocal collective fields"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows AdS/CFT and large-N field theory in outline"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory, path integrals and the basics of AdS/CFT"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract ("three aspects of this mapping": First, Second,
# Finally) and the introduction's list (section-1-p3 to p5). The vanishing empty-AdS amplitude and the critical
# model's boundary condition are announced only in section 2's own outline (finiteN-p1), not in the introduction:
# they are steps of finding A and go in the summary, not here.
# How they relate, from the paper's own words: the sphere free energy is computed with the finite-N formalism
# (finiteV-p1, the link quote), so c-sphere builds on c-finiteN across themes; the one-loop comparison and the
# regularization belong to the sphere (theme B) without a stated dependence on each other; the thermal map (C) uses
# the zero-temperature map of the earlier paper at leading large N and rests on none of the others. Three themes,
# one of them unlinked: several findings.
SHAPE = "several findings"
CONTRIBUTIONS = [
    {"id": "c-finiteN", "headline": True,
     "claim": r"Keeping the Lagrange-multiplier bilocal $\Sigma$ of a $G$–$\Sigma$ formalism, as in SYK, gives a bilocal theory exact at finite $N$ that enforces the finite-$N$ constraints; mapped to AdS it gives an exact bulk theory with additional auxiliary fields $\tilde\Phi_J$ that implement them, on a fixed AdS background.",
     "quote": "we can construct an exact mapping to the bulk that is valid also at finite",
     "where": ["finiteN2-p2", "finiteN2-p5", "bulkAction-p1"], "theme": "A"},
    {"id": "c-sphere",
     "claim": r"On $S^d$ the sphere free energy matches exactly between the two sides: in the finite-$N$ formalism it is the prefactor $Z_\phi^N$ in front of the bulk path integral, with no classical or quantum bulk contribution.",
     "quote": "how the sphere free energy matches exactly between the two sides",
     "where": ["section-3.2-p1", "section-3.2-p3"], "theme": "B",
     "builds_on": "c-finiteN", "link_quote": "We then use our finite $N$ formalism to schematically map the sphere free energy from the CFT to the bulk"},
    {"id": "c-oneloop",
     "claim": r"The paper argues that earlier one-loop bulk computations assumed canonical two-derivative kinetic terms, which its quartic-derivative bulk action does not have, so they do not suggest a shift of the bulk coupling for $O(N)$.",
     "quote": "it does not suggest any such shift",
     "where": ["section-3.2-p5", "section-3.2-p6"], "theme": "B"},
    {"id": "c-reg",
     "claim": r"The map can be consistently regularized: regulators on both sides that keep the same number of modes in each $SO(d+1)$ representation give an invertible map between the regulated theories, and such regulators can be argued to exist.",
     "quote": "how the mapping can be consistently regularized",
     "where": ["regs-p5", "regs-p6"], "theme": "B"},
    {"id": "c-thermal",
     "claim": r"In the low-temperature (confined) phase, at leading order in the large-$N$ saddle, the zero-temperature map applies and gives high-spin gravity on thermal AdS; the deconfined phase presumably needs a different, black-hole map, left open.",
     "quote": "the low-temperature phase of the vector models can be mapped to a high-spin gravity theory on thermal AdS space",
     "where": ["finiteT-p7", "finiteT-p9"], "theme": "C"},
]

# Every version states the four contributions the abstract claims (c-finiteN, c-sphere, c-reg, c-thermal), one point
# per finding; c-oneloop, claimed only in the introduction, is in the summary, and in the specialist gist's point B.
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">An earlier explicit map turns vector models into non-local high-spin gravity on $AdS_{d+1}$, order by order in $1/N$.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-finiteN"><span data-covers="finiteN2-p1 finiteN2-p5">A bilocal Lagrange multiplier, as in SYK, makes the map exact at finite $N$;</span> <span data-covers="bulkAction-p1 bulkAction-p2 section-1-p3">its bulk image, auxiliary fields on one fixed AdS, imposes the finite-$N$ constraints.</span></li>
  <li data-claims="c-sphere c-reg"><span data-covers="section-3.2-p1 section-3.2-p3">On the sphere the free energy matches exactly, as a prefactor of the bulk path integral;</span> <span data-covers="regs-p5 regs-p6">matching mode counts can regularize the map consistently.</span></li>
  <li data-claims="c-thermal"><span data-covers="finiteT-p9">The low-temperature phase maps to high-spin gravity on thermal AdS.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p1">Assuming the conjectured equivalence with Vasiliev's theory, such a map gives high-spin gravity an action whose quantum corrections can be computed systematically.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p3">An earlier map from the bilocal $G(x_1,x_2)$ to transverse traceless $\Phi_J$ on $AdS_{d+1}$ holds order by order in $1/N$ but misses finite-$N$ constraints.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-finiteN"><span data-covers="finiteN2-p2 finiteN2-p4 finiteN2-p5">A tree-level $G$–$\Sigma$ bilocal theory is exact at finite $N$, enforcing rank at most $N$;</span> <span data-covers="bulkAction-p1 bulkAction-p3">in the bulk $\Sigma$ becomes auxiliary $\tilde\Phi_J$, and empty AdS has zero amplitude on lattices of over $N$ points.</span></li>
  <li data-claims="c-sphere c-oneloop c-reg"><span data-covers="section-3.2-p1 section-3.2-p3">On $S^d$ both sides give $Z_\phi^N$ from a prefactor.</span> <span data-covers="section-3.2-p5 section-3.2-p6">Bulk kinetic terms are quartic in derivatives, so the $U(N)$ match of earlier one-loop tests is called a coincidence.</span> <span data-covers="regs-p5 regs-p6">Matching mode counts per $SO(d+1)$ representation can be argued to regularize it.</span></li>
  <li data-claims="c-thermal"><span data-covers="finiteT-p3 finiteT-p7">In the confined phase (large $N$ before large volume) the field theory's thermal circle is effectively $N\beta$ long;</span> <span data-covers="finiteT-p9">the zero-temperature map gives bulk fields of period $\beta$: thermal AdS.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p1">Assuming equivalence with gauge-fixed Vasiliev theory, the map gives high-spin gravity an action with computable quantum corrections.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="section-1-p1 section-1-p2">Vector models, $N$ scalars free or critical, are dual to high-spin gravity in AdS; an earlier map via their two-point field worked order by order in $1/N$.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-finiteN"><span data-covers="finiteN2-p1 finiteN2-p5">A Lagrange multiplier imposing the two-point field's definition, as in SYK, makes the map exact at finite $N$;</span> <span data-covers="bulkAction-p1 bulkAction-p2">in the bulk it becomes auxiliary fields imposing the constraints.</span></li>
  <li data-claims="c-sphere c-reg"><span data-covers="section-3.2-p1 section-3.2-p3">On a sphere both sides give exactly the same free energy.</span> <span data-covers="regs-p5 regs-p6">The map can be consistently regularized.</span></li>
  <li data-claims="c-thermal"><span data-covers="finiteT-p9">At low temperature it maps to high-spin gravity on thermal AdS (AdS with periodic time).</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="section-1-p1">Assuming the bulk theory is Vasiliev's high-spin gravity, the map gives it an action for computing quantum corrections.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="section-1-p1">An earlier paper by the authors turned the $U(N)$-singlet sector of $N$ free complex scalars in $d>2$ dimensions into a bulk theory on $AdS_{d+1}$.</span> <span data-covers="section-1-p1">It expands the bilocal $G(x_1,x_2)=\frac1N\sum_I\phi_I^*(x_1)\phi_I(x_2)$ in conformal representations and matches them to massless spin-$J$ fields $\Phi_J$.</span> <span data-covers="section-1-p1 section-1-p2">The result is a non-local high-spin gravity with coupling $1/N$, conjectured to be a gauge-fixed form of Vasiliev's theory, which reproduces the field theory order by order in $1/N$.</span> <span data-covers="section-1-p2">The paper studies three aspects of this map: finite $N$, the sphere $S^d$, and finite temperature.</span></p>
<p><span data-covers="finiteN2-p4">First, at finite $N$ the bilocal obeys constraints: on a lattice of $V$ points it is a matrix of rank at most $N$.</span> <span data-covers="largeN-p2">The earlier bilocal path integral ignores these; its weight $|\det G|^{N-V}$ even diverges unless $N\ge V$, so the continuum limit needs large $N$ first.</span> <span data-covers="finiteN2-p1">The fix, borrowed from the SYK model, keeps the Lagrange multiplier $\Sigma$ that defines $G$ as an independent bilocal field.</span> <span data-covers="finiteN2-p2">Because $\Sigma$ never contracts with itself, the resulting theory has no loop diagrams: each correlator is one tree diagram equal to the free-field answer, with no counter-terms.</span> <span data-covers="finiteN2-p5">Integrating over $\Sigma$ restricts the bilocal to configurations obeying the finite-$N$ constraints.</span></p>
<p><span data-covers="adscftmap-p3 adscftmap-p4">Both bilocals then map to AdS: the fluctuation $\eta$ of $G$ to the fields $\Phi_J$ as before, and $\Sigma$ to a second tower $\tilde\Phi_J$.</span> <span data-covers="bulkAction-p1">Suitable normalizations make the coupling between the towers local, $\int\tilde\Phi_J\Phi_J$, with unit Jacobian, so the bulk theory is exact for any $N$, with $G_N=1/N$.</span> <span data-covers="bulkAction-p2">Integrating out $\tilde\Phi_J$ order by order in $1/N$ gives back the earlier bulk action, but beyond perturbation theory these auxiliary fields seem necessary.</span> <span data-covers="adscftmap-p1 section-1-p3">The bulk is one fixed AdS background, with no sum over geometries or topologies, presumably a special feature of high-spin gravity.</span> <span data-covers="bulkAction-p3">As a check, the amplitude of empty AdS, computed exactly on the lattice, vanishes for integer $N<V$, as the rank constraint demands.</span> <span data-covers="critical-p1">For the critical model in $2<d<4$, only the boundary condition of the scalar $\Phi_0$ changes.</span></p>
<p><span data-covers="section-3.1-p1 section-3.1-p2">Second, since $S^d$ is conformal to flat space, the map carries over to hyperbolic space, with $L_2$ normalizability as the bulk boundary condition.</span> <span data-covers="section-3.2-p1 section-3.2-p3">The sphere free energy then matches exactly and trivially: integrating out $\eta$, or in the bulk $\Phi_J$, forces its partner to vanish, so both sides give $Z=Z_\phi^N$, the partition function of $N$ free fields.</span> <span data-covers="section-3.2-p3">It is a prefactor in front of the bulk path integral, with no classical or loop contribution.</span> <span data-covers="section-3.2-p5">Earlier one-loop tests assumed canonical two-derivative kinetic terms for each spin; they matched for $U(N)$, but for $O(N)$ needed a shift of the bulk coupling.</span> <span data-covers="section-3.2-p6">The bulk action here is quartic in derivatives, so the paper sees that match as a coincidence and suggests no shift.</span></p>
<p><span data-covers="regs-p2 regs-p3 regs-p4">To make the map rigorous, both sides must be regulated, the CFT by a cutoff on the Laplacian and the bulk by UV and IR cutoffs, each leaving finitely many modes and an $SO(d+1)$ symmetry.</span> <span data-covers="regs-p5">The regulators need not correspond: if each $SO(d+1)$ representation keeps equally many modes, the map splits into square blocks that are generically invertible.</span> <span data-covers="regs-p6 reg2-p2">The paper argues that bulk cutoffs tied to the CFT's can match every count, giving a precise but impractical map.</span></p>
<p><span data-covers="finiteT-p1 finiteT-p10">Finally, at finite temperature the singlet projection requires integrating over a $U(N)$ holonomy, which the paper does not know how to map to the bulk in general.</span> <span data-covers="finiteT-p2 finiteT-p3">At large $N$ a saddle dominates: uniform eigenvalues in the low-temperature confined phase, reached by taking $N$ large before the volume, and eigenvalues near one in the deconfined phase.</span> <span data-covers="finiteT-p6 finiteT-p7">In the confined phase the bilocal behaves as if the thermal circle had length $N\beta$, so at large $N$ its expectation value is the zero-temperature propagator.</span> <span data-covers="finiteT-p8 finiteT-p9">The zero-temperature map then applies unchanged and gives bulk fields periodic in $\beta$: the low-temperature phase is high-spin gravity on thermal AdS.</span></p>
<p><span data-covers="finiteN2-p3 bulkAction-p2">The paper does not perform the integral over $\Sigma$, or $\tilde\Phi_J$, beyond perturbation theory, so the exact bulk theory keeps its auxiliary fields.</span> <span data-covers="regs-p6 regs-p7">Its regularization fixes mode counts rather than explicit regulators, and bulk boundary conditions for the high-spin fields remain subtle.</span> <span data-covers="finiteT-p10 finiteT-p11">The thermal map holds only at leading order in the large-$N$ saddle: at finite $N$ the holonomy fluctuates, and the deconfined phase, presumably a black hole, needs a different map, left to future work.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "section-3.2-p5", "note": r"The dictionary shift is written $G_N\leftrightarrow1/(N+1)$ here but $1/(N-1)$ in section-1-p4. The one-loop $O(N)$ result (one real scalar's free energy) needs $1/(N-1)$; is $N+1$ a typo? The layers write $1/(N-1)$ (question q-oneloop) or no value."},
    {"node": "section-3.2-p5", "note": r"“the 1-loop correction was found to be identical to the tree level term”: the tree-level term is $N$ times one scalar's free energy, the one-loop term one scalar's. Is “equal to the free energy of a single real scalar” meant? The layers say so."},
    {"node": "critical-p1", "note": r"(2.54) has $N\cdot\frac12\sigma\,\eta(x,x)$, but with $\eta=N(G-G_0)$ of (2.7), $\frac12\sigma\sum_I|\phi_I|^2=\frac12\sigma\,\eta(x,x)$ plus a term linear in $\sigma$. Is the factor $N$ left from the normalization of [3] (footnote 7)? (2.53) also writes $\phi_I^2$ for complex fields, presumably $|\phi_I|^2$. Not used in the layers."},
    {"node": "adscftmap-p4", "note": r"“We can then convolve (2.35) with (2.36)”: (2.35) is the falloff condition on $\Sigma$; presumably the expansion (2.34). Also the $J=0$ term (2.38) has $\alpha_J$ where the $\eta$ version (2.31) has $\alpha_0$."},
    {"node": "finiteT-p3", "note": r"(4.2) integrates over $d^3x$ although the section is in general $d$; presumably $d^dx$."},
    {"node": "reg2-p3", "note": r"(A.5), $\Lambda^2-L\approx L^2e^{-2Y}$: from the stated estimate $L_{bulk}^2e^{-2Y}\approx u_{\rm max}^2$ with $L_{bulk}\sim L$ one would get $\Lambda^2\approx L^2e^{-2Y}$, which with $\Lambda Y\approx L$ has no solution with $Y\gg1$. Where does the $-L$ come from? The layers repeat only the conclusion $\Lambda,Y\propto\sqrt L$, as the paper's rough estimate. Unsure."},
    {"node": "finiteT-p2", "note": r"$V$ is the number of lattice points in sections 2 and 3 and a spatial volume in section 4. Not an error, but a reader comparing “$N<V$” (empty AdS) with “$T^{d-1}V\simeq N$” may be misled; the layers say which is meant (definition of lattice, question q-notation)."},
]
