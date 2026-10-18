# Outline of: AdS from CFT for scalar QED

Abstract:

We construct an explicit bulk dual in anti-de Sitter space, with couplings of order $1/N$, for the $SU(N)$-singlet sector of QED in $d$ space-time dimensions ($2 < d < 4$) coupled to $N$ scalar fields. We begin from the bulk dual for the theory of $N$ complex free scalar fields that we constructed in our previous work, and couple this to $U(1)$ gauge fields living on the boundary in order to get the bulk dual of scalar QED (in which the $U(1)$ gauge fields become the boundary value of the bulk vector fields). As in our previous work, the bulk dual is non-local but we can write down an explicit action for it. We focus on the CFTs arising at low energies (or, equivalently, when the $U(1)$ gauge coupling goes to infinity). For $d=3$ we discuss also the addition of a Chern-Simons term for $U(1)$, modifying the boundary conditions for the bulk gauge field. We also discuss the generalization to QCD, with $U(N_c)$ gauge fields coupled to $N$ scalar fields in the fundamental representation (in the large $N$ limit with fixed $N_c$).

# [root] paper
## [intro] section: 1 Introduction and Summary
### [intro-p1] paragraph

The AdS/CFT correspondence [1, 2, 3] is an equivalence between theories of quantum gravity on asymptotically
anti-de Sitter (AdS) space in $d+1$ dimensions, and conformal quantum field theories (CFTs) in $d$ dimensions.
Since for $d \geq 2$ we do not have any non-perturbative definition of these quantum gravity theories, the
correspondence should be viewed as providing a non-perturbative definition for these theories in terms of the
corresponding quantum field theories, whenever those are known and well-understood. In many cases of the
correspondence the gravitational theories have a classical limit, in which the ratio of the Planck scale to
the radius of anti-de Sitter space goes to infinity, and which corresponds to a large $N$ limit of some sort
in the CFT side. In those cases one can test the correspondence by checking that the semi-classical expansion
on the gravity side agrees with the large $N$ limit of the corresponding field theories.

### [intro-p2] paragraph

A derivation of the AdS/CFT correspondence requires showing that the CFT can be rewritten as a quantum gravity
theory, in the sense that its $1/N$ expansion reproduces the corresponding perturbative expansion around some
gravitational solution in AdS space. While one can often test this for specific observables, providing such a
derivation for the full theory is challenging (see [4, 5, 6, 7] for some recent progress in relating free
$d=2$ symmetric orbifold CFTs to string theory on $AdS_3$). In our recent paper [8] we provided such a
derivation for the simplest case of the AdS/CFT correspondence – the duality [9] between the $U(N)$-singlet
sector of $N$ free complex scalar fields in $d$ dimensions, and a theory of higher-spin gravity on
$AdS_{d+1}$. Our derivation in [8] followed the methods of bi-local holography [10, 11, 12, 13, 14, 15], in
its Lorentz-invariant version. We first changed variables in the CFT from the $N$ free scalar fields
$\phi_I(x)$ ($I=1,\cdots,N$) to their bi-local combinations

\[ G(x_1,x_2) \equiv {1\over N} \sum_{I=1}^N \phi_I^*(x_1) \phi_I(x_2), \]

(1.1)

which capture all the information about $U(N)$-invariant observables in the theory (at least in flat space).
In the large $N$ expansion one can write down an action for $G(x_1,x_2)$ that reproduces the correlators of
the original theory, to all orders in $1/N$ (as discussed in [8], the mapping to the bi-local variables makes
sense also for finite $N$ but it is more subtle then, and in this paper we only discuss the theory in the
$1/N$ expansion). In order to map this to a theory in AdS space, we first expanded the bi-local field
$G(x_1,x_2)$ in a basis of eigenstates of the Euclidean conformal group $SO(d+1,1)$. We then showed that the
same eigenstates appear in the expansion of transverse traceless fields $\Phi_J(x,z)$ of spin $J$
($J=0,1,2,\cdots$) living on a fixed $AdS_{d+1}$ space, enabling a one-to-one mapping between these fields and
the bi-local (1.1). Using this mapping we rewrote the action of the original theory as an action (with
coupling $1/N$) for fields in AdS space. This action is explicitly known but is non-local. For a specific
choice of the undetermined coefficients appearing in the mapping, the quadratic term in the bulk can be chosen
to be local. Since the $U(N)$-singlet sector of $N$ free scalars is conjectured [9] to be dual to Vasiliev’s
high-spin gravity theory [16, 17, 18], we believe that our action is equivalent to a gauge-fixed version of
this theory, in which its fields live on a fixed AdS space-time (as in [19]); the spectrum of physical fields
is consistent with this, but the equivalence has not yet been shown.

### [intro-p3] paragraph

In this paper, we generalize this construction to the $SU(N)$-singlet sector of scalar QED – the theory of a
$U(1)$ gauge field minimally coupled to $N$ charged scalar fields, for $2 < d < 4$. In principle this
generalization is straightforward, since on the field theory side it just involves introducing a dynamical
$U(1)$ gauge field and coupling it to $SU(N)$-singlet combinations of the scalar fields, and we can in
principle do this also on the gravity side. On-shell, local $SU(N)$-invariant operators (such as the ones
appearing in the coupling to the gauge field) map to the boundary values of the bulk fields on AdS space;
however, the construction above requires the off-shell mapping of the local CFT operators to the bulk, and at
first sight this seems to be more complicated. In [8] we showed that for $J=0$ and $d<4$ the naive on-shell
mapping works also off-shell, and we used it there to derive the dual to the critical $U(N)$ (or $O(N)$)
vector model, by coupling a singlet $\sigma(x)$ to the spin $J=0$ operator $\phi_I(x) \phi_I(x)$. In this
paper we show that the same is true also for $J=0$ and $d>4$, and also for higher values of $J$. This allows
us to write down a simple action for the $d$-dimensional $U(1)$ gauge field coupled to the bulk fields; in
fact, as may have been expected [20, 21, 22, 23, 24], the $U(1)$ gauge field becomes simply the boundary value
of the $(d+1)$-dimensional vector field $\Phi_1(x,z)$. Thus, compared to the original theory of $N$ free
scalars, the description of QED just involves changing the boundary condition for the bulk vector field
$\Phi_1$, and perhaps adding some boundary terms for it. The boundary terms are required if one wants to
describe QED at finite coupling, but they disappear in the low-energy limit, where QED (for $2 < d < 4$) flows
to a conformal field theory (at least at large $N$ and to all orders in $1/N$ [25], and perhaps also for all
finite values of $N$ [26, 27]). In the special case of $d=3$ one can also add a Chern-Simons coupling at level
$k$; when $k/N$ is kept fixed in the large $N$ limit, this coupling is translated into a modified boundary
condition for the bulk vector field.

### [intro-p4] paragraph

One application of our bulk formalism for QED would be to find classical solutions in the bulk describing
monopole operators, and perhaps to use them to compute their correlation functions. As we discuss below, our
formalism only includes monopole operators if there is no Chern-Simons coupling for the $U(1)$, and it may be
interesting to look for ways to get around this problem so that monopoles in Chern-Simons-matter theories may
also be incorporated.

### [intro-p5] paragraph

We also generalize our construction to the $SU(N)$ singlet sector of $N$ scalar fields in the fundamental
representation of a $U(N_c)$ gauge field (“scalar QCD" [28]), when $N_c$ is kept fixed in the large $N$ limit,
and for $d=3$ we can again include a Chern-Simons level $k$. The bulk dual is very similar to the $N_c=1$ QED
case, except the bulk fields now transform in the adjoint representation of $U(N_c)$. Note that this limit is
different from the large $N_c,k$ and fixed $\lambda\equiv N_c/k$ limit considered in [29], which is believed
to also be dual to a parity breaking higher spin bulk theory. It would be interesting to see if the
generalization of our construction to this limit just involves changing boundary conditions, or explicitly
changes the bulk interaction terms as a function of $\lambda$ (see discussions in [30, 23]). Such a
generalization, as well as the inclusion of fermions, would allow us to similarly construct the bulk dual of
ABJ theory [31] in its higher spin limit, which could ultimately lead to a connection to string theory and
M-theory via the ABJ triality [23, 32].

### [intro-p6] paragraph

Finally, our off-shell mapping allows us to construct the bulk dual for the critical $U(N)$ or $O(N)$ vector
model for $4<d<6$, as discussed in [33, 34]. This CFT is not unitarity at finite $N$ due to complex large $N$
instantons [35], but is unitary in the $1/N$ expansion. It would be interesting to study the classical
solutions corresponding to these instantons from the bulk perspective using our construction.

### [intro-p7] paragraph

We begin in section 2 by describing the $SU(N)$-singlet sector of scalar QED in bi-local variables, and
translating its action to these variables. In section 3 we review the mapping found in [8] between the free
scalar theory and the bulk, and extend it to an off-shell mapping for local operators in the CFT. In section 4
we then use this mapping to construct the bulk dual for the $SU(N)$-singlet sector of scalar QED, and show
that it reproduces the $1/N$ expansion of this theory. Finally, in section 5 we discuss the generalization to
scalar QCD.

## [sec-QED_bilocal] section: 2 Scalar QED in the bi-local formalism
### [sec-QED_bilocal-p1] paragraph

We begin in this section by discussing QED with $N$ charged scalars in the bi-local formalism. First we will
discuss scalar QED in the usual local formalism in a general dimension $2<d<4$, as well as in $d=3$ where we
can add a $U(1)$ Chern-Simons term with level $k$. We will then review how in $d=3$ one can realize the
restriction to $SU(N)$-singlet fields in a local fashion, by coupling to a non-Abelian $U(N)$ Chern-Simons
theory at level $k'$ and taking $k'\to\infty$, before coupling to the $U(1)$ gauge field of QED. Finally, we
will write the path integral for the $SU(N)$-singlet sector of scalar QED in the bi-local language, following
the discussion of free scalars in [10, 36], and perform a saddle point expansion at large $N$. In the 3d case
we fix $\kappa=k/N$ to be finite in the large $N$ limit.

### [sec-local_QED] section: 2.1 The local formalism
#### [sec-local_QED-p1] paragraph

We begin by discussing the conventional local formalism for QED with $N$ complex scalars $\phi^I$ on Euclidean
$\mathbb{R}^d$ for $2<d<4$, following [37, 38, 39, 40]. The actions for this theory can be assembled by
starting with the (Euclidean) free theory action

\[ \begin{split} 
  \mathcal{S}_\text{free}[\phi]=\int d^dx\partial_i\phi^*_I(x) \partial_i\phi^I(x)\,,
  \end{split} \]

(2.1)

where all repeated indices are summed, including the upper/lower $I=1,\cdots,N$ indices for the
fundamental/anti-fundamental of the $U(N)$ global symmetry, and the $i=1,\cdots,d$ index for the $SO(d)$
Euclidean rotations. We can then gauge the $U(1)$ subgroup by adding a Maxwell term with scalar couplings:

\[ \begin{split} 
  \mathcal{S}_e[\phi,A]=\int d^dx\Bigg[\frac{1}{4e^2}F_{ij}F_{ij}+J_i[\phi]\frac{A_i}{\sqrt{N}}+\frac{A_i
A_i}{N}\phi_I^*\phi^I\Bigg]\,,\quad J_i[\phi]\equiv i(\phi_I^*\partial_i\phi^I-\phi^I\partial_i\phi_I^*)\,,
  \end{split} \]

(2.2)

where $A_i$ is a $U(1)$ gauge field with field strength $F_{ij}$, the $U(1)$ current is $J_i$, the seagull
term is required by gauge-invariance, and we rescaled $e^2\to e^2/N$ and $A_i \to A_i /\sqrt{N}$ for later
convenience in the large $N$ limit. This action retains the $SU(N)$ subgroup of the original $U(N)$ global
symmetry, and also has a new $(d-3)$-form $U(1)_T$ global symmetry generated by the Hodge dual field strength
$* F$ [41, 42]. The $\phi^I$ are uncharged under $U(1)_T$, but we can couple it to codimension-3 operators,
which in $d=3$ become local operators called monopole operators [43]. Finally, we should add a quartic
coupling $\frac{\lambda}{4N}(\phi^*_I\phi^I)^2$, which can be equivalently written by using a Hubbard-
Stratonovich field $\sigma$ as

\[ \begin{split} 
 \mathcal{S}_{\lambda}[\phi,\sigma]=\int
d^dx\Bigg[-\frac{1}{4\lambda}\sigma^2+\frac{1}{2\sqrt{N}}\sigma\phi_I^*\phi^I\Bigg]\,,
  \end{split} \]

(2.3)

where integrating out $\sigma$ recovers the $\frac{\lambda}{4N}(\phi^*_I\phi^I)^2$ term. The most general UV
action for a $U(1)$ gauge theory coupled to $N$ complex scalars with relevant couplings in $2<d<4$ is then
given by $\mathcal{S}_\text{free}+ \mathcal{S}_e+\mathcal{S}_{\lambda}$, as well as a mass term (which we will
always fine-tune to have vanishing mass at low energies). This theory is believed to flow in the IR to an
interacting CFT called the $\mathbb{CP}^{N-1}$ or Abelian Higgs model1:

\[ \begin{split} 
\mathcal{S}_{\mathbb{CP}^{N-1}}[\phi,A,\sigma]\equiv\mathcal{S}_\text{free}[\phi]+
\mathcal{S}_{e\to\infty}[\phi,A]+\mathcal{S}_{\lambda\to\infty}[\phi,\sigma]\,,
 \end{split} \]

(2.4)

where $e,\lambda\to\infty$ since the Maxwell term is irrelevant while $(\phi^*_I\phi^I)^2$ is relevant (near
the free UV fixed point).2 In $d=3$, we can generalize this CFT by adding a level $k$ Chern-Simons term

\[ \begin{split} 
 \mathcal{S}_{k}[A]=-\int d^3x\frac{ik}{4\pi N}\varepsilon_{ijl}A_i\partial_j A_l\,,
  \end{split} \]

(2.5)

where $k\in\mathbb{Z}$ (recall that we rescaled the gauge field by a factor of $\sqrt{N}$). Note that this
term is marginal in 3d, unlike the Maxwell term which dropped out for $e\to\infty$.

#### [sec-local_QED-p2] paragraph

In general the fixed point written above is strongly coupled, but it becomes weakly coupled at large $N$, and
it can be studied perturbatively in a $1/N$ expansion. We begin by writing down the Feynman rules for this
expansion. The propagator for $\phi^I$ is

\[ \begin{split} 
 G_0(x_1,x_2)=\frac{\Gamma(d/2-1)}{4\pi^{d/2}}\frac{1}{|x_1-x_2|^{d-2}}\,.
  \end{split} \]

(2.6)

For $\sigma$, we have the momentum space $\sigma$ propagator and the one-loop correction from the $\phi^2$
bubble diagram

\[ \begin{split} 
D_{\sigma}(p)=-2\lambda\,,\qquad \mathbb{B}_{\phi^2}(p)= -|p|^{d-4}\frac{
        2^{1-2d}\pi^{\frac{3-d}{2}}}{\Gamma(\frac{d-1}{2})\sin(\frac{\pi d}{2})}\,,
 \end{split} \]

(2.7)

where the former comes from the trivial quadratic term $\sigma^2$, while the latter comes from the
$\frac{1}{2\sqrt{N}}\sigma \phi_I^*\phi^I$ vertex and is simply $G_0(x,0)^2/4$ in momentum space. Since both
are $O(N^0)$, at leading order in $1/N$ we need to resum an infinite geometrical series of bubble diagrams to
obtain the effective $\sigma$ propagator (see Figure 1)

\[ \begin{split} 
\langle\sigma(x)\sigma(0)\rangle_\lambda=&\int \frac{d^d{p}}{(2\pi)^d}e^{ip\cdot
x}\Big[D_\sigma(p)+D_\sigma(p)\mathbb{B}_{\phi^2}(p)D_\sigma(p) +\dots\Big]+O(N^{-1})\\
=&-\int \frac{d^d{p}}{(2\pi)^d}\frac{2\lambda e^{ip\cdot x}}{1-2\lambda \frac{
        |p|^{d-4}2^{1-2d}\pi^{\frac{3-d}{2}}}{\Gamma(\frac{d-1}{2})\sin(\frac{\pi d}{2})}}+O(N^{-1})\,.
 \end{split} \]

(2.8)

In the IR CFT at $\lambda\to\infty$, this becomes the propagator of a dimension two operator:

\[ \begin{split} 
\langle\sigma(x)\sigma(0)\rangle_\infty&=\frac{2^{d+3} \sin \left(\frac{\pi  d}{2}\right) \Gamma
(\frac{d-1}{2})}{\pi^{\frac32}  \Gamma
   \left(\frac{d}{2}-2\right)}\frac{1}{|x|^4}+O(N^{-1})\,.
 \end{split} \]

(2.9)

#### [fig-bubbles1] figure: Figure 1

Figure 1. Bubble diagrams contributing to the effective $\sigma$ propagator
$\langle\sigma(x)\sigma(0)\rangle_\lambda$ at leading $O(N^0)$ order. Thick lines correspond to $\sigma$
contractions, and dashed lines to the scalars $\phi_I$.

#### [sec-local_QED-p3] paragraph

For the gauge field $A_i$, we must fix a gauge in order to write down its propagator. It is convenient to
choose a gauge such that the IR limit $e\to\infty$ can be taken immediately. As discussed in [37] for the
similar fermionic QED$_3$ case, a simple family of gauges that has this property involves an average over
different gauge-fixings, which is implemented by adding to the action the non-local gauge-fixing term

\[ \begin{split} 
\mathcal{S}_{\zeta}[A]=\begin{cases}\frac{1}{1-\zeta} \frac{\Gamma \left(\frac{d}{2}\right)^2}{8\pi^d
(d-1)(d-2)} \int d^dxd^dy\frac{\partial_i A^i(x)\partial_j A^j(y)}{|x-y|^{2d-4}}\qquad\qquad \,d\neq3\\
 \frac{1}{1-\zeta}\left(\frac{\kappa^2}{\pi^4}+\frac{1}{64\pi^2}\right) \int d^3xd^3y\frac{\partial_i
A^i(x)\partial_j A^j(y)}{|x-y|^{2}}\qquad\qquad d=3\,,\\
\end{cases}
 \end{split} \]

(2.10)

where $\kappa\equiv k/N$, and we chose a different coefficient for $d=3$ for later convenience. This arises by
averaging over different $\partial_i A^i(x) = \omega(x)$ gauges with a non-local weight proportional to
$(1-\zeta)^{-1} \int d^d x d^d y \omega(x) \omega(y) / |x-y|^{2d-4}$, where $\zeta\in\mathbb{R}$; the limit
$\zeta\to1$ recovers the usual Landau gauge $\partial_i A^i=0$. Using this gauge-fixing term, along with the
Maxwell term in (2.2), and for $d=3$ the CS term in (2.5), we can find the momentum-space gauge field
propagator

\[ \begin{split} 
D_{ij}^\text{Max}(p)=\begin{cases}\frac{e^2}{p^2}\left(\delta_{ij}-\frac{p_ip_j}{|p|^2}\right)+(1-
\zeta)\frac{2^{d-2} \pi ^{d/2}\Gamma (d)}{ \Gamma \left(2-\frac{d}{2}\right) \Gamma
   \left(\frac{d}{2}\right)^2}\frac{p_ip_j}{|p|^d}\qquad\qquad\qquad\qquad\;\;\;\, d\neq3\\
\frac{1}{\frac{p^2}{e^4}+\frac{\kappa^2}{4\pi^2}}\left[\frac{1}{e^2}\left(\delta_{ij}-
\frac{p_ip_j}{|p|^2}\right)-\frac{\kappa}{2\pi}\varepsilon_{ijl}\frac{p_l}{|p|^2}\right]+(1-
\zeta)\frac{16\pi^2}{64\kappa^2+\pi^2}\frac{p_ip_j}{|p|^3}\qquad d=3\,.
\end{cases}
 \end{split} \]

(2.11)

#### [sec-local_QED-p4] paragraph

The coupling $J_iA_i$ and the contact term $A_i^2\phi^2$ in (2.2) both contribute to the momentum space photon
self-energy at one-loop order

\[ \begin{split} 
\mathbb{B}_{ij}(p)&=\int
\frac{d^dk}{(2\pi)^d}\left[-\frac{2\delta_{ij}}{|k|^2}+\frac{(2k+p)_i(2k+p)_j}{|k+p|^2|k|^2}\right]\\
&=-\frac{ \Gamma \left(2-\frac{d}{2}\right) \Gamma
   \left(\frac{d}{2}\right)^2}{2^{d-2} \pi ^{d/2}\Gamma (d)} |p|^{d-2}
\left(\delta_{ij}-\frac{p_ip_j}{|p|^2}\right)\,,
 \end{split} \]

(2.12)

where we see that the only role of the $A_i^2\phi^2$ term is to cancel a divergence in the contribution of the
$J_iA_i$ term. As with $\sigma$, at leading order in $1/N$ we need to resum an infinite geometric series of
bubble diagrams to find the effective photon propagator (see figure 2)

\[ \begin{split} 
&\langle A_i(x)A_j(0)\rangle_{\zeta,e,k}=  \int\frac{d^dp}{(2\pi)^d}  e^{ip\cdot
x}\left[D_{ij}^\text{Max}(p)+D_{ik}^\text{Max}(p)
\mathbb{B}_{kl}(p)D_{lj}^\text{Max}(p)+\dots\right]+O(N^{-1})\\
&= \begin{cases}\int\frac{d^dp}{(2\pi)^d}  e^{ip\cdot x}\Bigg[\frac{e^2
\left(\delta_{ij}-\frac{p_ip_j}{|p|^2}\right)}{|p|^2+\frac{ \Gamma \left(2-\frac{d}{2}\right) \Gamma
   \left(\frac{d}{2}\right)^2}{2^{d-2} \pi ^{d/2}\Gamma (d)} \frac{e^2}{|p|^{2-d}}}+\frac{2^{d-2} \pi
^{d/2}\Gamma (d)}{ \Gamma \left(2-\frac{d}{2}\right) \Gamma
   \left(\frac{d}{2}\right)^2}(1-\zeta)\frac{p_ip_j}{|p|^d}\Bigg]+O(N^{-1})\qquad d\neq3\\
\int\frac{d^3p}{(2\pi)^3}  \frac{e^{ip\cdot x}}{|p|}\Bigg[\frac{(\frac{1}{16}+\frac{|p|}{e^2})\left(\delta_{ij
}-\frac{p_ip_j}{|p|^2}\right)-
\frac{\kappa}{2\pi}\varepsilon_{ijl}\frac{p_l}{|p|}}{\left(\frac{1}{16}+\frac{|p|}{e^2}\right)^2+\frac{\kappa^
2}{4\pi^2}}+\frac{16}{1+\frac{64\kappa^2}{\pi^2}}({1-\zeta})\frac{p_ip_j}{|p|^2}\Bigg]
+O(N^{-1})\quad\quad\;\; \,d=3\,,
\end{cases}
  \end{split} \]

(2.13)

where the $k$ label is only there for $d=3$. In the IR CFT at $e\to\infty$ the expression simplifies and we
obtain the momentum space propagator

\[ \begin{split} 
\langle A_i(p)A_j(-p)\rangle_{\zeta,\infty,k}&=\begin{cases} \frac{1 }{|p|^{d-2}} \frac{2^{d-2} \pi
^{d/2}\Gamma (d)}{ \Gamma \left(2-\frac{d}{2}\right) \Gamma
   \left(\frac{d}{2}\right)^2}\left(\delta_{ij}-\zeta\frac{p_ip_j}{|p|^2}\right)+O(N^{-1})\qquad\quad
\,d\neq3\\
  \frac{1}{|p|}\frac{16\left(\delta_{ij}-\zeta\frac{p_ip_j}{|p|^2}\right)-
\frac{128\kappa}{\pi}\varepsilon_{ijl}\frac{p_l}{|p|}}{1+\frac{64\kappa^2}{\pi^2}} +O(N^{-1})\qquad\qquad\;\;
\,\;\;d=3
\end{cases}\\
  \end{split} \]

(2.14)

from which we can go to position space to get

\[ \begin{split} 
\langle A_i(x)A_j(0)\rangle_{\zeta,\infty,k}&=\begin{cases}\frac{\Gamma (d)}{2 \Gamma
\left(2-\frac{d}{2}\right) \Gamma
\left(\frac{d}{2}\right)^3}\frac{(d-2-\zeta)\delta_{ij}+2\zeta\frac{x_ix_j}{|x|^2}}{|x|^2}
+O(N^{-1})\qquad\qquad\qquad\; \;\;d\neq3\\
\frac{8}{\pi^2+{64\kappa^2}}\frac{1}{|x|^2}\left({(1-
\zeta)\delta_{ij}+2\zeta\frac{x_ix_j}{|x|^2}}+\frac{\kappa}{4}\varepsilon_{ijl}\frac{x_l}{|x|}\right)
+O(N^{-1})\quad d=3\,.
\end{cases}
  \end{split} \]

(2.15)

Note that the choice of gauge in (2.10) allowed us to take $e\to\infty$ in the propagator, while other gauge
choices such as $R_\xi$ gauge would give superficial divergences in this limit, which would only cancel after
computing gauge-invariant observables.

#### [fig-bubbles2] figure: Figure 2

Figure 2. Bubble diagrams contributing to the effective photon propagator $\langle
A_i(x)A_j(0)\rangle_{\zeta,e,k}$ at leading $O(N^0)$ order. Squiggly lines correspond to photon contractions
$D^\text{Max}_{ij}$, and dashed lines to the scalars $\phi_I$.

#### [sec-local_QED-p5] paragraph

Using these Feynman rules including the resummed propagators, we can compute correlation functions in scalar
QED, in an expansion in $1/N$ similar to the large $N$ expansion of vector models.

### [restrict] section: 2.2 A subtlety in restricting to the singlet sector
#### [restrict-p1] paragraph

We will be interested in the $SU(N)$ singlet sector of scalar QED. In general $d$, we can simply restrict to
this sector by hand, which has no nontrivial effects on $\mathbb{R}^d$. For $d=3$ and non-zero $k$, we need to
be more careful. What we actually do is first restrict the theory of $N$ scalars to its $U(N)$-invariant
sector, and then couple this sector to the $U(1)$ gauge field. We can perform the restriction in a rigorous
way [44] by coupling the theory to a $U(N)$ Chern-Simons term at infinite level before coupling to the new
$U(1)$ gauge field, and we will use this to show that monopole operators cannot appear in the singlet sector
(as we define it here) when $k\neq0$. Thus, for $d=3$ and non-zero $k$ our theory is not precisely the same as
the $SU(N)$-singlet sector of scalar QED (which could have $SU(N)$-singlet monopole operators), but we will
still call it by this name. In all other cases our theory includes the full $SU(N)$-singlet sector of scalar
QED.

#### [restrict-p2] paragraph

Let us start by considering the free theory with action $\mathcal{S}_\text{free}$ in $d=3$, with global
symmetry $U(N)$. We can gauge this $U(N)$ by adding a $U(N)_{k'}$ Chern-Simons term for a gauge field $B_i$,
with scalar couplings:

\[ \begin{split} 
  \mathcal{S}_{k'}&=\int d^3x\left[-\frac{ik'}{4\pi}\varepsilon_{ijl}(B_i{}^I_J\partial_jB_l{}^J_I-
\frac{2i}{3}B_i{}_I^JB_j{}_J^KB_l{}_K^I)+J_i{}_I^JB_i{}_J^I+B_i{}_I^J B_i{}_J^I\phi_K^*\phi^K\right]\,\\
  &=\int
d^3x\left[-\frac{iNk'}{4\pi}\varepsilon_{ijl}B_i\partial_jB_l+J_iB_i+NB_iB_i\phi^*_I\phi^I+\text{$SU(N)$
terms}\right]\,,\\
  \end{split} \]

(2.16)

where $B_i{}^{I}_J$ is the $U(N)$ gauge field, $J_i{}_I^J\equiv
i(\phi_I^*\partial_i\phi^J-\phi^J\partial_i\phi_I^*)$ is the $U(N)$ current, and in the second line we
separated out the $SU(N)\subset U(N)$ terms from the $U(1)$ gauge field $B_i\equiv \frac{B_i{}_I^I}{N}$, which
couples to the $U(1)$ current $J_i$ defined in (2.2). The gauge-invariant operators are then all singlets of
$U(N)$, as we want, but the theory is modified by the extra $B_i$ fields, and in particular it has new
monopole operators charged under a topological $U(1)_{T'}$ global symmetry generated by the dual of the field
strength of $B_i$. We can then take the $k'\to\infty$ limit, which on $\mathbb{R}^3$ removes all dynamical
effects of the gauging, including the existence of monopoles charged under the $U(1)_{T'}$, and we obtain
precisely the desired restriction to $U(N)$ singlets.

#### [restrict-p3] paragraph

From the $U(N)$-singlet sector of the free theory, we can then get the theory we are interested in (the
$SU(N)$-singlet sector of scalar QED at level $k$) by adding $\mathcal{S}_{e\to\infty}$, $\mathcal{S}_k$, and
$\mathcal{S}_{\lambda\to\infty}$ as discussed before. For $k\neq0$, monopole operators (charged under
$U(1)_T$) carry $k$ units of the gauge $U(1)$ charge, and so to be gauge-invariant under the $A$ gauging,
monopoles needs to be dressed by composites of $\phi^I$ that will cancel their $U(1)$ charge. But then the
dressed monopoles would also be charged under the original $B$ gauging due to the dressing. Thus, our theory
includes no gauge-invariant monopoles for $k\neq0$. For $k=0$, the monopole operators of QED are uncharged
under $U(1)$, so they are allowed. Similarly for $d\neq3$ where we have no Chern-Simons terms, the
codimension-3 monopole operators discussed above are also allowed.

### [sec-bilocal_QED] section: 2.3 The bi-local formalism
#### [sec-bilocal_QED-p1] paragraph

We will now show how the singlet sector discussed above can be usefully described in terms of bi-local
variables, which can then be naturally translated into the bulk in the later sections. We start by reviewing
the bi-local formalism for the free theory with action $\mathcal{S}_\text{free}$ in (2.1) following [8, 10,
36, 15]. All $U(N)$ invariants of $N$ free scalars can be written in terms of the bi-local field (1.1). We can
then change variables in the path integral from $\phi^I$ to $G$ to get the partition function

\[ \begin{split} 
        Z = \int DG(x_1,x_2) \exp(-\mathcal{S}_\text{free}[G]-\mathcal{S}_\text{Jac}[G])\,,\qquad
\mathcal{S}_\text{Jac}=-(N-V)\text{Tr}(\log(G))\,,
 \end{split} \]

(2.17)

where we regularized the path integral by placing our field theory on a lattice of $V$ points, such that
$G(x_1,x_2)$ is a Hermitian $V\times V$ matrix, and $\mathcal{S}_\text{Jac}$ is the non-trivial Jacobian (we
drop all factors that do not depend on $G$). Note that (2.17) is only correct for $N\geq V$, which applies to
the large $N$ expansion we consider in this paper, while for $N<V$ $G(x_1,x_2)$ must obey complicated non-
linear constraints. The continuum limit is reached by taking $V\to\infty$, in which case matrix traces become
continuum integrals as ${\rm Tr}(G) \equiv \int d^d x G(x,x)$ and $(GH)(x_1,x_2) \equiv \int d^d x_3
G(x_1,x_3) H(x_3,x_2)$. In particular, the continuum $\mathcal{S}_\text{free}[G]$ may be written as

\[ \begin{split} 
 \mathcal{S}_\text{free}[G]=N\int d^dx_1 \partial_{1,i} \partial_{2,i}G(x_1,x_2)\vert_{x_2=x_1}\,.
 \end{split} \]

(2.18)

Since both $\mathcal{S}_\text{free}[G]$ and the Jacobian include terms proportional to $N$, we can perform a
$1/N$ saddle point expansion by taking the large $N$ limit first, where all physical observables should be
independent of the regularization parameter $V$. In particular, we expand $G$ around its large $N$ saddle
point values given by the propagator $G_0(x_1,x_2)$ in (2.6) as

\[ \begin{split} 
        G(x_1,x_2)= G_{0}(x_1,x_2)+\frac{1}{\sqrt{N}}\eta(x_1,x_2)\,.
 \end{split} \]

(2.19)

The free bi-local action (2.17) in terms of the fluctuation $\eta$ now gives (up to additive constants)

\[ \begin{split} 
\mathcal{S}_\text{free}[\eta]={\sqrt{N}}\text{Tr}\left( G_{0}^{-1}\eta\right)\,,
 \end{split} \]

(2.20)

and

\[ \begin{split} 
 \mathcal{S}_\text{Jac}[\eta]&=-\left(N-V\right)\log\left(1+\frac{1}{\sqrt{N}} G_{0}^{-1}\eta\right)\\
 &=-\sum_{n=1}^{\infty}\frac{\left(-1\right)^{n+1}}{n}N^{1-\frac{n}{2}}\text{Tr}\left(\left( G_{0}^{-
1}\eta\right)^{n}\right)-V\sum_{n=1}^{\infty}\frac{\left(-1\right)^{n}}{n}N^{-
\frac{n}{2}}\text{Tr}\left(\left( G_{0}^{-1}\eta\right)^{n}\right)\,,
 \end{split} \]

(2.21)

where we expanded in large $N$. Note that the first $n=1$ term cancels the linear
$\mathcal{S}_\text{free}[\eta]$ as we expect from a saddle point solution. We can then write down Feynman
rules where the propagator is given by the $n=2$ bare term in (2.21), and we have bare $n$-point vertices for
$n\geq3$, as well as counterterm (multiplied by $V$) $n$-point vertices for $n\geq1$. As shown in [8], these
Feynman rules lead to the expected correlation functions for the free theory.

#### [sec-bilocal_QED-p2] paragraph

We can extend the bi-local formalism to QED by simply writing all $\phi$-dependent terms in the actions we
wrote above using $G$ as

\[ \begin{split} 
\mathcal{S}_e[G,A]&=\int d^dx\Bigg[\frac{1}{4e^2}F_{ij}^2(x)+J_i[G]A_i(x)+A_i^2(x)G(x,x)\Bigg] \,,\\
 \mathcal{S}_{\lambda}[G,\sigma]&=\int
d^dx\Bigg[-\frac{1}{4\lambda}\sigma^2(x)+\frac{\sqrt{N}}{2}\sigma(x)G(x,x)\Bigg]\,,\\
 \end{split} \]

(2.22)

where we write the $U(1)$ current in terms of $G$ as $J_i[G]\equiv
i{\sqrt{N}}(\partial_{2,i}-\partial_{1,i})G(x_1,x_2)\vert_{x_2=x_1}$. Note that $\mathcal{S}_\text{Jac}[G]$ is
gauge-invariant by itself, and then gauge-invariance of the other terms works exactly the same as in the
$\phi$ language. We would like to now expand $G$ around $G_0$ in (2.6) (which is not gauge-invariant, but is
still a saddle point in the gauge-fixing that we perform as described above) to get

\[ \begin{split} 
\mathcal{S}_e[\eta,A]&=\int d^dx\Bigg[\frac{1}{4e^2}F_{ij}^2(x)+J_i[\eta]A_i(x)+J_i[G_0]A_i(x)+\frac{{A_i^2}(x
)\eta(x,x)}{\sqrt{N}}+A_i^2(x)G_0(x,x)\Bigg] \,,\\
 \mathcal{S}_{\lambda}[\eta,\sigma]&=\int d^dx\Bigg[-
\frac{1}{4\lambda}\sigma^2(x)+\frac{1}{2}\sigma(x)\eta(x,x)+\frac{\sqrt{N}}{2}\sigma(x)G_0(x,x)\Bigg]\,,\\
 \end{split} \]

(2.23)

where $J_i[\eta]\equiv i(\partial_{2,i}-\partial_{1,i})\eta(x_1,x_2)\vert_{x_2=x_1}$. This includes divergent
terms involving $G_0(x,x)$ and its derivatives, which are not regularized by the lattice regulator used so
far. For $S_\lambda$, we can cancel $\sigma(x)G_0(x,x)$ at each order with a linear term in $\sigma$ (or,
equivalently, with a mass counterterm). For $S_e$, we expect that $J_i[G_0]=0$ in any Lorentz-invariant
regularization3. In the following, we will simply drop the divergent terms that can be cancelled in these
ways, and thus define

\[ \begin{split} 
\mathcal{S}_e[\eta,A]&\equiv\int d^dx\Bigg[\frac{1}{4e^2}F_{ij}^2(x)+J_i[\eta]A_i(x)+\frac{{A_i^2}(x)\eta(x,x)
}{\sqrt{N}}+A_i^2(x)G_0(x,x)\Bigg] \,,\\
 \mathcal{S}_{\lambda}[\eta,\sigma]&\equiv\int
d^dx\Bigg[-\frac{1}{4\lambda}\sigma^2(x)+\frac{1}{2}\sigma(x)\eta(x,x)\Bigg]\,.\\
 \end{split} \]

(2.25)

Note that we have kept the counterterm $A_i^2(x)G_0(x,x)$ in the action, because it is needed to cancel the
divergence in the contribution of $J_i[\eta]A_i$ to the photon self energy. In particular, $A_i^2(x)G_0(x,x)$
contributes the first divergent term in (2.12), while $J_i[\eta]A$ contributes the second term. The
$\frac{{A_i^2}(x)\eta(x,x)}{\sqrt{N}}$ term does not contribute at leading order in $1/N$, but will contribute
at sub-leading orders. In fact, for the $\mathbb{CP}^{N-1}$ model (2.4) we can make the field redefinition
(after gauge-fixing) $\sigma(x)\mapsto \sigma(x) - \frac{2 A_i^2(x)}{\sqrt{N}}$ which cancels
$\frac{{A_i^2}(x)\eta(x,x)}{\sqrt{N}}$ entirely (for $\lambda \to \infty$). In this way the Feynman diagrams
of the theory can be packed in terms of the effective $\sigma$ and $A$ propagators in (2.9) and (2.13),
respectively.

#### [sec-bilocal_QED-p3] paragraph

Our action is written in a specific gauge choice discussed above, using the non-gauge-invariant bi-local
variable $\eta(x_1,x_2)$. In order to construct gauge-invariant variables, we need to look at the limit $x_2
\to x_1$ of $\eta(x_1,x_2)$ to obtain gauge-invariant local operators, or alternatively to dress $G(x_1,x_2)$
with a Wilson line between $x_1$ and $x_2$. We can also compute correlation functions of $\eta(x_1,x_2)$’s
using our gauge-fixed action, but generally these are not meaningful, because we are averaging over different
gauge choices in which $G(x_1,x_2)$ corresponds to different operators4.

## [sec-map] section: 3 The AdS/CFT map
### [sec-map-p1] paragraph

In this section, we discuss the exact AdS/CFT map that we will use in the next section to write down the bulk
dual of the $SU(N)$-singlet sector of scalar QED. We start by reviewing the off-shell AdS/CFT map derived in
[8], which naturally acts on the CFT bi-local $\eta(x_1,x_2)$. We will then show how this map implies that
local single-trace operators of any spin $J$ in any dimension $d$ also map off-shell to the bulk in a simple
way, generalizing the $d<4$ and $J=0$ case proven in [8]. For $J=1$, this off-shell map will then be used to
write the bulk dual of scalar QED in the next section.

### [sec-review] section: 3.1 Review of the bi-local map
#### [sec-review-p1] paragraph

We begin by briefly reviewing the AdS/CFT map of the free scalar theory [8]. The map is given by expanding the
bi-local fluctuation $\eta( x_1 , x_2)$ on one side, and the spin $J$ transverse traceless AdS fields
$\Phi_J(x,z)$ on the other side, in terms of the same irreducible representations (labeled by $\Delta,J,y$) of
the conformal group, so that the exact map between $\eta( x_1 , x_2)$ to $\Phi_J(x,z)$ is given by the
convolution of the basis elements in each space.5

#### [fg-Delta_contour] figure: Figure 3

Figure 3. The deformation of the contour $\gamma_0$ from the principal series $\text{Re}(\Delta)=\frac{d}{2}$
to include $\Delta=2\Delta_0$ and exclude $d-2\Delta_0$, when $2\Delta_0<d/2$. In general we should deform the
contour $\gamma_J$ for any $2\Delta_0+2n+J<\frac{d}{2}$ and $n=0,1,\cdots$.

#### [sec-review-p2] paragraph

We expand $\eta( x_1 , x_2)$ in the complete basis

\[ \begin{split} 
        \eta(x_1,x_2) = \sum_{J=0}^\infty \int_{\gamma_J}\frac{d\Delta}{2\pi i} \int d^d y  \,
C_{\Delta,J}\left(y\right)
        \thpnorm{x_1}{x_2}{\Delta,J}{y}\,,
 \end{split} \]

(3.1)

where the basis elements are “3-point functions”6 of scalar operators $\mathcal{O}_{\Delta_0}$ and
$\hat{\mathcal{O}}_{\Delta_0}$ that have the same scaling dimension $\Delta_0=\frac{d-2}{2}$ as a free scalar
field, namely

\[ \begin{split} 
        \thpnormind{x_1}{x_2}{\Delta,J}{x_3}{i_1,...,i_J} = \frac
        {Z^{i_1}...Z^{i_J}-\text{traces}}
        {x_{12}^{2\Delta_{0}-\Delta+J}x_{13}^{\Delta-J}x_{23}^{\Delta-J}}\,,
 \end{split} \]

(3.2)

where $Z^{i} \equiv \frac{x_{13}^i}{x_{13}^2}-\frac{x_{23}^i}{x_{23}^2}$, we define $x_{12}\equiv |x_1-x_2|$,
and we will in general suppress spin indices for simplicity. The contours $\gamma_J$ of the $\Delta$ integrals
in (3.1) go over the principal series $\Delta=\frac d2+is$ for real $s$, except for $J=0$ and $d<4$ where we
deform the contour as shown in Figure 3 to ensure that the pole $2\Delta_0=d-2$ of the scalar single-trace
operator in the free theory appears on the same side of the contour as the other spin $J$ single-trace
operators with scaling dimension $d-2+J$. This expansion exists when $\eta(x_1,x_2)$ satisfies the conditions

$\lim_{x_2\to x_1}\eta(x_1,x_2)$ should be finite.

At large $|x_1+x_2|$ (and fixed difference) $\eta(x_1,x_2)$ should decay.7

At large $|x_1|$ (or $|x_2|$) and fixed $x_2$ ($x_1$)

\[ \eta(x_1,x_2) \sim \left|x_{1}\right|^{-2\Delta_{0}}\cdot \text{Power series in }\ensuremath{\frac{1}{|x_1|}}\,. \]

(3.3)

$\eta(x_1,x_2)$ must be smooth.

#### [sec-review-p3] paragraph

For $d>4$,8 we can use the orthogonality and completeness relations of the 3-point basis, as reviewed in
Appendix A.1, to invert (3.1) and write $C_{\Delta,J}(y)$ in terms of $\eta(x_1,x_2)$ as

\[ \begin{split} 
d>4:\qquad      C_{\Delta,J}(y)=\frac12\frac{1}{N_{\Delta,J}}\int d^dx_{1}d^dx_{2}\,
\eta\left(x_{1},x_{2}\right)
        \thptild{x_1}{x_2}{\tilde\Delta,J}{y}\,,
 \end{split} \]

(3.4)

where the normalization $N_{\Delta,J}$ is given in (A.2), and tildes over dimensions denote
$\tilde\Delta=d-\Delta$. The shadow relation (A.5) implies that only half of the coefficients
$C_{\Delta,J}(y)$ are independent along the contour $\gamma_J$. We define the physical $C_{\Delta,J}(y)$ to
have $\text{Im}(\Delta)\geq0$, and then the shadow $C_{\tilde\Delta,J}(y)$ are related to them by

\[ \begin{split} 
        C_{\tilde \Delta,J}(y) = \frac{1}{S^{(\tilde\Delta,J)}_{\Delta_0,\Delta_0} }
        \int d^d y^\prime
        \tp{\Delta,J}{y}{y^\prime}
        C_{\Delta,J}(y^\prime)\,,
 \end{split} \]

(3.5)

where the shadow coefficient $S^{(\tilde\Delta,J)}_{\Delta_0,\Delta_0}$ is given in (A.4), and the “2-point
function” is defined as

\[ \begin{split} 
\langle\mathcal{O}_{\Delta,J}^{i_1\dots i_J}(x_1)\mathcal{O}_{\Delta,J}^{i'_1\dots
i'_J}(x_2)\rangle&=\frac{I^{i_1i'_1}(x_{12})\dotsb I^{i_Ji'_J}(x_{12})}{x_{12}^{2\Delta}}-\text{traces}\,,\\
 \end{split} \]

(3.6)

where $I^{ii'}\equiv\delta^{ii'}-2\frac{x^{i} x^{i'}}{|x|^2}$. Hermiticity of $\eta(x_1,x_2)$ then implies
that $C^*_{\Delta,J}(y)=(-1)^JC_{\tilde\Delta,J}(y)$.

#### [sec-review-p4] paragraph

For $d<4$, the integral in (3.4) does not converge. As explained in [8], we can avoid this divergence by
considering the auxiliary bi-local

\[ \begin{split} 
                \tilde\eta(x_1,x_2) =\left( \frac{\Gamma(\frac{d-2}{2})}{4\pi^{\frac{d}{2}}}\right)^2
\nabla^2_1\nabla^2_2 \eta(x_1,x_2)\,,
 \end{split} \]

(3.7)

which can be expanded in the harmonic basis as

\[ \begin{split} 
\tilde\eta(x_1,x_2) = \sum_{J=0}^\infty \int_{P.S.}\frac{d\Delta}{2\pi i} \int d^d y  \, \tilde
C_{\Delta,J}(y)
        \thptild{x_1}{x_2}{\Delta,J}{y}\,,
         \end{split} \]

(3.8)

where the contour is now the principal series for all $J$, and

\[ \begin{split} 
d<4:\qquad      \tilde C_{\Delta,J}\left(y\right)=\frac12\frac{1}{N_{\Delta,J}}\int d^dx_{1}d^dx_{2}\,
\tilde\eta\left(x_{1},x_{2}\right)
        \thpnorm{x_1}{x_2}{\tilde\Delta,J}{y}
         \end{split} \]

(3.9)

is now convergent for $d<4$, unlike (3.4). The original expansion of $\eta(x_1,x_2)$ in (3.1) still holds for
$d<4$ provided that we identify

\[ \begin{split} 
        d<4:\qquad C_{\Delta,J}(y) \equiv \frac{16\pi^d
\Gamma^2(\frac{d}{2}-\Delta_0)}{\Gamma^2(\Delta_0)\lambda_{\Delta,J}} \,
        \tilde C_{\Delta,J}(y)\,,
 \end{split} \]

(3.10)

where $\lambda_{\Delta,J}$ is the eigenvalue of the bi-local Laplacian in the conformal basis and is given for
any $d$ by

\[ \begin{split} 
\lambda_{\Delta,J}=\left(M_{\Delta,J}^{2}-M_{d+J,J}^{2}\right)\left(M_{\Delta,J}^{2}-M_{d+J-
2,J}^{2}\right)\,,\qquad M_{\Delta,J}^{2}\equiv \Delta\left(\Delta-d\right)-J\,.
 \end{split} \]

(3.11)

#### [sec-review-p5] paragraph

In AdS space we use Poincaré coordinates ($ds^2 = (dx^i dx^i + dz^2) / z^2$), and in our formalism the metric
in the bulk is fixed, with traceless transverse spin $J$ fields $\Phi_J(x,z)$ (including a spin-two graviton)
propagating on this fixed background. We define the mapping from the CFT to the bulk by expanding the bulk
fields $\Phi_J(x,z)$ in the complete basis

\[ \begin{split} 
\Phi_{J}(x,z)=\int_{\gamma_J}\frac{d\Delta}{2\pi i}\int
        d^dy
        f_{\Delta,J}C_{\Delta,J}(y)G_{\Delta,J}(x,z|y)\,,
         \end{split} \]

(3.12)

where we identified the bulk coefficient $C_{\Delta,J}(y)$ with the same coefficient appearing in the bi-local
expansion, up to a multiplicative factor $f_{\Delta,J}$ that is not fixed by conformal symmetry. This
identification implies that the contour $\gamma_J$ in (3.12) is the same as the one in the bi-local expansion.
The basis elements in (3.12) are the bulk-to-boundary propagators in AdS space, defined by the differential
equation

\[ \begin{split} 
        &(\nabla^2_{x,z} -M^2_{\Delta,J})G _{\Delta,J}(x,z|y)=  0\,,\qquad \nabla^2_{x,z} \equiv
z^{d+1}\partial_{z}\left(z^{-d+1}\partial_{z}\right)+z^{2}\nabla_x^2\,,\\
 \end{split} \]

(3.13)

and by the $z\to0$ boundary condition9

\[ \begin{split} 
        G_{\Delta,J}(x,z|y)=z^{\Delta-J}
        \langle\mathcal{O}_{\Delta,J}(x)\mathcal{O}_{\Delta,J}(y)\rangle + z^{d-\Delta-J} S_B ^{\Delta,J}
\delta_J^{TT}(x-y)+ \dots\,,
 \end{split} \]

(3.14)

where $\delta_J^{TT}(x)$ denotes a delta function with $2J$ suppressed lower indices for spin $J$ traceless
transverse functions on the boundary $\mathbb{R}^d$,10 and we define the bulk shadow coefficient

\[ \begin{split} 
        S_B^{ \Delta,J}         \equiv \frac{\pi^{\frac{d}{2}} \Gamma( \Delta-\frac{d}{2})}
        {(J+ \Delta-1)\Gamma(\Delta-1)}\,.
 \end{split} \]

(3.15)

The solution to (3.13) and (3.14) is by construction transverse

\[ \begin{split} 
\text{for $a=1,\cdots, J$}:\qquad       \nabla^{\mu_a}G^{i_1\cdots i_J}_{\Delta,J}(x,z|y)_{\mu_1\cdots
\mu_a\cdots \mu_J} = 0\,, \qquad \nabla^\mu\equiv z^{d+3}\partial^\mu z^{-d-1} \,,
 \end{split} \]

(3.16)

where $\mu=z,1,\cdots,d$ denotes bulk spin indices that we in general suppress for simplicity (we denote the
index in the radial direction by $z$, this should not be confused with the value of the radial coordinate that
we also denote by $z$). See Appendix A.2 for an explicit expression for $G_{\Delta,J}$, as well as the
orthogonality, completeness, and shadow relations.

#### [sec-review-p6] paragraph

The CFT shadow relation (A.5) and the bulk shadow relations (A.7) imply that $f_{\Delta,J}$ must satisfy the
consistency condition

\[ \begin{split} 
                \frac{f_{\Delta,J}}{f_{\tilde \Delta,J} } = \frac{S_B^{\tilde
\Delta,J}}{S^{(\tilde\Delta,J)}_{\Delta_0,\Delta_0}} =
                \frac{ \Gamma\left(\Delta+J\right)\Gamma^2\left(\frac{\tilde\Delta+J}{2}\right)}
                { \Gamma\left(\tilde\Delta+J\right)\Gamma^2\left(\frac{\Delta+J}{2}\right)}\,,
 \end{split} \]

(3.17)

where the bulk shadow coefficient is given in (3.15). The expansion (3.12) assumes that $\Phi_J(x,z)$ decays
in the small $z$ limit as $z^{\frac d2-J}$ in general. For $J=0$ and $d<4$ recall that the contour $\gamma_0$
allows the integrand to have an extra contribution at $\Delta=d-2$, in which case $\Phi_0(x,z)$ could decay as
$z^{d-2}$. Finally, $\Phi_J(x,z)$ should decay at large $x$, which corresponds to $\eta(x_1,x_2)$ decaying at
large $|x_1+x_2|$.11

#### [sec-review-p7] paragraph

For $J>0$ or $d>4$, we can use the orthogonality and completeness of the propagators to write
$C_{\Delta,J}(y)$ in terms of $\Phi_J(x,z)$ as

\[ \begin{split} 
J>0\quad\text{or}\quad d>4:\qquad       C_{\Delta,J}(y)=\frac{1}{\alpha_Jf_{\Delta,J}N_{\Delta,J}}\int
\frac{d^dx dz}{z^{d+1}} \Phi_{J}(x,z|y)G_{\tilde\Delta,J}(x,z|y) \,,
 \end{split} \]

(3.18)

where the normalization $\alpha_J$ is given in (A.9). This integral is not convergent for $J=0$ and $d<4$, but
as shown in [8] it can be replaced by the modified relation

\[ \begin{split} 
J=0\ \text{and}\ d<4:\quad C_{\Delta,0}(y)=\int\frac{d^dx dz}{z^{d+1}}\frac{G_{\tilde\Delta,0}(x,z|y)}{\lambda
_{\Delta,0}\alpha_0f_{\Delta,0}N_{\Delta,0}}(\nabla^2_{x,z}-M_{d-2,0}^2)(\nabla^2_{x,z}-
M_{d,0}^2)\Phi_0(x,z)\,,
 \end{split} \]

(3.19)

where the AdS Laplacian is defined in (3.13).

#### [sec-review-p8] paragraph

The CFT-to-AdS map now simply follows from a convolution of the bulk and CFT bases, and it takes the explicit
form

\[ \begin{split} 
d>4:\qquad      \Phi_{J}(x,z)& =\frac12
        \int_{P.S.}\frac{d\Delta}{2\pi i}\frac{f_{\Delta,J}}{N_{\Delta,J}}\int d^dy\int d^dx_1 d^dx_2  \,
G_{\Delta,J}(x,z|y)
        \\
        &\qquad\qquad\times \thptild{x_1}{x_2}{\tilde\Delta,J}{y}\eta(x_1,x_2)\,,\\
d<4:\qquad      \Phi_{J}(x,z)& = \frac12 \int_{\gamma_J} \frac{d\Delta}{2\pi i}  \int d^dy \int d^dx_1 d^dx_2
\frac{f_{\Delta,J}}{\lambda_{\Delta,J}N_{\Delta,J}} \\
                &\quad \times
                G_{\Delta,J}(x,z|y)
                \thpnorm{x_1}{x_2}{\tilde\Delta,J}{y} \, \nabla^2_1\nabla^2_2\eta\left(x_1,x_2\right)\,,
 \end{split} \]

(3.20)

where for $d>4$ we plugged (3.4) into (3.12), while for $d<4$ we plugged (3.9) and (3.10) into (3.12). The
AdS-to-CFT map similarly comes from plugging (3.18) into (3.1), and it takes the form

\[ \begin{split} 
\eta(x_1,x_2) & =
                        \sum_{J=0}^\infty
                        \int_{P.S.}\frac{d\Delta}{2\pi i}
                        \int d^dy
                        \int \frac{d^dxdz}{z^{d+1}}
                        \frac{G_{\tilde{\Delta},J}(x,z|y)}{\alpha_J \, N_{\Delta,J} f_{\Delta,J}}
                        \thpnorm{x_1}{x_2}{\Delta,J}{y}
                        \Phi_{J}(x,z)\,,
 \end{split} \]

(3.21)

where for $d<4$ and $J=0$ we need to replace the $J=0$ term by

\[ \begin{split} 
                        \int_{\gamma_0}\frac{d\Delta}{2\pi i}
                        \int d^dy \int \frac{d^dxdz}{z^{d+1}}
                        \thpnorm{x_1}{x_2}{\Delta,0}{y}
                         \frac{G_{\tilde{\Delta},0}\left(x,z|y\right)}{\alpha_0 N_{\Delta,0}
\lambda_{\Delta,0} f_{\Delta,0}}\\
                        \times
\left(\nabla_{x,z}^{2}-M_{d-2,0}^{2}\right)\left(\nabla_{x,z}^{2}-M_{d,0}^{2}\right)\Phi_{0}(x,z)\,,
 \end{split} \]

(3.22)

due to the modified expansion in (3.19).

### [sec-newmap] section: 3.2 Off-shell map of single-trace operators
#### [sec-newmap-p1] paragraph

We will now discuss how the off-shell bi-local map reviewed above can be used to derive a simple off-shell map
for singlet local operators in the CFT. We start by reviewing the derivation of the map for $J=0$ and $d<4$
that was shown in [8], and then discuss how to generalize this to general $J$ and $d>2$.

#### [sec-newmap-p2] paragraph

Spin $J$ single-trace singlet local operators $S^J_{i_1\cdots i_J}(x)$ in the free theory are defined in terms
of the bi-local as

\[ \begin{split} 
S_{i_1\cdots i_J}^J(x_1)\equiv \lim_{\eps\to 0}D_{i_1\cdots
i_J}^{J,(x_1,x_2)}\eta(x_1,x_2)\vert_{x_2=x_1+\eps\hat e}\,,
 \end{split} \]

(3.23)

where $\hat e$ is an arbitary unit vector, and the bi-local differential operator $D_{i_1\dots
i_J}^{J,(x_1,x_2)}$ can be found in [46] and is fixed such that $S_J(x)$ is a conformal primary normalized
with two-point function

\[ \begin{split} 
\langle S_{i_1\dots i_J}^J(x_1)S^J_{j_1\dots
j_J}(x_2)\rangle=&\mathfrak{a}_{J}\left(\frac{I_{j_1(i_1}(x_{12})\dotsb
I_{i_J)j_J}(x_{12})}{x_{12}^{2(d-2+J)}}-\text{traces}\right)\,,\\
 I_{ij}\equiv\delta_{ij}-2\frac{x_i x_j}{x^2}\,,\quad \mathfrak{a}_{J}=&\frac{\pi ^{\frac{1}{2}-d}  \Gamma
\left(\frac{d}{2}+J-1\right) \Gamma
   (d+J-3)}{2^{d+J}\Gamma (J+1) \Gamma \left(\frac{d-3}{2}+J\right)}\,.
 \end{split} \]

(3.24)

For instance, for $J=0,1$ we have

\[ \begin{split} 
D^{0,(x_1,x_2)}=1\,,\qquad D^{1,(x_1,x_2)}_i=\frac{1}{2\sqrt{d-2}}(\partial_{i,x_2}-\partial_{i,x_1})\,,
 \end{split} \]

(3.25)

such that for $J=0$ we recover the coefficient $\mathfrak{a}_{0}=\frac{\Gamma(d/2-1)^2}{16\pi^d}$ in the
scalar 2-point function computed from (2.6), while for $J=1$ we identify
$S^1_i(x)=-\frac{i}{2\sqrt{d-2}}J_i[\eta]$ with $J_i[\eta]$ defined below (2.23).

#### [sec-newmap-p3] paragraph

As shown in [8], we can use the expansions (3.1) and (3.12) to show that

\[ \begin{split} 
        S^J_{i_1\dots i_J}(x_1) =& \lim_{\eps\to0}\Big[\int_{\gamma_{J}}\frac{d\Delta}{2\pi i}
\frac{2S^{(\tilde\Delta,J)}_{\Delta_0,\Delta_0}C_{i_1\dots
i_{J}}^{\tilde\Delta,J}(x_1)}{\eps^{2\Delta_0+J-\Delta}}+ \\ & \qquad\qquad \sum_{J'=0}^\infty
\int_{\gamma_{J'}}\frac{d\Delta}{2\pi i}\int d^dy C_{j_1\dots j_{J'}}^{\Delta,J'}(y)\frac{(\text{$\hat
e$-dependent})_{i_1\dots i_J;j_i\dots j_{J'}}}{\eps^{2\Delta_0+J'-\Delta}}\Big]\,,\\
        \Phi_{J,i_1\dots i_J}(x_1,\eps)=&2\int_{\gamma_J} \frac{d\Delta}{2\pi i}   f_{\Delta,J}\eps^{\Delta-J}
\left[S_{\Delta_0,\Delta_0}^{(\tilde\Delta,J)}C_{i_1,\dots i_J}^{\tilde\Delta,J}(x_1)+O(\eps)\right]\,.\\
 \end{split} \]

(3.26)

In general, it is difficult to perform the $\Delta$ integrals in (3.26), since we know very little about
general $C_{\Delta,J}$. For instance, the contour $\gamma_{J'}$ for $d>4$ or for $J'>0$ and $d\leq4$ is the
principal series $\text{Re}(\Delta)=d/2$, so along this contour the leading term $\eps^{2-d/2-J'}$ diverges
for the free theory. To get the finite answer for $S^J_{i_1\dots i_J}(x_1)$ that we expect, there must be
complicated cancellations. For $d<4$ and $J'=0$, however, recall that the contour $\gamma_0$ includes a
deformation from the principal series to include the pole $\Delta=d-2<d/2$. Since the principal series
contribution goes to zero as $\eps^{2-d/2}$ in this case, we know even off-shell that the only contribution as
$\eps \to 0$ to the integrals in (3.26) comes from the $\Delta=d-2$ pole, which is the only pole on the other
side of the principal series. This yields the off-shell relation

\[ \begin{split} 
 S^0(x)\equiv\eta(x,x)=\frac{1}{f_{d-2,0}}\lim_{\eps\to0}\eps^{2-d}\Phi_0(x,\varepsilon)\,,
 \end{split} \]

(3.27)

which in particular continues to hold under deformations of the theory.

#### [sec-newmap-p4] paragraph

We can generalize this relation to general $d>2$ and $J$ using a different argument. Consider deforming the
bi-local CFT action by $S^J$ coupled to a source $A^J$ as

\[ \begin{split} 
\mathcal{S}_{A_J}=\int d^dx \,A^J_{i_i\dots i_J}S^J_{i_1\dots i_J}\,.
 \end{split} \]

(3.28)

We can compute the VEV of $\eta(x_1,x_2)$ under this deformation (in the large $N$ limit) as

\[ \begin{split} 
\langle\eta(x_1,x_2)\rangle_{A_J}&=\int d^dy \,A^J_{i_i\dots i_J}(y)D_{i_1\cdots
i_J}^{J,(x_1,x_2)}G_0(x_1,y)G_0(y,x_2)\\
&=\mathfrak{a}_J\int d^dy \,A^J_{i_i\dots i_J}(y) \thpnormind{x_1}{x_2}{d-2+J,J}{y}{i_1,...,i_J}\,,
 \end{split} \]

(3.29)

where the second equality follows from the definitions (2.6), (3.2), and (3.23). As $x_2\to x_1$, this VEV
diverges as $S^{(d-2+J,J)}_{\Delta_0,\Delta_0}A^J(x_1)/x_{12}^{d-4+2J}$. At leading $N\to\infty$, this implies
the off-shell singularity

\[ \begin{split} 
\lim_{ \varepsilon\to0} \varepsilon^{4-d-2J} \eta(x_1,x_2)\vert_{x_2=x_1+\varepsilon\hat
e}=S^{(d-2+J,J)}_{\Delta_0,\Delta_0}\mathfrak{a}_J{A^J_{i_i\dots i_J}(x_1)\hat e_{i_1}\dots \hat e_{i_J}}{}\,,
 \end{split} \]

(3.30)

which is singular for all $d>2$ and $J$ except $J=0$ for $d<4$. In the original path integral in terms of the
local field $\phi_I(x)$, each $\phi_I(x)$ does not couple to the others, which implies that the off-shell
behavior of $\phi_I(x)$, and thus $\eta(x_1,x_2)$, is independent of $N$, so (3.30) in fact holds for finite
$N$. Recall that the conditions (3.3) to expand $\eta(x_1,x_2)$ in terms of $C_{\Delta,J}(y)$ require that
$\eta(x_1,x_2)$ be finite as $x_2\to x_1$, so we must modify our AdS/CFT map in the presence of this source
for all $d>2$ and $J$ except $J=0$ for $d<4$. We can cancel the divergence (3.30) by modifying the contour
$\gamma_J$ in (3.1) to include a piece around $\Delta=d-2+J$ with

\[ \begin{split} 
C_{d-2+J,J}(y)\vert_{A_J}=\mathfrak{a}_JA^J(y)\,,
 \end{split} \]

(3.31)

which will cancel the divergent VEV in (3.29). In the bulk, this modification of $\gamma_J$ will give the VEV

\[ \begin{split} 
\langle\Phi_J(x,z)\rangle\vert_{A_J}=\mathfrak{a}_J f_{d-2+J,J} \int d^dy\, A^J(y)G_{d-2+J,J}(x,z|y)\,,
 \end{split} \]

(3.32)

which follows from modifying the contour in (3.12), and is also what we would get by naively mapping (3.29)
using the un-modified map (3.20) and the CFT orthogonality relation (A.3). We can then take $z\to0$ to find
the modified off-shell bulk boundary condition

\[ \begin{split} 
\lim_{\varepsilon\to0}\varepsilon^{2J-2}\Phi_J(x,\varepsilon)=\mathfrak{a}_Jf_{d-2+J,J} S_B^{d-2+J,J}A^J(x)\,,
 \end{split} \]

(3.33)

which follows from (3.14). We could equivalently use the standard bulk boundary conditions and instead add to
the bulk action the source term

\[ \begin{split} 
\mathcal{S}^{bulk}_{A_J}=\int \frac{d^dxdz}{z^{d+1}} \,A^J_{i_i\dots i_J}(x)
\frac{1}{f_{d-2+J,J}}\lim_{\varepsilon\to0}\varepsilon^{2-d}\Phi_J(x,\varepsilon)\,.
 \end{split} \]

(3.34)

Now, comparing (3.34) to (3.28) for general $A^J(x)$ implies the off-shell relation

\[ \begin{split} 
 S^J(x)=\frac{1}{f_{d-2+J,J}}\lim_{\eps\to0}\eps^{2-d}\Phi_J(x,\varepsilon)\,,
 \end{split} \]

(3.35)

which for $J=0$ for $d<4$ was what we previously showed in (3.27), and for all other $d>2$ and $J$ follows
from the modified boundary condition argument. This off-shell map generalizes the on-shell relation previously
shown for general $d>2$ and $J$ in [8].

## [sec-QED_bulk] section: 4 The bulk dual of scalar QED
### [sec-QED_bulk-p1] paragraph

We will now use the AdS/CFT map of the previous section to write the action for the bulk dual of scalar QED.
We will first review the bulk action for the free and critical $U(N)$ theories, which were derived in [8]. We
will then use the off-shell map of single-trace local operators for $J=0,1$ to show that the bulk QED action
is given by a simple deformation of the bulk dual of the free theory. Finally, we will compute correlation
functions in the bulk and show that the bulk duals of the free theory and QED only differ by the boundary
conditions of the bulk $J=0,1$ two-point function, as anticipated in [20, 21, 22, 23, 24], where the $J=1$
two-point function is sensitive to the gauge-fixing in the CFT.

### [sec-action] section: 4.1 The bulk action
#### [sec-action-p1] paragraph

We start by reviewing the bulk action for the free theory, which in the bi-local language had an infinite
number of terms given by (2.20) and (2.21). The bi-local AdS/CFT map translates each of these terms to the
bulk, where for general $f_{\Delta,J}$ they take a complicated non-local form given explicitly in [8]. For the
special choice

\[ \begin{split} 
f_{\Delta,J}^\text{local} = \left( (-1)^J
\frac{S^{\tilde\Delta,J}_B}{S^{\tilde\Delta,J}_{\Delta_0,\Delta_0}}\right)^{\frac{1}{2}} \,,
 \end{split} \]

(4.1)

such that $f^\text{local}_{\Delta,J} f^\text{local}_{\tilde\Delta,J} = (-1)^J$, the quadratic term in the bulk
action can be written in the simple local way:

\[ \begin{split} 
\mathcal{S}^{(2)}_\text{free}[\Phi_J] = \sum_{J=0}^\infty &
         \frac{1}{\alpha_J}
        \int\frac{d^dxdz}{z^{d+1}} \Phi_{J}(x,z)
\left(\nabla_{x,z}^{2}-M_{d+J-2,J}^{2}\right)\left(\nabla_{x,z}^{2}-M_{d+J,J}^{2}\right) \Phi_{J}(x,z)\,,
 \end{split} \]

(4.2)

where for $d<4$ the modified map (3.22) gives a slightly different form for the $J=0$ term as shown in [8].
The higher order terms $\mathcal{S}^{(n)}[\Phi_J]$ in the bulk action remain non-local even for
$f_{\Delta,J}^\text{local}$, and include explicit bulk counterterms starting with $\mathcal{S}^{(1)}[\Phi_J]$
that are dual to the $V$-dependent counterterms in (2.21).

#### [sec-action-p2] paragraph

The various deformations to the free theory discussed in Section 2.3 can then be mapped to the bulk using the
off-shell map of local operators in (3.35). For instance, the scalar double-trace deformation in (2.25) maps
to

\[ \begin{split} 
\mathcal{S}_\lambda[\Phi_0,\sigma]=\int {d^dx}\left[-
\frac{1}{4\lambda}\sigma^2(x)+\frac{1}{2}\sigma(x)\frac{1}{f_{d-2,0}}\lim_{\eps\to0}\eps^{2-
d}\Phi_0(x,\eps)\right]\,,
 \end{split} \]

(4.3)

where $\sigma(x)$ can be thought of as living on the boundary of AdS. When $\lambda\to0$, this defines the
bulk dual of the critical $U(N)$ theory for any $d>2$ such that this CFT exists, which was argued to be (for
large enough $N$) $2<d<6$ in [33]12. The $\sigma(x)$ field then acts as a Lagrange multiplier in (4.3) that
sets $\lim_{\eps\to0}\eps^{2-d}\Phi_0(x,\eps)=0$ off-shell, just as in the CFT it set $\eta(x,x)=0$ off-shell.
Thus, the off-shell relation (3.27) becomes trivial in the critical theory. The vanishing of the $z^{d-2}$
mode implies that $\Phi_0(x,z)$ now has the same small $z$ boundary condition as all other $J>0$ bulk fields,
namely it scales as $z^{d/2}$, which is the real part of the principal series contour. For $2<d<4$ this was
already discussed in [8], and here we can generalize this to $d>4$ because we generalized the off-shell map
for $J=0$ to $d>4$.

#### [sec-action-p3] paragraph

For QED, we first gauge-fix the CFT by adding the term $\mathcal{S}_\zeta[A]$ given in (2.10), where the
family of possible gauge-fixings is parameterized by $\zeta\in\mathbb{R}$. Since this term, as well as the
Chern-Simons term $\mathcal{S}_k[A]$ given in (2.5) for $d=3$, do not depend on $\eta$, they map trivially to
the bulk such that $A_i(x)$ now lives on the boundary of AdS, just like $\sigma$. We then use the off-shell
map (3.35) for $J=0,1$ to map $\mathcal{S}_e[\eta,A]$ to the bulk to get

\[ \begin{split} 
\mathcal{S}_e[\Phi_0,\Phi_1,A]&=\int {d^dx}\Bigg[\frac{1}{4e^2}F_{ij}^2(x)+A_i^2(x)G_0(x,x)\\
&\qquad\qquad\quad+\lim_{\eps\to0}\eps^{2-d}\Big[\frac{2i\sqrt{d-2}}{f_{d-
1,1}}A_i(x)\Phi_1^i(x,\eps)+\frac{A_i^2(x)\Phi_0(x,\eps)}{\sqrt{N}f_{d-2,0}}\Big]\Bigg]\,,
 \end{split} \]

(4.4)

where we identified $S^1_i(x)=-\frac{i}{2\sqrt{d-2}}J_i[\eta]$, and recall that the counterterm
$A_i^2(x)G_0(x,x)$ is necessary to cancel divergences in the $A_i$ two-point function. We can then take the
limit $e\to\infty$ to get the bulk dual scalar QED (2.4) with bulk action:

\[ \begin{split} 
\mathcal{S}_{\mathbb{CP}^{N-1}}[\Phi_J,A,\sigma]&\equiv\sum_{n=1}^\infty\mathcal{S}_\text{free}^{(n)}[\Phi_J]+
\mathcal{S}_{e\to\infty}[\Phi_0,\Phi_1,A]+\mathcal{S}_{\lambda\to\infty}
 \end{split} \]

(4.5)

as well as the Chern-Simons term $\mathcal{S}_k[A]$ for $d=3$ (if desired).

#### [sec-action-p4] paragraph

Similar to the $\sigma, \Phi_0$ case, we can think of $A_i(x)$ as a Lagrange multiplier that for $k=0$ sets
$\lim_{\varepsilon\to0}\varepsilon^{2-d}\Phi_1(x,\varepsilon)=0$ as an operator equation, just as in the CFT
it set to zero the $U(1)$ current. The $z^0$ mode of $\Phi_1$ then becomes dynamical, according to the off-
shell relation:

\[ \begin{split} 
\text{QED with $k=0$}:\qquad \Phi_1^i(x,0) = i 2\sqrt{d-2} \mathfrak{a}_1 f_{d-1,1} S_B^{d-1,1}A_i(x)\,,
 \end{split} \]

(4.6)

which is just (3.33) with $J=1$ and $S^1_i(x)=-\frac{i}{2\sqrt{d-2}}J_i[\eta]$. Namely, in the bulk dual to
QED, $A_i(x)$ is nothing but the boundary value of the bulk vector field. It is convenient to write this
change of boundary condition by defining a boundary field strength for $\Phi_1$ (even though in our formalism
there is no gauge freedom for this field) as

\[ \begin{split} 
  \mathcal{F}_{\mu\nu}(x) \equiv \lim_{z\to0}\left(\partial_\mu \Phi_{1,\nu}(x,z)-\partial_\nu
\Phi_{1,\mu}(x,z)\right)\,.
 \end{split} \]

(4.7)

The boundary conditions for the free scalar theory and for QED for general $d$, as well as for $d=3$ and
general $k$, can then be written compactly as

\[ \begin{split} 
&\text{free}:\qquad \qquad\qquad\qquad \mathcal{F}_{ij}(x)=0\,,\\
&\text{QED$_d$ with $k=0$}:\qquad \mathcal{F}_{zi}(x)=0\,,\\
&\text{QED$_3$}:\qquad\qquad\qquad\quad \mathcal{F}_{ij}(x)+\frac{2\pi i}{16\kappa} \varepsilon_{ijl}
\mathcal{F}_{zl}(x) =0\,,\\
 \end{split} \]

(4.8)

where the free theory corresponds to electric boundary conditions, QED with $k=0$ corresponds to magnetic
boundary conditions, and QED$_3$ for general $k$ corresponds to mixed boundary conditions. Finally, the
$A_i^2(x)$ term in (4.4) will also alter the boundary behavior of $\Phi_0$ at subleading order in $1/N$,
according to (3.27).

### [sec-correlations] section: 4.2 The bulk correlation functions
#### [sec-correlations-p1] paragraph

We will now discuss the bulk correlation functions that follow from the bulk actions written above. For the
dual of the free theory with $\lambda=e=0$, the bulk two-point functions coming from the local quadratic
action (4.2) are [8]:

\[ \begin{split} 
\langle & \Phi_J (x_1,z_1) \Phi_J(x_2,z_2)\rangle = \frac{\alpha_J/2}{M^2_{d+J,J}-M^2_{d+J-2,J}}
                        \left(
                                \Pi^{TT}_{d-2+J,J}(x_1,z_1|x_2,z_2)-\Pi^{TT}_{d+J,J}(x_1,z_1|x_2,z_2)
                        \right)\,.
 \end{split} \]

(4.9)

Here, $\Pi^{TT}_{d-2+J,J}(x_1,z_1|x_2,z_2)$ are the traceless transverse bulk-to-bulk propagators defined in
[8] by the differential equation

\[ \begin{split} 
        \left( \nabla^2_{x,z} - M^2_{\Delta,J}\right) \Pi^{TT}_{\Delta,J}(x_1,z_1|x_2,z_2){}   =
-\delta^{TT}(x_1,z_1|x_2,z_2)\,,
 \end{split} \]

(4.10)

and by the $z_2\to0$ boundary condition

\[ \begin{split} 
        \Pi^{TT}_{\Delta,J}(x_1,z_1|x_2,z_2) =
        \begin{cases}
{z_2}^{\Delta-J} {\cal C}_{\Delta,J} G_{\Delta,J}(x_1,z_1|x_2) +O(z_2^{\Delta-J+1}) \qquad \Delta<d-J+4\\
O(z_2^{d-2J+4})\qquad\qquad\qquad\qquad\qquad\qquad\quad\;\;\;\, \Delta\geq d-J+4\,, \\
\end{cases}
 \end{split} \]

(4.11)

where $\delta^{TT}$ is a delta function for traceless transverse functions that is defined precisely in [8],
and the normalization is

\[ \begin{split} 
        {\cal C}_{\Delta,J} \equiv \frac{(J+\Delta-1)\Gamma(\Delta-1)}{2\pi^{\frac{d}{2}}
\Gamma(\Delta+1-\frac{d}{2})}\,.
 \end{split} \]

(4.12)

The solution to (4.10) and (4.11) is by construction traceless and transverse:

\[ \begin{split} 
\text{for $a=1,\cdots,J$:}\qquad&\nabla^{\mu_a} \Pi^{TT}_{\Delta,J}(x_1,z_1|x_2,z_2){}_{\mu_1,\dots,
\mu_a,\dots,\mu_J|\mu'_1,...,\mu'_J}=0\,,\\
&  \Pi^{TT}_{\Delta,J}(x_1,z_1|x_2,z_2){}_{\mu_1,\dots,
\mu_a,\dots,\mu_J|\mu'_1,\dots,\mu_a,\dots,\mu'_J}=0\,.
 \end{split} \]

(4.13)

The explicit propagators for $\Delta\geq d-2+J$ for $J>0$, or $J=0$ and any $\Delta$, were computed in [8],
and are reviewed in Appendix B.1. The massless propagators in the first term of (4.9) are identified with the
physical particles dual to the operators in our theory13. For $J>0$ they are dual to the infinite conserved
currents in the CFT, and for $J=0$ to the $\Delta=d-2$ single-trace scalar. The particle with negative
propagator and $\Delta=d+J-2$ is sub-leading in the $z\to0$ limit (it happens to match the ghost spectrum of a
certain gauge-fixing of Vasiliev’s theory [47, 48, 49], so we expect that probably it can be interpreted as
some kind of gauge-fixing-related ghost). The higher order correlation functions can be computed using the
Feynman rules for the higher order terms $\mathcal{S}^{(n)}[\eta]$, which were shown in [8] to lead to the
expected free theory results, where all loops and counterterms cancel (this cancellation will no longer be
exact in the non-free theory we are discussing here, but the divergences should cancel in the same way).

#### [sec-correlations-p2] paragraph

We can then consider the effect of the quadratic scalar deformation $\mathcal{S}_{\lambda}[\Phi_0,\sigma]$
given in (4.3), which only modifies the scalar propagator as [8]:

\[ \begin{split} 
&\langle  \Phi_0(x_1,z_1)\Phi_0(x_2,z_2\rangle_{\lambda}=\langle  \Phi_0(x_1,z_1)\Phi_0(x_2,z_2)\rangle_{\lamb
da=0}+\frac{1}{4(f_{d-2}^\text{local})^2}\left[\frac{\alpha_0\mathcal{C}_{d-2,0}/2}{M^2_{d,0}-M^2_{d-2,0}}
\right]^2\\
&\qquad\qquad \times \int d^dyd^dy' G_{d-2,0}(x_1,z_1|y)\langle\sigma(y)\sigma(y')\rangle_\lambda
G_{d-2,0}(x_2,z_2|y')+O(N^{-1})\,,
 \end{split} \]

(4.14)

where the $\sigma$ propagator at finite $\lambda$ is given in (2.8). For the critical theory at
$\lambda\to\infty$, the $\sigma$ propagator in (2.9) becomes a conformally invariant two-point function with
scaling dimension $\Delta=2+O(1/N)$, so we can use the identity [50, 51, 52]

\[ \begin{split} 
&\int d^dyd^dy' {G_{\Delta,0}(x_1,z_1|y)
\langle\mathcal{O}_{\tilde\Delta,0}(y)\mathcal{O}_{\tilde\Delta,0}(y')\rangle G_{\Delta,0}(x_2,z_2|y')}\\
&\qquad=\alpha_0 N_{\Delta,0}\left(\Delta-\frac
d2\right)\left(\Pi^{TT}_{\Delta,0}(x_1,z_1;x_2,z_2)-\Pi^{TT}_{\tilde\Delta,0}(x_1,z_1;x_2,z_2)\right)\,,
 \end{split} \]

(4.15)

with $\Delta=d-2$ to compute

\[ \begin{split} 
&\langle  \Phi_0(x_1,z_1)\Phi_0(x_2,z_2)\rangle_{\lambda\to\infty}=\frac{\alpha_0/2}{M_{d,0}^2-M_{d-
2,0}^2}(\Pi^{TT}_{2,0}(x_1,z_1;x_2,z_2)-\Pi^{TT}_{d,0}(x_1,z_1;x_2,z_2))+O(N^{-1})\,.\\
 \end{split} \]

(4.16)

We see that the physical propagator $\Pi^{TT}_{d-2,0}$ for $\Phi_0$ in the bulk dual of the free scalar theory
has been replaced by the shadow propagator $\Pi^{TT}_{2,0}$, which generalizes the $2<d<4$ results of [8] to
$2<d<6$ (where the critical theory is defined at large $N$). Both $\Pi^{TT}_{\Delta,J}$ and
$\Pi^{TT}_{\tilde\Delta,J}$ are defined by the same bulk differential equation (4.10), and differ only by the
boundary condition (4.11). Since the only difference between the free and critical bulk theories was this
scalar propagator, we see that to all orders in $1/N$ the only difference between the free and critical bulk
theories is the boundary condition for the bulk scalar, as anticipated in [20, 51, 50]. As shown in [51], the
modification of the free bulk Feynman rules by replacing $\Pi^{TT}_{d-2,0}\to \Pi^{TT}_{2,0}$ then leads to
the expected bulk dual of the critical CFT for all bulk correlators, at all orders in $1/N$.

#### [sec-correlations-p3] paragraph

Next, we consider the effect of coupling to the gauge field by adding $\mathcal{S}_{e}[\Phi_0,\Phi_1,A]$ with
the family of gauge-fixing terms $\mathcal{S}_{\zeta}[A]$ (and for $d=3$ we can add also the Chern-Simons term
$\mathcal{S}_{k}[A]$). The $J=1$ propagator is modified as

\[ \begin{split} 
&\langle  \Phi_1(x_1,z_1)\Phi_1(x_2,z_2)\rangle_{\zeta,e,k}=\langle  \Phi_1(x_1,z_1)\Phi_1(x_2,z_2)\rangle_{e=
0}+\frac{4(2-d)}{(f_{d-1,1}^\text{local})^2}\left[\frac{\alpha_1\mathcal{C}_{d-1,1}/2}{M^2_{d+1,1}-M^2_{d-
1,1}} \right]^2\\
&\qquad\qquad \times \int d^dyd^dy' G^i_{d-1,1}(x_1,z_1|y)\langle A_i(y)A_j(y')\rangle_{\zeta,e,k}
G^j_{d-1,1}(x_2,z_2|y')+O(N^{-1})\,,
 \end{split} \]

(4.17)

where we suppressed the bulk indices for simplicity, and where the gauge-fixed photon propagator is given in
(2.13) for the $\zeta$ family of gauges. Note that the bulk propagator now depends on the choice of gauge-
fixing in the CFT. For the critical theory at $e\to\infty$, we can derive a generalization of the identity
(4.15) to massless $J=1$ propagators:14

\[ \begin{split} 
&\int d^dyd^dy' {G_{d-1,1}(x_1,z_1|y){}_{i|\mu} \langle A_i(y)A_{i'}(y') \rangle_{\zeta,e\to\infty,k}
G_{d-1,1}(x_2,z_2|y')}{}_{i'|\mu'}\\
&\qquad=\frac{8\pi^\frac{3d}{2}}{\Gamma\left(\frac{d-2}{2}\right)\Gamma\left(d\right)}
\left(\Pi^{TT}_{d-1,1}(x_1,z_1;x_2,z_2)_{\mu|\mu'}-\Pi^{\zeta,k}_{1,1}(x_1,z_1;x_2,z_2)_{\mu|\mu'}\right)\,.
 \end{split} \]

(4.18)

Here, $\Pi^{\zeta,k}_{1,1}$ is a traceless and transverse propagator that satisfies the same differential
equation (4.9) as $\Pi^{TT}_{d-1,1}$, but has the alternate boundary condition

\[ \begin{split} 
\lim_{z_2\to0}\Pi^{\zeta,k}_{1,1}(x_1,z_1;x_2,z_2)= \frac{\Gamma\left(\frac{d-
2}{2}\right)\Gamma^{2}\left(\frac{d}{2}\right)}{2\pi^{\frac{d}{2}}\Gamma\left(d\right)}
G^{\zeta,k}_{1,1}(x_1,z_1|x_2)\,,
 \end{split} \]

(4.19)

where $G^{\zeta,k}_{1,1}(x_1,z|x_2)$ is a transverse bulk-to-boundary propagator that satisfies the same
differential equation (3.13) as $G_{d-1,1}(x_1,z|x_2)$ but has the alternate $z\to0$ boundary condition

\[ \begin{split} 
G^{\zeta,k}_{1,1}(x_1,z|x_2)_{ij}=\begin{cases} \langle A_i(x_1)A_j(x_2)\rangle_{\zeta,\infty}-z^{d-
2}\frac{\pi^{\frac{d}{2}}\Gamma\left(d\right)}{\Gamma^{3}\left(\frac{d}{2}\right)}\int\frac{d^dp}{(2\pi)^d}e^{
ipx_{12}}(\delta_{ij}-\frac{p_ip_j}{|p|^2})+\dots\,,\qquad d\neq3\,,\\
 \langle A_i(x_1)A_j(x_2)\rangle_{\zeta,\infty,k}-z\int\frac{d^{3}p}{\left(2\pi\right)^{3}}e^{ip x_{12}}\frac{
16\left(\delta_{ij}-\frac{p_{i}p_{j}}{\left|p\right|^{2}}\right)-
\frac{128\kappa}{\pi}\,\varepsilon_{ijk}\frac{p_{k}}{\left|p\right|}}{\frac{64\kappa^2}{\pi^2}+1}+\dots\,,\qua
d d=3\,.\\
\end{cases}
 \end{split} \]

(4.20)

Note that we expressed $\delta^{TT}_1(x_{12})$ explicitly in momentum space for $d\neq3$ for ease of
comparison to $d=3$. Alternatively, $\Pi_{1,1}^{\zeta,k}$ can be defined by their differential equation and
the boundary condition (4.8). Explicit expressions for $\Pi^{\zeta,k}_{1,1}$ and $G^{\zeta,k}_{1,1}$ are
derived in Appendix B.2, where we show that they satisfy (4.18). We can then apply (4.18) to the $e\to\infty$
limit of (4.17) to compute

\[ \begin{split} 
&\langle  \Phi_1(x_1,z_1)\Phi_1(x_2,z_2)\rangle_{\zeta,e\to\infty,k}=\frac{\alpha_1/2}{M_{d+1,1}^2-M_{d-
1,1}^2}(\Pi^{\zeta,k}_{1,1}(x_1,z_1;x_2,z_2)-\Pi^{TT}_{d+1,1}(x_1,z_1;x_2,z_2))+O(N^{-1})\,.\\
 \end{split} \]

(4.21)

As in the scalar deformation, we see that the physical propagator $\Pi^{TT}_{d-1,1}$ for $\Phi_1$ has been
replaced by the shadow propagator $\Pi^{\zeta,k}_{1,1}$, except that now the shadow propagator depends on the
CFT gauge-fixing parameter $\zeta$, and for $d=3$ it can also have an infinite number of possible boundary
conditions, parameterized by $k$.

#### [sec-correlations-p4] paragraph

For the $\mathbb{CP}^{N-1}$ model, we saw above that we can change variables for $\sigma(x)$ to get rid of the
$A_i^2 \phi^2$ term. In this way $\sigma,A_i$ couple in the bulk action (4.5) only linearly to $\Phi_0,\Phi_1$
respectively. As we explained in this section, this means that the $\mathbb{CP}^{N-1}$ bulk dual (at any order
in $1/N$) is the same as the free theory bulk dual, only with the alternative boundary conditions for both
$\Phi_0$ and $\Phi_1$. We can use this to argue that our bulk action gives the expected correlators to all
orders in $1/N$ for the $\mathbb{CP}^{N-1}$ model, following the analogous argument for the critical $O(N)$
model in [51]. In particular, already in the local description (2.4) we could change variables for $\sigma$,
which led to only linear couplings for $\sigma,A_i$ to the $\phi_I$’s. We can then consider the difference
between correlation functions of single-trace operators in the $\mathbb{CP}^{N-1}$ model and in the free
theory. At any order in $1/N$, this difference can be written as integrals of the free theory $S^0, S^1_i$
correlation functions with the effective propagators for $\sigma,A_i$. Using (4.15) for $S^0$ and (4.18) for
$S^1_i$, we can write the difference between the correlators as the difference between the same Witten
diagrams, only with alternative boundary conditions for $\Phi_0$ and $\Phi_1$.

## [sec-QCD_bulk] section: 5 The bulk dual of $U(N_c)$ scalar QCD at finite $N_c$
### [sec-QCD_bulk-p1] paragraph

The bulk dual of scalar QED in $2<d<4$ with $N\gg1$ scalars that we described in the previous sections can be
easily generalized to $U(N_c)$ QCD in $2<d<4$ with $N\gg1$ scalars [28], for finite $N_c$. For $d=3$ we can
again consider also the large Chern-Simons level $k$ limit with fixed $\kappa\equiv k/N$.

### [sec-QCD_bulk-p2] paragraph

We start by considering a free theory of $N\times N_c$ scalars with global symmetry $U(NN_c)$. The singlet
sector under the $U(N)\subset U(NN_c)$ subgroup can be translated to the bulk just like the usual $U(N)$ free
scalar theory, except that now both the $U(N)$ singlet bi-locals in the CFT and their dual bulk fields are
adjoints under $U(N_c)$, and the terms in the bulk action are all single traces of products of $U(N_c)$
matrices. We can then construct the bulk dual of scalar QCD by a procedure similar to the one described in the
previous sections: gauging $U(N_c)$ (in the CFT), fixing a gauge convenient for the large $N$ expansion,
mapping the $U(N_c)$ current (which is a $U(N)$ singlet) to the bulk using our usual CFT-to-AdS map, and
coupling it to the new $U(N_c)$ gauge fields. The main differences from the Abelian case are that now the
Yang-Mills and Chern-Simons terms for $U(N_c)$ contain self-interactions of the $U(N_c)$ gauge fields, and
that the gauge-fixing now leads to ghosts (in the adjoint of $U(N_c)$) which will live on the boundary and
couple to the $U(N_c)$ gauge fields there.

### [sec-QCD_bulk-p3] paragraph

As with QED, the resulting bulk theory is related to the bulk dual of the free theory by a simple change of
boundary conditions for the spin one bulk field (in the adjoint of $U(N_c)$). Note that this bulk construction
is useful for large $N$ with fixed $N_c$, and it does not apply to the limit of large $N_c,k$ with fixed
$N,k/N_c$ discussed in [29, 53], which is expected to have a different dual description.

## [acknowledgments] section: Acknowledgments
### [acknowledgments-p1] paragraph

We would like to thank Tal Sheaffer and Tomer Solberg for collaboration on related issues. This work was
supported in part by an Israel Science Foundation center for excellence grant (grant number 2289/18), by grant
no. 2018068 from the United States-Israel Binational Science Foundation (BSF), and by the Minerva foundation
with funding from the Federal German Ministry for Education and Research. OA is the Samuel Sebba Professorial
Chair of Pure and Applied Physics. SMC is supported in part by a Zuckerman STEM leadership fellowship.

## [bases] appendix: A Conformal bases
### [bases-p1] paragraph

In this appendix we review properties of the conformal bases that we use for the CFT and for the bulk fields.
For the CFT we follow [54, 55], while for the bulk we follow [52].

### [3pointBasis] appendix: A.1 Three-point function basis
#### [3pointBasis-p1] paragraph

The harmonic basis defined in (3.2) satisfies the completeness relation

\[ \begin{split} 
\delta(x_{13})\delta(x_{24})=\frac12\sum_{J=0}^\infty \int_{\gamma_J}\frac{d\Delta}{2\pi i} \int d^d y  \,
        \frac{1}{N_{\Delta,J}}
        \thpnorm{x_1}{x_2}{\Delta,J}{y}\thptild{x_3}{x_4}{\tilde\Delta,J}{y}\,,
 \end{split} \]

(A.1)

where the contour $\gamma_J$ was described in the main text, and the normalization factor is

\[ \begin{split} 
        N_{\Delta,J}=\frac{\pi^{\frac{3d}{2}}\Gamma(J+1)}
        {2^{J-1}\Gamma(\frac{d}{2}+J)}
        \frac{\Gamma\left(\Delta-\frac{d}{2}\right)}{\Gamma\left(\Delta-1\right)\left(\Delta+J-
1\right)}\frac{\Gamma\left(\tilde{\Delta}-\frac{d}{2}\right)}{\Gamma\left(\tilde{\Delta}-
1\right)\left(\tilde{\Delta}+J-1\right)}\,.
         \end{split} \]

(A.2)

The basis also satisfies the orthogonality relation

\[ \begin{split} 
        &\int d^d x_{1}d^d x_{2}
        \thpnorm{x_1}{x_2}{\Delta,J}{y}\thptild{x_1}{x_2}{\tilde\Delta^\prime,J^\prime}{y^\prime}\\
        & \quad = 2\pi i \,\, N_{\Delta,J}\left(
\delta_{J,J^\prime}\delta\left(\Delta-\Delta^\prime\right)\delta^{TT}_J(y-y^\prime) +
\frac{\delta\left(\Delta-\tilde \Delta^\prime\right)}{S^{(\tilde\Delta,J)}_{\Delta_0,\Delta_0} } \left\langle
O_{\Delta,J}(y) O_{\Delta,J'}(y^\prime) \right\rangle\right)\,,
         \end{split} \]

(A.3)

where the traceless transverse delta function $\delta^{TT}_J$ was defined in the main text, and the shadow
coefficient is

\[ \begin{split} 
        S^{(\tilde\Delta,J)}_{\Delta_0,\Delta_0} = \frac{\pi^{\frac{d}{2}} \Gamma\left( \tilde \Delta
-\frac{d}{2} \right)\Gamma\left(\tilde\Delta+J-1\right)\Gamma^2\left(\frac{\Delta+J}{2}\right)}
{\Gamma\left(\tilde\Delta-1\right)\Gamma\left(\Delta+J\right)\Gamma^2\left(\frac{\tilde\Delta+J}{2}\right)}\,.
 \end{split} \]

(A.4)

The reason for the second term in (A.3) is because the basis elements for $\Delta$ and for $\tilde \Delta$ are
related by the shadow transform:

\[ \thpnorm{x_1}{x_2}{\Delta,J}{y}
        = \frac{1}{S^{(\tilde\Delta,J)}_{\Delta_0,\Delta_0} }
        \int d^d y^\prime
        \tp{\Delta,J}{y}{y^\prime} \thpnorm{x_1}{x_2}{\tilde\Delta,J}{y^\prime}\,. \]

(A.5)

### [bulkBasis] appendix: A.2 Bulk-to-boundary propagator basis
#### [bulkBasis-p1] paragraph

The differential equation (3.13) with boundary condition (3.14) has the explicit solution

\[ \begin{split} 
        G _{\Delta,J}(x,z|y){}_{\mu_1,...,\mu_J|i_1,..,i_J}= \left(\frac{z}{(x-y)^2+z^2}\right)^\Delta
\left(X_{\mu_1,i_1}\cdot...\cdot X_{\mu_J,i_J}-\text{traces}\right)\,,
 \end{split} \]

(A.6)

where $X_{i,j} = z^{-1}\Big({\delta_{i,j}-2\frac{(x-y)_i (x-y)_j}{(x-y)^2+z^2}}\Big)$,
$X_{z,i}=\frac{-2(x-y)_i}{(x-y)^2+z^2}$. The propagator satisfies the bulk analog of the shadow transform
(A.5):

\[ \begin{split} 
        & G^{i_1 \dots i_J}_{\Delta,J}(x,z|y  )_{\mu_1,...,\mu_J}  =  \frac{1}{S_B^{\tilde \Delta,J}}\int
d^dy' G^{i'_1 \dots i'_J}_{\tilde\Delta,J}(x,z|y'  )_{\mu_1,...,\mu_J}
        \langle\mathcal{O}_{\Delta,J}^{i_1\dots i_J}(y')\mathcal{O}_{\Delta,J}^{i'_1\dots i_J'}(y')\rangle \,,
 \end{split} \]

(A.7)

where $S_B^{\tilde \Delta,J}$ was given in (3.15). The orthogonality relation takes the form

\[ \begin{split} 
&\int\frac{d^dxdz}{z^{d+1}} G^{\mu_1\dots\mu_J|i_1\dots i_J}_{\Delta,J}(x,z|x_1)G^{i'_1\dots
i'_J}_{\tilde\Delta',J}(x,z|x_2)_{\mu_1\dots\mu_J}=\\
& 2\pi i\delta(\Delta-\tilde\Delta')\langle\mathcal{O}^{i_1\dots i_J}_{\Delta,J}(x_1)\mathcal{O}^{i'_1\dots
i'_J}_{\Delta,J}(x_2)\rangle S_B^{\tilde\Delta,J}+2\pi i \delta(\Delta-\Delta')\delta^{TT}_{J,{i_1\dots
i_j|i'_1\dots i'_J}}(x_{12})\frac{N_{\Delta,J}\alpha_J}{2}\,,
 \end{split} \]

(A.8)

where $\delta^{TT}_J(x)$ is defined in [52] as a delta function for traceless transverse spin $J$ functions in
$d$ dimensions, $N_{\Delta,J}$ is defined in (A.2), and

\[ \begin{split} 
        \alpha_J  \equiv \frac{2^J \Gamma(\frac{d}{2}+J)}{\pi^{\frac{d}{2}}\Gamma(J+1)}\,.
         \end{split} \]

(A.9)

The bulk completeness relation for traceless transverse bulk functions is

\[ \delta^{\mu_1,...,\mu_J|\mu'_1,...,\mu'_J}_{TT}(x,z|x',z')=\int_{P.S.}\frac{d\Delta}{2\pi i} \int d^dy \frac{G^{\mu_1,...,\mu_J|i_1,..,i_J}_{\Delta,J}(x,z|y)G^{\mu'_1,...,\mu'_J|i_1,..,i_J}_{\tilde{\Delta},J}(x',z'| y  )}{\alpha_J N_{\Delta,J}}
        \,, \]

(A.10)

where here $\delta^{TT}$ is defined in the bulk.

## [erez] appendix: B Bulk-to-bulk propagators
### [erez-p1] paragraph

In this appendix, we will show explicit expressions for the bulk-to-bulk propagators discussed in the main
text. We will start by reviewing the traceless transverse propagators $\Pi^{TT}_{\Delta,J}$ introduced in [8],
which are defined by the differential equation (4.10) with standard boundary condition (4.11). These have
explicit position space expressions for all $J$ and $\Delta\geq d-2+J$. For $J=1$, we will also give the
explicit expression in momentum space. We will then consider the $J=1$ propagator defined by the same
differential equation (4.10) but with the alternate boundary condition (4.19), which we will also write
explicitly in momentum space. From these momentum space expressions, we can immediately see the identity
(4.18).

### [erez1] appendix: B.1 Standard boundary conditions
#### [erez1-p1] paragraph

The differential equation (4.10) with boundary condition (4.11) can be formally solved using the split
representation

\[ \begin{split} 
&       \Pi^{TT}_{\Delta,J}(x,z|x',z')=  \int_{\gamma_J} \frac{d \Delta^\prime}{2\pi
i}\frac{G_{\Delta,J}(x,z|y)G_{\tilde{\Delta},J}(x',z'| y
)}{\alpha_JN_{\Delta,J}(M^2_{\Delta,J}-M^2_{\Delta^\prime,J})}\,,
         \end{split} \]

(B.1)

where the boundary spin indices are contracted on the right-hand side, while the bulk indices on both sides
are implicit. For massive propagators, i.e. $\Delta>d-2+J$ or $J=0$, we can close the contour and collect
poles to get the explicit position-space expression

\[ \begin{split} 
        \Pi^{TT}_{\Delta,J}(x,z|x',z')  =\Pi_{\Delta,J}(x,z|x',z')-\sum_{p=d-1}^{d+J-2}
\frac{(2p-d)}{M^2_{\Delta,J}-M^2_{p,J}}\text{Res}\left[  \Pi_{\Delta^\prime,J}(x,z|x',z')
\right]_{\Delta^\prime=p}\,,
         \end{split} \]

(B.2)

where $\Pi_{\Delta,J}$ is the standard massive bulk-to-bulk propagator whose explicit form is given by a
complicated recursion relation in [56]. For instance, the $J=0$ propagator is

\[ \begin{split} 
\Pi_{\Delta,0}(x,z|x',z')=\mathcal{C}_{\Delta,0}(2u)^{-\Delta}{}_2F_1\left(\Delta,\Delta+\frac{1-
d}{2},2\Delta-d+1;-\frac{2}{u}\right)\,,
 \end{split} \]

(B.3)

where the chordal distance is

\[ \begin{split} 
u=\frac{\sum_ix_ix'_i +zz'}{2z z'}\,,
 \end{split} \]

(B.4)

and note that $\Pi^{TT}_{\Delta,0}=\Pi_{\Delta,0}$ since transversality and tracelessness are trivial for
$J=0$. For $J=1$ the propagator is

\[ \begin{split} 
\Pi^{TT}_{\Delta,1}(x,z|x',z'){}_{\mu|\mu'} =-g_0(u){\partial_\mu\partial_{\mu'}}u
+g_1(u)\partial_{\mu}u\partial_{\mu'}u \,,
 \end{split} \]

(B.5)

where $g_0(u)$ and $g_1(u)$ are

\[ \begin{split} 
g_0(u)&=\frac{ (d-\Delta ) \Gamma (\Delta +1) u^{-\Delta } \, _2F_1\left(\Delta ,\frac{1}{2} (-d+2 \Delta
+1);-d+2 \Delta
   +1;-\frac{2}{u}\right)}{\pi ^{d/2} 2^{\Delta +1}(\Delta -1) (d-\Delta -1) \Gamma \left(-\frac{d}{2}+\Delta
+1\right)}\\
   &-\frac{(u+1) \Gamma (\Delta +1)
   u^{-\Delta -1} \, _2F_1\left(\Delta +1,\frac{1}{2} (-d+2 \Delta +1);-d+2 \Delta +1;-\frac{2}{u}\right)}{\pi
^{d/2} 2^{\Delta +1}(\Delta -1) (d-\Delta -1) \Gamma
   \left(-\frac{d}{2}+\Delta +1\right)}\,,\\
g_1(u)&=\frac{ (u+1) (d-\Delta ) \Gamma (\Delta +1) u^{-\Delta -1} \, _2F_1\left(\Delta ,\frac{1}{2} (-d+2
\Delta +1);-d+2 \Delta
   +1;-\frac{2}{u}\right)}{\pi ^{d/2} 2^{\Delta +1}(\Delta -1) (u+2) (d-\Delta -1) \Gamma
\left(-\frac{d}{2}+\Delta +1\right)}\\
   &-\frac{
   \left(d+(u+1)^2\right) \Gamma (\Delta +1) u^{-\Delta -2} \, _2F_1\left(\Delta +1,\frac{1}{2} (-d+2 \Delta
+1);-d+2 \Delta +1;-\frac{2}{u}\right)}{\pi ^{d/2} 2^{\Delta +1}(\Delta
   -1) (u+2) (d-\Delta -1) \Gamma \left(-\frac{d}{2}+\Delta +1\right)}\,.\\
 \end{split} \]

(B.6)

In the massless limit $\Delta\to d-2+J$, the $\Delta'=d-2+J$ pole in (B.1) becomes a double pole and we get
the finite result

\[ \begin{split} 
        &\Pi^{TT}_{d-2+J,J}(x,z|x',z') =\\
        &\qquad \partial_\Delta\Big[(\Delta-d-J+2)\Pi_{\Delta,J}(x,z|x',z')\Big]_{\Delta=d-2+J}-
\frac{\text{Res}   \left[   \Pi_{\Delta^\prime,J}(x,z|x',z') \right]_{\Delta^\prime=d-(2-J)}}{4-d-2J} \\
        &\qquad -\sum_{p=d-1}^{d+J-3}  \frac{(2p-d)}{M^2_{\Delta,J}-M^2_{p,J}}\text{Res}\left[
\Pi_{\Delta^\prime,J}(x,z|x',z')   \right]_{\Delta^\prime=p}\,.
         \end{split} \]

(B.7)

For $J=1$, the massless propagator $\Pi^{TT}_{d-1,1}$ is the same as the position space Landau gauge
propagator given in [57], which can be explicitly checked from the definitions given here.

#### [erez1-p2] paragraph

We will find it convenient to express $\Pi^{TT}_{d-1,1}$ in momentum space. Instead of directly transforming
the known position space expression, we can instead solve the differential equation (4.10) in momentum space.
We start by writing the bulk-to-boundary differential equation (3.13) in momentum space as

\[ \begin{split} 
        \left(z^{2}\partial_{z}^{2}+\left(3-d\right)z\partial_{z}-p^{2}z^{2}\right)G_{d-
1,1}\left(p,z\right)_{i,j}-2izp_{i}G_{d-1,1}\left(p,z\right)_{z,j}&=0,\\
  \left(z^{2}\partial_{z}^{2}+\left(3-d\right)z\partial_{z}-p^{2}z^{2}+1-d\right)G_{d-
1,1}\left(p,z\right)_{z,j}+2iz\sum_{i=1}^{d}p_{i}G_{d-1,1}\left(p,z\right)_{i,j}&=0,
         \end{split} \]

(B.8)

with the $z\to0$ boundary condition (3.14). We can solve this to get

\[ \begin{split} 
  G_{d-1,1}\left(p,z\right)_{i,j} & =\frac{\pi^{\frac{d}{2}}2^{2-
\frac{d}{2}}}{\Gamma\left(d\right)}\left|pz\right|^{\frac{d}{2}-
1}\left(z\frac{p_{i}p_{j}}{\left|p\right|}K_{\frac{d-4}{2}}\left(\left|p\right|z\right)+\delta_{i,j}\left(d-
2\right)\,K_{\frac{d-2}{2}}\left(\left|p\right|z\right)\right)\\
  G_{d-1,1}(p,z)_{z,j} & =\frac{\pi^{\frac{d}{2}}2^{2-
\frac{d}{2}}}{\Gamma\left(d\right)}\left|pz\right|^{\frac{d}{2}-1}\cdot\left(ip_{j}z\right)K_{\frac{d-
2}{2}}\left(|p| z\right) \,,
   \end{split} \]

(B.9)

which is the momentum space version of (A.6). Next, we use transversality to rewrite (4.10) as

\[ \begin{split} 
  \partial_{\mu}\left(z^{3-d}\left(\partial_{\mu}\Pi_{\nu\rho}-\partial_{\nu}\Pi_{\mu\rho}\right)\right)&
=-\delta_{\nu,\rho}\delta(x,z|x',z')+z^{-d-1}\partial_{\rho'}z^{2}\partial_{\nu}\Pi_{d,0},\\
  \Pi_{d,0}\left(x,z|x',z'\right)&=\left(zz'\right)^{\frac{d}{2}}\int\frac{d^{3}p}{\left(2\pi\right)^{3}}e^{ip
\cdot\left(x-x'\right)}\begin{cases}
I_{\frac{d}{2}}\left(\left|p\right|z\right)K_{\frac{d}{2}}\left(\left|p\right|z'\right) & z<z'\\
I_{\frac{d}{2}}\left(\left|p\right|z'\right)K_{\frac{d}{2}}\left(\left|p\right|z\right) & z'<z
\end{cases}\,,
 \end{split} \]

(B.10)

which we then write in momentum space as

\[ \begin{split} 
 \partial_{z}\left(z^{-d+3}\left(\partial_{z}\Pi_{d-1,1}\left(p,z,z'\right)_{i,j}-ip_{i}\Pi_{d-
1,1}\left(p,z,z'\right)_{z,j}\right)\right)&\\
 -z^{-d+3}\left(p^{2}\Pi_{d-1,1}\left(p,z,z'\right)_{i,j}+p_{i}\sum_{k=1}^{d}p_{k}\Pi_{d-
1,1}\left(p,z,z'\right)_{k,j}\right)
 &\\
 =-\delta_{i,j}\delta\left(z-z'\right)-z^{-d+1}p_{i}p_{j'}&\Pi_{d,0}\left(p,z,z'\right),
 \end{split} \]

(B.11)

\[ \begin{split} 
   \Pi_{d,0}\left(p,z,z'\right)&=\left(zz'\right)^{\frac{d}{2}}\begin{cases}
  I_{\frac{d}{2}}\left(pz\right)K_{\frac{d}{2}}\left(pz'\right) & z<z'\\
  I_{\frac{d}{2}}\left(pz'\right)K_{\frac{d}{2}}\left(pz\right) & z'<z
  \end{cases}\,.
 \end{split} \]

(B.12)

We can solve this equation along with the boundary condition (4.11) and the explicit momentum space
$G_{d-1,1}(p,z)$ to get

\[ \begin{split} 
   \Pi_{d-1,1}^{TT}\left(p,z,z'\right)_{i,j}&=\left(zz'\right)^{\frac{d}{2}-1}K_{\frac{d-
2}{2}}\left(pz'\right)I_{\frac{d-2}{2}}\left(pz\right)\left(\delta_{i,j}-\frac{p_{i}p_{j}}{p^{2}}\right)\\
   &+\frac{p_{i}p_{j}}{p^{4}}\left[\left(zz'\right)^{d-1}\partial_{z,z'}\left(\left(zz'\right)^{-
d+1}\Pi^{TT}_{d-1,1}(p,z,z')_{z,z'}\right)\right],\\
   \Pi_{d-1,1}^{TT}\left(p,z,z'\right)_{i,z'}&=i\frac{p_{i}}{p^{2}}z^{d-1}\partial_{z}\left(z^{-
d+1}\Pi^{TT}_{d-1,1}(p,z,z')_{z,z'}\right),\\
   \Pi_{d-1,1}^{TT}\left(p,z,z'\right)_{z,j}&=-i\frac{p_{j}}{p^{2}}\left(z'\right)^{d-
1}\partial_{z'}\left(\left(z'\right)^{-d+1}\Pi^{TT}_{d-1,1}(p,z,z')_{z,z'}\right),\\
   \Pi_{d-1,1}^{TT}\left(p,z,z'\right)_{z,z'} &=
-\frac{p^{2}}{d-2}\left(\partial_{\Delta}\Pi_{\Delta,0}\left(p,z,z'\right)\right)\mid_{\Delta=d-1}\,,
 \end{split} \]

(B.13)

where $\Pi_{\Delta,0}\left(p,z,z'\right)$ is the scalar bulk-to-bulk propagator

\[ \begin{split} 
  \Pi_{\Delta,0}\left(p,z,z'\right)=\begin{cases}
\left(zz'\right)^{\frac{d}{2}}I_{\Delta-\frac{d}{2}}\left(\left|p\right|z\right)K_{\Delta-
\frac{d}{2}}\left(\left|p\right|z'\right) & z<z'\\
\left(zz'\right)^{\frac{d}{2}}I_{\Delta-\frac{d}{2}}\left(\left|p\right|z'\right)K_{\Delta-
\frac{d}{2}}\left(\left|p\right|z\right) & z>z'
\end{cases}.
 \end{split} \]

(B.14)

### [erez2] appendix: B.2 Alternate boundary conditions for $J=1$
#### [erez2-p1] paragraph

We will now solve the differential equation (B.11) with the alternate boundary conditions (4.19). We start by
computing the alternate bulk-to-boundary propagator $G_{1,1}^{\zeta,k}(p,z)$, by solving (B.8) with the
boundary condition (4.20) and the explicit momentum space photon 2-point function given in the first line of
(2.15), which depends on the family of gauge-fixings parameterized by $\zeta\in\mathbb{R}$, as well as the
Chern-Simons coupling $k$ for $d=3$. For $d\neq3$ we get

\[ \begin{split} 
    G^{\zeta}_{1,1}\left(p,z\right)_{i,j}&=\frac{2^{\frac{d}{2}-
2}\pi^{\frac{d}{2}}\Gamma\left(d\right)\left|p\right|^{\frac{2-d}{2}}z^{\frac{d-2}{2}}}{\Gamma\left(2-
\frac{d}{2}\right)\Gamma\left(\frac{d}{2}-1\right)\Gamma^{2}\left(\frac{d}{2}\right)}\left(\left(\delta_{i,j}-
\frac{p_{i}p_{j}}{p^{2}}\right)K_{\frac{d-2}{2}}\left(\left|p\right|z\right)+\frac{4\left(1-\zeta\right)}{d-
2}\frac{p_{i}p_{j}}{\left|p\right|}zK_{\frac{d}{2}}\left(\left|p\right|z\right)\right)\,,\\
    G^{\zeta}_{1,1}\left(p,z\right)_{z,j}&=i\frac{2^{\frac{d-
2}{2}}\pi^{\frac{d}{2}}\Gamma\left(d\right)}{\Gamma\left(2-
\frac{d}{2}\right)\Gamma^{3}\left(\frac{d}{2}\right)}\left(\zeta-1\right)\left|p\right|^{\frac{2-
d}{2}}z^{\frac{d}{2}}K_{\frac{d-2}{2}}\left(\left|p\right|z\right)p_{j}\,,
   \end{split} \]

(B.15)

while for $d=3$ and general $k$ we get

\[ \begin{split} 
  G_{1,1}^{\zeta,k}\left(p,z\right)_{i,j}&=\frac{e^{-
\left|p\right|z}}{\left|p\right|}\frac{\frac{1}{16}\left(\delta_{i,j}+\frac{p_{i}p_{j}}{\left|p\right|^{2}}\le
ft(\left(1-\zeta\right)\left(1+pz\right)-1\right)\right)-
\frac{\kappa}{2\pi}\,\varepsilon_{ijk}\frac{p_{k}}{\left|p\right|}}{\left(\frac{\kappa}{2\pi}\right)^{2}+\left
(\frac{1}{16}\right)^{2}}\\
  G_{1,1}^{\zeta,k}\left(p,z\right)_{z,j}&=i\frac{16\left(1-
\zeta\right)}{1+\left(\frac{16\kappa}{2\pi}\right)^{2}}e^{-\left|p\right|z}\frac{z}{\left|p\right|}\,p_{j}\,.
 \end{split} \]

(B.16)

We can then solve (B.11) with the alternate boundary conditions (4.19) to get for $d\neq3$:

\[ \begin{split} 
  \Pi_{1,1}^{\zeta}\left(p,z,z'\right)_{i,j}&=\left(zz'\right)^{\frac{d}{2}-1}K_{\frac{d-
2}{2}}\left(pz'\right)I_{\frac{2-d}{2}}\left(pz\right)\left(\delta_{i,j}-\frac{p_{i}p_{j}}{p^{2}}\right)\\
  &\qquad +\frac{p_{i}p_{j}}{p^{4}}\left[\left(zz'\right)^{d-1}\partial_{z,z'}\left(\left(zz'\right)^{-
d+1}\Pi^{\zeta}_{1,1}(p,z,z')_{z,z'}\right)\right],\\
  \Pi_{1,1}^{\zeta}\left(p,z,z'\right)_{i,z'}&=i\frac{p_{i}}{p^{2}}z^{d-1}\partial_{z}\left(z^{-
d+1}\Pi^{\zeta}_{1,1}(p,z,z')_{z,z'}\right),\\
  \Pi_{1,1}^{\zeta}\left(p,z,z'\right)_{z,j}&=-i\frac{p_{j}}{p^{2}}\left(z'\right)^{d-
1}\partial_{z'}\left(\left(z'\right)^{-d+1}\Pi^{\zeta}_{1,1}(p,z,z')_{z,z'}\right),\\
  \Pi_{d-1,1}^{\zeta}\left(p,z,z'\right)_{z,z'} &=
-\frac{p^{2}}{d-2}\left(\partial_{\Delta}\Pi_{\Delta,0}\left(p,z,z'\right)\right)\mid_{\Delta=d-1} \\
  & \qquad + \frac{4}{(d-2)\Gamma\left(2-\frac{d}{2}\right)\Gamma\left(\frac{d}{2}\right)}
\left(\zeta-1\right)
\,p^{2}\left(zz'\right)^{\frac{d}{2}}K_{\frac{d-2}{2}}\left(|p|z\right)K_{\frac{d-2}{2}}\left(|p|z'\right)\,,
 \end{split} \]

(B.17)

where we fixed the coefficients to match (4.19),(4.20) and (2.15).

#### [erez2-p2] paragraph

For $d=3$ and general $k$, we instead get (demanding (4.8) as boundary conditions)

\[ \begin{split} 
 \Pi_{1,1}^{\zeta,k}\left(p,z,z'\right)_{i,j}&=\frac{1}{2p}\Bigg[\frac{e^{-
\left|p\right|\left(z'+z\right)}}{\left(\frac{\kappa}{2\pi}\right)^{2}+\left(\frac{1}{16}\right)^{2}}\left(\le
ft(\left(\frac{1}{16}\right)^{2}-\left(\frac{\kappa}{2\pi}\right)^{2}\right)\left(\delta_{i,j}-
\frac{p_{i}p_{j}}{p^{2}}\right)-
\frac{\kappa}{16\pi}\,\varepsilon_{ijk}\frac{p_{k}}{\left|p\right|}\right)\\&\qquad +e^{-|p|\left|z'-
z\right|}\left(\delta_{i,j}-
\frac{p_{i}p_{j}}{p^{2}}\right)\Bigg]+\frac{p_{i}p_{j}}{\left|p\right|^{4}}\left[\left(zz'\right)^{2}\partial_
{z,z'}\left(\left(zz'\right)^{-
2}\Pi_{1,1}^{\zeta,k}\left(p,z,z'\right)_{z,z'}\right)\right]\\\Pi_{1,1}^{\zeta,k}\left(p,z,z'\right)_{i,z'}&=
-i\frac{p_{i}}{p^{2}}z^{2}\partial_{z}\left(z^{-
2}\Pi_{1,1}^{\zeta,k}\left(p,z,z'\right)_{z,z'}\right)\\\Pi_{1,1}^{\zeta,k}\left(p,z,z'\right)_{z,j}&=i\frac{p
_{j}}{p^{2}}\left(z'\right)^{2}\partial_{z'}\left(\left(z'\right)^{-
2}\Pi_{1,1}^{\zeta,k}\left(p,z,z'\right)_{z,z'}\right)\\\Pi_{1,1}^{\zeta,k}\left(p,z,z'\right)_{z,z'}&=\frac{\
left|p\right|}{2}zz'\Bigg[\left(e^{-
\left|p\right|\left(z+z'\right)}\text{Ei}\left(2\left|p\right|z\right)+e^{\left|p\right|\left(z+z'\right)}\tex
t{Ei}\left(-2\left|p\right|z'\right)\right)\\&\qquad\qquad -\left(e^{-\left|p\right|\left(z'-
z\right)}\text{Ei}\left(-2\left|p\right|z\right)+e^{-\left|p\right|\left(z-z'\right)}\text{Ei}\left(-
2\left|p\right|z'\right)\right)\\&\qquad\qquad
+2\frac{1-\zeta}{1+\left(\frac{16\kappa}{2\pi}\right)^{2}}\,e^{-\left|p\right|\left(z+z'\right)}\Bigg]\,.
 \end{split} \]

(B.18)

#### [erez2-p3] paragraph

Finally, the difference between $\Pi_{d-1,1}^{TT}\left(p,z,z'\right)$ and
$\Pi_{1,1}^{\zeta,k}\left(p,z,z'\right)$ can be written in terms of the momentum space bulk-to-boundary
propagators and the effective photon propagator (2.14) as

\[ \begin{split} 
&{G_{d-1,1}(p,z_1){}_{i|\mu} \langle A_i(p)A_{i'}(-p) \rangle_{\zeta,\infty,k}
G_{d-1,1}(-p,z_2)}{}_{i'|\mu'}\\
&\qquad=\frac{8\pi^\frac{3d}{2}}{\Gamma\left(\frac{d-2}{2}\right)\Gamma\left(d\right)}
\left(\Pi^{TT}_{d-1,1}(p,z_1,z_2)_{\mu|\mu'}-\Pi^{\zeta,k}_{1,1}(p,z_1,z_2)_{\mu|\mu'}\right)\,,
 \end{split} \]

(B.19)

which gives (4.18) in position space.

#### [footnotes] footnotes: Footnotes

Notes1This expectation is supported by lattice data for $d=3$ and all values of $N$ [26, 27], and by analytic
results in the large $N$ limit for all values of $d$ [25]. We will take (2.4) to be a formal definition of the
IR CFT, which should be valid for all values of $d$ and $N$ for which this CFT exists.

2At large $N$ one can also tune $\lambda=0$ to get a different IR CFT called the tricritical QED theory, but
for $d=3$ it is not clear if the fixed point exists at finite $N$.

3A gauge-invariant way of cancelling this term is to couple $N$ new scalars $\tilde\phi_I$ to $A_i$ with
opposite charge as $\phi_I$ and large mass $m$. We can then express $\tilde\phi_I$ in terms of bi-locals
$\tilde G$ in the usual way except the saddle point is now given by the massive free propagator
\[ \begin{split} 
\tilde G_0(x,0)=\frac{\Gamma(d/2-1)}{4\pi^{d/2}}\frac{e^{-m |x|}}{|x|^{d-2}}\,,
 \end{split} \]

(2.24)
 and the $J_iA_i$ terms in the $\tilde G$ version of (2.23) come with opposite sign. If we now take the limit
$m\to\infty$, then we see that $\tilde G_0(x_1,x_2)\to0$ except where $x_1\to x_2$ such that $\tilde G_0\to
G_0$, so the only effect of these new scalars is to cancel the $J_i[G_0]A_i$ term.

4In the special case $\zeta=1$ where we just have Landau gauge, these correlation functions are meaningful,
but they correspond to some complicated non-local gauge-invariant operators.

5For later convenience, we will not use the embedding space formalism used in [8].

6Note that while the harmonic basis resembles a three point function, it does not correspond to a correlator
in a physical CFT, and is simply a useful basis for conformally-covariant functions.

7In [8], a related map was also derived for $\eta(x_1,x_2)$ that do not satisfy this condition.

8We expect that $d=4$ should be an analytic continuation of our results for $d>4$, as is generally the case in
harmonic analysis [45], but we will not discuss this case in detail.

9When $\Delta=\tilde\Delta$, as can happen for the scalar bulk field in $d=4$, the second term will have a
$\log(z)$, which distinguishes its scaling in $z$ from the first term.

10For instance, when $J=1$ we can define $\delta^{TT}_{1,ij}(x)\equiv\int \frac{d^dp}{(2\pi)^d}
\,e^{ipx}(\delta_{ij}-\frac{p_ip_j}{|p|^2})$.

11A map for non-decaying $\Phi_0$ was also derived in [8].

12The CFT is believed to be unitary only for $2<d<4$.

13For massless propagators, the transversality constraint (4.13) can be interpreted as a bulk gauge choice in
a putative bulk gauge theory, which would be related to our bulk theory upon gauge-fixing.

14A similar identity in axial gauge was derived in [23].

15e-mail: ofer.aharony@weizmann.ac.il

16e-mail: iahs81@gmail.com

17e-mail: erez.urbach@weizmann.ac.il

#### [refs] references: References

References[1]J. M. Maldacena, “The Large N limit of superconformal field theories and supergravity,” Int. J.
Theor. Phys. 38 (1999) 1113–1133, hep-th/9711200. [Adv. Theor. Math. Phys.2,231(1998)].
[2]E. Witten, “Anti-de Sitter space and holography,” Adv. Theor. Math. Phys. 2 (1998) 253–291, hep-th/9802150.
[3]S. Gubser, I. R. Klebanov, and A. M. Polyakov, “Gauge theory correlators from noncritical string theory,”
Phys. Lett. B 428 (1998) 105–114, hep-th/9802109.
[4]L. Eberhardt, M. R. Gaberdiel, and R. Gopakumar, “Deriving the AdS$_{3}$/CFT$_{2}$ correspondence,” JHEP 02
(2020) 136, 1911.00378.
[5]A. Dei, M. R. Gaberdiel, R. Gopakumar, and B. Knighton, “Free field world-sheet correlators for ${\rm
AdS}_3$,” 2009.11306.
[6]L. Eberhardt, “AdS$_{3}$/CFT$_{2}$ at higher genus,” JHEP 05 (2020) 150, 2002.11729.
[7]H. Bertle, A. Dei, and M. R. Gaberdiel, “Stress-energy tensor correlators from the world-sheet,” JHEP 03
(2021) 036, 2012.08486.
[8]O. Aharony, S. M. Chester, and E. Y. Urbach, “A Derivation of AdS/CFT for Vector Models,” 2011.06328.
[9]I. R. Klebanov and A. M. Polyakov, “AdS dual of the critical O(N) vector model,” Phys. Lett. B550 (2002)
213–219, hep-th/0210114.
[10]S. R. Das and A. Jevicki, “Large N collective fields and holography,” Phys. Rev. D68 (2003) 044011, hep-
th/0304093.
[11]R. de Mello Koch, A. Jevicki, K. Jin, and J. P. Rodrigues, “$AdS_4/CFT_3$ Construction from Collective
Fields,” Phys. Rev. D 83 (2011) 025006, 1008.0633.
[12]R. de Mello Koch, A. Jevicki, J. a. P. Rodrigues, and J. Yoon, “Canonical Formulation of $O(N)$
Vector/Higher Spin Correspondence,” J. Phys. A 48 (2015), no. 10 105403, 1408.4800.
[13]R. de Mello Koch, A. Jevicki, J. P. Rodrigues, and J. Yoon, “Holography as a Gauge Phenomenon in Higher
Spin Duality,” JHEP 01 (2015) 055, 1408.1255.
[14]R. de Mello Koch, A. Jevicki, K. Jin, J. P. Rodrigues, and Q. Ye, “S=1 in O(N)/HS duality,” Class. Quant.
Grav. 30 (2013) 104005, 1205.4117.
[15]R. de Mello Koch, A. Jevicki, K. Suzuki, and J. Yoon, “AdS Maps and Diagrams of Bi-local Holography,” JHEP
03 (2019) 133, 1810.02332.
[16]M. A. Vasiliev, “Consistent equation for interacting gauge fields of all spins in (3+1)-dimensions,” Phys.
Lett. B243 (1990) 378–382.
[17]M. A. Vasiliev, “More on equations of motion for interacting massless fields of all spins in
(3+1)-dimensions,” Phys. Lett. B 285 (1992) 225–234.
[18]M. A. Vasiliev, “Higher spin gauge theories in four-dimensions, three-dimensions, and two-dimensions,”
Int. J. Mod. Phys. D 5 (1996) 763–797, hep-th/9611024.
[19]Y. Neiman, “Higher-spin gravity as a theory on a fixed (anti) de Sitter background,” JHEP 04 (2015) 144,
1502.06685.
[20]I. R. Klebanov and E. Witten, “AdS / CFT correspondence and symmetry breaking,” Nucl. Phys. B556 (1999)
89–114, hep-th/9905104.
[21]E. Witten, “Multitrace operators, boundary conditions, and AdS / CFT correspondence,” hep-th/0112258.
[22]E. Witten, “SL(2,Z) action on three-dimensional conformal field theories with Abelian symmetry,” in From
Fields to Strings: Circumnavigating Theoretical Physics: A Conference in Tribute to Ian Kogan, 7, 2003. hep-
th/0307041.
[23]C.-M. Chang, S. Minwalla, T. Sharma, and X. Yin, “ABJ Triality: from Higher Spin Fields to Strings,” J.
Phys. A 46 (2013) 214009, 1207.4485.
[24]M. Berkooz, A. Sever, and A. Shomer, “’Double trace’ deformations, boundary conditions and space-time
singularities,” JHEP 05 (2002) 034, hep-th/0112264.
[25]T. Appelquist, D. Nash, and L. C. R. Wijewardhana, “Critical Behavior in (2+1)-Dimensional QED,” Phys.
Rev. Lett. 60 (1988) 2575.
[26]A. K. Nguyen and A. Sudbø, “Topological phase fluctuations, amplitude fluctuations, and criticality in
extreme type-II superconductors,” Physical Review B 60 (Dec, 1999) 15307–15331.
[27]K. Kajantie, M. Laine, T. Neuhaus, A. Rajantie, and K. Rummukainen, “Duality and scaling in three-
dimensional scalar electrodynamics,” Nucl. Phys. B 699 (2004) 632–656, hep-lat/0402021.
[28]T. Appelquist and D. Nash, “Critical behavior in (2+1)-dimensional QCD,” Phys. Rev. Lett. 64 (Feb, 1990)
721–724.
[29]O. Aharony, G. Gur-Ari, and R. Yacoby, “d=3 Bosonic Vector Models Coupled to Chern-Simons Gauge Theories,”
JHEP 03 (2012) 037, 1110.4382.
[30]S. Giombi and X. Yin, “The Higher Spin/Vector Model Duality,” J. Phys. A 46 (2013) 214003, 1208.4036.
[31]O. Aharony, O. Bergman, and D. L. Jafferis, “Fractional M2-branes,” JHEP 11 (2008) 043, 0807.4924.
[32]D. J. Binder, S. M. Chester, and M. Jerdee, “ABJ Correlators with Weakly Broken Higher Spin Symmetry,”
JHEP 04 (2021) 242, 2103.01969.
[33]L. Fei, S. Giombi, and I. R. Klebanov, “Critical $O(N)$ models in $6-\epsilon$ dimensions,” Phys. Rev. D
90 (2014), no. 2 025018, 1404.1094.
[34]S. M. Chester, S. S. Pufu, and R. Yacoby, “Bootstrapping $O(N)$ vector models in 4 $< d <$ 6,” Phys. Rev.
D 91 (2015), no. 8 086014, 1412.7746.
[35]S. Giombi, R. Huang, I. R. Klebanov, S. S. Pufu, and G. Tarnopolsky, “The $O(N)$ Model in ${4 < d < 6}$ :
Instantons and complex CFTs,” Phys. Rev. D 101 (2020), no. 4 045013, 1910.02462.
[36]A. Jevicki and B. Sakita, “The Quantum Collective Field Method and Its Application to the Planar Limit,”
Nucl. Phys. B165 (1980) 511.
[37]S. M. Chester and S. S. Pufu, “Anomalous dimensions of scalar operators in QED$_{3}$,” JHEP 08 (2016) 069,
1603.05582.
[38]S. M. Chester, L. V. Iliesiu, M. Mezei, and S. S. Pufu, “Monopole Operators in $U(1)$ Chern-Simons-Matter
Theories,” JHEP 05 (2018) 157, 1710.00654.
[39]S. M. Chester, “Anomalous dimensions of monopole operators in scalar QED$_{3}$ with Chern-Simons term,”
JHEP 07 (2021) 034, 2102.07377.
[40]S. Giombi, I. R. Klebanov, and G. Tarnopolsky, “Conformal QED$_d$, $F$-Theorem and the $\epsilon$
Expansion,” J. Phys. A 49 (2016), no. 13 135403, 1508.06354.
[41]A. Kapustin, “Wilson-’t Hooft operators in four-dimensional gauge theories and S-duality,” Phys. Rev. D 74
(2006) 025005, hep-th/0501015.
[42]S. M. Chester, M. Mezei, S. S. Pufu, and I. Yaakov, “Monopole operators from the $4-\epsilon$ expansion,”
JHEP 12 (2016) 015, 1511.07108.
[43]V. Borokhov, A. Kapustin, and X.-k. Wu, “Topological disorder operators in three-dimensional conformal
field theory,” JHEP 11 (2002) 049, hep-th/0206054.
[44]S. Giombi and X. Yin, “Higher Spin Gauge Theory and Holography: The Three-Point Functions,” JHEP 09 (2010)
115, 0912.3462.
[45]S. Caron-Huot, “Analyticity in Spin in Conformal Theories,” JHEP 09 (2017) 078, 1703.00278.
[46]N. Craigie, V. Dobrev, and I. Todorov, “Conformally Covariant Composite Operators in Quantum
Chromodynamics,” Annals Phys. 159 (1985) 411–444.
[47]M. R. Gaberdiel, R. Gopakumar, and A. Saha, “Quantum $W$-symmetry in $AdS_3$,” JHEP 02 (2011) 004,
1009.6087.
[48]M. R. Gaberdiel, D. Grumiller, and D. Vassilevich, “Graviton 1-loop partition function for 3-dimensional
massive gravity,” JHEP 11 (2010) 094, 1007.5189.
[49]R. K. Gupta and S. Lal, “Partition Functions for Higher-Spin theories in AdS,” JHEP 07 (2012) 071,
1205.1130.
[50]T. Hartman and L. Rastelli, “Double-trace deformations, mixed boundary conditions and functional
determinants in AdS/CFT,” JHEP 01 (2008) 019, hep-th/0602106.
[51]S. Giombi and X. Yin, “On Higher Spin Gauge Theory and the Critical O(N) Model,” Phys. Rev. D 85 (2012)
086005, 1105.4011.
[52]M. S. Costa, V. Gonçalves, and J. Penedones, “Spinning AdS Propagators,” JHEP 09 (2014) 064, 1404.5625.
[53]S. Giombi, S. Minwalla, S. Prakash, S. P. Trivedi, S. R. Wadia, and X. Yin, “Chern-Simons Theory with
Vector Fermion Matter,” Eur. Phys. J. C 72 (2012) 2112, 1110.4386.
[54]V. K. Dobrev, G. Mack, I. T. Todorov, V. B. Petkova, and S. G. Petrova, “On the Clebsch-Gordan Expansion
for the Lorentz Group in n Dimensions,” Rept. Math. Phys. 9 (1976) 219–246.
[55]V. K. Dobrev, G. Mack, V. B. Petkova, S. G. Petrova, and I. T. Todorov, “Harmonic Analysis on the
n-Dimensional Lorentz Group and Its Application to Conformal Quantum Field Theory,” Lect. Notes Phys. 63
(1977) 1–280.
[56]J. Penedones, “Writing CFT correlation functions as AdS scattering amplitudes,” JHEP 03 (2011) 025,
1011.1485.
[57]E. D’Hoker and D. Z. Freedman, “Gauge boson exchange in AdS(d+1),” Nucl. Phys. B 544 (1999) 612–632, hep-
th/9809179.
