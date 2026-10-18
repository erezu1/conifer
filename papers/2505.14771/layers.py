"""The drafted layers of arXiv:2505.14771 (Absolute entropy and the observer's no-boundary state).

Drafted by an AI reader from the paper's text; nothing here has been checked by the authors yet, so every
rendition carries status ai-draft. Node ids are those of skeleton.json / outline.md. Math is TeX between
$ signs, drawn with the paper's own macros at build time. <span data-covers="..."> marks what a sentence of a
summary stands for.
"""
from layers_gists import GIST          # one line per paragraph, box and section
from layers_briefs import BRIEF        # one paragraph per section, with grounding spans
from layers_side import DEFS, QUESTIONS, BACKGROUND   # the definitions, questions and background notes

KICKER = "arXiv:2505.14771 · hep-th · May 2025"
DATE = "20 May 2025"
NOTE = ("The paper as a Conifer tree. The text at the Paper depth is the paper itself; the gist, the summaries, "
        "the definitions, the background notes and the questions were drafted by an AI reader and have not yet been checked by the authors.")
PAGE_TITLE = "The observer's no-boundary state"
# The headline is the one-line identity (1.1), rho_NB = 1, readable without its section. No figure carries it: the
# bra-ket wormhole is drawn inline as the "equation" (1.3), and the numbered figures show Penrose diagrams, JT
# geodesics and example cosmologies, none of which states the result; so the key figure is omitted.
KEY = {"equation": "1.1main"}
DEFAULT_AUDIENCE = "physicist"
AUDIENCES = [
    {"key": "specialist", "label": "Specialist", "hint": "works on observer algebras, the no-boundary state or gravitational path integrals"},
    {"key": "physicist", "label": "Physicist", "hint": "high-energy theorist; knows quantum gravity and holography in outline, not von Neumann algebras"},
    {"key": "student", "label": "Student", "hint": "knows quantum field theory, general relativity and density matrices"},
]

ROOT_STATUS = "ai-draft"

# The paper's own results (skill section 2), from the abstract and the introduction (sect-1.intro-p3 to p10).
# The absolute entropy with its O(1/G) term (sect-1.intro-p6, sect-5.conclusion-p1) is what the paper says its main
# result makes possible, so it is Why it matters, not a contribution. The axion FLRW wormholes of the discussion are a
# test case with open puzzles (sect-1.intro-p11 "We point out new questions"), not a result.
# How they relate (skill section 2), from the paper's own words: theme A is the global no-boundary state (the
# bra-ket wormhole, its identity with the inner product, the JT check of section 2's argument); theme B carries it to
# observers with horizons (section 4 opens by restricting the global identity to a subalgebra); theme C, the no-KMS
# theorem, is introduced as the obstacle to checking theme B explicitly (sect-nogo-p1). Every theme builds on
# another: one argument.
SHAPE = "one argument"
CONTRIBUTIONS = [
    {"id": "c-identity", "headline": True,
     "claim": r"The paper argues that the observer's no-boundary density matrix is the identity on the physical Hilbert space, the maximum-entropy state, because the path integral computing it is the one computing gravitational inner products; topology change does not alter this.",
     "quote": "is the identity operator on the physical Hilbert space, i.e., the maximum entropy state",
     "where": ["sect-2.2-p1", "sect-2.2-p3", "sect-2.4topo-p3"], "theme": "A",
     "builds_on": "c-wormhole", "link_quote": "With the path integral definition of the observer’s no-boundary state (2.4) , we would now like to argue"},
    {"id": "c-wormhole",
     "claim": r"Geometrically the observer's no-boundary state is a bra-ket wormhole: the observer's worldline has nowhere to end on a Hartle–Hawking cap, so the connected geometry joining bra and ket is the leading contribution and the state is mixed.",
     "quote": "Geometrically, the no-boundary state is a bra-ket wormhole",
     "where": ["sect-2.1-p2", "sect-2.1-p3"], "theme": "A"},
    {"id": "c-jt",
     "claim": r"In JT gravity with $\Lambda<0$, Euclidean wormhole amplitudes, without and with an observer particle, equal the matrix elements of the identity on the physical Hilbert space; with the observer the path integral also imposes the momentum constraint.",
     "quote": "show this explicitly in Jackiw-Teitelboim gravity",
     "where": ["subsect-JT1empty-p2", "sect-3.3ONBJT-p3", "sect-3.3ONBJT-p4"], "theme": "A",
     "builds_on": "c-identity", "link_quote": "we check the somewhat formal arguments of section 2 by showing that"},
    {"id": "c-trace",
     "claim": r"No-boundary expectation values give a trace on the observer's algebra, so the von Neumann entropy of an observer's state in any universe is minus its relative entropy to the no-boundary state; to leading order it is minus the on-shell action of the dominant no-boundary saddle.",
     "quote": "Expectation values in the no-boundary state provide a trace",
     "where": ["section-4.1-p3", "section-4.1-p4"], "theme": "B",
     "builds_on": "c-identity", "link_quote": "if the density matrix on the global slice is the identity, then the density matrix on a subalgebra is also the identity on that reduced algebra"},
    {"id": "c-consistent",
     "claim": r"For observers with horizons, a path integral with boundary data on the causal diamond's light cones again gives the identity, consistent with all previously discussed traces for invariantly defined regions: the de Sitter static patch, with its $e^{A/4G}$, and regions bounded by extremal surfaces.",
     "quote": "consistent with all previously discussed cases of traces for invariantly defined regions",
     "where": ["section-4.3-p4", "section-4.3-p6", "section-4.1-p3"], "theme": "B",
     "builds_on": "c-trace", "link_quote": "This serves as a consistency check because our formal arguments must match known results in de Sitter space"},
    {"id": "c-nokms",
     "claim": r"No asymptotically de Sitter spacetime other than de Sitter admits a state that is KMS on an observer's worldline, so de Sitter's explicit construction of the trace does not extend; this does not imply that the no-boundary state is not a trace.",
     "quote": "we show there is no KMS state for worldline correlation functions for any asymptotically de Sitter geometry besides de Sitter itself",
     "where": ["sect-5.1kms-p2", "sect-5.1kms-p3", "sect-5.2constructive-p5"], "theme": "C",
     "builds_on": "c-consistent", "link_quote": "We would like to check in controllable examples that the density matrix for an observer with causal horizons"},
]

# Every version states the five contributions the abstract claims (c-identity, c-wormhole, c-jt, c-trace,
# c-consistent); c-nokms, claimed only in the introduction, is in the summary (and the specialist's gist).
ROOT_GIST = {
    "html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sect-1.intro-p4">In closed universes, observer algebras fix entropy up to an $O(1/G)$ constant.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-identity"><span data-covers="sect-2.2-p1 sect-2.2-p3">The observer's no-boundary density matrix is argued to be the identity (maximum entropy): its path integral computes inner products.</span></li>
  <li data-claims="c-wormhole"><span data-covers="sect-2.1-p2">Geometrically, the state is a bra-ket wormhole; the worldline forbids the Hartle–Hawking cap.</span></li>
  <li data-claims="c-jt"><span data-covers="subsect-JT1empty-p2 sect-3.3ONBJT-p3">In Jackiw–Teitelboim gravity, wormhole amplitudes match the identity.</span></li>
  <li data-claims="c-trace"><span data-covers="section-4.1-p3 section-4.1-p4">No-boundary expectation values are a trace for the observer's algebra, defining entropy relative to that state.</span></li>
  <li data-claims="c-consistent"><span data-covers="section-4.3-p4 section-4.3-p6 section-4.1-p3">With horizons, the state is again the identity on the observer's region, consistent with all previously discussed traces for invariantly defined regions.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sect-1.intro-p6">This fixes entropy's $O(1/G)$ term asymptotically, where algebraic methods gave only $O(1)$ differences.</span></li>
</ul>""",
    "status": "ai-draft",
    "variants": {
        "specialist": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sect-1.intro-p4 sect-1.intro-p5">Type II observer algebras (CLPW and successors) fix entropy only up to $O(1/G)$; Witten proposed $S_\text{vN}(\rho)=-S_\text{rel}(\rho\|\rho_\text{NB})$, with $\rho_\text{NB}$ the identity.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-identity"><span data-covers="sect-2.2-p1 sect-2.2-p3 sec-canonical_quant-p5">With complete causal access, $\rho_\text{NB}=\mathbb{1}$ on the physical Hilbert space: its path integral is the gravitational inner product, in ADM form the rigging map $\delta(H_\text{WDW})$.</span></li>
  <li data-claims="c-wormhole"><span data-covers="sect-2.1-p2 sect-2.1-p3">Geometrically, $\rho_\text{NB}$ is a bra-ket wormhole $\mathcal{M}\times I$; the observer's worldline forbids the Hartle–Hawking hemispheres.</span></li>
  <li data-claims="c-jt"><span data-covers="subsect-JT1empty-p2 sect-3.3ONBJT-p3 sect-3.3ONBJT-p4">AdS JT wormhole amplitudes, with and without an observer, match the identity; the path integral imposes the momentum constraint too.</span></li>
  <li data-claims="c-trace"><span data-covers="section-4.1-p3 section-4.1-p4">$\langle\cdot\rangle_\text{NB}$ is a trace on the observer's algebra, giving $S=-I_\mathcal{M}+O(1)$ when one saddle dominates.</span></li>
  <li data-claims="c-consistent"><span data-covers="section-4.3-p4 section-4.3-p6 section-4.1-p3">With horizons, null boundary data on the diamond again give the identity, consistent with de Sitter's $e^{A/4G}$ and Chen–Penington's extremal-region trace.</span></li>
  <li data-claims="c-nokms"><span data-covers="sect-5.1kms-p2 sect-5.1kms-p3">Only de Sitter, among asymptotically de Sitter spacetimes, admits a worldline KMS state.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sect-1.intro-p6">The $O(1/G)$ term is fixed, beyond the $O(1)$ differences algebraic methods gave.</span></li>
</ul>""", "status": "ai-draft"},
        "student": {"html": r"""<ul class="gist-list">
<li><b>Context</b> <span data-covers="sect-1.intro-p4">In closed universes, entropy is known only up to a large constant.</span></li>
<li><b>Result</b><ul>
  <li data-claims="c-identity"><span data-covers="sect-2.2-p1 sect-2.2-p3">The no-boundary state of a universe with an observer is argued to be the identity matrix, maximally mixed: its path integral computes inner products.</span></li>
  <li data-claims="c-wormhole"><span data-covers="sect-2.1-p2">Geometrically, the state is a wormhole joining bra and ket: the observer's path cannot end.</span></li>
  <li data-claims="c-jt"><span data-covers="subsect-JT1empty-p2 sect-3.3ONBJT-p3">In two-dimensional Jackiw–Teitelboim gravity, wormhole amplitudes match the identity.</span></li>
  <li data-claims="c-trace"><span data-covers="section-4.1-p3 section-4.1-p4">Averages in the no-boundary state obey $\langle ab\rangle=\langle ba\rangle$ for observer operators: a trace, against which entropy is defined.</span></li>
  <li data-claims="c-consistent"><span data-covers="section-4.3-p4 section-4.3-p6 section-4.1-p3">Behind horizons, as in de Sitter, the result is consistent with all previously discussed traces.</span></li>
</ul></li>
<li><b>Why it matters</b> <span data-covers="sect-1.intro-p6">This fixes the large constant, as an expansion in small $G$.</span></li>
</ul>""", "status": "ai-draft"},
    },
}

ROOT_BRIEF = {
    "html": r"""<p><span data-covers="sect-1.intro-p1 sect-1.intro-p2">A closed universe has no asymptotic boundary to anchor observables, so recent work dresses them to an observer instead.</span> <span data-covers="sect-1.intro-p4">The resulting algebras are type II: they give entropy differences within one background but leave a state-independent $O(1/G)$ constant open.</span> <span data-covers="sect-1.intro-p5">Witten suggested fixing it with $S_\text{vN}(\rho)=-S_\text{rel}(\rho\|\mathbb{1})$, if one knew which state is the identity, and proposed the no-boundary state.</span> <span data-covers="sect-2.2-p1 sect-2.4topo-p3">The paper argues that the observer's no-boundary density matrix is indeed the identity on the physical Hilbert space, with or without topology change.</span> <span data-covers="section-4.1-p4">So no-boundary expectation values form a trace, and entropy acquires an absolute meaning.</span></p>
<p><span data-covers="sect-2.1-p2">The starting point is geometric. A Hartle–Hawking cap would leave the observer's worldline nowhere to end, so no pure no-boundary state exists.</span> <span data-covers="sect-2.1-p2 sect-2.1-p3">The density matrix exists, and its leading geometry is a bra-ket wormhole of topology $\mathcal{M}\times I$, so the state is mixed.</span> <span data-covers="sect-2.2-p1">That wormhole path integral is exactly the one that defines the gravitational inner product between the two slices, hence $\rho_\text{NB}=\mathbb{1}$.</span> <span data-covers="sect-2.2-p2 sect-2.2-p3">Multiplying density matrices integrates over boundary data modulo diffeomorphisms, and squaring returns the same wormhole, $\rho_\text{NB}^2=\rho_\text{NB}$.</span> <span data-covers="sect-2.2-p4">In ordinary field theory the same gluing doubles the inverse temperature; gravity differs because its Hamiltonian is a constraint.</span></p>
<p><span data-covers="sec-canonical_quant-p2 sec-canonical_quant-p3">In ADM variables the lapse multiplies the Wheeler–DeWitt constraint, and integrating it over the real line gives $\rho_\text{NB}=\delta(H_\text{WDW})$, the rigging map.</span> <span data-covers="sec-canonical_quant-p5 sec-canonical_quant-p6">That map is the inner product on physical states, so it is again the identity on the physical Hilbert space.</span> <span data-covers="sect-2.4topo-p2 sect-2.4topo-p3">Inner products include higher topologies too, so topology change leaves the result intact, given rules that suppress disconnected observer contributions.</span> <span data-covers="sect-2.2-p5 sect-2.2-p6">The trace often diverges, making the state a weight; with a dominant saddle it is $e^{-I}$, which fixes the entropy's constant.</span></p>
<p><span data-covers="sect-4.JT-p1 sect-3.1HJT-p1">Jackiw–Teitelboim (JT) gravity with $\Lambda<0$, a two-dimensional dilaton gravity whose closed universes crunch, makes this exact. Physical states are labelled by the universe's maximal size $b$.</span> <span data-covers="subsect-JT1empty-p2">The Euclidean double-trumpet wormhole equals $\int b\,db\,\psi_b\psi_b$, the identity's matrix element.</span> <span data-covers="sect-3.3ONBJT-p3 sect-3.3ONBJT-p4">With an observer particle, the known wormhole amplitude is reproduced too, which shows that the path integral also imposes the momentum constraint.</span> <span data-covers="subsect-JT4nonpert-p2">Summing topologies, the observer's Hilbert space is spanned by the $N$ energy levels of one ensemble member, where without an observer it is one-dimensional.</span></p>
<p><span data-covers="sect-3obshorizon-p1 section-4.1-p3">When the observer has a horizon, the global identity should restrict to the identity on the observer's algebra. Since that algebra's trace is unique up to scale, $\langle a\rangle_\text{NB}=\mathcal{Z}'_\mathcal{M}\operatorname{Tr}(a)$.</span> <span data-covers="section-4.1-p4">Entropy is then minus the relative entropy to $\rho_\text{NB}$, and to leading order $S=-I_\mathcal{M}+O(1)$, minus the action of the dominant no-boundary saddle.</span> <span data-covers="section-4.1-p3">For de Sitter this gives the factor $e^{A/4G}$.</span> <span data-covers="section-4.3-p2 section-4.3-p4">A direct path integral, with boundary data on the diamond's light cones, gives $\rho_\text{NB}^2=\rho_\text{NB}$, because gravity smooths the would-be conical excess at the diamond's edge.</span> <span data-covers="section-4.3-p6">For regions bounded by extremal surfaces the trace of Chen and Penington should be its $O(1)$ part.</span></p>
<p><span data-covers="sect-nogo-p1">Checking this beyond de Sitter explicitly would need the route of Chandrasekaran, Longo, Penington and Witten (CLPW), which rests on a state that is KMS, thermal, on the observer's worldline.</span> <span data-covers="sect-5.1kms-p2 sect-5.1kms-p3">No such state exists in any other asymptotically de Sitter spacetime. KMS forces worldline correlators to equal Bunch–Davies ones, whose commutator matches the universal short-distance form only at constant de Sitter curvature.</span> <span data-covers="sect-5.2constructive-p3 sect-5.2constructive-p5">Cosmologies built to be analytic and periodic in imaginary time fail as well, through curvature singularities in their Euclidean section.</span> <span data-covers="sect-nogo-p1 sect-5.conclusion-p2">This does not rule out a trace; the paper suggests a weaker “weak KMS” property of no-boundary saddles may suffice.</span></p>
<p><span data-covers="sect-2.1-p3 sect-2.4topo-p1">The general argument is formal: it assumes a well-defined contour and lacks a Hamiltonian for topology change.</span> <span data-covers="section-4.3-p7 sect-5.conclusion-p2">With horizons, how the sphere topology emerges on reduction is not understood, and a type III algebra with no trace is not excluded.</span> <span data-covers="sect-5.conclusion-p5 sect-5.conclusion-p6">In an axion-supported cosmology the leading entropy $-I$ differs from the horizon area and stays $O(1/G)$ where a type I algebra is expected; whether that saddle dominates is unclear.</span></p>""",
    "status": "ai-draft",
}

VARIANTS = {}

# Inconsistencies found in the paper and places the drafter was unsure (for the authors; not shown to readers).
FLAGS = [
    {"node": "sect-2.2-p3", "note": r"From $\rho_\text{NB}^2=\rho_\text{NB}$ the text concludes “a projector on the physical Hilbert space, i.e. $\rho_\text{NB}=\mathbb{1}$”. A projector is the identity only if its range is the whole physical space; is that range argument (from the inner-product identification in sect-2.2-p1) what is meant here?"},
    {"node": "sect-3.3ONBJT-p3", "note": r"(3.37) carries a factor $4^\Delta$ (from the twist integral (3.34)) that the path-integral result (3.26), which it is said to match, does not. Is the difference a normalization of $|\ell,\tau\rangle$ or of the observer states, or should one of the two be corrected?"},
    {"node": "sect-3.1HJT-p2", "note": r"With $x\sim x+1$ (3.3), “$\tau\sim\tau+b$ with $x=b\tau$” is inconsistent: $x=b\tau$ gives $\tau\sim\tau+1/b$. Later formulas integrate $\tau$ over $[0,b]$, so presumably $\tau=bx$ is meant?"},
    {"node": "sect-2.1-p1", "note": r"The observer's energy is continuous (“$q>0$ … any non-negative real value”), but (3.14), (3.26) and (3.45) sum over $q$ and use a Kronecker $\delta_{q_1q_2}$. Should these be an integral and $\delta(q_1-q_2)$, or is $q$ discretized in section 3?"},
    {"node": "sect-3.3ONBJT-p5", "note": r"(3.40) has $\langle b_1,k_1\dots k_n|\cdot|b,k_1\dots k_n\rangle$; presumably $b_1$ should be $b$."},
    {"node": "footnotes", "note": r"Footnote 18: in (3.41) the second exponential reads $e^{-\beta_1E_2}$ and in (3.42) both traces read $\delta(H-E_1)$; presumably $e^{-\beta_2E_2}$ and $\delta(H-E_2)$."},
    {"node": "section-4.2-p1", "note": r"“$2N$ qubits $\mathcal{H}_N=(\mathbb{C}^{2N})_R\otimes(\mathbb{C}^{2N})_L$”: $N$ qubits per side span $(\mathbb{C}^2)^{\otimes N}$, of dimension $2^N$, which (4.12) and (4.15) assume. Likewise (4.14) writes the trace as $\sum_{i=1}^N(\langle0|a|0\rangle_i+\langle1|a|1\rangle_i)$, a sum over single qubits rather than over the $2^N$ basis states. Typos?"},
    {"node": "sect-5.conclusion-p5", "note": r"(6.8) gives $A_h=2\pi H^{-1}(1+\sqrt{1-q^2})\sin^2\theta_h$, which at $q=0$ is $4\pi/H$, twice the dS$_3$ horizon length; then $A_h/4G\ne-I$ at $q=0$, though the text implies they differ only for $0<q<1$. The edge of the diamond at $t=0$ has length $2\pi a(0)\sin\theta_h=2\pi H^{-1}\sqrt{(1+\sqrt{1-q^2})/2}\,\sin\theta_h$. Is that the intended formula? The layers quote only that the area and $-I$ differ."},
    {"node": "subsect-JT1empty-p2", "note": r"“The integration over $b$ in (3.12) is a simple example of (2.8)”: the integral that realizes the gluing (2.8) is the one in (3.17)/(3.21); (3.12) is the canonical resolution of the identity. Is (3.17) meant?"},
    {"node": "sect-1.intro-p3", "note": r"The introduction says the main result is “establishing” Witten's proposal and calls the arguments “modest assumptions”, while the abstract says “we argue”. The layers follow the abstract and say “argues”."},
]
