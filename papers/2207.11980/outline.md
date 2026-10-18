# Outline of: Onset of Quantum Chaos in Random Field Theories

Abstract:

We study the quantum Lyapunov exponent $\lambda_L$ in theories with spacetime-independent disorder. We first derive self-consistency equations for the two- and four-point functions for products of $N$ models coupled by disorder at large $N$, generalizing the equations appearing in SYK-like models. We then study families of theories in which the disorder coupling is an exactly marginal deformation, allowing us to follow $\lambda_L$ from weak to strong coupling. We find interesting behaviors, including a discontinuous transition into chaos, mimicking classical KAM theory.

# [root] paper
## [introduction] section: Introduction
### [introduction-p1] paragraph

Systems with disorder are ubiquitous in nature, and display a wide range of interesting physical phenomena.
Disorder can sometimes be modeled by introducing random couplings, and averaging over these random couplings
can lead to simplifications which allow for exact computations, at least when the number of degrees of freedom
is parametrically large. A notable example is the Sachdev–Ye–Kitaev (SYK) model, in which (nearly) conformal
symmetry is restored at low energies Sachdev and Ye (1993); Kitaev (2015); Maldacena and Stanford (2016);
Kitaev and Suh (2018), and such averages allow for the computation of the quantum chaos exponent $\lambda_L$.
The latter is defined by the fastest growing exponential mode in the double-commutator $\langle
[U(t),W(0)]^2\rangle_\beta\sim e^{\lambda_L t}$ for generic operators $U,W$, over an appropriate time scale,
with temperature $1/\beta$ Larkin and Ovchinnikov (1969).

### [introduction-p2] paragraph

The SYK model consists of $N$ free quantum mechanical fermions deformed by a relevant all-to-all spacetime-
independent disordered interaction. Generalizations have appeared which consist of $N$ copies of other free
theories with similar interactions Murugan et al. (2017); Fu et al. (2017); Peng (2018); Bulycheva (2018);
Chang et al. (2021); Popov (2020); Gross and Rosenhaus (2017); Lian et al. (2019). In this letter we study
quantum chaos in a more general setting by studying $N$ copies of a general core model $\mathcal{Q}$ (which
can be a quantum field theory or a spin system), deformed by a spacetime-independent all-to-all interaction.
In particular, we eventually focus on $Q$ being a conformal field theory (CFT) in 0+1 or in higher dimensions,
and with an exactly marginal disorder interaction. In such a setup we have better control over the space of
couplings over which we are averaging, eliminating the complications of the renormalization group (RG) and
without having to resort to strong coupling.

### [introduction-p3] paragraph

The theories we study are of the form

\[ \mathcal{Q}^N+\sum_{i_1\neq ...\neq i_q}^N J_{i_1...i_q}\mathcal{O}_{i_1}...\mathcal{O}_{i_q}\;, \]

(1)

where $\mathcal{Q}^N$ denotes $N$ decoupled copies of the model $\mathcal{Q}$, $\mathcal{O}_i$ with
$i=1,...,N$ are the $N$ copies of a local operator $\mathcal{O}$ in $\mathcal{Q}$, and $J_{i_1...i_q}$ are
Gaussian random variables with variance

\[ \langle J_{i_1...i_q}^2\rangle= \frac{J^2(q-1)!}{N^{q-1}}\;. \]

(2)

In the case where $\mathcal{Q}$ is a CFT, we will take $\mathcal{O}$ to be a primary operator of this core
CFT, and equation (1) should be interpreted in conformal perturbation theory in $J$. We call such theories
disordered CFTs; the simplest example of this setup is the SYK model itself, as a disordered free fermion
theory.

### [introduction-p4] paragraph

We will first derive self-consistency equations for the two- and four-point functions of $\mathcal{O}_i$ at
leading order in $1/N$ for general disordered CFTs. These extend known results for disordered free theories
like the SYK model Maldacena and Stanford (2016); Kitaev and Suh (2018)), and for spin systems Bray and Moore
(1980). We will also discuss similar results for the double-commutator (defined in (7) below). Although these
self-consistency equations are complicated, they are tractable in perturbation theory in $J$ and allow us to
establish the existence of a kernel structure from which we can extract the chaos exponent $\lambda_L$, which
is the rate of growth of a double commutator. The latter is given by the fastest growing eigenvector (with
eigenvalue 1) of a specific integral kernel $K_R$ (see equation (9)), as long as this rate of growth is indeed
positive Kitaev (2015); Kitaev (2015); Larkin and Ovchinnikov (1969). We will denote by
$\lambda_L^{\text{ker}}$ the putative chaos exponent read from the diagonalization $K_R$.

### [fig-discontinuouschaos] figure: Figure 1

Figure 1. The behaviors we find for the chaos exponent as a function of an exactly marginal disorder
deformation $J$: (a) continuous and (b) discontinuous. $\lambda_L^{\text{ker}}$ corresponds to the dashed line
and $\lambda_L$ to the solid line.

### [introduction-p5] paragraph

We will be interested in computing the chaos exponent $\lambda_L$ as a function of $J$, as it is varied from
weak to strong coupling. The diagonalization of $K_R$ is a difficult process, which can usually be done only
when conformal invariance is restored. Normally, the disorder is a relevant deformation. To compute the chaos
one first flow to the IR CFT (which is equivalent to take $J=\infty$) and find the chaos exponent there
Murugan et al. (2017). In this work we focus on cases where the averaged interacting theory is conformally
invariant for all $J$. This can be done by demanding that the disorder interaction itself be exactly marginal,
in which case the theory is conformally invariant for every realization of the couplings, and the space of
$J$’s forms a conformal manifold 1. The disorder average is then simply a non-uniform average over this
conformal manifold, with no RG-related complications (for recent discussions of averages over conformal
manifolds see Maloney and Witten (2020); Afkhami-Jeddi et al. (2021), and for the marginal case see Berkooz
et al. (2017)).

### [introduction-p6] paragraph

Surprisingly, we will find models where $\lambda_L^{\text{ker}}(J)$ is negative at weak coupling. This signals
a breakdown of the approximations involved in the computation, and so in this case the true chaos exponent
simply vanishes, $\lambda_L= 0$. In other words, we have

\[ \lambda_L=\max(0,\lambda_L^{\text{ker}})\;. \]

(3)

As a result, there are two possible behaviors for the onset of chaos: either the theory undergoes a continuous
transition into chaos as in figure 1a or a discontinuous transition as in figure 1b, corresponding to whether
$\lambda_L^{\text{ker}}$ is non-negative or negative at small enough $J$ respectively.2

### [introduction-p7] paragraph

The discontinuous transition into chaos is a surprising result, and it is tempting to compare it to similar
results in classical chaos, the most famous one being the KAM theorem. In order to sharpen the comparison, we
also discuss what a single core CFT should obey in order for the transition into chaos to be discontinuous.
Similar works on the onset of quantum chaos include Stanford (2016); de Mello Koch et al. (2019); Chowdhury
and Swingle (2017); Steinberg and Swingle (2019); Maldacena and Stanford (2016); Peng (2018), and Lian et al.
(2019); Hu and Lian (2021) are especially relevant.

### [introduction-p8] paragraph

We will apply our formalism to two classes of examples where the disorder interaction is exactly marginal. The
first class is disordered generalized free fields in $1$d (following Gross and Rosenhaus (2017)) and in $2$d.
The second class is the disordered $\mathcal{N}=2$ supersymmetric (SUSY) $A_{q-1}$ minimal models. In
practice, we will only discuss the simplest case of the $A_2$ minimal model here. We will find a discontinuous
transition in the former and a continuous transition in the latter.

### [introduction-p9] paragraph

More details and discussions on the computations and results can be found in the companion paper Berkooz
et al. (2021).

## [disorder-around-a-nontrivial-cft] section: Disorder around a nontrivial CFT
### [the-kernel-structure-of-the-four-point-function] section: The kernel structure of the four-point function
#### [the-kernel-structure-of-the-four-point-function-p1] paragraph

We start by writing a self-consistency equation for the averaged two-point function of (1),

\[ G(x)= \langle \mathcal{O}_i(x)\mathcal{O}_i(0) \rangle\;. \]

(4)

Using the $G-\Sigma$ formalism Maldacena and Stanford (2016); Kitaev (2015), it can be shown that $G$ obeys a
generalized Schwinger-Dyson (SD) equation at leading order in $1/N$, which appears diagrammatically in figure
2a.

#### [fig-sdeqsfull] figure: Figure 2

Figure 2. (a) The SD equations. $G$ insertions appear as red lines, and black dots denote insertions of the
deformation (1). (b) Examples of $n_s$, The subtracted $n$-point functions. Dashed lines connect to the
external points, and numerical factors indicate symmetry factors. The blue numbers inside the brackets denote
possible ways of permuting the legs.

#### [the-kernel-structure-of-the-four-point-function-p2] paragraph

The equation includes subtracted $n$-point functions denoted by “$n_s$”, which are combinations of the
standard core CFT $n$-point functions with additional theory-independent subtractions which can be derived
order-by order in $n$ Berkooz et al. (2021). The first few subtracted $n$-point functions (assuming
$\mathcal{O}_i$ are real) are shown in figure 2b. Generalizations to complex $\mathcal{O}_i$ exist, and also
to superfields (in which case the diagrams correspond to supergraphs).

#### [the-kernel-structure-of-the-four-point-function-p3] paragraph

The contributions to the averaged connected four-point function

\[ C=\frac{1}{N^2} \sum_{i,j}(\langle\mathcal{O}_i\mathcal{O}_i\mathcal{O}_j\mathcal{O}_j\rangle-\langle \mathcal{O}_i\mathcal{O}_i \rangle\langle \mathcal{O}_j\mathcal{O}_j \rangle) \]

(5)

also have a simple form, and obey an iterative ladder structure similar to the case of disordered free fields:

\[ C=\sum_{n=0}^\infty K^n F_0\;, \]

(6)

where the kernel $K$ and the initial diagram $F_0$ are defined in figure 3a. The definition requires new
subtracted $n$-point functions called $n_s'$, which are again theory-independent Berkooz et al. (2021). The
first few $n_s'$ for real $\mathcal{O}_i$ appear in figure 3b.

#### [fig-fullkernel] figure: Figure 3

Figure 3. (a) The kernel $K$ and initial diagram $F_0$ for general disordered CFTs. Red lines denote full
propagators $G$, and black dots denote insertions of the disorder interaction, with $q-2$ red propagators
between each pair. (b) Examples of correlation functions $n_s'$. Dashed lines corresponds to external points,
while solid lines are connected via $\Sigma$’s defined in figure 2a.

#### [the-kernel-structure-of-the-four-point-function-p4] paragraph

Some comments are in order. First, although the kernel $K$ is very complicated, knowing that an iterative
ladder structure exists for the four-point function is already an important result since it allows for a
systematic computation of $\lambda_L$, as we now discuss. Second, although a full solution of the two- and
four-point functions requires knowing all $n$-point functions of the core CFT, a solution to order $J^{2n}$ in
perturbation theory in $J$ only requires knowing the $2m$-point functions for $m\leq n+1$.

### [the-double-commutator-and-chaos] section: The double-commutator and chaos
#### [the-double-commutator-and-chaos-p1] paragraph

A similar analysis also applies to the computation of the double-commutator:

\[ \begin{split}
    W_R(t_1,t_2) = \frac{1}{N^2} \sum_{i,j=1}^N &\langle [\mathcal{O}_i(\beta/2) ,\mathcal{O}_j(\beta/2+i
t_2)] \\
    &\cdot [\mathcal{O}_i(0), \mathcal{O}_j(i t_1)]
    \rangle,
\end{split} \]

(7)

where we suppress the spatial positions. In chaotic theories, at large Lorentzian times $t_1,t_2$, the double
commutator is expected to grow exponentially:

\[ \lim_{t_1,t_2\rightarrow \infty} W_R(t_1,t_2) \sim \frac{1}{N} \exp(+\lambda_L (t_1+t_2)/2)\;. \]

(8)

#### [the-double-commutator-and-chaos-p2] paragraph

Since the double commutator can be written in terms of analytically continued $4$-point functions (5), (7)
satisfies a “retarded” version of the kernel structure of figure 3a:

\[ W_R=\sum_{n=0}^\infty K_R^n F_0 \ \Longrightarrow\ (1-K_R)W_R = F_0\;, \]

(9)

with $K_R$ the retarded kernel Kitaev (2015). The retarded kernel is composed of the same diagrams as in
figure 3a, where one plugs in specific analytic continuations in time of the $n$-point functions.

#### [the-double-commutator-and-chaos-p3] paragraph

If $\lambda_L>0$, the ladder structure (however complicated) allows us to compute it in cases where the
averaged correlator has conformal symmetry (see Murugan et al. (2017) for a review). This is done by finding
the largest solution $\lambda_L^{\text{ker}}$ of the equation $k_R(\lambda_L^{\text{ker}})=1$, where
$k_R(\lambda)$ are the eigenvalues of the retarded kernel $K_R$. If $\lambda_L^{\text{ker}}>0$ then we can
identify $\lambda_L=\lambda_L^{\text{ker}}$, and otherwise we learn that $\lambda_L=0$.

#### [the-double-commutator-and-chaos-p4] paragraph

Importantly, if $J$ is exactly marginal, $k_R(\lambda_L)$ can be found perturbatively in $J$. As a result, one
can compute $\lambda_L^{\text{ker}}(J)$ in orders of $J$ by using finitely many core CFT correlation functions
at every order. The leading order of the equation is explicitly

\[ \begin{split}
    & k_R(\lambda) = \frac{J^2}{4} \int d^2 x_3 d^2 x_4 \exp(\lambda/2 (t_3+t_4-t_1-t_2)) \\
    &\cdot \langle [\mathcal{O}(\beta/2+i t_2), \mathcal{O}(\beta/2+i t_4)]
    [\mathcal{O}(i t_1), \mathcal{O}(i t_3)]\rangle_0
    \\
    &\cdot \frac{G_{lr,\Delta(q-1)+\frac{\lambda}{2}}(3,4)}{G_{lr,\Delta+\frac{\lambda}{2}}(1,2)} +O(J^4)\;,
\end{split} \]

(10)

where $\langle \cdot \rangle_0$ denotes an expectation value at $J=0$ (i.e. of the core CFT). The integration
range of the points $3,4$ is over the past light-cone of the points $1,2$ respectively, and $G_{lr,\Delta}$ is
the analytically continued cylinder $2$-point function:

\[ G_{lr,\Delta}(1,2) = \frac{1}{\left( 4 
    \cosh\left(\frac{t_{12}-x_{12}}{2}\right)
    \cosh\left(\frac{t_{12}+x_{12}}{2}\right)
    \right)^\Delta}. \]

(11)

#### [the-double-commutator-and-chaos-p5] paragraph

The expansion in $J$ can also be used to determine whether the transition into chaos would be continuous or
discontinuous (see figure 1). This requires finding the sign of $\lambda_L^{\text{ker}}$ in the limit $J=
0^+$. Using the leading contribution to $k_R$ in orders of $J^2$ (10), it is easy to see that the exponent
$\lambda_L^{\text{ker}}(J= 0^+)$ is given by the maximal $\lambda$ for which the integral (10) diverges. If
the integral diverges at a positive (negative) value of $\lambda$, we have a continuous (discontinuous)
transition into chaos.

#### [the-double-commutator-and-chaos-p6] paragraph

At $J=0$, the kernel vanishes, and so it is not clear that $\lambda_L(J=0)$ is related to chaos. Instead, at
$J=0$ we find $N$ decoupled core CFTs, and we expect

\[ \begin{split}
    \lim_{t_1,t_2\rightarrow \infty} W_R(t_1,t_2)\mid_{J=0} \;\sim \frac{1}{N} \exp(+\lambda_L^0 (t_1+t_2)/2)
\end{split} \]

(12)

for some $\lambda_L^0$. Note that the CFTs are decoupled and so $\lambda_L^0$ is a property of a single core
CFT. However, we emphasize that it is not a chaos exponent in a single core CFT (as we take $t_1,t_2$ to be
larger then any timescale of the core CFT); in fact, for unitary theories in $2d$ it is always non-positive,
$\lambda_L^0\le 0$ Caron-Huot (2017).

#### [the-double-commutator-and-chaos-p7] paragraph

Surprisingly, under reasonable physical assumptions it can be shown that $\lambda_L^{\text{ker}}(J=0^+)$ and
$\lambda_L^0$ are equal Berkooz et al. (2021). This amounts to showing that the integral (10) diverges for
$\lambda \le \lambda_L^0$ due to the large (negative) $t_3,t_4$ regime of the integrand. Putting these pieces
together, we claim that $\lambda_L^{\text{ker}}(J)$ satisfies

\[ \lambda_L^{\text{ker}}(J=0^+) = \lambda_L^0. \]

(13)

The LHS is calculated through the kernel equation $k_R(\lambda)=1$ in the limit $J=0^+$, and the RHS is a
property of the core CFT. We can interpret the result by noticing that $\lambda_L^0$ describes the core CFT
double-commutator behavior at large time scales. At arbitrarily weak coupling this behavior seems to control
the $1\ll t \ll \log N$ behavior of the disordered theory double-commutator. The result is striking: in order
to determine the type of transition into chaos, it is enough to find (the sign of) $\lambda_L^0$ in a single
core CFT. Below we give one example for each type of transition into chaos. In both cases we find that our
conjecture (13) holds.

## [examples-of-the-onset-of-chaos] section: Examples of the Onset of chaos
### [disordered-generalized-free-fields] section: Disordered generalized free fields
#### [disordered-generalized-free-fields-p1] paragraph

We now discuss our first class of examples with exactly marginal chaos, which are the disordered generalized
free fields in $1$d and in $2$d. Generalized free fields (GFFs) are non-local theories with no energy-momentum
tensor, but can be obtained by specific large-flavor limits of local theories, and are good toy-models for
more complicated theories. Conformal invariance allows us to set the inverse temperature to be $\beta=2\pi$ in
the following.

#### [disordered-generalized-free-fields-p2] paragraph

In $1$d, the generalized free fermion model is called the “cSYK” model and was introduced in Gross and
Rosenhaus (2017). Explicitly, the action is

\[ S=S_0+S_\text{SYK} \]

(14)

with

\[ \begin{split}
S_0&=-\Delta \sum_{i=1}^n  \int d \tau_1 d \tau_2 \chi_i\left(\tau_1\right)
\frac{\operatorname{sgn}\left(\tau_1-\tau_2\right)}{\left|\tau_1-\tau_2\right|^{2-2 \Delta}}
\chi_i\left(\tau_2\right)\;,\\
S_\text{SYK}&=\frac{i^{\frac{q}{2}}}{q !} \sum_{i_1, \ldots, i_{q}=1}^n  \int d \tau J_{i_1 i_2 \ldots i_{q}}
\chi_{i_1} \chi_{i_2} \cdots \chi_{i_{q}}\;.
\end{split} \]

(15)

Here, $J_{i_1...i_q}$ are Gaussian random variables with variance $\langle J_{i_1...i_q}^2\rangle=
\frac{J^2(q-1)!}{N^{q-1}}$. Choosing $\Delta=1/q$, the deformation becomes classically marginal, and it is
argued in Gross and Rosenhaus (2017) that it is exactly marginal at leading order in $1/N$.

#### [disordered-generalized-free-fields-p3] paragraph

The two- and four-point functions of $\chi_i$ for this model were found in Gross and Rosenhaus (2017). It is
simple to extend the results also to the double-commutator. One finds that the corresponding retarded kernel
$K_R^{\text{cSYK}}$ has eigenvalues

\[ k^{\text{cSYK}}_R(\lambda)=\left(\frac{\bar{b}(J)}{\bar b(J\to \infty)}\right)^{q}\frac{\Gamma(3-2 \Delta) \Gamma(2 \Delta+\lambda)}{\Gamma(1+2 \Delta) \Gamma(2-2 \Delta+\lambda)}\;, \]

(16)

where $\bar b(J)$ solves the equation

\[ \frac{\bar{b}^{q}}{1-2 \bar{b}}=\frac{1}{J^2 \psi(1-\Delta) \psi(\Delta)},\; \psi(\Delta) \equiv 2 \cos (\pi \Delta) \Gamma(1-2 \Delta). \]

(17)

#### [disordered-generalized-free-fields-p4] paragraph

$\lambda_L^{\text{ker}}$ is found by taking the largest solution to $k^{\text{cSYK}}_R(\lambda)=1$. The result
for $\Delta=1/4$ appears in figure 4, and similar results apply for other $\Delta$.

#### [fig-GFFchaos] figure: Figure 4

Figure 4. The chaos exponent $\lambda_L(J)$ at $\Delta=1/4$ for disordered GFFs in QM and for SUSY disordered
GFFs in $2d$. Dashed lines represent $\lambda_L^{\text{ker}}$ and solid lines represent $\lambda_L$.

#### [disordered-generalized-free-fields-p5] paragraph

At any $\Delta$, $\lambda_L^{\text{ker}}$ approaches the maximal value $\lambda_L=1$ Maldacena et al. (2016)
at large $J$ as in the SYK model. More relevant to this study, $\lambda_L^{\text{ker}}$ approaches $-2\Delta$
at $J=0$ (corresponding to the dashed red line), and so becomes negative at small $J$ for any $\Delta>0$. As
discussed above, we cannot identify $\lambda_L^{\text{ker}}$ with $\lambda_L$ when the former is negative, but
we immediately learn that $\lambda_L= 0$ in this regime. We thus conclude that there is no chaos at small
enough $J$, corresponding to $\lambda_L$ denoted by the solid red line. We thus find a discontinuous
transition into chaos, as in figure 1b. We also comment that the long time exponent $\lambda_L^0$ of a single
core CFT is equal to $\lambda_L^0=-2\Delta$, which matches $\lambda_L^{\text{ker}}(J=0^+)$, and so the
conjecture (13) is obeyed.

#### [disordered-generalized-free-fields-p6] paragraph

The same analysis can be done for disordered GFFs in 2d. In this case we choose to work with $\mathcal{N}=2$
SUSY GFFs, since this results in an exact conformal manifold even at finite $N$. The model consists of $N$
generalized free chiral superfields $\Phi_i$ of dimension $\Delta=1/q$, coupled via the superpotential

\[ W=\sum_{i_1\neq ...\neq i_q}^NJ_{i_1...i_q}\Phi_{i_1}...\Phi_{i_q}\;. \]

(18)

The computation is very similar, and the results appear in figure 4. At large enough $J$, the chaos exponent
for any $\Delta$ approaches the result in the $2$d SUSY versions of the SYK model Murugan et al. (2017);
Bulycheva (2018). In addition, we again find that $\lambda_L^{\text{ker}}$ approaches $-2\Delta$ as $J\to
0^+$, and so for small enough $J$ $\lambda_L^{\text{ker}}$ is negative for any $\Delta>0$. As a result, we
again find a discontinuous transition into chaos for any $\Delta>0$. We also find once again that the
conjecture (13) is obeyed.

### [disordered-minimal-models] section: Disordered minimal models
#### [disordered-minimal-models-p1] paragraph

We now discuss the disordered 2d $\mathcal{N}=2$ minimal models. A single core CFT in this case consists of an
$\mathcal{N}=2$ SUSY $A_{q-1}$ minimal model, which can be represented by a single chiral superfield $\Phi$
and superpotential $W=\Phi^q$. The full disordered theory is then

\[ W=\sum_{i=1}^N\Phi_{i}^q+\sum_{i_1\neq....\neq i_q} J_{i_1...i_q}\tilde{\Phi}_{i_1}...\tilde{\Phi}_{i_q}\;. \]

(19)

We emphasize that we interpret this equation in conformal perturbation theory in $J$ around $N$ copies of the
$A_{q-1}$ minimal model, where $\tilde\Phi$ is the chiral operator of dimension $1/q$ which appears in
$A_{q-1}$. Since the CFT at $J=0$ has no continuous non-R global symmetries, every classically marginal
operator is exactly marginal Green et al. (2010); Kol (2002); Kol (2010), and so each deformation
$J_{i_1...i_q}$ for $i_1\neq...\neq i_q$ is exactly marginal. Thus each realization of the model is conformal,
and as a result averaged correlators of $\tilde\Phi_i$ will also be conformal (even at finite $N$).

#### [disordered-minimal-models-p2] paragraph

We can now attempt to compute $\lambda_L(J)$ in perturbation theory. This computation is generically
difficult, and so we focus on the case $q=3$, where a core CFT has central charge $c=1$ and so corresponds to
the free compact boson at a specific radius. We can identify the operators $\tilde{\Phi}_i$ in terms of vertex
operators of the $c=1$ boson, and as a result we can read off all $n$-point functions of the $\tilde{\Phi}_i$.
Using this result to compute the leading contribution to the retarded kernel at small $J$ given in (10), we
find that at small $J$ the exponent $\lambda_L^{\text{ker}}$ approaches zero. As a result, we expect a
continuous transition into chaos in this model, as in figure 1a. In particular, the value of $\lambda_L^0$ in
a single $A_2$ minimal model is also zero, so that the conjecture (13) is again obeyed.

## [acknowledgments] section: Acknowledgments
### [acknowledgments-p1] paragraph

We would like to thank O. Aharony, N. Brukner, C. Choi, Y. Jia, R.R. Kalloor, B. Lian, J. Maldacena, O.
Mamroud, M. Mezei, M. Rangamani, V. Rosenhaus, D. Tong and M. Watanabe for useful conversations. This work was
partly funded by an Israel Science Foundation center for excellence grant (grant number 2289/18), by grant no.
2018068 from the United States-Israel Binational Science Foundation (BSF), by the Minerva foundation with
funding from the Federal German Ministry for Education and Research, by the German Research Foundation through
a German-Israeli Project Cooperation (DIP) grant “Holography and the Swampland", and by a research grant from
Martin Eisenstein. MB is the incumbent of the Charles and David Wolfson Professorial Chair of Theoretical
Physics.

### [footnotes] footnotes: Footnotes

Notes1It is important that $\mathcal{O}$ itself does not obtain an anomalous dimension as a function of $J$,
which will be the case in the examples in this letter.

2We implicitly assumed that the chaos exponent increases monotonically with the strength of the disorder $J$.
As we start with N decoupled systems it is reasonable, but not necessarily true. For example, an integrable
deformation keeps the exponent at zero, but these are hard to come by in this context.

### [refs] references: References

References S.  Sachdev and J.  Ye,  Phys. Rev. Lett.  70, 3339 ( 1993)
 A.  Kitaev, “ A simple model of quantum holography,”  ( 2015 a), talks at KITP
 J.  Maldacena and D.  Stanford,  Phys. Rev. D  94, 106002 ( 2016), arXiv:1604.07818 [hep-th]
 A.  Kitaev and S. J. Suh,  JHEP  05, 183 ( 2018), arXiv:1711.08467 [hep-th]
 A. I. Larkin and Y. N. Ovchinnikov, Journal of Experimental and Theoretical Physics ( 1969)
 J.  Murugan, D.  Stanford, and E.  Witten,  JHEP  08, 146 ( 2017), arXiv:1706.05362 [hep-th]
 W.  Fu, D.  Gaiotto, J.  Maldacena, and S.  Sachdev,  Phys. Rev. D  95, 026009 ( 2017), [Addendum: Phys.Rev.D
95, 069904 (2017)], arXiv:1610.08917 [hep-th]
 C.  Peng,  JHEP  12, 065 ( 2018), arXiv:1805.09325 [hep-th]
 K.  Bulycheva,  JHEP  04, 036 ( 2018), arXiv:1801.09006 [hep-th]
 C.-M. Chang, S.  Colin-Ellerin, C.  Peng, and M.  Rangamani, ( 2021), arXiv:2108.00027 [hep-th]
 F. K. Popov,  Phys. Rev. D  101, 026020 ( 2020), arXiv:1907.02440 [hep-th]
 D. J. Gross and V.  Rosenhaus,  JHEP  07, 086 ( 2017), arXiv:1706.07015 [hep-th]
 B.  Lian, S. L. Sondhi, and Z.  Yang,  JHEP  09, 067 ( 2019), arXiv:1906.03308 [hep-th]
 A. J. Bray and M. A. Moore,  J. Phys. C: Solid State Phys.  13, L655 ( 1980)
 A.  Kitaev, “ Hidden correlations in the hawking radiation and thermal noise,”  ( 2015 b), talks at KITP
It is important that $\protect \mathcal {O}$ itself does not obtain an anomalous dimension as a function of
$J$, which will be the case in the examples in this letter.
 A.  Maloney and E.  Witten,  JHEP  10, 187 ( 2020), arXiv:2006.04855 [hep-th]
 N.  Afkhami-Jeddi, H.  Cohn, T.  Hartman, and A.  Tajdini,  JHEP  01, 130 ( 2021), arXiv:2006.04839 [hep-th]
 M.  Berkooz, P.  Narayan, M.  Rozali, and J.  Simón,  JHEP  09, 057 ( 2017), arXiv:1702.05105 [hep-th]
We implicitly assumed that the chaos exponent increases monotonically with the strength of the disorder $J$.
As we start with N decoupled systems it is reasonable, but not necessarily true. For example, an integrable
deformation keeps the exponent at zero, but these are hard to come by in this context.
 D.  Stanford,  JHEP  10, 009 ( 2016), arXiv:1512.07687 [hep-th]
 R.  de Mello Koch, W.  LiMing, H. J. R. Van Zyl, and J. a. P. Rodrigues,  Phys. Lett. B  793, 169 ( 2019),
arXiv:1902.06409 [hep-th]
 D.  Chowdhury and B.  Swingle,  Phys. Rev. D  96, 065005 ( 2017), arXiv:1703.02545 [cond-mat.str-el]
 J.  Steinberg and B.  Swingle,  Phys. Rev. D  99, 076007 ( 2019), arXiv:1901.04984 [cond-mat.str-el]
 Y.  Hu and B.  Lian, ( 2021), arXiv:2109.13263 [cond-mat.str-el]
 M.  Berkooz, A.  Sharon, N.  Silberstein, and E. Y. Urbach, ( 2021), arXiv:2111.06108 [hep-th]
 S.  Caron-Huot,  JHEP  09, 078 ( 2017), arXiv:1703.00278 [hep-th]
 J.  Maldacena, S. H. Shenker, and D.  Stanford,  JHEP  08, 106 ( 2016), arXiv:1503.01409 [hep-th]
 D.  Green, Z.  Komargodski, N.  Seiberg, Y.  Tachikawa, and B.  Wecht,  JHEP  06, 106 ( 2010),
arXiv:1005.3546 [hep-th]
 B.  Kol,  JHEP  09, 046 ( 2002), arXiv:hep-th/0205141
 B.  Kol, ( 2010), arXiv:1005.4408 [hep-th]
