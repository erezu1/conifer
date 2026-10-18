# Outline of: Absolute entropy and the observer's no-boundary state

Abstract:

We investigate the no-boundary proposal for closed universes with an observer. We argue that the observer’s no-boundary state is the identity operator on the physical Hilbert space, i.e., the maximum entropy state and show this explicitly in Jackiw-Teitelboim gravity. Geometrically, the no-boundary state is a bra-ket wormhole. Expectation values in the no-boundary state provide a trace for the observer’s algebra, which allows one to define von Neumann entropy for observers in different universes as the relative entropy with respect to the no-boundary state. This result is consistent with all previously discussed cases of traces for invariantly defined regions.

# [root] paper
## [sect-1.intro] section: 1 Introduction
### [sect-1.intro-p1] paragraph

The advent of the AdS/CFT correspondence [1, 2, 3, 4] has led to tremendous progress in our understanding of
quantum gravity in open spacetimes. Much less is known about quantum gravity in closed spacetimes. One reason
for this is that because diffeomorphisms are redundant in gravity, to describe local physics, one must
consider “relational observables” [5]. In open universes, bulk observables can be defined with respect to an
asymptotic holographic boundary. In the absence of such a boundary, such as for a closed universe or black
hole interiors, it is less obvious how to define meaningful bulk observables. This has stymied progress.

### [sect-1.intro-p2] paragraph

A way forward is to “dress” observables to other features of the spacetime, such as an observer [6]. Recently,
Witten proposed a general construction of quasi-local gauge-invariant observables dressed to an observer’s
worldline [7], extending the construction in de Sitter space with Chandrasekaran, Longo, and Penington (CLPW)
[8]. The “observer’s algebra” captures the experiences of the observer in perturbation theory around a given
background geometry. In this paper, we combine this progress with a recent improved understanding of the
gravitational path integral for closed universes.

### [sect-1.intro-p3] paragraph

An important application of the gravitational path integral for closed universes is the no-boundary proposal
[9]. It proposes that the state of the universe is prepared by the gravity path integral with no boundaries,
aside from the boundary where measurements are performed. In this paper, we introduce the “observer’s no-
boundary state.” Our main result is that this no-boundary density matrix is the identity operator (once
properly defined) for general closed universes under modest assumptions, establishing a proposal by Witten [7]

\[ \rho_\text{NB}=\mathbb{1}\,. \]

(1.1)

Our arguments go beyond perturbation theory, and follow directly from the gravitational path integral and an
interpretation of the no-boundary proposal. Before presenting intuition for the validity of (1.1), we recall
why this proposal is useful to define entropies.

### [sect-1.intro-p4] paragraph

Following the great success of studying von Neumann entropies in open universes [10, 11, 12, 13, 14, 15, 16,
17, 18, 19, 20], one would like to assign entropies to states in the observer’s Hilbert space in closed
universes. For the static patch of de Sitter space, CLPW successfully calculated entropy differences between
two perturbative states using the observer’s algebra, and found agreement with the generalized entropy of the
static patch. This construction was later generalized to several other invariantly defined regions with
horizons [21, 22, 23, 24] as well as proposals for treating more general subregions in semiclassical quantum
gravity [25, 24]. The observable algebra in these constructions is classified as a type II von Neumann
algebra. Type II algebras allow for a calculation of entropy differences unambiguously.1 By their perturbative
nature, unfortunately, these constructions leave undetermined a state-independent, but background dependent,
leading $O(1/G)$ contribution to entropy so do not enable one to compute entropy differences between two
different backgrounds or for the calculation of the absolute entropy.

### [sect-1.intro-p5] paragraph

To address this issue, Witten suggested an intriguing hypothesis [7] motivated by the standard finite-
dimensional identity

\[ S_\text{vN}(\rho) = -S_\text{rel}(\rho \parallel \mathbb{1})\,, \]

(1.2)

between the von-Neumann entropy and the relative entropy with the identity matrix. Given an understanding of
the (unnormalized) identity matrix, instead of defining von Neumann entropy directly, one can define it as
relative entropy with respect to the identity operator. This is convenient because relative entropies are
generally well-defined, even in infinite-dimensional systems such as quantum field theory.2 This reduces the
question of defining the absolute entropy $S_\text{vN}(\rho)$ to an understanding of the (unnormalized)
quantum gravity state that is given by $\mathbb{1}$, which is proposed to be the no-boundary state, (1.1). In
the context of de Sitter spacetimes, this suggestion is consistent with the long-standing lore that the no-
boundary state for the static patch has maximal entropy [32, 33, 34, 35]. Our main result is establishing this
proposal more generally, under standard assumptions about the gravitational path integral.

### [sect-1.intro-p6] paragraph

In summary, the identification (1.1) allows one to define the absolute entropy of states including in
particular the $O(1/G)$ contribution via an asymptotic expansion, whereas previously only $O(1)$ entropy
differences were available using algebraic methods. We briefly summarize the remainder of the paper.

### [sect-1.intro-p7] paragraph

In section 2, we consider spacetimes in which the observer has access to a complete Cauchy slice. The matrix
elements of $\rho_\text{NB}$ are then between two global slices of the universe. We will argue that the
leading topology that contributes to $\rho_\text{NB}$ is a wormhole connecting the bra and ket

\[ \rho_\text{NB}=\ \mathrel{\raisebox{-0.5\height}
 {\class{l2mpic-0}{\rule[-0.0000em]{7.8326em}{8.8073em}}}} \]

(1.3)

where the observer’s worldline is drawn in orange and the Cauchy slices in blue. Crucially, the leading no-
boundary topology (two hemispheres) is forbidden by the connectivity of the observer worldline. This is in
line with recent discussions of the rules for the gravitational path integral in the presence of an observer
[36, 37, 38]. We will present a general path integral argument for $\rho_\text{NB}=\mathbb{1}$. Intuitively,
this path integral gives the identity operator because time evolution in gravity acts trivially, as the
Hamiltonian is a constraint $H_{\text{WDW}}=0$.

### [sect-1.intro-p8] paragraph

In section 3, we check the somewhat formal arguments of section 2 by showing that, for closed universes in
Jackiw-Teitelboim (JT) gravity with $\Lambda < 0$, the path integral that prepares the observer’s no-boundary
state (1.3) indeed matches with matrix elements of the identity operator $\mathbb{1}$ on the physical Hilbert
space.

### [sect-1.intro-p9] paragraph

We believe that (1.3) is not only consistent with, but is actually the natural extension of the sphere
preparation of the no-boundary state for the de Sitter static patch with an observer [8], schematically drawn
by

\[ \rho_\text{NB}= \ \mathrel{\raisebox{-0.5\height}{\class{l2mpic-1}{\rule[-0.0000em]{7.8326em}{8.4864em}}
}} \]

(1.4)

The observer’s observations are limited by a causal horizon, so the matrix elements of $\rho_\text{NB}$ are
between two Cauchy slices of the causal diamond (blue). We use the null boundaries of the diamond in order to
have an invariantly defined subregion related to the observer in more general spacetimes, as will become clear
in section 4. Semiclassically, this path integral prepares the Bunch-Davies state for the static patch. In
both (1.3) and (1.4), the path integrals describe the leading topology for the observer’s no-boundary
proposal. However, as in the de Sitter case, the observer causal access is bounded by a horizon, the leading
topology is a sphere. One can interpret (1.4) as the “partial trace” of (1.3) to a properly defined region.
Section 4 is devoted to generalizing the path integral arguments of section 2 to invariantly defined
subregions of closed spacetimes, which naturally reproduces and extends results from [8] and [24] to more
general cases where the observer has causal horizons.

### [sect-1.intro-p10] paragraph

In principle, it should be possible to explicitly check our claim for the case of an observer with causal
horizons in the perturbative $G\to 0$ limit. One would like to consider examples of such spaces that are not
pure de Sitter (dS), construct the observer’s algebra and check that the tracial state is indeed prepared by
the no-boundary path integral. So, one would like to generalize the construction of [8, 7] beyond dS. One key
ingredient in their construction was the KMS property of correlation functions on the worldline of the
observer. In section 5, we show there is no KMS state for worldline correlation functions for any
asymptotically de Sitter geometry besides de Sitter itself. We speculate that the notion of “weak KMS” which
is generally satisfied by worldline correlation functions prepared by a no-boundary geometry might, however,
suffice to define the trace explicitly.

### [sect-1.intro-p11] paragraph

In the discussion (section 6) we discuss intriguing classical FLRW wormhole solutions that contribute to the
no-boundary density matrix. We believe that these are a good testing ground for the ideas of sections 4 and 5.
We point out new questions that these solutions pose.

## [sect-2.obscomplete] section: 2 Observers with complete causal access
### [sect-2.obscomplete-p1] paragraph

In this section, we consider the observer’s no-boundary state in the case where the observer has complete
causal access. For example, consider a semiclassical spacetime where an observer, whose worldline extends
infinitely to the future and past, has causal access to a complete Cauchy slice in a closed universe such that
the Penrose diagram is as in figure 1. Because the observer sees the global quantum state at some time, they
have complete information about the quantum state at all times by Schrödinger evolution. The observer’s
algebra will be type I because their exist pure states.

### [fig-complete1] figure: Figure 1

Figure 1. Penrose diagram for an observer (orange) with complete access to a Cauchy surface (blue). Explicit
solutions with this Penrose diagram are described in section 6.

### [sect-2.obscomplete-p2] paragraph

The main goal of this section is to argue that the gravitational path integral prepares the identity matrix on
a complete Cauchy slice when imposing the no-boundary rules, (1.1). We first detail why this occurs while
ignoring the effects of topology change. In section 2.1, we explain that the observer’s no-boundary state is a
mixed state and gets its leading contribution from geometries directly connecting the bra and ket boundary
conditions. Crucially, the usual Hartle-Hawking no-boundary geometry does not contribute. In section 2.2, we
then show explicitly that $\rho_\text{NB}=\mathbb{1}$. The basic point is that the gravitational path integral
that computes matrix elements of $\rho_\text{NB}$ is the same path integral that computes inner products. In
section 2.3, we show that the Arnowitt–Deser–Misner (ADM) formalism leads to the same conclusion. In section
2.4, we explain that this property is not affected by taking into account topology change. The arguments in
this section are general, and so necessarily somewhat abstract. We complement this by working out the details
explicitly for JT gravity in section 3.

### [sect-2.1] section: 2.1 Nothing but bra-ket wormholes
#### [sect-2.1-p1] paragraph

Matrix elements of the no-boundary state are specified by the induced metric, the configuration of the quantum
fields, and the observer on a Cauchy slice. We will collectively denote these boundary conditions as $\phi$.3
One then sums (path integrates) over all configurations with no additional spacetime boundaries. The action of
the observer taken to be

\[ \begin{align*}
 I_\text{obs} =\int_{\gamma}\d\tau\left(p\frac{\d q}{\d\tau}-\sqrt{-g_{\tau \tau}}(m+q)\right),
 \tag{2.1}\end{align*} \]

where $\gamma$ is the worldline parametrized by $\tau$ and the mass $m$ is large in cosmological units buts
small in Planck units so that the geodesic approximation is valid without significant backreaction. $q>0$ is
the observer’s energy, which could have (in the idealized limit) any non-negative real value.

#### [sect-2.1-p2] paragraph

Our first observation is that for the observer’s no-boundary state, where one considers Cauchy slices with one
observer present, there are no “no-boundary” field configurations of the usual type imagined by Hartle and
Hawking, where spacetime caps off in the (complex) past of the Cauchy slice. Indeed, without a second
boundary, the observer worldline has no place to end

\[ \begin{align*}
    \class{l2mpic-3}{\rule[-0.0000em]{5.2460em}{2.1581em}}
 \tag{2.2}\end{align*} \]

In order to make sense of the observer’s no-boundary state, we propose that one must instead consider the
density matrix, rather than only consider pure states. In a density matrix, one specifies boundary field
values for both the bra and the “ket,” as follows

\[ \begin{align*}
    \class{l2mpic-4}{\rule[-0.0000em]{5.2460em}{6.5393em}}
 \tag{2.3}\end{align*} \]

There now exist configurations where the observer worldline stretches from the bra to the “ket.” The
connection between the bra and ket implies that the no-boundary state is a mixed state. Such bra-ket wormhole
configurations were previously considered as contributions to the no-boundary density matrix [40, 41, 42]. The
important distinction with our setup is that, for the observer’s density matrix, the usual Hartle-Hawking
disconnected contribution never exists. The connected (wormhole) solution always provides the leading
contribution to the path integral.

#### [sect-2.1-p3] paragraph

In summary, the observer’s no-boundary state is computed by the path integral over spacetimes with wormhole
topology $\mathcal{M}\times I$ and the specified boundary conditions. Denoting the bulk metric, quantum
fields, and observer data by $\phi_\text{bulk}$, matrix elements of $\rho_\text{NB}$ are schematically
computed as

\[ \begin{align*}

\bra{\phi''}\rho_{NB}\ket{\phi'} = \int \mathcal{D}\phi_\text{bulk}\quad
\raisebox{-0.47\height}{\class{l2mpic-5}{\rule[-0.0000em]{13.1012em}{8.8073em}}}. \tag{2.4}\end{align*} \]

Contributions from spacetimes with topology change will be included in section 2.4. We have not specifed
whether the path integral is over Lorentzian, Euclidean, or complex spacetimes connecting the bra and ket
because our conclusions to not rely on this, only on the assumption that there does exist a well-defined
contour of integration. Several contours have been considered for bra-ket wormholes in two-dimensional gravity
in [42, 43]. A simple way of thinking about bra-ket wormholes is to consider a purely Lorentzian geometry that
connects two time slices of the same classical geometry. The data on one of these slices represents the bra
boundary condition and the data on the other time slice represents the ket boundary conditions. This
Lorentzian way of thinking about bra-ket wormholes is directly related with our Hamiltonian discussion in
section 2.3. In section 3, we demonstrate the equivalence of the Lorentzian and Euclidean descriptions of bra-
ket wormholes in JT gravity.

### [sect-2.2] section: 2.2 The no-boundary state is the identity
#### [sect-2.2-p1] paragraph

With the path integral definition of the observer’s no-boundary state (2.4), we would now like to argue that
$\rho_\text{NB}=\mathbb{1}$. The simplest way to argue this is to think about the inner product in quantum
gravity. A natural candidate is the inner product induced by the gravitational path integral [9], filling in
the bulk region in all possible ways that has the prescribed states as boundary conditions

\[ \begin{align*}
 \bra{\phi''}{\phi'}\rangle = \int \mathcal{D}\phi_\text{bulk}\,\,\,\,\raisebox{-0.46\height}{\class{l2mpic-
6}{\rule[-0.0000em]{10.5146em}{6.8142em}}}.
 \tag{2.5}\end{align*} \]

In particular, one generally only includes geometries in the inner product that have no other boundaries.
Since in $\phi_\text{bulk}$ one path integrates over all spacetimes with the relevant boundary conditions, we
see that this is the same equation as for the matrix elements $\bra{\phi''}\rho_\text{NB}\ket{\phi'}$.
Therefore

\[ \rho_\text{NB}=\mathbb{1}. \]

(2.6)

Using the gravitational path integral as an inner product is fairly uncontroversial. Therefore, we believe the
same is true for the statement that the observer’s no-boundary state is the identity matrix.

#### [sect-2.2-p2] paragraph

It is important to explain on which Hilbert space this is the identity matrix. In quantum gravity, we must
distinguish the space of boundary conditions from the physical Hilbert space [44]. The physical Hilbert space
is labeled (roughly speaking) by the space of boundary conditions modulo diffeomorphisms. This includes time-
like diffeomorphisms generated by the Wheeler-DeWitt (WDW) Hamiltonian constraint [5], which evolves between
different Cauchy slices in the same geometry. The observer’s no-boundary state is the identity on the physical
Hilbert space which we label $\ket{\psi}$. As we have explained, there is an equivalence class of boundary
conditions $\psi$ (related by diffeomorphisms) associated with $\ket{\psi}$. These statements will be further
clarified in section 2.3.

#### [sect-2.2-p3] paragraph

To drive home the point that $\rho_\text{NB}=\mathbb{1}$, we will investigate the square of the density
matrix. In quantum field theory path integrals, matrix multiplication is achieved by gluing the ket of one
matrix to the bra of the other by path integrating over boundary conditions $\phi$. The situation is more
subtle in quantum gravity. Instead of gluing by integrating over all boundary conditions, one should only
integrate over boundary conditions modulo diffeomorphisms. This reflects matrix multiplication in the physical
Hilbert space by avoiding overcounting which could arise, for instance, by gluing the same geometry on
different Cauchy slices (which are related by gauge transformations) [44]. Matrix elements of the square of
the observer’s no-boundary state are therefore computed as4

\[ \bra{\phi''}\rho_\text{NB}^2\ket{\phi'}=\underset{\substack{\text{boundary conditions}\\\text{modulo diffeomorphisms}}}{\int\mathcal{D}\psi}\, \bra{\phi''}\rho_\text{NB}\ket{\psi}\bra{\psi}\rho_\text{NB}\ket{\phi'}\,. \]

(2.7)

Omitting the integration over bulk fields $\phi_\text{bulk}$ (to avoid clutter), this can be graphically
represented as

\[ \begin{align*}

 \bra{\phi''}\rho_\text{NB}^2\ket{\phi'} = \underset{\substack{\text{boundary conditions}\\\text{modulo
diffeomorphisms}}}{\int\mathcal{D}\psi}\quad
\raisebox{-0.46\height}{\class{l2mpic-7}{\rule[-0.0000em]{21.4857em}{8.8073em}}}, \tag{2.8}\end{align*} \]

where the green slices represent boundary conditions modulo diffeomorphisms in contrast to the blue slices
which are any fixed boundary conditions. Hence, the prescription in the gravitational path integral to compute
$\bra{\phi''}\rho_\text{NB}^2\ket{\phi'}$ is to path integrate over all configurations with wormhole topology
$\mathcal{M}\times I$ with boundary conditions $\phi'$ and $\phi''$. This is identical to the computation of
$\bra{\phi''}\rho_\text{NB}\ket{\phi'}$ in (2.4). Therefore

\[ \rho_\text{NB}^2=\rho_\text{NB}. \]

(2.9)

This leads to the conclusion that the no-boundary density matrix is a projector on the physical Hilbert space,
i.e. $\rho_{\text{NB}} =\mathbb{1}$.

#### [sect-2.2-p4] paragraph

It is instructional to compare the squaring of $\rho_{\text{NB}}$ to the squaring of similar-looking path
integrals in non-gravitational quantum field theories. As a simple example, consider the path integral in a
quantum field theory on a manifold $\mathcal{M}\times [0,\beta]$. This density matrix is a Gibbs state at
inverse temperature $\beta$

\[ \begin{align*}
 \bra{\phi''}e^{-\beta H}\ket{\phi'} = \int\mathcal{D}\phi_\text{bulk}\quad
\mathrel{\raisebox{-0.5\height}{\class{l2mpic-8}{\rule[-0.0000em]{10.0497em}{4.2116em}}}}.
 \tag{2.10}\end{align*} \]

The square of this density matrix is the Gibbs state at inverse temperature $2\beta$, $e^{-2\beta H}$

\[ \begin{align*}
 \bra{\phi''}e^{-2\beta H}\ket{\phi'} = \int\mathcal{D}\phi_\text{bulk}\quad
\mathrel{\raisebox{-0.5\height}{\class{l2mpic-9}{\rule[-0.0000em]{10.2986em}{6.7982em}}}}.
 \tag{2.11}\end{align*} \]

This is clearly not a projector unless $H=0$. One case where $H = 0$ (besides gravity) is topological quantum
field theory. The analogy between gravity and standard topological quantum field theory however no longer
holds when including topology change, see section 2.4.

#### [sect-2.2-p5] paragraph

The norm of the no-boundary state is formally given by the trace

\[ \begin{align*}
 \Tr \rho_\text{NB} = \underset{\substack{\text{boundary conditions}\\\text{modulo
diffeomorphisms}}}{\int\mathcal{D}\psi}\int \mathcal{D}\phi_\text{bulk}\,\,\,\raisebox{-
0.47\height}{\class{l2mpic-10}{\rule[-0.0000em]{12.9292em}{8.8073em}}}.
 \tag{2.12}\end{align*} \]

This computes the gravitational path integral on $\mathcal{M}\times S_1$. In many cases, including JT gravity
discussed in section 3, the answer is divergent. In these cases, the no-boundary state is more properly
referred to a “weight,” which is an unnormalizable state, like a position eigenstate of the harmonic
oscillator.

#### [sect-2.2-p6] paragraph

In cases where there is a dominant saddle point, the norm is approximately $e^{-I}$, with $I$ the on-shell
action. We may evaluate the von Neumann entropy, as defined via the relative entropy, of the unit normalized
observer’s no-boundary state $\tilde \rho_\text{NB} \equiv \left(\text{Tr} \rho_\text{NB}\right)^{-1}
\rho_\text{NB}$

\[ \begin{align*}
 S_\text{vN}(\tilde \rho_{\text{NB}}) \equiv -S_\text{rel}(\tilde \rho_{\text{NB}}\parallel\rho_\text{NB} )=
-S_\text{rel}(\tilde \rho_{\text{NB}}\parallel\tilde \rho_{\text{NB}} ) -I= -I\,,
 \tag{2.13}\end{align*} \]

as well as the entropy of any normalized state $\rho$

\[ \begin{align*}
S_\text{vN}(\rho) = - S_\text{rel}(\rho  \parallel  \tilde{\rho}_{\text{NB}}) -I. \tag{2.14}\end{align*} \]

In section 6, we discuss an explicit example of this, an Einstein static universe. In that case, the classical
action, $I$, is zero. This is consistent with there being no additive constant in states of a type I algebra.

### [sec-canonical_quant] section: 2.3 Lorentzian quantum gravity and the lapse contour
#### [sec-canonical_quant-p1] paragraph

In this section we present an alternative (though more heuristic) derivation of (1.1), still ignoring topology
change. In particular, we detail how to compute the inner products between boundary states $\ket{\phi}$ in
quantum gravity and show that this inner product is implemented by a Lorentzian path integral over spacetimes
of topology $\mathcal{M}\times I$ which we argued computes the no-boundary state (2.4).

#### [sec-canonical_quant-p2] paragraph

Consider first the Lorentzian path integral in the ADM formalism [45, 46] (see also [47] for relevant
discussion), where the metric is parameterized in terms of the induced metric $g_{ij}$, the lapse $N$ and
shift vector $N^j$

\[ \begin{align*}
 \d s^2 = -N^2 \d t^2 + g_{ij}(\d x^i + N^i \d t)(\d x^j +N^j \d t)\,, \tag{2.15}\end{align*} \]

all functions of $t$, $x^i$. Introducing conjugate momenta $\Pi_{i j} = -\i \delta/\delta g_{ij}$ for the
induced metric one finds the Lorentzian action simply takes the form

\[ I= \int \d t \d^3 x \bigg( \Pi^{ij}\dot g_{ij} -N H_\text{WDW}-\sum_i N^i P_i\bigg)\,. \]

(2.16)

Here $H_\text{WDW}$ is a function on phase space called the Hamiltonian constraint

\[ \begin{split}
 H_\text{WDW}
 &= -R(g)+2\Lambda + \frac{(16\pi G)^2}{\det g} \left(\Pi_{ij}\Pi^{ij}-\Pi_i^i \Pi_j^j \right)+\text{matter
contributions}\,,
\end{split} \]

(2.17)

with $R(g)$ the three-dimensional Ricci scalar. Crucially, the action does not depend on time derivatives of
$N$ and $N^j$ and they do not appear in the phase space. Written in a Hamiltonian form, the Lorentzian path
integral on spacetimes over topology $\mathcal{M}\times I$ with boundary conditions $\phi'$ and $\phi''$
therefore becomes

\[ \bra{\phi''}\rho_\text{NB}\ket{\phi'}= \bra{\phi''}\frac{1}{2\pi}\int_{-\infty}^{+\infty}\d N\,e^{-\i H_\text{WDW} N }\ket{\phi'}\,. \]

(2.18)

Here, we made the gauge choice that $t$ in (2.15) runs between $-1/2$ on one Cauchy slice and $1/2$ on the
other Cauchy slice, and gauged-fix the lapse function to be $t$-independent (see [48] for more details).
Furthermore, we consider a minisuperspace truncation where the entire metric is homogeneous (otherwise one
path integrates over $N(x^j)$) and we left implicit the integrals over the shifts implementing the so-called
momentum constraints $P_i=0$ in the path integral.

#### [sec-canonical_quant-p3] paragraph

Equation (2.18) demonstrates that the Lorentzian no-boundary path integral implements a “rigging map” $\eta$
[49]

\[ \rho_\text{NB}=\eta=\frac{1}{2\pi}\int_{-\infty}^{+\infty}\d N\,e^{-\i H_\text{WDW} N }=\delta(H_\text{WDW})\,. \]

(2.19)

There has been discussion in the literature regarding the contour of this lapse integral, for instance [50,
51, 52]. However, the most reasonable answers are obtained when integrating $N$ from $-\infty$ to $+\infty$.
One a priori reason for this contour is that this results in a Hermitian density matrix. Another reason is
that, in the spirit of gauging spacetime inversions [53], the bra and ket should be on equal footing in terms
of their time ordering. In other words, we should consider Lorentzian geometries where one first encounters
the data $\phi'$ at $t=-1/2$ and later the data $\phi''$ at $t=+1/2$, but also Lorentzian geometries where one
encounters the data $\phi''$ at $t=-1/2$ and only later the data $\phi'$ at $t=+1/2$. This effectively means
one should integrate over $N>0$ and $N<0$ in Lorentzian quantum gravity.

#### [sec-canonical_quant-p4] paragraph

This may naively seem in tension with the fact that we can alternatively compute the no-boundary state using
the Euclidean path integral, where one imagines integrating in some sense only over positive lapses $N>0$. To
accommodate the potentially skeptical reader, we will show explicitly in section 3 that the Lorentzian and
Euclidean path integrals agree for AdS JT gravity both with and without an observer.

#### [sec-canonical_quant-p5] paragraph

We now explain in which sense (2.19) is consistent with our earlier claim that $\rho_\text{NB}=\mathbb{1}$. To
do so, we must distinguish two Hilbert spaces relevant in quantum gravity.5 We will take the minisuperspace
approximation of a single constraint $H_\text{WDW}$. The “auxiliary” Hilbert space, $\mathcal{H}_0$, is
roughly speaking the square-integrable functions on the set of boundary conditions, with states that we
labelled $\ket{\phi}$. The physical Hilbert space, $\mathcal{H}$, is the set of physical states, which we
label $|\psi\rangle\!\rangle$. The physical Hilbert space can be understood as obtained from $\mathcal{H}_0$
by identifying states that differ by a “gauge transformation” [55, 56, 57, 58, 59, 60, 61]

\[ \begin{align*}
 \ket{\psi} \sim \ket{\psi}+ H_\text{WDW} \ket{\phi}.
 \tag{2.20}\end{align*} \]

This leads to a Hilbert space of equivalence classes called co-invariants $|\psi\rangle\!\rangle$. The inner
product on these co-invariants is given by the rigging map [55, 56, 57, 58, 59, 60, 61]6

\[ \begin{align*}
\langle\!\langle{\psi'}|\psi\rangle\!\rangle =\bra{\psi'}\eta \ket{\psi}\,. \tag{2.21}\end{align*} \]

Thus, we find that in the Lorentzian path integral, the no-boundary state (2.19) implements an inner product
and, from the right-hand-side of (2.21), that it implements the identity operator on $\mathcal{H}$. This can
be understood directly by realizing that in (2.19), $\delta(H_\text{WDW})$ is a projector onto the physical
Hilbert space $\mathcal{H}$.

#### [sec-canonical_quant-p6] paragraph

Consider a basis for $\mathcal{H}_0$, $\{ \ket{E,\alpha} \}$, where $E$ is the eigenvalue of $H_\text{WDW}$
and $\alpha$ labels the rest of the quantum numbers. The physical Hilbert space, $\mathcal{H}$, is understood
as the eigenspace spanned by $\{\ket{0,\alpha}\}$. If $a$ is a physical operator, i.e one that commutes with
$\mathcal{H}_\text{WDW}$, then its expectation value in the no-boundary state is

\[ \begin{split}
 \text{Tr}_{\mathcal{H}_0}\left(\rho_\text{NB} a\right) & = \sum_\alpha \int dE \bra{E,\alpha}
\delta(H_\text{WDW}) a \ket{E,\alpha}\\
 &= \sum_\alpha \bra{0,\alpha} a \ket{0,\alpha} = \text{Tr}_\mathcal{H}(a).
\end{split} \]

(2.22)

In the second line, we used that $a$ commutes with $H_\text{WDW}$ and thus acts diagonally on $E$ eigenstates.
Comparing the first and last equality, we see that $\rho_\text{NB}$, as a density matrix in $\mathcal{H}_0$,
is identified with the identity matrix in $\mathcal{H}$.

### [sect-2.4topo] section: 2.4 Including topology change
#### [sect-2.4topo-p1] paragraph

Thus far we have not considered the impact of topology change. Unfortunately, we do not know how to include
topology changing processes in the Hamiltonian description of section 2.3. However, they are naturally
included in the gravitational path integral, and appear to be necessary for recovering the expected physics of
quantum gravity [64, 65, 19, 20]. The basic argument of section 2.2 remains valid with topology change.

#### [sect-2.4topo-p2] paragraph

We first note a contributions to the path integral of the forms7

\[ \begin{align*}
\raisebox{0.25\height}{\class{l2mpic-11}{\rule[-0.0000em]{16.8857em}{6.5393em}}}
\quad \raisebox{1cm}{\text{,}} \quad
 \class{l2mpic-12}{\rule[-0.0000em]{16.8857em}{9.7097em}}
 \tag{2.23}\end{align*} \]

are disallowed by the gravitational path integral rules for the observer in [36, 37] and are exponentially
suppressed in the entropy of the observer in the rules of [38]. Indeed, without these rules, the gravitational
path integral appears to imply that the Hilbert space of closed universes is one-dimensional [18, 19, 66, 67].
In that case, the no-boundary state is a pure state and is trivially the identity matrix.

#### [sect-2.4topo-p3] paragraph

Now suppose that we compute the gravitational inner product between two states specified by boundary data
$\phi'$ and $\phi''$. In gravity, one computes inner products by filling in the region between the boundary
conditions with all possible spacetimes, including higher topologies. This is again the same calculation one
would do to compute matrix elements of the observer’s no-boundary state

\[ \bra{\phi''}\rho_\text{NB}\ket{\phi'}=~~~\mathrel{\raisebox{-0.5\height}{\class{l2mpic-13}{\rule[-0.0000em]{23.3390em}{9.8037em}}}} \]

(2.24)

Therefore $\rho_\text{NB}=\mathbb{1}$ even after including topology change. It is important that when
including topology change, the sum over geometries remains over spacetimes without boundary.

#### [sect-2.4topo-p4] paragraph

We have focused on the Hilbert space of a single closed universe. This is because the observer only lives in a
single universe. One may attempt to include baby universes in the path integral, but following the same logic
as [18, 19, 66, 67], one will find that including these does not change the dimension of the Hilbert space,
which is dictated only by the universe with the observer. In this case, time evolution also generates topology
change. Therefore, even data $\phi'$ and $\phi''$ on spatial manifolds $\mathcal{M}'$ and $\mathcal{M}''$ with
different topologies can be gauge equivalent.

#### [sect-2.4topo-p5] paragraph

When including topology change, quantum gravity is distinct from topological quantum field theory because in
topological field theory, one does not naturally sum over topologies.8 More precisely, in topological field
theory one does not sum over geometries to compute an inner product between states, and even if one did, one
would not allow topologies to connect different copies of an inner product calculation as one does in gravity
when determining the dimensional of the Hilbert space via the replica trick.

## [sect-4.JT] section: 3 Closed universes in JT gravity
### [sect-4.JT-p1] paragraph

In section 2, we argued on general grounds that the observer’s no-boundary density matrix is the identity
operator. As a consequence of their generality, the arguments were necessarily formal. Here, we complement
that discussion with explicit checks in JT gravity with $\Lambda < 0$. Previous work on algebras in JT gravity
with $\Lambda < 0$ has focused on open universes [69, 70, 71]. In JT gravity, the Euclidean path integral that
computes the no-boundary density matrix (2.4) can be done exactly. We will match these Euclidean wormhole
amplitudes [65, 72, 73, 74] with the matrix elements of the identity operator $\mathbb{1}$ on the physical
Hilbert space. As in section 2, we first consider no topology change. Topology change will be included in
section 3.4.

### [fig-perogi] figure: Figure 2

Figure 2. The Lorentzian spacetime with metric (3.2) with big bang and big crunch singularities. The time-
reflection symmetric surface has the maximal length, $b$.

### [sect-4.JT-p2] paragraph

JT gravity is a theory of two-dimensional dilaton gravity with action

\[ I = \frac{1}{2}\int \d x \sqrt{g}\, \Phi (R+2)+\text{boundary terms}\,. \]

(3.1)

The classical Lorentzian metric solutions are collapsing Milne universes with singularities at $t=\pm \pi/2$

\[ \d s^2=b^2\cos(t)^2\,\d x^2-\d t^2\,,\quad -\frac{\pi}{2}<t<\frac{\pi}{2}\quad \]

(3.2)

as shown in figure 2. We consider adding a quantum mechanical observer to this spacetime. This observer is
perceived in the gravitational theory as a minimally coupled matter particle with energy $q$. For clarity’s
sake, both in our discussion of the Hilbert space and of the gravitational path integral, we first consider JT
gravity without this observer particle.

### [sect-3.1HJT] section: 3.1 Hilbert spaces
#### [sect-3.1HJT-p1] paragraph

We first review the Hilbert space of closed universes in JT gravity with $\Lambda < 0$, which was discussed in
detail in [54].9$^,$10 In ADM variables, the most general metric configuration is

\[ ds^2 = -N^2 \d t^2 + a^2 (\d x+N_\perp \d t)^2\,,\quad x\sim x+1\,. \]

(3.3)

Following section 2.3, integrating $N$ and $N_\perp$ over the real line imposes the local Hamiltonian and
momentum constraints, which are the generators of timelike and, respectively, spacelike diffeomorphisms. The
canonical conjugates of $a$ and $\Phi$ are $p$ and $k$,

\[ \begin{align*}
 [a,p]=\i, \quad [\Phi,k]=\i.
 \tag{3.4}\end{align*} \]

We can gauge-fix $k$ and $a$ to be $x$-independent. The constraints then fix $\Phi$ and $p$ to also be
$x$-independent [54]. This leaves us with a four-dimensional phase space of $x$-independent $(a,\Phi,p,k)$
that exactly describes JT gravity [76]. In this description, all that remains from the constraints is the
global Hamiltonian constraint

\[ H_\text{WDW}=-p k -a \Phi=0\,. \]

(3.5)

The space of boundary conditions is two-dimensional. For instance, we can fix the length $a$ of the slice and
the dilaton $\Phi$. As discussed in section 2.2 and 2.3, this auxiliary Hilbert space is larger than the
physical Hilbert space. The latter is spanned by solutions of the Wheeler DeWitt equation,
$H_{\text{WDW}}\ket{\psi} = 0$, which may be found by diagonalizing an operator which commutes with
$H_\text{WDW}$, for instance

\[ b=\sqrt{a^2+k^2}\,. \]

(3.6)

This has the geometric meaning of the maximal size of the universe (3.2). Indeed, the classical solutions are
$a=b\cos(t)$ and $k=b\sin(t)$. In this parameterization, one obtains

\[ H_\text{WDW}=-\i \frac{\d}{\d t}\,, \]

(3.7)

so the WDW constraint generates timelike diffeomorphisms. Data that corresponds to different time slices in
the same geometry describe the same quantum state. Thus, we can label physical states by $b$. The
wavefunctions that diagonalize $b$ and $H_\text{WDW}$ are

\[ \psi_b(a,\Phi)
 = \frac{1}{\sqrt{2\pi}}\frac{1}{\sqrt{b^2-a^2}}e^{\i \Phi \sqrt{b^2-a^2}}\, \equiv \langle a,\Phi | b\rangle
. \]

(3.8)

In the range of Euclidean wormholes solutions $t=\i \rho$ where $a>b$ this becomes

\[ \psi_b(a,\Phi)
 =\frac{1}{\sqrt{2\pi}}\frac{1}{\sqrt{a^2-b^2}}e^{- \Phi \sqrt{a^2-b^2}}\,. \]

(3.9)

This will be used in section 3.2. The inner product of physical states is computed using the expectation value
of the rigging map (2.19)

\[ \eta=\frac{1}{2\pi}\int_{-\infty}^{+\infty}\d N\,e^{-\i H_\text{WDW} N }\,. \]

(3.10)

Alternatively, one can do a Faddeev–Popov gauge-fixing which results in the usual Klein-Gordon inner product
on superspace [44]. A convenient gauge-fixing for this calculation is to consider $a=0$ [75]. This immediately
gives

\[ \begin{split}
 \braket{b_1|b_2} & = -\frac{\i}{2}\int_{-\infty}^{+\infty} \d\Phi \bigg( \psi_{b_1}^*\frac{\d}{\d
\Phi}\psi_{b_2}-\psi_{b_2}\frac{\d}{\d \Phi}\psi_{b_1}\bigg)
 = \frac{1}{b_1} \delta(b_1-b_2).
\end{split} \]

(3.11)

The identity matrix on the physical Hilbert space is therefore

\[ \begin{align*}

 \mathbb{1} = \int \d b\, b \ket{b}\bra{b}\,. \tag{3.12}\end{align*} \]

#### [sect-3.1HJT-p2] paragraph

We now introduce one matter particle which represents the observer. Useful background and related comments can
be found in [54, 69, 70, 77]. Matter does not couple to the dilaton $\Phi$, so the classical solutions are
unaffected. We continue working in the same gauge for the geometric data. The location of the matter particle
(observer) on the Cauchy slice is determined by an angular coordinate $\tau \sim \tau+b$ with $x=b \tau$.
Before imposing the constraints, the phase space consists of $a,\Phi, \tau,q$ and their conjugates. One might
now be tempted to claim that the Hilbert space consists of states $\ket{b}$ describing the spacetime, tensored
with the Hilbert space of a matter particle on each fixed geometry. This would indeed be the case for open
Cauchy slices in JT gravity describing eternal black holes [69, 70]. The states would then be labeled
$\ket{b,\tau,q}$, or upon Fourier transforming $\ket{b,k,q}$.11 However, we should recall that spatial
translations are a gauge symmetry in gravity. Therefore, phase space is also subject to a momentum constrain,
which in the presence of a matter particle reads [54]

\[ P_\text{matter}=k=0\,, \]

(3.13)

so the physical Hilbert space for a single particle is spanned by the states $\ket{b,k=0,q}$.12 The resolution
of the identity is

\[ \begin{align*}

 \mathbb{1} = \sum_q\int \d b\, b \ket{b,k=0,q}\bra{b,k=0,q}\,. \tag{3.14}\end{align*} \]

It would be very interesting to give this observer access to matter quantum field theory operators along their
worldline, but this goes beyond our present goals.

### [subsect-JT1empty] section: 3.2 The no-boundary state
#### [subsect-JT1empty-p1] paragraph

A static observer in the spacetime (3.2) has complete causal access. In section 2, we explained that in such a
scenario the observer’s no-boundary state equals the identity on the physical Hilbert space

\[ \rho_\text{NB}=\mathbb{1}. \]

(3.15)

We will now compute matrix elements of the no-boundary state in JT gravity using the Euclidean path integral
and show that they are consistent with the Hilbert space discussion of section 3.1, supporting the general
claim of section 2.

#### [subsect-JT1empty-p2] paragraph

For clarity, we will first consider the no-boundary state without an observer. However, to facilitate
comparison with the observer’s no-boundary state, we will still consider the cylinder topology instead of the
disc

\[ \bra{a_1,\Phi_1}\rho_{\text{NB}}\ket{a_2,\Phi_2} = \raisebox{-0.5\height}{\class{l2mpic-15}{\rule[-0.0000em]{10.1796em}{6.8399em}}} \]

(3.16)

We will comment on the Lorentzian calculation towards the end of this section. The path integral of JT gravity
on Euclidean wormholes can be computed following [65] by separating it into two “trumpets” that are connected
at the geodesic $b$ and including the appropriate Weil-Peterson measure

\[ \bra{a_1,\Phi_1}\rho_{\text{NB}}\ket{a_2,\Phi_2}=\int_0^\infty \d b\,b\,Z_\text{trumpet}(b,a_1,\Phi_1)Z_\text{trumpet}(b,a_2,\Phi_2)\,. \]

(3.17)

The trumpet partition functions with finite $a$ and $\Phi$ can be computed by a certain deformation of the
Schwarzian path integral [79]

\[ \raisebox{-0.5\height}{\class{l2mpic-16}{\rule[-0.0000em]{7.6785em}{4.0327em}}} = Z_\text{trumpet}(b,a,\Phi)\,. \]

(3.18)

The calculation is greatly simplified by considering a subclass of boundary conditions corresponding with
asymptotically Euclidean AdS [80, 81, 82],

\[ a = \frac{\beta}{\varepsilon}, \quad \Phi = \frac{1}{2\varepsilon}\,,\quad \varepsilon\to 0\,. \]

(3.19)

Upon renormalization in the $\varepsilon\rightarrow0$ limit, both the Euclidean wavefunction (3.9) and the
trumpet partition function become [65, 83]

\[ Z_\text{trumpet}(b,\beta)=\psi_b(\beta) = \frac{1}{\sqrt{2\pi\beta}}e^{-b^2/4\beta}. \]

(3.20)

Therefore, asymptotic matrix elements of the no-boundary state (3.17) can be written as

\[ \bra{\beta_1}\rho_{\text{NB}}\ket{\beta_2}=\int_0^\infty\d b\, b\,\psi_b(\beta_1)\psi_b(\beta_2)=\bra{\beta_1}\mathbb{1}\ket{\beta_2}\,, \]

(3.21)

so the wormhole amplitude is indeed the identity operator on the physical Hilbert space. The integration over
$b$ in (3.12) is a simple example of (2.8), with each of the trumpets computing a gauge-fixed matrix element
of one no-boundary density matrix.

#### [subsect-JT1empty-p3] paragraph

The matching (3.21) can readily be extended to finite values of $a$ and $\Phi$. This is because the
gravitational path integral has to satisfy the WDW equation, and so it necessarily decomposes into the basis
of solutions (3.9)

\[ \bra{a_1,\Phi_1}\rho_{\text{NB}}\ket{a_2,\Phi_2}=\int_0^\infty \d b_1\int_0^\infty \d b_2\,\rho_\text{NB}(b_1,b_2)\,\psi_{b_1}(a_1,\Phi_1)\psi_{b_2}(a_2,\Phi_2)\,, \]

(3.22)

with only the expansion coefficient $\rho_\text{NB}(b_1,b_2)$ left to be determined. Investigating this
expression with asymptotic boundary conditions (3.19) is sufficient to uniquely determine this expansion
coefficient

\[ \rho_\text{NB}(b_1,b_2)=\frac{1}{b_1}\delta(b_1-b_2)\,. \]

(3.23)

Similar logic was used to determine the finite cutoff disk amplitude in [79].

#### [subsect-JT1empty-p4] paragraph

We pause to make a comment on the lapse contour. Consider a Lorentzian path integral with boundary conditions
$(\ell_1,k_1)$ and $(\ell_2,k_2)$. The classical solutions (3.2) are $\ell=b\cos(t),\,k=b\sin(t)$. In quantum
gravity, we must sum over all geometries connecting these boundary conditions. Classically, there are two
contributions. Viewing $(\ell_1,k_1)$ as initial boundary condition, the classical solution is (3.2) evolved
for a time $t_2-t_1$. The second contribution comes from viewing $(\ell_2,k_2)$ as the initial condition, in
which case the classical solution is (3.2) evolved for a time $t_1-t_2$. If bras and kets are
indistinguishable,13 both $\braket{\ell_1,k_1|\ell_2,k_2}$ and $\braket{\ell_2,k_2|\ell_1,k_1}$ are non-zero,
indicating that we count solutions with elapsed time $N>0$, and with $N<0$. So, the lapse $N$ is to be
integrated from $-\infty$ to $+\infty$ in the Lorentzian path integral, which is consistent with section 2 and
[50, 52].

### [sect-3.3ONBJT] section: 3.3 The observer’s no-boundary state
#### [sect-3.3ONBJT-p1] paragraph

We next consider the Euclidean path integral with a single particle that represents an observer. In this case,
the finite cutoff amplitude is not known, so we only consider asymptotic boundary conditions (3.19)

\[ \bra{\beta_1,\tau_1,q_1}\rho_\text{NB}\ket{\beta_2,\tau_2,q_2} = \raisebox{-0.5\height}{\class{l2mpic-17}{\rule[-0.0000em]{11.6208em}{6.8510em}}}. \]

(3.24)

This path integral was computed in [84, 72]. We will find it convenient to present the result by an inverse
Laplace transform to fixed energy holographic boundary conditions

\[ \ket{\beta}=\int_0^\infty \d E\,\rho(E)\,e^{-\beta E}\ket{E}\,, \]

(3.25)

with $\rho(E)$ the Schwarzian spectral density [85]. This leads to[86, 78]

\[ \bra{E_1,\tau_1,q_1}\rho_\text{NB}\ket{E_2,\tau_2,q_2} = \frac{\Gamma(\Delta)^2\Gamma(\Delta\pm 2\i\sqrt{E_1})}{\Gamma(2\Delta)}\frac{1}{\rho(E_1)}\delta(E_1-E_2)\,\delta_{q_1 q_2}\, ,\quad \Delta(\Delta-1) = q_1^2\ , \]

(3.26)

where the $\pm$ signify a product over $\Gamma$ functions with both signs.

#### [sect-3.3ONBJT-p2] paragraph

We would like to show that (3.26) is consistent with interpreting the wormhole as an identity operator
(3.14).14 It is useful to rewrite the identity operator with an explicit momentum constraint

\[ \begin{split}
 \mathbb{1}&=\int_0^\infty \d b\,b\ket{b,k=0}\bra{b,k=0}
 =\int_0^\infty \d b\,b\sum_{k=-\infty}^{+\infty}
 \eta_\text{momentum} \ \ket{b,k}\bra{b,k}
 \,,
\end{split} \]

(3.27)

with the momentum rigging map

\[ \eta_\text{momentum}=\frac{1}{b}\int_0^b \d N_\perp\,e^{\i P_\text{matter} N_\perp}. \]

(3.28)

In equation (3.27), we suppressed the $q$ label, and will continue to do so throughout this section to avoid
clutter. To compute the matrix element of (3.27) in asymptotic states $\ket{E,\tau}$, a convenient
intermediate step is to transform from fixed energy $E$ states to fixed asymptotic geodesic length $\ell$
states (see figure 3). The wavefunctions are [87, 86]

\[ \ket{E}=\int_{-\infty}^{+\infty}\d \ell \psi_E(\ell)\ket{\ell}\,,\quad \psi_E(\ell)=K_{2\i E^{1/2}}(e^{-\ell/2})\,, \]

(3.29)

where $K$ is a Bessel function.

#### [fig-teardrop_tikz] figure: Figure 3

Figure 3. Open geodesic $\ell$ (cyan) which ends at the insertion of the observer particle near the asymptotic
boundary (orange) in a spacetime with fixed energy asymptotic boundary conditions. This geodesic is homologous
to a closed geodesic of length $b$ (green). The amplitude for the white and gray regions are (3.29) and (3.33)
respectively.

#### [sect-3.3ONBJT-p3] paragraph

The matrix elements of the identity operator (3.27) in this basis then decompose as

\[ \begin{align*}
 \bra{\ell_1,\tau_1}\mathbb{1}&\ket{\ell_2,\tau_2}=\int_0^\infty\d b \sum_{k=-\infty}^{+\infty}\int_{0}^{b}\d
\tau\, e^{\i k \tau}\braket{\ell_1,\tau_1|b,k}\braket{b,k|\ell_2,\tau_2} \tag{3.30}\\&=\int_0^\infty\d b
\int_{0}^{b}\d
\tau\sum_{k=-\infty}^{+\infty}\braket{\ell_1,\tau_1|b,k}\braket{b,k|\ell_2,\tau_2+\tau}=\int_0^\infty \d b
\braket{\ell_1|b}\braket{b|\ell_2}\int_0^b\d \tau \braket{\tau_1|\tau_2+\tau}_b\,.
\end{align*} \]

Here, $\braket{\tau_1|\tau_2}_b$ is the inner product between matter states obtained by inserting matter
particles in the geometry (3.2) with size $b$. By the definition of $\ket{\ell,\tau}$, the matter states are
prepared by inserting a matter particle of mass $q$ at the asymptotic Euclidean boundary at spatial coordinate
$\tau$, while fixing the length $\ell$ of the geodesic that is homologous to $b$ and ending on the location of
this operator insertion (see figure 3). The matter propagator in this geometry equals15

\[ \braket{\tau_1|\tau_2}_b=G_\Delta(\tau_1,\tau_2)=e^{-(\ell_1+\ell_2)\Delta/2}\sinh(b/2)^{2\Delta}\sum_{w=-\infty}^{+\infty}\frac{1}{\cosh((\tau_2-\tau_1+b w)/2)^{2\Delta}}\,. \]

(3.31)

The sum over $w$ corresponds with the sum of windings of the particle around the spatial circle

\[ \braket{\tau_1|\tau_2}=\raisebox{-0.5\height}{\class{l2mpic-19}{\rule[-0.0000em]{8.8100em}{7.5729em}}
} + \raisebox{-0.5\height}{\class{l2mpic-20}{\rule[-0.0000em]{8.8100em}{7.5729em}}
} + \quad\dots\, . \]

(3.32)

Note that the geometry is completely fixed once we specify $\ell_1$, $\ell_2$, $b$, $\tau_1$, and $\tau_2$.
This allows computation of (3.31), using suitable holographic renormalization. Finally, to compute (3.30), we
need the gravitational transformation from the $b$ basis to the $\ell$ basis which reads16

\[ \braket{\ell|b}=e^{-e^{-\ell/2}\cosh(b/2)}. \]

(3.33)

Defining $\psi_b(\ell)=e^{-\ell \Delta/2}\sinh(b/2)^\Delta \braket{\ell|b}$, one can explicitly compute the
matrix element of the identity operator (3.27) in asymptotic fixed energy basis17

\[ \begin{split}
&\bra{E_1,\tau_1}\mathbb{1}\ket{E_2,\tau_2}\\
 &=\int_0^\infty\d b\int_{-\infty}^{+\infty}\d \ell_1
\psi_{E_1}(\ell_1)\psi_b(\ell_1)\int_{-\infty}^{+\infty}\d \ell_2
\psi_{E_2}(\ell_2)\psi_b(\ell_2)\int_{-\infty}^{+\infty}\d \tau
\frac{1}{\cosh((\tau+\tau_2-\tau_1)/2)^{2\Delta}}\\
 &=
 {4^\Delta}
 \frac{\Gamma(\Delta)^2\Gamma(\Delta\pm 2\i\sqrt{E_1})}{\Gamma(2\Delta)}\frac{1}{\rho(E_1)}\delta(E_1-E_2)\,.
\end{split} \]

(3.37)

This matches with the evaluation of matrix elements of the no-boundary state (3.26) using the Euclidean
gravitational path integral which used different techniques [84, 72].

#### [sect-3.3ONBJT-p4] paragraph

A takeaway point of this calculation is that we learned that the Euclidean gravitation path integral
implements naturally the projector $\eta_\text{momentum}$ (3.28) that imposes the momentum constraint, in
addition to the Hamiltonian constraint (3.10). This was not manifest in earlier calculations of this wormhole
amplitude. The no-boundary state is thus the tracial state on the physical Hilbert space

\[ \begin{align*}
 \Tr ( \cdot )=\int_0^\infty\d b\,b \bra{b,k=0}\cdot \ket{b,k=0}\,.
 \tag{3.38}\end{align*} \]

Of course, one should consider reasonable operators for which this converges, which does not include
e.g. simple functions of $b$.

#### [sect-3.3ONBJT-p5] paragraph

The above construction generalizes to the Hilbert space of closed universes in JT with $n$ matter particles,
which is spanned by states of the form

\[ \ket{b,k_1\dots k_n},\quad \sum_{i=1}^n k_i=0. \]

(3.39)

The matter Fock space is constructed on spacetimes (3.2) specified by the geodesic length $b$. The trace on
the sector with $n$ identical particles is

\[ \Tr(\cdot)=\int_{0}^\infty \d b\,\frac{1}{n!}\sum_{k_1=-\infty}^{+\infty}\dots \sum_{k_n=-\infty}^{+\infty}\int_0^b\d N_\perp\, e^{\i N_\perp (k_1+\dots +k_n)} \bra{b_1,k_1\dots k_n}\cdot \ket{b,k_1\dots k_n}\,. \]

(3.40)

The wormhole with $n$ particles inserted on Euclidean asymptotic boundaries computes an inner product of the
identity in this Hilbert space, but writing out this amplitude is messy for $n>1$.

### [subsect-JT4nonpert] section: 3.4 Including topology change
#### [subsect-JT4nonpert-p1] paragraph

To conclude this section, examine the effect of topology change. To our knowledge, it is not understood what
the WDW Hamiltonian on phase space is that generates topology change. Thus, we limit ourselves to interpreting
the answer of the gravitational path integral as a suggestion for what the relevant Hilbert spaces are. The
fact that we sum over all spacetimes consistent with boundary conditions shows that one can not distinguish
$\rho_\text{NB}$ from $\rho_\text{NB}^2$.

#### [subsect-JT4nonpert-p2] paragraph

We first consider, as in section 3.2, the case of JT gravity without observer. Summing over topologies in the
gravitational path integral, in JT gravity one finds [65]18

\[ \bra{\beta_1}\rho_\text{NB}\ket{\beta_2}=\sum_{i=1}^N e^{-\beta_1 E_i}\sum_{j=1}^N e^{-\beta_2 E_j}\,. \]

(3.43)

We imagine working in one member of the JT ensemble [90, 66, 89], where $E_i$ are fixed eigenvalues. In this
expression, there is no correlation between the bra and the ket $\ket{\beta}$. This admits an interpretation
as inserting an identity operator in a “physical Hilbert space” if and only if that physical Hilbert space is
one dimensional, $\mathcal{H} = \ket{E_1\dots E_N}$, where

\[ \braket{\beta_1|E_1\dots E_N}=\sum_{i=1}^N e^{-\beta_1 E_i}\,. \]

(3.44)

The fact that the Hilbert space without the observer is one-dimensional remains true after we average over
eigenvalues using the matrix integral, roughly speaking because the average of one is one [67]. With the
observer one finds from explicit JT gravity calculations [73, 72]

\[ \bra{\beta_1,\tau_1,q_1}\rho_\text{NB}\ket{\beta_2,\tau_2,q_2}=\sum_{i=1}^Ne^{-(\beta_1+\beta_2)E_i}\frac{\Gamma(\Delta)^2\Gamma(\Delta\pm 2\i \sqrt{E_i})}{\Gamma(2\Delta)}\,\delta_{q_1q_2}\,,\quad \Delta(\Delta-1)=q_1^2\,. \]

(3.45)

The key feature is the diagonal sum over $E_i$ correlating the bra and ket. This admits an interpretation as
inserting a density operator in a “physical Hilbert space” if and only if that physical Hilbert space is (for
a given $q$) $N$ dimensional and spanned by orthogonal states $\{\ket{E_i} \}$. This is a weight because the
algebra is type I$_{\infty}$ ($N = \infty$). For UV completions of JT gravity, such as sine dilaton gravity
[75], the algebra is finite-dimensional, type I$_{N}$, so the no-boundary state is a normalizable state.

## [sect-3obshorizon] section: 4 Observers with causal horizons
### [sect-3obshorizon-p1] paragraph

Thus far, we have considered density matrices for the entire universe. It is important to understand the more
generic case where an observer experiences a horizon, the canonical example being de Sitter space. We will
proceed in two complementary ways. First, we formalize the statement that, if the density matrix on the global
slice is the identity, then the density matrix on a subalgebra is also the identity on that reduced algebra.
We then work more constructively, providing a similar path integral approach to section 2. This serves as a
consistency check because our formal arguments must match known results in de Sitter space derived from a
different direction [8].

### [section-4.1] section: 4.1 The algebraic approach
#### [section-4.1-p1] paragraph

In the perturbative $G\to 0$ limit, we can use semiclassical tools to study the no-boundary proposal. In this
limit, we can consider a specific classical background $\mathcal{M}$ and study the perturbative (GNS) Hilbert
space around it, which we denote $\mathcal{H}_\mathcal{M}$. In the previous sections, we discussed the global
Hilbert space $\mathcal{H}$ involving all possible backgrounds. Here, we will assume the perturbative Hilbert
space $\mathcal{H}_\mathcal{M}$ can be understood as a superselection sector of $\mathcal{H}$, as is familiar
from the quantum error correction interpretation of AdS/CFT [91, 92]. The Hilbert space description
$\mathcal{H}_\mathcal{M}$ should hold for generic low energy excitations in the perturbative limit.

#### [section-4.1-p2] paragraph

Within a superselection sector $\mathcal{H}_\mathcal{M}$ the observer has access to an algebra corresponding
to its causal diamond, $\mathcal{A}_{obs}^{\mathcal{M}}$. $\mathcal{A}_{obs}^{\mathcal{M}}$ and its commutant
on $\mathcal{H}_{\mathcal{M}}$ are subalgebras of a larger algebra of (bounded) operators
$\mathcal{B}(\mathcal{H})$. There is some degeneracy in specifying the commutant, as globally distinct
classical backgrounds can be indistinguishable in the observer’s causal diamond. This is a source of entropy.
One example is Schwarzschild de Sitter space (SdS). There are solutions that consist of $n$ black holes and
$n$ cosmological horizons cyclically glued (see figure 4).

#### [fig-SdS_tikz] figure: Figure 4

Figure 4. SdS with $n = 3$. An observer (orange) cannot distinguish different values of $n$. The arrows denote
a periodic identification.

#### [section-4.1-p3] paragraph

The no-boundary path-integral can be used to define expectation values $\langle ... \rangle_\text{NB}$ for the
observer’s algebra that satisfies the properties of a trace on $\mathcal{B}(\mathcal{H})$

\[ \begin{align*}

 \braket{ab}_\text{NB} = \braket{ba}_\text{NB}\,,\quad \forall a,b \in \mathcal{A}_\text{obs}\,.
\tag{4.1}\end{align*} \]

Let us now consider operators $a$ in $\mathcal{A}_{obs}^{\mathcal{M}}$. If the subalgebra
$\mathcal{A}_{obs}^{\mathcal{M}}$ is type I or II, it has a trace $\text{Tr}(...)$. Assuming that
$\mathcal{A}_{obs}^{\mathcal{M}}$ does not have a center, this trace is unique up to overall rescalings.
Therefore, it must be related with $\rho_\text{NB}$ up to an overall constant19

\[ \langle a \rangle_\text{NB} = \mathcal{Z}'_\mathcal{M} \cdot \text{Tr}(a), \]

(4.2)

with

\[ \mathcal{Z}'_\mathcal{M} = \frac{\mathcal{Z}_\mathcal{M}}{\text{Tr}(\mathbb{1}_{\mathcal{M}})}, \]

(4.3)

and $\mathcal{Z}_\mathcal{M} = \langle \mathbb{1}_{\mathcal{M}} \rangle_\text{NB}$. Recall that the definition
of the no-boundary state is through the gravitational path integral. Therefore, $\mathcal{Z}_\mathcal{M}$ can
be understood as the no-boundary path integral around the saddle $\mathcal{M}$. For example, if we take
$\mathcal{M}$ to be the static patch of de Sitter space, then the no-boundary path integral is dominated by
the sphere partition function. To leading order in $G$, one would find $\log \mathcal{Z}_\mathcal{M} =
\frac{A}{4G}$ [93]. In this case the algebra is type II$_1$, which enables us to canonically choose a
rescaling such that $\text{Tr}(\mathbb{1}_{\mathcal{M}}) = 1$, leading to (ignoring the subleading corrections
to $\mathcal{Z}_\mathcal{M}$)

\[ \langle a \rangle_\text{NB} = e^{\frac{A}{4G}} \cdot \text{Tr}(a). \]

(4.4)

In a more general background however, (4.3) is more subtle. The problem is that generically we expect both
$\mathcal{Z}_\mathcal{M}$ and $\text{Tr}(\mathbb{1})$ to diverge. This happens both when the algebra is type
I$_\infty$ or II$_\infty$, such as in SdS [22], dS with a massless scalar field [94], or inflationary
cosmology [23, 24, 95]. However, we expect that in these cases a proper renormalization scheme renders
$\mathcal{Z}'_\mathcal{M}$ finite. For example, one may regularize the algebra by taking a limit of projection
operators in the trace, as is done in section 2 of [24]. Assuming such a scheme is well-defined and defining
$\langle a \rangle_\text{NB} = \text{Tr}(\rho_\text{obs}^\mathcal{M}\,a)$, we find that

\[ \begin{align*}
\rho_\text{obs}^\mathcal{M} = \mathcal{Z}'_{\mathcal{M}}\mathbb{1}_{\mathcal{M}}.
 \tag{4.5}\end{align*} \]

#### [section-4.1-p4] paragraph

A slightly more general setup with multiple dS vacua as superselection sectors was considered in [7], in which
case (formally, as we are omitting the perturbative and non-perturbative corrections from each sector, and
between the sectors)

\[ \begin{align*}

 \rho_\text{NB} =\bigoplus_{\alpha} e^{\frac{A_{\alpha}}{4G}}\mathbb{1}_{\mathcal{M_{\alpha}}}.
\tag{4.6}\end{align*} \]

When computing the von Neumann entropy of a state in one vacuum $\alpha$, one can appeal to the relative
entropy of this normalized state with respect to the unnormalized no-boundary state $\rho_\text{NB}$

\[ \begin{align*}
 S_\text{vN}(\rho) = -S_\text{rel}(\rho\parallel \rho_\text{NB}) = -S_\text{rel}(\rho\parallel
e^{\frac{A_{\alpha}}{4G}}\mathbb{1}_{\mathcal{M}_{\alpha}})= -S_\text{rel}(\rho\parallel
\mathbb{1}_{\mathcal{M}_{\alpha}})+\frac{A_{\alpha}}{4G}\,.
 \tag{4.7}\end{align*} \]

The first term is the $O(1)$ entropy of [8] and the second term is this $O(1/G)$ contribution that depends on
the subsector. Thus, there is no additive ambiguity when interpreted as an asymptotic expansion. For a general
density matrix (in the full Hilbert space $\mathcal{H}$), the entropy is given by

\[ S_\text{vN}(\rho) = -S_\text{rel}\left(\rho \parallel \rho_\text{NB}\right)
 = -\langle \rho \log \rho \rangle_\text{NB}. \]

(4.8)

Here the normalization used is $\langle \rho \rangle_\text{NB}=1$. Now consider a density matrix $\rho$
affiliated to $\mathcal{A}_{obs}^\mathcal{M}$. By (4.2) the same normalization would mean $\text{Tr}\rho =
(\mathcal{Z}'_\mathcal{M})^{-1}$. Defining the normalized $\tilde \rho = \mathcal{Z}'_\mathcal{M} \cdot \rho$
(with $\text{Tr}\tilde \rho = 1$), we may use (4.2) to find

\[ \begin{split}
 S_\text{vN}(\rho) &=
 \log \mathcal{Z}'_{\mathcal{M}}-S_\text{rel}(\tilde \rho\parallel \mathbb{1}_{\mathcal{M}})= \log
\mathcal{Z}'_{\mathcal{M}}-\text{Tr}\left(\tilde\rho \log \tilde\rho\right).

 \end{split} \]

(4.9)

Here $S_\text{rel}$ is defined using the perturbative trace. If $\mathcal{Z}'_\mathcal{M}$ is dominated by a
classical no-boundary saddle, we find to leading order in $G$ that the entropy is minus the on-shell action of
that saddle

\[ \begin{align*}
 S_\text{vN}(\rho) = \log \mathcal{Z}'_\mathcal{M} +O(1) = -I_{\mathcal{M}} +O(1)\,.
 \tag{4.10}\end{align*} \]

Thus, the no-boundary state enables us to compute absolute entropy.

### [section-4.2] section: 4.2 A qubit example
#### [section-4.2-p1] paragraph

In order to gain further intuition for what is occuring in a completely controllable environment, it is useful
to revisit the Araki-Woods construction of type II algebras [96]. Consider the Hilbert space of $2N$ qubits
$\mathcal{H}_N = (\mathbb{C}^{2N})_R \otimes (\mathbb{C}^{2N})_L$, where the subscripts denote qubits on the
“right” and the “left.” This is the analog of a single $\mathcal{H}_{\mathcal{M}}$ with $N$ playing the role
of $1/G$. We will later generalize to the direct sum of several Hilbert spaces in analogy to $\mathcal{H}$
itself. The complete algebra of operators acting on both sides is type I by construction. We consider a state
that consists of each qubit in the right maximally entangled with the corresponding qubit in the left in a
Bell pair

\[ \begin{align*}

 \ket{\Psi_N} = \frac{1}{2^{N/2}}\bigotimes_i^N(\ket{00}_i + \ket{11}_i). \tag{4.11}\end{align*} \]

The reduced density matrix on the right is given by the identity operator

\[ \begin{align*}
 \rho_R = 2^{-N}\mathbb{1}_R.
 \tag{4.12}\end{align*} \]

As an operator on the joint Hilbert space $\mathcal{H}_N$, this is of course $\rho_R \otimes
\mathbb{1}_L=\tilde{\rho}_R$. This implies that $\ket{\Psi_N}$ is a tracial state for the algebra of operators
acting nontrivially only on right side

\[ \begin{align*}
 \bra{\Psi_N}a_R b_R \ket{\Psi_N} = \bra{\Psi_N}b_R a_R \ket{\Psi_N} , \quad \forall a_R ,b_R \in
\mathcal{A}_R.
 \tag{4.13}\end{align*} \]

Indeed, it is straightforward to check that this is simply the matrix trace on $(\mathbb{C}^{2N})_R$,
normalized such that the trace of the identity is one

\[ \begin{align*}
 \bra{\Psi_N}a_R \ket{\Psi_N} =2^{-N}\Tr_R(a_R) = 2^{-N}\sum_{i = 1}^{N}\left(\bra{0}a_R\ket{0}_i +
\bra{1}a_R\ket{1}_i \right).
 \tag{4.14}\end{align*} \]

In comparing to CLPW, $\ket{\Psi_N}$ is the analog of the global Bunch-Davies state with an observer.

#### [section-4.2-p2] paragraph

Note that $\ket{\Psi_N}$ is not the unique way to extend $\rho_R$ to a state on the joint left-right system.
For instance, the partial trace of the joint identity operator reduces to $\rho_R$

\[ \begin{align*}
 \Tr_L(2^{-2N}\mathbb{1}_R\otimes \mathbb{1}_L) = \rho_R.
 \tag{4.15}\end{align*} \]

The unnormalized version of this operator, $\mathbb{1}_R\otimes \mathbb{1}_L$, is analogous to the
unnormalized no-boundary state on $\mathcal{M}$. In the thermodynamic limit ($N\rightarrow \infty$), this
state does not lead to finite expectation values for any element of $\mathcal{A}_R$ unless the normalization
of $2^{-2N}$ is included. We can, however, consider it as a formal asymptotic expansion in $N$

\[ \begin{align*}
 \mathbb{1}_R\otimes \mathbb{1}_L=
 2^{N} \tilde{\rho}_R.
 \tag{4.16}\end{align*} \]

The diverging prefactor $2^{N}$ is the analog of $\mathcal{Z}'_{\mathcal{M}}$ while the remaining operator is
a valid state for operators on $\mathcal{A}_R$. The reduced state $\tilde{\rho}_R$ is the analog of
$\mathbb{1}_{\mathcal{M}}$. In this construction, $\Tr_R \rho_R = 1$, equivalently, the normalized trace of
the identity is one, $\bra{\Psi_N} \mathbb{1}_R \ket{\Psi_N} = 1$, even in the thermodynamic limit. Thus, this
construction has so far modeled a type II$_1$ algebra, such as that in de Sitter space. This can be modified
to model a type II$_{\infty}$ algebra by appending a single Harmonic oscillator to the right side, which has
Hilbert space $L^2(\mathbb{R})$. With this addition, there is no normalizable state in the Hilbert space that
acts a trace. Nevertheless, the above identifications of $\mathcal{Z}'_{\mathcal{M}}$ and
$\mathbb{1}_{obs}^{\mathcal{M}}$ go through, with the modification that $\rho_R \rightarrow \rho_R\otimes
\mathbb{1}_{L^2(\mathbb{R})}$, which is not normalizable because it has an infinite trace.

#### [section-4.2-p3] paragraph

The final step is generalizing this construction to a direct sum Hilbert space, labeled by $\mathcal{M}$. In
this case, the number of qubits $N$ in each superselection sector is $\mathcal{M}$ dependent, i.e. it can take
different values in the asymptotic expansion in $N$. For simplicity, consider the case of just two sectors,
though it is immediately generalizable. The identity matrix on the global Hilbert space restricted to $R$ is

\[ \begin{align*}
\begin{aligned}
 \left(\mathbb{1}_{R,\mathcal{M}_1}\otimes \mathbb{1}_{L,\mathcal{M}_1} \right)\oplus
\left(\mathbb{1}_{R,\mathcal{M}_2}\otimes \mathbb{1}_{L,\mathcal{M}_2}\right)
 &= 2^{N(\mathcal{M}_1)}\tilde{\rho}_{R,\mathcal{M}_1}\oplus2^{N(\mathcal{M}_2)}\tilde{\rho}_{R,\mathcal{M}_2}
\end{aligned}
 \tag{4.17}\end{align*} \]

where we have defined the density matrices such that $\Tr_R(\rho_R) = 1$. $\tilde{\rho}_{R,\mathcal{M}_1}$ and
$\tilde{\rho}_{R,\mathcal{M}_2}$ are the analogs of $\mathbb{1}_{obs}^{\mathcal{M}_1}$ and
$\mathbb{1}_{obs}^{\mathcal{M}_2}$. The prefactors are the analogs of $\mathcal{Z}'_{\mathcal{M}_1}$ and
$\mathcal{Z}'_{\mathcal{M}_2}$.

### [section-4.3] section: 4.3 The path integral approach
#### [section-4.3-p1] paragraph

We now present a path integral argument along the lines of section 2.1. One can consider the density matrix
associated with a subregion if the subregion of interest is invariantly defined on a partial Cauchy surface.
There are two general ways we know how to do this: (1) When the region is the causal diamond associated with
an infinitely extended observer. In this case, the position of the observer at infinity invariantly define the
region and is robust to perturbations of the geometry. This is the approach of [7]. (2) When the partial
Cauchy surface is bounded by an extremal surface, the subregion is unambigously defined because the extremal
surface is robust to perturbations. This is the approach of [24]. We will propose a no-boundary prescription
that applies equally well in both cases.

#### [section-4.3-p2] paragraph

When an observer sees only a portion of the spacetime, there is no way to prepare a pure quantum state.
Therefore, we begin with physical boundary conditions for a density matrix where the bra and ket meet at a
codimension-two surface, $\gamma$, which is the intersection of the boundaries of the observer’s future and
past light cones. In the case where $\gamma$ is an extremal surface, the observer’s end-points need not be
asymptotic and the causal diamond associated to the extremal surface need not be associated to any one
observer worldline. With the causal diamond invariantly defined, using options (1) or (2), we then specify
boundary conditions on these light cones

\[ \begin{align*}
     \class{l2mpic-22}{\rule[-0.0000em]{7.7008em}{6.7979em}}
 \tag{4.18}\end{align*} \]

The purpose of using null surfaces instead of spatial surfaces for the boundary conditions is so that the fact
that the observer only sees a portion of the universe is explicitly part of the definition of the path
integral.20 The surface $\gamma$ may be connected or not depending on the background. For simplicity, we will
restrict ourselves to cases where the topology of these null boundaries is the same as the null boundaries of
the static patch in de Sitter. More complicated topologies require more care, though we expect that none of
our conclusions are sensitive. Matrix elements of the observer’s no-boundary state are computed by path
integrating over all geometries and field configuration $\phi_\text{bulk}$ consistent with boundary conditions
on these null surfaces, as in (2.4)21

\[ \begin{align*}
 \bra{\phi''}\rho_\text{NB}\ket{\phi'}=\int \mathcal{D}\phi_\text{bulk}\quad
 \raisebox{-0.47\height}{\class{l2mpic-23}{\rule[-0.0000em]{11.2571em}{8.4864em}}} \tag{4.19}\end{align*} \]

This causal diamond is well-defined semiclassically if we consider a subspace of states that all have the same
expectation value of induced metric and extrinsic curvature on this diamond at $O(1)$, but are generally
different at $O(\sqrt{\hbar G})$ and have small fluctuations consistent with the uncertainty relations
$\braket{\Delta K \Delta g}\lesssim \hbar G$. In this subspace, the expectation values provide initial data
that fully specifies the geometry at leading order within the causal diamond, without specifying the geometry
outside of the diamond. In practice, one can complete the partial Cauchy surface to a full Cauchy surface, and
place “trace-out” boundary conditions in the unobservable region [97].

#### [section-4.3-p3] paragraph

Matrix elements of $\rho_\text{NB}^2$ are computed along the lines of equation (2.8) as

\[ \begin{align*}
\bra{\phi''}\rho_\text{NB}^2\ket{\phi'} = \underset{\substack{\text{boundary conditions}\\\text{modulo diffeom
orphisms}}}{\int\mathcal{D}\psi}\,\,\raisebox{-0.46\height}{\class{l2mpic-24}{\rule[-
0.0000em]{16.8857em}{8.4864em}}}\,\,\,=\bra{\phi''}\rho_\text{NB}\ket{\phi'}\,. \tag{4.20}\end{align*} \]

The matrix multiplication is not a simple geometric gluing of the green surfaces. Rather, similar to the inner
product for full Cauchy slices, it involves integrating over geometries with the past boundary conditions
given by the green surface in the left diagram and the future boundary conditions given by the green surface
in the right figure.

#### [section-4.3-p4] paragraph

A crucial point is that matrix multiplication does not result in a conical excess at $\gamma$. This is
distinct from the replica trick in AdS/CFT where a conical excess arises at the asymptotic boundary where the
two copies are glued. In a closed universe, there is nothing to enforce the conical excess like the non-
gravitating boundary where the CFT resides, and gravity smooths out the singularity. The integral over bulk
geometries, which was left implicit in the picture, selects the smooth single-cover configuration. An
analogous comment was made in [97] in the context of the no-boundary density matrix for slow-roll inflation.
We conclude from (4.20) that

\[ \rho_\text{NB}^2=\rho_\text{NB}\,. \]

(4.21)

Therefore, the observer’s no-boundary density matrix is the identity matrix for this subregion.

#### [section-4.3-p5] paragraph

As in section 2.2, the density matrix prepared by the path integral is not normalized. The partition function
$\mathcal{Z}'_{\mathcal{M}}$ is the norm of the density matrix (4.19).22 In the sense of an asymptotic
expansion in $G$, this determines the additive constant in the von Neumann entropy of normalized states $\rho$
in $\mathcal{H}_{\mathcal{M}}$

\[ \begin{align*}
 S(\rho) = \log \mathcal{Z}'_{\mathcal{M}} +O(1).
 \tag{4.22}\end{align*} \]

In the case of dS, the sphere path integral equals to leading order the area of the cosmological horizon. In
more general spacetimes where the region of interest is not bounded by an extremal surface, we do not expect
that the path integral is equal to the area. We comment more on this in a specific example in the discussion
section 6.23 Interestingly, the result for the partition function in [97] is somewhere in between. It is not
the (very large) area of the boundary of the region of interest but rather the area of a surface to the past
of the region, namely, the horizon at the end of inflation.

#### [section-4.3-p6] paragraph

We can compare our analysis to that of [24] for regions bounded by an extremal surface. In [24], a
gravitational mode related to the area operator that generates a local boost about the extremal surface was
quantized, leading to a type II$_{\infty}$ algebra. One expects this algebra to not have a center, so the
trace is unique up to rescalings. We have shown that the no-boundary state is also tracial for such an
algebra. Thus, the tracial state from [24] ought to be the $O(1)$ contribution to our no-boundary state for
these subregions. Indeed, in the specific example of slow-roll inflation, [24] explicitly invoked the
semiclassical limit of the no-boundary state to land on a trace. It would be extremely interesting if there
was an analogous gravitational mode for non-extremal surfaces to more explicitly analyze entropy in these
spacetimes. We expect that if such a mode exists, it will include corrections to the area operator. That would
provide a complementary explanation for why the entropy is related to action more generically. Such an
analysis may be tractable in low-dimensional models, extending [99, 100].

#### [section-4.3-p7] paragraph

The global no-boundary state with an observer has no contribution from a sphere topology. However, when
reducing the no-boundary state to a state for a subregion by tracing out “degrees of freedom” in the other
patch, the path integral does generally include a sphere topology. This results in a confusing formal equality

\[ \begin{align*}
    \class{l2mpic-25}{\rule[-0.0000em]{38.9167em}{8.8073em}}
 \tag{4.23}\end{align*} \]

This seems clear from the rules of the gravitational path integral, but is non-perturbative. A detailed
understanding of this would thus require understanding the decomposition of the Hilbert space on the global
slice into Hilbert spaces for subregions at the non-perturbative level. Assuming the equality makes sense, it
would be interesting to understand how the sphere emerges, but this is beyond our current scope. Perhaps the
simplest theory to investigate this is JT gravity with $\Lambda > 0$. There, the wormhole amplitude without an
observer computed in [101, 102] is an identity operator [54], but a semiclassical observer has restricted
causal access, and so the observer’s density matrix had not been fully understood thus far. A similar
observation was also made in [43].

## [sect-nogo] section: 5 No KMS theorem
### [sect-nogo-p1] paragraph

We would like to check in controllable examples that the density matrix for an observer with causal horizons
in section 4 defines a trace. A case in which it is understood how to find the trace is when the matter state
satisfies the Kubo–Martin–Schwinger (KMS) condition with respect to time translations on an observer’s
worldline. In this case, the matter can be dressed to the observer and an explicit formular for the trace can
be found [7]. In de Sitter space, there exists a state that is KMS in the full static patch, the so-called
Bunch-Davies state [103, 104, 105, 106, 107], which was critical the analysis of CLPW. In this section, we
show that this construction cannot work for any other spacetime that is asymptotically de Sitter in the far
past or future. In particular, we show that the existence of a KMS state, even when we only require it to be
KMS on the observer’s worldline, is unique to de Sitter.24 We emphasize that this does not imply that the no-
boundary state is not the trace or that a trace cannot be defined. It simply means that the explicit
construction of the trace requires more work than the construction of [7] and that the resulting entropy
cannot describe an equilibrium thermodynamic entropy. We discuss promising directions on this front in section
6.

### [sect-nogo-p2] paragraph

Before presenting the arguments, we explain what is meant by a KMS state on the worldline. Given a quantum
state and a worldline geodesic parametrized by a time $t$, we may consider correlation functions of the form

\[ f(t_1,t_2) = \langle \phi_1(t_1) \phi_2(t_2) \rangle\,, \]

(5.1)

where $\phi_{1,2}$ are any local operators in the theory. The KMS property of the state requires that
$f(t_1+z, t_2)$ is analytic for in the interior of the strip $-\beta < \Im(z) < 0$ and

\[ \langle \phi_1(t_1) \phi_2(t_2) \rangle = \langle \phi_2(t_2) \phi_1(t_1+\i\beta)\rangle\,. \]

(5.2)

This equation (or the requirement for analyticity) is not required to hold for operators not on the worldline.

### [sect-nogo-p3] paragraph

We note that a (faithful semi-finite normal) state always satisfies the KMS condition with respect to abstract
modular time evolution. In this section, we are concerned with the more restrictive condition that this
modular evolution coincides with a physical time evolution.

### [sect-5.1kms] section: 5.1 General argument
#### [sect-5.1kms-p1] paragraph

Let us now assume that the perturbative algebra of observables on a worldline in an asymptotically de Sitter
background admits a KMS state with respect to proper time translations on the worldline. In particular, we
consider FLRW spacetimes of the form

\[ \begin{align*}

 \d s^2 = -\d t^2 + a(t)^2\d\Omega_{3}\,,\quad a(t) \sim \frac{1}{H}e^{H |t|} \text{ for } \abs{t}\to
\infty\,, \tag{5.3}\end{align*} \]

where $d\Omega_3$ is the metric on the unit three-sphere. We will show that the state on the observer’s
worldline in such a geometry can only satisfy KMS if the geometry is exactly de Sitter space. To prove this,
we first show that if correlation functions on the worldline satisfy KMS, they are indistinguishable from the
correlation functions of the Bunch-Davies state. We then show that the Bunch-Davies state is inconsistent with
the operator product expansion (OPE) for any background except for de Sitter.

#### [sect-5.1kms-p2] paragraph

Consider the two-point function on the worldline (5.1). Because there are no light-cone singularities on the
worldline, the correlation function is analytic for a given ordering $t_1 \ne t_2$. If it satisfies KMS (5.2),
it is periodic under a combined shift $t_i \to t_i + \i \beta$ and is analytic on the strip $0\le \Im (t_i)
\le \beta$. Consider now

\[ f(T) = \langle \phi_1(t_1+T) \phi_2(t_2+T) \rangle\,. \]

(5.4)

This agrees with (5.1) at $T=0$. By the above assumptions, this function is periodic $f(T)=f(T+\i \beta)$ and
analytic on the strip $0\le \Im (T) \le \beta$. Because the background is asymptotically de Sitter, the
correlation function asymptotes to the Bunch-Davies correlation function at large $|T|$, by the “cosmic no-
hair theorem” [113, 114, 115, 116, 117]. This is a finite limit. By Liouville’s theorem, $f(T)$ is thus a
constant as a function of $T$. This shows that the correlation function agrees with the BD correlation
function on the worldline for all times.

#### [sect-5.1kms-p3] paragraph

Every state must respect the OPE of the theory. The OPE is a property of the algebra and depends on the
underlying background geometry [118]. It places constraints on possible correlation functions. While the
Bunch-Davies state satisfies these constraints for the de Sitter background, it will not satisfy them, even
only on the worldline, for any other background. To illustrate this point, consider a massless minimally
coupled Klein-Gordon scalar field on an FLRW background.25 Free fields in curved spacetime satisfy the
canonical commutation relations [118]

\[ [\phi(x) ,\phi(y)] = \i E(x,y)\ \mathbb{1}\,. \]

(5.5)

Here, $E(x,y)$ is the advanced minus retarded Green’s function for the Klein-Gordon equation. Therefore every
state in the theory must have the property that correlation functions on the worldline satisfy

\[ \begin{align*} 
 \braket{[\phi(t_1) ,\phi(t_2)] }= \i E(t_1,t_2)\,. \tag{5.6}\end{align*} \]

For $t_1\to t_2$, the Green’s function takes a universal form [119, 108]

\[ \begin{align*}
 E(t_1,t_2) \to \frac{R(t_1)}{48\pi}+\dots,\quad t_1 < t_2. \tag{5.7}\end{align*} \]

However, correlation functions in the Bunch-Davies state are (by definition) identical to dS correlation
functions and satisfy [107]

\[ \begin{align*}
 \braket{[\phi(t_1) ,\phi(t_2)] } = \i \frac{H^2}{4\pi}, \quad t_1 < t_2. \tag{5.8}\end{align*} \]

This is inconsistent with (5.7) for spacetimes without constant scalar curvature. Thus, the Bunch-Davies state
for FLRW spacetimes is not in the Hilbert space. Higher orders in the OPE expansion (5.7) depend on all the
curvature components [120, 121], so even for inhomogeneous backgrounds, the BD constraint $E=H^2/4\pi$ fixes
the background around the worldline to that of de Sitter. Under suitable conditions on the metric, this will
constrain the geometry for the entire region accessible to the observer. We expect that similar arguments
using the OPE as a constraint should hold for other local quantum field theories. In summary, we conclude that
the only asymptotically de Sitter spacetime that admits a KMS state on a timelike worldline is de Sitter space
itself.

#### [sect-5.1kms-p4] paragraph

This statement is somewhat related to the cosmic no-hair theorem. Indeed, in order to define KMS states in
QFT, the geometry should possess a timelike isometry which acts as time translations on the worldline.26 This
requires the background geometry in the causal region of the observer to be stationary. Since the geometry is
also asymptotically de Sitter, the cosmic no-hair theorem fixes the geometry in the causal region to de
Sitter.

### [sect-5.2constructive] section: 5.2 Constructive argument
#### [sect-5.2constructive-p1] paragraph

In this section, we flip the logic around by attempting to construct FLRW solutions with conformal matter
correlation functions on a worldline that satisfy KMS. We will find that only de Sitter space satisfies this
requirement.

#### [sect-5.2constructive-p2] paragraph

We again consider the FLRW metric (5.3), now coupled to a conformal field theory with a primary operator
$O_\Delta$ of dimension $\Delta$. Using the conformal time coordinate $\d t = a \ d\eta$, the metric is
related to $R\times S^3$ as

\[ \d s^2 = a(t)^2(-\d \eta^2 + \d \Omega_3)\,. \]

(5.9)

Time translation is therefore a conformal Killing direction in this background. Consider the state that
annihilates the time translation operator. The conformal two-point function on this state is therefore

\[ \langle O_\Delta(t_1,0) O_\Delta(t_2, \alpha)\rangle = \frac{1}{a^\Delta(t_1) a^\Delta(t_2)} G_\Delta(\eta(t_1)-\eta(t_2),\alpha)\,, \]

(5.10)

with $\alpha$ the angular difference in $S^3$ and $G_\Delta(\eta,\alpha)$ the vacuum conformal two-point
function on $R \times S^3$

\[ G_\Delta(\eta_1,\eta_2,\alpha)=\left(2\cos(\eta_1-\eta_2)-2\cos \alpha\right)^{-\Delta}\,. \]

(5.11)

A necessary condition for (5.10) to satisfy KMS is that it is analytic in the complex $t_1$ strip away from
the usual short-distance singularities. $G_\Delta(\eta,\alpha)$ has this property, so for analyticity we need
$\eta(t)$ and $a(t)$ to be analytic. Moreover, the two-point function has a branch cut whenever $a(t)=0$ with
$|\eta(t)|<\infty$.

#### [sect-5.2constructive-p3] paragraph

The most general analytic function $a(t)$ that is also periodic $a(t+i\beta) = a(t)$ (as demanded by KMS) is a
sum of $\sinh(n \, H t)$’s and $\cosh(n \, H t)$’s with integer $n$ and $H=2\pi/\beta$. The asymptotic de
Sitter condition imposes that $a(t) \simeq e^{H|t|}$ for large $|t|$, restricting $n$ to $0$ or $1$. Choosing
$t=0$ as a moment of time-reflection symmetry, one is left with the functions $a(t) = a_0 + a_1 \cosh(H t)$.
Wick-rotating to $\tau = \i t$, there exists an Euclidean time coordinate $\tau=\tau_0$ with $a(\pm\tau_0) =
0$. To avoid a conical singularity at this point, one should impose $\dot a(\pm\tau_0) = \pm 1$. The most
general analytic solution is thus found to be

\[ a(t) = \frac{\cosh(H t)-\cos(H\tau_0)}{H \sin(H\tau_0)}. \]

(5.12)

This FLRW geometry can actually be realized by considering a positive cosmological constant $\Lambda = 3H^2$
and a homogeneous density of domain walls27, which have energy density redshifting as $\omega/a$. An exact
solution to Einstein’s equations is then indeed of the form (5.12)

#### [fig-pinchoff_tikz] figure: Figure 5

Figure 5. Cartoon of Lorentzian spacetimes (5.13) when $\omega = 0$ (left), $0< \omega < \infty$ (middle), and
$\omega \rightarrow \infty$ (right), each with de Sitter asymptotics. The throat shrinks as $\omega$
increases, pinching off in the $\omega \rightarrow \infty$ limit.

#### [sect-5.2constructive-p4] paragraph

\[ a(t)=\frac{1}{2H^2}\left(\sqrt{4H^2+\omega^2}\cosh(H t)-\omega\right)\,. \]

(5.13)

These solutions are pictured in figure 5. For $\omega=0$, the solution reduces to pure de Sitter. The length
of the throat goes to zero in the extreme $\omega\to\infty$ limit.

#### [sect-5.2constructive-p5] paragraph

To appreciate that the analyticity of $a(t)$ goes some way towards having a KMS state, we have checked
explicitly that on the worldline ($\alpha=0$) in the geometry (5.13), correlation functions of scalar
conformal primaries (5.10) are equal to those of the Bunch-Davies state for de Sitter with $\beta=2\pi/H$.
Unfortunately (but in line with the discussion of section 5.1) however, even this spacetime with analytic
$a(t)$ does not result in a KMS state on the worldline for all operators. To see this, notice that the Ricci
scalar of (5.12) is given by

\[ \begin{align*}
 R =6 H^2\frac{2 \cosh (H t)+\cos (H\tau_0)}{\cosh (H t)-\cos (H\tau_0)}\,. \tag{5.14}\end{align*} \]

The curvature thus diverges at the poles of the Euclidean geometry $t=\pm \i \tau_0$ unless $\tau_0 = \pi/2H$,
which is the de Sitter ($\omega=0$). As a result, some correlation functions are non-analytic. For instance,
consider a conformally-coupled scalar $\phi$. While the associated primary two-point function is equal to the
Bunch-Davies correlation function, the Laplacian descendant is divergent at the poles28

\[ \langle \nabla^2 \phi(t_1) \phi(t_2)\rangle = H^2 \frac{2\cosh(H t_1)+\cos(H \tau_0)}{\cosh(H t_1)-\cos(H \tau_0)} \, \langle \phi(t_1) \phi(t_2)\rangle. \]

(5.15)

The only FLRW geometry that avoids this issue and thus has the potential for worldline KMS is de Sitter itself
with $a(t)=\cosh(Ht)/H$, as we argued also in section 5.1.

## [sect-5.conclusion] section: 6 Concluding remarks
### [sect-5.conclusion-p1] paragraph

We have argued using the gravitational path integral that the no-boundary density matrix of the universe with
an observer is the identity matrix on the physical Hilbert space and thus provides a trace for the observer’s
algebra. This realizes a proposal of [7] that the observer’s no-boundary state can be used to define von
Neumann entropy in a background-independent manner so that there is no arbitrary constant for each spacetime.
To provide a concrete example, we showed that Euclidean wormhole amplitudes in JT gravity (i.e. the no-
boundary path integral) compute matrix elements of an identity operator on the physical Hilbert space.

### [sect-5.conclusion-p2] paragraph

Following the claims of section 4 where the observer has causal horizons, one would like to explicitly solve
for the no-boundary state on a specific background. The no-go results of section 5 suggest that a generic no-
boundary saddle does not prepare a KMS state on the worldline which is an obstruction to repeating the
analysis of [8, 7]. It can, however, prepare a state with a “weak KMS” relation. By this we mean that from the
no-boundary prescription, the observer worldline has the topology of a circle in the complex geometry. On an
open set around the worldline, quantum field theory correlation functions remain analytic (see figure 6). This
allows one to uniquely define an analytic continuation of Lorentzian operators of the type $\phi(t+\i \beta)$
that can be shown to satisfy a KMS-like relation (5.2). We stress that, unlike in the standard KMS relation,
we do not have analyticity on the entire strip $0\le \Im (t) \le \beta$. It is plausible that this “weak KMS”
(5.2) suffices to explicitly find the trace for these backgrounds as well. We are obligated to mention the
logical possibility that there is no perturbative trace on a general background, though we are optimistic that
this is not the case. In this case, the observer’s algebra would be type III. This is not in contradiction
with any of our claims of section 4, as mentioned in footnote 19.

### [fig-weak_kms] figure: Figure 6

Figure 6. The complex $t$ plain for the axion wormhole (6.3). The dashed lines represent where the correlation
functions are analytic. The horizontal line is the Lorentzian contour and the vertical line is the Euclidean
contour. The existence of a smooth Euclidean background gives a path (in orange) which allows one to define
$\phi(T+\i \beta)$ unambiguously. The correlation functions of these fields satisfy “weak KMS” (5.2).

### [sect-5.conclusion-p3] paragraph

We conclude this paper with a digestif, by introducing a particular class of spacetimes where one can test our
proposal. We intend to report more details regarding this elsewhere. We consider solutions of the Friedmann
equations with a positive cosmological constant supported by axion flux [128]. Recall the 3D FLRW metric29

\[ \d s^2=-\d t^2+ a(t)^2\d \Omega_2\,,\quad \d \Omega_2=\d\theta^2+\sin^2(\theta)\d \phi^2\,. \]

(6.1)

The Friedmann equation with axion flux density $Q \equiv q H^{-1}({16\pi G})^{-1/2}$ becomes

\[ \begin{align*}
 \frac{1}{a^2}\bigg(\frac{\d a}{\d t}\bigg)^2 = -\frac{1}{a^2} +H^2 + \frac{q^2}{4 H^2}\frac{1}{a^4}\,
\tag{6.2}\end{align*} \]

and solve to

\[ a(t)=\left(\frac{1+\sqrt{1-q^2}\cosh(2 Ht)}{2H^2}\right)^{1/2}\,. \]

(6.3)

This solution has a minimal size at $t=0$ and asymptotes to de Sitter space for $\abs{t}\to\infty$ if $q<1$.
If $q = 1$, this is an Einstein static universe $a=\tfrac{1}{\sqrt{2}H}$. To check whether a comoving observer
in this spacetime has causal horizons, we compute the conformal time that passes between the $t = 0$ and
$t=\infty$. For an observer at $\theta=0$, one finds that there is a causal horizon at30

\[ \theta_\text{h}(q)=\sqrt{\frac{2}{1+\sqrt{1-q^2}}} \ 
 K\bigg(\frac{1-\sqrt{1-q^2}}{1+\sqrt{1-q^2}}\bigg), \]

(6.5)

where $K$ is the complete elliptic integral of the first kind. In empty de Sitter space ($q=0$), a static
observer sees exactly half of the space $\theta_\text{h}=\tfrac{\pi}{2}$. For $q>0$, an observer sees more
than half of the spacetime, consistent with the general fact that positive energy brings the antipodal
observers in dS in causal contact with one another [129]. Interestingly, there is a critical value
$q_\text{c}$ such that for $q>q_\text{c}$ the observer has complete causal access. Therefore, the observer’s
algebra is expected to transition to a type I von Neumann algebra.

### [fig-kettlebell] figure: Figure 7

Figure 7. Left: The Euclidean FLRW wormhole geometry described in (6.6). Right: The necklace geometry.

### [sect-5.conclusion-p4] paragraph

The Lorentzian geometry can be continued ($\tau = \i t$) to a smooth no-boundary Euclidean wormhole solution
(see figure 7)

\[ a(\tau)=\left(\frac{1+\sqrt{1-q^2}\cos(2H\tau)}{2H^2}\right)^{1/2}
 \,,\quad 0<H \tau<\pi . \]

(6.6)

When $q\rightarrow 1$, we can see explicitly that the algebra of dressed observerables has a trace
corresponding to the no-boundary state. This is because the path integral prepares a thermal state of quantum
fields including gravitons with respect to global time translations. Using the KMS property of the quantum
fields, the tracial property of the expectation value of dressed operators can be verified [7]. In this case,
one finds that the trace is the standard Hilbert space trace because the algebra is type I.

### [sect-5.conclusion-p5] paragraph

We have previously argued that the von Neumann entropy appearing in every state for the algebra on this
background includes a contribution of minus the action of the no-boundary background (4.9). The Euclidean on-
shell action is straightforward to compute [128]

\[ I=-\frac{\pi }{{2 G}H}\left(1- q \right). \]

(6.7)

This vanishes for $q=1$ which is the expected behavior for a type I algebra because type I algebras admit pure
states with zero entropy. The horizon area for this geometry is distinct from (minus) the action for $0<q<1$

\[ \begin{align*}
 A_h = 2\pi H^{-1}(1+\sqrt{1-q^2})\sin(\theta_\text{h})^2\,.
 \tag{6.8}\end{align*} \]

For $0<q<1$, one is tempted to interpret $-I$ as the leading contribution of the entropy, following section 4.
This is also the answer one would arrive at from the gravitational replica trick. This raises several puzzles.
For instance, when $q>q_\text{c}$ we expect a type I algebra with $O(1)$ entropy, yet the action is $O(1/G)$.

### [sect-5.conclusion-p6] paragraph

However, the identification of $-I$ as an entropy assumes that the Euclidean saddle (6.6) dominates the no-
boundary partition function for these geometries. This is not obviously the case. Indeed, because the action
of this wormhole is negative, there are Euclidean solutions with action unbounded from below if one takes
$0<H\tau<n\pi$. This leads to an unbounded path integral. These solutions dominate even over the sphere
geometry if $q$ is a dynamical variable, creating a tension with interpreting the sphere as the dominant
contribution to the de Sitter entropy. It would be interesting if this could be addressed via a better
understanding of the gravitational path integral. This would be analogous to the pathological vacuum solutions
of a chain of spheres that were ruled out by the Kontsevich-Segal-Witten criterion [130, 131].

### [sect-5.conclusion-p7] paragraph

There is also a second Lorentzian continuation of (6.6) starting from the minimal surface $H\tau=\pi/2+\i t$.
This is a cosmology with a big bang and big crunch that occurs at finite proper time, but infinite conformal
time. Because of these singularities, matter correlation functions will not satisfy KMS, as explained in
section 5.2. Indeed, one finds branch cuts in the conformal two-point function (5.10) (see figure 6). However,
the correlation functions do satisfy the “weak KMS” property. We hope that this will suffice to define a
trace. Clearly, there is much more to learn about the no-boundary state in general spacetimes.

## [acknowledgments] section: Acknowledgments
### [acknowledgments-p1] paragraph

We thank Luca Ciambelli, Daniel Harlow, Luca Iliesiu, Victor Ivo, Jorrit Kruthoff, Juan Maldacena, Rob Myers,
Vladimir Narovlansky, Pratik Rath, Gautam Satishchandran, and Jonathan Sorce for useful discussions. We are
especially grateful to Edward Witten for numerous discussions that were integral to this work. AB was
supported by the Marvin L. Goldberger Member Fund, the US DOE DE-SC0009988 and by the Ambrose Monell
Foundation. JKF is supported by the Marvin L. Goldberger Member Fund at the Institute for Advanced Study and
the National Science Foundation under Grant No. PHY-2207584. EYU is supported by the J. Robert Oppenheimer
Endowed Fund.

## [app-cosmo] appendix: A Cosmological constant as observer in JT gravity
### [app-cosmo-p1] paragraph

There is a simplification of the observer model [132] which allows for very straightforward comparison with
the Euclidean path integral. Instead of including a point-like observer, we can quantize an energy density

\[ q=\ell \Lambda\,. \]

(A.1)

The WDW Hamiltonian becomes

\[ H_\text{WDW}=-p k-\Phi \ell+\Lambda \ell=0\,,\quad [\Lambda,T]=\i\,. \]

(A.2)

The action for is that of a $U(1)$ 2D Yang-Mills theory coupled to JT gravity where the Hamiltonian is
$\Lambda$ times the area of the surface. In the holographic limit ($\Phi=1/\varepsilon$ and $\Lambda$ finite),
it is not difficult to compute the associated Euclidean wormhole path integral31

\[ \bra{\beta_1,\Lambda_1}\rho_\text{NB}\ket{\beta_2,\Lambda_2}=\delta(\Lambda_1-\Lambda_2)\int_0^\infty \d b\, b\,Z_\text{trumpet}(b,\beta_1) Z_\text{trumpet}(b,\beta_2)\,. \]

(A.3)

It is simple to show that this is consistent with inserting the identity matrix in canonical quantization

\[ \mathbb{1}_\text{phys}=\int_0^\infty \d b\, b\int_{-\infty}^{+\infty}\d \Lambda \ket{b,\Lambda}\bra{b,\Lambda}. \]

(A.4)

To show that this is the correct identity operator we recognize the WDW Hamiltonian as implementing the
Schrödinger equation

\[ \frac{1}{\ell}\frac{\d}{\d \Phi}\frac{\d}{\d \ell}+\Phi=\i \frac{\d }{\d T} \]

(A.5)

Using a separation of variables, we maydiagonalize

\[ \i \frac{\d}{\d T}=\Lambda. \]

(A.6)

The remaining WDW equation can be solved by recognizing that we can absorb the $\Lambda$ eigenvalue upon
shifting $\Phi$ by a constant. The wavefunctions are therefore

\[ \braket{b,\Lambda|\ell,\Phi,T}= e^{-\i T \Lambda}\frac{1}{\sqrt{2\pi}}\frac{1}{\sqrt{b^2-\ell^2}}e^{\i (\Phi-\Lambda) \sqrt{b^2-\ell^2}}\,. \]

(A.7)

We can compute the Klein-Gordon inner product by gauge-fixing to slices $\ell=0$ (other options are possible
and give the same answer, like gauge-fixing to $T=T_0$ which gives a basis of square integrables on
$\ell,\Phi$). This is the same inner product as in (3.11) but now with a $T$ integral. The $T$ integral
produces $\delta(\Lambda_1-\Lambda_2)$. We can then shift $\Phi$ by $\Lambda$ in the $\Phi$ integral (3.11) to
obtain

\[ \braket{b_1,\Lambda_1|b_2,\Lambda_2}=\frac{1}{b_1}\delta(b_1-b_2)\delta(\Lambda_1-\Lambda_2)\,. \]

(A.8)

This result in the aforementioned identity operator on the physical Hilbert space, which is consistent with
the Euclidean path integral. Indeed, in the asymptotic limit (A.7) is the JT trumpet (3.20).

### [footnotes] footnotes: Footnotes

Notes1See recent reviews on von Neumann algebra application in quantum-information theory in quantum field
theory [26] or their type classification [27].

2Relative entropy between two states can be defined for any von Neumann algebra [28, 29]. More generally, it
can be defined for $C^*$ algebras using an appropriate algebraic definition of the states [30, 31].

3In a theory without time-reversal symmetry, one may also want to impose an orientation on the manifold to
specify whether the boundary represents a bra or ket [39].

4The path integral over boundary conditions modulo diffeomorphisms $\psi$ comes with a nontrivial
Faddeev–Popov determinant in any particular gauge choice which we leave implicit [44]. We will be more precise
in section 3.1.

5In recent literature we recommend [54, 44] for pedagogical and in depth explanations.

6See [62, 63] for a detailed discussion on this approach and the work of CLPW.

7Even though these contributions have the same topology as (2.8), we include them in this section for
historical reasons.

8However, see [68] for a study of what occurs when one does include a sum of topologies.

9Similar discussion for more general dilaton potentials (including periodic ones) can be found in [75].

10A version of this discussion actually also works for open universes (intervals). The WDW Hamiltonian
constraint in that case generates a timelike flow in the patch, and is modified by boundary terms. Details of
such a construction will be presented elsewhere.

11For fixed $b$ and $q$ these span a complete basis for solutions of the AdS$_2$ Klein-Gordon equation,
analogous to (3.10) in [77] for dS$_2$.

12We note that in [78] this constraint seems to have been ignored.

13This seems consistent with [53] but potentially in tension with [39].

14It is difficult to directly solve the WDW equation for this configuration because of the point-like nature
of the observer. Our goal in this section is more modest than in the previous one. We demonstrate consistency
by using a hybrid between the path integral and canonical arguments. In appendix A, we consider a dynamical
cosmological constant as some simpler model for an observer. In that case, one can completely separate the
path integral and canonical arguments and find agreement.

15To compute this, one takes the asymptotic limit of the bulk-bulk correlator in AdS$_2$ with the sum over
windings. In the asymptotic limit this becomes just $e^{-\Delta d(\tau_1,\tau_2)}$.

16The action for this piece of spacetime (gray region in figure 3) comes from the corner term in the JT
action. Denoting the angle enclosed by the geodesic $\alpha$ one finds using hyperbolic geometry
$\alpha=-2\varepsilon\, e^{-\ell/2}\cosh(b/2)$ with the action $\alpha\Phi=\alpha/2\varepsilon$.

17The twist integral in (3.30) is extended to the full real axis by leveraging the sum over windings in
(3.31). The integral over twists gives
\[ \int_{-\infty}^{+\infty}\d \tau \frac{1}{\cosh(\tau/2)^{2\Delta}}=\frac{4^\Delta \Gamma(\Delta)^2}{\Gamma(2\Delta)}\,. \]

(3.34)
 In addition, we explicitly evaluated the following integral using (6.624.3) [88] and some further
simplifications
\[ \psi_E(b)=\int_{-\infty}^{+\infty}\d\ell\, \psi_E(\ell)\psi_b(\ell)= {i^{\frac{1}{2}-\Delta} \sqrt{2\pi}}\Gamma(\Delta\pm 2\i \sqrt{E})\sqrt{\sinh(b/2)}P_{2\i \sqrt{E}-1/2}^{1/2-\Delta}(\cosh(b/2)). \]

(3.35)
 with $P_l^m$ the associated Legendre functions. Completeness follows from the Mehler-Fock transform
\[ \int_0^\infty \d E\,\rho(E) \frac{1}{\Gamma(\Delta\pm 2\i\sqrt{E})}\psi_E(b_1)\psi_E^*(b_2)=\delta(b_1-b_2)\,. \]

(3.36)
 Their orthogonality relation was used to obtain the delta function in (3.37). This slightly improves some
equations in [78]. They consider what they call a basis $\ket{b,u}$ which we labeled $\ket{b,\tau}$. This is
over-complete because the $\tau$ label is redundant. We can see this explicitly from these calculations but
also from the general discussion on gauging spatial diffeomorphisms around (3.13).

18This is computed by summing over all topologies connecting the two asymptotic boundaries
\[ Z(\beta_1.\beta_2)=\int_{-\infty}^{+\infty}\d E_1\,e^{-\beta_1 E_1}\int_{-\infty}^{+\infty}\d E_2\,e^{-\beta_1 E_2}\average{\rho(E_1)\rho(E_2)}\,. \]

(3.41)
 Here $\average{\rho(E_1)\rho(E_2)}$ decomposes into a genus expansion associated with the different
gravitational topologies. This expansion matches exactly with the expansion of computing a certain observable
in some particular random matrix integral [65]
\[ \average{\rho(E_1)\rho(E_2)}=\frac{1}{\mathcal{Z}}\int \d H\,e^{-V(H)}\Tr \delta(H-E_1)\Tr\delta(H-E_1)\,. \]

(3.42)
 In one member of the ensemble, which also has a gravity interpretation as some theory of dilaton gravity
[89], the integral over $H$ collapses to a fixed Hamiltonian $H_0$ with eigenvalues $E_i$ and one recovers the
claimed equation.

19If $\mathcal{A}_{obs}^{\mathcal{M}}$ is of type III, the expectation value of any operator with respect to
the no-boundary state is infinite. Then (4.1) is a vacuous statement because both sides are divergent.

20We thank Edward Witten for suggesting null surfaces as the appropriate partial Cauchy slices for boundary
conditions.

21The notation $\ket{\phi'}$ and $\ket{\phi''}$ is formal because we do not expect to have a genuine Hilbert
space for a subregion.

22For example, in de Sitter space, the matrix multiplication involves a purely Lorentzian evolution of both
the bra and ket to the spatial $t = 0$ slice, before gluing. The Lorentzian parts of the path integral cancel.
The partition function is then dominated by the Euclidean action of the sphere.

23This is somewhat different to the conclusions of [25] where entropy changes were related to area changes of
the boundary of the subregion. We attribute this difference (in the case of non-extremal surfaces) to a
difference in how we are defining our subregions. We define the subregion as the accessible region for an
observer, whereas [25] appear to be making a “gauge choice” not related to any particular observer’s causal
diamond, the same as in [98]. With their choice, the location of the bifurcation surface is unchanged under
perturbations of spacetime. In the case where the surface is extremal, the two definitions agree.

24For some interesting results on the sparsity of KMS states, see [108, 109, 110, 111, 112].

25An analogous argument holds when adding mass or considering the free Maxwell field or linearized graviton,
and for more general geometries.

26For conformally invariant QFTs, a timelike isometry may be replaced by a timelike conformal isometry.

27These generically appear in models of the early universe when there is spontaneous symmetry breaking via the
Kibble-Zurek mechanism [122]. A physically motivated case arises in the invisible axion extension of the
Pecci-Quinn model [123, 124, 125]. At energies below the QCD scale, domain walls form in a network, connecting
cosmic strings [126]. These are topologically stable and are the source of the domain wall problem [127].

28By the Klein-Gordon equation, the prefactor is indeed proportional to the Ricci scalar.

29It is straightforward to generalize to higher dimensions, though the formulas become slightly less elegant.

30The metric can be brought in conformal form by the coordinate transformation
\[ \eta(t)=\int_{0}^t \frac{\d t}{a(t)}. \]

(6.4)
 Half of the height of the causal diamond in the Penrose diagram is obtained in the limit $t\to+\infty$ of the
observer worldline.

31We used the fact that $\Lambda A(\Sigma)$ in JT can be rewritten using the Gauss-Bonnet theorem as
proportional to $\Lambda K$. The net effect is the JT finite cutoff trumpets (3.8) with $\Phi\to \Phi-\Lambda$
(as we also see from the WDW equation). However, in the holographic limit, the $\Lambda$ dependence drops out.

### [refs] references: References

References[1]J. M. Maldacena, “The Large $N$ limit of superconformal field theories and supergravity,” Adv.
Theor. Math. Phys. 2 (1998) 231–252, arXiv:hep-th/9711200.
[2]S. S. Gubser, I. R. Klebanov, and A. M. Polyakov, “Gauge theory correlators from noncritical string
theory,” Phys. Lett. B 428 (1998) 105–114, arXiv:hep-th/9802109.
[3]E. Witten, “Anti de Sitter space and holography,” Adv. Theor. Math. Phys. 2 (1998) 253–291, arXiv:hep-
th/9802150.
[4]O. Aharony, S. S. Gubser, J. M. Maldacena, H. Ooguri, and Y. Oz, “Large N field theories, string theory and
gravity,” Phys. Rept. 323 (2000) 183–386, arXiv:hep-th/9905111.
[5]B. S. DeWitt, “Quantum Theory of Gravity. 1. The Canonical Theory,” Phys. Rev. 160 (1967) 1113–1148.
[6]D. N. Page and W. K. Wootters, “Evolution without evolution: Dynamics described by stationary observables,”
Phys. Rev. D 27 (1983) 2885.
[7]E. Witten, “A background-independent algebra in quantum gravity,” JHEP 03 (2024) 077, arXiv:2308.03663
[hep-th].
[8]V. Chandrasekaran, R. Longo, G. Penington, and E. Witten, “An algebra of observables for de Sitter space,”
JHEP 02 (2023) 082, arXiv:2206.10780 [hep-th].
[9]J. B. Hartle and S. W. Hawking, “Wave function of the universe,” Physical Review D 28 no. 12, (1983) 2960.
[10]S. Ryu and T. Takayanagi, “Holographic derivation of entanglement entropy from AdS/CFT,” Phys. Rev. Lett.
96 (2006) 181602, arXiv:hep-th/0603001.
[11]S. Ryu and T. Takayanagi, “Aspects of Holographic Entanglement Entropy,” JHEP 08 (2006) 045, arXiv:hep-
th/0605073.
[12]V. E. Hubeny, M. Rangamani, and T. Takayanagi, “A Covariant holographic entanglement entropy proposal,”
JHEP 07 (2007) 062, arXiv:0705.0016 [hep-th].
[13]A. Lewkowycz and J. Maldacena, “Generalized gravitational entropy,” JHEP 08 (2013) 090, arXiv:1304.4926
[hep-th].
[14]T. Faulkner, A. Lewkowycz, and J. Maldacena, “Quantum corrections to holographic entanglement entropy,”
JHEP 11 (2013) 074, arXiv:1307.2892 [hep-th].
[15]N. Engelhardt and A. C. Wall, “Quantum Extremal Surfaces: Holographic Entanglement Entropy beyond the
Classical Regime,” JHEP 01 (2015) 073, arXiv:1408.3203 [hep-th].
[16]G. Penington, “Entanglement Wedge Reconstruction and the Information Paradox,” JHEP 09 (2020) 002,
arXiv:1905.08255 [hep-th].
[17]A. Almheiri, N. Engelhardt, D. Marolf, and H. Maxfield, “The entropy of bulk quantum fields and the
entanglement wedge of an evaporating black hole,” JHEP 12 (2019) 063, arXiv:1905.08762 [hep-th].
[18]A. Almheiri, R. Mahajan, J. Maldacena, and Y. Zhao, “The Page curve of Hawking radiation from
semiclassical geometry,” JHEP 03 (2020) 149, arXiv:1908.10996 [hep-th].
[19]G. Penington, S. H. Shenker, D. Stanford, and Z. Yang, “Replica wormholes and the black hole interior,”
JHEP 03 (2022) 205, arXiv:1911.11977 [hep-th].
[20]A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, and A. Tajdini, “Replica Wormholes and the Entropy
of Hawking Radiation,” JHEP 05 (2020) 013, arXiv:1911.12333 [hep-th].
[21]V. Chandrasekaran, G. Penington, and E. Witten, “Large N algebras and generalized entropy,” JHEP 04 (2023)
009, arXiv:2209.10454 [hep-th].
[22]J. Kudler-Flam, S. Leutheusser, and G. Satishchandran, “Generalized black hole entropy is von Neumann
entropy,” Phys. Rev. D 111 no. 2, (2025) 025013, arXiv:2309.15897 [hep-th].
[23]J. Kudler-Flam, S. Leutheusser, and G. Satishchandran, “Algebraic Observational Cosmology,”
arXiv:2406.01669 [hep-th].
[24]C.-H. Chen and G. Penington, “A clock is just a way to tell the time: gravitational algebras in
cosmological spacetimes,” arXiv:2406.02116 [hep-th].
[25]K. Jensen, J. Sorce, and A. J. Speranza, “Generalized entropy for general subregions in quantum gravity,”
JHEP 12 (2023) 020, arXiv:2306.01837 [hep-th].
[26]E. Witten, Why does quantum field theory in curved spacetime make sense? And what happens to the algebra
of observables in the thermodynamic limit? 2022. arXiv:2112.11614 [hep-th].
[27]J. Sorce, “Notes on the type classification of von Neumann algebras,” Rev. Math. Phys. 36 no. 02, (2024)
2430002, arXiv:2302.01958 [hep-th].
[28]H. Araki, “Relative entropy of states of von neumann algebras,” Publications of the Research Institute for
Mathematical Sciences 11 no. 3, (1975) 809–833.
[29]H. Araki, “Relative entropy for states of von neumann algebras ii,” Publications of the Research Institute
for Mathematical Sciences 13 no. 1, (1977) 173–192.
[30]A. Uhlmann, “Relative Entropy and the Wigner-Yanase-Dyson-Lieb Concavity in an Interpolation Theory,”
Commun. Math. Phys. 54 (1977) 21.
[31]V. P. Belavkin and P. Staszewski, “C*-algebraic generalization of relative entropy and entropy,” Annales
De L Institut Henri Poincare-physique Theorique 37 (1982) 51–58.
[32]K. Maeda, T. Koike, M. Narita, and A. Ishibashi, “Upper bound for entropy in asymptotically de Sitter
space-time,” Phys. Rev. D 57 (1998) 3503–3508, arXiv:gr-qc/9712029.
[33]R. Bousso, “Positive vacuum energy and the N bound,” JHEP 11 (2000) 038, arXiv:hep-th/0010252.
[34]R. Bousso, “Bekenstein bounds in de Sitter and flat space,” JHEP 04 (2001) 035, arXiv:hep-th/0012052.
[35]X. Dong, E. Silverstein, and G. Torroba, “De Sitter Holography and Entanglement Entropy,” JHEP 07 (2018)
050, arXiv:1804.08623 [hep-th].
[36]A. I. Abdalla, S. Antonini, L. V. Iliesiu, and A. Levine, “The gravitational path integral from an
observer’s point of view,” arXiv:2501.02632 [hep-th].
[37]C. Akers, G. Bueller, O. DeWolfe, K. Higginbotham, J. Reinking, and R. Rodriguez, “On observers in
holographic maps,” arXiv:2503.09681 [hep-th].
[38]D. Harlow, M. Usatyuk, and Y. Zhao, “Quantum mechanics and observers for gravity in a closed universe,”
arXiv:2501.02359 [hep-th].
[39]E. Witten, “Bras and Kets in Euclidean Path Integrals,” arXiv:2503.12771 [hep-th].
[40]D. N. Page, “Density matrix of the universe,” Physical Review D 34 no. 8, (1986) 2267.
[41]S. W. Hawking, “The density matrix of the universe,” Physica Scripta 1987 no. T15, (1987) 151.
[42]Y. Chen, V. Gorbenko, and J. Maldacena, “Bra-ket wormholes in gravitationally prepared states,” JHEP 02
(2021) 009, arXiv:2007.16091 [hep-th].
[43]A. Fumagalli, V. Gorbenko, and J. Kames-King, “De Sitter Bra-Ket Wormholes,” arXiv:2408.08351 [hep-th].
[44]E. Witten, “A note on the canonical formalism for gravity,” Adv. Theor. Math. Phys. 27 no. 1, (2023)
311–380, arXiv:2212.08270 [hep-th].
[45]R. L. Arnowitt, S. Deser, and C. W. Misner, “Dynamical Structure and Definition of Energy in General
Relativity,” Phys. Rev. 116 (1959) 1322–1330.
[46]D. L. Wiltshire, “An Introduction to quantum cosmology,” in 8th Physics Summer School on Cosmology: The
Physics of the Universe, pp. 473–531. 1, 1995. arXiv:gr-qc/0101003.
[47]A. O. Barvinsky, “BRST technique for the cosmological density matrix,” JHEP 10 (2013) 051, arXiv:1308.3270
[hep-th].
[48]J. J. Halliwell, “Derivation of the Wheeler-De Witt Equation from a Path Integral for Minisuperspace
Models,” Phys. Rev. D 38 (1988) 2468.
[49]D. Marolf, “Path integrals and instantons in quantum gravity: Minisuperspace models,” Phys. Rev. D 53
(1996) 6979–6990, arXiv:gr-qc/9602019.
[50]J. Diaz Dorronsoro, J. J. Halliwell, J. B. Hartle, T. Hertog, and O. Janssen, “Real no-boundary wave
function in Lorentzian quantum cosmology,” Phys. Rev. D 96 no. 4, (2017) 043505, arXiv:1705.05340 [gr-qc].
[51]J. Feldbrugge, J.-L. Lehners, and N. Turok, “Lorentzian Quantum Cosmology,” Phys. Rev. D 95 no. 10, (2017)
103508, arXiv:1703.02076 [hep-th].
[52]B. Banihashemi and T. Jacobson, “On the lapse contour in the gravitational path integral,” Phys. Rev. D
111 no. 6, (2025) 066014, arXiv:2405.10307 [hep-th].
[53]D. Harlow and T. Numasawa, “Gauging spacetime inversions in quantum gravity,” arXiv:2311.09978 [hep-th].
[54]J. Held and H. Maxfield, “The Hilbert space of de Sitter JT: a case study for canonical methods in quantum
gravity,” arXiv:2410.14824 [hep-th].
[55]A. Higuchi, “Quantum linearization instabilities of de sitter spacetime. i,” Classical and Quantum Gravity
8 no. 11, (1991) 1961.
[56]A. Higuchi, “Quantum linearization instabilities of de sitter spacetime. ii,” Classical and Quantum
Gravity 8 no. 11, (1991) 1983.
[57]D. Marolf and I. A. Morrison, “Group Averaging for de Sitter free fields,” Class. Quant. Grav. 26 (2009)
235003, arXiv:0810.5163 [gr-qc].
[58]A. Ashtekar, J. Lewandowski, D. Marolf, J. Mourao, and T. Thiemann, “Quantization of diffeomorphism
invariant theories of connections with local degrees of freedom,” J. Math. Phys. 36 (1995) 6456–6493,
arXiv:gr-qc/9504018.
[59]D. Giulini and D. Marolf, “On the generality of refined algebraic quantization,” Class. Quant. Grav. 16
(1999) 2479–2488, arXiv:gr-qc/9812024.
[60]D. Marolf, “Group averaging and refined algebraic quantization: Where are we now?,” in 9th Marcel
Grossmann Meeting on Recent Developments in Theoretical and Experimental General Relativity, Gravitation and
Relativistic Field Theories (MG 9). 7, 2000. arXiv:gr-qc/0011112.
[61]D. Giulini, “Group averaging and refined algebraic quantization,” Nucl. Phys. B Proc. Suppl. 88 (2000)
385–388, arXiv:gr-qc/0003040.
[62]J. De Vuyst, S. Eccles, P. A. Hoehn, and J. Kirklin, “Crossed products and quantum reference frames: on
the observer-dependence of gravitational entropy,” arXiv:2412.15502 [hep-th].
[63]J. De Vuyst, S. Eccles, P. A. Hoehn, and J. Kirklin, “Gravitational entropy is observer-dependent,”
arXiv:2405.00114 [hep-th].
[64]P. Saad, S. H. Shenker, and D. Stanford, “A semiclassical ramp in SYK and in gravity,” arXiv:1806.06840
[hep-th].
[65]P. Saad, S. H. Shenker, and D. Stanford, “JT gravity as a matrix integral,” arXiv:1903.11115 [hep-th].
[66]D. Marolf and H. Maxfield, “Transcending the ensemble: baby universes, spacetime wormholes, and the order
and disorder of black hole information,” JHEP 08 (2020) 044, arXiv:2002.08950 [hep-th].
[67]M. Usatyuk, Z.-Y. Wang, and Y. Zhao, “Closed universes in two dimensional gravity,” SciPost Phys. 17
no. 2, (2024) 051, arXiv:2402.00098 [hep-th].
[68]A. Banerjee and G. W. Moore, “Comments on summing over bordisms in TQFT,” JHEP 09 (2022) 171,
arXiv:2201.00903 [hep-th].
[69]G. Penington and E. Witten, “Algebras and States in JT Gravity,” arXiv:2301.07257 [hep-th].
[70]D. K. Kolchmeyer, “von Neumann algebras in JT gravity,” JHEP 06 (2023) 067, arXiv:2303.04701 [hep-th].
[71]G. Penington and E. Witten, “Algebras and states in super-JT gravity,” arXiv:2412.15549 [hep-th].
[72]P. Saad, “Late Time Correlation Functions, Baby Universes, and ETH in JT Gravity,” arXiv:1910.10311 [hep-
th].
[73]A. Blommaert, “Dissecting the ensemble in JT gravity,” JHEP 09 (2022) 075, arXiv:2006.13971 [hep-th].
[74]L. V. Iliesiu, M. Mezei, and G. Sárosi, “The volume of the black hole interior at late times,” JHEP 07
(2022) 073, arXiv:2107.06286 [hep-th].
[75]A. Blommaert, A. Levine, T. G. Mertens, J. Papalini, and K. Parmentier, “Wormholes, branes and finite
matrices in sine dilaton gravity,” arXiv:2501.17091 [hep-th].
[76]M. Henneaux, “Quantum gravity in two dimensions: Exact solution of the jackiw model,” Physical review
letters 54 no. 10, (1985) 959.
[77]D. K. Kolchmeyer and H. Liu, “Chaos and the Emergence of the Cosmological Horizon,” arXiv:2411.08090 [hep-
th].
[78]L. V. Iliesiu, A. Levine, H. W. Lin, H. Maxfield, and M. Mezei, “On the non-perturbative bulk Hilbert
space of JT gravity,” JHEP 10 (2024) 220, arXiv:2403.08696 [hep-th].
[79]L. V. Iliesiu, J. Kruthoff, G. J. Turiaci, and H. Verlinde, “JT gravity at finite cutoff,” SciPost Phys. 9
(2020) 023, arXiv:2004.07242 [hep-th].
[80]J. Maldacena, D. Stanford, and Z. Yang, “Conformal symmetry and its breaking in two dimensional Nearly
Anti-de-Sitter space,” PTEP 2016 no. 12, (2016) 12C104, arXiv:1606.01857 [hep-th].
[81]J. Engelsöy, T. G. Mertens, and H. Verlinde, “An investigation of AdS$_{2}$ backreaction and holography,”
JHEP 07 (2016) 139, arXiv:1606.03438 [hep-th].
[82]K. Jensen, “Chaos in AdS$_2$ Holography,” Phys. Rev. Lett. 117 no. 11, (2016) 111601, arXiv:1605.06098
[hep-th].
[83]T. G. Mertens and G. J. Turiaci, “Defects in Jackiw-Teitelboim Quantum Gravity,” JHEP 08 (2019) 127,
arXiv:1904.05228 [hep-th].
[84]A. Blommaert, T. G. Mertens, and H. Verschelde, “Fine Structure of Jackiw-Teitelboim Quantum Gravity,”
JHEP 09 (2019) 066, arXiv:1812.00918 [hep-th].
[85]D. Stanford and E. Witten, “Fermionic Localization of the Schwarzian Theory,” JHEP 10 (2017) 008,
arXiv:1703.04612 [hep-th].
[86]Z. Yang, “The Quantum Gravity Dynamics of Near Extremal Black Holes,” JHEP 05 (2019) 205, arXiv:1809.08647
[hep-th].
[87]A. Blommaert, T. G. Mertens, and H. Verschelde, “The Schwarzian Theory - A Wilson Line Perspective,” JHEP
12 (2018) 022, arXiv:1806.07765 [hep-th].
[88]I. S. Gradshteyn and I. M. Ryzhik, Table of integrals, series, and products. Academic press, 2014.
[89]A. Blommaert, L. V. Iliesiu, and J. Kruthoff, “Gravity factorized,” JHEP 09 (2022) 080, arXiv:2111.07863
[hep-th].
[90]A. Blommaert, T. G. Mertens, and H. Verschelde, “Eigenbranes in Jackiw-Teitelboim gravity,” JHEP 02 (2021)
168, arXiv:1911.11603 [hep-th].
[91]A. Almheiri, X. Dong, and D. Harlow, “Bulk Locality and Quantum Error Correction in AdS/CFT,” JHEP 04
(2015) 163, arXiv:1411.7041 [hep-th].
[92]D. Harlow, “The Ryu–Takayanagi Formula from Quantum Error Correction,” Commun. Math. Phys. 354 no. 3,
(2017) 865–912, arXiv:1607.03901 [hep-th].
[93]G. W. Gibbons and S. W. Hawking, “Action integrals and partition functions in quantum gravity,” Physical
Review D 15 no. 10, (1977) 2752.
[94]J. Kudler-Flam, K. Prabhu, and G. Satishchandran, “Vacua and infrared radiation in de Sitter quantum field
theory,” arXiv:2503.19957 [hep-th].
[95]A. J. Speranza, “An intrinsic cosmological observer,” arXiv:2504.07630 [hep-th].
[96]H. Araki and W. EJ, “A classification of factors,” Publications of the Research Institute for Mathematical
Sciences, Kyoto University. Ser. A 4 no. 1, (1968) 51–130.
[97]V. Ivo, Y.-Z. Li, and J. Maldacena, “The no boundary density matrix,” JHEP 02 (2025) 124, arXiv:2409.14218
[hep-th].
[98]V. Chandrasekaran and K. Prabhu, “Symmetries, charges and conservation laws at causal diamonds in general
relativity,” JHEP 10 (2019) 229, arXiv:1908.00017 [gr-qc].
[99]M. Kaplan and D. Marolf, “The action of HRT-areas as operators in semiclassical gravity,” JHEP 08 (2022)
102, arXiv:2203.04270 [hep-th].
[100]X. Dong, D. Marolf, and P. Rath, “Geometric Entropies and their Hamiltonian Flows,” arXiv:2501.12438
[hep-th].
[101]J. Cotler and K. Jensen, “Emergent unitarity in de Sitter from matrix integrals,” JHEP 12 (2021) 089,
arXiv:1911.12358 [hep-th].
[102]J. Cotler and K. Jensen, “Non-perturbative de Sitter Jackiw-Teitelboim gravity,” JHEP 12 (2024) 016,
arXiv:2401.01925 [hep-th].
[103]N. A. Chernikov and E. A. Tagirov, “Quantum theory of scalar fields in de Sitter space-time,” Ann. Inst.
H. Poincare A Phys. Theor. 9 (1968) 109.
[104]C. Schomblond and P. Spindel, “Conditions d’unicite pour le propagateur delta(x,y) du champ scalaire dans
l’univers de de sitter,” in Annales de l’institut Henri Poincare. Section A, Physique Theorique, vol. 25,
pp. 67–78. 1976.
[105]T. S. Bunch and P. C. W. Davies, “Quantum Field Theory in de Sitter Space: Renormalization by Point
Splitting,” Proc. Roy. Soc. Lond. A 360 (1978) 117–134.
[106]E. Mottola, “Particle Creation in de Sitter Space,” Phys. Rev. D 31 (1985) 754.
[107]B. Allen, “Vacuum states in de sitter space,” Physical Review D 32 no. 12, (1985) 3136.
[108]B. S. Kay and R. M. Wald, “Theorems on the uniqueness and thermal properties of stationary, nonsingular,
quasifree states on spacetimes with a bifurcate killing horizon,” Physics Reports 207 no. 2, (1991) 49–136.
[109]M. Keyl, “Remarks on the relation between causality and quantum fields,” Class. Quant. Grav. 10 (1993)
2353–2362.
[110]H. J. Borchers, “On revolutionizing quantum field theory with Tomita’s modular theory,” J. Math. Phys. 41
(2000) 3604–3673.
[111]N. Pinamonti, K. Sanders, and R. Verch, “Local incompatibility of the microlocal spectrum condition with
the KMS property along spacelike directions in quantum field theory on curved spacetime,” Lett. Math. Phys.
109 no. 8, (2019) 1735–1745, arXiv:1806.02124 [math-ph].
[112]J. Sorce, “Analyticity and the Unruh effect: a study of local modular flow,” JHEP 24 (2024) 040,
arXiv:2403.18937 [hep-th].
[113]R. M. Wald, “Asymptotic behavior of homogeneous cosmological models in the presence of a positive
cosmological constant,” Physical Review D 28 no. 8, (1983) 2118.
[114]S. Hollands, “Correlators, Feynman diagrams, and quantum no-hair in deSitter spacetime,” Commun. Math.
Phys. 319 (2013) 1–68, arXiv:1010.5367 [gr-qc].
[115]S. M. Carroll and A. Chatwin-Davies, “Cosmic Equilibration: A Holographic No-Hair Theorem from the
Generalized Second Law,” Phys. Rev. D 97 no. 4, (2018) 046012, arXiv:1703.09241 [hep-th].
[116]D. Marolf and I. A. Morrison, “The IR stability of de Sitter: Loop corrections to scalar propagators,”
Phys. Rev. D 82 (2010) 105032, arXiv:1006.0035 [gr-qc].
[117]D. Marolf and I. A. Morrison, “The IR stability of de Sitter QFT: results at all orders,” Phys. Rev. D 84
(2011) 044040, arXiv:1010.5327 [gr-qc].
[118]S. Hollands and R. M. Wald, “Quantum fields in curved spacetime,” Phys. Rept. 574 (2015) 1–35,
arXiv:1401.2026 [gr-qc].
[119]B. S. DeWitt and R. W. Brehme, “Radiation damping in a gravitational field,” Annals of Physics 9 no. 2,
(1960) 220–259.
[120]S. Hollands and R. M. Wald, “The Operator Product Expansion in Quantum Field Theory,” arXiv:2312.01096
[hep-th].
[121]S. Hollands, “The Operator product expansion for perturbative quantum field theory in curved spacetime,”
Commun. Math. Phys. 273 (2007) 1–36, arXiv:gr-qc/0605072.
[122]T. W. Kibble, “Topology of cosmic domains and strings,” Journal of Physics A: Mathematical and General 9
no. 8, (1976) 1387.
[123]M. A. Shifman, A. Vainshtein, and V. I. Zakharov, “Can confinement ensure natural cp invariance of strong
interactions?,” Nuclear Physics B 166 no. 3, (1980) 493–506.
[124]M. Dine, W. Fischler, and M. Srednicki, “A simple solution to the strong cp problem with a harmless
axion,” Physics letters B 104 no. 3, (1981) 199–202.
[125]A. R. Zhitnitsky, “On Possible Suppression of the Axion Hadron Interactions. (In Russian),” Sov. J. Nucl.
Phys. 31 (1980) 260.
[126]P. Sikivie, “Axions, domain walls, and the early universe,” Physical Review Letters 48 no. 17, (1982)
1156.
[127]Y. B. Zel’dovich, I. Y. Kobzarev, and L. B. Okun, “Cosmological consequences of spontaneous violation of
discrete symmetry,” Zh. Eksp. Teor. Fiz. 40 (1974) 3–11.
[128]S. E. Aguilar-Gutierrez, T. Hertog, R. Tielemans, J. P. van der Schaar, and T. Van Riet, “Axion-de Sitter
wormholes,” JHEP 11 (2023) 225, arXiv:2306.13951 [hep-th].
[129]S. Gao and R. M. Wald, “Theorems on gravitational time delay and related issues,” Class. Quant. Grav. 17
(2000) 4999–5008, arXiv:gr-qc/0007021.
[130]M. Kontsevich and G. Segal, “Wick Rotation and the Positivity of Energy in Quantum Field Theory,” Quart.
J. Math. Oxford Ser. 72 no. 1-2, (2021) 673–699, arXiv:2105.10161 [hep-th].
[131]E. Witten, “A Note On Complex Spacetime Metrics,” arXiv:2111.06514 [hep-th].
[132]B. Alexandre, A. Etkin, and F.-S. Rassouli, “Unimodular JT gravity and de Sitter quantum cosmology,”
arXiv:2501.17213 [gr-qc].
