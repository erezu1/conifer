# Outline of: The cosmological necklace problem

Abstract:

We investigate 3d de Sitter axion wormhole which contribute to the no-boundary density matrix. We identify “cosmological necklace’’ solutions: an infinite series of Euclidean saddles corresponding with repeated bounces. This results in an unbound gravitational entropy, and a divergent path integral. To remedy this, we study the gravitational path integral using a (mostly) Lorentzian lapse contour. Within a minisuperspace steepest-descent analysis, we find that a single necklace dominates, leading to a finite entropy. A crucial element is to take into account an $(a\to -a)$ redundancy in the FLRW path integral, where $a$ is the scale factor. Surprisingly, the dominant solution is not purely Euclidean. Its entropy turns out to be independent of the axion flux, and equals the empty de Sitter entropy. We also study higher-dimensional necklaces, sourced by either an axion flux or by Yang-Mills instantons, and argue for qualitatively similar results: the single necklace solution dominates along a Lorentzian lapse contour.

# [root] paper
## [sect-1.intro] section: 1 Introduction and summary
### [sect-1.intro-p1] paragraph

Defining the gravitational path integral via summing over all Euclidean geometries and topologies is
notoriously subtle, not least of all because of the unboundedness of the Euclidean action, the so-called
conformal factor problem [1], which is inherently off-shell. Despite these challenges, in 2019, two
significant pieces of progress in the context of black hole physics came from summing over large classes of
Euclidean spacetimes in Jackiw-Teitelboim gravity, a simple 2d model of AdS quantum gravity [2, 3]. In
particular, the inclusion of Euclidean spacetime wormholes elucidates how black holes can evaporate unitarily
(following a Page curve) [3], and why late time matter correlators near black holes stop decaying [2, 4, 5].
This progress emphasized the importance of including non-trivial geometries and topologies in the
gravitational path integral. Indeed, in [2], “all” hyperbolic geometries were included.

### [sect-1.intro-p2] paragraph

In this work, we argue that one should not sum over all geometries and topologies, even when they are real
Euclidean solutions to the Einstein field equations (such solutions trivially satisfy the KSW condition [6,
7]). There is earlier evidence that summing over all Euclidean geometries does not make much sense. For
instance, in AdS$_3$ the sum over all manifolds ending on the holographic torus boundary seems divergent1 (see
however [9]). This seemingly unreasonable output raises questions about the definition of the path integral
itself, as summing over all geometries. Our analysis demonstrates a more severe problem. We identify an
infinite class of problematic classical solutions where incorporating any such saddle yields unphysical
results: their entropy is greater than the Gibbons-Hawking entropy, thus violating the second law of
thermodynamics (as each of these saddles asymptotes to empty dS space at infinite time).

### [sect-1.intro-p3] paragraph

Gibbons and Hawking (GH) [10, 11] proposed that an observer in the de Sitter (dS) static patch has an entropy
$S=A/4\text{G}$, with $A$ the area of the cosmological horizon. As for the case of black holes, there is both
a thermodynamic and a path integral derivation. The path integral derivation follows from evaluating the path
integral classical action of the sphere, the Wick rotation of dS, which equals the exponential of the horizon
area:

\[ \class{l2mpic-0}{\rule[-2.2371em]{4.8452em}{4.9028em}} \quad = e^\frac{A}{4 G}\,. \]

(1.1)

Rotations analytically continue to static patch time evolution. One is naturally tempted to interpret this
sphere as computing some trace of (something like) an identity operator on (something like) the static patch
Hilbert space $\mathcal{H}$:2

\[ \class{l2mpic-1}{\rule[-3.1072em]{10.8193em}{6.6429em}}\quad = e^\frac{A}{4 G}\overset{?}{=}\tr_\mathcal{H}(1)=e^S\,. \]

(1.2)

Is $A/4\text{G}$ an entropy? Further, largely independent, support for this interpretation came from a
Lorentzian calculation that constructed a novel algebra of observables satisfying the Hamiltonian constraint
in the dS static patch [14].3 Remarkably, they showed that such an algebra has a well-defined notion of von
Neumann entropy that equaled the generalized entropy.4 Furthermore, there is suggestive evidence for a state
counting interpretation of the sphere path integral at one-loop [17, 18, 19, 20, 21, 22, 23] (see however [24,
25, 26, 27, 28, 29] for recent tension with this interpretation).

### [sect-1.intro-p4] paragraph

In this work we take the perspective that (much like the Page curve [30] and the late-time correlation
function [31, 32] in AdS/CFT) $S=A/4\text{G}$ is an external input (for instance, from the Lorentzian CLPW
calculation) that helps us better understand the proper definition of the gravitational path integral. In
particular, the setting we will be interested in is the no-boundary density matrix [33, 34, 35, 36, 37], and
more precisely its trace, which ought to compute the dS entropy according to GH. From this perspective, one
views the Gibbons-Hawking proposal as a necessary output of the no-boundary density matrix in a reasonable
theory of gravity. We scrutinize this assertion in the discussion section 5.

### [sect-1.intro-p5] paragraph

Based on equation (1.1), the Euclidean gravitational path integral may appear to be in good shape at tree
level. Unfortunately, as we explain in section 1.1, it is not. Our conclusion will be that the gravitational
path integral cannot be defined as integrating over all Euclidean spacetimes. We will explore an alternative
definition of the gravitational path integral in section 1.2, integrating over (almost) Lorentzian spacetimes.
Unlike the integral over all Euclidean spacetimes, our definition gives a reasonable prediction for the
entropy associated with an observer in more general FLRW cosmologies.

### [sect1.1unentropicsols] section: 1.1 The cosmological necklace problem
#### [sect1.1unentropicsols-p1] paragraph

In this work, we focus on $d$-dimensional FLRW cosmologies with closed spatial slices, obtained by adding
specific matter to Einstein gravity with a positive cosmological constant. Concrete examples include the 3d
axion de Sitter wormholes that we will study in section 2, higher dimensional axion wormholes of section 3 and
the magnetic wormholes of section 4.

#### [sect1.1unentropicsols-p2] paragraph

A concrete example of such a spacetime is equation (2.6). Adding homogeneous matter to de Sitter space enables
a comoving observer to see a greater portion of the spacetime. Depending on the amount of matter stress
energy, the observer in this spacetime can have causal access to more than half of the spatial slice, or even
a whole spatial slice:

\[ \class{l2mpic-2}{\rule[-5.0859em]{13.3443em}{10.6003em}} \qquad \qquad\qquad
    \class{l2mpic-3}{\rule[-5.1426em]{11.8571em}{10.7139em}} \]

(1.3)

For the present argument, we consider scenario 1, which limits (as the matter density approaches zero) to dS
space. In this case, an observer has a causal horizon.

#### [sect1.1unentropicsols-p3] paragraph

For these theories, we study the no-boundary state for an observer existing in the corresponding matter
density sector. The analog of the dS sphere solution, for the axionic and Yang-Mills matter which we consider
in this work, would be a Wick rotation of the aforementioned FLRW solutions, of the type

\[ \d s^2=N^2\d \tau^2+a(\tau)^2\d \Omega_{d-1}^2\,,\quad 0\leq \tau\leq 1, \]

(1.4)

with $N$ the Euclidean lapse. To investigate the entropy, as in (1.2), one takes $a(0)=a(1)$, which results in
a compact geometry (the unusual conditions for matter configurations to result in such Euclidean wormhole
solutions are discussed in section 4). We can draw these wormhole solutions as follows

\[ \class{l2mpic-4}{\rule[-2.2470em]{11.5936em}{4.9226em}} \quad = e^{-I_0} \neq e^\frac{A}{4 G}, \]

(1.5)

where the two blue ends are glued together to produce a closed Euclidean spacetime and $I_0<0$ is the
solution’s on-shell action. In the empty dS limit, the blue region pinches off, reproducing the sphere. Unlike
the sphere, the wormhole action has no (obvious) interpretation as an extremal area, or the area of the
boundary of a stationary observer’s causal diamond. Nevertheless, with motivations from [38] it was suggested
in [39] that $-I_0$ could be interpreted as the gravitational entropy associated with the observer’s causal
diamond (or, a Cauchy slice of the diamond):5

\[ \class{l2mpic-5}{\rule[-5.5954em]{6.5936em}{11.6195em}} \quad = \,e^{-I_0}\overset{?}{=}\tr_\mathcal{H}(1)=e^S\,. \]

(1.6)

#### [sect1.1unentropicsols-p4] paragraph

So far, the picture seems reasonable. The issue, however, is that we can easily construct more dominant
saddles by gluing $k\in \mathbb{Z}$ copies of the wormhole solutions,

\[ \class{l2mpic-6}{\rule[-2.7756em]{24.2631em}{5.9799em}}\quad = e^{-k I_0}\,. \]

(1.7)

These solutions are also closed Euclidean saddles with the same boundary conditions, only with a different
lapse $N=k N_0$, with $N_0$ the lapse of the original wormhole solution. Being simple covers of the original
solution, no local criterion can allow the original solution but exclude its covers. Considering all these
solutions as contributions to the no-boundary trace, the entropy of each is $k \cdot |I_0|$. Thus, any $k>1$
cover is more dominant than the wormhole. Worse, there is no dominant saddle and the entropy diverges. We
refer to this as the necklace problem. What makes this setup stand out is that the divergence comes from a sum
over real classical solutions, rather than field configurations. We therefore conclude that summing over all
Euclidean classical solutions, and excitations around them, is not a reasonable definition of a gravitational
path integral.

#### [sect1.1unentropicsols-p5] paragraph

In the remainder of this work we advance an alternative definition of the gravitational path integral, one
that leads to a convergent answer for the sum over geometries and that agrees with GH in the empty dS limit.
We note that the necklace problem persists in the empty dS case if one allows for disconnected manifolds: a
Euclidean path integral sums over multiple copies of the Euclidean sphere:6

\[ \class{l2mpic-7}{\rule[-2.7757em]{13.9190em}{5.9801em}}\quad = e^{-k I} \]

(1.8)

which can be thought of as a limit where the wormhole throat becomes small. This is inconsistent with GH. See
section 2.3. Our proposal rules out necklaces with $k>1$.

### [sect1.2proposal] section: 1.2 Resolution: Lorentzian lapses
#### [sect1.2proposal-p1] paragraph

Instead of a local criterion for on-shell solutions, we will consider an off-shell prescription for the no-
boundary path integral that will yield global constraints on possible saddles. To go off-shell, we will
consider the gravitational path integral in the ADM formalism in minisuperspace variables; see section 2. The
dynamical fields are $N$ and $a$ (and the conjugate momentum $p$ of $a$) from (1.4). We consider quantum
gravity defined by the following Lorentzian lapse contour:7

\[ \boxed{N=\varepsilon+\i \mathbb{R}\,} \]

(1.9)

Lorentzian lapse contours have a long history in quantum cosmology [42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
52, 53, 54, 55, 56]; see [57] for a review.8

#### [sect1.2proposal-p2] paragraph

In order to study the effects of this contour, it will prove useful to first integrate out $a(\tau)$ and
obtain an effective action $I(N)$ for the no-boundary trace. We will either do it exactly when possible, as in
section 2.2, or by saddle point when not possible. This action will have saddles at $N=k\cdot N_0$,
representing necklaces. We will see in section 2 that there are two important and topologically distinct
classes of solutions for $a(\tau)$. They arise because the metric depends only on the combination $a^2$. This
means that if we compute the density matrix of the universe to propagate from a slice with metric
$a^2\d\Omega_d^2$ to itself, we have to sum two propagators in the minisuperspace quantum mechanics (where $a$
is a particle with potential $V(a)$, see equation (2.11)):

\[ \mathcal{G}_N(a\rvert a)+\mathcal{G}_N(a\rvert -a)\,. \]

(1.10)

The other combinations $\mathcal{G}_N(-a\rvert -a)$ and $\mathcal{G}_N(-a\rvert a)$ produce a factor of two.
In other words, we are treating $\bf{a\leftrightarrow-a}$ as a gauge redundancy. We now describe the
configurations $a(\tau)$ that contribute to each propagator.

#### [configuration-1-tunneling-solutions] section: Configuration 1: Tunneling solutions
##### [configuration-1-tunneling-solutions-p1] paragraph

Consider first the configurations that contribute to $\mathcal{G}_N(a\rvert -a)$. We will conclude that these
configurations capture saddles with odd values of $k=2n+1$. In terms of a (typical) FLRW potential $V(a)$ (see
section 2.1 for an explicit example) the simplest solution (with $k=1$ or $N=N_0$) looks as follows:9

\[ \class{l2mpic-8}{\rule[-3.4345em]{23.1261em}{7.2975em}} \]

(1.11)

The universe starts at spatial size $a$ (we consider $a=a_\text{max}$, the thickest part of the necklace in
equation (1.5)) and decreases in size, until it reaches $a_\text{min}$. At this point, the Euclidean solution
tunnels through a Lorentzian region and goes through $a=0$. Then $a$ becomes negative and grows in absolute
value, first in Lorentzian space, and then in Euclidean space until the size of the universe again reaches
$\abs{a}=a_\text{max}$.

##### [configuration-1-tunneling-solutions-p2] paragraph

Summarizing: the geometry $a(\tau)$ for $k=1$ ($N=N_0$) looks like:10

\[ \class{l2mpic-9}{\rule[-4.6675em]{28.6711em}{9.7636em}} \]

(1.12)

For 3d axion wormholes, one can show that this solution contributes to $\mathcal{G}(a\rvert -a)$ by analyzing
the exact quantum propagator (see [41] for a related calculations). We avoid the big-bang singularity at $a=0$
by going in the complex $a$ plane, resulting in a bra-ket wormhole [66, 67]. For higher necklaces $k>1$, we
paste $2n+1$ copies of this spacetime together.

##### [configuration-1-tunneling-solutions-p3] paragraph

The complex action $I_{a\to-a}(N)=-\log \mathcal{G}(a\rvert-a)$ schematically has the following structure:

\[ \class{l2mpic-10}{\rule[-4.5583em]{26.3824em}{9.5453em}} \]

(1.13)

A Picard-Lefschetz analysis crucially shows that only the saddles $k\leq 1$ contribute. This avoids the
problematic saddles. The geometry pictured in (1.12) is the leading contribution to the gravitational path
integral, and predicts an entropy $S=-I$ that agrees with GH in the empty dS limit. The key feature that makes
us pick up the usual GH saddle ($k=1$) is the presence of a pole for $\bf{N\to0}$ in the propagator
$\mathcal{G}_N(a\rvert -a)$. This arises in the quantum mechanics because it takes infinite energy to go from
$a\to -a$ in no time (see section 2.2). This is the reason why the Lorentzian contour $N=\varepsilon+\i
\mathbb{R}$ can pick up a positive entropy saddle, even though Lorentzian metrics have entirely imaginary
actions. Positive entropy requires this pole. Fortunately, this pole is universal. See section 2.5.

##### [configuration-1-tunneling-solutions-p4] paragraph

Note that solutions with negative $e^{\varphi} \equiv a<0$ also appear to contribute in the timelike Liouville
path integral [68], along the Hankel contour [69]. In timelike Liouville, the rigid framework of 2d CFT can be
used to better understand the rules of the gravitational path integral. In this setup, 2d CFT naively
therefore seems to agree that $a<0$ should be taken seriously.

#### [configuration-2-standard-solutions] section: Configuration 2: Standard solutions
##### [configuration-2-standard-solutions-p1] paragraph

Next, we consider the configurations which contribute to $\mathcal{G}_N(a\rvert a)$. We will find that these
configurations capture saddles with even $k=2n$. These consist of $2n$ copies of the spacetime in equation
(1.12), glued together. In terms of the potential $V(a)$ (1.11), the universe bounces back and forth $n$
times, ending and starting at an identical value of $a$. The case $k=0$ describes a universe with total
elapsed time $N=0$ (static) with size $a=a_\text{max}$. The complex structure of $I_{a\to a}(N)=-\log
\mathcal{G}(a\rvert a)$ with a contour $N=\varepsilon+\i \mathbb{R}$ looks as follows:

\[ \class{l2mpic-11}{\rule[-4.5583em]{26.5406em}{9.5453em}} \]

(1.14)

The steepest descent contours show that only those saddles with $n<1$ contribute. We stress that the problem
of unphysical saddles with a Euclidean action that is unbounded from below is already there within this more
standard $\mathcal{G}(a\rvert a)$ calculation. A Lorentzian $N=\varepsilon+\i \mathbb{R}$ contour avoids this
divergence.

#### [conclusion] section: Conclusion
##### [conclusion-p1] paragraph

Thus, defining the gravitational path integral through the contour $N=\varepsilon+\i \mathbb{R}$ rules out the
problematic saddles ($k>1$) with unbound actions. The Gibbons-Hawking saddle dominates. This is consistent
with the prediction $S=-I$ for the entropy associated with an FLRW observer, and agrees with GH in the empty
dS limit. This suggests that $N=\varepsilon+\i \mathbb{R}$ is the appropriate contour to define the
gravitational path integral, from an observer’s perspective.

##### [conclusion-p2] paragraph

As we highlight more in the discussion section 5, another possible Lorentzian contour would be
$N=-\varepsilon+\i \mathbb{R}$ or $N = \i \mathbb{R}^+$. These contours only pick up the saddles with $k\leq
0$ and crucially not $k=1$. This suggests $k=0$ as the dominating gravitational “saddle” as predicted by the
contour $N=-\varepsilon+\i \mathbb{R}$. Since the only non-trivial saddles contribute non-perturbatively
suppressed terms in $G$, one might call it a “Vilenkin-type contour” [70, 47, 71, 45, 72, 46].

##### [conclusion-p3] paragraph

A comment on fluctuations is in order. The conformal mode has wrong-sign fluctuations for $\text{Re}\,N>0$. A
purely Lorentzian lapse contour avoids this problem. Because of the positive regulator, the contour
$N=\varepsilon+\i\mathbb{R}$, unfortunately, does not. Equivalently: the GH saddle, which dominates the path
integral, still suffers from a conformal mode problem. On the bright side, fluctuations of matter fields are
stable for $\text{Re}\,N>0$. On the Vilenkin contour, the conformal mode problem is resolved but all matter
fluctuations are unstable. We comment more on “allowability” of these saddles in the discussion section 5.

##### [conclusion-p4] paragraph

Throughout, we will rely on the following standard statement of Picard-Lefschetz theory [73, 51]. For an
integral of $e^{-I(N)}$ with $I(N)$ holomorphic away from isolated singularities, the integration contour
$\mathcal{C}$ is deformed to a sum of steepest descent contours $\mathcal{D}_\sigma$ (Lefschetz thimbles),
attached to saddle points $\sigma$:

\[ \int_\mathcal{C}\d N\, e^{-I(N)}=\sum_\sigma n_\sigma \int_{\mathcal{D}_\sigma}\d N\, e^{-I(N)}\,. \]

(1.15)

Here, the integer $n_\sigma$ is the intersection number of $\mathcal{C}$ with the steepest ascent contour
$\mathcal{A}_\sigma$ of the saddle $\sigma$. A saddle contributes when $n_\sigma \neq 0$. Both
$\mathcal{D}_\sigma,\mathcal{A}_\sigma$ have constant $\text{Im}\,I(N)$ (constant phase).

### [section-1.3] section: 1.3 Structure
#### [section-1.3-p1] paragraph

In the remainder of this article, we will work out detailed examples. This work is organized as follows.

#### [section-1.3-p2] paragraph

In section 2 we investigate 3d axion-dS wormholes [74, 75]. Following [41] we compute the propagators
$\mathcal{G}_N(a\rvert \pm a)$ via the minisuperspace quantum mechanics, and compare with classical solutions.
We then perform a steepest descent analysis. We find that the $k=1$ classical solution dominates for the
contour $N=\varepsilon+\i \mathbb{R}$. The $k=0$ saddle dominates for the contour $N=-\varepsilon+\i
\mathbb{R}$. One very interesting but puzzling fact is that the resulting $k=1$ action is independent of the
amount of axion flux $q$:

\[ \boxed{-I=\frac{\pi}{2G}\overset{?}{=}S\quad q\text{-independent}\,} \]

(1.16)

This equals $A/4G$ for the empty dS space. This gives a clear and sufficiently simple target for Lorentzian
algebraic calculations to reproduce (or disprove). We leave a further investigation of this fact, including
whether this generalizes to higher dimensions, to future work.

#### [section-1.3-p3] paragraph

In section 3 we study higher dimensional axion wormholes numerically. These numerics take place in what we
call kinetic gauge. In appendix A we study 5d axion wormholes in what we call proper-time gauge, analytically
and numerically.

#### [section-1.3-p4] paragraph

In section 4 we construct Euclidean wormhole solutions for Einstein gravity coupled to SO$(d-1)$ Yang-Mills
theory. These SO$(d-1)$ magnetic wormholes have a cosmological necklace problem with identical resolution as
the axion case.

#### [section-1.3-p5] paragraph

Finally, in the discussion section 5 we take stock of the two Lorentzian lapse contours $N=\pm \varepsilon+\i
\mathbb{R}$.

## [sect2-3daxion] section: 2 Three dimensional axion necklaces
### [sect2-3daxion-p1] paragraph

This section is the core of this paper. We work out in detail the propagators $\mathcal{G}_N(a\rvert \pm a)$
for 3d axion-dS wormhole solutions [75, 41] and find the general structure claimed in section 1.2. In section
2.1, we explain the details of our setup (namely, the definition of the propagators $\mathcal{G}_N(a\rvert \pm
a)$ and which of their properties we will investigate). In section 2.2 (within the minisuperspace
approximation), we exactly evaluate the gravitational propagators $\mathcal{G}_N(a\rvert \pm a)$. We study the
classical limit of the exact answer and find the structure of saddles and steepest descent contours as claimed
in equation (1.13) and (1.14).

### [sect2-3daxion-p2] paragraph

The exact quantum propagator is powerful, because it implicitly already makes a selection in which
configurations contribute to the gravitational path integral. We clarify this point in section 2.4, where we
study the classical solutions of the equations of motion, and identify which of those solutions actually do
contribute in the quantum propagators $\mathcal{G}_N(a\rvert \pm a)$. Two features which we will confirm are
that the odd saddles $k=2n+1$ appear as saddles of (the effective action for) $\mathcal{G}_N(a\rvert -a)$, as
discussed around (1.11), and that the even saddles $k=2n$ appear only in $\mathcal{G}_N(a\rvert a)$. Which of
these saddles actually contributes is then determined by the steepest descent analysis. On the contour
$N=\varepsilon+\i\mathbb{R}$ only $k=1$ and the (suppressed) $k<0$ saddles contribute in the odd sector, and
only $k\leq 0$ in the even sector. We furthermore show that the Lorentzian tunneling in the odd sectors as
depicted in equation (1.12) can be deduced from the exact propagator $\mathcal{G}_N(a\rvert \pm a)$.

### [sect2-3daxion-p3] paragraph

As this analysis contains several elements, we first scrutinize the classical solutions for empty dS in
section 2.3, where a contour $N=\varepsilon+\i \mathbb{R}$ results in a single sphere as the dominant saddle.
In section 2.5 we briefly discuss a generalization of part of our argument to more general FLRW potentials
$V(a)$. In section 2.6 we provide an intuitive argument for why the on-shell action of our 3d axion wormholes
is $q$-independent, matching the empty dS cosmological horizon area (1.16): the contour which computes the on-
shell action may be deformed to late times - where any FLRW solution will approach empty dS.

### [sect2.1setup] section: 2.1 Setup
#### [sect2.1setup-p1] paragraph

Following [74, 41] we consider 3d axion-dS wormholes. See [75] for background. Consider the Euclidean action
(up to boundary terms) with Hubble constant set to $H=1$:

\[ I= -\frac{1}{16\pi G}\int \d^3 x\sqrt{g}(R-2)+\frac{1}{4}\int\d^3 x\sqrt{g} H^{\mu \nu}H_{\mu\nu}\,,\quad H_{\mu\nu}=Q\, \eps_{\mu\nu}(S^2)\,,\quad Q^2 =  \frac{q^2}{16\pi G}\, \]

(2.1)

where $\eps_{\mu\nu}(S^2)$ is the volume form of the spatial sphere. Consider furthermore the FLRW ansatz
(1.4):

\[ \d s^2=N^2\d \tau^2+ a(\tau)^2\d \Omega_2\,,\quad \d \Omega_2=\d\theta^2+\sin^2(\theta)\d \phi^2\,,\quad 0\leq \tau\leq 1\,. \]

(2.2)

Throughout this section, we will study the gravitational path integral with boundary conditions where one
fixes the induced boundary geometry on the initial and final Cauchy slices:

\[ \d s^2_\text{boundary}\rvert_{\tau=0}=a_0^2 \d \Omega_2^2\,,\quad \d s^2_\text{boundary}\rvert_{\tau=1}=a_1^2 \d \Omega_2^2\,. \]

(2.3)

The range of the time variable $0\leq \tau\leq 1$ is convention, placing all the dynamical data about the
spacetime in the fields $N$ and $a(\tau)$. The action (2.1) evaluated on FLRW spacetimes (2.2) with $0\leq
\tau\leq 1$ becomes:

\[ \boxed{I=\frac{1}{\text{G}}\int_0^1\d \tau \bigg\{ -\frac{1}{2N}\dot{a}^2+\frac{N}{2}\bigg(-1+a^2+\frac{q^2}{4}\frac{1}{a^2}  \bigg) \bigg\}\,} \]

(2.4)

The Friedmann equation is obtained by variation with respect to the lapse function $N$:

\[ \begin{align*}
\frac{1}{N^2}\frac{\dot{a}^2}{a^2} -\frac{1}{a^2} +1 + \frac{q^2}{4 }\frac{1}{a^4}=0\,. \tag{2.5}\end{align*}
\]

The solutions are:

\[ a^2=\frac{1-\sqrt{1-q^2}}{2}+\sqrt{1-q^2}\cos(N \tau)^2\,. \]

(2.6)

Notice that the total Euclidean proper time between the two ends of the spacetime equals $N$. Rotating
$\tau=\i T$ we obtain Lorentzian expanding dS space:

\[ a^2=\frac{1-\sqrt{1-q^2}}{2}+\sqrt{1-q^2}\cosh( NT)^2\,. \]

(2.7)

These asymptote to exponentially expanding 3d dS space, as expected. Indeed, the axion term in (2.5) becomes
subdominant for $a\to\infty$. The maximal size of the Euclidean solution and the minimal size of the
Lorentzian solution occur at the time-reflection symmetric point from which Lorentzian expansion starts. This
maximal size equals:

\[ a_\text{max}^2=\frac{1+\sqrt{1-q^2}}{2}\,. \]

(2.8)

The solutions oscillate in Euclidean signature. Variation with respect to $a$ of (2.4) produces the second
Friedmann equation:

\[ \frac{1}{N^2}\ddot{a}+a-\frac{q^2}{4}\frac{1}{a^3}=0\,. \]

(2.9)

Observe that solving the $N$ EOM (2.5) guarantees a solution for the $a$ EOM (acting with $\dot{\cdots}$ on
the $N$ EOM produces the $a$ EOM). But solving the $a$ EOM does not guarantee a solution for the $N$ EOM.

#### [sect2.1setup-p2] paragraph

A path integral with action (2.4), initial value $a_0$ and final value $a_1$ decomposes into minisuperspace
quantum mechanics propagators as follows:

\[ \int_\mathcal{C}\d N \int_{a_0}^{a_1} \mathcal{D}a\,e^{-I}=\int_\mathcal{C}\d N\,\mathcal{G}_N(a_0\rvert a_1)\,. \]

(2.10)

Here $\mathcal{G}_N(a_0\rvert a_1)$ is a propagator of the $a$ quantum mechanics describing propagation from
$a_0$ to $a_1$ with Euclidean time $N$:

\[ \mathcal{G}_N(a_0\rvert a_1)=\bra{a_1}e^{-\frac{N}{G} H_\text{WDW}}\ket{a_0}\,,\quad H_\text{WDW}=E=\frac{p^2}{2}+V(a)\,,\quad \boxed{2V(a)=-1+a^2+\frac{q^2}{4}\frac{1}{a^2}\,} \]

(2.11)

The Hamiltonian for this minisuperspace quantum mechanics is the gravitational WDW Hamiltonian [76]:
$H_\text{WDW}$. This Hamiltonian describes the propagation of a particle (the universe) in the potential
$V(a)$:

\[ \class{l2mpic-12}{\rule[-3.4345em]{18.9104em}{7.2975em}} \]

(2.12)

Note that $a$ can take values on all of $\mathbb{R}$. Here, $p$ is the Euclidean momentum conjugate to $a$:
$p=-\dot{a}/N$. The $N$ equation of motion (the Hamiltonian constraint) is saying that the universe has
vanishing energy:

\[ H_\text{WDW}=\frac{p^2}{2}+V(a)=0\,. \]

(2.13)

This is the usual statement that “the gravitational Hamiltonian vanishes”. This is a consequence of the fact
that time reparameterizations are redundancies in gravity. One such reparameterization changes the value of
$N$. This translates in minisuperspace into the fact that, in (2.4), $N$ shows up as a Lagrange multiplier
(after going to first order variables, see (2.24)), which indeed enforces that $H_\text{WDW}=0$.

#### [gauged-quantum-mechanics] section: Gauged quantum mechanics
##### [gauged-quantum-mechanics-p1] paragraph

To investigate a gravitational path integral subject to boundary conditions (2.3), we should take into account
the important fact that $a$ and $-a$ in the quantum mechanics describe physically equivalent spatial metrics
$a^2\d \Omega_2^2$. As such, the gravitational path integral decomposes into a sum of four propagators,
integrated over elapsed time:

\[ \begin{align*}
   &\rho_\text{no-boundary}(a_0^2\rvert a_1^2)= \quad \class{l2mpic-13}{\rule[-2.1587em]{11.1273em}{4.7459em}}
   \\&\qquad = \int_\mathcal{C}\d N\,\mathcal{G}_N(a_0\rvert a_1)+\int_\mathcal{C}\d
N\,\mathcal{G}_N(a_0\rvert -a_1)+\int_\mathcal{C}\d N\,\mathcal{G}_N(-a_0\rvert a_1)+\int_\mathcal{C}\d
N\,\mathcal{G}_N(-a_0\rvert -a_1) \tag{2.14}\end{align*} \]

The question which we are investigating in this work is what the correct gravitational contour $\mathcal{C}$
for the lapse integral is. As explained in the introduction section 1.1, the naive Euclidean gravitational
path integral would amount to integrating over positive real lapses $0\leq N<\infty$. We now detail the
statement made around equation (1.7): this Euclidean contour leads to a divergent gravitational amplitude.

##### [gauged-quantum-mechanics-p2] paragraph

For the gravitational path integral to produce a prediction for the entropy associated with the causal patch
of an observer in the spacetime (2.7),11 as explained in section 1.1, we are interested in computing a closed
gravitational path integral. We will do this semiclassically. The classical closed solutions are of the type
shown in equation (1.7). They are obtained by gluing the Euclidean solution (2.6) at matching zero extrinsic
curvature surfaces, where $a^2=a_\text{max}^2$.12 Imposing the boundary conditions:

\[ a^2\rvert_{\tau=0}=a^2\rvert_{\tau=1}=a^2_\text{max}\,, \]

(2.16)

on the classical solutions (2.6), determines the set of classical solutions for $N$ and $a$ completely:

\[ N=k\pi\,,\quad  a^2=\frac{1-\sqrt{1-q^2}}{2}+\sqrt{1-q^2}\cos(k \pi \tau)^2\,,\quad 0<\tau<1\,,\quad k\in\mathbb{Z}\,. \]

(2.17)

These solutions look like necklaces, once we do the gluing of the $\tau=0$ and $\tau=1$ zero extrinsic
curvature slices (as was required to obtain a solution which contributes to the closed gravitational path
integral). The Euclidean lapse contour $0\leq N<\infty$ would thus semiclassically correspond to

\[ \mathcal{Z}_\text{no-boundary}= \sum_{k=0}^\infty\qquad 
    \class{l2mpic-14}{\rule[-3.8467em]{28.5406em}{8.1220em}} \]

(2.18)

The Euclidean on-shell action for each necklace (2.17) is negative and equals:

\[ I_\text{Euclidean}=-\frac{k\pi (1-q)}{2G}<0\,. \]

(2.19)

A Euclidean lapse contour $0\leq N<\infty$ sums over the $k\geq 0$ saddles and leads to a divergent Euclidean
path integral. This is a concrete example of the necklace problem as explained in section 1.1. The sum over
all Euclidean saddles makes no sense [77, 78, 39], and hence neither does the Euclidean gravitational path
integral (given that physically interesting quantities had better be finite).

#### [plan-for-the-remainder-of-this-section] section: Plan for the remainder of this section
##### [plan-for-the-remainder-of-this-section-p1] paragraph

We will investigate a definition of the lapse contour $\mathcal{C}$ in equation (2.10) which does lead to a
finite and reasonable answer for the gravitational path integral; and agrees with the Lorentzian semiclassical
prediction (1.2) by CLPW for empty dS. The gravitational path integral for closed amplitudes takes
semiclassically the following form:13

\[ \boxed{\mathcal{Z}_\text{no-boundary}=2 \int_\mathcal{C} \d N\,\mathcal{G}_N(a_\text{max}\rvert a_\text{max})+2 \int_\mathcal{C}\d N\,\mathcal{G}_N(a_\text{max}\rvert -a_\text{max})\,,} \]

(2.20)

As compared to equation (2.14), we have accounted for sign symmetry in the propagator when $a_0^2=a_1^2$.
Integrating over different values of $a_0^2$ at which to glue is a gravitational redundancy as this
corresponds to slicing the gravitational solution (2.17) at different $\tau$ values.14 In section 2.2, we
shall evaluate the propagators $\mathcal{G}_N(a\rvert \pm a)$. We then take a semiclassical limit of the exact
expression to obtain effective actions

\[ \mathcal{G}_N(a\rvert a)\to e^{-I_{a\to a}(N)}\,,\quad \mathcal{G}_N(a\rvert -a)\to e^{-I_{a\to -a}(N)}\,. \]

(2.21)

Later, in section 2.4, we will see that these effective actions $I_{a\to\pm a}(N)$ may be found by solving
only the $a$ equations of motion (2.9) subject to boundary conditions (2.16), and plugging these into the
gravity action (2.4). One can then evaluate the lapse integral in equation (2.20) semiclassically, by
performing a Picard-Lefschetz analysis (steepest descent). We will show that Lorentzian contours result in
reasonable answers. For the contour $\mathcal{C}=\varepsilon+\i \mathbb{R}$ the saddle $k=1$ dominates
$\mathcal{Z}_\text{no-boundary}$, in agreement with CLPW. For the contour
$\mathcal{C}=-\varepsilon+\i\mathbb{R}$ the trivial “saddle” $k=0$ will dominate. As explained in the
introduction section 1.2 and expanded upon in the discussion section 5, this would appear a reasonable answer
when studying $\rho_\text{no-boundary}(a_0^2\rvert a_1^2)$ for the purposes of understanding the global
Hilbert space (which no single observer has access to, but which might nevertheless be of independent
interest).

### [sect2.2exact] section: 2.2 Resolution 1: Exact quantum amplitude
#### [sect2.2exact-p1] paragraph

We start with an exact evaluation of the propagator $\mathcal{G}_N(a_1\rvert a_2)$:

\[ \mathcal{G}_N(a_0\rvert a_1)=\bra{a_1}e^{-\frac{N}{G} H_\text{WDW}}\ket{a_0}\,. \]

(2.22)

Recall the action (2.4). Introduce the Euclidean momentum

\[ p=-\frac{\dot{a}}{N}\,. \]

(2.23)

The Euclidean action becomes

\[ I=\frac{1}{G}\int_{0}^{1}\d \tau\big(\, p\, \dot{a}+N H_\text{WDW}\big)\,,\quad H_\text{WDW}=\frac{p^2}{2}+V(a)\,. \]

(2.24)

$p$ acts on wavefunctions $\psi(a)$ as: $p=-G\,\d/\d a$. One fixes the propagator $\mathcal{G}_N(a_1\rvert
a_2)=\bra{a_2} e^{-\frac{N}{G} H_\text{WDW}}\ket{a_1}$ following [41, 79] by demanding that it satisfies the
Schrodinger equation:

\[ -G \frac{\d}{\d N} \mathcal{G}_N(a_1\rvert a_2) = \frac{1}{2} \bigg( G^2 \frac{\d ^2}{\d a_2^2} -1+a_2^2+\frac{q^2}{4}\frac{1}{a_2^2} \bigg) \,\mathcal{G}_N(a_1\rvert a_2)\,. \]

(2.25)

With the boundary condition

\[ \mathcal{G}_{N\to 0}(a_1\rvert a_2)=\left\langle a_2\rvert a_1\right\rangle\,, \]

(2.26)

quite non-trivially one obtains the following solution:15

\[ \mathcal{G}_N(a_1\rvert a_2) = \frac{2 \sqrt{-a_1a_2}}{\sin(N)} \exp\bigg\{ \frac{N}{2G} +\frac{(a_1^2+a_2^2)}{2G\tan(N)} \bigg\} K_{\nu } \bigg( \frac{a_1a_2}{G\sin(N)} \bigg)\,,\quad \nu = \sqrt{\frac{1}{4}-{\frac{q^2}{4G^2}}}\,. \]

(2.28)

One checks using the differential equation satisfied by the modified Bessel function $K_\nu(x)$ that, indeed,
(2.28) satisfies the Schrodinger equation (2.25). There is another solution $I_\nu(x)$, which was advocated by
[41] as being the correct propagator. We argue that crucially the correct propagator involves $K_\nu(x)$.
Using the Bessel asymptotics and equation (2.28) one indeed obtains for $N\to 0$

\[ \mathcal{G}_N(a_1\rvert a_2)\to 2\pi  \frac{\sqrt{G}}{\sqrt{-2\pi N}} e^{\frac{(a_1-a_2)^2}{2NG} } \to 2\pi G \, \delta (a_1-a_2)\sim \left\langle a_2\rvert a_1\right\rangle\,. \]

(2.29)

Instead, $I_\nu(x)$ would result in $\delta(a_1+a_2)$, the wrong result for a quantum mechanical propagator in
the limit $N\to 0$. This selects the solution (2.28).

#### [sect2.2exact-p2] paragraph

As discussed in equation (2.21) and equation (1.13), we now consider the semiclassical $G\to 0$ limit, to
compute an effective action $I_{a\to-a}(N)=-\log \mathcal{G}_N(a\rvert-a)$ and $I_{a\to a}(N)=-\log
\mathcal{G}_N(a\rvert a)$. For $G\to 0$ we observe that $\nu\to \i q/2 G$. For this range of parameters, we
deduce the following Bessel asymptotics:

\[ K_{\i z/G} (x/G) =\frac{1}{2}\int_{-\infty}^{+\infty } \d T \, \exp\bigg\{-\frac{x}{G}\cosh(T)+\i\frac{z}{G}T\bigg\}\to \exp\bigg\{-\frac{x}{G}\sqrt{1-z^2/x^2}-\frac{z}{G}\arcsin(z/x)\bigg\}\,. \]

(2.30)

Here we used that the integral representation for $G\to 0$ is dominated by a saddle point: $\sinh(T)=\i z/x$.
Inserting this classical approximation in equation (2.28) gives the following effective action:16

\[ G I_{a_1 \to a_2}(N) = -\frac{N}{2} -\frac{a^2_1+a_2^2}{2}\cot(N) +\frac{a_1 a_2}{\sin (N)} \sqrt{1- \frac{q^2}{4}\frac{\sin^2 (N)}{a_1^2 a_2^2} }+ \frac{q}{2}\arcsin \bigg( \frac{q}{2}\frac{\sin(N)}{a_1 a_2}\bigg)\,. \]

(2.31)

The arcsin$(x)$ is on the principle branch close to the origin $N\to 0$ and continued away from that. In the
diagonal case $a_1=a_2=a$, this action reduces to:

\[ G I_{a \to a}(N) = -\frac{N}{2} -\frac{a^2}{\tan(N)} +\frac{a^2}{\sin (N)} \sqrt{1- \frac{q^2}{4}\frac{\sin^2 (N)}{ a^4} }+ \frac{q}{2}\arcsin \bigg( \frac{q}{2}\frac{\sin(N)}{a^2}\bigg)\,. \]

(2.32)

For the $a_1\to -a_2$ configuration, we simply analytically continue this result from $a_2$ to $-a_2$:

\[ G I_{a_1\to -a_2}(N) = -\frac{N}{2} -\frac{a^2_1 +a_2^2}{2}\cot(N) -\frac{a_1 a_2}{\sin (N)} \sqrt{1- \frac{q^2}{4}\frac{\sin^2 (N)}{a_1^2 a_2^2} }- \frac{q}{2}\arcsin \bigg( \frac{q}{2}\frac{\sin(N)}{a_1 a_2}\bigg)\,. \]

(2.33)

We are almost exclusively interested in the diagonal case:

\[ \boxed{G I_{a \to -a}(N) = -\frac{N}{2} -\frac{a^2}{\tan(N)} -\frac{a^2}{\sin (N)} \sqrt{1- \frac{q^2}{4}\frac{\sin^2 (N)}{ a^4} }- \frac{q}{2}\arcsin \bigg( \frac{q}{2}\frac{\sin(N)}{a^2}\bigg)\,} \]

(2.34)

Note that (2.31) has square root branch points at $\sin(N) = \pm 2 a_1 a_2/q$, which for
$\abs{a_1}=\abs{a_2}=a_\text{max}$ and $0\leq q< 1$ (our case of interest) are off the real $N$ axis. The
branch cuts are associated with Stokes lines for the Bessel functions: the function becomes oscillatory. The
two sides of the branch cut both contribute (this is obvious because $K_{\i z}(x)$ is real for real $x$).
These branch cuts are largely irrelevant for our present purposes, however.

#### [sect2.2exact-p3] paragraph

For the purposes of doing a GH calculation, as explained around equation (2.20), we are especially interested
in the scenario where the universe’s evolution starts and ends at its maximal Euclidean size:

#### [fig-plot_plus_sol_N_plane] figure: Figure 1

Figure 1. Action $I_{a_\text{max} \to a_\text{max}}(N)$ (in (2.32)) in the complex $N$ plane. Poles in the
action are red $\cross$’s. Saddles are black dots. Steepest descent (ascent) curves are black solid (dashed)
lines. The Lorentzian $N=\varepsilon+\i\mathbb{R}$ contour is drawn vertically in magenta and the absolutely
convergent contour that it deforms into is shown in orange. Here $G$ was slightly complexified to make the
ascent/descent lines non-degenerate.

#### [sect2.2exact-p4] paragraph

\[ a^2=a_\text{max}^2=\frac{1+\sqrt{1-q^2}}{2}\,. \]

(2.35)

The action $I_{a \to a}(N)$ has saddles at $N=2n\pi$ and poles at $N=(2n+1)\pi$ as pictured in equation
(1.14). The action $I_{a \to -a}(N)$ has saddles at $N=(2n+1)\pi$ and poles at $N=2n\pi$, as shown in equation
(1.13).

#### [standard-sector] section: Standard sector
##### [standard-sector-p1] paragraph

Figure 1 pictures $I_{a \to a}(N)$ for complex $N$ including saddles and steepest descent lines. In this case,
the most natural integration contour is the Lorentzian contour $N=\i \mathbb{R}$.

##### [fig-plot_minus_sol_N_plane] figure: Figure 2

Figure 2. Complex $N$ plane for $I_{a_\text{max} \to -a_\text{max}}(N)$ in (2.34). Singularities in the action
are red $\cross$’s and saddles are black dots. Steepest descent (ascent) curves are black solid (dashed)
lines. The Lorentzian $N=\varepsilon+\i\mathbb{R}$ contour is drawn vertically in magenta and the absolutely
convergent contour that it is deformed into is drawn in orange. Here $G$ was slightly complexified to make the
ascent/descent lines non-degenerate. The degenerate real $G$ version is shown in figure 3.

##### [fig-plot_minus_degenerate] figure: Figure 3

Figure 3. Complex $N$ plane for $I_{a_\text{max} \to -a_\text{max}}(N)$ in (2.34), with $q=0.1$ and real $G$.
A slightly complexified $G$ results in figure 2. The defining contour deforms to the orange contour dominated
by $k=1$, as expected.

##### [standard-sector-p2] paragraph

For this contour, the saddle points contribute if $N\leq 0$. The dominant one $N=0$ has $I=0$. The other
contributing saddles ($n<0$) have:

\[ I_{a\to a}(2\pi n)=-\frac{\pi n}{G}>0\,. \]

(2.36)

These contribute negligibly to the path integral. This confirms the picture sketched in equation (1.14).

#### [tunneling-sector] section: Tunneling sector
##### [tunneling-sector-p1] paragraph

The action $I_{a\to -a}(N)$ is shown for complex $N$ in figure 2. The saddles occur at $N=(2n+1)\pi$.
Crucially, there is a singularity at $N=0$, such that there are a priori (at least) two reasonable definitions
of the Lorentzian contour: $N=\pm \varepsilon+\i \mathbb{R}$. The question of how the $N$ contour should avoid
$N=0$ was recently emphasized in [60]. For $N=-\varepsilon+\i \mathbb{R}$ one picks up $N<0$ saddles, which
are suppressed in the path integral. Crucially, however, for the contour $N=\varepsilon+\i \mathbb{R}$ one
picks up the saddle at $N=\pi$, with negative action, and thus positive entropy:

\[ \boxed{I_{a\to-a}(\pi)=-\frac{\pi}{2 G}\overset{?}{=}-S\quad q\text{-independent}\,} \]

(2.37)

This is the dominant contribution to the no-boundary amplitude (2.20), and it gives a positive entropy
prediction $S=-I$. This is our main point: a regularized version $N=\varepsilon+\i \mathbb{R}$ of the
Lorentzian contour still gives a positive entropy prediction, one that agrees with CLPW [14] when $q\to 0$.
Crucially, the pole at $N=0$ avoids the standard argument that negative action saddles could not contribute to
the Lorentzian path integral. That argument is that for real configurations, the Lorentzian action is real,
and therefore the real part of the Euclidean action vanishes. Because the integration contour could only “slip
down” to lower values of $\abs{e^{-I}}$, this would usually forbid picking up saddles with $\text{Re}\,I<0$.
The $i\varepsilon$ prescription around this $N=0$ singularity avoids this argument. See also section 2.5. Note
further that $N=+\varepsilon+\i \mathbb{R}$ is the choice of regulator that results in stable matter, in the
sense of allowability [7, 6].

##### [tunneling-sector-p2] paragraph

The previous calculation was kind of a “black box”. We computed the exact propagator and took its
semiclassical limit, resulting in effective actions (2.32) and (2.34). But what actually are the spacetime
configurations $a(N,\tau)$ responsible for the actions $I_{a\to a}(N)$ and $I_{a\to -a}(N)$? The answer to
this question is kind of surprising, and less obvious than what one might expect. To orient the reader, we
first discuss the configurations responsible for these actions in the $q\to 0$ dS limit, in section 2.3. We
discuss general $q$ configurations in section 2.4.

### [sec-pure_grav_3d] section: 2.3 The pure gravity limit
#### [sec-pure_grav_3d-p1] paragraph

As claimed around (2.21) we now reproduce the actions $I_{a\to \pm a}(N)$ in equation (2.32)/(2.34) by
plugging in solutions $a(N,\tau)$ of the $a$ equations of motion (2.9), without solving the Friedmann
equations (the $N$ equations of motion) (2.5). For empty dS $q\to 0$, the $a$ equations of motion are:

\[ \begin{align*}
    \frac{\ddot a}{N^2}+a = 0\,. \tag{2.38}\end{align*} \]

The unique solution $a_+$ with boundary conditions $a_0=a_1=a_\text{max}=1$ (see equation (2.8) for
$a_\text{max}$) is:

\[ \begin{align*}
    a_+=\frac{\cos(N/2-N\tau)}{\cos(N/2)}\,. \tag{2.39}\end{align*} \]

Furthermore, the solution $a_-$ with boundary conditions $a_0=-a_1=a_\text{max}=1$ is:

\[ \begin{align*}
    a_-=\frac{\sin(N/2-N\tau)}{\sin(N/2)}\,. \tag{2.40}\end{align*} \]

Plugging these into the Einstein-Hilbert action (2.4) one obtains:

\[ \begin{align*}
    \boxed{GI_{a_\text{max}\to a_\text{max}}(N)=-\frac{N}{2}+\tan(N/2) \,,\quad GI_{a_\text{max}\to
-a_\text{max}}(N)=-\frac{N}{2}-\cot(N/2)\,}  \tag{2.41}\end{align*} \]

These reproduce $I_{a\to \pm a}(N)$ in equation (2.32)/(2.34) found by taking a semiclassical limit in the
exact propagator.

#### [sec-pure_grav_3d-p2] paragraph

We would now like to understand the meaning of the configurations $a_\pm$ for general $N$. Solutions of the
$a$ equations of motion (2.38) which do not solve the $N$ equations of motion describe the motion of the
universe in a quadratic potential:

\[ 2V(a)=-1+a^2\,, \]

(2.42)

with nonzero energy $E\neq 0$. Indeed, the $N$ equations of motion constrain $E=0$, with $E=p^2/2+V(a)$. Given
the trajectory that $a$ covers for $0\leq \tau\leq 1$, we obtain the following convenient relation between the
energy $E$ and the elapsed time $N$:

\[ N=\int\frac{\d a}{\sqrt{2 E-2V(a)}}. \]

(2.43)

One derives this by studying the action (2.4) using $(a,p)$ first order variables at fixed energy and writing
the symplectic form term as $p\,\d a=\sqrt{2 E-2 V(a)}\,\d a$. Variation with $E$ reproduces the above
equation.

#### [sec-pure_grav_3d-p3] paragraph

We call the solutions $a_+$ standard solutions and $a_-$ tunneling solutions, for reasons that will become
clear in section 2.4.

#### [standard-solutions] section: Standard solutions
##### [standard-solutions-p1] paragraph

Consider first the configurations $a_+$ in (2.39). We discuss the evolution of this universe for $0<N<2\pi$.
We will be rather pedantic, as the structure of the configurations $a_\pm$ as a function of $N$ largely
survives for $q>0$ (with one important modification regarding the behavior as $a\to0$, see section 2.4). At
$N=0$ the universe is static: $a=1$. Otherwise, there are two regimes:

$0<N<\pi$ The universe starts at $a=1$. The size of the universe increases until a maximal value
$a_\text{largest}=1/\cos(N/2)$. From there, the universe shrinks again until $a=1$. The energy $E$ increases
monotonically $\d E/\d N>0$ with $E(0)=0$ and $E(\pi)=\infty$. Configurations with infinite energy are solely
responsible for singularities (poles) in the gravitational effective action $I(N)$ for $N\to N_\text{sing}$:

\[ GI_{a_\text{max}\to \pm a_\text{max}}(N)\to -\frac{2}{N-N_\text{sing}}\to E(N_\text{sing})=+\infty\,. \]

(2.44)
This evolution of the universe is described by a particle that goes up the potential $V(a)$ (trajectory
${\color{blue}1}$) before rolling back (trajectory ${\color{blue}2}$):

\[ \class{l2mpic-15}{\rule[-3.4345em]{19.2388em}{7.2975em}} \]

(2.45)
The Euclidean geometry is one sphere of radius $a_\text{largest}$, cut off at two longitudes where
$\abs{a_+}=1$:

\[ \class{l2mpic-16}{\rule[-4.2533em]{13.4024em}{8.9351em}} \]

(2.46)

$\pi<N<2\pi$ The universe starts at $a=1$, and shrinks until $a=0$. Crucially, it then passes into the region
$a<0$ (this observation will have important implications for $q>0$ in section 2.4). The size of the universe
increases in absolute value, until $a=-\abs{1/\cos(N/2)}$. Then the universe starts shrinking again. It passes
through $a=0$, and grows until it reaches $a=1$. This evolution of the universe in the quadratic potential
$V(a)$ looks like a particle that makes almost a complete orbit:

\[ \class{l2mpic-17}{\rule[-3.8784em]{19.9879em}{8.1854em}} \]

(2.47)
The Euclidean geometry is three spheres of size $a_\text{largest}$, cut off at two longitudes where
$\abs{a_+}=1$:

\[ \class{l2mpic-18}{\rule[-4.2985em]{18.2911em}{9.0256em}} \]

(2.48)
In this regime, energy decreases monotonically $\d E/\d N<0$, from $E(\pi)=\infty$ until $E(2\pi)=0$. At
$N=2\pi$, one finds a gravitational saddle (2.17) that describes two copies of the Euclidean sphere.

We stress that the single Euclidean sphere (with action $I=-A/4 G$) does not arise in this $a\to a$ sector.
Crucially, the single sphere does arise as a solution in the $a\to -a$ sector (2.40), which we discuss next.

#### [tunneling-solutions] section: Tunneling solutions
##### [tunneling-solutions-p1] paragraph

Consider the configurations $a_-$ given in equation (2.40). We describe the evolution of $a_-$ for $0\leq
N<2\pi$.

$0<N<\pi$ The universe starts at $a=a_\text{max}=1$ and shrinks, until it crunches: $a=0$. Afterwards, the
universe is described by $a<0$ and the size grows in absolute value until $a=-a_\text{max}=-1$. In this
sector, crucially the solution $N=0$ requires infinite energy: $E(0)=\infty$. Indeed, we force the particle in
the quadratic potential (representing the universe’s size) to travel a nonzero distance $2a_\text{max}$ in no
time. A basic mechanics fact is that this requires an infinite energy. In terms of $V(a)$, the particle
travels in a straight line from $a\to -a$:

\[ \class{l2mpic-19}{\rule[-3.4345em]{17.3266em}{7.2975em}} \]

(2.49)
The Euclidean solution consists of two hemispheres touching at the poles, cut at longitudes where
$\abs{a_-}=1$:

\[ \class{l2mpic-20}{\rule[-3.4917em]{13.1259em}{7.4120em}} \]

(2.50)
Energy decreases monotonically $\d E/\d N<0$ until we reach a gravitational saddle $N=\pi$. As we have shown
in section 2.2, using the contour $N=\varepsilon+\i \mathbb{R}$, this saddle dominates the gravitational path
integral and leads to an action consistent with an entropic interpretation according to CLPW:

\[ I=-\frac{\pi}{2 G}=-\frac{A}{4 G}\,. \]

(2.51)

$\pi<N<2\pi$ In this sector the universe overshoots. It first grows until $a=1/\sin(N/2)$, then travels all
the way to $a=-1/\sin(N/2)$ (passing through $a=0$) before bouncing back to $a=-a_\text{max}=-1$:

\[ \class{l2mpic-21}{\rule[-3.5724em]{19.2388em}{7.5733em}} \]

(2.52)
The energy grows monotonically in this domain: $\d E/\d N>0$. The singular configuration $N=2\pi$ corresponds
to a completely closed orbit in $a$ space, see equation (2.43). One indeed finds that:

\[ N_\text{orbit}=\oint \frac{\d a}{\sqrt{2 E-2V(a)}}=2\pi\,. \]

(2.53)
One way to compute this is by contour deformation, picking up the pole at $a\to\infty$. This will be useful in
section 2.5.

##### [tunneling-solutions-p2] paragraph

We remark that from the point of view of a particle moving in a quadratic potential $V(a)$, combining
equations (2.45)/(2.47)/(2.49)/(2.52), we conclude that it is certainly not true that all trajectories from
$a_\text{max}\to\pm a_\text{max}$ contribute in the exact quantum propagator. For instance, take a trajectory
in equation (2.52) without an overshoot in the $a<0$ part. Such a trajectory apparently does not contribute in
the gravitational path integral. This conclusion persists for $q>0$ (see section 2.4). In 4d and 5d in section
4 and section 3, where we will not have the exact quantum propagator at our disposal, we shall use this output
from the 3d analysis as (a proposed) input on which topological sectors of solutions to consider.

##### [tunneling-solutions-p3] paragraph

This concludes our discussion of the gravitational configurations responsible for the action $I_{a\to \pm
a}(N)$ in equation (2.32)/(2.34) for empty dS ($q\to 0$). This is part of the process of learning which
solutions to count in the gravitational path integral. We now consider $q>0$.

### [sect2.4necklasesemi] section: 2.4 Resolution 2: Semiclassical necklace analysis
#### [sect2.4necklasesemi-p1] paragraph

The goal of this subsection is to generalize the analysis of section 2.3 to $0<q<1$, and identify precisely
which configurations are responsible for the effective actions $I_{a\to a}(N)$ and $I_{a\to -a}(N)$ which we
obtained from the exact quantum propagators in section 2.2. Recall the $a$ equations of motion (2.9):

\[ \frac{1}{N^2}\ddot{a}+a-\frac{q^2}{4}\frac{1}{a^3}=0\,. \]

(2.54)

The generalization of the $a_+$ dS solution (2.39) is:

\[ a_+^2=\sqrt{c_+ ^2+\frac{q^2}{4}}+c_+\cos(2N(\tau-1/2))\,,\quad \sin^2(N)c_+ =-a_0^2\cos(N)+ \sqrt{a_0^4-\frac{q^2}{4}\sin^2(N)}\,. \]

(2.55)

The naive generalization of the $a_-$ dS solution (2.40) is:

\[ a_-^2=\sqrt{c_- ^2+\frac{q^2}{4}}+c_-\cos(2N(\tau-1/2))\,,\quad \sin^2(N)c_- =-a_0^2\cos(N)- \sqrt{a_0^4-\frac{q^2}{4}\sin^2(N)}\,. \]

(2.56)

Both naively satisfy boundary conditions $a_0=a_1$. Indeed, unlike the dS solution (2.40), when $0<q<1$ the
solution $a_-$ in equation (2.56) has constant sign when $0\leq\tau\leq 1$:

\[ a_-^2>0\,,\quad 0\leq \tau\leq 1\,. \]

(2.57)

Eventually, we will nonetheless identify $a_-$ as representing the configurations with boundary conditions
$a_0=-a_1=a$ responsible for $I_{a\to -a}(N)$. This identification will require a modification of the $\tau$
contour. For now, we consider the solutions (2.55)/(2.56) with $0\leq \tau\leq 1$. Notice that for $q\to 0$,
they reduce to their dS counterparts (2.39)/(2.40). The action (2.4) reduces using the $a$ equation of motion
to:

\[ G I_{\pm}=-\frac{N}{2}+N \frac{q^2}{4}\int_0^1\frac{\d\tau}{a_\pm^2}-\frac{1}{2 N}a_\pm\dot{a_\pm}\rvert_{\tau=0}^{\tau=1}\,. \]

(2.58)

#### [standard-solutions-2] section: Standard solutions
##### [standard-solutions-2-p1] paragraph

Plugging in (2.55) one obtains (we changed notation $a_0\to a$), for $-\pi<N<\pi$17

\[ G I_+(N) = -\frac{N}{2} -\frac{a^2}{\tan(N)} +\frac{a^2}{\sin (N)} \sqrt{1- \frac{q^2}{4}\frac{\sin^2 (N)}{ a^4} }+ \frac{q}{2}\arcsin \bigg( \frac{q}{2}\frac{\sin(N)}{a^2}\bigg)=G I_{a\to a}(N)\,. \]

(2.60)

Comparing with (2.32), this matches the action that follows from the exact propagator with boundary conditions
$a_0=a_1=a$. So, $a_+$ is the configuration contributing to this propagator. A classical saddle of this action
is $N=2\pi$.

#### [tunneling-solutions-2] section: Tunneling solutions
##### [tunneling-solutions-2-p1] paragraph

What about the $a_-$ solution? The on-shell action becomes

\[ \begin{align*}
    G I_-(N) &= -\frac{N}{2} -\frac{a^2}{\tan(N)} -\frac{a^2}{\sin (N)} \sqrt{1- \frac{q^2}{4}\frac{\sin^2
(N)}{ a^4} }- \frac{q}{2}\arcsin \bigg( \frac{q}{2}\frac{\sin(N)}{a^2}\bigg)+\frac{\pi q}{2}\\
    &=GI_{a\to -a}(N)+\frac{\pi q}{2}\,. \tag{2.61}\end{align*} \]

This action differs significantly from $I_{a\to a}(N)$. So, despite satisfying boundary conditions
$a_0=a_1=a$, the solution $a_-$ does not contribute to the propagator $\mathcal{G}_N(a\rvert a)$. Instead, we
observe that (in analogy with its dS counterpart (2.40)) the solution almost reproduces the action $I_{a\to
-a}(N)$, corresponding to boundary conditions $a_0=-a_1=a$. There are two issues with such an identification.
Firstly, the solution $a_-$ must become negative along $0\leq \tau\leq 1$. Secondly, the actions differ by a
constant addition $\pi q/2$. We now solve both issues simultaneously.

##### [tunneling-solutions-2-p2] paragraph

Consider the solution $a_-$ along the contour $\tau=1/2+\i T$. This is a crunching Lorentzian spacetime with a
Milne-type singularity $a_-=0$ at $T=T_\text{sing}$. It seems logical that to pass from $a_->0$ to $a_-<0$ (in
order to respect boundary conditions $a_0=-a_1=a$), one should somehow pass by this singularity. The right
procedure is to consider the solution $a_-$ in equation (2.56) along a $\tau$ contour that winds once around
the big-crunch singularity:

\[ \class{l2mpic-22}{\rule[-4.1136em]{10.2565em}{8.6558em}} \]

(2.62)

An instructive example of this configuration is the classical saddle of the action $I_-(N)$ (at $N=\pi$) with
boundary conditions $a^2=a_\text{max}^2$. Solving for $c_-$ in equation (2.56) one recovers the classical
solution (2.6):

\[ a_-^2=\frac{1}{2}+\frac{\sqrt{1-q^2}}{2}\cos(2\pi\tau)\,. \]

(2.63)

Along the contour $\tau=1/2+\i T$ one now finds the following big-bang big-crunch Lorentzian spacetime:

\[ a_-^2=\frac{1}{2}-\frac{\sqrt{1-q^2}}{2}\cosh(2\pi T)\qquad \class{l2mpic-23}{\rule[-3.2758em]{7.0133em}{6.9803em}} \]

(2.64)

The location of the singularities is

\[ T_\text{sing}=\frac{1}{2\pi}\text{arccosh}\left(\frac{1}{\sqrt{1-q^2}}\right)\,. \]

(2.65)

Crucially, expanding around $T\to T_\text{sing}$ gives $a_-(T) \sim (T-T_\text{sing})^{1/2}$. Hence, we see
that, going around the singularity once as instructed by the $\tau$ contour in equation (2.62), $a_-$ acquires
an additional phase: $a_-\to e^{\i \pi} a_-$. This proves that along the contour (2.62), $a_-$ is indeed a
solution with boundary conditions $a_0=-a_1=a$.

##### [tunneling-solutions-2-p3] paragraph

Crucially, the on-shell gravitational action $I_-$ (2.58) receives a nontrivial extra contribution due to
winding around the singularity. Using equation (2.56), somewhat miraculously one finds:

\[ GI_-(N)\to G I_-(N)+ N\frac{q^2}{4}\oint_{a_-=0}\frac{\d \tau}{a_-^2} =G I_-(N)-\frac{\pi q}{2}=GI_{a\to -a}(N)\,. \]

(2.66)

This is the main result of this section: the solution $a_-$ (2.56) along a bra-ket wormhole contour (2.62)
satisfies boundary conditions $a_0=-a_1=a$ and is responsible for the exact propagator $\mathcal{G}_N(a\rvert
-a)$. An important point was that there was a contribution from winding around the singularity in the complex
$a$ plane. As explained in section 2.2, a steepest descent analysis now reveals that the dominant contribution
to the gravitational path integral is the solution $a_-$ (with $N=\pi$).

##### [tunneling-solutions-2-p4] paragraph

We stress that this Lorentzian detour, and the associated correction (2.66) to the action, is essential to
obtain a $q$-independent on-shell action (2.37). We discuss the puzzling $q$-independence of the entropy in
more detail in section 2.6. The $a\to a$ sector with action $I_{a\to a}(N)$ should be interpreted in a similar
manner: like the empty dS solution (2.47), the solutions with $N=2\pi n$ crosses $a=0$ a total $2n$ times.
This gives the $q$-independent necklace action (2.36).

##### [tunneling-solutions-2-p5] paragraph

We remark that the action is unique provided $I_{a_1\to a_2}(N\in \i \mathbb{R})\in \i\mathbb{R}$ for
configurations $a_1,a_2$ associated with Lorentzian solutions. In particular, one could not simply add terms
like $\pi q/2$ to the action for all $N$. This makes for instance equation (2.34) robust, and thus also our
key (but confusing) result (2.68) below.

#### [dominant-solution] section: Dominant solution
##### [dominant-solution-p1] paragraph

This dominant solution looks as follows:

\[ \class{l2mpic-24}{\rule[-3.6968em]{31.2431em}{7.8222em}} \]

(2.67)

In the dS limit the Lorentzian region shrinks away to a point, resulting in the usual sphere amplitude. If the
no-boundary path integral computes an entropy, as suggested by [38, 39], that entropy would be the on-shell
action associated with this geometry:

\[ \boxed{S=\frac{\pi}{2 G}\,} \]

(2.68)

This is a clear target for Lorentzian algebraic calculations.

##### [dominant-solution-p2] paragraph

We started out in section 2.2 with describing the universe as a quantum mechanical particle traveling in a
potential $V(a)$ (2.11):

\[ 2V(a)=-1+a^2+\frac{q^2}{4}\frac{1}{a^2}\,. \]

(2.69)

The generalization of the dS motion of the particle in the potential, discussed in equation (2.49), is the
following motion:

\[ \class{l2mpic-25}{\rule[-3.4345em]{15.5491em}{7.2975em}} \]

(2.70)

From this perspective, the Lorentzian bra-ket wormhole piece of the geometries is viewed as a tunneling
solution. Because we started from Euclidean signature, the tunneling process is in Lorentzian signature, the
opposite of what happens usually. Other off-shell values of $N$ correspond to configurations $a_-$ in equation
(2.56) which describe the motion of the particle higher up in the potential, analogous to what happened in
empty dS, see equation (2.49). The $q\to 0$ pure dS limit is similar to the operator insertion limit of [80]
(see also [81]).

##### [dominant-solution-p3] paragraph

We briefly reiterate the logic. We studied the exact quantum propagator, and used this to identify which
classical configurations $a_+$ and $a_-$ contribute to respectively the propagators $\mathcal{G}_N(a\rvert a)$
and $\mathcal{G}_N(a\rvert -a)$. The remainder of this work concerns generalizations where we do not have
access to exact quantum propagators, but where instead we assume these same “topological sectors” of solutions
are responsible for $\mathcal{G}_N(a\rvert a)$ and $\mathcal{G}_N(a\rvert -a)$.

### [subsect2.5.4gen] section: 2.5 General argument
#### [subsect2.5.4gen-p1] paragraph

Consider the regime $N\to 0$ for the Euclidean action (2.4) describing propagation in a generic potential:

\[ I=\frac{1}{\text{G}}\int_0^1\d \tau \bigg\{ -\frac{1}{2N}\dot{a}^2+N V(a) \bigg\}\,. \]

(2.71)

The $N\to 0$ approximation is to drop the potential term when computing $\mathcal{G}_N(a_1\rvert a_2)$, as a
particle needs very high kinetic energy to travel from $a_1\to a_2$ in almost zero time $N$. The solution is
$a=a_1+(a_2-a_1) \tau$, leading to the leading order $N\to 0$ approximation generalizing equation (2.29):

\[ \boxed{\mathcal{G}_N(a_1\rvert a_2)\,\to\, e^{\frac{1}{2 N \text{G}}(a_1-a_2)^2}\,} \]

(2.72)

For $\mathcal{G}_N(a\rvert a)$ the action vanishes and indeed we did not observe a singularity at $N=0$,
rather the action develops a classical saddle (the particle not moving). Crucially, for $\mathcal{G}_N(a\rvert
-a)$, this action does develop an $N\to 0$ singularity, as shown in equation (2.72).

#### [subsect2.5.4gen-p2] paragraph

More generally, consider any FLRW potential of the form (2.11), with quadratic asymptotics. Two ingredients
survive from the 3d analysis. First, the zero-energy bounce has some period $N_0$, and gluing $k$ bounces
produces necklace saddles at $N=kN_0$, with odd $k$ describing the $a\to-a$ sector and even $k$ the $a\to a$
sector. The former can be viewed as tunneling through $a=0$. Secondly, the actions $I_{a\to\pm a}(N)$ are real
on the real $N$ axis and the $N=0$ pole (2.72) is there in the $a\to -a$ sector only. The segment $(0,N_0)$ of
the real axis is a steepest ascent line of the $k=1$ saddle. This crosses the contour
$N=\varepsilon+\i\mathbb{R}$. Picard-Lefschetz therefore guarantees that it contributes to the path
integral.18

#### [walls] section: Walls
##### [walls-p1] paragraph

The more difficult part is proving that the higher necklaces ($k\geq 2$) will not contribute. In other words,
ascent lines from $k\geq 2$ may not cross $N=\varepsilon+\i\mathbb{R}$. For the analytically solvable axion
model one can understand this analytically. Consider the actions (2.32)/(2.34). We focus on
$I_{a_\text{max}\to -a_\text{max}}(N)$. Define the height function

\[ H(N)=-\text{Re}\,I_{a_\text{max}\to -a_\text{max}}(N)\,. \]

(2.73)

Ascent lines $\mathcal{A}_k$ follow lines of constant $\text{Im}\,I_{a_\text{max}\to -a_\text{max}}(N)$, start
at $N=k N_0$, and have monotonically increasing height functions (they are ascending). Therefore (recalling
that saddles have odd $k=2m+1$):

\[ H(\mathcal{A}_{2m+1})>(2m+1) \abs{I_0}\,. \]

(2.74)

The function $I_{a_\text{max}\to -a_\text{max}}(N)$ given in equation (2.34) has a remarkable property. The
height function $H(N)$ is constant on lines above and below the singularities $N=2m N_0$:

\[ H(2m N_0+\i \mathbb{R})=2m \abs{I_0}\,. \]

(2.75)

Combined with equation (2.74), we see that the ascent line of the saddle at $N=(2m+1)N_0$ is confined to the
region $\text{Re}\, N>2m N_0$:

\[ \text{Re}\,\mathcal{A}_{2m+1}>2 m N_0\,. \]

(2.76)

Therefore the ascent line does not intersect the defining contour $\mathcal{A}_{2m+1} \cap \varepsilon+\i
\mathbb{R}=\varnothing$. This demonstrates analytically that the higher necklaces $k\geq 2$ indeed do not
contribute.

### [sect-3.3] section: 2.6 Area law universality
#### [sect-3.3-p1] paragraph

In equation (2.37), we found that the dominant saddle $k=1$ gives an entropy independent of the axion flux
parameter $q$ equal to the empty dS entropy (2.37). This might be interpreted as one version of the cosmic no-
hair theorem, as we explain next.

#### [sect-3.3-p2] paragraph

The contour used in (2.62) to evaluate the on-shell action may be deformed in the following manner:

\[ \class{l2mpic-26}{\rule[-5.2337em]{9.1531em}{10.8961em}} \]

(2.77)

This contour is labeled by a large Lorentzian time $T\to \infty$. We study the contribution from the $N=\pi$
GH saddle along this contour in the case $a_1 = -a_2 = a_\text{max}$ (2.8). The solution for complex $\tau$
reads:

\[ a^2(\tau) = \frac{1}{2} + \frac{\sqrt{1-q^2}}{2} \cos(2\pi\tau). \]

(2.78)

The two Lorentzian contributions $\tau=0\to \i T$ and $\tau=1+\i T\to 1$ exactly cancel. What remains is the
late time contour $\tau = \i T + \theta/\pi$

\[ a(\theta)\to a_T\,e^{-\i \theta}\,,\quad 0\leq \theta\leq \pi\,,\quad a_T=\frac{(1-q^2)^{1/4}}{2} e^{\pi T}\,. \]

(2.79)

Shifting $T\to T+c$ this becomes the $q$-independent pure dS solution, as demanded by the cosmic no-hair
theorem [82, 10, 83]. Since $T\to T+c$ is an analytic contour deformation, the value of the action does not
change. $T\to T+c$ absorbs the $q$-dependence in $a_T$, so the on-shell action is $q$-independent. Explicitly,
substituting (2.79) into the $d=3$ action (2.4):

\[ \begin{split}
    G I_{a\to -a}(2\pi) &= \int_0^\pi d\theta \left\{-\frac{a_\theta^2}{2} +
\frac{1}{2}\left(-1+a^2+\frac{q^2}{4 a^2}\right)\right\}\\
    &= \int_0^\pi d\theta \frac{(1-q^2)\sinh^2(2\pi T - 2i \theta)}{2+2\sqrt{1-q^2} \cosh(2\pi T-2i \theta)}\\
    & \to  \int_0^\pi d\theta \  \left\{a_T^2 e^{- 2i \theta} -\frac{1}{2}\right\}= -\frac{\pi}{2}.
\end{split} \]

(2.80)

The integral on the second line is exact and gives $\pi/2$. The one on the last line takes the large $T$ limit
and follows from the dS potential $q=0$.

#### [sect-3.3-p3] paragraph

We find the independence of this result on $q$ to be puzzling. However, at least in 3d, this conclusion
appears difficult to avoid, despite attempts, and so we may need to reckon with the physical implications.

## [sect3-5daxion] section: 3 Higher dimensional axion necklaces
### [sect3-5daxion-p1] paragraph

In this section, we will provide further evidence for the generality of our claim. We investigate higher-
dimensional axion wormholes numerically. Within minisuperspace, we show that the Lorentzian lapse contour
$N=\varepsilon+\i \mathbb{R}$ picks up the GH saddle as the dominating contribution.

### [sect3-5daxion-p2] paragraph

In section 3.1 we set up the minisuperspace necklace problem in (what we will call) kinetic gauge. In this
gauge, the scale factor has a standard kinetic term, and the action possesses $a\mapsto -a$ symmetry. As in
the 3d analysis, the quantum gravity propagator follows from the $a(\tau)$ path integral upon gauging this
symmetry. Unlike in 3d (section 2.2) we do not know the exact analytic propagator. Instead, we rely on the
semiclassical lessons of section 2.4 as a guide for which trajectories $a(\tau)$ to investigate. The
associated action $I(N)$ is studied numerically in 4d and 5d, in section 3.2. In appendix A, we present an
alternative analytic and numerical analysis in (what we call) proper-time gauge for 5d.

### [sect3.2kinetic] section: 3.1 Setup
#### [sect3.2kinetic-p1] paragraph

Following section 2.1, we consider an axion flux coupled to $\Lambda>0$ gravity. The Euclidean action reads:

\[ I = \int \d^d x \sqrt{g} \bigg\{-\frac{1}{16\pi G}\left(R-2\Lambda\right) + \frac{1}{(d-1)!} H^{ij\cdots}H_{ij\cdots}\bigg\}\,. \]

(3.1)

Here $H_{ij\cdots} = Q \cdot \text{vol}$ is a $(d-1)$-form field strength and $\text{vol}$ is the
$(d-1)$-sphere volume form. For the metric, we will use minisuperspace FLRW with the non-standard kinetic
gauge:

\[ \d s^2=N^2 a(\tau)^{2(d-3)}\d \tau^2+a(\tau)^2\d \Omega_{d-1}^2\,,\quad 0\leq \tau \leq 1\,. \]

(3.2)

The purpose of this gauge is that the Euclidean action (3.1) (with $H=1$) has an ordinary kinetic term.
Indeed, following the conventions of [75]:

\[ \Lambda = \frac{(d-1)(d-2)}{2}H^2\,,\quad Q^2 = \frac{d-2}{16\pi G} \left( \frac{d-2}{d-1} H^{-2}\right)^{d-2} q^2\,,\quad 0\le q \le 1\,, \]

(3.3)

the Euclidean action has a standard $\dot{a}^2$ kinetic term:

\[ \boxed{I = \frac{\Omega_{d-1}(d-1)(d-2)}{8\pi G}\int_0^1 \d\tau\, \bigg\{-\frac{\dot a^2}{2N} +\frac{N}{2}\bigg(-a^{2d-6}+a^{2d-4} + \frac{1}{d-1}\left(\frac{d-2}{d-1}\right)^{d-2} \frac{q^2}{a^2} \bigg)\bigg\}\,} \]

(3.4)

#### [sect3.2kinetic-p2] paragraph

This action shares key properties with our $d=3$ case. First, since the kinetic term is standard, we can set
up a similar well-posed quantum mechanical system, which will reproduce a sensible propagator
$\mathcal{G}_N(a_1|a_2)$ for $a(\tau)$. Secondly, $a\mapsto -a$ is again a symmetry of the action, so we can
gauge it, leading to the same two sectors as in 3d. Thirdly, due to the last term in (3.4), the big-bang
solution behaves as $a(t) \sim t^{1/2}$ for any $d$. For this reason, we expect that a contour similar to
(2.62) will again map positive to negative $a$. Therefore, the saddles that contribute to each sector follow
the same structure as in 3d.

#### [sect3.2kinetic-p3] paragraph

In any dimension, the classical equations of (3.4) describe a particle in a potential. Below we study this
action numerically for 4d and 5d where the potential equals:

\[ \begin{split}
        2V_\text{4d}(a) &= -a^2+a^4+\frac{4}{27} \frac{q^2}{a^2},\\
        2V_\text{5d}(a) &= -a^4+a^6+\frac{27}{256}\frac{q^2}{a^2}.
    \end{split} \]

(3.5)

In both cases, this potential allows for periodic solutions with zero energy. These solutions are exactly the
higher-dimensional analogs of the necklaces we found in the previous section. Working for general lapse
$N$/energy, just as in 3d, we can find semiclassical solutions for $a(\tau)$. In the $a\to a$ sector
(analogous to equation (2.45) for 3d) the solution would be:

\[ \class{l2mpic-27}{\rule[-3.4585em]{19.2388em}{7.3456em}} \]

(3.6)

The tunneling solution $a\to -a$ similarly generalizes the 3d tunneling solution shown in equation (2.70):

\[ \class{l2mpic-28}{\rule[-3.4585em]{17.7872em}{7.3456em}} \]

(3.7)

In the next section 3.2 we present the numerical evaluation of the semiclassical actions $I_{a_\text{max}\to
\pm a_\text{max}}(N)$. Picard-Lefschetz reveals that a Lorentzian lapse contour $N=\varepsilon+\i \mathbb{R}$
will pick up the GH saddle as the dominating contribution. The $q=0$ dS case may be studied partially
analytically. See equation (4.16).

#### [on-shell-action] section: On-shell action
##### [on-shell-action-p1] paragraph

Our approach in this section is to assume that the solutions are given by the ordinary necklace solutions, as
can also be obtained without a minisuperspace approximation, plus the tunneling piece (or several of these for
higher necklaces). In the tunneling piece, the Lorentzian parts cancel and we are left with the contribution
around $a=0$. In kinetic gauge, this is a pole in any dimension and we can calculate its contribution. Indeed,
around $a \approx 0$, only the $1/a^2$ term in the potential is important, leading to a solution $a(\tau) =
(-4N^2 q^2 x)^{1/4}\sqrt{\tau}$ where we denote the coefficient in the action
$x=\frac{1}{d-1}\left(\frac{d-2}{d-1}\right)^{d-2}$. Therefore for small $a$ (meaning also small $\tau$),
plugging back into the action, we see that the action behaves as $\frac{\Omega_{d-1}(d-1)(d-2)}{8\pi G} \int
d\tau \frac{iq\sqrt{x}}{2\tau}$, and so the pole contribution to the entropy is

\[ S_{\text{pole}}=\frac{\Omega_{d-1}(d-1)(d-2)}{8\pi G} \pi q \, \sqrt{\frac{1}{d-1}\left(\frac{d-2}{d-1}\right)^{d-2}} . \]

(3.8)

For $d=3$ this is indeed $\frac{\pi q}{2G}$.

##### [on-shell-action-p2] paragraph

On the other hand, for pure de Sitter in Euclidean signature, the on-shell action for a single sphere is just

\[ I_{\text{sphere}} = -\frac{1}{4\pi G(d-2)} \int d^dx \sqrt{g} \, \Lambda = -\frac{\Omega_d (d-1)}{8\pi G} \]

(3.9)

where in the second equality we used $H=1$ units.

##### [on-shell-action-p3] paragraph

The Einstein static universe case is the value of $q$ for which there is a minimum of the potential at $V=0$,
and this happens at any dimension at $q=1$ in these conventions (and the size of the universe is
$a_0=\sqrt{\frac{d-2}{d-1}}$ in this case). At this value, the Euclidean solution has vanishing action (since
it is stationary and the potential is zero). Therefore the only contribution of the tunneling solution is from
the pole (3.8). We notice that at $d=3$ this value is equal to the entropy of the sphere $S=-I$ from (3.9)
(for $q=0$ there is no contribution from the $a=0$ pole), but at $d>3$ we have $S_{q=1}=S_{\text{pole}}(q=1) >
S_{\text{sphere}}$ which would contradict the second law of thermodynamics.

##### [on-shell-action-p4] paragraph

We emphasize that only at $d=3$ we have really shown that the tunneling solution is what governs the quantum
mechanics. It may well be that this is not the case for generic $d$. In particular, the pole contribution is
linear in $q$ for any $d$, whereas the necklace action is linear in $d=3$ but not for general $d$, which would
mean that the total action of the tunneling solution is $q$ independent only for $d=3$ but not for higher $d$.
If the tunneling solution is not the right answer in higher dimensions, that would invalidate this conclusion.
It would also avoid the violation of the second law discussed above. At $d=3$ where we know the tunneling
solution is correct, there is no such violation. See section 2.6 for more discussion.

### [sect3.3kineticnum] section: 3.2 Numerical analysis
#### [fig-np33check3d] figure: Figure 4

Figure 4. Numerical simulations of the 3d action $I_{a_\text{max}\to \pm a_\text{max}}(N)$ show excellent
agreement with plots of the analytically obtained on-shell actions (figure 1 and figure 2). This supports
higher dimensional numerics. Here $G$ was slightly complexified to make the ascent/descent lines non-
degenerate.

#### [sect3.3kineticnum-p1] paragraph

To implement numerically, we solve the $a$ equations of motion as a boundary value problem for general complex
lapse $N$ using the shooting method. The action is then evaluated on this solution for each $N$.

#### [sect3.3kineticnum-p2] paragraph

Before tackling 4d/5d, we test the procedure in 3d, where we can check against the analytic solution of
section 2. In figure 4, the $N$ plane for the $a_-$ solution is shown, to be compared with figure 2.19 The
singularity for $N\to 0$ is clear. There is a saddle point on the positive real $N$ axis with steepest ascent
line crossing the defining integration contour. More generally, one finds good agreement with analytics,
though there are some numerical artifacts. The most significant is that the numerical analysis, in some
places, picks up the wrong solution. This issue persists in 4d/5d. However, fortunately, the branch cuts and
associated choices of solutions only cloud things (relatively) far away from the origin $N\to 0$.

#### [sect3.3kineticnum-p3] paragraph

Consider the height function $H(N)$ defined in section 2.5. There are several solutions for fixed $N$, so the
action $I(N)$ has many sheets and many branch cuts. This complicates following either the lines of constant
height $H(N)= 2m \abs{I_0}$ or the ascent lines $\mathcal{A}_{2m+1}$. We found that one can numerically track
individual ascent lines $\mathcal{A}_{2m+1}$, even as they cross sheets, and check whether these eventually
cross $N= \varepsilon+\i \mathbb{R}$. We did not find any higher necklaces that contribute. However, a case-
by-case numerical investigation of all ascent lines $\mathcal{A}_{2m+1}$ from all saddles is neither practical
nor fully airtight.

#### [sect3.3kineticnum-p4] paragraph

Instead, one proceeds as follows. On the defining contour $N=\varepsilon+\i \beta$ we have (away from $N\to
0$) $H(\varepsilon+\i \beta)\sim \varepsilon$, as the action is purely imaginary for purely imaginary $N$
(indeed, Lorentzian solutions), and that $I(N)$ has a Taylor expansion (away from $N\to 0$). Including the
pole $I(N\to 0)\sim 1/N$, we have (modulo a constant) $H(\varepsilon+\i\beta)\to\delta(\beta)$. Furthermore,
notice (2.74) $H(\mathcal{A}_{2m+1})>(2m+1) \abs{I_0}$, an order one number (in units of $1/G$). So,
$\mathcal{A}_{2m+1}$ could only cross the contour $N=\varepsilon+\i \mathbb{R}$ at $N=0$.

#### [fig-zerophase45] figure: Figure 5

Figure 5. Lines of real action $I(N)$ arriving at the origin for 4d/5d axion wormholes in kinetic gauge
(black). According to section 2.5 one should track when those lines reach $H(\mathcal{A}_\kappa)<2\abs{I_0}$.
The color reflects the phase.

#### [sect3.3kineticnum-p5] paragraph

Figure 5 shows the ascent lines emerging from the origin for any real saddle. Their degeneracy may be broken
by slightly complexifying $G$, however, this will not be needed for our present argument. The higher necklaces
have actions $kI_0$ with $k\geq 2$. For some ascent line $\mathcal{A}_\kappa$ to reach the origin
(contributing to the defining gravitational path integral) and to have originated from some higher necklace,
the ascent line emerging from the origin may not enter any region where $H(\mathcal{A}_\kappa)<2\abs{I_0}$
prior to reaching the saddle (otherwise descent into the saddle is impossible). We now show that any
contributing $\mathcal{A}_\kappa$ in fact does enter any region where $H(\mathcal{A}_\kappa)<2\abs{I_0}$,
prior to reaching the saddle.

#### [fig-ring] figure: Figure 6

Figure 6. Lines of constant height $H(N)$. Any ascent line ending at $N=0$ (so, contributing to the path
integral along the defining contour) necessarily crosses the $H(N)=2\abs{I_0}$ locus (purple). Thus, there are
points for every contributing ascent line $\mathcal{A}_\kappa$ where $H(\mathcal{A}_\kappa)<2\abs{I_0}$. This
proves that these ascent lines could not originate from $k\geq 2$ necklace solutions. The dashed line (black)
is some contour to which the defining contour may be deformed, along which $H(N)<2\abs{I_0}$, fundamentally
ruling out contributions from $k\geq 2$ necklaces. The color reflects the height.

#### [sect3.3kineticnum-p6] paragraph

Figure 6 shows numerically for 4d/5d axion wormholes a line with $H(N)=2\abs{I_0}$ (purple) that any
contributing $\mathcal{A}_\kappa$ must cross. This rules out contributions from $k\geq 2$ necklaces in the
gravitational path integral, thus supporting our claim that the GH saddle dominates, and concluding our
discussion.

## [sect4-magnetic] section: 4 Magnetic necklaces
### [sect4-magnetic-p1] paragraph

We again consider Euclidean FLRW metric with closed slices

\[ \begin{align*}
    \d s^2 =  \d\tau^2 + a(\tau)^2\ \d\Omega_{d-1}^2\,. \tag{4.1}\end{align*} \]

Let us recall the special characteristics of axions that enable them to support a Euclidean cosmological
wormhole/necklace [84, 85, 86, 87]. The (first and second) Friedmann equations in Euclidean signature are:20

\[ \begin{align*}
    \frac{\dot{a}^2}{a^2}  = \frac{1}{a^2} - H^2 +\frac{16\pi G }{(d-1)(d-2)}T_{\tau\tau}\,,\quad
\frac{\ddot{a}}{a} = -H^2-\frac{(d-3)}{(d-1)(d-2)}8\pi G\,T_{\tau\tau}+\frac{8\pi
G}{(d-2)}\frac{T_{\theta\theta}}{a^2}\,. \tag{4.2}\end{align*} \]

Euclidean wormholes are characterized by the existence of a throat, where $\dot{a}=0$, $\ddot{a}>0$. A
sufficiently negative energy $T_{\tau\tau}$ results in such a Euclidean cosmological wormhole. This is of
course nonstandard. For instance, a scalar $\phi$ field with an ordinary sign kinetic term and potential
$V(\phi)$ has the stress tensor:

\[ \begin{align*}
    T_{\tau\tau} = \frac{1}{2}\dot{\phi}^2-V(\phi)\,, \quad \frac{T_{\theta\theta}}{a^2} =
-\frac{1}{2}\dot{\phi}^2-V(\phi)\,.
 \tag{4.3}\end{align*} \]

The Friedmann equations (4.2) now do not allow for configurations with $\dot{a}=0$, $\ddot{a}>0$. Indeed,
imposing that $\dot{a}=0$ one finds

\[ \frac{\ddot{a}}{a} = -\frac{1}{a^2}-\frac{8\pi G}{d-2}\dot{\phi}^2<0\,. \]

(4.4)

Axions are different: they have an opposite sign kinetic term (when the action is viewed as the dual of the
$(d-1)$ form) [84]. Similarly, an imaginary massless scalar (such as timelike Liouville theory [64, 68, 69],
depending on the contour) has an opposite sign kinetic term. In this section, we will describe solutions in
Yang-Mills theory that also satisfy these criteria.21 A nice feature is that their stress energy redshifts as
$a^{-4}$ in all dimensions.

### [sect4-magnetic-p2] paragraph

Yang-Mills solution The sphere $\Omega_{d-1}$ equals the coset space:

\[ \begin{align*}
    S^{d-1} = SO(d)/SO(d-1)\,.
 \tag{4.5}\end{align*} \]

We consider $SO(d-1)$ Yang-Mills on an FLRW background (4.1). Identifying the gauge field with a spin
connection automatically solves the Yang-Mills equations on Einstein backgrounds [88, 89]. Gauge-field-
supported wormholes of this type were constructed in $d=4$ in [90, 91, 92], though our interpretation will be
different. We thus consider the following (purely magnetic) gauge field:22

\[ \begin{align*}
    A = \frac{1}{2}\omega^{ab}\, t_{ab}\,.
 \tag{4.6}\end{align*} \]

Here, $\omega^{ab}$ is the spin connection on the unit sphere and $t_{ab}$ are the generators of
$\mathfrak{so}(d-1)$. By Cartan’s structure equation and using the fact that $\Omega_{d-1}$ is maximally
symmetric, one computes:

\[ \begin{align*}
    \d A=\frac{1}{2}R^{ab}\,t_{a b} - \frac{1}{2}\omega^a_c\wedge \omega^{cb}\,t_{ab}\,,\quad R^{ab} =
\frac{1}{2}R^{ab}{}_{cd}\,e^c\wedge e^d = e^a \wedge e^b\,.
 \tag{4.7}\end{align*} \]

Using the $\mathfrak{so}(d-1)$ algebra one furthermore finds:

\[ \begin{align*}
     A \wedge A  = \frac{1}{8}\omega^{ab}\wedge \omega^{cd}\, [t_{ab},t_{cd}] = \frac{1}{2}\omega^a_c\wedge
\omega^{cb}\,t_{ab}\,.
 \tag{4.8}\end{align*} \]

Therefore one finds the simple field strength:

\[ \begin{align*}
    F = \frac{1}{2}e^a \wedge e^b\, t_{ab}.
 \tag{4.9}\end{align*} \]

The Lorentzian stress-energy tensor associated with this field strength takes the form of a perfect fluid.
Restoring $N$ dependence via $\tau\to N\tau$:

\[ \begin{align*}
    N^{-2} T_{\tau \tau} = -\frac{(d-1)(d-2)}{4g_\text{YM}^2}\frac{1}{a^4}\,, \quad T_{ii} =
\frac{(d-2)(5-d)}{4g_\text{YM}^2}\frac{1}{a^2}\,,\quad T=\frac{(4-d)(d-2)(d-1)}{4g_{YM}^2}\frac{1}{a^4}\,.
 \tag{4.10}\end{align*} \]

In 4d the field is therefore classically conformal ($T=0$), as indeed expected of 4d Yang-Mills theory.

### [sect4-magnetic-p3] paragraph

Gravitational solution In minisuperspace, this YM configuration adds a dimension-independent $1/a^2$
contribution to the potential $V(a)$, which for axions was discussed in equation (A.2):

\[ I=\frac{\Omega_{d-1}(d-1)(d-2)}{8\pi G}\int_0^1\d\tau\, a^{d-3}\bigg\{-\frac{\dot a^2}{2N}+\frac{N}{2}\bigg(-1+H^2 a^2+\frac{4\pi G}{g_\text{YM}^2}\frac{1}{a^2}\bigg)\bigg\}\,. \]

(4.11)

Crucially, the sign of the $1/a^2$ correction is identical to the sign of the axion $1/a^{2(d-2)}$ correction.
This creates a wall in the potential around $a\to 0$, and hence results in a bouncing solution. So: a
Euclidean necklace. The Friedmann equation (the $N$ equation of motion) indeed admits wormhole solutions:

\[ \frac{1}{N^2}\frac{\dot{a}^2}{a^2}  = \frac{1}{a^2} - H^2 -\frac{4\pi G}{g_\text{YM}^2}\frac{1}{a^4}\quad \to \quad a^2= \frac{1+ \sqrt{\Delta}\cos(2H N \tau)}{2 H^2}, \quad \Delta = 1- H^2 \frac{16\pi G}{g_\text{YM}^2}\,,\quad 0\leq \Delta\leq1\,. \]

(4.12)

These periodic solutions can be repeated any number of times, with classical saddles:

\[ N=\frac{\pi k}{H}\,,\quad 0\leq \tau \leq 1\,. \]

(4.13)

The action of one oscillation involves Legendre functions of the first kind, and interpolates between (minus)
the dS entropy at $\Delta=1$ and zero at $\Delta=0$:

\[ \begin{align*}
    I= \frac{1}{H^{d-4}}\frac{(d-1)\,2^{(5-d)/2}\,\pi^{(d+2)/2}\,}{\Gamma(d/2)}\frac{1}{g_\text{YM}^2}\,(1-
\Delta)^{(d-5)/4}\bigg\{P_{\frac{d-5}{2}}\bigg(\frac{1}{\sqrt{1-\Delta}}\bigg) -
P_{\frac{d-1}{2}}\bigg(\frac{1}{\sqrt{1-\Delta}}\bigg)\bigg\}\,.
 \tag{4.14}\end{align*} \]

### [sect4-magnetic-p4] paragraph

We remark finally that in kinetic gauge $N\to a^{d-3}N$, this YM contribution to $V(a)$ scales as $a^{2d-8}$.
In particular in four dimensions the YM contribution becomes simply a constant in units where $H=1$:

\[ \boxed{I_\text{4d} = \frac{3\pi}{2 G}\int_0^1 \d\tau\, \bigg\{-\frac{\dot a^2}{2N} +\frac{N}{2}\bigg(-a^{2}+a^{4} + \frac{4\pi G}{g_\text{YM}^2} \bigg)\bigg\}\,} \]

(4.15)

This case could be studied analytically. The $a$ equations of motion are solved in terms of Jacobi elliptic
tangent functions $\text{sc}(u,m)$, which are indeed (doubly) periodic functions:

\[ \frac{\ddot{a}}{N^2}-a+2a^3=0\,\quad \to \quad a =\sqrt{C^2-1}\,\mathrm{sc} \Big(C N \tau\, \Big|\, 2-\frac{1}{C^2}\Big)\,. \]

(4.16)

The special case $g_\text{YM}^2=16\pi G$ results in an Einstein static universe, where $\dot{a}=0$. This
corresponds to a particle at rest at the bottom of the quartic potential ($a_\text{rest}=1/\sqrt{2}$). The
propagators $\mathcal{G}_N(a_\text{rest}\rvert a_\text{rest})$ and $\mathcal{G}_N(a_\text{rest}\rvert
-a_\text{rest})$ are the topic of Coleman’s standard example for the study of instantons in QM [94].

### [sect4-magnetic-p5] paragraph

One may repeat the numerical analysis of section 3.2 using the algorithm of section 2.5 to conclude that the
contour $N=\varepsilon+\i \mathbb{R}$ picks up the GH saddle as the leading contribution.

## [sect5-concl] section: 5 Concluding remarks
### [sect5-concl-p1] paragraph

We emphasized a problem with the Euclidean gravitational path integral, reminiscent of the conformal mode
problem, but pertaining to genuine classical solutions. For certain special matter contents (with wrong sign
kinetic term) there exist cosmological solutions that oscillate indefinitely in Euclidean space. This means
that the Euclidean gravitational path integral is divergent, and therefore cannot reasonably be considered the
correct definition of quantum gravity.

### [sect5-concl-p2] paragraph

Working in minisuperspace, we considered two alternative definitions of quantum gravity which (from this
perspective) seem more reasonable. These options are characterized by Lorentzian lapse contours.

$N=\varepsilon+\i \mathbb{R}$ The main point of this work was to show that this contour agrees with the
Gibbons-Hawking proposal: that the Euclidean gravitational path integral computes the entropy of the dS static
patch. This contour similarly predicts a finite order $1/G$ entropy for an observer in a static patch with
negative-kinetic-energy matter (like the axion and YM configurations we have studied). The dominant saddle
lives in the $a\to -a$ sector:

\[ \class{l2mpic-29}{\rule[-4.1585em]{16.2044em}{8.7457em}} \]

(5.1)

$N=-\varepsilon+\i \mathbb{R}$ (or $N = \i\mathbb{R}^+$) This contour predicts an entropy which is of order
one (in $G$) for an observer in the dS static patch. This would mean that the area of the cosmological horizon
is not measuring entropy. Even though this seems a radical idea, recent work questions to what degree
cosmological area is entropy survives when finite $G$ effects are taken into account [24, 25, 26, 27]. The
reason that the contour $N=-\varepsilon+\i \mathbb{R}$ gives no $1/G$ term in the entropy is as follows.
Thinking about the trace of the density matrix as integrating over $a_0=a_1$, for $a_0<a_{\text{max}}$ there
are two Euclidean saddle points in the $N$ plane close to $N=0$, of positive and negative values of $N$,
corresponding to $k=0$. They differ by the orientation of time. When $a_0$ approaches $a_{\text{max}}$ the
proper time of the corresponding saddle goes to zero. This contour picks the saddle with $N<0$. The result of
integration over $a_0$ gives in terms of $1/G$ dependence a vanishing entropy, since it is dominated by
$a_0\to a_\text{max}$. For a contour $N = \i\mathbb{R}^+$, there is a similar conclusion, but its origin is in
the $N=0$ endpoint of the integration contour, rather than a saddle point.

\[ \class{l2mpic-30}{\rule[-4.1585em]{14.3938em}{8.7457em}} \]

(5.2)

### [sect5-concl-p3] paragraph

We end with various comments. Firstly, the minisuperspace approximation is of course not complete. In
particular the Picard-Lefschetz analysis may well change beyond minisuperspace. See [81] for an analysis of
fluctuations on these spacetimes. Here we simply note that the fact that Lorentzian contours in minisuperspace
give reasonable answers is encouraging to undertake an analysis beyond minisuperspace.

### [sect5-concl-p4] paragraph

Secondly, we have described things from the perspective of a global slicing ADM quantum mechanics. It would of
course be interesting to describe this immediately from the perspective of a static-patch-type quantum
mechanics, describing an observer’s density matrix [37] directly. Obviously, such a quantum mechanics is very
hard to come by, as its microstates would be a microscopic realization of dS entropy.

### [sect5-concl-p5] paragraph

Thirdly, it may be interesting to understand if Kontsevich-Segal-Witten in the no-boundary state [6, 7, 95,
96, 97] has something to say about necklaces, as it did for a chain of spheres $q\to 0$. Our configurations
are not allowable according to the KSW criterion: avoiding the big-bang at $a=0$ as in equation (2.62), one
infinitesimally passes through an un-allowable region, crossing for instance $a^2=-\varepsilon^2<0$. However,
they may still be physical, as they seem to obey the weaker “spectral KSW condition” [98] which is a condition
on the well-definedness of one-loop matter partition functions on these complex metrics, allowing for more
general contour rotations of the fields.23

### [sect5-concl-p6] paragraph

Relatedly, following [66, 67], one could propose the following stability criterion for a general FLRW-type
background with scale factor $a(T)$ and spatial manifold $\Sigma$. Imagine we couple conformal matter to this
background. By a naive Weyl transformation, one maps to $\Sigma \times I$ with time coordinate $\d\eta = \d
T/a(T)$. The Euclidean length of the interval is

\[ \beta = \i \int \frac{\d T}{a(T)}\,. \]

(5.3)

For $\text{Re}\,\beta \leq 0$ the CFT partition function diverges, rendering the FLRW spacetime unstable to
quantum fluctuations.

### [sect5-concl-p7] paragraph

How about our contour (2.62)? Naively, $a(T)$ changes sign due to the Lorentzian detour around the
singularity, resulting in a troubling $\text{Re}\, \beta=0$.24 Take the generator of conformal time
transformations $H_\eta=a(T) H_T$. If $\text{Re}\,a(T)>0$ the generator of $\eta$ transformations remains
bounded from below, which keeps the stability condition sensible. When $\text{Re}\,a(T)<0$, negative $\eta$
flow arises. However, we notice that simultaneously $H_\eta$ becomes unbounded from above, such that negative
$\eta$ evolution actually is the stable case. We propose to think about (2.62) as the product of the contour
before and after winding around the singularity. Each part by itself is a bounded operator, and hence so is
the product. The alternative would be to conclude that a configuration with $a(T)<0$ everywhere, which is
gauge-equivalent to one with $a(T)>0$ everywhere (these describe the same metric), would be an unstable
background.25 Note that the $\pi$ contour [66, 67] would be to go from $\tau=0$ to $1$ in a straight line in
(2.62). Along this contour $a(\tau)>0$.

### [sect5-concl-p8] paragraph

Finally, consider the universal area law scaling for the 3d axion wormhole action (1.16), see section 2.6. It
would be interesting to understand if a version of this argument generalized to higher dimensions. Is there
any contour in the complex $a$ plane for which the on-shell action (see section 3) exactly matches the $q=0$
GH action, which deforms to a late-time dS contour? Converse, suppose we take a late-time dS contour and
contour deform “as much as possible” to the purely Euclidean contour, what wormhole geometry does this
produce? We leave this for future investigations.

## [acknowledgments] section: Acknowledgments
### [acknowledgments-p1] paragraph

We are happy to thank Jan de Boer, Victor Gorbenko, Aidan Herderschee, Victor Ivo, Oliver Janssen, Juan
Maldacena, Don Marolf, Henry Maxfield, Nathan Seiberg, and Edward Witten for discussions. We especially thank
Sergio Ernesto Aguilar Gutierrez for pointing us to the work of Halliwell and Myers [41]. AB was supported by
the US DOE and the Leinweber Foundation. JKF is supported by the Marvin L. Goldberger Member Fund at the
Institute for Advanced Study and the National Science Foundation under Grant No. PHY-2514611. VN is supported
by DARPA AIQ grant (HR001124S0029). EYU was supported by the J. Robert Oppenheimer Endowed Fund and the Fund
for Natural Sciences. We acknowledge discussions in the workshop “Observers, wormholes and complex saddles in
cosmology” at the Bernoulli center, at EPFL, Lausanne, CH. The authors used the assistance of Claude and of
ChatGPT for numerical simulations, proofreading, and development of arguments. All derivations were carried
out and written up by the authors, who take full responsibility.

## [app-5dproper] appendix: A Five dimensional axion necklaces using proper-time gauge
### [app-5dproper-p1] paragraph

In this appendix, we will study 5d axion wormholes in proper-time gauge (introduced in section A.1). In
section A.2 we present analytically the case of pure gravity (solutions and on-shell actions). In section A.3
we show that the Lorentzian lapse contour $N=\varepsilon+\i\mathbb{R}$ picks up the GH sphere saddle as
dominating configuration. In section A.4 we study numerically $q>0$ and show that this picture persists,
reducing to our analytical analysis for $q\to 0$.

### [sect3.1-5fproper] appendix: A.1 Proper-time gauge
#### [sect3.1-5fproper-p1] paragraph

Beginning with the action (3.1), we consider FLRW configurations in the standard proper-time gauge:

\[ \d s^2 = N^2 \d \tau^2 + a(\tau)^2 \d \Omega_{d-1}^2\,,\quad 0\leq \tau\leq 1\,. \]

(A.1)

Using (3.3), one finds the following action:

\[ I = \frac{\Omega_{d-1}(d-1)(d-2)}{8\pi G}\int_0^1 \d\tau\, a^{d-3}\bigg\{-\frac{\dot a^2}{2N} +\frac{N}{2}\bigg(-1+H^2 a^2 + \frac{1}{d-1}\left(\frac{d-2}{d-1}\right)^{d-2} \frac{q^2}{(H a)^{2(d-2)}} \bigg)\bigg\}. \]

(A.2)

Compared to the kinetic gauge analysis of section 3, we find two differences. First, the kinetic term for the
scale factor is non-standard, which makes the quantum mechanical analysis less standard. Secondly, $a\mapsto
-a$ is a symmetry of the action only for odd $d$. For this reason, we shall consider only $5d$ here. In units
$H=1$, the 5d action becomes:

\[ I_\text{5d} = \frac{4\pi}{G}\int_0^1 \d \tau \bigg\{-\frac{a^2\dot a^2}{2N} +\frac{N}{2}\bigg(-a^2+a^4 + \frac{27}{256} \frac{q^2}{a^4} \bigg)\bigg\}\,. \]

(A.3)

#### [sect3.1-5fproper-p2] paragraph

As the kinetic term is non-standard, it is convenient to think of this system as describing quantum mechanics
of a particle with a coordinate:

\[ A=a^2\,. \]

(A.4)

The action then becomes

\[ \boxed{I_\text{5d}=\frac{4\pi}{G}\int_0^1\d \tau \bigg\{-\frac{\dot{A}^2}{8 N}+\frac{N}{2}\bigg(-A+A^2+ \frac{27}{256} \frac{q^2}{A^2}\bigg)  \bigg\}\,} \]

(A.5)

This shares many similarities with the 3d action (2.4). The natural analogs of the $a\to -a$ configurations in
3d are, in proper-time gauge (A.1), the $A\to -A$ configurations. Following section 2.5 one finds for $N\to 0$

\[ \mathcal{G}_N(A_1\rvert A_2)\, \to\, e^{\frac{\pi}{2 N G}(A_1-A_2)^2}\,. \]

(A.6)

This has a very similar property to the relevant 3d $N\to 0$ propagators: $\mathcal{G}_N(A\rvert A)$ has no
singularity, and instead a saddle at $N=0$. Furthermore, crucially, $\mathcal{G}_N(A\rvert -A)$ does have a
singularity for $N\to 0$. The defining contour thus again deforms to a steepest descent contour through the
first saddle (at $N=N_0$).

#### [sect3.1-5fproper-p3] paragraph

In the remainder of this section we study the $q=0$ case analytically, and the finite $q$ case numerically.

### [appa1] appendix: A.2 Pure gravity analytically
#### [appa1-p1] paragraph

In this section we take the pure gravity limit $q\rightarrow 0$, which can be solved analytically. Rescaling
$\tau \to N\tau$ and introducing

\[ B=A-\frac{1}{2} = a^2-\frac{1}{2}\,, \]

(A.7)

the Euclidean action becomes:

\[ I = \frac{\pi}{G}\int_0^N \d \tau \bigg\{-\frac{1}{2}\dot B^2-\frac{1}{2}+2 B^2  \bigg\}\,. \]

(A.8)

This resembles the 3d theory (2.4) for $q\to 0$. The equations of motion are

\[ \ddot{B}+4 B=0\,. \]

(A.9)

The classical dS solution reads

\[ B=\frac{1}{2}\cos(2\tau)\quad \to \quad a=\cos(\tau)\,,\quad N=\pi\,. \]

(A.10)

We distinguish two interesting solution sectors.

Standard solutions Imposing $a(0)=a_1>0\,,a(N)=a_2>0$ one finds

\[ a^2_+(\tau) = \frac{1}{2}+\left(a^2_1-\frac{1}{2}\right)\frac{\sin(2(N-\tau))}{\sin(2N)}+\left(a^{2}_2-\frac{1}{2}\right)\frac{\sin(2\tau)}{\sin(2N)}\,. \]

(A.11)
In Lorentzian signature, one takes $\tau = \i T$ and $N = \i N_\text{L}$. The Lorentzian solution satisfies
$a^2>0$ for every $N_\text{L}$, and so corresponds to a valid real solution for $a(t)$. The Euclidean solution
satisfies $a^2(\tau)>0$ for $0\le \tau \le N$ only when $-\pi/2\le N\le \pi/2$. For generic $N$, $a(\tau)$ is
complex. Our perspective is that to study $I_{a_0\to a_0}(N)$ one takes real $a(T)$ on the Lorentzian axis,
and analytically continues those in $N$. The action becomes

\[ \frac{G}{2\pi}I_{a_1\to a_2}(N)=-\frac{N}{4}-
    \frac{1}{2}(B_1^2+B_2^2)\,\cot(2N)
    +\frac{B_1 B_2}{\sin(2N)}\,,\quad B_i=a_i^2-\frac{1}{2}\,. \]

(A.12)
As a check, for $N\to 0$ we find $I_{a_1\to a_2}(N\to 0)\to -\pi (B_1-B_2)^2/(2 G N)$, consistent with formula
(A.6). For computing the GH entropy, we are interested in $a_1=a_2=a_\text{max}=1$. The action now reads:

\[ \boxed{\frac{2 G}{\pi} I_{a_\text{max}\to a_\text{max}}(N)=-N+\tan(N)\,} \]

(A.13)
This is identical to the 3d action for pure dS (2.41) modulo $N\to N/2$. Indeed, rescaling $N\to N/2$ and
$B\to B/2$ brings equations (A.8) and (2.4) in identical form.

Bouncing solutions Based on our analysis of section 2, we would like to mimic a solution which goes through
the origin in the $a$ plane: $a_0\to 0\to -a_0$. Notice that this involves only $B\geq -1/2$. Indeed, equation
(A.7) suggests that we should view the $B$ quantum theory as having a brick wall at $B=-1/2$:

\[ \class{l2mpic-31}{\rule[-4.3338em]{24.5390em}{9.0961em}} \]

(A.14)
The solution $a_0\to 0\to -a_0$ is translated in $B$ coordinates as a particle that bounces off the wall at
$B=-1/2$. In quantum mechanics, we compute the total propagator by first propagating from $a_0\to 0$ and then
from $0\to -a_0$. The total action is

\[ I_{a_0\to -a_0}(N)=I_{a_0\to 0}(N_1)+I_{0\to-a_0}(N-N_1)\,. \]

(A.15)
The solution is found upon extremizing over $N_1$. In the Hamiltonian formulation, which involves a momentum
$P=\dot{B}/N$ as in (2.24), extremizing over $N_1$ imposes that the $a$ particle has the same energy before
and after the bounce: $E_1=E_2$. This imposes that after the bounce the momentum $P$ simply flips sign. The
saddle is: $N_1=N/2$. A particle with conserved energy indeed takes the same time to reach the wall as it does
to come back. Therefore we find:

\[ \frac{G}{2\pi} I_{a_0\to-a_0}(N)=
    -\frac{N}{4}
    +\left(a_0^2-a_0^4-\frac{1}{2}\right)\cot(N)
    - \left(a_0^2-\frac{1}{2}\right)\frac{1}{\sin(N)}\,. \]

(A.16)
More specifically:

\[ \boxed{\frac{2G}{\pi} I_{a_\text{max}\to -a_\text{max}}(N)=-N-2\cot(N/2)\,} \]

(A.17)
This action has saddles at $N=\pi+2\pi k$ and singularities at $N=2\pi k$. A contour analysis in the next
section A.3 shows that the Lorentzian contour $N=\varepsilon+\i \mathbb{R}$ is dominated by the saddle $N=\pi$
with entropy $S=-I$ equal to the area of the cosmological horizon of 5d dS space, as is expected:

\[ S=\frac{\pi^2}{2 G}\,. \]

(A.18)
In section A.4 we check numerically that bouncing off a wall as described here is the correct $q\to 0$ limit
of the particle bouncing off the finite potential wall at $B\to -1/2$ due to $q\neq 0$ axions. See for
instance equation (A.5) for the $q\neq 0$ potential wall.

### [app-contours] appendix: A.3 Deformations of Lorentzian contours
#### [app-contours-p1] paragraph

We next perform the steepest descent analysis starting from the Lorentzian contour $N=\varepsilon+\i
\mathbb{R}$ for the actions (A.12)/(A.16).

#### [app-contours-p2] paragraph

Standard solutions Consider first a trajectory $a_0\to a_0$. The Euclidean action (A.12) matches with the 3d
action (2.41) (when rescaling the integrating variable $N\to N/2$):

\[ -\frac{2G}{\pi}I_{a_0\to a_0}(N)=N-a_{0\,\text{3d}}^2\tan(N)\,,\quad a_{0\,\text{3d}}=2 a_0^2-1\,. \]

(A.19)

The structure of singularities and saddles was discussed in section 2.2. This action has singularities at
$N=\pi(k+1/2)$. The saddles are:

\[ N=\pm \i\, \text{arccosh}(a_{0\,\text{3d}})+\pi k\,. \]

(A.20)

For $a_0>1$, the classical solution has a piece of Lorentzian evolution, hence the imaginary contributions to
elapsed time $N$. Expanding around the saddles, one finds that fixed phase lines emerging from these saddles
have angles $\pm \pi/4$ with the real $N$ axis. A Lorentzian contour $N= \pm \varepsilon+\i \mathbb{R}$ picks
up the saddles with $k\leq 0$. See figure 7.

#### [fig-app1] figure: Figure 7

Figure 7. Complex $N$ plane for $I_{a_0 \to +a_0}(N)$ for pure dS (A.19). Poles in the action are red
$\cross$’s and saddles are black dots. Steepest descent (ascent) curves are black solid (dashed) lines. The
Lorentzian $N=\varepsilon+\i\mathbb{R}$ contour is drawn vertically in magenta and the absolutely convergent
contour that it is deformed into is drawn in orange. Here $G$ was slightly complexified to make the
ascent/descent lines non-degenerate.

#### [app-contours-p3] paragraph

This is a slightly more refined version of the 3d figure 1. The leading saddle has purely imaginary action, as
the $k=0$ solution represents an entirely Lorentzian bra-ket wormhole:

\[ \pm \frac{2G}{\pi}I_{a_0\to a_0}(N)=-\i\,\text{arccosh}(a_{0\,\text{3d}})+\i\,a_{0\,\text{3d}}\sqrt{a_{0\,\text{3d}}^2-1}\,. \]

(A.21)

#### [app-contours-p4] paragraph

Bouncing solutions The action (A.16) can be rewritten as

\[ -\frac{2G}{\pi} I_{a_0\to-a_0}(N)=N +(a_{0\,\text{3d}}^2+1)\cot(N)+\frac{2 a_{0\,\text{3d}}}{\sin(N)}\,. \]

(A.22)

The singularities are located at $N=\pi k$ and the saddles are located at

\[ N=\pm \i\, \text{arccosh}(a_{0\,\text{3d}})+\pi (2k+1)\,. \]

(A.23)

In the case in which we are interested, $a_{0\,\text{3d}}=1$ and the saddles are on the real axis. The only
remaining singularities are at $N=2\pi k$. The action is singular at $N=0$, is real for real $N$, and
$-I_{a_\text{max}\to -a_\text{max}}(N)$ decreases monotonically to the saddle at $N=\pi$. The steepest ascent
contour starting at $N=\pi$ crosses the contour $N=\varepsilon+\i \mathbb{R}$. According to Picard-Lefschetz,
this means that the $N=\pi$ saddle contributes to the Lorentzian gravitational path integral. A detailed plot
confirms that this is also the dominating saddle. See figure 8.

#### [fig-app2] figure: Figure 8

Figure 8. Complex $N$ plane for $I_{a_0 \to -a_0}(N)$ for pure dS (A.22). Poles in the action are red
$\cross$’s and saddles are black dots. Steepest descent (ascent) curves are black solid (dashed) lines. The
Lorentzian $N=\varepsilon+\i\mathbb{R}$ contour is drawn vertically in magenta and the absolutely convergent
contour that it is deformed into is drawn in orange. Here $G$ was slightly complexified to render the
ascent/descent lines non-degenerate. Singularities between the saddles go away for $a_0\to a_\text{mas}$.

#### [app-contours-p5] paragraph

Notice that instead choosing the contour $N=-\varepsilon+\i \mathbb{R}$, the leading contribution is $k=-1$.
Hence, the path integral would predict $S=0$ (at order $1/G$). In subsection A.4, we show numerically that
this behavior of the action $I_{a_0\to-a_0}(N)$ persists for finite $q\neq 0$.

### [app-numerics] appendix: A.4 Numerical analysis at finite q
#### [app-numerics-p1] paragraph

Recall equation (A.5) (with $A=a^2$ and rescaled $N\to N/2$):

\[ I_\text{5d}=\frac{2\pi}{G}\int_0^1\d \tau \bigg\{-\frac{\dot{A}^2}{2 N}+\frac{N}{2}\bigg(-A+A^2+ \frac{27}{256} \frac{q^2}{A^2}\bigg)  \bigg\}\,. \]

(A.24)

Figure 9 shows the numerical solutions for a particle moving in this potential with boundary conditions
$a_\text{max}\to -a_\text{max}$, generalizing the bouncing solution to finite $q$. For $q\to 0$ we found an
action (A.17) for the bouncing solution. The numerical analysis leads to the following conclusions. The finite
$q$ solution for $A$ limits to a solution which bounces off a wall at $A=0$ for $q\to 0$,

#### [fig-appnum1] figure: Figure 9

Figure 9. The finite $q$ numerical solution of (A.24) limits to a solution which bounces off the wall at $A=0$
for $q\to 0$.

#### [app-numerics-p2] paragraph

confirming the picture (A.14).

#### [app-numerics-p3] paragraph

As shown in figure 10, the numerically evaluated action $I_{a_\text{max}\to -a_\text{max}}(N)$ associated with
the bouncing solution matches with the analytic formula (A.17) when $q\to 0$. Furthermore, the action
$I_{a_\text{max}\to a_\text{max}}$ of the standard solution limits to (A.13).

#### [fig-appnum2] figure: Figure 10

Figure 10. The finite $q$ action (A.24) approaches the bounce analytic action (A.17) for $q\to 0$ (left),
taking into account rescaling $N\to N/2$. For $q\to 0$ one finds $A_\text{min}\sim q^{2/3}$, $2\pi-N_0\sim
q^{1/3}$, and the action deficit scaling with $q$ analytically. Numerics support this (right).

#### [app-numerics-p4] paragraph

The difference for finite $q$ is the appearance of branch points off the real $N$ axis, identified
analytically in 3d below equation (2.34). These branch points represent values of $N$ where the bouncing and
standard solutions coincide, as we see explicitly in 3d in equation (2.56). The associated branch cuts connect
the two sheets of the solution/action, namely $a_\text{max}\to  a_\text{max}$ and $a_\text{max}\to
-a_\text{max}$. In 3d we have at times called these the $a_+$ and $a_-$ solutions. The general situation, for
general potential, general gauge, or general dimension, as discussed in section 3.2, is a multi-sheeted
solution space, on which one must perform a Picard-Lefschetz analysis.

#### [footnotes] footnotes: Footnotes

Notes1See for instance [8] and later work.

2Subregions in quantum gravity (like the static patch) are difficult to define. Furthermore, even plain QFT on
a subregion does not usually have a well-defined trace on some Hilbert space. See for instance [12, 13].
Therefore, it is far from obvious what the relevant Hilbert space and trace would be.

3The other leading order gravitational constraints were imposed in [15] leading to further edge mode
contributions.

4Technically they only showed that generalized entropy differences measure entropy differences between states.
A relative state counting interpretation has been discussed in [16].

5The analogy with the sphere is not completely obvious. Indeed, it is not obvious if an analytic continuation
of a Lorentzian time in the causal patch of an observer in this spacetime maps nicely to a Euclidean time
coordinate on this wormhole. However, independent of this confusion, arguments were presented in [39] that
(1.5) does actually compute the observer’s entropy. A perturbative calculation supporting this proposal, along
the lines of CLPW [14], would be extremely valuable.

6See also for instance [40, 41].

7We impose initial and final boundary conditions $a=a_\text{max}$ at $\tau=0$ and $\tau=1$. For real $N$ the
metric (1.4) is Euclidean between the initial and final slice $0\leq \tau\leq 1$. If $N=\i \mathbb{R}$ the
metric preparing the state is Lorentzian between $0<\tau<1$. Lorentzian lapses means that we integrate over
Lorentzian path integral preparations. The dS sphere has a Euclidean lapse (real $N$). The invariant statement
is whether the integral of $\d s$ between initial and final Cauchy slices is real (Euclidean lapse), or purely
imaginary (Lorentzian lapse).

8In general, the lapse contour is a question of active investigation, see for instance [58, 51, 59, 60, 61,
39]. The real axis is natural in quantum mechanics and gives reasonable answers, however it is not obviously
equivalent to calculations for instance in 2d quantum gravity, and in matrix models [62, 63]. We thank Dio
Anninos and Nathan Seiberg for discussions. Timelike Liouville might provide a rigid framework to make
progress on this [64, 65].

9This picture for $V(a)$ is most clear in 3d (see section 2). It extends to odd spacetime dimensions in a
rather straightforward manner (see section 3). For even spacetime dimensions, this symmetry between $a$ and
$-a$ is less obvious (see section 3), but persists in (what we will call) kinetic gauge.

10The two slices where $\abs{a}=a_\text{max}$ are identified such as to produce a closed topology, in the
spirit of equation (1.5). $a_\text{max}$ and $a_\text{min}$ are surfaces of time-reflection symmetry (and zero
extrinsic curvature) where one could glue geometries together, or continue smoothly to Lorentzian signature
spacetimes.

11For some observer at $\theta=0$ the causal horizon at the time reflection symmetric slice is located at [39]
\[ \theta_h=\sqrt{\frac{2}{1+\sqrt{1-q^2}}} \ 
 K\bigg(\frac{1-\sqrt{1-q^2}}{1+\sqrt{1-q^2}}\bigg)>\frac{\pi}{2}\,. \]

(2.15)
 As indicated already in the Penrose diagram equation (1.3), this means this observer has causal access to
more than half of the time reflection symmetric global slice.

12Alternatively, we could glue at $a^2=a_\text{min}^2$, as shown in equation (1.7). All calculations in this
section could be repeated for $\rho_\text{no-boundary}(a_\text{min}^2\rvert a_\text{min}^2)$ with identical
results.

13When treating $a\mapsto-a$ as a $\mathbb{Z}_2$ gauge symmetry, the overall factor $2$ in (2.20) should be
replaced by $1/2$. However, such $N$-independent prefactors would not affect the semiclassical statements in
this paper, and they are subleading to quantum corrections that we are ignoring, so we do not keep track of
them.

14Even if one would not view this as redundancy, it would only produce a finite volume prefactor which does
not contribute meaningfully to the semiclassical action which we will be investigating.

15The general differential equation has a one-parameter family of solutions labeled by energy $H_\text{WDW}=E$
eigenvalues. The boundary condition essentially fixes the complete expansion into Hamiltonian eigenfunctions
(using delta ortho-normal eigenfunctions $\psi_E(a)$) to have trivial integration kernel:
\[ \mathcal{G}_{N}(a_1\rvert a_2)=\int\d E\,\overline{\psi_E(a_1)}\psi_E(a_2)\,e^{-\frac{N}{G} E}\,. \]

(2.27)
 This is unique. The Schrodinger equation alone (in both $a_1$ and $a_2$) generally still allows for a free
integration kernel $\rho(E)$.

16We have implicitly assumed the parameters are so that we are describing Euclidean configurations, otherwise
the Bessel function asymptotics is governed by two oscillatory saddles. For real $N$ and for
$a_1^2=a_2^2=a_\text{max}^2$ this is the correct regime.

17Use
\[ \int_{-N}^{+N} \frac{\d \tau}{A+\cos(\tau)} = -\frac{4}{\sqrt{1-A^2}}\text{arctanh}\bigg(\frac{A-1}{\sqrt{1-A^2}}\tan(N/2)\bigg)\,. \]

(2.59)


18At $a=a_\text{max}$ the saddle is cubic. It may be convenient to view this as a limit of Lorentzian boundary
conditions $a>a_\text{max}$ in which case there are two saddles on opposite sides of the real axis, which
coincide when $a\to a_\text{max}$. See figure 8. For Euclidean $a<a_\text{max}$ boundary conditions, two
saddles are on the real axis, and according to the Picard-Lefschetz argument, only the first saddle
contributes. This transition matches the Stokes phenomenon in the asymptotics of the Bessel function (2.28).

19Technically, we are solving the problem for $a_\text{max}\to a_\text{max}$ boundary conditions and are
indeed investigating the so-called $a_-$ bouncing solution. As discussed in section 2, around equation (2.61),
this is related to the tunneling $a_\text{max}\to -a_\text{max}$ solution by the addition of a constant in the
action. This structure persists in higher dimensions, because of the universal $a\to 0$ behavior of the
potential in kinetic gauge (3.4), giving a universal solution for $a\to 0$ and ditto pole contributions.

20Here $\theta$ denotes an angle on the $d-1$ sphere $\Omega_{d-1}$ with unit metric component
$\gamma_{\theta\theta } = 1$.

21We thank Edward Witten for bringing the 4d solution to our attention, from which the generalization to $d>4$
naturally follows.

22In $d=4$ this configuration is the meron of [93].

23We thank Aidan Herderschee for checking the spectrum of a scalar field on this background numerically and in
certain limits, providing evidence for this.

24We thank Victor Gorbenko for raising this concern.

25The GH saddle, in our current interpretation as an $a_\text{max}\to -a_\text{max}$ solution, would also not
prepare the global vacuum state $\beta=\infty$ but rather the maximally mixed state $\beta=0$. This would be
an extremely troubling conclusion.

#### [refs] references: References

References[1]G. W. Gibbons, S. W. Hawking, and M. J. Perry, “Path Integrals and the Indefiniteness of the
Gravitational Action,” Nucl. Phys. B 138 (1978) 141–150.
[2]P. Saad, S. H. Shenker, and D. Stanford, “JT gravity as a matrix integral,” arXiv:1903.11115 [hep-th].
[3]G. Penington, S. H. Shenker, D. Stanford, and Z. Yang, “Replica wormholes and the black hole interior,”
JHEP 03 (2022) 205, arXiv:1911.11977 [hep-th].
[4]P. Saad, “Late Time Correlation Functions, Baby Universes, and ETH in JT Gravity,” arXiv:1910.10311 [hep-
th].
[5]A. Blommaert, “Dissecting the ensemble in JT gravity,” JHEP 09 (2022) 075, arXiv:2006.13971 [hep-th].
[6]M. Kontsevich and G. Segal, “Wick Rotation and the Positivity of Energy in Quantum Field Theory,” Quart. J.
Math. Oxford Ser. 72 no. 1-2, (2021) 673–699, arXiv:2105.10161 [hep-th].
[7]E. Witten, “A Note On Complex Spacetime Metrics,” arXiv:2111.06514 [hep-th].
[8]A. Maloney and E. Witten, “Quantum Gravity Partition Functions in Three Dimensions,” JHEP 02 (2010) 029,
arXiv:0712.0155 [hep-th].
[9]D. Stanford and C. Yan, “Cusps in 3d gravity,” arXiv:2510.19920 [hep-th].
[10]G. W. Gibbons and S. W. Hawking, “Cosmological Event Horizons, Thermodynamics, and Particle Creation,”
Phys. Rev. D 15 (1977) 2738–2751.
[11]G. W. Gibbons and S. W. Hawking, “Action integrals and partition functions in quantum gravity,” Physical
Review D 15 no. 10, (1977) 2752.
[12]E. Witten, “APS Medal for Exceptional Achievement in Research: Invited article on entanglement properties
of quantum field theory,” Rev. Mod. Phys. 90 no. 4, (2018) 045003, arXiv:1803.04993 [hep-th].
[13]E. Witten, Why does quantum field theory in curved spacetime make sense? And what happens to the algebra
of observables in the thermodynamic limit? 2022. arXiv:2112.11614 [hep-th].
[14]V. Chandrasekaran, R. Longo, G. Penington, and E. Witten, “An algebra of observables for de Sitter space,”
JHEP 02 (2023) 082, arXiv:2206.10780 [hep-th].
[15]M. S. Klinger, J. Kudler-Flam, and G. Satishchandran, “Generalized Entropy is von Neumann Entropy II: The
complete symmetry group and edge modes,” arXiv:2601.07910 [hep-th].
[16]C. Akers and J. Sorce, “Relative State Counting for Semiclassical Black Holes,” Phys. Rev. Lett. 133
no. 20, (2024) 201601, arXiv:2404.16098 [hep-th].
[17]D. Anninos, F. Denef, Y. T. A. Law, and Z. Sun, “Quantum de Sitter horizon entropy from quasicanonical
bulk, edge, sphere and topological string partition functions,” JHEP 01 (2022) 088, arXiv:2009.12464 [hep-th].
[18]D. Anninos, T. Bautista, and B. Mühlmann, “The two-sphere partition function in two-dimensional quantum
gravity,” JHEP 09 (2021) 116, arXiv:2106.01665 [hep-th].
[19]D. Anninos, C. Baracco, V. A. Letsios, and B. Mühlmann, “dS$^4$ Metamorphosis,” arXiv:2602.19812 [hep-th].
[20]D. Anninos, P. Benetti Genolini, and B. Mühlmann, “dS$_{2}$ supergravity,” JHEP 11 (2023) 145,
arXiv:2309.02480 [hep-th].
[21]J. Maldacena, “Real observers solving imaginary problems,” arXiv:2412.14014 [hep-th].
[22]Y. Chen, D. Stanford, H. Tang, and Z. Yang, “On the phase of the de Sitter density of states,” JHEP 05
(2026) 068, arXiv:2511.01400 [hep-th].
[23]Y. T. A. Law and V. Lochab, “Horizon Edge Partition Functions in $\Lambda >
  0$ Quantum Gravity,” Phys. Rev. Lett. 136 no. 15, (2026) 151601, arXiv:2603.20913 [hep-th].
[24]Y. Chen, D. Stanford, H. Tang, and Z. Yang, “Negative shocks versus static patch holography,”
arXiv:2607.14042 [hep-th].
[25]A. Milekhin, V. Narovlansky, and J. Xu, “Out-of-time-ordered Correlators in de Sitter Revisited,”
arXiv:2607.13137 [hep-th].
[26]W. Cui and D. K. Kolchmeyer, “A de Sitter Anti-Scrambling Algebra,” arXiv:2607.13665 [hep-th].
[27]D. Harlow and Y. Zhao, “Anti-scrambling and euclidean folds from observer correlators in de Sitter space,”
arXiv:2607.14215 [hep-th].
[28]D. K. Kolchmeyer and H. Liu, “Chaos and the Emergence of the Cosmological Horizon,” arXiv:2411.08090 [hep-
th].
[29]V. Narovlansky, “Towards a microscopic description of de Sitter dynamics,” arXiv:2506.02109 [hep-th].
[30]D. N. Page, “Information in black hole radiation,” Phys. Rev. Lett. 71 (1993) 3743–3746, arXiv:hep-
th/9306083.
[31]J. M. Maldacena, “Eternal black holes in anti-de Sitter,” JHEP 04 (2003) 021, arXiv:hep-th/0106112.
[32]J. S. Cotler, G. Gur-Ari, M. Hanada, J. Polchinski, P. Saad, S. H. Shenker, D. Stanford, A. Streicher, and
M. Tezuka, “Black Holes and Random Matrices,” JHEP 05 (2017) 118, arXiv:1611.04650 [hep-th]. [Erratum: JHEP
09, 002 (2018)].
[33]J. B. Hartle and S. W. Hawking, “Wave function of the universe,” Physical Review D 28 no. 12, (1983) 2960.
[34]S. W. Hawking, “The Quantum State of the Universe,” Nucl. Phys. B 239 (1984) 257.
[35]D. N. Page, “Density matrix of the universe,” Physical Review D 34 no. 8, (1986) 2267.
[36]S. W. Hawking, “The density matrix of the universe,” Physica Scripta 1987 no. T15, (1987) 151.
[37]V. Ivo, Y.-Z. Li, and J. Maldacena, “The no boundary density matrix,” JHEP 02 (2025) 124, arXiv:2409.14218
[hep-th].
[38]E. Witten, “A background-independent algebra in quantum gravity,” JHEP 03 (2024) 077, arXiv:2308.03663
[hep-th].
[39]A. Blommaert, J. Kudler-Flam, and E. Y. Urbach, “Absolute entropy and the observer’s no-boundary state,”
JHEP 11 (2025) 113, arXiv:2505.14771 [hep-th].
[40]I. R. Klebanov, L. Susskind, and T. Banks, “Wormholes and the Cosmological Constant,” Nucl. Phys. B 317
(1989) 665–692.
[41]J. J. Halliwell and R. C. Myers, “Multiple-sphere configurations in the path-integral representation of
the wave function of the universe,” Physical Review D 40 no. 12, (1989) 4011.
[42]C. Teitelboim, “Quantum Mechanics of the Gravitational Field,” Phys. Rev. D 25 (1982) 3159.
[43]C. Teitelboim, “Causality Versus Gauge Invariance in Quantum Gravity and Supergravity,” Phys. Rev. Lett.
50 (1983) 705.
[44]C. Teitelboim, “The Proper Time Gauge in Quantum Theory of Gravitation,” Phys. Rev. D 28 (1983) 297.
[45]A. Vilenkin, “Boundary Conditions in Quantum Cosmology,” Phys. Rev. D 33 (1986) 3560.
[46]A. D. Linde, “Quantum Creation of the Inflationary Universe,” Lett. Nuovo Cim. 39 (1984) 401–405.
[47]J. J. Halliwell and J. Louko, “Steepest Descent Contours in the Path Integral Approach to Quantum
Cosmology. 1. The De Sitter Minisuperspace Model,” Phys. Rev. D 39 (1989) 2206.
[48]J. J. Halliwell and J. Louko, “Steepest Descent Contours in the Path Integral Approach to Quantum
Cosmology. 2. Microsuperspace,” Phys. Rev. D 40 (1989) 1868.
[49]J. J. Halliwell and J. Louko, “Steepest Descent Contours in the Path Integral Approach to Quantum
Cosmology. 3. A General Method With Applications to Anisotropic Minisuperspace Models,” Phys. Rev. D 42 (1990)
3997–4031.
[50]J. J. Halliwell and J. B. Hartle, “Integration Contours for the No Boundary Wave Function of the
Universe,” Phys. Rev. D 41 (1990) 1815.
[51]J. Feldbrugge, J.-L. Lehners, and N. Turok, “Lorentzian Quantum Cosmology,” Phys. Rev. D 95 no. 10, (2017)
103508, arXiv:1703.02076 [hep-th].
[52]J. Feldbrugge, J.-L. Lehners, and N. Turok, “No smooth beginning for spacetime,” Phys. Rev. Lett. 119
no. 17, (2017) 171301, arXiv:1705.00192 [hep-th].
[53]J. Feldbrugge, J.-L. Lehners, and N. Turok, “No rescue for the no boundary proposal: Pointers to the
future of quantum cosmology,” Phys. Rev. D 97 no. 2, (2018) 023509, arXiv:1708.05104 [hep-th].
[54]D. Marolf, “Path integrals and instantons in quantum gravity: Minisuperspace models,” Phys. Rev. D 53
(1996) 6979–6990, arXiv:gr-qc/9602019.
[55]D. Marolf, “Gravitational thermodynamics without the conformal factor problem: partition functions and
Euclidean saddles from Lorentzian path integrals,” JHEP 07 (2022) 108, arXiv:2203.07421 [hep-th].
[56]G. J. Loges, G. Shiu, and N. Sudhir, “Complex saddles and Euclidean wormholes in the Lorentzian path
integral,” JHEP 08 (2022) 064, arXiv:2203.01956 [hep-th].
[57]J.-L. Lehners, “Review of the no-boundary wave function,” Phys. Rept. 1022 (2023) 1–82, arXiv:2303.08802
[hep-th].
[58]J. Diaz Dorronsoro, J. J. Halliwell, J. B. Hartle, T. Hertog, and O. Janssen, “Real no-boundary wave
function in Lorentzian quantum cosmology,” Phys. Rev. D 96 no. 4, (2017) 043505, arXiv:1705.05340 [gr-qc].
[59]A. Di Tucci, J.-L. Lehners, and L. Sberna, “No-boundary prescriptions in Lorentzian quantum cosmology,”
Phys. Rev. D 100 no. 12, (2019) 123543, arXiv:1911.06701 [hep-th].
[60]B. Banihashemi and T. Jacobson, “On the lapse contour in the gravitational path integral,” Phys. Rev. D
111 no. 6, (2025) 066014, arXiv:2405.10307 [hep-th].
[61]B. Dittrich, T. Jacobson, and J. Padua-Argüelles, “de Sitter horizon entropy from a simplicial Lorentzian
path integral,” Phys. Rev. D 110 no. 4, (2024) 046006, arXiv:2403.02119 [gr-qc].
[62]D. Anninos and S. Brian, “Aspects of Closed Matricial Worlds,” arXiv:2607.21509 [hep-th].
[63]G. W. Moore, N. Seiberg, and M. Staudacher, “From loops to states in 2-D quantum gravity,” Nucl. Phys. B
362 (1991) 665–709.
[64]D. Anninos, C. Baracco, and B. Mühlmann, “Remarks on 2D quantum cosmology,” arXiv:2406.15271 [hep-th].
[65]D. Anninos, T. Hertog, and J. Karlsson, “Quantum Liouville Cosmology,” arXiv:2512.15969 [hep-th].
[66]Y. Chen, V. Gorbenko, and J. Maldacena, “Bra-ket wormholes in gravitationally prepared states,” JHEP 02
(2021) 009, arXiv:2007.16091 [hep-th].
[67]A. Fumagalli, V. Gorbenko, and J. Kames-King, “De Sitter Bra-Ket Wormholes,” arXiv:2408.08351 [hep-th].
[68]D. Harlow, J. Maltz, and E. Witten, “Analytic Continuation of Liouville Theory,” JHEP 12 (2011) 071,
arXiv:1108.4417 [hep-th].
[69]R. Usciati, C. Guillarmou, R. Rhodes, and R. Santachiara, “Probabilistic Construction of Noncompactified
Imaginary Liouville Field Theory,” Phys. Rev. Lett. 136 no. 3, (2026) 031601, arXiv:2505.09390 [hep-th].
[70]A. Vilenkin, “Creation of universes from nothing,” Physics Letters B 117 no. 1-2, (1982) 25–28.
[71]A. Vilenkin, “Quantum Creation of Universes,” Phys. Rev. D 30 (1984) 509–511.
[72]A. Vilenkin, “Quantum Cosmology and the Initial State of the Universe,” Phys. Rev. D 37 (1988) 888.
[73]E. Witten, “Analytic Continuation Of Chern-Simons Theory,” AMS/IP Stud. Adv. Math. 50 (2011) 347–446,
arXiv:1001.2933 [hep-th].
[74]R. C. Myers, “New Axionic Instantons in Quantum Gravity,” Phys. Rev. D 38 (1988) 1327.
[75]S. E. Aguilar-Gutierrez, T. Hertog, R. Tielemans, J. P. van der Schaar, and T. Van Riet, “Axion-de Sitter
wormholes,” JHEP 11 (2023) 225, arXiv:2306.13951 [hep-th].
[76]B. S. DeWitt, “Quantum Theory of Gravity. 1. The Canonical Theory,” Phys. Rev. 160 (1967) 1113–1148.
[77]W. Fischler and L. Susskind, “A WORMHOLE CATASTROPHE,” Phys. Lett. B 217 (1989) 48–54.
[78]W. Fischler, I. R. Klebanov, J. Polchinski, and L. Susskind, “Quantum Mechanics of the Googolplexus,”
Nucl. Phys. B 327 (1989) 157–177.
[79]J. J. Halliwell, “Derivation of the Wheeler-De Witt Equation from a Path Integral for Minisuperspace
Models,” Phys. Rev. D 38 (1988) 2468.
[80]E. Witten, “Duality and Axion Wormholes,” arXiv:2601.01587 [hep-th].
[81]V. Ivo and H. Tang, “One-loop aspects of de Sitter axion wormholes,” arXiv:2603.02335 [hep-th].
[82]R. M. Wald, “Asymptotic behavior of homogeneous cosmological models in the presence of a positive
cosmological constant,” Phys. Rev. D 28 (1983) 2118–2120.
[83]A. A. Starobinsky, “Isotropization of arbitrary cosmological expansion given an effective cosmological
constant,” JETP Lett. 37 (1983) 66–69. [Pisma Zh. Eksp. Teor. Fiz. 37, 55 (1983)].
[84]S. B. Giddings and A. Strominger, “Axion Induced Topology Change in Quantum Gravity and String Theory,”
Nucl. Phys. B 306 (1988) 890–907.
[85]S. W. Hawking, “Wormholes in Space-Time,” Phys. Rev. D 37 (1988) 904–910.
[86]S. B. Giddings and A. Strominger, “Baby Universes, Third Quantization and the Cosmological Constant,”
Nucl. Phys. B 321 (1989) 481–508.
[87]G. V. Lavrelashvili, V. A. Rubakov, and P. G. Tinyakov, “Disruption of Quantum Coherence upon a Change in
Spatial Topology in Quantum Gravity,” JETP Lett. 46 (1987) 167–169.
[88]J. M. Charap and M. J. Duff, “Space-Time Topology and a New Class of Yang-Mills Instanton,” Phys. Lett. B
71 (1977) 219–221.
[89]J. M. Charap and M. J. Duff, “Gravitational Effects on Yang-Mills Topology,” Phys. Lett. B 69 (1977)
445–447.
[90]A. Hosoya and W. Ogura, “Wormhole Instanton Solution in the Einstein Yang-Mills System,” Phys. Lett. B 225
(1989) 117–120.
[91]A. K. Gupta, J. Hughes, J. Preskill, and M. B. Wise, “Magnetic Wormholes and Topological Symmetry,” Nucl.
Phys. B 333 (1990) 195–220.
[92]S.-J. Rey, “Space-time Wormholes With Yang-Mills Fields,” Nucl. Phys. B 336 (1990) 146–156.
[93]V. de Alfaro, S. Fubini, and G. Furlan, “A New Classical Solution of the Yang-Mills Field Equations,”
Phys. Lett. B 65 (1976) 163–166.
[94]S. R. Coleman, “The Uses of Instantons,” Subnucl. Ser. 15 (1979) 805.
[95]T. Hertog, O. Janssen, and J. Karlsson, “Kontsevich-Segal criterion in the no-boundary state constrains
anisotropy,” Phys. Rev. D 111 no. 4, (2025) 046008, arXiv:2408.02652 [hep-th].
[96]T. Hertog, O. Janssen, and J. Karlsson, “Kontsevich-Segal Criterion in the No-Boundary State Constrains
Inflation,” Phys. Rev. Lett. 131 no. 19, (2023) 191501, arXiv:2305.15440 [hep-th].
[97]J.-L. Lehners, “Allowable complex metrics in minisuperspace quantum cosmology,” Phys. Rev. D 105 no. 2,
(2022) 026022, arXiv:2111.07816 [hep-th].
[98]J. Caminiti and A. Herderschee, “Inner Horizon Saddles and a Spectral KSW Criterion,” arXiv:2605.08335
[hep-th].
