# Outline of: On type II string theory on AdS_3 S^3 T^4 and symmetric orbifolds

Abstract:

We discuss in detail the $1+1$-dimensional superconformal field theory dual to type II string theory on $AdS_3\times S^3\times T^4$, emphasizing the string theoretic aspects of this duality. For one unit of NS-NS 5-brane flux ($Q_5=1$), this string theory has been suggested to be dual to a grand-canonical ensemble of $T^{4N}/S_N$ free symmetric orbifold CFTs. We show how the string genus expansion emerges to all orders for the free orbifold grand-canonical correlation functions. We also discuss how the strong coupling limit of the NS-NS string theory arises (even at large $N$) in the free orbifold description, and argue why this limit does not have a weakly coupled R-R description. The dual CFT includes (for all values of $Q_5$) an extra $T^4$ factor that is decoupled from perturbative string theory. We discuss the exactly marginal deformations that relate the different values of $Q_5$, including the precise $J{\bar J}$ deformations mixing this extra $T^4$ with the symmetric orbifold.

# [root] paper
## [sec-intro] section: 1 Introduction and summary
### [sec-intro-p1] paragraph

The duality between type II string theory on $AdS_3\times S^3\times T^4$ (which can be viewed as the near-
horizon limit of $Q_1$ D1-branes and $Q_5$ D5-branes wrapped on $T^4$) and a specific $1+1$-dimensional ${\cal
N}=(4,4)$ superconformal field theory (SCFT) (the “D1-D5 SCFT") is one of the original examples of the AdS/CFT
correspondence [1, 2]. It shares many features with other examples of the AdS/CFT correspondence; for $Q_1 \gg
Q_5 \gg 1$ the theory has one limit of its continuous parameters where it is described by string theory on a
weakly coupled and weakly curved background, and another limit where it is a free field theory (a free
symmetric orbifold $(T^4)^{Q_1 Q_5} / S_{Q_1 Q_5}$). However, it also has several advantages compared to
higher-dimensional examples, most notably the fact that when the background has purely Neveu-Schwarz (NS-NS)
charges the string worldsheet theory is under very good control, either in the Ramond-Neveu-Schwarz (RNS)
formalism [3, 4, 5, 6, 7, 8, 9, 10] (for $Q_5 > 1$) or in the hybrid formalism [11, 12, 13, 14].

### [sec-intro-p2] paragraph

Many features of this theory, such as its moduli space [15], chiral ring [16, 17], protected [18, 19, 20, 21,
22, 23, 24] and unprotected [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] correlators, and its perturbative
string spectrum [37, 14] were studied and understood over the years. However, some of its features, in
particular features related to string perturbation theory, are more subtle. In this paper we review what is
known about this theory, highlighting three specific confusing issues and how they are resolved.

### [sec-intro-p3] paragraph

We begin in section 2 by reviewing this theory from various different points of view – the supergravity
approximation, the CFT, and the string worldsheet. In particular, we describe the parameter space of the
theory and the relations between theories with different (relatively prime) values of $Q_1$ and $Q_5$ (and the
same $N = Q_1 Q_5$).

### [sec-intro-p4] paragraph

In section 3 we review one of the strange features of this theory, the fact that perturbative string theory in
the background with only NS-NS fluxes on $AdS_3$ and on $S^3$ is not dual to a specific SCFT but rather to a
grand-canonical ensemble of SCFTs (with different values of $Q_1$). This fact was suspected based on the
worldsheet in the RNS formalism for $Q_5 > 1$ [7, 38]. For $Q_5=1$, where the theory is dual to a free
symmetric orbifold, the relation between string theory and the SCFT can be analyzed in great detail. We
describe (following [39, 40, 41]; see also [20, 29, 42]) how correlation functions of free symmetric orbifolds
${\rm Sym}_N({\cal M})$ have a $1/N$ expansion. However, this expansion does not map directly to a string
theory, while its grand-canonical version does, and we write in detail the relation between string theory and
CFT correlation functions. The main result is equation (3.12), which shows how appropriately defined grand-
canonical correlation functions exhibit an exact string genus expansion (generalizing the relation between the
partition functions, discussed in [43, 44, 45]). We comment on the generalization of this relation to $Q_5 >
1$.

### [sec-intro-p5] paragraph

In section 4 we discuss the fact that even though the $Q_5=1$ background (with vanishing Ramond-Ramond (R-R)
scalars) maps to a free orbifold theory for any value of its parameters, with the $1/N$ expansion of the
orbifold mapping to perturbative string theory in the NS-NS description of this background, there is a region
in parameter space where the NS-NS string becomes strongly coupled and an S-dual string seems to become weakly
coupled. We show that in this region of parameter space the $1/N$ expansion of the free orbifold breaks down,
and discuss the fact that even though naively the string coupling in the dual R-R description can become
arbitrarily weakly coupled, this description is never really weakly coupled (similar to the behavior of type
IIB string theory on $AdS_5\times S^5$ with a small integer flux $N$, which does not become weakly coupled
even when $g_s \to 0$).

### [sec-intro-p6] paragraph

Finally, in section 5, we describe a mysterious feature of the CFT, which is that it includes an extra ${\hat
T}^4$ factor, which is completely decoupled when the rest of the CFT is a free symmetric orbifold (for general
values of the parameters, this factor only couples to the rest of the SCFT through $J{\bar J}$ deformations).
Usually, string theory does not allow for decoupled sectors (since all states couple to gravity), but in this
case, the decoupled sector is a topological Chern-Simons theory on $AdS_3$, and we discuss to what extent and
how it couples to the rest of string theory for general values of the parameters.

### [sec-intro-p7] paragraph

Our analysis suggests various interesting future directions. When $N$ is not prime, the CFT has a singular
limit corresponding to every $N = Q_1 Q_5$ factorization with $Q_5 > 1$, in which its spectrum becomes
continuous (described by “long strings” on $AdS_3$ [46]). The CFT also has another singular limit where it is
described by the orbifold $(T^4)^N/S_N$ with a vanishing theta angle at the $\mathbb{Z}_2$ singularity, and it
would be nice to know if this limit has some controllable string theory description. Our results in section 5
suggest various properties of string theory on $AdS_3$ and its D-branes, and it would be nice to confirm these
properties directly. It would also be interesting to understand in more detail the precise grand-canonical
ensemble that is dual to string theory on the NS-NS background with $Q_5>1$.

### [sec-intro-p8] paragraph

The discussion of the free orbifold limit can be generalized to other purely NS-NS type IIB backgrounds with
$1$ unit of 3-form flux on an $S^3$, such as $AdS_3\times S^3\times K3$ or $AdS_3\times S^3\times S^3\times
S^1$ [47]. However, in those cases there is no direct relation to other values of the flux, so it is not clear
what can be said about them. It would be interesting to understand what can be said about other backgrounds,
like orbifolds of $AdS_3$ and/or $S^3$ [48, 49, 50, 51], type IIA string theory on $AdS_3\times S^3\times K3$
[52] and heterotic string theories (including non-supersymmetric ones [53, 54]) on $AdS_3$.

### [sec-intro-p9] paragraph

Last but not least, it would be nice if the detailed understanding of the duality between free orbifolds and
string theory could be generalized to the case of free gauge theories with continuous gauge groups.

## [sec-review] section: 2 A review of type II string theory on $AdS_3\times S^3\times T^4$ and its dual CFT
### [sec-review-p1] paragraph

One way to obtain type II string theory on $AdS_3\times S^3\times T^4$ is by considering the near-horizon
limit [1] of BPS strings preserving 2d ${\cal N}=(4,4)$ supersymmetry in type II string theory on $T^4$
(coming from fundamental strings, wrapped NS5-branes or 8 types of wrapped D-branes). The type IIA and type
IIB cases are related by T-duality so there is no need to discuss them separately, for convenience we will use
the type IIB language throughout this paper. Type II string theory on $T^4$ has an $SO(5,5,\mathbb{Z})$
U-duality group, under which the ten string charges transform as a vector. By a U-duality transformation one
can go to a frame where we have only D-string charge $Q_1$ and wrapped D5-brane charge $Q_5$, and we will
focus on this case in our discussion. By S-duality these configurations are identical to configurations
carrying $Q_1$ units of fundamental string charge and $Q_5$ units of wrapped NS5-brane charge. In this
section, we review what is known about these configurations from three different points of view –
supergravity, the string worldsheet, and the dual CFT. We will then review how U-duality relates different
$AdS_3$ backgrounds.

### [sec-sugra] section: 2.1 Supergravity solutions
#### [sec-sugra-p1] paragraph

The near-horizon limit of $Q_1$ D1-branes and $Q_5$ D5-branes wrapped on a $T^4$ is $AdS_3\times S^3\times
T^4$. String theory on $T^4$ has 25 massless scalar fields, including the metric and $B$-field on the $T^4$
(16 scalars), the dilaton (1 scalar), and 8 R-R scalars. When both $Q_1$ and $Q_5$ are non-zero (as we will
assume throughout this paper) 5 of these scalars (4 of the R-R scalars and the overall volume of the $T^4$)
are fixed in the near-horizon limit, while the other 20 scalars remain as moduli.

#### [sec-sugra-p2] paragraph

We will begin by focusing on the case where the R-R scalars vanish, while the string coupling takes some
arbitrary value $g_{10}$, and the torus has some fixed shape and $B$-field. In this case the near-horizon
limit is $AdS_3\times S^3\times T^4$, with R-R 3-form flux on $AdS_3$ and on $S^3$, where the radius $R$ of
$AdS_3$ and $S^3$ and the volume of $T^4$ are given by (up to numerical constants that will not be important
for our discussion) :

\[ \frac{R^2}{\alpha'} = g_{10} Q_5 = g_6 \sqrt{Q_1 Q_5}, \quad \frac{\text{vol}(T^4)}{\alpha'^2} = \frac{Q_1}{Q_5}, \quad 
        g^2_{10} = g_6^2 \frac{Q_1}{Q_5}. \]

(2.1)

Here we defined the six-dimensional string coupling $g_6$ in the standard way, and the expressions are derived
from the supergravity solution for these branes, so they are reliable when $R$ and $\text{vol}(T^4)$ are much
larger than the string scale. Naively, perturbative string theory in this R-R background is reliable when
$g_6, g_{10} \ll 1$, while supergravity is valid when $Q_1 \gg Q_5$, $g_{10} Q_5 \gg 1$. The 6- and 10-
dimensional Newton constants (in AdS units) in the background described above are

\[ \frac{G_N^{(6)}}{R^4} = \frac{1}{Q_1 Q_5}, \quad \frac{G_N^{(10)}}{R^8} = \frac{1}{g_6^2 Q_1 Q_5^3}. \]

(2.2)

#### [sec-sugra-p3] paragraph

Performing S-duality, we find a purely NS-NS background (that also arises as the near-horizon limit of $Q_1$
fundamental strings and $Q_5$ NS5-branes). In this background, there is NS-NS 3-form flux on $AdS_3$ and on
$S^3$ instead of R-R 3-form flux. While the ten-dimensional string coupling in this new frame,
$g_{10}'=1/g_{10}$, is still a free parameter, the six-dimensional string coupling is now fixed, while the
volume of the torus in string units in this frame is a free parameter which we will denote by $v_4$, related
to the R-R frame by $v_4 = g_6^{-2}$. The new background is given by

\[ \frac{R^2}{\alpha'} = Q_5, \quad \frac{\text{vol}(T^4)}{\alpha'^2} = v_4, \quad g_6'^2 = \frac{Q_5}{Q_1}, \quad g_{10}'^2 = v_4 \frac{Q_5}{Q_1}. \]

(2.3)

In this background all 16 scalars parameterizing the metric and $B$ field on the $T^4$ are massless moduli, as
well as 4 R-R scalars (which we are still setting to zero). Perturbative string theory is now valid whenever
$g_6', g_{10}' \ll 1$, while supergravity is valid for $Q_5, v_4 \gg 1$. The NS-NS description is invariant
under a T-duality transformation inverting the four cycles of the torus, so we can choose without loss of
generality $v_4 \ge 1$ (implying that for fixed $Q_1$, $Q_5$, the ten-dimensional string coupling cannot be
arbitrarily small). Newton’s constants remain the same, and in terms of $v_4$ they are given by (2.2)

\[ \frac{G_N^{(6)}}{R^4} = \frac{1}{Q_1 Q_5}, \quad \frac{G_N^{(10)}}{R^8} = \frac{v_4}{Q_1 Q_5^3}. \]

(2.4)

### [sec-dual_cft] section: 2.2 The dual conformal field theory
#### [sec-dual_cft-p1] paragraph

The general arguments of the AdS/CFT correspondence [1] imply that string theory on the $AdS_3$ background
discussed above should be dual to the 2d ${\cal N}=(4,4)$ superconformal field theory (SCFT) that arises at
low energies on a bound state of $Q_1$ D-strings and $Q_5$ D5-branes wrapped on $T^4$. In this section we will
discuss this theory when all the R-R scalars vanish. One way to describe this theory is as a sigma model on
the moduli space of $Q_1$ instantons of a $U(Q_5)$ theory on $T^4$ (T-duality implies that another way to
describe the same low-energy theory is as a sigma model on the moduli space of $Q_5$ instantons of a $U(Q_1)$
gauge theory on a dual $T^4$). The dimension of this moduli space is $4Q_1Q_5+4$, where the first factor comes
from the moduli space of $Q_1$ instantons of $SU(Q_5)$ on $T^4$, and the second factor from the Wilson lines
of the overall $U(1)$ in $U(Q_5)$ (which do not affect the $SU(Q_5)$ gauge fields, except through global
constraints). The corresponding conformal field theory thus has central charge $c=6 Q_1 Q_5 + 6$, consistent
at large $Q_1$, $Q_5$ with the central charge following from the supergravity background of the previous
section (2.2), (2.4). We will denote $N \equiv Q_1 Q_5$.

#### [sec-dual_cft-p2] paragraph

In general, this sigma model is a complicated SCFT, and no simple theory that flows to it at low energies is
known. In the limit that the volume of $T^4$ becomes infinite, it can be identified (for $Q_5 > 1$) as the
conformal field theory describing the Higgs branch of a $U(Q_1)$ ${\cal N}=(4,4)$ supersymmetric QCD theory
with one hypermultiplet in the adjoint representation and $Q_5$ hypermultiplets in the fundamental
representation (this theory decouples at low energies from the theory of the Coulomb branch [55, 56], which
corresponds to separating the D-strings from the D5-branes).

#### [sec-dual_cft-p3] paragraph

The sigma model on the instanton moduli space is singular for $Q_5 > 1$ when instantons go to zero size; for a
single $SU(2)$ instanton on $\mathbb{R}^4$ becoming small, this singularity is locally an
$\mathbb{R}^4/\mathbb{Z}_2$ singularity with a vanishing theta angle. At these singularities, the sigma model
develops semi-infinite throats (which before taking the low-energy limit connect the Higgs branch to the
Coulomb branch [57]), with a continuous spectrum of dimensions above a gap of order $Q_5$.

#### [sec-dual_cft-p4] paragraph

The moduli space simplifies significantly for $Q_5=1$; in this case all instantons are point-like, so the
moduli space of instantons becomes $(T^4)^{Q_1}/S_{Q_1}$. Including the Wilson lines, and noting that in this
case $N = Q_1$, the CFT is expected to be a sigma model on

\[ (T^4)^{N}/S_{N} \times \hat T^4 \]

(2.5)

(where the second $\hat T^4$, arising from the $U(1)$ Wilson lines, is inversely related to the first $T^4$).
This moduli space has orbifold singularities when instantons come together on the $T^4$ (these are not related
to the small-instanton singularities discussed above). A priori the value of the theta angle at these
singularities is not clear, but we will review below the arguments that it has the value $\theta=\pi$
corresponding to a free orbifold (rather than the value $\theta=0$ that appeared above).1

#### [sec-dual_cft-p5] paragraph

Returning to the case of general $Q_5$, as in any ${\cal N}=(4,4)$ SCFT, the super-Virasoro algebra contains
$SU(2)_L\times SU(2)_R$ affine Lie algebras of level $Q_1 Q_5 + 1$. In addition, the SCFT described above has
$8$ left-moving and $8$ right-moving $U(1)$ affine Lie algebras. $4+4$ of these symmetries have level $Q_1$,
and are related to the compact scalars describing the center of mass position of the $Q_1$ instantons (which
lives on $T^4$). The other $4+4$ affine Lie algebras have level $Q_5$, and are related to the $U(1) \subset
U(Q_5)$ Wilson lines (which live on the dual $\hat T^4$). These symmetries are manifest in the $Q_5=1$ case
(2.5). In the dual supergravity description of the previous subsection, if we consider the NS-NS background,
the first $8$ $U(1)$’s arise from the NS-NS sector (as the $g_{\mu i}$ and $B_{\mu i}$ components of the
metric and $B$ field, where $i$ labels the four coordinates of $T^4$), and the other $8$ $U(1)$’s arise from
the R-R sector (by taking suitable components of the R-R 2-form and 4-form potentials). The level of the
affine Lie algebras in the CFT is related to the Chern-Simons level of the corresponding $U(1)$ gauge fields
on $AdS_3$, and the levels mentioned above agree with type II supergravity on $AdS_3\times S^3\times T^4$.

### [sec-string_ws] section: 2.3 The string worldsheet
#### [sec-string_ws-p1] paragraph

There are various methods for studying string theory in the R-R $AdS_3\times S^3\times T^4$ background – the
Green-Schwarz string, the pure spinor string and a hybrid formalism. However, as in other R-R backgrounds,
quantization of the string is not yet well-understood in any of these approaches.

#### [sec-string_ws-p2] paragraph

The situation is much better in the NS-NS background. This background can be described in the standard RNS
formalism (with ${\cal N}=(1,1)$ supergravity on the worldsheet), in which the worldsheet action is a sum of
supersymmetric WZW models of $SL(2)$ (describing $AdS_3$ with NS-NS flux) and $SU(2)$ (describing $S^3$ with
NS-NS flux), both at level $Q_5$, and a supersymmetric sigma model on $T^4$ (together these give a critical
type II superstring). The supersymmetric $SU(2)$ WZW model can be written as a direct sum of a bosonic $SU(2)$
model at level $(Q_5-2)$ and three free fermions, so this description makes sense for $Q_5 \geq 2$, and it was
investigated in detail in [5, 7].

#### [sec-string_ws-p3] paragraph

One unusual property of string theory in these backgrounds is that it has a continuous spectrum. From the
point of view of the worldsheet this arises because $SL(2)$ has representations with continuous ‘spins’, while
in space-time it is related to “long strings” [46] winding around the angular direction of $AdS_3$, that can
go all the way to the boundary at a finite cost in energy (so their radial momentum is a continuous
parameter). This continuous spectrum can be related to the continuous spectrum arising at small instanton
singularities in the SCFT, discussed in the previous subsection.

#### [sec-string_ws-p4] paragraph

The NS-NS background may also be described in the hybrid formalism for the worldsheet, where the $AdS_3\times
S^3$ part corresponds [11] to a super-WZW model on the supergroup $PSU(1,1|2)$ at level $Q_5$ (for a recent
review see [59]). This description makes sense for any integer value of $Q_5$. For $Q_5>1$ it agrees with the
RNS formalism discussed above, while for $Q_5=1$ it behaves very differently and, in particular, it does not
have a continuous spectrum. It was shown in [60] that the spectrum [13, 14] and correlation functions [42, 61,
62, 63] of string theory in this background with $Q_5=1$ precisely reproduce those of the symmetric orbifold
$(T^4)^{Q_1}/S_{Q_1}$, and we will discuss the precise form of this matching (and its consistency with our
discussion in the previous subsection) in more detail below. Together with the discussion of the previous
subsection, and with the fact that this background (like the free orbifold) maps to itself under T-duality,
this strongly suggests that string theory on the $(N,1)$ NS-NS $AdS_3$ background with vanishing R-R scalars
is dual to the CFT (2.5) with $\theta=\pi$, the free orbifold value.

### [sec-diffrent_back] section: 2.4 Relations between different backgrounds
#### [sec-diffrent_back-p1] paragraph

Naively, the backgrounds with different values of $(Q_1,Q_5)$ are distinct, and each of them corresponds to a
different SCFT. But in fact, as discussed in detail in [15]2, all the backgrounds with the same $N \equiv Q_1
Q_5$ and with mutually prime $(Q_1, Q_5)$ are related by $SO(5,5,\mathbb{Z})$ U-duality transformations of
type II string theory on $T^4$. Those $SO(5,5,\mathbb{Z})$ transformations that preserve $(Q_1, Q_5)$ remain
as duality symmetries of string theory on $AdS_3\times S^3\times T^4$, and form a subgroup of
$SO(4,5,\mathbb{Z})$ (among these, we already mentioned the $SO(4,4,\mathbb{Z})$ T-duality in the NS-NS
description). On the other hand, the remaining transformations relate the theories with different values of
$(Q_1, Q_5)$; we already described the S-duality transformation that maps NS-NS charges to R-R charges, and in
this subsection we focus on transformations between backgrounds with purely NS-NS charges (a more general
discussion of these dualities will be given in section 5). In our descriptions in the previous subsections,
the theories with different $Q_1$ and $Q_5$ looked very different, because we focused on the co-dimension 4
subspace of their moduli space where the R-R scalars vanish. However, the duality transformations do not leave
this subspace invariant, but rather they relate configurations with vanishing R-R scalars for one value of
$(Q_1,Q_5)$ to configurations with non-zero R-R scalars for other values. When the string coupling in one
description is small, it is large in all other descriptions, so there is no direct relation between the
perturbative string expansions for different values of $(Q_1,Q_5)$.

#### [sec-diffrent_back-p2] paragraph

Turning on the R-R scalars corresponds to an exactly marginal deformation of the CFT, so this implies that all
the theories with different mutually prime $(Q_1,Q_5)$ but the same $N=Q_1 Q_5$ sit on the same moduli space
of exactly marginal deformations. In particular, they can all be described as exactly marginal deformations of
the free sigma model on (2.5). This sigma model actually has an 84-dimensional space of exactly marginal
deformations. 16 of these are the metric and $B$-field on the $T^4$ in $(T^4)^N/S_N$ (which map to the metric
and $B$-field of the $T^4$ in the NS-NS description). 4 additional ones are blow-up modes of the
$\mathbb{Z}_2$ singularity of this orbifold. The other 64 exactly marginal deformations take the form $J_i
{\bar J}_j$, where $i$ ($j$) go over the 8 left-moving (right-moving) $U(1)$ currents of the SCFT. 16 of these
deformations are the metric and $B$ field on the $\hat T^4$ in (2.5), 16 of them can be thought of as changing
the metric and $B$ field on the “center of mass” $T^4$ in the orbifold, and the remaining 32 mix the $U(1)$
symmetries of the orbifold and those of $\hat T^4$. As discussed in [15], turning on the 4 R-R scalars on
$AdS_3$ corresponds in the CFT to a linear combination of turning on the blow-up modes of the orbifold, and
specific $J{\bar J}$ deformations mixing the $T^4$ and $\hat T^4$ symmetries. For every mutually prime pair
$(Q_1, Q_5)$ there is a co-dimension 4 subspace of the 20-dimensional space of non-$J{\bar J}$ deformations
that maps to the $(Q_1,Q_5)$ background with vanishing R-R scalars, and on that subspace the specific $J{\bar
J}$ deformations that are related to string theory on $AdS_3$ deform the currents such that there are $4+4$
$U(1)$ currents of level $Q_1$, and $4+4$ additional currents (orthogonal to them) of level $Q_5$. In figure 1
we show a slice of these subspaces for $N=30$, where we turn on only the string coupling and the 10d R-R
scalar field $\chi$ (this determines also the value of the R-R 4-form on the $T^4$); we draw this slice in the
language of the R-R background with $Q_1=30$ and $Q_5=1$ (with a fixed $T^4$ shape), and describe the
positions of the subspaces mentioned above in this parameterization (a similar figure for $Q_1=6$ appears in
[15]). This background is mapped to itself under a $\Gamma_0(N)$ subgroup of an $SL(2,\mathbb{Z})\times
SL(2,\mathbb{Z})$ subgroup of the U-duality group, which acts on $\tau=\chi+\frac{i}{g_{10}}$ in the same way
as the $\Gamma_0(N)$ subgroup of $SL(2,\mathbb{Z})$, and we draw a fundamental domain containing all
inequivalent theories (in this slice).3 In section 5 we will describe in detail where all the subspaces
mentioned above (of $(Q_1,Q_5)$ charges with vanishing R-R fields) sit inside this slice; they are denoted by
thick black lines in the figure. Note that the subspaces corresponding to charges $(Q_1,Q_5)$ and $(Q_5,Q_1)$
are identical, since the two descriptions are related (for fixed $T^4$ shape) by a combination of S-duality,
T-duality on all $4$ cycles, S-duality and another T-duality on all $4$ cycles.

#### [sec-diffrent_back-p3] paragraph

The other 64 exactly marginal deformations, that are not related to scalar fields in $AdS_3$, are all related
to changes in the boundary conditions for the $U(1)^{8}\times U(1)^8$ CS gauge fields on $AdS_3$ (these can be
written as 8 copies of a $\frac{k}{4\pi} \int A \wedge dB$ theory, where $k$ is equal to either $Q_5$ or
$Q_1$, depending on the gauge field). For a given choice of complex coordinates in the CFT, they can be
thought of as choosing which $8$ bulk gauge fields have a boundary condition in which their $z$-component is
fixed at the boundary (so that they correspond to anti-holomorphic currents), while the other $8$ gauge fields
have their ${\bar z}$ component fixed at the boundary.

#### [fig-N30_moduli] figure: Figure 1

Figure 1. The subspace of the moduli space parameterized by $\tau_\text{RR}=(\chi + i/g_{10})$ in the R-R
description of the $Q_1=30$, $Q_5=1$ background, for fixed $T^4$ moduli. A fundamental domain under the
U-duality subgroup $\Gamma_0(N)$ (that keeps both the charges $(Q_1,Q_5)=(N,1)$ and the $T^4$ normalized
metric fixed) is bounded by the grey lines, and divided into different $SL(2,\mathbb{Z})$ fundamental domains.
 The $(Q_1,Q_5)=(N,1)$ NS-NS background with vanishing R-R scalars sits on the imaginary axis at $\chi=0$, and
is weakly coupled close to $\tau= 0$. Its S-dual, the $(N,1)$ R-R background, is weakly-coupled close to
$\tau= i \infty$. The two limits are continuously connected to each other as a function of $g_{10}$, drawn in
a vertical thick black line, and this line maps to the free orbifold (2.5).
 For every other $(Q_1,Q_5)$ background with $Q_1 Q_5 = N$, there is a line describing its singular
($\chi'=0$) locus, connecting the weakly coupled $(Q_1,Q_5)$ NS-NS and R-R backgrounds. These are the rest of
the thick black lines in the figure. Up to the sign of $\chi$, the $(15,2)$ line connects the NS-NS theory at
$\tau= 1/2$ to the R-R theory at $\tau=7/15$, the $(10,3)$ line connects the NS-NS theory at $\tau= 1/3$ to
the R-R theory at $\tau=3/10$, and the $(6,5)$ line connects the NS-NS theory at $\tau= 1/5$ to the R-R theory
at $\tau=1/6$.

#### [sec-diffrent_back-p4] paragraph

Note that for $Q_5>1$ with vanishing R-R scalars the CFT contains a long-string sector with a continuous
spectrum, which is far from evident in our description of the CFT as a deformation of the symmetric orbifold.
The subsector of the CFT describing the long strings is believed to itself be described as an $S_{Q_1}$
symmetric orbifold [46, 65, 66, 67], and it would be nice to understand how this is related to the picture
described above.4

#### [sec-diffrent_back-p5] paragraph

There is another subspace of the moduli space of the deformed free orbifold which is singular, which is the
subspace where the metric is given by (2.5) but the theta angle on the vanishing 2-cycle at the $\mathbb{Z}_2$
orbifold singularity of (2.5) is taken to $\theta=0$ (instead of its value $\theta=\pi$ at the free orbifold
point [69]). This subspace is not the same as the singular subspaces that are weakly coupled NS-NS-background
strings; we believe that in the R-R background of figure 1 it sits at $\chi = \pm 1/2$, on the boundary of the
fundamental domain.

### [section-2.5] section: 2.5 Questions
#### [section-2.5-p1] paragraph

The picture described in this section raises 3 questions:

String theory in NS-NS $AdS_3$ backgrounds is believed [7, 8, 38, 70, 45] to describe not a background with
fixed $Q_1$, but rather a grand-canonical ensemble of theories with different $Q_1$ (and the same $Q_5$). How
is this consistent with the picture described above, and how is it consistent with the detailed matching of
the correlation functions of the $Q_5=1$ string to the free orbifold (2.5)?

For $Q_5=1$ we mentioned that the NS-NS perturbative expansion matches the $1/N$ expansion of the free
orbifold (2.5). However, the orbifold is free for any value of the moduli of the torus, while (2.3) implies
that the $(N,1)$ NS-NS string theory becomes strongly coupled once $v_4 > N$. Moreover, for $v_4 \gg N$ it
seems that the same theory should have a different weakly coupled description, as string theory on the R-R
background. How is this consistent?

The SCFT (2.5) (dual to string theory with $Q_5=1$) has a decoupled $\hat T^4$ sector, which did not show up
in the mapping of this string theory to the free orbifold. Moreover, this sector is still essentially
decoupled from the rest of the SCFT even after we deform it by $J{\bar J}$ deformations to go to other values
of $(Q_1, Q_5)$ (one can think of these deformations as just modifying the energies of states with given
charges). How is this decoupled sector realized in string theory?

#### [section-2.5-p2] paragraph

The answers to these questions will be discussed in the next three sections of the paper, respectively. The
three sections are almost completely independent of each other, so readers who are just interested in one
question can jump directly to the relevant section.

## [sec-st_grand_can] section: 3 String theory and the grand-canonical ensemble
### [sec-st_grand_can-p1] paragraph

The near-horizon limit suggests that (the non-perturbative completion of) string theory on $AdS_3\times
S^3\times T^4$ with fixed fluxes $Q_1$ and $Q_5$ should be equivalent to the conformal field theories
discussed above, at any point in their moduli space. In principle, one can consider instead of the quantum
gravity theory (and its dual CFT) with some fixed flux $Q$, the grand-canonical ensemble defined as the sum
over the theories with flux $Q$, weighted by $e^{-\mu Q}$. In the bulk this can be thought of as choosing a
different boundary condition for the 2-form field potential on $AdS_3$, for which the integral over $AdS_3$ of
its field strength is equal to $Q$.

### [sec-st_grand_can-p2] paragraph

Somewhat surprisingly, it turns out that perturbative string theory on the NS-NS background with NS5-brane
flux $Q_5$ computes such a grand-canonical ensemble with respect to $Q_1$, rather than being dual to a
specific conformal field theory.5 This was first understood in the RNS formalism for $Q_5 \geq 2$ [7, 8, 38],
and it was then claimed to be the case also in the hybrid formalism for $Q_5=1$ [70, 45]. In this section, we
explain in detail how the grand-canonical ensemble for $Q_5=1$ is consistent with the relation between free
orbifold correlation functions and perturbative string theory.

### [section-3.1] section: 3.1 A brief review of string theory in the NS-NS background
#### [section-3.1-p1] paragraph

In this subsection we review the relevant information about string theory on $AdS_3\times S^3\times T^4$ with
a purely NS-NS background.

#### [section-3.1-p2] paragraph

As reviewed in section 2.1, when we take the near-horizon limit of $Q_1$ fundamental strings and $Q_5$
NS5-branes wrapped on $T^4$, we obtain this $AdS_3$ background, with a fixed value for the six-dimensional
string coupling (related to the vacuum expectation value of the dilaton field) given by $g_6'^2 = Q_5 / Q_1$.
So from this point of view, we would expect string theory on the NS-NS background to have a fixed value of
$Q_1$ and not to have any continuous NS-NS parameters beyond the moduli of the $T^4$.

#### [section-3.1-p3] paragraph

However, if we directly study string theory on the NS-NS $AdS_3$ background, either in the RNS formalism (for
$Q_5 \geq 2$) [5, 7, 8, 38] or in the hybrid formalism [70, 45], we find a rather different picture. The
worldsheet action depends explicitly on $Q_5$, but the parameter $Q_1$ does not appear in it. On the
worldsheet one can have as usual a continuous parameter $g_s$ related to the coefficient of $\int d^2\sigma
\sqrt{{\rm det}(h)} R[h]$ where $h$ is the worldsheet metric, which weighs connected string diagrams arising
from genus $g$ surfaces by $g_s^{2g-2}$. Unlike in most other string theories, here this parameter is not
related to the expectation value of any field in space-time, but it is still present on the worldsheet.

#### [section-3.1-p4] paragraph

In addition, when computing from the worldsheet the central charge appearing in the space-time operator
product expansion (OPE) of two CFT energy-momentum tensors or NS-NS $U(1)$ currents, one finds that it is
given by $c = 6 Q_5 I$ and by $k = I$, respectively, where $I$ is a specific operator on the worldsheet
(naively it depends on a position on the boundary of $AdS$ space, but in fact this dependence is trivial) [5].
If the string theory corresponded to the CFT suggested by the near-horizon limit, we would expect to have
$Q_1$ appearing in these equations instead of $I$, but instead the operator $I$ appears, whose correlation
functions are not equivalent to replacing it by a constant. The correlation functions of this operator are not
arbitrary, but are fixed by the worldsheet theory. The fact that $I$ is not a constant prevents the
interpretation of string theory as dual to a specific CFT with a given central charge, and from having the
expected space-time factorization properties.

#### [section-3.1-p5] paragraph

The interpretation of this property was suggested in [38, 70, 45]. Since $I$ is a vertex operator on the
worldsheet, it is natural to turn on a coupling $\mu$ for it, like for any other vertex operator. Then,
naively one obtains a string theory labelled by two continuous parameters, $g_s$ and $\mu$. However, the
properties of correlation functions of $I$ imply a specific dependence of correlation functions on $\mu$ [8,
38], and this dependence is such that its effect can be swallowed into a rescaling of the string coupling
$g_s$ and a $\mu$-dependent normalization of the worldsheet vertex operators. So, in this normalization of the
vertex operators, string theory on $AdS_3$ depends just on a single continuous parameter $g_s$. It was then
suggested that this string theory should be identified with a grand canonical ensemble of the $(Q_1,Q_5)$ CFTs
reviewed in section 2, with the same $Q_5$ but with different values of $Q_1$, weighted by $p^{Q_1}$, with
some specific relation between the continuous parameters $p$ and $g_s$. It was argued in [38] that one can
obtain the CFT with fixed $Q_1$ by a Legendre transform of the string theory. In this section, following the
analysis of $Q_5=1$ partition functions in [45], we describe the precise relation between the grand canonical
ensemble of CFTs and the dual string theory. For $Q_5=1$ we argue that the precise way to obtain fixed-$Q_1$
CFT correlation functions from string theory is more complicated than a Legendre transform (though it agrees
with it at leading order), and we conjecture that this should be true also for $Q_5>1$.

### [sec-genus_exp] section: 3.2 The genus expansion for symmetric orbifolds
#### [sec-genus_exp-p1] paragraph

Before introducing the grand-canonical ensemble, it is illuminating to understand why the fixed $N$ orbifold
theory (2.5) does not behave as a string theory. Specifically, it does not have a proper genus expansion. Even
though we focus on the $(T^4)^N/S_N$ orbifold in this paper, our analysis of the free orbifold in this section
is relevant for any symmetric orbifold.

#### [sec-genus_exp-p2] paragraph

We begin by briefly reviewing the construction of the genus expansion for the (fixed $N$) $(T^4)^N/S_N$
symmetric orbifold, following [39, 40] (see also [18, 20, 29, 42]). The Hilbert space of the symmetric
orbifold at low energies and large $N$ can be understood as a Fock space of single-cycle-twist operators,
divided into different $w$-sectors. The basic operator for a given such sector $1 < w \leq N$ is the $w$-cycle
twist operator, defined as

\[ \sigma_w(z) = \frac{1}{w (N-w)!} \sum_{h\in S_N} \sigma_{h^{-1} (1,...,w) h}(z), \]

(3.1)

where $(1,...,w)$ is the cyclic permutation of the first $w$ elements, and $\sigma_g(z)$ is the twist operator
with holonomy $g\in S_N$ permuting the $N$ copies as one goes around it. The sum over $S_N$ ensures the gauge
invariance of the operator. Our choice of normalization may appear non-standard, but as we will see below,
this is the correct normalization for comparison with string theory vertex-operators. It is mathematically
natural, as the denominator is the stabilizer size of $(1,...,w)$ in $S_N$ (by $S_N$ conjugations), so that
each different permutation is counted in (3.1) with weight $1$. In this section we will consider only
correlation functions of $\sigma_w$’s, but the extension to more general single-cycle operators (with
additional CFT excitations in addition to the twist operator) and to untwisted-sector operators (which have
$w=1$) is straightforward.

#### [sec-genus_exp-p3] paragraph

The insertion of $\sigma_w(0)$ can be understood as cutting a hole around $z=0$, with a cyclic gluing of $w$
copies of $T^4$ around the boundary circle (different ones for each term in (3.1)), and a trivial gluing for
the rest of the $(N-w)$ copies. A correlation function of $\sigma_w(z)$’s will get contributions from
consistent gluings between the insertions. Each such consistent gluing between the $N$ copies gives a non-
trivial covering of the original CFT manifold. The contribution of each gluing to the correlation function is
proportional to the partition function of the $T^4$ CFT on the covering space. For this reason, the covering
space is believed [40] (and later also shown [42, 61, 62, 63, 71]) to be identified with the string
worldsheet.

#### [sec-genus_exp-p4] paragraph

We begin with the two-point function of two $\sigma_w$’s on the plane (which can be conformally mapped to the
sphere), given by [40]

\[ \langle \sigma_{w}(z) \sigma_{w'}(0)\rangle = \frac{N!}{w (N-w)!} \frac{\delta_{w,w'}}{|z|^{2\Delta_{w}}}, \]

(3.2)

with $\Delta_{w}=\frac{c}{24}(w-1/w)$ (where in our case $c=6$ is the central charge of the $T^4$ SCFT). In
this case all consistent gluings are related by a gauge transformation, and the topology of the gluing is of a
sphere with two insertions of degree-$w$ branch points (more precisely, this is the topology of the non-
trivial part of the correlation function which involves $w$ copies of the $T^4$, ignoring all other copies).
We thus understand (3.2) as a single worldsheet diagram contribution with genus zero. The combinatorial factor
of the diagram can be understood as follows. In the normalization we choose, each gluing is summed over once,
and we only need to count how many different permutations are gauge-equivalent to $(1,...,w)$. This is given
by $N!$ divided by the size of the stabilizer of $(1,...,w)$, which is $w (N-w)!$.

#### [sec-genus_exp-p5] paragraph

In a general diagram contributing to a correlation function on the plane, there will be $N_c$ copies of $T^4$
which are involved in non-trivial permutations, while the other $(N-N_c)$ copies may be viewed as “vacuum
diagrams”. We will call a diagram “connected” if all the $N_c$ copies are permuted non-trivially (rather than
having some of them only permuted among themselves). By the Riemann–Hurwitz formula, in connected diagrams
$N_c$ is related to the genus $g$ of the covering space by

\[ N_c = 1-g + \frac{1}{2}\sum_{j=1}^n (w_j -1). \]

(3.3)

The contribution from such connected diagrams goes as

\[ \langle \sigma_{w_1}(z_1) ... \sigma_{w_s}(z_s)\rangle_\text{conn} = 
    \sum_{g=0}^{g_\text{max}} \frac{N!}{N_c (N-N_c)!} \cdot (...), \]

(3.4)

where $(...)$ stands for the contribution of diagrams with the appropriate value of $N_c$, given in terms of
the path-integral over the appropriate branched covering, divided by the appropriate vacuum path-integral
[39]. For a given $N_c$, the combinatorial factor in (3.4) is simply the orbit size of the cyclic permutation
$(1,...,N_c)$ in $S_N$; in a specific diagram, after choosing the $N_c$ participating sheets and their cyclic
ordering, there is just one permutation from (3.1) which contributes for each operator. Here we are interested
in the large $N$ limit in which the $w_i$ are kept fixed; for finite values of $N$ there is an extra
restriction that $N_c \leq N$.

#### [sec-genus_exp-p6] paragraph

In the literature [39, 40] one usually defines a normalized version $\tilde \sigma_w$ of the twisted operators
(3.1), in which their two-point function (3.2) is normalized to one. Then one can ask about the leading large
$N$ behavior of a given connected diagram to (3.4). The result from genus $g$ diagrams is

\[ \langle \tilde \sigma_{w_1}\cdots \tilde \sigma_{w_n}\rangle_{\text{conn},g} \propto \frac{N!}{N_c (N-N_c)!}\prod_{j=1}^n \sqrt{\frac{w_j (N-w_j)!}{N!}} \sim N^{N_c - \frac{1}{2}\sum_{j=1}^n w_j} = N^{1-g-n/2}. \]

(3.5)

This result looks very appealing, after comparing it to the general structure expected in string theory,

\[ \langle O_1 \cdots O_n \rangle_\text{conn} = \sum_{g=0}^{\infty} g_s^{2g-2+n}\cdot \sum_{\text{Diagrams with genus } g} (....). \]

(3.6)

A naive comparison gives $g_s^2 = 1/N$, with an identification between string theory diagrams and the
symmetric orbifold’s sum over branched coverings.

#### [sec-genus_exp-p7] paragraph

However, this identification actually works only at leading order in $1/N$. We will give two different reasons
to suspect the identification. The first reason, which was noticed already in [20], is that the right-hand
side of (3.5) describes only the leading $1/N$ behavior from a given genus, and receives $1/N$ corrections
from expanding the product in the middle. Thus, at subleading order in $1/N$, a given correlator will receive
contributions from higher genus diagrams, but also from the subleading corrections to the planar diagrams, and
we find

\[ \langle O_1 \cdots O_n \rangle_\text{conn} = g_s^{n-2}\cdot (\text{genus 0}) +  g_s^{n}\cdot (\text{genus 1}+\# \cdot \text{genus 0}) + \cdots \ . \]

(3.7)

This is not what we expect in (3.6). Note that because of the structure of (3.5), it is not possible to fix
this by redefining $g_s$ and/or the operator normalizations at higher orders in $1/N$.

#### [sec-genus_exp-p8] paragraph

The second problem with identifying $g_s^2=1/N$ arises for disconnected diagrams. For simplicity, consider the
four-point function of two $w_1$ and two $w_2$ twist operators. Diagrammatically the four-point function has a
leading disconnected piece, with $w_1$ sheets permuted among themselves and $w_2$ other sheets permuted among
themselves. Following the string theory picture, one would expect this contribution to be equal to the product
of the two two-point functions. However, for a given $N$, the combinatorial factor associated with this
disconnected piece also accounts for the fact that the $w_1$ and $w_2$ cycles should not overlap. The exact
ratio between the disconnected piece and the product of the connected diagrams is thus

\[ \frac{\langle \sigma_{w_1}(z_1)\sigma_{w_1}(z_2)\sigma_{w_2}(z_3)\sigma_{w_2}(z_4)\rangle_\text{disc}}{\langle \sigma_{w_1}(z_1)\sigma_{w_1}(z_2)\rangle \langle \sigma_{w_2}(z_3)\sigma_{w_2}(z_4)\rangle} = \frac{(N-w_1)!(N-w_2)!}{N! (N-w_1-w_2)!} = 1 +O(1/N), \]

(3.8)

and is not exactly equal to $1$. As a result, at fixed $N$, correlation functions do not obey the expected
“cluster decomposition" of string theory beyond the leading order in $1/N$.6

### [sec-grand] section: 3.3 The grand canonical ensemble
#### [sec-grand-p1] paragraph

To solve this issue we would like to work not with fixed $N$ but rather in the grand canonical ensemble with a
chemical potential for $N$. As we reviewed at the beginning of this section, this is generally expected for
string theory on $AdS_3$ with NS-NS backgrounds. It was suggested in [38] that the string theory at $Q_5>1$ is
related to a fixed CFT by taking a Legendre transform with respect to the coefficient of the operator $I$. A
slightly different suggestion was made in [45] for $Q_5=1$, that string theory and the dual CFT are related by
a Laplace transform, so that the string theory corresponds to a grand canonical ensemble of the $(Q_1,Q_5)$
theories with the same NS-NS moduli, with a chemical potential for $Q_1$. In this subsection we analyze this
suggestion in detail for $Q_5=1$, generalizing the analysis of the partition function in [45] to general
correlation functions. In this case we just have a grand canonical ensemble of (2.5) with respect to $N$;
since this does not affect the ${\hat T}^4$ factor, we will ignore it here and return to it in section 5.

#### [sec-grand-p2] paragraph

Denoting by $Z_N[J]$ the partition function of the $\text{Sym}_N(T^4)$ CFT on some manifold with sources $J$
for various operators, the grand canonical partition function is defined as7

\[ Z_p[J] = \sum_{N=0}^\infty p^N Z_N[J], \]

(3.9)

with $Z_0[J]=1$. Sources for untwisted sector operators exist for any $N$, while sources for twisted operators
start appearing at some $N_{min}$ that depends on the twisted sector. Note that we are summing here $Z_N[J]$
rather than $Z_N[J]/Z_N[0]$ (which would be the generating function for correlation functions in the
$\text{Sym}_N(T^4)$ CFT), since already the vacuum partition function (discussed in [45]) is non-trivial when
the CFT lives on higher-genus manifolds.

#### [sec-grand-p3] paragraph

Simplifying to the case where we turn on sources just for the leading twist operators in each twisted sector
of the orbifold, the $\text{Sym}_N(T^4)$ generating function is given schematically by8

\[ Z_N[J] = \frac{1}{N!} \int D^N X e^{-S[X]} \exp\left(\sum_{w=1}^\infty \int d^2 z J_w(z) \sigma_w(z)\right). \]

(3.10)

The expansion of $Z_N[J]$ generally includes disconnected coverings. Some of the connected components include
operator insertions and others, the vacuum diagrams, do not. The normalization (3.1) exactly allows us to
compute the combinatorial factor from each component on equal footing. Let us denote by $N_1,...,N_k$ and
$n_1,...,n_k$ the number of copies of $T^4$ of the different connected components (which can differ in the
number of copies and/or in the operator insertions) and their multiplicity, respectively, so that
$\sum_{i=1}^k N_i n_i = N$. The generalization of (3.4) is given by

\[ Z_N[J] = \sum_{n=0}^\infty \frac{(\sum_{w=1}^\infty \int d^2 z J_{w}(z))^n}{n!}
    \sum_{\substack{\text{Disconnected} \\ \text{diagrams}\\ \sum_{i=1}^k n_i N_i = N}}
    \prod_{i=1}^k \frac{1}{n_i ! N_i^{n_i}} (Z_\text{covering}^{(i)})^{n_i}, \]

(3.11)

with $Z_\text{covering}^{(i)}$ the partition function coming from the $i$-th connected component (such that
the product of the partition functions contains also insertions of $n$ $\sigma_{w_j}(z_j)$ operators)9. We
stress again that some of these components include no operator insertions and correspond to vacuum diagrams.
For example, in (3.4) there’s a single $n_1=1, N_1=N_c$ connected diagram with all the insertions, and
$n_2=N-N_c$ vacuum diagrams with $N_2=1$ each. For given operator insertions, not all the possible $N_i$’s and
$n_i$’s are included in the sum, as only some will correspond to a possible diagram. For example, only $N_i=1$
diagrams are possible when all $w_j=1$. Of course, for some values of $\{w_j\}$ there are no covering spaces
at all if the corresponding permutations cannot be multiplied to give the identity permutation (and in
particular there are no diagrams if any $w_j > N$).

#### [sec-grand-p4] paragraph

Importantly, the only dependence on $N$ in (3.11) is in the definition of the sum over $N_i, n_i$. Considering
now the grand-canonical ensemble (3.9), the sum over the diagrams is no longer constrained by $N$. Notice that
as (3.1) are cyclic, each insertion will appear in a single connected component.10 As a result, the now
unconstrained sums over $n$ and $n_i$ nicely exponentiate into connected components

\[ Z_p[J] = \exp\left\{
    \sum_{n=0}^\infty \frac{(\sum_{w=1}^\infty \int d^2 z J_{w}(z))^n}{n!}
    \sum_{\substack{\text{Connected} \\ \text{diagrams}}} \frac{p^{N_c}}{N_c} {Z}_\text{covering}^{\{w_j\}}
\right\}, \]

(3.12)

with $N_c$ the number of $T^4$’s in the connected covering, and $Z_\text{covering}^{\{w_j\}}$ the
corresponding partition function in the presence of the $n$ $\sigma_{w_j}(z_j)$ operators. In this expression,
the vacuum diagrams appear in the $n=0$ term in the exponent. The vacuum partition function is known to
exponentiate nicely in the grand-canonical ensemble [43, 44]. Using the normalization (3.1), (3.12) is a
generalization of that statement which incorporates operator insertions.11

#### [sec-grand-p5] paragraph

Up to now our discussion was valid for the CFT on any manifold, but let us now consider the case of the CFT on
the sphere (higher genus surfaces will be discussed in the next subsection). In this case there is a single
vacuum diagram in $Z_N$, which gives $Z_N[0] = Z_1[0]^N / N!$. Thus, the grand-canonical partition function
for the sphere can also be written as

\[ Z_p^\text{sphere}[J] = \exp\left\{
    \sum_{n=1}^\infty \frac{(\sum_{w_n=1}^\infty \int d^2 z J_{w}(z))^n}{n!}
    \sum_{\substack{\text{Connected} \\ \text{non-vacuum}}} \frac{p^{N_c}}{N_c} {Z}_\text{covering}^{\{w_j\}}
+ p \cdot Z_1[0]
    \right\}. \]

(3.13)

#### [sec-grand-p6] paragraph

Unlike the fixed $N$ ensemble discussed above, the exponential form of (3.12) has a nice interpretation as a
perturbative string theory. What is the corresponding string coupling? Redefining our operators by

\[ \sigma_w' = p^{-w/2} \sigma_w, \]

(3.14)

and using (3.3), the grand-canonical generating function for $\sigma_w'$ takes the form

\[ Z_p[J'] = \exp\left\{
    \sum_{n=0}^\infty \frac{(\sum_{w=1}^\infty \int d^2 z J_{w}'(z))^n}{n!}
    \sum_{\substack{\text{Connected} \\ \text{diagrams}}} \frac{p^{1-g-n/2}}{N_c}
{Z}_\text{covering}^{\{w_j\}} \right\}. \]

(3.15)

Comparing with (3.6) gives exactly the string theory genus expansion with

\[ g_s^{-2} \propto p. \]

(3.16)

The problems discussed in the previous subsection disappear when going to the grand-canonical ensemble.

#### [sec-grand-p7] paragraph

Note that a priori one may expect string theory to compute a grand-canonical generating function for the
correlation functions, where the coefficient of $p^N$ in the expansion of an $n$-point correlation function
would be the correlation function in the $N$’th CFT. Instead, we find that string theory computes correlation
functions that are derivatives of $Z_p[J]$ divided by $Z_p[0]$, and these are not directly related to
correlators for specific values of $N$ (which are derivatives of $Z_N[J]$ divided by $Z_N[0]$). To obtain
correlators with a specific $N$ one has to separately inverse-Laplace-transform the correlation functions and
the vacuum diagrams of the string theory. In particular, it seems that one should view the grand canonical
ensemble not as a sum over different independent theories, but more like summing over some extra ‘particle
number’ charge in a given theory, that is present also in the vacuum diagrams.12

#### [sec-grand-p8] paragraph

To make the matching to string theory more precise, we can define an operator “$I_\text{CFT}$” that would
couple to $\log(p)$, and that should be related to the operator $I$ discussed above on the worldsheet [5, 8,
45]. For the free orbifold ($Q_5=1$) this can be identified with “$N$" inside the sum over $N$ in (3.9). The
VEV of $I_\text{CFT}$ for the CFT on the sphere (from vacuum diagrams), related to string theory on Euclidean
$AdS_3$, is given by

\[ \langle I_\text{CFT} \rangle = \partial_{\log (p)}\log (Z_p[0]) = p Z_1[0]. \]

(3.17)

This agrees with the expectation that for large $p$ (corresponding to weak string coupling) the sum over $N$
should have a saddle point with $N \propto p$, with a smaller and smaller variation as $p$ increases. Note
that because of the conformal anomaly, $Z_1[0]$ depends on the radius of the sphere that the CFT lives on as
$Z_1[0] \propto R^2$. So the relation between $p$ and the typical value of $N$ depends on this radius (see the
related discussion in [75]). However, the relation between the string coupling and this typical value does not
depend on the radius. This can be seen by rewriting $p^{N_c} {Z}_\text{covering}^{\{w_j\}}$ in (3.13) as $(p
Z_1[0])^{N_c} ({Z}_\text{covering}^{\{w_j\}} / Z_1[0]^{N_c})$, where the factor in the second parenthesis is
independent of the radius, suggesting that a more precise version of (3.16) is $g_s^{-2} \propto p Z_1[0]$.

#### [sec-grand-p9] paragraph

To find the expectation value of $I_\text{CFT}$ for a given connected diagram, we can compute the derivative
of the generating function $\log (Z_p[J])$ by $\log (p)$. Directly from the form of $\log (Z_p[J])$ in (3.12)
we get

\[ \left\langle I_\text{CFT} \ \prod_{j=1}^n \sigma_w(z_j) \right\rangle_{\text{conn},g} = N_c \cdot \left\langle \prod_{j=1}^n \sigma_w(z_j) \right\rangle_{\text{conn},g}. \]

(3.18)

This agrees with the arguments of [45] for correlation functions of $I$ in the corresponding string theory.

#### [sec-grand-p10] paragraph

In [38] it was noted that the string theory disconnected 4-point function (for $Q_5 > 1$) does not satisfy the
naively expected field-theoretic cluster decomposition, due to the appearance of the central element $I$ in
the appropriate channel. Similarly, for $Q_5=1$ where we can compute the correlation functions from $Z_p$,
what would naively be identified as a connected correlation function in the dual CFT is given by

\[ \begin{split}
    \langle \sigma_{w_1}(z_1)\sigma_{w_1}&(z_2)\sigma_{w_2}(z_3)\sigma_{w_2}(z_4)\rangle_p
     - \left\langle \sigma_{w_1}(z_1)\sigma_{w_1}(z_2)\right\rangle_p
\left\langle\sigma_{w_2}(z_3)\sigma_{w_2}(z_4)\right\rangle_p\\
     & = \frac{\partial_{J_{w_1}}^2\partial_{J_{w_1}}^2 Z_p[0]}{Z_p[0]} - \frac{\partial_{J_{w_1}}^2
Z_p[0]}{Z_p[0]}\frac{\partial_{J_{w_1}}^2 Z_p[0]}{Z_p[0]}\\
     & = \left(1-\exp(-p \cdot Z_1[0])\right) \cdot \left\langle
\sigma_{w_1}(z_1)\sigma_{w_1}(z_2)\right\rangle \left\langle\sigma_{w_2}(z_3)\sigma_{w_2}(z_4)\right\rangle +
\left(\text{Connected}\right).
\end{split} \]

(3.19)

The first term on the right-hand side does not vanish when the distance between the pairs of operators becomes
large, as expected for a standard CFT. Expanding in orders of $p$, the sum can be interpreted as the OPE
contribution of $(I-\langle I \rangle)^k$ operators.

### [sec-higher_genus_CFT] section: 3.4 Higher genus partition functions
#### [sec-higher_genus_CFT-p1] paragraph

Equation (3.12) holds also for the CFT on higher genus Riemann surfaces (which is expected to be dual to
string theory on orbifolds of $AdS_3$). The main difference is that already without any operator insertions,
we now have a sum over holonomies in $S_N$ around the various cycles of the Riemann surface (subject to a
global consistency condition), and a similar sum over holonomies appears in the correlation functions of
vertex operators. So, in (3.12) the sum over coverings should also allow different $S_N$ holonomies (already
for the $n=0$ term). The definition of the $N_c$ ‘participating’ sheets now involves both the sheets that are
permuted by vertex operators, and the ones that are permuted by non-trivial holonomies (it is still the degree
of the covering). The splitting into ‘connected’ contributions (which are linked by some permutation, either
from a vertex operator or a holonomy) is the same. Because of the sum over the holonomies, there is no longer
a simple relation between $Z_N[0]$ and $Z_1[0]$.

#### [sec-higher_genus_CFT-p2] paragraph

Surprisingly, $Z_p$ has peculiar properties for higher genus. Let us denote the genus of the CFT manifold by
$G$, and assume $G>1$. To repeat the calculation of the string coupling, we can use the generalization of
(3.3) to general genus $G$

\[ (1-G) N_c = (1-g) + \frac{1}{2} \sum_{j=1}^n (w_j-1). \]

(3.20)

Unlike the $G=0$ case where we had contributions from $g=0,\cdots,g_{max}$, for $G>1$ the worldsheet genus $g$
can range from $g_{min} = G + \sum_j (w_j-1)/2$ to values of order $N$.

#### [sec-higher_genus_CFT-p3] paragraph

Repeating the same redefinition (3.14) of the operators, the generating function for $\sigma_w'$ now gives the
string coupling identification

\[ p \propto g_s^{2G-2}, \]

(3.21)

as also found by [45]. Note that while for $G=0$ small coupling corresponded to large $p$ (and therefore large
$N$), for $G>1$ the string coupling appears to become large for large $p$. To understand the reason behind
this, we repeat the calculation of $\langle I_\text{CFT} \rangle$ for general $G$,

\[ \langle I_\text{CFT} \rangle_G 
    = \sum_{N_c=1} p^{N_c} Z_{\text{Vac},N_c}^{(G)}
    = \sum_{g} g_s^{2g-2} Z_{\text{Vac},g}^{(G)}, \]

(3.22)

with $Z_{\text{Vac}}^{(G)}$ the corresponding vacuum diagram. For the sphere $G=0$, we only had the sphere
$g=0$ diagram, which gave the expected leading behavior $\langle I_\text{CFT} \rangle \sim g_s^{-2}$. For
$G>1$ one would expect a similar relation to arise from the sphere diagram. However because in this theory the
worldsheet is localized to be a covering of the CFT manifold, the minimal worldsheet genus is $g=G$, so we
find (for small $g_s$) the peculiar relation

\[ \langle I_\text{CFT} \rangle_G \sim p \sim g_s^{2G-2}. \]

(3.23)

This relation explains why the large $p$ (or $N$) limit does not have the same relation to the string coupling
for different $G$’s. We emphasize that in any correlation function, (3.20) forbids tree-level $g=0$ diagrams
for $G\ge 1$. This is a unique property of the $Q_5=1$ string theory, due to the localization of the
worldsheet to the boundary, and we do not expect it (and the related properties discussed in this subsection)
to persist for $Q_5>1$.

#### [sec-higher_genus_CFT-p4] paragraph

An even more peculiar case is the CFT on the torus $G=1$ (related to the string theory on thermal AdS, which
is an orbifold of $AdS_3$). In this case (3.20) degenerates, so that the worldsheet genus is completely
determined by the operator insertions (with $g=1$ for vacuum diagrams), independently of $N_c$. For that
reason we can set $p=1$, and ‘mimic’ a genus expansion by simply appropriately defining a normalized
$\sigma'_w$.

### [section-3.5] section: 3.5 Final comments
#### [section-3.5-p1] paragraph

It is natural to guess that a similar relation between string theory and the CFT applies also to $Q_5>1$. The
natural guess is that while there is an exact CFT for every $Q_1$ and $Q_5$, the NS-NS string theory
backgrounds for $Q_5>1$ are given by a Laplace transform over $Q_1$

\[ Z_{p,Q_5}[J] = \sum_{Q_1=0}^\infty p^{Q_5 Q_1} Z_{Q_1,Q_5}[J], \]

(3.24)

such that only $Z_{p,Q_5}$ has a well behaved string perturbation theory. This suggestion is a refinement of
the Legendre transform suggested in [38] (which gives a good approximation for large $Q_1$ or small $g_s$).
Note that when $Q_1$ is relatively prime to $Q_5$ the CFTs appearing here are also on the moduli space of the
$N=Q_1 Q_5$ free orbifold as discussed above, while for other values of $Q_1$ they are not; it is not obvious
if all values of $Q_1$ should appear in (3.24) or just the relatively prime ones.

#### [section-3.5-p2] paragraph

To be precise, for (3.24) to make sense it is essential to properly normalize the sources in the CFT as a
function of $Q_1$ (as we did in (3.1) above). Furthermore, we saw that to get the expected powers of $g_s$, it
was necessary to also normalize the sources by a power of $p$ (3.14). This is important if we would like to
perform an inverse Laplace transform to fixed $Q_1$. For $Q_5>1$, the operator $I$ (related to $Q_1$) was
found to satisfy [8, 38]

\[ \left\langle I \ \prod_{j=1}^n \Phi_{h_j}(z_j) \right\rangle_{\text{conn},g} = \frac{1}{Q_5}\left(1-g+\sum_{j=1}^n (h_j-1) \right)\cdot \left\langle \prod_{j=1}^n \Phi_{h_j}(z_j) \right\rangle_{\text{conn},g}, \]

(3.25)

where $h_j$ is the CFT dimension of the operator. Comparing with (3.18), this suggests that only in the
normalization of $\Phi_{h}$ where each string diagram comes with a power of $p^{1-g+\sum_{j=1}^n (h_j-1)}$
does an inverse Laplace transform give the fixed $Q_1$ generating function. One can further wonder if
something can be said about the appropriate fixed-$Q_1$ normalization. For large $Q_1$, using the relation
$Q_1 \propto p$, the two-point function will scale as $\langle \Phi_h(z_1)\Phi_h(z_2)\rangle_{Q_1} \sim
Q_1^{2h-1}$. To find the exact normalization, we need to compute the inverse Laplace transform of the full
string theory calculation.

#### [section-3.5-p3] paragraph

For $Q_5=1$, since we have an equality in (3.13) for finite values of $p$, it seems that the perturbative
string theory here captures the full partition function of the free symmetric orbifold, with no non-
perturbative contributions. Naively, for higher genus manifolds, one would expect (based on weakly curved
examples) to have different bulk backgrounds that give saddle points leading to non-perturbative contributions
(in $g_s$) to the same CFT partition function. But, as noted in [45], this is not the case here, suggesting
that the perturbative expansion around any bulk background (with the appropriate boundary) is complete by
itself, giving a strong version of background independence (and in [45] this was shown explicitly for some
orbifolds of $AdS_3$, see also [71]). This is obviously related to the localization of the string worldsheets
on the boundary. Presumably, all of these properties will no longer be present once we deform away from the
free orbifold theory (and, in particular, for $Q_5 > 1$).

## [sec-breakdown] section: 4 Breakdown of string perturbation theory
### [section-4.1] section: 4.1 The large volume limit and S-duality
#### [section-4.1-p1] paragraph

As reviewed in section 2, the symmetric orbifold (2.5) is believed to be dual (up to the Laplace
transformation reviewed in the previous section) to the NS-NS background with $(Q_1,Q_5)=(N,1)$ and vanishing
R-R scalars, where the moduli of the $T^4$ in the symmetric orbifold are identified with the moduli of $T^4$
in string theory (we will discuss the other ${\hat T}^4$ in (2.5) in the next section). The six-dimensional
string coupling in this background is $g_6^2 = 1/N$ (2.3), so this description is weakly coupled when $N\gg
1$, and the $1/N$ expansion of the free orbifold correlation functions [39, 41, 42] was argued to exactly
match with the NS-NS perturbative expansion. However, while for some observables the perturbative expansion is
governed by $g_6$, for other observables it is governed by $g_{10}$, and, in particular, the latter parameter
is expected to control string perturbation theory in the large volume limit. We denote the volume of the torus
in string units in this frame, which is also the dual symmetric orbifold metric, by $V$. Since $g_{10}^2 =
V/N$ (2.3), this implies that string perturbation theory should break down when $V$ becomes as large as $N$,
even though the orbifold remains free for any value of $V$. Moreover, for $g_{10}^2 \gg 1$ the S-dual R-R
background becomes weakly coupled, so we may expect to obtain a different perturbative expansion for the free
orbifold in this large-volume regime, that would reproduce this different string perturbation theory. How is
this consistent with the free orbifold?

#### [section-4.1-p2] paragraph

The point is that even though the orbifold (2.5) is free for any $V$ and $N$, its (non-trivial) $1/N$
expansion, reviewed in the previous section, can sometimes break down. In particular, it was shown in [42]
that this expansion can be mapped to the NS-NS perturbative expansion. In this expansion, for large $V \gg 1$,
higher genus diagrams are proportional to $V^g$, because this factor would arise (for $V \gg 1$) from the
momentum states running in the loops. For instance, the torus partition function of a scalar of radius $R \gg
1$ is proportional to $R$. The general structure of the $1/N$ perturbation theory that arises from the free
orbifold (on a sphere) for $V \gg 1$ is thus schematically

\[ \langle O_{w_1}(z_1) ... O_{w_n}(z_n) \rangle = N^{1-\frac{n}{2}}\left((g=0) + \frac{V}{N} \cdot (g=1) + \cdots + 
    \left(\frac{V}{N}\right)^{g_\text{max}} \cdot (g=g_\text{max})\right), \]

(4.1)

where $g_\text{max}$ is the maximal genus arising in that correlation function. In the language of the free
orbifold, even though it lives on a topologically trivial space, there are non-trivial loops going around
branch points where twist operators are inserted, along which the different $T^4$ factors are permuted, and
there are non-trivial zero modes of the $T^4$ scalars along these loops, such that the integrals over them
give the factors of $V$ in (4.1). Thus, even though the description (2.5) is always free, its $1/N$ expansion
indeed breaks down (in any correlation function that contains $g>0$ contributions) once $V$ becomes as large
as $N$, consistent with the bulk string theory.

#### [section-4.1-p3] paragraph

As mentioned above, S-duality in string theory seems to imply that for $V \gg N$ we should find a new
perturbative description of the free orbifold, that would match with the R-R string theory perturbative
expansion, that has $g_{10}^2 = N/V$. Indeed, our analysis in section 2.1 tells us that this string theory has
a $(Q_1,Q_5)=(N,1)$ R-R description with parameters

\[ g_6^2 = \frac{1}{V}, \quad g_{10}^2 = \frac{N}{V}, \quad \frac{R^2}{\alpha'} = \sqrt{\frac{N}{V}}, \quad \frac{\text{Vol}(T^4)}{\alpha^{'2}} = N, \]

(4.2)

such that the theory with $V \gg N \gg 1$ seems to be weakly coupled.

#### [section-4.1-p4] paragraph

While individual correlation functions like (4.1) can be rewritten as expansions in $N/V$, it is easy to check
that there is no sensible expansion in this parameter of the full theory. The resolution of this apparent
paradox is that (4.2), which follows from supergravity, is not valid in this regime, since it gives an AdS
radius that is much smaller than the string scale. When this happens, we expect all the stringy modes to be at
the AdS energy scale, rather than the string scale. The physics (at least for the gravitational sector) is
expected to be governed by Newton’s constants in AdS units, which are given by the S-duality invariant values

\[ G_N^{(6)}/R^4 = 1/N, \quad G_N^{(10)}/R^8 = V/N. \]

(4.3)

The fact that $G_N^{(10)}$ is large in AdS units implies that perturbation theory is not valid, despite the
naive expectations from (4.2). The bottom line is, as discussed in [23], that for $Q_5=1$ the R-R picture is
always strongly coupled, but the NS-NS picture is weakly coupled for $V \ll N$. For $V \gg N$ both pictures
are strongly coupled. It is only for $Q_5 \gg 1$ that there is a region where the R-R description is truly
weakly coupled, and both the string couplings and Newton’s constants in AdS units are small.

### [sec-planck] section: 4.2 Breakdown of perturbation theory at high energies
#### [sec-planck-p1] paragraph

There is another regime where we expect string perturbation theory to break down, which is the regime of high
energies (scaling as some power of the inverse string scale and the inverse string coupling). In this
subsection, we study the $n$-point function of single-cycle operators, all with dimensions scaling as $E\gg
1$, and we will see for which energies the $1/N$ expansion breaks down. Note that in a highly curved
background it is not clear from the space-time point of view at which energies this should happen.

#### [sec-planck-p2] paragraph

If we look at an operator of dimension $L_0=h$ in the $w$’th twisted sector of the orbifold, its energy (the
conformal dimension of the corresponding twisted sector operator) is given by

\[ L_0 = \frac{h}{w} + \frac{w-w^{-1}}{4}, \]

(4.4)

where the second term comes from the dimension of the twist field (in the NS-NS sector of the CFT). For a
given operator with some $h \gg 1$, this implies that the lowest-energy state it gives will come from the
sector with $w \simeq \sqrt{h}$ and will have $E = L_0+{\overline L}_0 \simeq \sqrt{h}$. Conversely, this
implies that typical operators with energy $E$ will come from sectors with $w \simeq E$.

#### [sec-planck-p3] paragraph

We start by estimating the number of diagrams with genus $g$ that contribute to the $n$-point correlation
function, following [76]. Each genus $g$ diagram satisfies

\[ n - n_E + n_F = 2-2g, \]

(4.5)

with $n_E, n_F$ the number of edges and faces of the skeleton graph. For high enough $E$, we can approximate
the graphs being triangular $3 n_F = 2 n_E$, which gives

\[ n_E = 3(2g-2+n). \]

(4.6)

The diagram is completely determined by the number of edges between each pair of vertices $i$ and $j$, which
we denote by $n_{ij}$. In a graph with $n_E$ edges, $n_{ij}$ has $n_E$ (4.6) non-trivial elements, and it has
to satisfy $\sum_{j} n_{ij} = w_i$, giving $n$ constraints. So overall there are $3(2g-2)+2n$ independent
variables $n_{ij}$, each of order $\sim w \sim E$. In this way we can approximate the number of diagrams by

\[ \# (\text{coverings with genus }g) \simeq E^{3(2g-2)+2n}. \]

(4.7)

#### [sec-planck-p4] paragraph

It is not clear how the contribution of individual diagrams scales in the large energy / cycle length limit.
If we assume that the contribution of each diagram separately does not scale with the energy, then the $1/N$
expansion breaks down when the number of diagrams grows faster than $N^g$, which happens (using (4.7)) when $E
\sim N^{1/6}$. If individual diagrams grow with the energy in a way that depends on the genus, the expansion
could break down at lower scales, such as the naive ten dimensional Planck scale coming from (2.4), which
scales as $N^{1/8}$. In any case, we find that perturbation theory breaks down at high energies going as a
negative power of the string coupling, as expected.

## [sec-decoupled_sec] section: 5 The decoupled sector
### [sec-q5_1_dec_sector] section: 5.1 The decoupled sector of the $Q_5=1$ CFT
#### [sec-q5_1_dec_sector-p1] paragraph

In section 2.2 we reviewed the argument that the SCFT dual of the $Q_5=1$, $Q_1=N$ NS-NS background with
vanishing R-R scalars is given by a product of the symmetric orbifold over $T^4$ and an extra $\hat T^4$
(2.5). The symmetric orbifold ${\rm Sym}_N(T^4)$ has 4 holomorphic and 4 anti-holomorphic $U(1)$ currents
associated with the “center-of-mass” momentum and winding of the $T^4$, whose currents are given by the sums
of the corresponding $U(1)$ currents over the $N$ copies of the $T^4$, such that they have level $N$. The
$\hat T^4$ CFT has its own $8$ (winding and momentum) currents, all at level $1$.

#### [sec-q5_1_dec_sector-p2] paragraph

Invoking the coset construction, it is possible to rewrite this theory as the semi-direct product

\[ (T^{4})^N/S_N\times \hat T^4 \equiv 
    \left((T^{4})^N/S_N\right)/U(1)_N^8 \rtimes \left(U(1)_N^8 \times \hat U(1)_1^8\right). \]

(5.1)

We will name the first term on the right-hand side the “coset CFT”, and the second the “Sugawara CFT”. The
operators of the full theory are spanned by products of operator pairs, one from the coset and one in the
Sugawara $U(1)_N^8 \times \hat U(1)_1^8$ theory; the product with $U(1)_N^8$ is semi-direct, meaning that not
all possible products of operators appear in the theory, while the product with ${\hat U(1)}_1^8$ is direct,
such that the theory contains any operator in this sector multiplied by any operator in the rest of the CFT.

#### [sec-q5_1_dec_sector-p3] paragraph

The left-moving and right-moving energies of the full theory can each be written as a sum

\[ E^{L/R} = E^{L/R}_\text{coset} + E^{L/R}_\text{Sugawara}, \]

(5.2)

with $E_\text{Sugawara}$ given by the Sugawara stress tensor of the $8$ left-moving or right-moving currents.
Due to unitarity, the Sugawara energy of a state gives a lower bound for the left and right moving energies

\[ E^{L/R} \ge E^{L/R}_\text{Sugawara}. \]

(5.3)

#### [sec-q5_1_dec_sector-p4] paragraph

We denote the metric and $B$-field of the $T^4$ in the orbifold by $E = G+B$, and $\hat E = \hat G + \hat B$
for the decoupled $\hat T^4$. We also denote the integer winding and momentum charges of the orbifold by
$w^i$, $p_i$, and the $\hat T^4$ charges by $\hat w^i$, $\hat p_i$ ($i=1,\cdots,4$). In this notation, the
left/right Sugawara energy is given by

\[ \begin{split}
    E_\text{Sugawara}^{L/R} &=\frac{1}{4}
    \begin{bmatrix}
        w & p & \hat w & \hat p
    \end{bmatrix}
    \begin{bmatrix}
        \frac{1}{N}(G+B^T G^{-1} B) & \frac{1}{N}(\pm 1 + B G^{-1}) & 0 & 0\\
        \frac{1}{N}(\pm 1 - G^{-1} B) & \frac{1}{N} G^{-1} & 0 & 0\\
        0 & 0 & \hat G + \hat B^T \hat G^{-1} \hat B & \pm 1 + \hat B \hat G^{-1}\\
        0 & 0 & \pm 1 -\hat G^{-1} \hat B & \hat G^{-1}
    \end{bmatrix}
    \begin{bmatrix}
        w\\
        p \\
        \hat w\\
        \hat p
    \end{bmatrix}.
\end{split} \]

(5.4)

#### [sec-q5_1_dec_sector-p5] paragraph

We now turn to the string theory background with NS-NS fluxes13. The charges $w^i$ and $p_i$ correspond to
fundamental string winding and momentum on the $T^4$, respectively. The extra $\hat T^4$ accounts for the
charges of R-R D-branes wrapping on the $T^4$. In type IIB string theory, we have 4 charges from D1-branes
winding on one of the $T^4$ circles $w^i_\text{D1}$, and $\binom{4}{3}=4$ from D3-branes winding on $3$
circles of the $T^4$, $w^\text{D3}_{i} =\epsilon_{ijkl} w_\text{D3}^{jkl}$. We identify the $\hat T^4$ charges
with the bulk R-R charges by

\[ \hat w^i = w^i_\text{D1}, \quad \hat p_i = w^\text{D3}_{i}. \]

(5.5)

#### [sec-q5_1_dec_sector-p6] paragraph

What is the meaning of the Sugawara energy bound from the string theory side? This question was answered in
[15]. The authors used the description of the $AdS_3 \times S^3 \times T^4$ background as a near-horizon limit
of a flat space brane configuration. The flat-space BPS formula holds even in the decoupling limit, and when
subtracting the energies of the strings and 5-branes making up the background, it gives an energy bound14 on
particle-like excitations in $AdS_3$. We will discuss the energy formula for a general background in the next
subsection. For the $(Q_1,Q_5)=(N,1)$ NS-NS background with $T^4$ metric $G$ and vanishing $B$-field and R-R
scalars, the resulting BPS formula is [15]

\[ \begin{split}
    E_\text{BPS}^{L/R}
    &=
    \frac{1}{4 N^{1/2}} \left(g_{10} w^2 + g_{10}^{-1} w_{D1}^2
    + (g_{10}/V) \ p^2 + (V/g_{10}) \ (w^{D3})^2 \right)
    \pm \frac{1}{2N} p \cdot  w \pm \frac{1}{2} w_{D1} \cdot w^{D3} \\
    &= \frac{1}{4N}\left(V^{1/2} w^2 + V^{-1/2} p^2 \pm 2 w \cdot p\right)
    +\frac{1}{4}\left(V^{-1/2} \hat w^2 + V^{1/2} \hat p^2 \pm 2 \hat w \cdot \hat p \right).
\end{split} \]

(5.6)

All the (implicit) $T^4$ metric contractions in this equation are written in terms of the unit-volume metric
$(G_0)_{ij} = V^{-1/2} G_{ij}$, where $V$ is the $T^4$ volume $V = \sqrt{\det(G)}$. In the second line we used
(5.5) and the relation (2.3)

\[ V = N g_{10}^{2}. \]

(5.7)

To find the relation to the CFT parameters, we compare the bulk BPS bound (5.6) to the CFT Sugawara bound
(5.4). The orbifold metric is immediately identified with the bulk $T^4$ metric, while the $\hat T^4$ metric
has the same shape but an inverse volume, $\hat G = \frac{1}{V} G$. The fact that we got an inverse volume can
be traced to the fact that the D1-brane tension is proportional to $g_{10}^{-1} \sim V^{-1/2}$ (or,
alternatively, to the fact that this extra ${\hat T}^4$ comes from Wilson lines which live on a dual torus).
Choosing a different $\hat G$ in the CFT corresponds in the bulk to different boundary conditions for the
$(U(1)\times U(1))^4$ R-R gauge fields (analogous to a double-trace deformation).

#### [sec-q5_1_dec_sector-p7] paragraph

We can generalize (5.6) to non-zero bulk B-fields, by performing the transformation [15]

\[ p_i \mapsto p_i + B_{ij} w^j, \quad
    \hat w^i \mapsto \hat w^i - \frac{1}{2} \epsilon^{iljk} B_{jk} \hat p_{l}. \]

(5.8)

The first transformation gives a $B$-field (identical to the one in the bulk) to the $T^4$ in the orbifold
CFT. The second (coming from the $C_2 \wedge B_2$ coupling in the D3-brane action) amounts to adding $B^{' ij}
= -\frac{1}{2} \epsilon^{ijkl} B_{kl}$ in the T-dual frame of the $\hat T^4$ sigma-model. Altogether, the CFT
moduli are related to the string theory moduli (for vanishing R-R scalars) by

\[ E_{ij} = G_{ij} + B_{ij}, \quad
    (\hat E)^{-1, ij} = V \cdot G^{-1, ij} - \frac{1}{2} \epsilon^{ijkl} B_{kl}. \]

(5.9)

#### [sec-q5_1_dec_sector-p8] paragraph

What is the worldsheet interpretation of the decoupled sector? The momentum and winding currents of the
orbifold have a clear worldsheet dual, coming from the metric and B-field of the bulk $T^4$, whose $U(1)^8$
currents can be used to construct the corresponding currents of the CFT (for $Q_5>1$ this was discussed in [7,
12], and for $Q_5=1$ in [14]). Perturbative string states are charged under these currents. On the other hand,
the charged states under the ${\hat U(1)}^8_1$ R-R currents can all be constructed as “boundary modes” of the
bulk Chern-Simons theory (for general level $k$ this is only true for states whose charges are integer
multiples of $k$, while here $k=1$). In the bulk they are pure-gauge modes of the R-R gauge potentials. One
would naively expect the $\hat T^4$ currents to have their own worldsheet vertex operator, describing the R-R
potential in the bulk15, and to have D-branes (though no perturbative string states) that carry their charge.
However, the structure of the dual CFT contradicts this expectation.16 Notice that each single-string state
has its single-string descendants under the NS-NS $U(1)^8_N$ current algebra. In the CFT these are descendants
in the core CFT whose symmetric orbifold we are considering. More generally, the existence of a worldsheet
vertex for a CFT current means there’s a $U(1)^8$ current algebra module already in the single-string
partition function $Z_\text{1-string} = \log (Z)$. However, the partition function of the $\hat T^4$ CFT is
simply an overall factor in the full partition function. In terms of the string theory, for every multi-string
state, each of its single-strings has its own NS-NS $U(1)^8_N$ descendants, but only one multi-string R-R
${\hat U(1)}^8_1$, or $\hat T^4$, descendant. This suggests that the $\hat T^4$ ${\hat U}(1)^8_1$ currents
have no local string theory vertex.17

#### [sec-q5_1_dec_sector-p9] paragraph

An alternative perspective on this is that a $(U(1)\times U(1))^4_1$ Chern-Simons theory on $AdS_3$ is dual by
itself to a ${\hat T}^4$ CFT, with the moduli of the ${\hat T}^4$ determined by the boundary conditions on the
CS fields (see, for instance, [77, 78]). So this sector of the theory, which is modular invariant by itself,
decouples completely from the rest of the string theory; it has no interactions with any string states (and
does not even depend on the topology of the interior of the AdS space, just on the boundary conditions). In
particular, even though naively one may expect the string theory with $Q_5=1$ to contain particle-like
D-branes wrapped on cycles of the $T^4$ which are charged under these ${\hat U(1)}$’s, such D-branes have not
yet been found, and this analysis implies that they should not exist as non-trivial boundary states.

#### [sec-q5_1_dec_sector-p10] paragraph

This behavior is special to level $k=1$, and does not apply to the decoupled $U(1)^8_N$ sector; we will
discuss in what sense it is decoupled later, after generalizing to other values of $Q_5$.

### [section-5.2] section: 5.2 String dualities and exact CFT deformations
#### [section-5.2-p1] paragraph

We now extend our discussion to more general string theory backgrounds with different charges, following [15].
We write the string and 5-brane integer fluxes as a charge matrix

\[ Q = \begin{bmatrix}
    f_1 & d_1\\
    -d_5 & n_5
    \end{bmatrix}, \]

(5.10)

which labels the (integer) number of F1, D1, D5, and NS5-branes in the original flat-space construction (we
assume for simplicity there are no wrapped D3-branes). Before taking the near-horizon limit, the backgrounds
are also labeled by $\tau = \chi + i g_{10}^{-1}$ and by $\tilde \tau = A_4 +i v_4 g_{10}^{-1}$. Here $g_{10}$
is the ten-dimensional string coupling, $v_4=\sqrt{{\rm det}(G)}$ the volume of the $T^4$, and $\chi$ and
$A_4$ are the R-R scalar $C_0$ and the holonomy of the R-R 4-form $C_4$ on the $T^4$, respectively.18 It is
useful to write $\tau,\tilde\tau$ also as matrices

\[ \mathcal{T} = g_s \begin{bmatrix}
        1 & -\chi \\
        -\chi & g_s^{-2} + \chi^2
    \end{bmatrix}, \quad
    \tilde{\mathcal{T}} = \frac{g_s}{v_4} \begin{bmatrix}
        1 & -A_4 \\
        -A_4 & v_4^2/g_s^2 + A_4^2
    \end{bmatrix}. \]

(5.11)

When taking the near-horizon limit of a brane configuration with a charge matrix $Q$, the attractor mechanism
gives a relation between $\tau$ and $\tilde\tau$ of the form

\[ \det(Q) \cdot 1 = \tilde{\mathcal{T}} Q \mathcal{T} Q^T. \]

(5.12)

This minimizes the tension formula $\text{tr}(\tilde{\mathcal{T}} Q \mathcal{T} Q^T)$. For example, in the
case of the $d_1,d_5$ background the equation is $\tilde \tau = (d_1/d_5) \tau$.

#### [section-5.2-p2] paragraph

As in the $Q_5=1$ case, we now consider particle excitations in this background. These are labeled by their
$T^4$ winding and momentum $w^i_\text{F1}$, ${\tilde p}_i$, and by the R-R winding charges $w_\text{D1}^i$ and
$w^\text{D3}_i$. It is useful to organize them in pairs based on their natural $T^4$ indices

\[ q^i = \begin{bmatrix}
        w_{F1}^i\\
        w_{D1}^i
    \end{bmatrix}, \quad
    q_i = \begin{bmatrix}
        {\tilde p}_i\\
        w^{D3}_i
    \end{bmatrix}
    . \]

(5.13)

For a general string theory background, the energy bound found by [15] is given by

\[ E_\text{BPS}^{L/R} = \frac{1}{4} \begin{bmatrix}
        q^i & q_j
    \end{bmatrix}
    \begin{bmatrix}
        \frac{\mathcal{T}}{\det^{1/2}(Q)} & \pm Q^{-1}\\
        \pm (Q^{-1})^T & \frac{\tilde{\mathcal{T}}}{\det^{1/2}(Q)}
    \end{bmatrix}
    \begin{bmatrix}
        q^k \\
        q_l
    \end{bmatrix}, \]

(5.14)

where any $T^4$ index contraction is written in terms of the unit metric $v_4^{-1/2} G$ (the $v_4$ dependence
appears through $\mathcal{T}, \tilde{\mathcal{T}}$).

#### [section-5.2-p3] paragraph

The U-duality group of the system is $SO(5,5;\mathbb{Z})$. In this section we are interested only in the
$SL(2,\mathbb{Z})_L\times SL(2,\mathbb{Z})_R$ U-duality subgroup which fixes the general form (5.10) of the
charges, the vanishing of $B_2$ and $C_2$, and the unit-volume metric on the $T^4$. $SL(2,\mathbb{Z})_R$ is
generated by the S-duality of type IIB string theory and by the transformation $\chi \mapsto \chi+1$.
$SL(2,\mathbb{Z})_L$ is generated by $T_{1234} S T_{1234}$ (where $T_{1234}$ means a T-duality transformation
on the four cycles of the $T^4$) and by the transformation $A_4 \mapsto A_4+1$. For $g_L,g_R \in
SL(2,\mathbb{Z})$, the background parameters are transformed by

\[ \begin{split}
    Q' = g_L Q g_R^{T}, \quad \mathcal{T}' = g_R^{-1,T} \mathcal{T} g_R^{-1},
    \quad \tilde{\mathcal{T}}' = g_L^{-1,T} \tilde{\mathcal{T}} g_L^{-1}.
\end{split} \]

(5.15)

The particle charges are transformed by

\[ q^{i\prime} = g_R \cdot q^i, \quad q_j' = g_L \cdot q_j. \]

(5.16)

We note that the energy formula (5.14) (as well as the relation (5.12)) is duality-invariant under the
transformation of the background parameters and the charge lattice.

#### [section-5.2-p4] paragraph

We would like to describe the structure of the conformal manifold for (5.1). Different values of
$\tau,\tilde\tau$ correspond to different deformations of (5.1), but because $\tau$ and $\tilde \tau$ are
related through (5.12), each deformation can be labeled by $\tau$ alone. The $(N,1)$ NS-NS background is given
by

\[ Q = \begin{bmatrix}
    N & 0\\
    0 & 1
    \end{bmatrix}, \]

(5.17)

and we consider values of the charges (5.10) that can be mapped to these charges by a U-duality
transformation. We can then describe the deformations by $\tau$ in this background, and two deformations are
identical if and only if there is a U-duality transformation mapping one $\tau$ to the other, while keeping
the canonical background (5.17) fixed. In other words, the conformal manifold is given by the fundamental
domain of the U-duality subgroup which stabilizes the canonical background (5.17).19 As explained in [15],
this subgroup is isomorphic to the congruence modular subgroup $\Gamma_0(N)$, or the set of pairs

\[ g_L =  \begin{bmatrix}
    \alpha & \beta N \\
    \gamma & \delta
    \end{bmatrix}, \quad
    g_R = \begin{bmatrix}
    -\delta & -\gamma N\\
    -\beta & -\alpha
    \end{bmatrix}, \]

(5.18)

with $\alpha \delta - \beta \gamma N=1$. Figure 1 depicts the fundamental domain of $\Gamma_0(N)$ for $N=30$,
in terms of the S-dual parameter $\tau_{RR} = -1/\tau$. The grey dashed lines separate the domain into
(halves) of $SL(2,\mathbb{Z})$ fundamental domains. The number of $SL(2,\mathbb{Z})$ fundamental domains in
the fundamental domain of $\Gamma_0(N)$ is given by [15, 64]

\[ (SL(2,\mathbb{Z}):\Gamma_0(N)) = N \prod_{\substack{p\mid N\\ p \text{ is prime}}} (1+p^{-1}). \]

(5.19)

The vertical black line corresponds to the $(N,1)$ background with vanishing R-R scalars $\chi=A_4=0$. The
point $\tau_\text{RR} = 0$ corresponds to the $g_{10}=0$ limit of the NS-NS background. The point
$\tau_\text{RR} = i \infty$ is the strongly coupled limit, or, by S-duality, the $g_{10}=0$ limit of the
$(N,1)$ R-R background.

#### [section-5.2-p5] paragraph

Every NS-NS (and R-R) $(Q_1,Q_5)$ background with $Q_1$,$Q_5$ mutually prime is related to the canonical
$(N,1)$ background (5.17) with $N=Q_1\cdot Q_5$ by a U-duality transformation, and can be described as a CFT
deformation of (5.1). We are specifically interested in the singular locus of these backgrounds (with
vanishing R-R scalars $\chi=A_4=0$), given by

\[ Q = \begin{bmatrix}
    Q_1 & 0\\
    0 & Q_5
    \end{bmatrix}, \quad
    \mathcal{T} = \begin{bmatrix}
        t & 0 \\
        0 & t^{-1}
    \end{bmatrix}, \quad
    \tilde{\mathcal{T}} = \begin{bmatrix}
        t^{-1} Q_5/Q_1 & 0 \\
        0 & t Q_1/Q_5
    \end{bmatrix}, \]

(5.20)

with $t$ the ten-dimensional string coupling in the NS-NS $(Q_1,Q_5)$ background. These backgrounds are
related to the canonical background (5.17) by the duality transformation

\[ g_L =  \begin{bmatrix}
    a Q_5 & b Q_1 \\
    1 & 1
    \end{bmatrix}, \quad
    g_R = \begin{bmatrix}
    Q_5 & -Q_1\\
    -b & a
    \end{bmatrix}, \]

(5.21)

with $a$, $b$ integers satisfying $a Q_5 - b Q_1 = 1$. Under the transformation (5.15), the dual canonical
parameters are

\[ g_{10} = a^2 t + b^2 t^{-1}, \quad 
    \chi = -\frac{Q_1 a t + Q_5 b t^{-1}}{a^2 t + b^2 t^{-1}}. \]

(5.22)

#### [section-5.2-p6] paragraph

Written in terms of $\tau_\text{RR} = - (\chi + i/g_{10})^{-1}$, these lines are drawn as thick black arcs in
figure 1. Each arc is drawn twice, related by a sign $\chi\mapsto -\chi$, but the two arcs are identified by
the action of $\Gamma_0(N)$. The limit $t=0$ is the weakly coupled limit of the NS-NS $(Q_1,Q_5)$ background,
which is also dual by a $T_{1234}ST_{1234}$ duality transformation to the weakly coupled R-R $(Q_5,Q_1)$
background.20 Both are mapped to the point $\tau_\text{RR} = \pm b/Q_5$ in the figure. The limit $t=\infty$ in
(5.20) corresponds by S-duality to the weakly coupled R-R $(Q_1,Q_5)$ background, and by another
$T_{1234}ST_{1234}$, to the weakly coupled NS-NS $(Q_5,Q_1)$ background. Both are mapped to $\tau_\text{RR} =
\pm a/Q_1$ in the figure. Generally, the arcs of the fundamental domain’s boundary are identified in a
complicated way. We conjecture that the CP-invariant line $\chi = \pm 1/2$ in the figure (in the R-R
background) corresponds to the orbifold (2.5) at the singular point $\theta=0$ for the 2-cycle at the
$\mathbb{Z}_2$ fixed point; note that this line has $A_4 = \pm N/2$ both in the R-R and in the NS-NS
descriptions21.

#### [section-5.2-p7] paragraph

For a given $t$, the string theory background (5.20) is a deformation of the CFT (5.1); this deformation
involves both a blow-up of the $\mathbb{Z}_2$ singularity of the orbifold, which affects only the “coset CFT”,
and a $J {\bar J}$ deformation, which affects only the “Sugawara CFT”. In the dual $(N,1)$ background, it is
described by $\tau$ and $\tilde \tau$ given by (5.22). Consider a general deformation labeled by
$\tau,\tilde\tau$. For the canonical background (5.12) the two are related by

\[ A_4 = -v_4 \chi, \quad v_4 = \frac{V}{1+ \chi^2 \frac{V}{N}}, \]

(5.23)

with $V = N g_{10}^2$. Labelling a general deformation by $V, \chi$, the BPS energy bound (5.14) gives in the
canonical frame (assuming $B=0$)

\[ \begin{split}
    E_\text{BPS}^{L/R} &= \frac{1}{4} \begin{bmatrix}
        w & p & \hat w & \hat p
    \end{bmatrix}
    \begin{bmatrix}
        \frac{V^{1/2}}{N} & \pm \frac{1}{N} & - \chi \frac{V^{1/2}}{N} & 0\\
        \pm \frac{1}{N} & \frac{1+ \frac{V}{N} \chi^2}{N V^{1/2}} & 0 & \chi \frac{V^{1/2}}{N}\\
        - \chi \frac{V^{1/2}}{N} & 0 & \frac{1+ \frac{V}{N} \chi^2}{V^{1/2}} & \pm 1\\
        0 & \chi \frac{V^{1/2}}{N} & \pm 1 & V^{1/2}
    \end{bmatrix}
    \begin{bmatrix}
        w \\
        p\\
        \hat w\\
        \hat p
    \end{bmatrix}\\
    & = \frac{1}{4N}\left(V^{1/2} (w- \chi \hat w)^2 + V^{-1/2} p^2 \pm  2 w \cdot p \right)\\
    &\quad + \frac{1}{4}\left(V^{-1/2} \hat w^2 + V^{1/2} \left(\hat p+\frac{\chi}{N} p\right)^2 \pm  2 \hat w
\cdot \hat p\right).
\end{split} \]

(5.24)

This generalizes (5.6) to the case of non-zero $\chi$. We see that in the BPS formula the $\chi$ deformation
is equivalent to the shift

\[ w^i \mapsto w^i - \chi \hat w^i, \quad \hat p_j \mapsto \hat p_j +\frac{\chi}{N} p_j. \]

(5.25)

#### [section-5.2-p8] paragraph

We would like to repeat the exercise of the previous section. Interpreting the BPS bound (5.24) as the
Sugawara energy, we can find the Sugawara CFT deformation for every $V, \chi$. However, unlike (5.6), (5.24)
is no longer decoupled between the charges of $T^4$ and $\hat T^4$. It is therefore not enough to simply
deform the $G$, $\hat G$ metrics. As explained in [15], the Sugawara CFT needs to be further deformed by a
mixed $J{\bar J}$ deformation to match with (5.24).

#### [section-5.2-p9] paragraph

Let us denote the $U(1)^8_N$ orbifold currents by $J^i$, $\bar J^i$, and the $U(1)^8_1$ $\hat T^4$ currents by
$\hat J^i$ and $\hat {\bar J}^i$ ($i=1,\cdots,4$). All the currents are normalized such that the corresponding
charges are integers (see appendix A). A general $J{\bar J}$ marginal deformation is of the form

\[ \Delta S  = 2\pi 
    \int d^2 z \left(
    M_{ij}^{11} J^i \bar J^j +
    M_{ij}^{12} J^i \hat {\bar J}^j +
    M_{ij}^{21} \hat J^i \bar J^j +
    M_{ij}^{22} \hat J^i \hat {\bar J}^j
    \right)
    , \]

(5.26)

for some $8\times 8$ matrix $M_{ij}^{\alpha\beta}$ ($\alpha,\beta = 1,2$, $i,j = 1,\cdots,4$). The $M^{22}$
matrix simply deforms the $\hat T^4$ moduli, $\hat E\mapsto \hat E + M^{22}$. $M^{11}, M^{12}$ and $M^{21}$
don’t have such an interpretation, but together with $M^{22}$ they label an $SO(8,8)/(O(8)\times O(8))$
conformal manifold. In the appropriate sense (which takes care of the different levels),
$M_{ij}^{\alpha\beta}$ deforms the metric and the $B$-field on the $T^4\times \hat T^4$ manifold.

#### [section-5.2-p10] paragraph

For every $V$ and $\chi$, it is possible to find the exact $M_{ij}^{\alpha\beta}$ deformation such that the
new $E_\text{Sugawara}$ will exactly agree with the string theory BPS bound (5.24). Starting from the moduli
(5.9) with the appropriate $V$, the answer is

\[ \begin{split}
    M^{11}_{ij} &= 0,\\
    M^{12}_{ij} &= M^{21}_{ij} = - \frac{\chi}{N} G_{ij},\\
    M^{22}_{ij} &= \frac{V}{N} \chi^2 \hat G_{ij} =
    \frac{\chi^2}{N} G_{ij},
\end{split} \]

(5.27)

where in the last equation we used $\hat G = \frac{1}{V} G$. Specifically, plugging in (5.22) will give us the
exact Sugawara CFT deformation which corresponds to the singular $(Q_1,Q_5)$ string theory backgrounds.

#### [section-5.2-p11] paragraph

Let us emphasize that the deformation labeled by $\chi$ on the string theory side deforms both the coset CFT
and the Sugawara CFT in (5.1). The coset deformation is known to correspond at leading order to one of the
blow-up modes of the $\mathbb{Z}_2$ orbifold singularity [79]. Following the deformation is a highly
complicated task, even in conformal perturbation theory, and it is beyond the scope of this paper (see [80,
81, 82, 83, 84, 85, 86, 87, 88] and references therein for recent progress on this). In this section we
identified the exact deformation only of the Sugawara part of the CFT, not the coset CFT. This was possible
because the $J{\bar J}$ deformation is integrable from the CFT perspective, and can be matched exactly to the
string theory using string dualities.

### [section-5.3] section: 5.3 The decoupled sector of the $Q_5>1$ CFT
#### [section-5.3-p1] paragraph

In section 5.1 we asked for the worldsheet interpretation of the decoupled $\hat T^4$ currents. For the
backgrounds (5.20) at small $g_{10}=t$ there is a different perturbative worldsheet description with $Q_5 > 1$
[5, 7, 8, 37]. We would like to ask more generally, what is the $Q_5>1$ worldsheet interpretation of the
deformed Sugawara CFT (5.27)?

#### [section-5.3-p2] paragraph

First, it is useful to re-write the Sugawara energy (5.24) in terms of the $(Q_1,Q_5)$ charges, and not the
original CFT charges. The two charge lattices are related through (5.16), (5.21) by

\[ \begin{bmatrix}
        w^i_{F1}\\
        w^i_{D1}
    \end{bmatrix}
    = \begin{bmatrix}
        a & Q_1\\
        b & Q_5
    \end{bmatrix}
    \begin{bmatrix}
        w^i\\
        \hat w^i
    \end{bmatrix}, \quad
    \begin{bmatrix}
        {\tilde p}_j\\
        w_j^{D3}
    \end{bmatrix} =
    \begin{bmatrix}
        1 & -b Q_1 \\
        -1 & a Q_5
    \end{bmatrix}
    \begin{bmatrix}
        p_j\\
        \hat p_j
    \end{bmatrix}. \]

(5.28)

In terms of the $(Q_1,Q_5)$ string theory charges, the Sugawara energy (also given directly from (5.14)) takes
the simple form

\[ \begin{split}
    E_\text{Sugawara}^{L/R} &= \frac{1}{4 Q_1} \left(
    v_4^{1/2} w_\text{F1}^2 + v_4^{-1/2} {\tilde p}^2 \pm 2 w_\text{F1}\cdot {\tilde p}\right)\\
    &+ \frac{1}{4 Q_5} \left(
    v_4^{1/2} (w^\text{D3})^2 + v_4^{-1/2} w_\text{D1}^2 \pm 2 w_\text{D1}\cdot w^\text{D3}\right),
\end{split} \]

(5.29)

where $v_4 = t^2 Q_1/Q_5$ is the worldsheet $T^4$ volume (2.3). Equation (5.29) should be understood as the
generalization of (5.6) for $Q_5>1$. It agrees with the fact that, as reviewed in section 2, the bulk theory
includes a $U(1)^8_{Q_1}\times U(1)^8_{Q_5}$ CS theory in $AdS_3$, from the $4+4$ NS-NS and $4+4$ R-R bulk
gauge fields, respectively. The $J{\bar J}$ deformation at these points in the moduli space has precisely the
effect of forming orthogonal linear combinations of the original currents of (5.1) that have these new levels.
Each set of currents involves linear combinations of the currents from the orbifold and from ${\hat T}^4$.

#### [section-5.3-p3] paragraph

Just as in the $Q_5=1$ case, the NS-NS currents at level $Q_1$ have a string worldsheet vertex operator, found
explicitly in [7]. As the authors comment there, the R-R currents do not seem to appear in the string
spectrum, consistent with the fact discussed above that single-string states should have descendants under $8$
of the $U(1)$ symmetries but not under the other $8$.22 This also agrees with the string 1-loop calculation
done recently for $Q_5>1$ [89], in which the $U(1)^8_{Q_5}$ R-R currents were absent.23

#### [section-5.3-p4] paragraph

After discussing the currents of the decoupled Sugawara sector, we would next like to understand the bulk
interpretation of its charged states. Consider first the undeformed theory (5.1) for $Q_5=1$. A general
charged state will satisfy the Sugawara/BPS bound, but will not saturate it. The operators that saturate the
bound are exactly the operators that are given entirely by the Sugawara CFT, with only the identity in the
coset CFT. These operators can have any $\hat w$, $\hat p$ integer charges (any operator from $\hat T^4$), but
the charges $w,p$ must be integer multiples of $N$. We term this charge sub-lattice the BPS lattice24. We can
immediately generalize this statement to the $(Q_1, Q_5)$ backgrounds. Under the $\chi$, $V$ deformation, the
energy of the coset changes in a non-trivial way. However, for the BPS lattice, the coset operator is simply
the identity. Therefore, also at finite $\chi$ these operators remain BPS, as their energy is given exactly by
the (deformed) Sugawara energy (5.29). In order to understand what are these operators from the perspective of
the $(Q_1, Q_5)$ background, we rewrite (5.28) as

\[ \begin{bmatrix}
        \frac{w^i_{F1}}{Q_1}\\
        \frac{w^i_{D1}}{Q_5}
    \end{bmatrix}
    = \begin{bmatrix}
        a Q_5 & 1\\
        b Q_1 & 1
    \end{bmatrix}
    \begin{bmatrix}
        \frac{w^i}{N}\\
        \hat w^i
    \end{bmatrix}, \quad
    \begin{bmatrix}
        \frac{{\tilde p}_j}{Q_1}\\
        \frac{w_j^{D3}}{Q_5}
    \end{bmatrix} =
    \begin{bmatrix}
        Q_5 & -b \\
        -Q_1 & a
    \end{bmatrix}
    \begin{bmatrix}
        \frac{p_j}{N}\\
        \hat p_j
    \end{bmatrix}
    . \]

(5.30)

The matrices appearing here also have determinant $1$. Therefore, in terms of the $(Q_1,Q_5)$ NS-NS theory,
the BPS sub-lattice $w,p = 0 \text{ mod } N$ is exactly

\[ \begin{split}
    w_\text{F1}^i &= {\tilde p}_j = 0 \text{ mod } Q_1,\\
    w_\text{D1}^i &= w^\text{D3}_j = 0 \text{ mod }Q_5.
\end{split} \]

(5.31)

Namely, the charges are all integer multiples of the corresponding Chern-Simons levels. States carrying other
charges, including now also singly-wrapped D-branes, are not BPS.

#### [section-5.3-p5] paragraph

We now discuss the bulk interpretation of this BPS lattice. Already in the undeformed case, the interpretation
of the $\hat T^4$ charged states seems to have a paradoxical nature. On the one hand, they carry R-R charge
($\hat p$, $\hat w$), with the interpretation of D-branes. On the other hand, these states exactly decouple
from the entire closed string spectrum (and for example don’t emit gravitons). This seems to contradict the
basic property of D-branes as worldsheet boundary conditions. For $Q_5>1$ we found a generalization of that
question. The BPS states don’t just saturate the bound. As they live entirely in the Sugawara CFT, they also
decouple exactly (in correlation functions) from operators in the coset CFT. These modes appear to be
completely topological, and yet they carry ($Q_5$-quantized) R-R charges like D-branes.25 Similarly, we find
states carrying the same charge as $Q_1$ winding fundamental strings, that decouple from all operators in the
coset CFT.

#### [section-5.3-p6] paragraph

The solution to the paradox is that these states are pure bulk gauge modes, not D-branes, that nevertheless
carry R-R (and/or NS-NS) charges. One way to think of these modes is as boundary modes of the low-energy
Chern-Simons theories, as in our discussion of the $Q_5=1$ case above. Alternatively, the existence of such
charged modes in string theory in the presence of non-zero Kalb-Ramond $H_3$ flux was described in [91].
Consider the $AdS_3\times S^3 \times T^4$ type IIA background with $H_3 = Q_5 \omega_3$, with $\omega_3$ the
unit volume-form on the $S^3$ (the $AdS_3$ component of the flux is not important for our analysis).26 Denote
the pure-gauge mode of the $C_3$ field on $S^3$ by $\psi$,

\[ C_3 = \psi\  \omega_3 + c_3, \]

(5.32)

where $c_3$ includes the rest of the directions. In type IIA, the gauge transformation of $\delta C_1 = d
\Lambda$ is followed by $\delta C_3 =\Lambda H_3$ [92], with 0-form $\Lambda$. In our case,

\[ \delta \psi = Q_5 \Lambda. \]

(5.33)

Because $\psi$ is the $C_3$ holonomy over $S^3$, $\psi\sim \psi +2\pi$. The holonomy $\exp(i \psi)$ is thus an
operator with charge $Q_5$ under the R-R gauge field $C_1$. In terms of type IIB charges (upon T-dualizing one
of the $T^4$ directions), those are pure $C_4$ (wrapping $S^3\times T^1$) gauge modes with $w_\text{D1}=Q_5$
R-R charge. Applying T-duality on the four directions of the torus also reveals pure $\tilde C_6$ modes
(wrapping $S^3\times T^3$) with $Q_5$-quantized $w^\text{D3}$ charge. Applying $ST_{1234}S$ gives the
topological modes with $Q_1$-quantized momentum and winding modes. In the language of [91], the full string
theory includes a $U(1)^{16}$ gauge theory with $\mathbb{Z}^{16}$ charges, but the coset has only
$\mathbb{Z}_{Q_1}^8 \oplus \mathbb{Z}_{Q_5}^8 \equiv \mathbb{Z}_{Q_1 Q_5}^{8}$ charges.

## [acknowledgments] section: Acknowledgments
### [acknowledgments-p1] paragraph

We would like to thank Vijay Balasubramanian, Lorenz Eberhardt, Rajesh Gopakumar, David Kutasov, Juan
Maldacena, Emil Martinec, Sameer Murthy, Mukund Rangamani, and Edward Witten for useful discussions. We
especially thank Matthias Gaberdiel and Rohit Kalloor for many useful discussions and for collaboration in the
early stages of the project. This work was supported in part by an Israel Science Foundation (ISF) grant
number 2159/22, by Simons Foundation grant 994296 (Simons Collaboration on Confinement and QCD Strings), by
the Minerva foundation with funding from the Federal German Ministry for Education and Research, by the German
Research Foundation through a German-Israeli Project Cooperation (DIP) grant “Holography and the Swampland”,
and by a research grant from Martin Eisenstein. OA is the Samuel Sebba Professorial Chair of Pure and Applied
Physics.

## [app-orbifold] appendix: A Toroidal sigma models and $J\bar J$ deformations
### [app-orbifold-p1] paragraph

In this appendix we write down basic facts about $1+1$ dimensional sigma models on tori and their $J\bar J$
deformations.

### [section-A.1] appendix: A.1 Compact bosons
#### [section-A.1-p1] paragraph

We will follow Polchinski’s notations [93] with

\[ \begin{split}
    z &= \sigma^1 + i \sigma^2, \quad \bar z = \sigma^1 - i \sigma^2,\\
    \partial &= \frac{1}{2}(\partial_1 - i \partial_2), \quad \bar\partial = \frac{1}{2}(\partial_1 + i
\partial_2),
\end{split} \]

(A.1)

and $d^2 z = 2 d^2 \sigma$. We take $d$ compact scalar fields $X^i$ ($i=1,\cdots,d$) with

\[ X^i \sim X^i + 2\pi. \]

(A.2)

In these conventions, we take the (Euclidean) action

\[ \begin{split}
    S &= \frac{1}{4\pi} \int d^2 \sigma \left(G_{ij} g^{\mu\nu} + i B_{ij} \epsilon^{\mu\nu}\right)
\partial_\mu X^i \partial_\nu X^j \\
    &= \frac{1}{2\pi} \int d^2 z \left(G_{ij} \partial X^i \bar\partial X^j + B_{ij} \partial X^i \bar\partial
X^j\right),
\end{split} \]

(A.3)

with some constant metric and B-field $E_{ij} = G_{ij} + B_{ij}$. The momentum and winding Noether currents
are

\[ \begin{split}
    J^{\mu}_i &= \frac{1}{2\pi} \left(G_{ij} g^{\mu\nu} + i B_{ij} \epsilon^{\mu\nu}\right)\partial_\nu X^j,\\
    \tilde J_\mu^i &= \epsilon_{\mu\nu} G^{ij} J_{j}^\nu =
    \frac{1}{2\pi} \left(\delta_j^i \epsilon_{\mu\nu} - i G^{ik} B_{kj} g_{\mu\nu} \right)\partial^\nu X^j.
\end{split} \]

(A.4)

We can write these in a holomorphic/anti-holomorphic basis

\[ \begin{split}   
    J_{i} &= \frac{1}{2}(J_{i, z} - i \tilde J_{i, z})
    = \frac{1}{2\pi} \left(
    G_{ij} - B_{ij} \right) \partial X^j,
    \\
    \bar J_{i} &= \frac{1}{2}(J_{i,\bar z} + i \tilde J_{i,\bar z}) =
    \frac{1}{2\pi} \left(
    G_{ij} + B_{ij} \right) \bar \partial X^j,
\end{split} \]

(A.5)

which satisfy $\bar \partial J_{i} = \partial \bar J_{i} = 0$.

#### [section-A.1-p2] paragraph

To consider the Hilbert space on a circle, we use the transformation $z=\exp(-i w)$, with

\[ w = \theta + i \tau \sim w + 2\pi. \]

(A.6)

To consider the Lorentzian version we further take $\tau=it$. The different particle sectors are labeled by
the winding $w^j \in \mathbb{Z}$

\[ X^j(w + 2 \pi) = X^j(w) + 2\pi w^j, \]

(A.7)

and the center of mass momentum $p_i \in \mathbb{Z}$

\[ p_i = \int d\theta J^{t}_{i} = G_{ij} v^j + B_{ij} w^j, \]

(A.8)

with the target space velocity $v^i$ , with the quantization

\[ v_i = p_i - B_{ij} w^j. \]

(A.9)

The Hilbert space is labeled by the integers $p_i, w^j$ together with the usual harmonic oscillators
$\alpha_n$. The Hamiltonian (ignoring the Casimir energy) is given by

\[ H = \frac{1}{4}\left(v_R^2 + v_L^2\right) + N + \bar N, \]

(A.10)

with

\[ v_{i,L/R} = v_i \pm G_{ij} w^j. \]

(A.11)

The Sugawara energy is given solely by the first term in (A.10), which gives a lower bound on $L_0,\bar L_0$,

\[ \begin{split}
    E^{L/R}_\text{Sugawara} = \frac{1}{4} v_{L/R}^2
    &= \frac{1}{4}v^2 + \frac{1}{4}w^2 \pm \frac{1}{2} v \cdot w\\
    &=\frac{1}{4}
    \begin{bmatrix}
        w^i & p_j
    \end{bmatrix}
    \begin{bmatrix}
        G + B^T G^{-1} B & \pm1 +B G^{-1}\\
        \pm 1-G^{-1}B & G^{-1}
    \end{bmatrix}
    \begin{bmatrix}
        w^i\\
        p_j
    \end{bmatrix},
\end{split} \]

(A.12)

where we omitted the $G$ contractions in the first line. The last formula is explicitly invariant under
T-duality, which acts as

\[ p_i \leftrightarrow w^i, \quad E \leftrightarrow E^{-1}. \]

(A.13)

#### [section-A.1-p3] paragraph

Back to the Euclidean plane $z,\bar z$. For a given $G,B$ we would like to know the metric on the currents.
The two-point function

\[ \begin{split}
    \langle \partial X^i(z) \partial X^j(0) \rangle &=  \frac{G^{ij}}{2z^2},\\
    \langle \bar\partial X^i(\bar z) \bar\partial X^j(0) \rangle &= \frac{G^{ij} }{2\bar z^2},
\end{split} \]

(A.14)

gives the current two-point function for the chiral components of the momentum current (A.5)

\[ \begin{split}
    \langle J_i(z) J_j(0) \rangle &= \frac{1}{8\pi^2} \frac{G_{ij} + B_{ik} G^{k l} B_{lj}}{z^2},\\
    \langle \bar J_i(\bar z) \bar J_j(0) \rangle &=
    \frac{1}{8\pi^2} \frac{G_{ij} + B_{ik} G^{k l} B_{lj}}{\bar z^2}.
\end{split} \]

(A.15)

This exactly the $G+B^T G^{-1}B$ term that we have in (A.12). The winding Noether current is given by $\hat
J^{\mu,i}=\frac{1}{2\pi}\epsilon^{\mu\nu}\partial_\mu X^i$. Its holomorphic and anti-holomorphic components
are 27

\[ J^i = \frac{i}{2\pi}\partial X^i, \quad  \bar J^j = -\frac{i}{2\pi} \bar \partial X^j, \]

(A.16)

which are also given by raising the target space index of (A.5) using $E$. The two-point function is

\[ \begin{split}
    \langle J^i(z) J^j(0) \rangle &= -\frac{1}{8\pi^2} \frac{G^{ij}}{z^2},\\
    \langle {\bar J}^i(\bar z) {\bar J}^j(0) \rangle &=
    -\frac{1}{8\pi^2} \frac{G^{ij}}{\bar z^2},
\end{split} \]

(A.17)

with the mixed terms

\[ \begin{split}
    \langle J_i(z) J^j(0) \rangle &= \frac{i}{8\pi^2} \frac{\delta_i^j-B_{ik}G^{kj}}{z^2},\\
    \langle \bar J_i(\bar z) {\bar J}^j(0) \rangle &=
    -\frac{i}{8\pi^2} \frac{\delta_i^j+B_{ik}G^{kj}}{\bar z^2}.
\end{split} \]

(A.18)

We can directly see that the matrix (A.12) is also the matrix of the current-current two-point functions, as
required in the Sugawara construction.

#### [section-A.1-p4] paragraph

The $J \bar J$ deformation [94] (see also the recent [95]) is given by the general deformation

\[ \partial_\lambda S  = 2\pi \int d^2 z M^{ij} J_i \bar J_j
    =\frac{1}{2\pi}\int d^2z E_{ki} M^{ij} E_{jl} \partial X^k \bar \partial X^l, \]

(A.19)

for some matrix $M^{ij}$ and currents $J_i, \bar J_j$ depending on $\lambda$. In other words, the sigma-model
moduli exactly changes with

\[ \partial_\lambda E_{ij} = E_{ik} M^{kl} E_{lj}. \]

(A.20)

These deformations cover the entire space of $E_{ij}$ deformations. They can be labeled by the
$O(d,d)/\\(O(d)\times O(d))$ moduli.

### [section-A.2] appendix: A.2 Going to the next level
#### [section-A.2-p1] paragraph

We will now specialize to the (bosonic version of) theory (2.5). Namely, we have $4N$ fields $X^{I,i}$
($I=1,\cdots,N$ and $i=1,\cdots,4$) which will constitute the $T^{4N}/S_N$ orbifold, and $4$ more fields $\hat
X^i$. We assume the moduli on the $X^{I,i}$ are independent of $I$ and consist of “single-trace" moduli. The
action is given by

\[ \begin{split}
    S &= \frac{1}{2\pi} \int d^2 z \left(E_{ij} \partial X^{I,i} \bar\partial X^{I,j}
    + \hat E_{ij} \partial \hat X^i \bar\partial \hat X^j\right).
\end{split} \]

(A.21)

#### [section-A.2-p2] paragraph

The single-trace momentum currents are

\[ \begin{split}
    J_i = \frac{1}{2\pi} \sum_{I=1}^N E_{ji} \partial X^{I,j}, &\quad
    \bar J_i = \frac{1}{2\pi} \sum_{I=1}^N E_{ij} \bar \partial X^{I,j},\\
    \hat J_i = \frac{1}{2\pi}\hat E_{ji} \partial \hat X^{j}, &\quad
    \hat {\bar J}_i = \frac{1}{2\pi} \hat E_{ij} \bar \partial \hat X^{j}.
\end{split} \]

(A.22)

In the normalization we use, the $w$-cycle twisted sectors (including the untwisted sector) have integer
charges $Q_i, Q^j$. We denote the integer charges of these currents by $w^i$, $p_j$, $\hat w^k$ and $\hat
p_l$, respectively.

#### [section-A.2-p3] paragraph

Setting $E=G+B$, $\hat E = \hat G + \hat B$, the two-point function for the currents is

\[ \begin{split}
    \langle J_i(z) J_j(0) \rangle &= \frac{N}{8\pi^2 }\frac{G_{ij} + B_{ik} G^{kl}B_{lj}}{z^2},\\
    \langle \hat J_i(z) \hat J_j(0) \rangle &= \frac{1}{8\pi^2}\frac{\hat G_{ij} + \hat B_{ik} \hat G^{kl}
\hat B_{lj}}{z^2}.
\end{split} \]

(A.23)

Inverting the matrix, the Sugawara energy bound is given by

\[ \begin{split}
    E^{L/R}_\text{Sugawara} &=\frac{1}{4}
    \begin{bmatrix}
        w & p & \hat w & \hat p
    \end{bmatrix}
    \begin{bmatrix}
        \frac{G+B^T G^{-1} B}{N} & \frac{\pm 1 + B G^{-1}}{N} & 0 & 0\\
        \frac{\pm 1 - G^{-1} B}{N} & \frac{1}{N} G^{-1} & 0 & 0\\
        0 & 0 & \hat G + \hat B^T \hat G^{-1} \hat B & \pm 1 + \hat B \hat G^{-1}\\
        0 & 0 & \pm 1 -\hat G^{-1} \hat B & \hat G^{-1}
    \end{bmatrix}
    \begin{bmatrix}
        w\\
        p \\
        \hat w\\
        \hat p
    \end{bmatrix}.
\end{split} \]

(A.24)

Notice that this is exactly two blocks of (A.12), only with the $p, w$ block multiplied by $1/N$ (as the two-
point functions of $J$ are proportional to $N$).

#### [section-A.2-p4] paragraph

A general $J\bar J$ deformation in this theory can be written as

\[ \partial_\lambda S  = 2\pi
    \int d^2 z \left(
    M_{ij}^{11} J^i \bar J^j +
    M_{ij}^{12} J^i \hat {\bar J}^j +
    M_{ij}^{21} \hat J^i \bar J^j +
    M_{ij}^{22} \hat J^i \hat {\bar J}^j
    \right)
    , \]

(A.25)

for some $8\times 8$ matrix $M_{ij}^{\alpha\beta}$ ($\alpha,\beta = 1,2$, $i,j = 1,\cdots,4$). In (A.25) we
raise indices of $J,\bar J$ by $E$, and those of $\hat J, \hat {\bar J}$ by $\hat E$. The $M^{22}$ matrix
simply deforms the $\hat T^4$ moduli just like (A.20),

\[ \partial_\lambda \hat E_{ij} = M_{ij}^{22}. \]

(A.26)

$M^{11}, M^{12}$ and $M^{21}$ do not have that interpretation anymore, but together with $M^{22}$ they label
an $SO(8,8)/(O(8)\times O(8))$ manifold.

#### [section-A.2-p5] paragraph

To make contact with the $\chi$-deformation of (5.24), we set $B=\hat B=0$ and consider the $J \bar J$
deformation

\[ \begin{split}
    M^{11}_{ij} &= 0,\\
    M^{12}_{ij} &= M^{21}_{ij} = - \frac{\chi}{N} G_{ij},\\
    M^{22}_{ij} &= \frac{V}{N} \chi^2 \hat G_{ij} =
    \frac{\chi^2}{N} G_{ij},
\end{split} \]

(A.27)

where we took $\hat G = \frac{1}{V} G$ as in section 5. In terms of the (un-gauged) $4N+4$ fields, we deformed
the $(4N+4)\times(4N+4)$ metric to

\[ \begin{split}
    G_{4N+4} =
    \mleft[
    \begin{array}{c|c}
      \delta_{IJ} & -  \chi \frac{1}{N}\\
      \hline
      -  \chi \frac{1}{N} & V^{-1} + \frac{\chi^2}{N}
    \end{array}
    \mright] \otimes G,
\end{split} \]

(A.28)

with the inverse

\[ \begin{split}
    G_{4N+4}^{-1} =
    \mleft[
    \begin{array}{c|c}
      \delta_{IJ} + \frac{V \chi^2}{N^2} & \chi \frac{V}{N} \\
      \hline
       \chi \frac{V}{N} & V
    \end{array}
    \mright] \otimes G^{-1}.
\end{split} \]

(A.29)

Projecting to the single-trace currents (A.22) gives the Sugawara energy

\[ \begin{split}
    E^{L/R}_\text{Sugawara} &=\frac{1}{4}
    \begin{bmatrix}
        w & \hat w & p & \hat p
    \end{bmatrix}
    \begin{bmatrix}
        \frac{1}{N} G & - \chi \frac{1}{N} G & \pm \frac{1}{N} & 0\\
        - \chi \frac{1}{N} G & \frac{1+ \frac{V}{N} \chi^2}{V} G & 0 & \pm 1\\
        \pm \frac{1}{N} & 0 & \frac{1+ \frac{V}{N} \chi^2}{N} G^{-1} & \chi \frac{V}{N} G^{-1}\\
        0 & \pm 1 & \chi \frac{V}{N} G^{-1} & V G^{-1}
    \end{bmatrix}
    \begin{bmatrix}
        w \\
        \hat w\\
        p \\
        \hat p
    \end{bmatrix}.
\end{split} \]

(A.30)

Re-writing in terms of contractions with the unit metric $V^{-1/2} G$ (and changing the order of the vector
components) gives exactly (5.24).

#### [footnotes] footnotes: Footnotes

Notes1Naively this statement contradicts statements made in the previous paragraphs, because we stated that
the $(Q_1,Q_5)=(N,1)$ theory is the same as the $(Q_1,Q_5)=(1,N)$ theory (possibly at different values of the
moduli), and naively the latter theory of a single instanton in $U(N)$ is expected to have a continuous
spectrum because of the small-instanton singularity. However, it turns out that there are actually no smooth
$SU(N)$ instantons on $T^4$ [58], so the naive expectation that the local small-instanton singularity looks
the same on $T^4$ and on $\mathbb{R}^4$ does not hold in the $Q_1=1$ case. Our arguments imply that the sigma
model on the one-instanton moduli space of $U(N)$ on $T^4$ should be given by the free orbifold (2.5), which
one would naively obtain from the position of a zero-size-instanton and from the $U(N)$ Wilson lines in this
theory, and it would be interesting to confirm this directly.

2In [15] it was assumed that the free orbifold (2.5) sits at $Q_5=1$ at a non-zero value of the R-R scalar
$\chi$, since at the time it was believed that the $\chi=0$ theory has a continuous spectrum (as it does for
higher values of $Q_5$). However, up to moving the subspace associated with the free orbifold to sit at
$\chi=0$, the analysis of the dualities relating different backgrounds in [15] is still valid, and we review
it in this subsection and in section 5.

3The number of fundamental domains of $SL(2,\mathbb{Z})$ inside a fundamental domain of $\Gamma_0(N)$ is $N
\prod_{p | N, p\ \text{prime}} (1 + p^{-1})$ [64]. For $N=30$, which we draw in the figure, it is $72$.

4It was suggested in [68] that perhaps even the full CFT has a description as a deformed symmetric orbifold of
this type.

5Note that perturbative string theory in the R-R background is believed to correspond to fixed fluxes; in
particular string theory in this background has a T-duality symmetry exchanging $Q_1$ and $Q_5$.

6We stress that the CFT still maintains standard field-theory cluster decomposition at fixed $N$. It is only
the string theory interpretation that breaks. It was noticed in [38] that the string theory dual for $Q_5>1$
does not obey field-theory cluster decomposition, due to the Legendre transform; we will comment further on
$Q_5>1$ below.

7As we will discuss below, $p$ is related to the string coupling. In general it is not clear if the sum (3.9)
converges, and correspondingly we do not expect string perturbation theory to converge but just to be an
asymptotic series. Our statement is that the asymptotic series on the two sides of the duality are the same.
In the special case of the free orbifold CFT on a sphere we will see that the sum does converge (at least for
any finite number of operator insertions).

8We include here the $w=1$ case even though $\sigma_1(z)$ is trivial, because the same formulas will be
relevant also for sources for any other operators from the same sectors.

9We are not writing down explicitly the dependence of the CFT partition function on the metric (some such
dependence is required by the conformal anomaly), and, if it is on a manifold of genus $G \geq 1$, on the spin
structure. The covering spaces inherit the metric and spin structure in an obvious way from those of the
original manifold.

10The fact that only for single-cycle operators the grand-canonical partition function exponentiates further
supports their identification as single-string states.

11It would be interesting to study extensions of (3.12) to incorporate defects [72], and other permutation
groups [73, 74].

12This suggests in particular that the string theory dual to the CFT on a disconnected surface should also
correspond to a product of the corresponding $Z_p$’s, rather than the naive product of the corresponding
$Z_N$’s, as discussed in [45].

13In this section we ignore the fact that perturbative string theory in this background actually involves a
grand-canonical ensemble of CFTs, as discussed in section 3; namely, we consider the theory with fixed $Q_1$
and $Q_5$, even though its perturbative string description is more complicated. The U-duality group that we
discuss in this section acts naturally on the backgrounds with fixed $Q_1$ and $Q_5$, rather than on the
grand-canonical ensemble that appears in the perturbative NS-NS-background string.

14This is obvious in the R-R sector of the CFT, in which the fermions are periodic around the circle and
supersymmetry is preserved. Here we discuss the NS-NS sector of the CFT which is dual to string theory on
$AdS_3$ (where the spatial circle of the CFT is contractible), where the fermions are anti-periodic, so that
the configuration does not directly arise as a near-horizon limit. However, ${\cal N}=(4,4)$ supersymmetry
implies that this sector is related by spectral flow to the R-R sector, so the same BPS bounds hold.

15One reason why this is not obvious is that in flat space, vertex operators for R-R potentials, as opposed to
field strengths, exist in some pictures for the worldsheet ghosts but not in others.

16We thank Sameer Murthy and Mukund Rangamani for discussions on this issue.

17It is possible that worldsheet operators for the total charge of these currents can be defined.

18We assume here vanishing $B_2$ and $C_2$ fields on the $T^4$, although the generalization is straightforward
[15].

19Of course, we could just as well describe the geometry of the conformal manifold in terms of deformations of
any other string theory background U-dual to (5.17).

20By weak coupling here we mean a small ten-dimensional string coupling; as discussed above, this does not
necessarily imply that the six-dimensional string coupling or Newton’s constant are small, so the theory may
not really be weakly coupled.

21The line $\chi=\pm N/2$ in the $(N,1)$ NS-NS background, which is related to the $A_4 = \pm N/2$ line by
T-duality in the NS-NS frame, and that appears in the figure as the two (identified) boundary arcs emanating
from $\tau_\text{RR}=0$, is also singular.

22Note that the higher Kaluza-Klein modes of the R-R potential which have a non-zero R-R field strength do
have a worldsheet vertex operator [7], but here we consider the pure-gauge mode of the R-R potential.

23We thank Rohit Kalloor for his help in clarifying this issue.

24Note that the states saturating the Sugawara/BPS bound are BPS states before taking the near-horizon limit,
where the supersymmetry algebra has central charges corresponding to the momenta and winding numbers on the
$T^4$. These states are not BPS states of the theory on $AdS_3$, where there are different BPS states,
carrying charges under the $SU(2)_L\times SU(2)_R$ symmetry; we do not discuss these states here. The bound on
the energy of the states we discuss in $AdS_3$ comes from the form of the CFT energy-momentum tensor discussed
above, rather than from the supersymmetry algebra.

25For $Q_5>1$ there are also operators with $O(1)$ R-R charge that are not BPS, and we expect them to take the
form of D-branes in the bulk. For $Q_5=1$ all the operators with R-R charge are BPS, and in this theory we
expect no D-brane particle excitations (see also [90, 72]).

26We use the conventions of [91] which are slightly different than [92], but more natural for these purposes.

27These $i$’s are an outcome of the holomorphic coordinates in Euclidean space with $\epsilon_{z,\bar z} =
\frac{i}{2}$. After continuing to the circle $w,\bar w = \theta \mp t$ we have $\epsilon_{w,\bar w} =
\frac{1}{2}$, which gives the familiar formulas.

#### [refs] references: References

References[1]J.M. Maldacena, The Large N limit of superconformal field theories and supergravity, Adv. Theor.
Math. Phys. 2 (1998) 231 [hep-th/9711200].
[2]O. Aharony, S.S. Gubser, J.M. Maldacena, H. Ooguri and Y. Oz, Large N field theories, string theory and
gravity, Phys. Rept. 323 (2000) 183 [hep-th/9905111].
[3]J.M. Maldacena and A. Strominger, AdS(3) black holes and a stringy exclusion principle, JHEP 12 (1998) 005
[hep-th/9804085].
[4]J.M. Evans, M.R. Gaberdiel and M.J. Perry, The no ghost theorem for AdS(3) and the stringy exclusion
principle, Nucl. Phys. B 535 (1998) 152 [hep-th/9806024].
[5]A. Giveon, D. Kutasov and N. Seiberg, Comments on string theory on AdS(3), Adv. Theor. Math. Phys. 2 (1998)
733 [hep-th/9806194].
[6]J. de Boer, H. Ooguri, H. Robins and J. Tannenhauser, String theory on AdS(3), JHEP 12 (1998) 026 [hep-
th/9812046].
[7]D. Kutasov and N. Seiberg, More comments on string theory on AdS(3), JHEP 04 (1999) 008 [hep-th/9903219].
[8]A. Giveon and D. Kutasov, Notes on AdS(3), Nucl. Phys. B 621 (2002) 303 [hep-th/0106004].
[9]M. Cho, S. Collier and X. Yin, Strings in Ramond-Ramond Backgrounds from the Neveu-Schwarz-Ramond
Formalism, JHEP 12 (2020) 123 [1811.00032].
[10]G. Giribet, C. Hull, M. Kleban, M. Porrati and E. Rabinovici, Superstrings on AdS$_{3}$ at $k = 1$, JHEP
08 (2018) 204 [1803.04420].
[11]N. Berkovits, C. Vafa and E. Witten, Conformal field theory of AdS background with Ramond-Ramond flux,
JHEP 03 (1999) 018 [hep-th/9902098].
[12]M.R. Gaberdiel and S. Gerigk, The massless string spectrum on AdS$_3$ x S$^3$ from the supergroup, JHEP 10
(2011) 045 [1107.2660].
[13]L. Eberhardt, M.R. Gaberdiel and R. Gopakumar, The Worldsheet Dual of the Symmetric Product CFT, JHEP 04
(2019) 103 [1812.01007].
[14]M.R. Gaberdiel and K. Naderi, The physical states of the Hybrid Formalism, JHEP 10 (2021) 168
[2106.06476].
[15]F. Larsen and E.J. Martinec, U(1) charges and moduli in the D1 - D5 system, JHEP 06 (1999) 019 [hep-
th/9905064].
[16]A. Dabholkar and A. Pakman, Exact chiral ring of AdS(3) / CFT(2), Adv. Theor. Math. Phys. 13 (2009) 409
[hep-th/0703022].
[17]J. de Boer, J. Manschot, K. Papadodimas and E. Verlinde, The Chiral ring of AdS(3)/CFT(2) and the
attractor mechanism, JHEP 03 (2009) 030 [0809.0507].
[18]O. Lunin and S.D. Mathur, Three point functions for M(N) / S(N) orbifolds with N=4 supersymmetry, Commun.
Math. Phys. 227 (2002) 385 [hep-th/0103169].
[19]A. Pakman and A. Sever, Exact N=4 correlators of AdS(3)/CFT(2), Phys. Lett. B 652 (2007) 60 [0704.3040].
[20]A. Pakman, L. Rastelli and S.S. Razamat, Extremal Correlators and Hurwitz Numbers in Symmetric Product
Orbifolds, Phys. Rev. D 80 (2009) 086009 [0905.3451].
[21]M. Baggio, J. de Boer and K. Papadodimas, A non-renormalization theorem for chiral primary 3-point
functions, JHEP 07 (2012) 137 [1203.1036].
[22]M.R. Gaberdiel and B. Nairz, BPS correlators for AdS$_{3}$/CFT$_{2}$, JHEP 09 (2022) 244 [2207.03956].
[23]E.J. Martinec, S. Massai and D. Turton, On the BPS Sector in AdS3/CFT2 Holography, Fortsch. Phys. 71
(2023) 2300015 [2211.12476].
[24]S. Iguri, N. Kovensky and J.H. Toro, Spectral flow and the exact AdS$_{3}$/CFT$_{2}$ chiral ring, JHEP 08
(2023) 034 [2304.08361].
[25]G. Giribet and C.A. Nunez, Correlators in AdS(3) string theory, JHEP 06 (2001) 010 [hep-th/0105200].
[26]J.M. Maldacena and H. Ooguri, Strings in AdS(3) and the SL(2,R) WZW model. Part 3. Correlation functions,
Phys. Rev. D 65 (2002) 106006 [hep-th/0111180].
[27]J. Troost, Winding strings and AdS(3) black holes, JHEP 09 (2002) 041 [hep-th/0206118].
[28]M.R. Gaberdiel and I. Kirsch, Worldsheet correlators in AdS(3)/CFT(2), JHEP 04 (2007) 050 [hep-
th/0703001].
[29]G. Giribet, A. Pakman and L. Rastelli, Spectral Flow in AdS(3)/CFT(2), JHEP 06 (2008) 013 [0712.3046].
[30]M. Taylor, Matching of correlators in AdS(3) / CFT(2), JHEP 06 (2008) 010 [0709.1838].
[31]C.A. Cardona and C.A. Nunez, Three-point functions in superstring theory on AdS(3) x S**3 x T**4, JHEP 06
(2009) 009 [0903.2001].
[32]C.A. Cardona and I. Kirsch, Worldsheet four-point functions in $AdS_3/CFT_2$, JHEP 01 (2011) 015
[1007.2720].
[33]A. Dei and L. Eberhardt, String correlators on AdS$_{3}$: three-point functions, JHEP 08 (2021) 025
[2105.12130].
[34]A. Dei and L. Eberhardt, String correlators on AdS$_{3}$: four-point functions, JHEP 09 (2021) 209
[2107.01481].
[35]A. Dei and L. Eberhardt, String correlators on $\text{AdS}_3$: Analytic structure and dual CFT, SciPost
Phys. 13 (2022) 053 [2203.13264].
[36]A. Dei, B. Knighton and K. Naderi, Solving AdS$_3$ string theory at minimal tension: tree-level
correlators, 2312.04622.
[37]J.M. Maldacena and H. Ooguri, Strings in AdS(3) and SL(2,R) WZW model 1.: The Spectrum, J. Math. Phys. 42
(2001) 2929 [hep-th/0001053].
[38]J. Kim and M. Porrati, On the central charge of spacetime current algebras and correlators in string
theory on AdS$_{3}$, JHEP 05 (2015) 076 [1503.07186].
[39]O. Lunin and S.D. Mathur, Correlation functions for M**N / S(N) orbifolds, Commun. Math. Phys. 219 (2001)
399 [hep-th/0006196].
[40]A. Pakman, L. Rastelli and S.S. Razamat, Diagrams for Symmetric Product Orbifolds, JHEP 10 (2009) 034
[0905.3448].
[41]A. Pakman, L. Rastelli and S.S. Razamat, A Spin Chain for the Symmetric Product CFT(2), JHEP 05 (2010) 099
[0912.0959].
[42]L. Eberhardt, M.R. Gaberdiel and R. Gopakumar, Deriving the AdS$_{3}$/CFT$_{2}$ correspondence, JHEP 02
(2020) 136 [1911.00378].
[43]R. Dijkgraaf, G.W. Moore, E.P. Verlinde and H.L. Verlinde, Elliptic genera of symmetric products and
second quantized strings, Commun. Math. Phys. 185 (1997) 197 [hep-th/9608096].
[44]P. Bantay, Symmetric products, permutation orbifolds and discrete torsion, Lett. Math. Phys. 63 (2003) 209
[hep-th/0004025].
[45]L. Eberhardt, Summing over Geometries in String Theory, JHEP 05 (2021) 233 [2102.12355].
[46]N. Seiberg and E. Witten, The D1 / D5 system and singular CFT, JHEP 04 (1999) 017 [hep-th/9903224].
[47]L. Eberhardt and M.R. Gaberdiel, Strings on $\text{AdS}_3 \times
  \text{S}^3 \times \text{S}^3 \times \text{S}^1$, JHEP 06 (2019) 035 [1904.01585].
[48]D. Kutasov, F. Larsen and R.G. Leigh, String theory in magnetic monopole backgrounds, Nucl. Phys. B 550
(1999) 183 [hep-th/9812027].
[49]E.J. Martinec and W. McElgin, String theory on AdS orbifolds, JHEP 04 (2002) 029 [hep-th/0106171].
[50]E.J. Martinec, AdS$_{3}$ orbifolds, BTZ black holes, and holography, JHEP 10 (2023) 016 [2307.02559].
[51]M.R. Gaberdiel, B. Guo and S.D. Mathur, Tensionless strings on AdS$_{3}$ orbifolds, JHEP 04 (2024) 057
[2312.01348].
[52]S. Hohenegger, C.A. Keller and I. Kirsch, Heterotic AdS(3) / CFT(2) duality with (0,4) spacetime
supersymmetry, Nucl. Phys. B 804 (2008) 193 [0804.4066].
[53]Z.K. Baykara, D. Robbins and S. Sethi, Non-supersymmetric AdS from string theory, SciPost Phys. 15 (2023)
224 [2212.02557].
[54]B. Fraiman, M. Graña, H. Parra De Freitas and S. Sethi, Non-Supersymmetric Heterotic Strings on a Circle,
2307.13745.
[55]O. Aharony, M. Berkooz, S. Kachru, N. Seiberg and E. Silverstein, Matrix description of interacting
theories in six-dimensions, Adv. Theor. Math. Phys. 1 (1998) 148 [hep-th/9707079].
[56]E. Witten, On the conformal field theory of the Higgs branch, JHEP 07 (1997) 003 [hep-th/9707093].
[57]O. Aharony and M. Berkooz, IR dynamics of D = 2, N=(4,4) gauge theories and DLCQ of ’little string
theories’, JHEP 10 (1999) 030 [hep-th/9909101].
[58]C.H. Taubes, Self-dual connections on 4-manifolds with indefinite intersection matrix, J. Diff. Geom. 19
(1984) 517.
[59]S. Gerigk, Superstring theory on AdS$_3$ x S and the PSL$(2|2)$ WZW model, Ph.D. thesis, Zurich, ETH,
2012. 10.3929/ethz-a-007595532.
[60]M.R. Gaberdiel and R. Gopakumar, Tensionless string spectra on AdS$_{3}$, JHEP 05 (2018) 085 [1803.04423].
[61]A. Dei, M.R. Gaberdiel, R. Gopakumar and B. Knighton, Free field world-sheet correlators for ${\rm
AdS}_3$, JHEP 02 (2021) 081 [2009.11306].
[62]L. Eberhardt, AdS$_{3}$/CFT$_{2}$ at higher genus, JHEP 05 (2020) 150 [2002.11729].
[63]B. Knighton, Higher genus correlators for tensionless AdS$_{3}$ strings, JHEP 04 (2021) 211 [2012.01445].
[64]B. Schoeneberg, J. Smart and E. Schwandt, Elliptic Modular Functions: An Introduction, Grundlehren der
mathematischen Wissenschaften, Springer Berlin Heidelberg (2012).
[65]R. Argurio, A. Giveon and A. Shomer, Superstrings on AdS(3) and symmetric products, JHEP 12 (2000) 003
[hep-th/0009242].
[66]L. Eberhardt and M.R. Gaberdiel, String theory on AdS$_3$ and the symmetric orbifold of Liouville theory,
Nucl. Phys. B 948 (2019) 114774 [1903.00421].
[67]A. Dei, L. Eberhardt and M.R. Gaberdiel, Three-point functions in AdS$_{3}$/CFT$_{2}$ holography, JHEP 12
(2019) 012 [1907.13144].
[68]L. Eberhardt, A perturbative CFT dual for pure NS–NS AdS$_{3}$ strings, J. Phys. A 55 (2022) 064001
[2110.07535].
[69]P.S. Aspinwall, Enhanced gauge symmetries and K3 surfaces, Phys. Lett. B 357 (1995) 329 [hep-th/9507012].
[70]L. Eberhardt, Partition functions of the tensionless string, JHEP 03 (2021) 176 [2008.07533].
[71]B. Knighton, A note on background independence in $\text{AdS}_3$ string theory, 2404.19571.
[72]B. Knighton, V. Sriprachyakul and J. Vošmera, Topological defects and tensionless holography, 2406.03467.
[73]F.M. Haehl and M. Rangamani, Permutation orbifolds and holography, JHEP 03 (2015) 163 [1412.2759].
[74]A. Belin, C.A. Keller and A. Maloney, Permutation Orbifolds in the large N Limit, 1509.01256.
[75]L. Eberhardt and S. Pal, Holographic Weyl anomaly in string theory, SciPost Phys. 16 (2024) 027
[2307.03000].
[76]M.R. Gaberdiel, R. Gopakumar, B. Knighton and P. Maity, From symmetric product CFTs to AdS$_{3}$, JHEP 05
(2021) 073 [2011.10038].
[77]S. Gukov, E. Martinec, G.W. Moore and A. Strominger, Chern-Simons gauge theory and the AdS(3) / CFT(2)
correspondence, in From Fields to Strings: Circumnavigating Theoretical Physics: A Conference in Tribute to
Ian Kogan, pp. 1606–1647, 3, 2004, DOI [hep-th/0403225].
[78]O. Aharony, A. Dymarsky and A.D. Shapere, Holographic description of Narain CFTs and their code-based
ensembles, 2310.06012.
[79]J.R. David, G. Mandal and S.R. Wadia, Microscopic formulation of black holes in string theory, Phys. Rept.
369 (2002) 549 [hep-th/0203048].
[80]N. Benjamin, C.A. Keller and I.G. Zadeh, Lifting 1/4-BPS states in AdS$_{3}$× S$^{3}$× T$^{4}$, JHEP 10
(2021) 089 [2107.00655].
[81]B. Guo, M.R.R. Hughes, S.D. Mathur and M. Mehta, Universal lifting in the D1-D5 CFT, JHEP 10 (2022) 148
[2208.07409].
[82]L. Apolo, A. Belin, S. Bintanja, A. Castro and C.A. Keller, Deforming symmetric product orbifolds: a tale
of moduli and higher spin currents, JHEP 08 (2022) 159 [2204.07590].
[83]B. Guo and S. Hampton, Bootstrapping the effect of the twist operator in the D1D5 CFT, JHEP 03 (2024) 030
[2210.07217].
[84]M.-A. Fiset, M.R. Gaberdiel, K. Naderi and V. Sriprachyakul, Perturbing the symmetric orbifold from the
worldsheet, JHEP 07 (2023) 093 [2212.12342].
[85]M.R.R. Hughes, S.D. Mathur and M. Mehta, Lifting of two-mode states in the D1-D5 CFT, JHEP 01 (2024) 183
[2309.03321].
[86]M.R.R. Hughes, S.D. Mathur and M. Mehta, Lifting of superconformal descendants in the D1-D5 CFT, JHEP 04
(2024) 129 [2311.00052].
[87]M.R. Gaberdiel, R. Gopakumar and B. Nairz, Beyond the Tensionless Limit: Integrability in the Symmetric
Orbifold, 2312.13288.
[88]S. Frolov and A. Sfondrini, Comments on Integrability in the Symmetric Orbifold, 2312.14114.
[89]C. Ferko, S. Murthy and M. Rangamani, Superstring partition functions in AdS$_3$, To appear (2024) .
[90]M.R. Gaberdiel, B. Knighton and J. Vošmera, D-branes in AdS$_{3}$ × S$^{3}$ × $\mathbb{T}$$^{4}$ at k = 1
and their holographic duals, JHEP 12 (2021) 149 [2110.05509].
[91]J.M. Maldacena, G.W. Moore and N. Seiberg, D-brane charges in five-brane backgrounds, JHEP 10 (2001) 005
[hep-th/0108152].
[92]J. Polchinski, String theory. Vol. 2: Superstring theory and beyond, Cambridge Monographs on Mathematical
Physics, Cambridge University Press (12, 2007), 10.1017/CBO9780511618123.
[93]J. Polchinski, String theory. Vol. 1: An introduction to the bosonic string, Cambridge Monographs on
Mathematical Physics, Cambridge University Press (12, 2007), 10.1017/CBO9780511816079.
[94]A. Giveon, M. Porrati and E. Rabinovici, Target space duality in string theory, Phys. Rept. 244 (1994) 77
[hep-th/9401139].
[95]R. Borsato, Lecture notes on current-current deformations, 2312.13847.
