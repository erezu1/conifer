# Outline of: The black hole/string transition in 3 and confining backgrounds

Abstract:

String stars, or Horowitz-Polchinski solutions, are Euclidean string theory saddles with a normalizable condensate of thermal winding strings. String stars were suggested as a possible description of stringy (Euclidean) black holes close to the Hagedorn temperature. In this work, we continue the study initiated in [1] by investigating the thermodynamic properties of string stars in asymptotically (thermal) anti-de Sitter backgrounds. First, we discuss the case of AdS$_{3}$ with mixed RR and NS-NS fluxes (including the pure NS-NS system) and comment on a possible BTZ/string transition unique to AdS$_{3}$. Second, we present new “winding-string gas” saddles for confining holographic backgrounds such as the Witten model and determine the subleading correction to their Hagedorn temperature. We speculate a black brane/string transition in these models and argue for a possible relation to the deconfined phase of 3+1 dimensional pure Yang-Mills.

# [root] paper
## [section-1] section: 1 Introduction
### [section-1-p1] paragraph

In string theory, black holes are solutions of the low energy effective action, usually valid only for horizon
size larger than the string scale $r_h \gg l_s$ (and small string coupling $g_s$). What is the correct
description of a black hole microstate when it is adiabatically shrunk to the string scale? The black
hole/string transition or the correspondence principle [2, 3, 4] is the idea that such stringy black holes are
indistinguishable from high energy stringy bound states. In [5] a canonical ensemble version of this idea was
explored (see also [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]). As a thermodynamic phase of quantum gravity, the
Euclidean black hole is a saddle of the string theory thermal partition on asymptotically $R^d \times S^1$.1
In terms of the temperature, this saddle is reliable for $\beta \gg l_s$. Slightly below the Hagedorn
temperature of string theory $\beta_H$, Horowitz and Polchinski found [5] a new saddle, a condensate of
strings winding around the thermal $S^1$ bound by gravitational interactions. We term such a saddle a “string
star”, imagining it describes a gravitational bound state of hot strings. The black hole and the string star
saddle are reliable at different regimes of temperatures, but a crude extrapolation to intermediate
temperatures shows a qualitative agreement of their thermodynamic properties. The black hole/string transition
can now be phrased as a precise conjecture: there exists a line of string theory backgrounds (well-defined
only for small $g_s$) connecting the Euclidean black hole to the string star, and eventually (at the Hagedorn
temperature $\beta=\beta_H$) to thermal $R^d\times S^1$. Technically, this line of saddles can be interpreted
as a line of worldsheet CFTs connecting the Euclidean black hole to $R^d\times S^1$ through winding
condensates. In [12] an argument was presented against the existence of such a line for $d>2$ type II string
theory, via a worldsheet index argument. A refined version of the conjecture thus allows for the possibility
of phase transitions along the line.

### [section-1-p2] paragraph

In [1] this discussion was extended to anti-de Sitter (AdS) spaces, by studying the properties of AdS$_{d+1}$
string stars for $d>2$. An AdS string star is a thermal winding condensate in the middle of thermal
AdS$_{d+1}$. The saddle is reliable near the AdS Hagedorn temperature $\beta_c$, $\beta-\beta_c \ll \beta_c$.
As the temperature increases the solution’s size grows, with a maximal size of $L \sim \sqrt{l_{ads} l_s}$.
Its amplitude and free energy decrease to zero at the Hagedorn temperature, where it merges with thermal
AdS$_{d+1}$. At lower temperatures, the solution size becomes small $L\sim l_s$, at which point a
correspondence principle to Euclidean AdS black holes can be drawn similar to flat space: a conjectured line
of string theory backgrounds connecting the Euclidean AdS black hole solution and thermal AdS at the Hagedorn
temperature via thermal winding-string condensate.2 Unlike flat space, string theory on AdS$_{d+1}$ also has a
holographic dual in terms of $d$-dimensional CFT. The black hole/string transition in terms of the holographic
CFT would be a conjectured line of large $N$ saddles in the thermal partition function on $S^{d-1}$,
connecting the deconfined phase to the confined phase at the Hagedorn temperature (defined by the $N=\infty$
spectrum [17, 18]) [19, 17, 20].

### [section-1-p3] paragraph

In this work, we continue our study of AdS string stars. The first extension is the study of AdS$_{3}$ string
stars ($d=2$), presented in section 2. This is an interesting test for the correspondence principle that is
inherently different from the flat space case. The reason is that both black holes and string stars do not
exist in asymptotically flat $R^2 \times S^1_\beta$. However, in AdS$_{3}$ black hole solutions do exist and
are known by the name BTZ [21]. Similarly, string star solutions don’t exist on flat $R^2\times S^1_\beta$.
But in thermal AdS$_{3}$ we find that the AdS$_{3}$ curvature stabilizes the potential for the winding
condensate. As a result, thermal AdS$_{3}$ allows for reliable string star solutions close to the Hagedorn
temperature. This is an interesting check that such a correspondence is possible for a more general setting
and may exist whenever black holes exist in a weakly coupled string theory. However, contrary to higher
dimensional small AdS black holes, a BTZ with small horizon radius $r_h \ll l_{ads}$ has very low temperature
$\beta \gg l_{ads} \gg \beta_c$. As the BTZ gets smaller, its temperature continues to decrease further away
from the Hagedorn temperature, and a simple black hole/string transition between them is impossible.

### [section-1-p4] paragraph

It is still possible to conjecture a different kind of correspondence. Below temperature $\beta_c' = 4\pi^2
l_{ads}^2/\beta_c$ the BTZ solution has a tachyonic instability from strings winding the angular circle [22,
23, 24]. This is exactly the Hagedorn instability of thermal AdS$_{3}$, after switching the two asymptotic
circles. The natural candidate for a “BTZ/string transition” in AdS$_{3}$ would be conjectured line of saddles
connecting the BTZ at $\beta_c'$ to thermal AdS$_{3}$ at $\beta_c$, with winding condensates at each end of
the line [25, 26]. See figure 1. Notice that unlike at higher dimensions, in AdS$_{3}$ there exists a large
temperature difference between the regimes of validity of the two saddles $\beta_c \ll \beta_c'$. As a result,
no qualitative match can be extrapolated between the AdS$_{3}$ string star and small BTZs as a sanity check.
We admit that the evidence for such a line is much weaker compared to higher dimensions.

### [section-1-p5] paragraph

Another interesting feature of AdS$_{3}$ string stars is the possibility in AdS$_{3}$ to turn on NS-NS flux
[27, 28, 29, 30, 31]. As the string is charged under the Kalb-Ramond field, the winding string field $\chi(x)$
is electrically charged in the effective two-dimensional description. Non-zero flux changes the solution at
leading order. We study the properties of AdS$_{3}$ string stars for mixed RR and NS-NS fluxes and for the
pure NS-NS system. Denoting the fraction of the NS-NS flux by $0\le \lambda \le 1$, the size of the RR flux is
proportional to $\sqrt{1-\lambda^2}$. In section 3.2 we study string star solutions for finite RR flux. We
find that the solutions are similar to those found in higher dimensions [1]. The NS-NS flux only contributes
to the effective mass of the winding mode (at leading order in $\alpha'$), and the size of the solution is $L
\sim \sqrt{l_s l_{ads}} \cdot (1-\lambda^2)^{-1/4}$. In section 4 we study solutions for small RR flux
$\sqrt{1-\lambda^2} \sim l_s/l_{ads}$ and for the pure NS-NS system. In this regime, the background NS-NS flux
is high enough to (almost) flatten the potential for the winding mode, similar to long strings in AdS$_{3}$
with NS-NS flux [32, 33]. As a result, the size of the solution increases to the AdS scale $L \sim l_{ads}$.
Moreover, the back-reacted NS-NS flux from the winding mode now appears at leading order, along with the
metric and the dilaton.

### [section-1-p6] paragraph

In section 3 we also discuss winding string condensates in a family of confining backgrounds which includes
the D3 and D4 Witten models [34], the Maldacena-Nuñez [35] and the Klebanov-Strassler [36] backgrounds. These
gravitational backgrounds are holographically dual to theories believed to be continuously related (at low
energies) to confining field theories on flat space $R^{p+1}$ ($p=2,3$). The thermodynamics of these models
was studied using a semiclassical bulk analysis [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]. The confined
phase has a “thermal” background dual given by analytically continuing the boundary to $R^p\times S^1_\beta$.
The deconfined phase has a black-brane dual. In this work, we find a new saddle with a thermal winding string
condensate on top of the thermal background. The solution is homogeneous parallel to the spatial boundary
directions $R^p$, and it is localized to the bulk IR region. We term this saddle a ‘winding-string gas’. As
before, it is reliable only close to the Hagedorn temperature of the holographic confining string
$\beta-\beta_c \ll \beta_c$, and it is highly subdominant. We describe the properties of the solution and find
the first correction to the Hagedorn temperature in these models due to the bulk curvature. It is possible to
conjecture a black brane/string transition for these models, connecting the black brane saddle to the winding-
string gas saddle. The phase diagram for the Witten models is similar to AdS$_{3}$, discussed above. In this
case, it is also natural to conjecture that the string winding gas is continuously related to the deconfined
phase of pure $3+1$ Yang-Mills.

### [section-1-p7] paragraph

Several future directions are possible. The AdS$_{3}$ calculation we performed was only at leading order in
the winding condensate and at leading order in $\alpha'$. The worldsheet theory in the pure NS-NS case
($\lambda=1$) is known exactly [28, 29, 48], and it is exciting to find the string star profile exactly in
$\alpha'$ [25, 26, 49]. Of course, ultimately one would like to find (for the pure NS-NS background) the
entire line of worldsheet CFTs interpolating between the thermal AdS$_{3}$ and BTZ. At the moment it sounds
improbable, as such a deformation away from $\beta - \beta_c \ll \beta_c$ will require the entire string
spectrum that couples to the winding mode, and all the orders of their interactions. Finally, the confining
backgrounds solution gives interesting predictions on its holographic dual. It would be interesting to compare
these predictions to the weakly coupled regime.

## [sec-gen_prop_ads3] section: 2 General properties of the AdS$_{3}$ string star
### [sec-eft] section: 2.1 Winding-string condensates in type II string theory
#### [sec-eft-p1] paragraph

In this section, we will describe the low energy effective field theory (EFT) for type II string theory
Euclidean saddles with a perturbative (normalizable) winding-string condensate. This is an extension of the
EFT for the winding mode together with the metric around flat space [16, 5, 12] to more general cases that
include curved metric and (possibly) background fluxes such as the Kalb-Ramond flux $H_3 \ne 0$.

#### [sec-eft-p2] paragraph

By “perturbative saddle” we mean that we start with a type II “background saddle” without a winding-string
condensate, and will consider a small deformation of it that will include such a condensate. We will assume
the undeformed metric is of the form $M_{D}\times X_{10-D}$, with $X_{10-D}$ being a $10-D$ dimensional
compact space. We denote by $t\sim t+\beta$ the compact ’temporal’ direction in $M_{D}$ on which we will
reduce the theory, and the rest of the directions by $x^i$, $i=1,...,d=D-1$. We will assume the undeformed
metric on $M_{D}$ has the form

\[ G = g_{tt}(x) dt^2 + g_{ij}(x) dx^i dx^j. \]

(2.1)

Besides the metric, the background saddle can also include non-zero NS-NS and RR gauge fields. All the
background fields are assumed to be in a gauge where they are independent of $t$, making $t$ translations a
symmetry. We set the units such that the curvature scale of the background fields is set to one $l_{curv}=1$,
while keeping the $\alpha'$ explicit, and assume the background is weakly-curved $\alpha' \ll 1$.

#### [sec-eft-p3] paragraph

Following [16] we would like to consistently add an action for $\chi$, the string mode that winds once around
the temporal circle $t$. We take $\chi(x)$ to be homogeneous on the compact $X_{10-D}$ directions and to
depend only on $x$. Denoting the size of the normalizable $\chi(x)$ profile $L$, we will assume that it is
much larger than the string scale $L \gg l_s$. Assuming the entire deformation from the saddle has $L \gg
l_s$, higher order terms in the $\alpha'$ expansion of the action will be suppressed by derivatives. At
leading order in $\alpha'$ the total action is

\[ I = I_\text{SUGRA} + I_\chi. \]

(2.2)

The type II supergravity (SUGRA) action (at leading order in $\alpha'$) is [50]

\[ I_\text{SUGRA} = \frac{1}{16\pi G_N^{(10)}} \int d^{10} x \sqrt{G} \left[ e^{-2\Phi} \left(-R - 4\partial_\mu\Phi \partial^\mu \Phi + \frac{1}{2} |H_3|^2\right) + \frac{1}{2} |F_p|^2 \right], \]

(2.3)

with $H_3 = d B_2$, $F_{p+1} = d C_p$ and $|F_p|^2 = \frac{1}{p!} F_{\mu_1 ... \mu_p} F^{\mu_1 ... \mu_p}$.
$G_N^{(10)}$ is the $10$-dimensional gravitational constant. The last term stands for the possible RR $F_p$
fluxes, and we omitted the possible Chern-Simons terms for brevity.

#### [sec-eft-p4] paragraph

Considering the action for the winding mode, the new ingredient compared to [1] is that here we need to
describe the coupling of the winding mode to the Kalb-Ramond field. The leading interaction comes from the
electric coupling of the fundamental string to the Kalb-Ramond field along the $t$ direction. It is convenient
to define the 1-form gauge field

\[ A_i = B_{t\  i}, \text{ and } F=dA. \]

(2.4)

In these conventions for $A_i$, $\chi$ is electrically charged under the $U(1)$ winding with charge
$g=\frac{\beta}{2\pi \alpha'}$.3 Up to $O(\alpha')$ terms, the $\chi$ $d$-dimensional action takes the form

\[ \begin{split}
        I_\chi &= \frac{\beta}{16\pi G_N} \int d^d x \ \text{vol} \  e^{-2\Phi}
        \Bigg(
        |D\chi|^2 \\
        & + m^2\left(R(x)\right)|\chi|^2 + O(\alpha'^{-1}|\chi|^4)\\
        &
        + \left(g_1 \mathcal{R}_D[g]  + g_2 \frac{g^{tt}}{2} F_{ij} F^{ij} +
\frac{g_3}{12}H_{ijk}H^{ijk}\right)|\chi|^2\Bigg) ,
\end{split} \]

(2.6)

with $R(x) \equiv \frac{\beta}{2\pi} \sqrt{g_{tt}}$, $D_j = \partial_j - i g A_j$, and $g_1$, $g_2$, $g_3$ are
some unknown $O(1)$ couplings. $G_N$ and

\[ \text{vol}=\sqrt{g}\sqrt{g_{tt}}, \]

(2.7)

are the $D$-dimensional gravitational constant and volume respectively. For type II string theory the winding
mode mass and the flat space Hagedorn temperature $R_H=\frac{1}{2\pi}\beta_H$ are

\[ \begin{split}
        m^2(R) = \frac{R^2-R^2_H}{\alpha'^2},\qquad &R_H^2/\alpha' = 2.
\end{split} \]

(2.8)

In these notations, we also define the effective mass for the winding mode as

\[ m^2_\text{eff}(x) = m^2(R(x)) + g^2 A_i A^i. \]

(2.9)

#### [sec-eft-p5] paragraph

In (2.2) we added the first winding mode and the supergravity fields but neglected the rest of the higher
winding modes and the rest of the massive string spectrum. This is consistent only when the mass of the
winding mode is parametrically below the string scale $\alpha' m^2_\text{eff} \ll 1$ at the support of $\chi$.
In practice, we need to tune the temperature of the background to be close to the Hagedorn temperature $R-R_H
\ll R_H$. The second line of (2.6) includes all the $\alpha'^{-1}$ terms. After fine-tuning the quadratic mass
term to be small, we still have higher order interaction terms starting at $\alpha'^{-1}|\chi|^4$. We will
neglect these terms below by our assumption that the deformation is perturbative and the profile of the
winding mode is parametrically small $|\chi|\ll 1$.

#### [sec-eft-p6] paragraph

In the third line of (2.6) we listed the first $\alpha'^0$ terms in the action. These terms correct the mass
term by a curvature scale (which also controls the Kalb-Ramond flux) amount $\Delta m^2 \sim O(1)$.4 These
terms are naively leading whenever the size of the winding mode profile is comparable to the curvature scale.
Indeed some of the solutions we will find below will satisfy this condition. Nevertheless, we will argue that
these terms are negligible for these cases.

#### [sec-eft-p7] paragraph

Imagining a general deformation of the supergravity fields, what are the leading interaction terms? Expanding
the total action around the background, the quadratic order (as in any Euclidean theory) is trivial. The
leading $\alpha'^{-1}$ cubic interaction comes by expanding the kinetic term for $\chi$ to linear order around
the background. Parametrizing the deformation of the $tt$ component of the metric by $G_{tt} = g_{tt} e^{2
\varphi(x)}$, there is a universal cubic interaction by expanding the mass term

\[ m^2(x) |\chi|^2 = m^2(R(x)) |\chi|^2 + \frac{2R(x)^2}{\alpha'^2} \varphi |\chi|^2 + O(\varphi^2 |\chi|^2), \]

(2.10)

where on the RHS $R(x)$ is of the (undeformed) background metric. Close to the Hagedorn temperature $R \sim
l_s$ the interaction term is of leading $\alpha'^{-1}$ order. Whenever the background solution has a non-
trivial Kalb-Ramond flux around the temporal circle $F_{ij} \ne 0$ there is also a leading cubic term from the
$A_i A^i |\chi|^2$ term, of the schematic form $\frac{1}{\alpha'}\delta A_i |\chi|^2$ (we will deal with this
term in the next section). However, the dilaton $\Phi$ cubic coupling to $\chi$ is of higher $\alpha'$ order
due to our assumption $L \gg l_s$ and is negligible.5 Considering a general deformation of the supergravity
fields, the leading cubic interactions of $I_\text{SUGRA}$ are all with $O(1)$ (the curvature scale) couplings
and can be neglected as well. Only the quadratic interactions in $I_\text{SUGRA}$ around the saddle are
leading.

#### [sec-eft-p8] paragraph

It is, therefore, crucial to find out which fields couple to $\varphi$ (and $\delta A_i$) at quadratic order
in $I_\text{SUGRA}$. The Einstein-Hilbert term by itself gives only a kinetic term for $\varphi$, but the
linear term does give a quadratic coupling to the dilaton. To see this we proceed as follows. The overall
volume in (2.3) is $\sqrt{G} \exp(\varphi-2\Phi)$. It is therefore useful to redefine the dilaton as

\[ \phi = \Phi-\frac{1}{2}\varphi. \]

(2.11)

In this form, the quadratic order of the metric + dilaton action is given by

\[ \begin{split}
        \frac{1}{16\pi G_N^{(10)}} &\int d^{10} x \sqrt{G} e^{-2\Phi} \left[-R-4\partial_\mu \Phi \partial^\mu
\Phi \right] \\
        &=\frac{\beta}{16\pi G_N} \int d^{d} x \text{vol} \left[ \partial_i \varphi \partial^i \varphi
        - 4\partial_i \phi \partial^i \phi
        -2\phi \frac{\partial_i g_{tt} \partial^i \varphi}{g_{tt}} + (...)\right].
\end{split} \]

(2.12)

On the RHS we integrated over the other $10-d$ directions (including $t$) and kept only quadratic terms in
$\varphi, \phi$. The last term gives a leading quadratic $\phi \partial \varphi$ interaction, that generically
appears whenever $g_{tt}$ is not flat.6 The dilaton however is expected to couple quadratically in a similar
way to any supergravity field with a non-trivial profile along the $x^i$ directions. To find a saddle with a
winding condensate, it is necessary to consider a general deformation of the metric and the dilaton (and other
fields present in the background).

#### [sec-eft-p9] paragraph

In many cases, however, there is a significant simplification that can be considered assuming the solution’s
length scale is also much smaller than the curvature scale $L \ll 1$. For those cases, we can further expand
in orders of $L$ and neglect lower derivatives or higher powers of $x$. Looking back at (2.12), the kinetic
terms are of order $L^{-2}$ while the interaction term is of $L^{-1}$ subleading order. In fact, in the gauge
we will choose $A_i \sim O(L)$, and it is possible to show that the $\delta B |\chi|^2$ is also subleading (we
will explain it for the AdS$_{3}$ case below). As a result, at leading order in $L$ the dilaton $\phi$ and the
Kalb-Ramond field decouple, and we can consistently consider a perturbative deformation of the winding mode
$\chi$ and the temporal metric $\varphi$ alone. The effective action in this limit will be reviewed in section
3.1. Whenever the size of the profile reaches the curvature scale $L\sim 1$, this approximation breaks. For
those cases a general supergravity deformation is necessary. We will describe such a case in section 4 below.

### [sec-eom] section: 2.2 The mixed AdS$_{3}$ background
#### [sec-eom-p1] paragraph

In this section, we begin the discussion of the AdS$_{3}$ string star. We work in units of $l_{ads}=1$. The
set of backgrounds we will consider are Euclidean 10d solutions of type IIB string theory with both NS-NS and
RR fluxes, and the geometry of (thermal) $AdS_3\times S^3\times M_4$, where $M_4$ can be a four torus $T^4$ or
a $K3$ manifold [27, 30, 31]. The thermal AdS$_{3}$ component is given by the following background

\[ \begin{split}
        ds^2 &= d\rho^2 + \sinh^2\rho \  d\phi^2 + \cosh^2\rho \ dt^2,\\
        B_2 &= i \lambda \sinh^2\rho \  d\phi \wedge dt,\\
        C_2 &= i \sqrt{1-\lambda^2} \sinh^2\rho \  d\phi \wedge dt,
\end{split} \]

(2.13)

with $t\sim t+\beta$ and $0\le \lambda\le 1$.7 The gauge fields $B,C$ also have fluxes from the $S^3$
component, which we omitted. $\lambda = 0$ is the pure RR solution, for which string stars solutions were
studied in [1], and $\lambda=1$ is the pure NS-NS solution. We note that the latter can be studied not only
for type IIB but in any closed string theory, and it is also known exactly in $\alpha'$ via an
$\text{SL}(2,R)$ WZW worldsheet description [28, 29, 48]. As in [1] $\beta$ is also the holographic
temperature in the dual CFT on $S^1_{2\pi}\times S^1_\beta$.

#### [sec-eom-p2] paragraph

In these conventions the background gauge field (2.4) is $A_\phi = i \lambda \sinh^2\rho$ and $R(\rho) = R_0
\cosh(\rho)$, with $R_0 = \frac{\beta}{2\pi}$. The (background) effective mass (2.9) is given by

\[ m^2_\text{eff}(\rho) = \frac{1}{\alpha'^2} \left(R_0^2 \left(\cosh^2\rho - \lambda^2 \sinh^2\rho \right) -R_H^2\right). \]

(2.14)

For self consistency we assumed scale separation $\alpha' m^2_\text{eff}(\rho) \ll 1$, which in this case
gives $R_0-R_H \ll R_H$ for $\rho \sim O(1)$. The EFT is therefore applicable only for temperatures close to
the Hagedorn temperature.

#### [sec-eom-p3] paragraph

Following the previous section, to write the two-dimensional EFT we need to expand $I_\text{SUGRA}$ to
quadratic order around a general supergravity deformation. Assuming the spherical symmetry of the solution, we
are instructed to consider a deformation for every field with a nontrivial background profile along the $\rho$
direction. A general spherically symmetric deformation of the AdS$_{3}$ components of (2.13) has the form8

\[ \begin{split}
        \Phi &= \phi + \frac{1}{2} (\varphi + \psi),\\
        G &= d\rho^2+e^{2\varphi} \cosh^2\rho \ dt^2 + e^{2 \psi} \sinh^2\rho \  d\phi^2,\\
        B_2 &= i \lambda e^{\zeta} \sinh^2\rho \  dt \wedge d\phi,\\
        C_2 &= i \sqrt{1-\lambda^2} e^{\eta} \sinh^2\rho \  dt \wedge d\phi,
\end{split} \]

(2.15)

with $\phi, \varphi, \zeta$ and $\eta$ all function of $\rho$. In particular, we don’t need to consider
deformations of other RR fluxes. Similar to (2.11), we redefined $\Phi$ in such a way to satisfy

\[ \sqrt{G} e^{-2\Phi} = \text{vol} \  e^{-2\phi}, \]

(2.16)

with $\text{vol}=\cosh \rho \ \sinh \rho$ the volume form of the background metric.

#### [sec-eom-p4] paragraph

Following the discussion in the previous section, we assume small back-reaction
$|\phi|,|\varphi|,|\psi|,|\zeta|, |\eta|\ll 1$ and consider only its leading coupling to $\chi$. Expanding the
winding mode action (2.6) to ($\alpha'^{-1}$) cubic order, and integrating over the angular direction, gives

\[ \begin{split}
        I_\chi &= \frac{2\pi \beta}{16\pi G_N}\int d\rho \ \text{vol} \left[
                |\chi'|^2+m^2_\text{eff}(\rho) |\chi|^2 + \frac{2 R_0^2}{\alpha'^2} \left(
                \cosh^2\rho \  \varphi -\sinh^2\rho \  (\zeta-\psi)\right) |\chi|^2
        \right],
\end{split} \]

(2.17)

with $G_N$ being the 3-dimensional gravitational constant, and the effective mass (2.14). Here and below,
primes are derivatives with respect to $\rho$. In particular, we find both $\varphi |\chi|^2$ and
$(\zeta-\psi) |\chi|^2$ terms of the same leading $\alpha'^{-1}$ order. Substituting the deformation (2.15) in
the SUGRA action (2.3) gives to quadratic order

\[ \begin{split}
        I_\text{SUGRA}^{(2)} &= \frac{2\pi \beta}{16\pi G_N^{(3)}} \int d\rho \ \text{vol} \  \Bigg[
        -4 (\phi')^2 +(\varphi')^2 +(\psi')^2 \\
        &-\lambda^2\left(\frac{1}{2}\tanh^2\rho \ (\zeta')^2+4(\psi+\varphi-\zeta)^2-4\tanh\rho \
\zeta'(\psi+\varphi-\zeta)\right)\\
        &-(1-\lambda^2)\left(\frac{1}{2}\tanh^2\rho \ (\eta')^2
        + 4\eta^2-4\eta (\varphi+\psi)-2\tanh\rho \ \eta'(\psi+\varphi-2\eta)
        \right)\\
        &-4\phi\left(\tanh\rho \ \varphi'+\coth\rho \ \psi'
        +\lambda^2 (2\varphi+2\psi-2\zeta-\tanh\rho \ \zeta')
        \right)
        \Bigg].
\end{split} \]

(2.18)

To avoid a curvature singularity at $\rho=0$ we need to maintain $\psi(0)=0$. Regularity of the fields at
$\rho=0$ also sets $\chi'(0)=\phi'(0)=\varphi'(0)=\psi'(0)=\zeta'(0)=\eta'(0)=0$. At $\rho=\infty$ all the
fields should vanish for normalizability.

### [sec-thermo] section: 2.3 Thermodynamics and the BTZ/string transition
#### [sec-thermo-p1] paragraph

The total EFT action compared to that of thermal AdS$_{3}$ is the sum of (2.17) and (2.18)

\[ I_\text{String star} -I_{\text{TAdS}_3} = I^{(2)}_\text{SUGRA}+I_\chi. \]

(2.19)

The AdS$_{3}$ string star is the bound state saddle of (2.19). Being a solution of the action, it is a
Euclidean saddle of the (Euclidean) string theory partition function with asymptotic thermal AdS$_{3}$
boundary condition. As a Euclidean saddle, it has free energy of order $G_N^{-1}$, just like black holes. It
is applicable only near the Hagedorn temperature $R_0-R_H \ll R_H$.

#### [sec-thermo-p2] paragraph

In $d=2$ the AdS black hole solution is known by the BTZ solution [21]. It’s on-shell action, compared to the
thermal AdS$_{3}$, is (in units $l_{ads}=1$)

\[ I_\text{BTZ} -I_{\text{TAdS}_3} = -\frac{\pi}{4 G_N} \left(R_0^{-1}-R_0\right). \]

(2.20)

Thus, thermal AdS$_{3}$ is canonically dominant for low temperatures $R_0 > 1$, while the BTZ is dominant for
high temperatures $R_0 < 1$. Whenever the string star saddle is reliable $R \sim R_H \ll 1$ the dominant
saddle is the BTZ. The string star saddle is therefore non-perturbatively unstable, and exponentially
subdominant canonically. As we will see numerically in figure 7 below (and also in [1]) the string star free
energy (2.19) is positive (note that the expression is not clearly positive due to the $\zeta, \eta$ kinetic
terms (2.18)). Therefore it is subdominant also compared to the thermal AdS$_{3}$ solution.

#### [sec-thermo-p3] paragraph

For higher dimensional AdS$_{d+1}$ $d>2$ an AdS black hole/string transition was suggested between the AdS
string star saddle and AdS black holes [1]. The argument was carried from the black hole/string transition
previously suggested between the flat-space string star saddle (or the Horowitz-Polchinski solution) and the
(Euclidean) Schwarzschild saddle [5, 12]. The reason is that at the two ends of the correspondence point
around $R_0 \sim l_s$, both the AdS black hole and the AdS string star are of size much smaller than the AdS
scale and can be well approximated by their asymptotically flat counterparts.

#### [fig-ads3_phase_diagram] figure: Figure 1

Figure 1. A conjectured phase diagram for AdS$_{3}$ (for $l_{ads} \gg l_s$). The Euclidean action as a
function of the inverse temperature $R_0$ is sketched. The gray and black lines describe the thermal AdS$_{3}$
and the BTZ respectively. The string star saddle is the blue line close to the Hagedorn temperature $R_c$. Its
dual, a BTZ winding condensate, is the blue line connected to the BTZ saddle at $R_c'$. A BTZ/string
transition in AdS$_{3}$ would be a hypothetical line of saddles connecting the two (dashed blue line). We note
that the sketch should be understood in the limit $g_s \rightarrow 0$. At finite but small $g_s$ the string
star saddle can’t be trusted arbitrarily close to $R_c$ whenever the 1-loop effect is leading.

#### [sec-thermo-p4] paragraph

In $d=2$ however asymptotically flat Schwarzschild solutions simply don’t exist, so a similar argument can’t
be drawn. Going back to AdS$_{d+1}$, AdS black holes exist only for $R_0 < l_{ads}/\sqrt{d(d-2)}$. For small
enough horizon radius $r_h / l_{ads} < \sqrt{\frac{d-2}{d}}$ the temperature grows as the radius shrinks, just
like in flat space. This is not the case for $d=2$. The temperature of the BTZ solution always grows with the
radius $R_0 = 1 / r_h$. As a result, any attempt to connect the AdS$_{3}$ string star to a small black hole
close to the Hagedorn temperature is impossible, because at high temperatures only large black hole solutions
exist. A clue comes when we consider the asymptotic symmetries of the question. Any worldsheet with asymptotic
$S^1_\phi \times S^1_\beta$ has two $U(1)$ windings. The thermal AdS$_{3}$ saddle breaks the $S^1_\phi$
winding spontaneously, while the BTZ saddle breaks the $S^1_\beta$ winding. The AdS$_{3}$ string star saddle
on the other hand (spontaneously) breaks both winding symmetries. To connect the AdS$_{3}$ string star saddle
to the BTZ we need to consider deformations of the BTZ by $S^1_\phi$ winding strings.

#### [sec-thermo-p5] paragraph

Denoting the AdS$_{3}$ Hagedorn temperature by $R_c$, the BTZ solution has a known instability at $R_c' =
1/R_c$ [22, 23, 24]. This instability is exactly the tachyon instability of the thermal AdS$_{3}$ at the AdS
Hagedorn temperature after we switch the roles of the two asymptotic circles ($R_0 \mapsto 1/R_0$). In other
words, below $R_0>R_c'$ strings winding around the $\phi$-circle are tachyonic. Considering the AdS$_{3}$
string star saddle after switching the circles we get a new saddle that describes a normalizable
$\phi$-winding condensate in the BTZ background. This saddle also breaks both winding symmetries
spontaneously, but it is connected (in its regime of validity $R_c'-R_0 \ll R_c'$) to the BTZ instead of the
thermal AdS$_{3}$. In terms of global symmetries pattern, it is therefore natural to speculate these two
branches meet around $R_0 \sim 1$.9 This phase diagram for AdS$_{3}$ was also suggested in [26]. A schematic
plot of this suggested picture is drawn in figure 1.

## [sec-sub_ads] section: 3 Sub-AdS solutions and confining strings
### [sec-gen_disc] section: 3.1 General discussion
#### [sec-gen_disc-p1] paragraph

This section studies general properties of holographic thermal confining theories, in cases where the “IR
wall” is geometrically realized by a contractible (non-thermal) cycle. Thermal $AdS_{d+1}$ is one such example
[1], in which an $S^{d-1}$ closes in the IR region. We start by showing that around such a background there
exists a saddle of thermal winding string condensate that depends (to leading order) only on the curvature
scale at the IR point at which the cycle closes. The reason would be that for this background, the size of the
solution would be much smaller than the characteristic curvature scale. In terms of AdS$_{d+1}$ these
solutions satisfy $L \ll l_{ads}$ and were reviewed in [1]. The analysis allows us to find the characteristic
behavior of the solution and the leading correction to the Hagedorn temperature in the dual holographic
theory.

#### [sec-gen_disc-p2] paragraph

The topology of the geometries we will study is $S^1_\beta \times \mathbb{R}^{d} \times \mathcal{M}$.
$S^1_\beta$ asymptotes to the thermal cycle of the holographic theory, $\mathbb{R}^{d}$ is made of a radial
direction $r$ and a shrinking $S^{d-1}$, and $\mathcal{M}$ is some (perhaps non-compact) manifold. We further
assume the solution preserves $SO(2) \times SO(d)$ symmetry. The string metric close to the shrinking point
$r=0$ of the $S^{d-1}$ sphere is, to subleading order in $r^2$,

\[ ds^2 = dr^2 + \left( 1 + \frac{r^2}{l^2}\right) dt^2 + r^2 d\Omega^2_{d-1} + ds^2_{\mathcal{M}} \]

(3.1)

The Euclidean time direction satisfies $t \sim t +2\pi R_0$. Higher orders of the metric are assumed to be
down by higher orders of $r^2/l^2$ with $l$ being the curvature scale of the (IR) geometry. As a result, we
implicitly assume $r \ll l$ and $l_s \ll l$. On general grounds the parameter $R_0$ is related linearly to the
holographic theory temperature $\beta$. We also assume that for $r \ll l$ the internal space geometry
$ds^2_\mathcal{M}$ is independent of $r$. In this geometry, and for temperatures close to the Hagedorn
temperature, we look for non-trivial winding solutions that are homogeneous both on $\mathcal{M}$ and on the
closing $S^{d-1}$ sphere. In cases that $\mathcal{M}$ is non-compact these solutions are dual (in the
holographic theory) to a gas of interacting (confining) strings, and so we term them “winding-string gas”
solutions.

#### [sec-gen_disc-p3] paragraph

In section 2.1 we explained that whenever the winding mode profile size is parametrically smaller than the
curvature scale $L \ll l$ we can expand the EFT in orders of $L/l$ and consider only the winding mode $\chi$
and the temporal metric deformation $\varphi$. In practice, we take only the highest number of derivatives
(within the $O(\alpha')$ action) and fewer powers of $r$. Assuming both $\chi(r),\varphi(r)$ depend only on
$r$, the leading $O(l^2/L^2)$ terms in (2.2) are

\[ I_{L \ll l} = \frac{\beta V_{d-1}}{16\pi G_N} \int r^{d-1} dr \left[(\varphi')^2 + |\chi'|^2 + m^2_\text{eff}(r) |\chi|^2 + \frac{2R_0^2}{\alpha'^2} \varphi |\chi|^2 \right], \]

(3.2)

with $V_{d-1}$ the volume of a unit $S^{d-1}$ sphere. At leading order for small $r$ it is enough to expand
the effective mass to quadratic order in $r$. Assuming no Kalb-Ramond flux in the $t$ direction the effective
mass (2.9) is

\[ m^2_\text{eff} (r) = \frac{1}{\alpha'^2}\left(R_0^2 - R_H^2 + \frac{R_0^2 r^2}{l^2} \right). \]

(3.3)

Notice that the only $l$ dependence in the action (3.2) is through (3.3). Whenever a (non-singular) Kalb-
Ramond flux exists it only corrects the $r^2$ term and can be swallowed into a redefinition of $l$. Naively
the second term is subleading for $L\ll l$, but for temperatures close enough to the Hagedorn temperature
$(R_0^2-R_H^2)/R_0^2 \sim L^2/l^2$ it is of the same order and should be added (while higher orders in $r$ are
still subleading). The resulting equations for $\chi(r), \varphi(r)$ are

\[ \begin{split}
        \chi ''+ \frac{d-1}{r} \, \chi ' - \left(m^2_\text{eff}(r)+ \frac{4}{\alpha'} \varphi \right) \chi & =
0, \\
        \varphi ''+ \frac{d-1}{r} \, \varphi ' - \frac{2}{\alpha'} |\chi|^2 & = 0.
\end{split} \]

(3.4)

These equations are of the same form found in the near-Hagedorn limit at [1].

#### [sec-gen_disc-p4] paragraph

The winding EFT regime of validity for the winding EFT is $(R_0^2-R_H^2)/R_H^2 \ll 1$. In this section, we
further restrict ourselves to $(R_0^2-R_H^2)/R_H^2 \sim l_s/l$. We will denote this regime of temperatures as
“near-Hagedorn” and parameterize it explicitly by defining

\[ R_0^2 \equiv R_H^2 + \delta \cdot \frac{l_s^{3}}{l}. \]

(3.5)

We can further reparameterize

\[ \chi(r) = \frac{l_s}{l} \cdot \hat \chi(r/L), \quad \varphi(r) = \frac{l_s}{l} \cdot \ \hat \varphi(r/L), \]

(3.6)

with $L^2\equiv l_s l$, to get ($x=r/L$)

\[ \begin{split}
        \hat \chi ''+ \frac{d-1}{x} \, \hat \chi ' - \left(\delta + 2 x^2 + 4 \hat \varphi \right) \hat \chi &
= 0, \\
        \hat \varphi ''+ \frac{d-1}{x} \, \hat \varphi ' - 2 |\hat \chi|^2 & = 0,
\end{split} \]

(3.7)

with $'$ denote an $x$ derivative. These equations were studied numerically in [1]. Because (3.7) is
dimensionless we find $|\chi|,|\varphi| \sim l_s/l$ and solution’s size $L \sim \sqrt{l_s l}$. Because (for
the original metric to be weakly curved) $l_s/l \ll 1$ the solutions for (3.7) are all self-consistent.
Specifically note that $l_s \ll L\ll l$, justifying the approximation (3.2). Numerically it was found that the
solution’s size increases with the temperature [1].

#### [sec-gen_disc-p5] paragraph

The Hagedorn temperature of the theory is defined as the temperature where the linearized equations have a
normalizable solution, giving rise to a normalizable zero mode in the partition function. At the order we work
with, this is given by $\delta_c = -\sqrt{2} d$, and the corresponding normalizable mode is $\chi(r) =
\exp(-r^2/(\sqrt{2} L^2))$. In other words, the leading curvature correction to the Hagedorn value for $R_0$
is

\[ R_c^2  = 2 \alpha' \left(1 - \frac{d}{\sqrt{2}} \frac{l_s}{l} + O(l_s^2/l^2)\right). \]

(3.8)

#### [sec-gen_disc-p6] paragraph

However, $R_0$ is not directly related to the holographic theory temperature $\beta$. In the examples below
the geometry is given by an analytic continuation from a Lorentzian manifold with a boundary of $R^{p,1}$ for
some $p$. The Lorentzian solutions take the general form

\[ ds^2 =  dr^2 + f(r)\left( -(dx^0)^2 + \sum_{i=1}^p (dx^i)^2\right) + (...), \]

(3.9)

where $r$ is again the radial bulk direction, $x^0,...,x^p$ are parallel to the boundary $R^{p,1}$, and in the
bracket we ignored the rest of the coordinates. The Euclidean solution is then taken by analytically
continuing $x_0 = i t$, with the same $t \sim t+\beta$ as in (3.1). Comparing to (3.1) gives $f(r=0) = 4\pi^2
R_0^2 / \beta^2$ at $r=0$. The confining string tension $T_{st}$ is given by calculating the bulk worldsheet
action in the $t, x^i$ IR plane ($r=0$) measured in units of the holographic boundary lengths given by
$\beta$:

\[ T_{st} = \frac{1}{2\pi \alpha'}\sqrt{g_{tt} g_{xx}}\mid_{r=0} = \frac{f(0)}{2\pi \alpha'}=\frac{2\pi R_0^2}{\alpha' \beta^2}. \]

(3.10)

Together with (3.8), the leading curvature correction to the holographic Hagedorn temperature is

\[ \beta_c = \sqrt{\frac{4\pi}{T_{st}}} \left(1-\frac{d}{2\sqrt{2}} \frac{l_s}{l} + O(l_s^2/l^2) \right). \]

(3.11)

### [sec-finite_RR] section: 3.2 AdS$_{3}$ with finite RR flux
#### [sec-finite_RR-p1] paragraph

We now go back to study the AdS$_{3}$ string star solutions in the background (2.13). Following the previous
section we will when small solutions $L \ll l_{ads}$ exist. Assuming $\rho \ll l_{ads}$ we can directly expand
(2.18) and (2.17) to $L^{-2}$ order and see that all the fields besides $\varphi$ decouple, leaving us with
(3.2) (at $d=2$). In particular, notice that while both $\varphi$ and $\zeta$ couple to $\chi$ at the same
$\alpha'^{-1}$ order (2.17), the $\zeta$ coupling is smaller by a factor of $\rho^2/l_{ads}^2 \ll 1$.
Expanding the effective mass (2.14) to leading order gives (bringing back the $l_{ads}$ units)10

\[ m^2_\text{eff}(\rho) = \frac{1}{\alpha'^2}\left(R_0^2 + \frac{(1-\lambda^2) R_0^2}{l_{ads}^2}\rho^2 - R_H^2\right). \]

(3.12)

This is the same form as in (3.3) only with the effective scale $l = l_{ads}/\sqrt{1-\lambda^2}$. We can
follow the same steps as in the previous section and assume a small solution $l_s \ll L \ll l$. We also note
that as the winding mass of order $m^2 \sim l_{ads}/l_s^3$, we can consistently neglect higher-curvature
contributions to the mass which are of subleading order $\Delta m \sim l_{ads}^{-2}$.

#### [sec-finite_RR-p2] paragraph

Following the previous section, for near-Hagedorn temperatures $(R_0^2-R_H^2)/R_H^2 \sim l_s/l_{ads}$ the
AdS$_{3}$ string star solution has an amplitude of

\[ |\chi|,|\varphi| \sim \frac{l_s}{l_{ads}} \sqrt{1-\lambda^2}, \]

(3.13)

and a characteristic size

\[ L \sim \sqrt{l_s l_{ads}} (1-\lambda^2)^{-1/4}. \]

(3.14)

In this geometry $\beta = 2\pi R_0$ and therefore, following (3.11), the leading correction to the AdS$_{3}$
Hagedorn temperature is

\[ R_c^2 = 2 \alpha' - 2^{3/2} \sqrt{1-\lambda^2} \frac{l_s^3}{l_{ads}} + O(\alpha'^2/l_{ads}^2). \]

(3.15)

In [1] the leading correction for the Hagedorn temperature in $AdS_5\times S^5$ was matched with an
integrability analysis of $\mathcal{N}=4$ SYM [18]. It would be interesting to find a way to similarly compare
(3.15) to the recent integrability results for the pure RR AdS$_{3}$ case ($\lambda=0$) [51, 52, 53, 54].

#### [sec-finite_RR-p3] paragraph

The thermodynamic stability of these solutions was studied in [1]. $\zeta$ is negligible in (7) and the string
star free energy can be shown to be positive. This saddle is therefore non-perturbatively unstable compared to
the thermal AdS$_{3}$ saddle (and to the BTZ saddle).

#### [sec-finite_RR-p4] paragraph

This discussion is self-consistent only when the size of the solution is smaller than the AdS curvature scale,
$L \ll l_{ads}$, or $1-\lambda^2 \gg \alpha'/l_{ads}^2$. Note that $\sqrt{1-\lambda^2}$ is the magnitude of
the RR flux $F_3$ (2.13). We, therefore, conclude that for near-Hagedorn temperatures $(R_0^2-R_H^2)/R_H^2
\sim l_s/l_{ads}$ and large enough RR-flux $1-\lambda^2 \gg \alpha'/l_{ads}^2$ the leading behavior of the
mass around $\rho=0$ solely controls the profile of the string star. As we lower the RR flux the profile size
is larger and the amplitude is smaller. Around $1-\lambda^2 \sim \alpha'/l_{ads}^2$ the solution size reaches
the AdS scale and the approximation we took breaks. We will discuss this case in section 4 below.

#### [sec-finite_RR-p5] paragraph

For lower temperatures, the solution size turns shorter. Below the near-Hagedorn regime, but for temperatures
in which the EFT is still valid $l_s/l_{ads} \ll (R_0^2 - R_H^2)/R_H^2 \ll 1$ one might expect reliable
solutions that are arbitrarily short (although with $L \gg l_s$). This is not the case and for a good reason.
If arbitrarily small solutions would exist, they would approximately solve the flat space equations for $d=2$,
and it is known that no such solutions exist [5, 12]. Instead, whenever the solution is reliable
($|\chi|,|\varphi|\ll 1$) its size remains comparable to $L \sim \sqrt{l_s l_{ads}}$. In other words, this
section describes the behavior of AdS$_{3}$ string stars whenever they exist for finite RR flux $1-\lambda^2
\gg \alpha'/l_{ads}^2$.

### [sec-d4_back] section: 3.3 The D4 Witten model
#### [sec-d4_back-p1] paragraph

Consider $4+1$ dimensional maximally symmetric $SU(N)$ Yang-Mills theory (with coupling $g_5$) compactified on
a circle of radius $R$ with anti-periodic boundary condition for the fermions. We denote the $4+1$ ’t Hooft
coupling by $\lambda_5 = g_5^2 N$. It is holographically dual to the near horizon limit of $N$ D4 branes [55],
with the $9+1$ (type IIA) metric

\[ \begin{split}
        ds^2 & = \left(\frac{u}{R_{D4}}\right)^{3/2} \left[ -(dx^0)^2 + \sum_{i=1}^3 (dx^i)^2 +f(u) (dx^4)^2
\right] + \left(\frac{R_{D4}}{u}\right)^{3/2} \left[\frac{du^2}{f(u)} + u^2 d\Omega_4^2 \right]\\
        F_{(4)} &= \frac{2\pi N}{V_4} \epsilon_4, \quad e^\phi = g_s \left(\frac{u}{R_{D4}}\right)^{3/4},
\quad
        R_{D4}^3 \equiv \pi g_s N l_s^3, \quad
        f(u) \equiv 1-\left(\frac{u_\Lambda}{u}\right)^3,
\end{split} \]

(3.16)

The string coupling $g_s$ is related to the $4+1$ Yang-Mills coupling by $4\pi^2 g_s l_s = g_5^2$. Here $x_4
\sim x_4 + 2\pi R$ with $R = \frac{2}{3} \left(\frac{R_{D4}^3}{u_\Lambda}\right)^{1/2}$ (by demanding smooth
solution where the $x_4$ circle shrinks at $u=u_\Lambda$).

#### [sec-d4_back-p2] paragraph

The thermodynamics of this system was studied in [44]. The thermal solution is produced by analytically
continuing the time direction to a circle of size $\beta$, $x_0 = i t$ $t \sim t+\beta$. On the gravity side,
the analytically continued solution is the dominating solution for low temperatures. For high temperatures,
one can take the same solutions, only with the $R$ and $\beta$ circles switched, so that now the temporal
circle shrinks in the bulk. This last solution is a Euclidean black brane solution. The phase transition
between the two happens at $\beta=2\pi R$ [44].

#### [sec-d4_back-p3] paragraph

Here we are interested in winding condensate solutions around the (analytically continued) thermal saddle
(3.16). The solutions extend homogeneously on the $x^i$ directions but localize around $u=u_\Lambda$. Defining
$r^2 = \frac{4}{3} \left(\frac{R_{D4}^3}{u_\Lambda}\right)^{1/2} (u-u_\Lambda)$, $x_0 = i t$ and $\phi =
\frac{x_4}{R}$ we have to leading order in $r^2$

\[ \begin{split}
        ds^2 & = \left(\frac{u_\Lambda}{R_{D4}}\right)^{3/2} \left[ dt^2 + \sum_{i=1}^3 (dx^i)^2\right] + r^2
d\phi^2 + dr^2 + \left(\frac{R_{D4}^3}{u_\Lambda}\right)^{1/2} d\Omega_4^2.
\end{split} \]

(3.17)

And at the next order in $r^2$

\[ G_{tt} = \left(\frac{u_\Lambda}{R_{D4}}\right)^{3/2}\left(1+\frac{3}{2} \frac{u-u_\Lambda}{u_\Lambda}\right) = \left(\frac{u_\Lambda}{R_{D4}}\right)^{3/2}\left(1+\frac{27 R}{16 R_{D4}^3} r^2\right). \]

(3.18)

Comparing with (3.1) we find the curvature scale $l^2 = \frac{16}{27} \frac{R_{D4}^3}{R}$. In this model, the
(confining) string tension is given by $T_{st} = \frac{1}{2\pi \alpha'}
\left(\frac{u_\Lambda}{R_{D4}}\right)^{3/2} = \frac{4}{27 \pi \alpha'} (R_{D4}/R)^3$ and the mass gap (called
the glueball mass) is of order $M_{gb} = 1/R$. Plugging inside (3.11) with $d=2$ gives the leading correction
to the holographic Hagedorn temperature

\[ \begin{split}
        \beta_c  = \sqrt{\frac{4\pi}{T_{st}}} - \frac{1}{\sqrt{2}}\frac{M_{gb}}{T_{st}}+ O(M_{gb}^2
T_{st}^{-3/2}),
\end{split} \]

(3.19)

or in terms of the dimensionless ratio $\lambda_5/R$:

\[ \beta_c / R = \sqrt{108 \pi^3}\cdot \left(\lambda_5/R\right)^{-1/2}
            - \frac{27 \pi^2}{\sqrt{2} \left(\lambda_5/R\right)^{-1}}
            +O((\lambda_5/R)^{-3/2}). \]

(3.20)

For a worldsheet derivation of (3.19), see [56].

#### [sec-d4_back-p4] paragraph

We found that this model admits a ‘winding-string gas’ saddle for near-Hagedorn temperatures: a normalizable
condensate of winding strings around Euclidean time $t$ that extends homogeneously on the $R^3$ directions
(and $x^4$). The condensate is localized in the bulk around $u=u_\Lambda$ with a size of $L \sim \sqrt{l_s l}
\sim l_s \cdot (T_{st} / M_{gb}^2)^{1/4}$.

#### [sec-d4_back-p5] paragraph

The winding-string gas saddle is highly metastable, as it has free energy higher than both the thermal
solution and (because we are above the phase transition) the black brane solution. Note that the phase diagram
is very similar to that of the AdS$_{3}$, due to $2\pi R \iff \beta$ symmetry. Just like for the BTZ solution,
the black brane solution has a tachyonic instability below the temperature

\[ \beta'_c = \frac{4\pi}{3} R_{D4} \left(\frac{R^2}{\alpha'}\right)^{1/3} = 2^{4/3} \pi \left(T_{st} M_{gb}^{-5}\right)^{1/3}. \]

(3.21)

For temperatures slightly above it, there exists a condensate of winding $x^4$ strings homogeneous on
$R^3\times S^1_\beta$, obtaining by interchanging the asymptotic circles for the winding-string gas saddle. It
is possible to speculate a new kind of correspondence principle or a black brane/string transition. The black
brane with $x^4$ winding condensate and the thermal solution with $t$-winding condensate are connected via a
line of metastable saddles.

#### [sec-d4_back-p6] paragraph

To understand the relation to pure Yang-Mills, it is useful to write the critical temperatures in terms of $R$
and the $4+1$ Yang-Mills coupling $\lambda_5$

\[ \beta_c/R = \sqrt{108 \pi^3\frac{R}{\lambda_5}}, \quad \beta_{HP}/R = 2\pi, \quad \beta_c'/R = \frac{2}{3} \left(\pi^2 \frac{\lambda_5}{R}\right)^{1/3}. \]

(3.22)

The semiclassical approximation is valid when $l \gg l_s \gg l_{pl}$ or $1 \ll \lambda_5 / R \ll N$. In this
regime $\beta_c / R \ll 1 \ll \beta_c' / R$. In the opposite limit, $\lambda_5/R \ll 1$ the holographic theory
at energies below $\sim 1/R$ is that of pure $3+1$ Yang-Mills. In [44] the phase diagram of the system was
suggested for any $\lambda_5,R$. At $\lambda_5/R \ll 1$ and for low temperatures $\beta \gg R$ the theory is
described by $3+1$ SYM. This theory has a first-order confinement/deconfinement close to its Hagedorn
temperature $\beta_c \gg R$. As a result, we also expect a phase transition at high temperatures $\beta_c' \ll
R$. The simplest scenario suggested in [44] was a single new dominating phase for temperatures $\beta_c' <
\beta <\beta_c$. In such a scenario, this phase should have the unique property that it maps to itself when
interchanging $\beta,R$.11

#### [sec-d4_back-p7] paragraph

Going back to the gravity limit $1 \ll \lambda_5/R \ll N$. If indeed the winding-string gas saddle is the one
that connects the two saddles between $\beta_c$ and $\beta_c'$, the simplest option would be that its
continuation to the $\lambda_5/R \ll 1$ is the dominant phase for temperatures $\beta_c' < \beta <\beta_c$,
see figure 2. Notice that because the winding-string gas phase breaks the winding of both circles, it is
indeed invariant to switching $\beta,R$. This picture is also supported by the analysis of [57] which studied
$2d$ SYM on a torus. In the weakly coupled regime, the authors found a dominating phase with non-zero
holonomies on both circles.

#### [fig-witten_model] figure: Figure 2

Figure 2. The phase diagram of the D4 Witten model as suggested by the analysis of [44]. Left: The phase
diagram when the bulk geometry is weakly curved $R \ll \lambda_5$. The two black lines represent the thermal
and the black brane geometry, with a Hawking-Page transition at $\beta=2\pi R$. The two red dots represent the
two critical temperatures $\beta_c$, $\beta_c'$ above (below) which the thermal (black brane) saddle suffers
from tachyonic instability. The blue line represents the ‘winding-string gas’ saddle, which we suggest
connects the two winding condensate solutions of each saddle. Right: In the regime $R \gg \lambda_5$ the low
energy behavior is that of $3+1$ Yang-Mills, with a confinement/deconfinement transition at $\beta_c \gg R$. A
similar transition happens for the ‘black brane’ below some $\beta_c' \ll R$. We suggest that the dominating
phase for $\beta_c'<\beta < \beta_c$ is nothing but the ‘winding-string gas’ saddle.

### [sec-d3_back] section: 3.4 The D3 Witten model
#### [sec-d3_back-p1] paragraph

It is possible to repeat the previous construction also for D3s compactified on a circle [34, 58, 59]. The
holographic theory is now $3+1$ $\mathcal{N}=4$ $SU(N)$ Yang-Mills on $R^3 \times S^1$ with anti-periodic
boundary conditions on the fermions. The gravity dual is the near-Horizon limit of $N$ D3 branes on $S^1$.
After analytically continuing $x^0 = i t$ we find the thermal solution

\[ \begin{split}
        ds^2 / l_{ads}^2 &= f(u) d\tau^2 + f^{-1}(u)du^2 + u^2 \left[ dt^2 + \sum_{i=1}^2 (dx^i)^2\right] +
d\Omega^2_5,\\
        f(u) &= u^2 - \frac{u_0^4}{u^2}, \quad F_5 = 16 \pi  N \alpha'^2 \omega_5,
\end{split} \]

(3.23)

with $l_{ads}^2 = \sqrt{4\pi g_s N} \alpha'$, $\tau \sim \tau + \pi/u_0$ (the $\tau$-circle closes at $u=u_0$)
and the length of the asymptotic circle is $R=1/(2 u_0)$. There is a non-zero RR flux through the $S^5$,
$\int_{S^5} \omega_5 = \pi^3$. Close to $u=u_0$ the radial coordinate is $r = R ((u-u_0)/u_0)^{1/2}$ and

\[ G_{tt} = R^2 u_0^2 \left(1 + 2 \frac{r^2}{l_{ads}^2}+...\right). \]

(3.24)

Comparing with (3.1) we find the curvature scale $l^2 = l_{ads}^2/2$ with $d=2$ (shrinking $S^1$). Following
(3.11) the leading correction to the holographic Hagedorn temperature is

\[ \beta_c = \sqrt{\frac{4\pi}{T_{st}}} \left(1 - (4\pi g_s N)^{-1/4} + O\left((4\pi g_s N)^{-1/2}\right)\right), \]

(3.25)

with $T_{st} = R^2 u_0^2/(2\pi \alpha')$. The phase diagram of this model (when the gravity approximation is
valid) is similar to the D4 case. A black brane solution exists by replacing the two Euclidean circles and
dominates the canonical ensemble for high temperatures $\beta > 2\pi R$. The black brane is tachyonic for
temperatures below (at leading $g_s N$ order)

\[ \beta_c' = \frac{\pi}{2^{3/2}} \frac{R}{l_s u_0} = \frac{\pi}{4} \sqrt{\frac{4\pi g_s N}{T_{st}}}. \]

(3.26)

The same line of argument used for the D4 suggests a similar black brane/string transition. The black brane
and the thermal saddle are connected between $\beta_c \le \beta \le \beta_c'$, with perturbative winding
condensates being the near-critical description at each side.

### [sec-mn_back] section: 3.5 The Maldacena-Nuñez background
#### [sec-mn_back-p1] paragraph

In [35] Maldacena and Nuñez (interpreting the solutions of [60]) considered $N$ D5 branes on $R^4 \times S^2$,
with a twisted normal bundle on $S^3$. The holographic effective description is $5+1$ maximally supersymmetric
YM on $R^4\times S^2$ with twisting of the $S^2$ using a gauge background for a $U(1)_R \subset SU(2)_R
\subset SO(4)$ global symmetry. In terms of $R^4$ the twist preserves $\mathcal{N}=1$ supersymmetry. We denote
the $5+1$ ’t Hooft coupling $\lambda_6$ and the radius of the $S^2$ by $R$. The near horizon 10d metric and RR
flux of the D5 system is given by

\[ \begin{split}
        ds^2_{str} / \alpha' &= e^{\phi_D} \left( -(dx^0)^2 + \sum_{i=1}^3 (dx^i)^2 + N \left[ d\rho^2 +
e^{2g(\rho)} d\Omega_2^2 + \frac{1}{4} \sum_{a=1}^3 (w_a - A_a)^2\right]\right)\\
        F_3 &= N \left[-\frac{1}{4} (w^1-A^1)\wedge(w^2-A^2)\wedge (w^3-A^3)+\frac{1}{4}\sum_{a=1}{3}F^a
\wedge(w^a-A^a)\right],
\end{split} \]

(3.27)

with

\[ \begin{split}
                e^{2\phi_{D}} &= g_s^2 \frac{\sinh 2\rho}{2 e^{g}}=g_s^2\left(1+\frac{8}{9}
\rho^2+O(\rho^4)\right),\\
                e^{2g} &= \rho \coth(2\rho) - \frac{\rho^2}{\sinh^2(2\rho)} - \frac{1}{4}.
\end{split} \]

(3.28)

here $w_a$ label 1-forms on $S^3$, and $A_a$ is a smooth solution that asymptotes at large $\rho$ to the
prescribed $S^2$ twist, and $F=dA$. In this geometry, the asymptotic $S^2$ shrinks at $\rho=0$. This solution
is weakly coupled and curved for $1 \ll g_s N \ll N$, or $1 \ll \lambda_6 /R^2 \ll N$. For $\lambda_6/R^2 \ll
1$ (in which gravity is highly curved) on the other hand the four-dimensional $\mathcal{N}=1$ theory decouples
at energies below $1/R$ [35].

#### [sec-mn_back-p2] paragraph

The thermal ensemble is produced by analytically continuing $x_0 = i t/ l_s$ ($t \sim t+\beta$). Close to
$\rho=0$ the radial coordinate is $r = (\alpha' g_s N)^{1/2} \rho$, and the temporal (string) metric component
is

\[ G_{tt} = e^{\phi_{D}} = g_s \left(1+ \frac{4}{9} \frac{r^2}{\alpha' g_s N} + O\left(\frac{r^4}{(\alpha'g_s N)^2}\right)\right). \]

(3.29)

At $r=0$ the $S^3$ has no twist ($A_i$ is flat), and as long as the solution’s size is smaller than $L \ll
(\alpha'g_s N)^{1/2}$ we can approximate the geometry by $S_1 \times R^3 \times R^{3} \times S^3$ ($r$ being
the radial direction in $R^3$). Comparing with (3.1), we find ‘winding-string gas’ saddles
$\chi(r),\varphi(r)$ homogeneous on $R^3 \times S^3$ for near-Hagedorn temperatures. In terms of section 3.1
$l = \frac{3}{2} (\alpha' g_s N)^{1/2}$ and $d=3$ (as we have a shrinking $S^2$), and the first correction to
the Hagedorn temperature is (3.11)

\[ \beta_c = \sqrt{\frac{4\pi}{T_{st}}} \left(1-(2 g_s N)^{-1/2} + O(N^{-1}) \right). \]

(3.30)

with $T_{st} = \frac{1}{2\pi \alpha'} g_s$.12

#### [sec-mn_back-p3] paragraph

Close to the Hagedorn temperature $\beta-\beta_c \ll \beta_c$ there exists a reliable winding-string gas
saddle homogeneous on the $R^3$ (and the rest of the compact directions) and localize at the IR $\rho=0$
region with size $L \sim l_s (g_s N)^{1/4}$. The black brane-like solution, in which the thermal circle
closes, and its thermodynamics were studied in [40, 41, 42].13 A black brane/string transition for this model
suggests the black brane (with a small horizon radius) is connected to the winding-string gas saddle via a
line of worldsheet CFTs.

### [sec-ks_back] section: 3.6 The Klebanov-Strassler conifold background
#### [sec-ks_back-p1] paragraph

The Klebanov-Strassler geometry is given by [36]

\[ ds^2 = h^{-1/2} \left(-(dx^0)^2 + \sum_{i=1}^3 (dx^i)^2\right) 
        + h^{1/2}\left(
        \frac{\varepsilon^{4/3} K(\tau)}{6 K^3(\tau)} d\tau^2 + (...)
        \right) \]

(3.31)

In $(...)$ we omitted the remaining 5 dimensions of the conifold geometry. For small $\tau$

\[ \begin{split}
        K(\tau) &= (2/3)^{1/3} - \tau^2/(5 \cdot 2^{2/3}\cdot 3^{1/3}) + O(\tau^4)\\
        h(\tau) &= (g_s M \alpha')^2 2^{2/3} \varepsilon^{-8/3}(a_0 - 2^{-1/3} 3^{-4/3} \tau^2 + O(\tau^4)),
\end{split} \]

(3.32)

and $a_0 \approx 0.71805$ [62]. Here $M$ is the number of fractional $D3$ branes and $\varepsilon$ is the
deformation parameter. The background also includes RR and NS-NS fluxes, which are immaterial in the
discussion of winding condensate.

#### [sec-ks_back-p2] paragraph

The thermodynamics of Klebanov-Strassler was studied in [38, 39, 45, 47]. Here we are interested only in the
thermal solution, given by analytically continuing (3.31) by $x^0 = i l_s t$ ($t\sim t+\beta$). At $\tau=0$ an
$S^2$ of the conifold geometry closes, and the geometry is approximately $R^4 \times R^3 \times S^3$. Defining
the radial coordinate $r=G_{\tau\tau}^{1/2} \tau$ we find 14

\[ G_{tt} = \frac{\varepsilon^{4/3}}{2^{1/3} a_0^{1/2} \ g_s M } \left(1 + \frac{1}{3 a_0^{3/2}} \frac{r^2}{g_s M \alpha'}\right). \]

(3.33)

In terms of (3.1) $d=3$ and a curvature scale $l^2 = 3 a_0^{3/2} g_s M \alpha'$. As a result, the leading
correction to the Hagedorn temperature in this background is

\[ \beta_c = \sqrt{\frac{4\pi}{T_{st}}} \left(1 - \frac{3^{1/2}}{2^{3/2} a_0^{3/4}} \left(g_s M\right)^{-1/2} + O\left((g_s M)^{-1}\right) \right), \]

(3.34)

they with the confining string tension $T_{st} = \frac{\varepsilon^{4/3}}{2^{4/3} a_0^{1/2} \pi} (\alpha' g_s
M)^{-1}$.

## [sec-small_RR] section: 4 AdS-sized solutions for AdS$_{3}$ with small RR flux
### [sec-small_RR_anal] section: 4.1 The effective action
#### [sec-small_RR_anal-p1] paragraph

In section 3.2 we concluded that the analysis for sub-AdS solutions breaks for small RR fluxes $1-\lambda^2
\sim \alpha'/l_{ads}^2$, where the solution’s size reaches the AdS scale $L \sim l_{ads}$. For those cases, we
can’t neglect the backreaction of the winding mode on the supergravity fields (2.15). In this section, we turn
to study the behavior of AdS$_{3}$ string stars for small RR fluxes, as well as the pure NS-NS case. To that
end we define

\[ 1-\lambda^2 \equiv a \cdot \frac{\alpha'}{l_{ads}^2}, \]

(4.1)

and assume $0 \le a \ll l_{ads}^2/\alpha'$.15 Section 3.2 considered only near-Hagedorn temperatures
$(R_0^2-R_H^2)/R_H^2 \sim l_s/l_{ads}$. For small RR flux, the important regime is the tighter
$(R_0^2-R_H^2)/R_H^2 \sim \alpha'/l_{ads}^2$ (which we can call the very-near-Hagedorn regime). We therefore
define

\[ R_0^2 = R_H^2 + \hat m^2 \cdot \frac{\alpha'^2}{l_{ads}^2}. \]

(4.2)

Solutions are expected to be valid as long as $R_0^2-R_H^2 \ll R_H^2$, or $\hat m^2 \ll l_{ads}^2/\alpha'$,
which we will therefore assume.

#### [sec-small_RR_anal-p2] paragraph

In the rest of the section, we will set the units to $l_{ads}=1$ for brevity. In terms of the new variables
and at leading order in $l_s/l_{ads}$ the effective mass (2.14) is

\[ m^2_\text{eff} = \hat m^2 + 2 a \ \sinh^2\rho. \]

(4.3)

In the limit $\lambda \approx 1$ the RR flux terms in the action (2.18) are subleading and can be neglected
$\eta=0$. For the rest of the fields, it is useful to redefine by (in $l_{ads}=1$ units)

\[ \chi = \alpha' \hat \chi, \quad 
        \phi = \alpha' \hat \phi, \quad
        \varphi = \alpha' \hat \varphi, \quad
        \psi = \alpha' \hat \psi, \quad
        \zeta = \alpha' \hat \zeta. \]

(4.4)

At leading order, we get the action

\[ \begin{align*}
        I_\text{String star} -I_{\text{TAdS}_3} &= \frac{\beta \alpha'^2}{16\pi G_N} \cdot F,
\tag{4.5}\end{align*} \]

with, upon integrating by parts, the normalized free energy (compared to that of thermal AdS$_{3}$)

\[ \begin{split}
        F  = \int d\rho \ \text{vol} \  &\Bigg[
        (\hat\psi')^2 +(\hat\varphi')^2-4 (\hat\phi')^2 \\
        &-\frac{1}{2}\tanh^2\rho \ (\hat\zeta')^2-4(\hat\psi+\hat\varphi-\hat\zeta)^2
        +4\tanh\rho \ \hat\zeta'(\hat\psi+\hat\varphi-\hat\zeta)\\
        &+4\hat\phi'\left(
        \tanh\rho \  \hat\varphi + \coth\rho \  \hat\psi - \tanh\rho \  \hat\zeta\right)\\
        &+|\hat\chi'|^2+m^2_\text{eff}\rho \  |\hat\chi|^2 + 4 \left( \cosh^2\rho \ \hat\varphi -\sinh^2\rho\
(\hat\zeta-\hat\psi)\right) |\hat\chi|^2
        \Bigg],
\end{split} \]

(4.6)

The equation of motion for the dilaton gives the first-order constraint (upon using the boundary conditions
for $\hat \psi$)

\[ 2\hat\phi' = \tanh\rho \  \hat\varphi + \coth\rho \  \hat\psi - \tanh\rho \  \hat\zeta. \]

(4.7)

Substituting (4.7) gives the equations of motion for the rest of the fields

\[ \begin{split}
        \hat \chi''+v(\rho) \hat \chi'&=(\hat m^2 + 2 a \ \sinh^2\rho) \hat \chi+4 \left(\cosh^2\rho \  \hat
\varphi+\sinh^2\rho \ (\hat\psi-\hat\zeta)\right)\hat\chi,\\
        \hat\varphi''+v(\rho) \hat\varphi'&=
        2\tanh\rho \  \hat\zeta'
        +\tanh^2\rho \  (\hat\varphi-\hat\zeta)+\hat\psi
        -4(\hat\varphi+\hat\psi-\hat\zeta)
        +2 \cosh^2\rho \ |\hat\chi|^2,\\
        \hat\psi''+v(\rho) \hat\psi' &=
        2\tanh\rho \  \hat\zeta'
        +\hat\varphi-\hat\zeta+\coth^2\rho \  \hat\psi
        -4(\hat\varphi+\hat\psi-\hat\zeta)
        +2 \sinh^2\rho \ |\hat\chi|^2,\\
        \hat\zeta''+u(\rho)\hat\zeta'&=
        4\coth\rho \ (\hat\varphi'+\hat\psi')
        +2(\hat\varphi-\hat\zeta+\coth^2\rho \ \hat\psi)
        +4 \cosh^2\rho \ |\hat\chi|^2,
\end{split} \]

(4.8)

with

\[ v(\rho) = \tanh\rho +\coth\rho , \quad u(\rho) = 3\coth\rho -\tanh\rho . \]

(4.9)

$a$ adds a potential to the linear equation for $\hat \chi$ and therefore for $a > 0$ we expect a normalizable
solution with size $L \sim 1$. Assuming an $O(1)$ result (for $\hat m^2 \sim O(1)$) gives
$|\chi|,|\varphi|,|\zeta| \sim \alpha' \ll 1$ which is self-consistent with our assumptions. The reader may
worry that as the effective mass is now $m^2_\text{eff}(\rho) \sim O(1)$ (in $l_{ads}$ units), higher
curvature corrections are now leading. In section 4.3 below we argue that the resulting mass shift is
proportional to $\Delta m^2 \propto (1-\lambda^2)$. For finite $a$ this is a $O(\alpha')$ correction to the
mass and therefore subleading.

#### [sec-small_RR_anal-p3] paragraph

In the extreme case $a=0$ ($\lambda=1$) we find the pure NS-NS background. In this case, the $\rho$ dependence
in $m^2_\text{eff}$ is exactly canceled between the metric and the NS-NS flux, which results in a constant
mass

\[ m^2_\text{eff}(\rho) = \hat m^2 = \frac{1}{\alpha'^2}(R^2_0-R_H^2), \]

(4.10)

equals to the flat space result (2.8). This property means that very close to the Hagedorn temperature strings
winding around the thermal circle are light arbitrarily close to the boundary $\rho \gg 1$, although the
proper length of the thermal circle diverges exponentially. Physically, this is due to the cancellation
between the gravitational attraction (of AdS space) and the electric repulsion (or the non-zero $H_3$). This
is related to the well-studied pure NS-NS AdS$_{3}$ long strings [32, 33]. These strings wind around the
angular circle of Lorentzian AdS$_{3}$ with finite energy arbitrarily close to the boundary. Because
asymptotically there is no difference between the two circles, the cancellation of the energy divergence at
large $\rho$ is of the same origin. As a result, for $a = 0$ the potential in (4.8) is quadratic and not
exponential. Nevertheless, we expect a normalizable solution for $\chi,\varphi,\zeta$ also in this case for
high enough $\hat m^2$, with a generic $L \sim 1$. We present numerical solutions to this equation in section
4.4 below.

### [section-4.2] section: 4.2 The AdS$_{3}$ Hagedorn temperature
#### [section-4.2-p1] paragraph

To find the leading correction to the AdS$_{3}$ Hagedorn temperature, we should look for the maximal value of
$\hat m^2$ (as a function of $a \ge 0$) for which there’s a solution to the linearized (4.8) equation for
$\hat\chi$16

\[ \hat \chi ''+ v(\rho) \, \hat \chi ' - \left(\hat m^2 +2a \ \sinh^2\rho \right) \hat \chi = 0. \]

(4.11)

Denoting this critical value by $\hat m^2_c$, the first correction to the AdS$_{3}$ Hagedorn temperature is

\[ R_c^2(\lambda) = \frac{2}{k} + \frac{\hat m^2_c}{k^2} + O(k^{-3}), \]

(4.12)

with $k=l_{ads}^2/\alpha'$. For $a=0$ the (smooth) linear solution can be found analytically to be

\[ \hat \chi_\text{lin}(\rho) = P_{\frac{-1+\sqrt{1+\hat m^2}}{2}}(\cosh(2\rho)), \]

(4.13)

with $P_n(x)$ being the Legendre function [22]. For $\rho \gg 1$ and $\hat m^2 > -1$ we have $\hat
\chi_\text{lin} \sim \exp(-\Delta_\chi \rho)$ with $\Delta_\chi = \Re(1-\sqrt{1+\hat m^2})$, and as $\hat
\chi_\text{lin} \sim \rho \exp(-\rho)$ for $\hat m^2=-1$. The solution is thus non-normalizable for any $\hat
m^2$, but it turns delta-function normalizable at $\hat m^2 = -1$ (at the Breitenlohner-Freedman bound).
Therefore for $a=0$ the critical value is $\hat m^2_c = -1$, and the first correction to the pure NS-NS
AdS$_{3}$ Hagedorn temperature is

\[ R_c^2(\lambda=1) = \frac{2}{k} - \frac{1}{k^{2}} + O(k^{-3}). \]

(4.14)

Interestingly, for the type II pure NS-NS this is also the exact result $R_c^2 = 2/k - 1/k^2$ [22, 63].17 The
fact that the zero-mode (4.13) is only delta-function normalizable is similar to flat space [16], and probably
corresponds to the fact the Lorentzian spectrum, in this case, is continuous.

#### [section-4.2-p2] paragraph

For $a>0$ the linear equation has a potential and so we expect only discrete values of $\hat m^2$ for which
exist normalizable solutions. We are interested in the ‘ground state’ solution, with the largest $\hat m^2$.
We weren’t able to find an analytical solution in this case, but it is possible to find it numerically. In
figure 3 we plotted $\hat m_c^2$ as a function of $a$. It can be seen from the figure that $\hat m^2$
decreases as $a$ grows. This is to be expected, as when $a \gg 1$ we expect from section 3.2 to find $\hat
m^2_c = - 2^{3/2} a^{1/2}$ (by translating (3.15) in terms of $\hat m^2$). This behavior is shown in the
figure by a black dashed line.

#### [fig-m2s_alpha] figure: Figure 3

Figure 3. The value of the leading correction to the Hagedorn temperature $\hat m^2_c$ as a function of $a$
(blue). The $a \gg 1$ behavior from section 3.2 is plotted in a black dashed line.

### [sec-higher_curv] section: 4.3 An argument against higher curvature corrections
#### [sec-higher_curv-p1] paragraph

Higher curvature corrections always appear with non-negative powers of the string scale and therefore are
naively subleading. For $d=2$, two operators still contribute at zeroth order in the string scale:
$\mathcal{R}_{2} |\chi|^2$ and $g^{tt} F_{ij} F^{ij} |\chi|^2$. For the mixed background (2.13) their value is
exactly a constant

\[ \mathcal{R}_{2} = -2,\quad g^{tt} F_{ij} F^{ij} = -4\lambda^2. \]

(4.15)

We can write these terms in the Lagrangian as

\[ \mathcal{L}_\text{hige-curv} = g_1 \cdot \mathcal{R}_{2} |\chi|^2 + g_2 \cdot \frac{1}{2}g^{tt} F^{ij} |\chi|^2 = -2(g_1 + g_2 \lambda^2) |\chi|^2, \]

(4.16)

for some unknown couplings $g_1,g_2 \sim O(1)$. Therefore the overall effect of these two terms is to shift
the effective mass of $\chi$ by a constant $\Delta m^2 = -2(g_1 + g_2 \lambda^2)$.18 As a result, the
effective mass for the pure NS-NS case is ($k=l_{ads}^2/\alpha'$)

\[ m^2_\text{eff}(\rho) = k^2(R_0^2-R_H^2) + \Delta m^2 + O(1/k). \]

(4.17)

We now turn specifically to the pure NS-NS theory $\lambda=1$, in which the worldsheet theory on thermal AdS
is known [22, 24, 63]. The mass of the particle dictates the asymptotic behavior of its mode close to the
boundary. As such, it should match the AdS$_{3}$ $SL(2,R)$ Casimir of the corresponding worldsheet vertex
operator. To find the exact worldsheet mass, we follow the discussion of [63], which uses the description of
thermal AdS$_{3}$ as a specific coset of $SL(2,C)$ [64]. For a given $\beta$, a bosonic $SL(2,C)$ WZW primary
with winding $\pm 1$ and $SL(2,C)$ Casimir $J^2 = s^2 + \frac{1}{4}$ (and $h_{int} =0$) has dimension

\[ h=\bar h = \frac{s^2 + \frac{1}{4}}{k-2} + \frac{k \beta^2}{16 \pi^2} \]

(4.18)

We change variables to $R_0 = \frac{\beta}{2\pi}$, $-4m^2 = s^2 + \frac{1}{4}$ to get

\[ h=\bar h = -\frac{1}{4}\frac{m^2}{k-2} + \frac{k R_0^2}{4}. \]

(4.19)

To write the type II expression we shift $k\mapsto k+2$ (only for the first term, as we keep the temperature
in string units $k R_0^2$ constant) and find

\[ h=\bar h = -\frac{1}{4}\frac{m^2}{k} + \frac{k R_0^2}{4}=\frac{1}{2}. \]

(4.20)

As a result, the mass of the winding vertex operator as a function of $R_0$ is

\[ m^2 = k^2 \left(R_0^2 - \frac{2}{k}\right). \]

(4.21)

Comparing with (4.17) we find that the higher curvature correction to the mass vanishes $\Delta m^2=0$, for
$\lambda=1$. In other words $g_1=-g_2$, and (for any $\lambda$)

\[ \Delta m^2 = -2g_1(1- \lambda^2). \]

(4.22)

Because in this section we consider only $1-\lambda^2 \sim 1/k$, this is a subleading effect.

### [sec-small_RR_num] section: 4.4 Numerical results
#### [fig-example] figure: Figure 4

Figure 4. The two profiles of $\hat \chi$, $\hat \varphi$ and $\hat \zeta$ for temperature $\hat m^2 = 0$ in
the pure NS-NS theory $a=0$ (left) and for $a=0.5$ (left).

#### [fig-chi0] figure: Figure 5

Figure 5. The value of $\hat\chi(0)$, $\hat\varphi(0)$ and $\hat\zeta(0)$ as a function of $\hat m^2$, for
$a=0.1$ (left) and $a=0.5$ (right). The horizontal dashed green line indicates the AdS Hagedorn temperature
$\hat m_c^2$.

#### [fig-lengthscale] figure: Figure 6

Figure 6. The size of $\hat \chi(\rho)$ as a function of $\hat m^2$, for $a=0.1$ (left) and $a=0.5$ (right).
The size is defined as the radius $\rho$ in which the value of $\hat \chi(\rho)$ is decreased by a factor of
$e$ compared to $\hat\chi(0)$. The horizontal dashed green line indicates the AdS Hagedorn temperature $\hat
m_c^2$.

#### [fig-free_energy] figure: Figure 7

Figure 7. The string star normalized free energy as a function of $\hat m^2$, in the pure NS-NS theory $a=0.1$
(left) and $a=0.5$ (right). The horizontal dashed green line indicates the AdS Hagedorn temperature $\hat
m_c^2$.

#### [sec-small_RR_num-p1] paragraph

To further study the profile of the AdS-sized string star solution we used numerical analysis to find the non-
linear solutions for (4.8) of $\hat \chi, \hat \varphi, \hat \psi$ and $\hat \zeta$ as a function of $a$ and
$\hat m^2$. We set the boundary condition $\hat\psi(0)=0$ to avoid curvature singularity and for a smooth and
normalizable solution

\[ \hat \chi'(0) = \hat \varphi'(0) =\hat \psi'(0)= \hat\zeta'(0) = 0, \quad 
        \hat \chi(\infty) = \hat \varphi(\infty) =\hat\psi(\infty) = \hat\zeta(\infty) = 0. \]

(4.23)

In practice, we chose $\rho_\text{min}=0.00001$ and $\rho_\text{max}=3$, and tried to satisfy
$\psi(\rho_\text{min})=0$ with

\[ \hat \chi'(\rho_\text{min}) = \hat \varphi'(\rho_\text{min}) = \hat\psi'(\rho_\text{min}) = \hat\zeta'(\rho_\text{min}) = 0, \quad 
        \hat \chi(\rho_\text{max}) = \hat \varphi(\rho_\text{max}) = \hat\psi(\rho_\text{max}) =
\hat\zeta(\rho_\text{max}) = 0, \]

(4.24)

using the shooting method. That is, we optimized the initial values at $\rho_\text{min}$ to satisfy the
boundary condition at $\rho_\text{max}$. Notice that the variable $\rho$ is already the dimensionless length
in which the characteristic size of the solution should be $O(1)$. Figure 4 shows the profile of the solution
at $\hat m^2=0$ for the pure NS-NS system $a=0$ and for $a=0.5$. We found that the near-Hagedorn solutions
require higher and higher accuracy for smaller values of $a$. The reason is that $a$ controls the size of the
potential for $\hat\chi$. In the extreme case of $a=0$, the linear equation for $\hat\chi$ has a continuous
normalizable spectrum above the Hagedorn temperature. As a result, below we treat $a$ as a regulator for the
simulation and plot $a=0.1$ instead of $a=0$.

#### [sec-small_RR_num-p2] paragraph

As the solutions are monotonically decreasing functions of $x$, the initial value at $\rho=0$ sets the
amplitude of the solution. Figure 5 shows the initial values $\hat\chi(0)$ (black), $\hat\varphi(0)$ (red) and
$\hat\zeta(0)$ (blue) as a function of the temperature $\hat m^2$. For large $\hat m^2 \gg 1$ (lower
temperatures) the solution amplitude seems to grow linearly with $\hat m^2$, or $|\chi| \sim
(R_0^2-R_H^2)/R_H^2$. This is the same scaling found for (higher dimensional) flat space solutions [12]. As in
flat space, the solution is no longer reliable at $|\chi| \sim (R_0^2-R_H^2)/R_H^2 \sim 1$ or for $\hat m^2
\sim l_{ads}^2/\alpha'$. This is self-consistent, as we assumed $\hat m^2 \ll l_{ads}^2/\alpha'$ to derive
(4.8). Notice that the temperature regime considered for finite RR flux $\hat m^2 \sim l_{ads}/l_s$ is inside
the regime of validity.

#### [sec-small_RR_num-p3] paragraph

As expected, the solution merges with the trivial solution $\hat \chi = \hat \varphi = \hat \psi = \hat \zeta
= 0$ at the Hagedorn temperature $\hat m^2_c$ (drawn in green dashed line). Close to $\hat m^2_c$ the winding
mode gets similar to the linear mode $\hat \chi_\text{lin}$ found numerically above, while
$|\hat\varphi|,|\hat\psi|,|\hat\zeta|\ll |\hat\chi|$ are much smaller. This behavior is similar to the one
found for higher dimensional AdS string stars [1] as well as for finite RR flux above (which is the large $a
\gg 1$ limit of the simulation).

#### [sec-small_RR_num-p4] paragraph

Figure 6 shows the size $L$ of the winding mode profile (in AdS units) as a function of the temperature. $L$
is defined as the value of $\rho$ at which the amplitude of $\hat\chi$ reaches $e^{-1} \hat\chi(0)$. The
length grows with the temperature, as was found for finite $RR$ flux (including higher dimensions [1]). For
finite $\hat m^2$ the size is at the AdS scale and bounded from above by the size of the linear solution at
the Hagedorn temperature $\hat m^2=\hat m^2_c$. At lower temperatures, $\hat m^2 \gg 1$ the solution size
reaches the string scale and the solutions are unreliable.

#### [sec-small_RR_num-p5] paragraph

The normalized AdS$_{3}$ string star free energy $F$ (4.6) is presented in figure 7 as a function of the
temperature. The free energy turns out to always be positive, which is not immediately clear from its form
(4.6). The AdS$_{3}$ string star is therefore thermodynamically disfavored compared to the thermal AdS$_{3}$
solution. As we explain above, the solution is also non-perturbatively metastable due to the dominant BTZ
solution. The free energy decreases with the temperature and goes to zero at the Hagedorn temperature when the
solution becomes trivial. General EFT arguments predict that close enough to the critical value $|\hat\chi|
\sim (\hat m^2-\hat m^2_c)^{1/2}$ (and $|\hat\varphi|,|\hat\psi|,|\hat\zeta| \sim (\hat m^2-\hat m^2_c)^1$).
As a result, we expect the Euclidean action to scale as

\[ I_\text{String star} -I_{\text{TAdS}_3} \sim \frac{\alpha'^2}{G_N} (\hat m^2 - \hat m^2_c)^2 \sim \frac{l_s}{G_N} \left(\frac{R_0-R_c}{R_c}\right)^2, \]

(4.25)

where in the last line we moved back to general units for brevity.

## [acknowledgments] section: Acknowledgments
### [acknowledgments-p1] paragraph

I would like to thank Micha Berkooz, Shai Chester, Rajesh Gopakumar, Indranil Halder, Daniel Jafferis, Yiyang
Jia, Zohar Komargodski, Suman Kundu, Ohad Mamroud, Adar Sharon, Tal Sheaffer, Gabriel Wong and Xi Yin for
useful discussions and comments. I especially thank Ofer Aharony and David Kutasov for their guidance and
comments on the manuscript.
 This work was partly funded by an Israel Science Foundation center for excellence grant (grant number
2289/18), by grant no. 2018068 from the United States-Israel Binational Science Foundation (BSF), by the
Minerva foundation with funding from the Federal German Ministry for Education and Research, by the German
Research Foundation through a German-Israeli Project Cooperation (DIP) grant “Holography and the Swampland",
and by a research grant from Martin Eisenstein.

### [footnotes] footnotes: Footnotes

Notes1Assuming the asymptotic circumference of the circle can be consistently frozen at the value $\beta$
[16].

2The definition of this line should be understood only in the $g_s\rightarrow0$ limit. At finite but small
$g_s$ the 1-loop corrections become leading close enough to the Hagedorn temperature. As the tree level result
gives an on-shell action $I \sim g_s^{-2} \left(\frac{\beta-\beta_c}{\beta_c}\right)^2$, we find the solution
is trustworthy only for $(\beta-\beta_c)/\beta_c \gg g_s$.

3To see this, notice the worldsheet action of the configuration $t(\sigma,\tau) = \frac{\beta}{2\pi} \sigma,
x^i(\sigma,\tau)=x^i(\tau)$ is
\[ S_B = \frac{i \beta}{2\pi \alpha'} \int d\tau \dot x^i(\tau) B_{ti}(x^i). \]

(2.5)

4One can also write $\alpha'^0$ terms that correct the $\varphi |\chi|^2$ coupling, which are also subleading.

5We assume $\Phi=0$ for the undeformed background.

6This is the reason this term is absent in [16, 5, 12].

7The quantization of the fluxes (on $S^3$) requires both $\lambda / \alpha'$, $\sqrt{1-\lambda^2} / \alpha'$
to be integers. In this work, we expand at leading order in $\alpha'$, and therefore this quantization is
invisible [27, 31].

8We gauge fixed the field potential $B_2$, $C_2$ to also depend solely on $\rho$, which fixes the allowed
components.

9By ‘meet’ we mean through a line of string theory backgrounds labeled by the asymptotic temperature $\beta =
2\pi R_0$.

10The discussion here is for $\lambda \sim O(1)$. We note that for small enough $\lambda \sim l_s/l_{ads}$ the
$\lambda$ (and the entire NS-NS flux) dependence is absent at leading order in $\alpha'$, and appears together
with the suppressed higher $\alpha'$ terms in (2.6).

11In other words, the line of solutions is smooth at $\beta=2\pi R$ and the saddle there is mapped to itself
under switching the circles. In more complicated scenarios, there are further phase transitions and phases
that are mapped to each other under interchanging $\beta,R$.

12The high energy description of this model is in terms of little string theory, which has its own, different,
Hagedorn temperature [61]. The latter appear at much higher temperatures $\beta_{H,LST} = 2\pi (\alpha'
N)^{1/2} \ll \beta_c$ (in the case we are considering $g_s N \ll 1$).

13For the thermodynamics of other supergravity duals of 4d confining gauge theories see [37, 43, 46]

14here the $x_i$ have units of length squared. When we write $G_{tt}$ we already multiplying by $\alpha'$ to
make contact with (3.1).

15Notice that the quantization of the RR charge requires $\sqrt{1-\lambda^2} l_{ads}^2/\alpha'=\sqrt{a}
l_{ads}/l_s$ to be integers. In our $l_{ads} \gg l_s$ limit it gives no restriction on the range of $a$.

16At the linearized order the other fields in (4.8) have no non-trivial solutions.

17I thank David Kutasov for pointing out that the first correction here is $O(k^{-2})$, and not $O(k^{-3/2})$
as found above (3.15) and in [1]. It is his comment that led me to study the AdS$_{3}$ case.

18Of course, both terms also induce a correction to the coupling of $\varphi$, $\zeta$ to $|\chi|^2$. Whenever
the constant shift is subleading, so is the coupling.

### [refs] references: References

References[1]E.Y. Urbach, String stars in anti de Sitter space, JHEP 04 (2022) 072 [2202.06966].
[2]G. Veneziano, A Stringy Nature Needs Just Two Constants, EPL 2 (1986) 199.
[3]L. Susskind, Some speculations about black hole entropy in string theory, hep-th/9309145.
[4]G.T. Horowitz and J. Polchinski, A Correspondence principle for black holes and strings, Phys. Rev. D 55
(1997) 6189 [hep-th/9612146].
[5]G.T. Horowitz and J. Polchinski, Selfgravitating fundamental strings, Phys. Rev. D 57 (1998) 2557 [hep-
th/9707170].
[6]T. Damour and G. Veneziano, Selfgravitating fundamental strings and black holes, Nucl. Phys. B 568 (2000)
93 [hep-th/9907030].
[7]R.R. Khuri, Selfgravitating strings and string / black hole correspondence, Phys. Lett. B 470 (1999) 73
[hep-th/9910122].
[8]D. Kutasov, Accelerating branes and the string/black hole transition, hep-th/0509170.
[9]A. Giveon and D. Kutasov, The Charged black hole/string transition, JHEP 01 (2006) 120 [hep-th/0510211].
[10]Y. Chen and J. Maldacena, String scale black holes at large D, JHEP 01 (2022) 095 [2106.02169].
[11]R. Brustein and Y. Zigdon, Black hole entropy sourced by string winding condensate, JHEP 10 (2021) 219
[2107.09001].
[12]Y. Chen, J. Maldacena and E. Witten, On the black hole/string transition, 2109.08563.
[13]B. Balthazar, J. Chu and D. Kutasov, Winding Tachyons and Stringy Black Holes, 2204.00012.
[14]A. Bedroya, High energy scattering and string/black hole transition, 2211.17162.
[15]B. Balthazar, J. Chu and D. Kutasov, On Small Black Holes in String Theory, 2210.12033.
[16]J.J. Atick and E. Witten, The Hagedorn Transition and the Number of Degrees of Freedom of String Theory,
Nucl. Phys. B 310 (1988) 291.
[17]O. Aharony, J. Marsano, S. Minwalla, K. Papadodimas and M. Van Raamsdonk, The Hagedorn - deconfinement
phase transition in weakly coupled large N gauge theories, Adv. Theor. Math. Phys. 8 (2004) 603 [hep-
th/0310285].
[18]T. Harmark and M. Wilhelm, Solving the Hagedorn temperature of AdS$_5$/CFT$_4$ via the Quantum Spectral
Curve: Chemical potentials and deformations, 2109.09761.
[19]B. Sundborg, The Hagedorn transition, deconfinement and N=4 SYM theory, Nucl. Phys. B 573 (2000) 349 [hep-
th/9908001].
[20]L. Alvarez-Gaume, C. Gomez, H. Liu and S. Wadia, Finite temperature effective action, AdS(5) black holes,
and 1/N expansion, Phys. Rev. D 71 (2005) 124023 [hep-th/0502227].
[21]M. Banados, C. Teitelboim and J. Zanelli, The Black hole in three-dimensional space-time, Phys. Rev. Lett.
69 (1992) 1849 [hep-th/9204099].
[22]M. Berkooz, Z. Komargodski and D. Reichmann, Thermal AdS(3), BTZ and competing winding modes condensation,
JHEP 12 (2007) 020 [0706.0610].
[23]F.-L. Lin, T. Matsuo and D. Tomino, Hagedorn Strings and Correspondence Principle in AdS(3), JHEP 09
(2007) 042 [0705.4514].
[24]M. Rangamani and S.F. Ross, Winding tachyons in BTZ, Phys. Rev. D 77 (2008) 026010 [0706.0663].
[25]D.L. Jafferis and E. Schneider, Stringy ER = EPR, JHEP 10 (2022) 195 [2104.07233].
[26]I. Halder, D.L. Jafferis and D. Kolchmeyer, A duality in string theory on AdS$_3$, 2208.00016.
[27]J.M. Maldacena, The Large N limit of superconformal field theories and supergravity, Adv. Theor. Math.
Phys. 2 (1998) 231 [hep-th/9711200].
[28]A. Giveon, D. Kutasov and N. Seiberg, Comments on string theory on AdS(3), Adv. Theor. Math. Phys. 2
(1998) 733 [hep-th/9806194].
[29]D. Kutasov and N. Seiberg, More comments on string theory on AdS(3), JHEP 04 (1999) 008 [hep-th/9903219].
[30]J.R. David, G. Mandal and S.R. Wadia, Microscopic formulation of black holes in string theory, Phys. Rept.
369 (2002) 549 [hep-th/0203048].
[31]M. Cho, S. Collier and X. Yin, Strings in Ramond-Ramond Backgrounds from the Neveu-Schwarz-Ramond
Formalism, JHEP 12 (2020) 123 [1811.00032].
[32]J.M. Maldacena, J. Michelson and A. Strominger, Anti-de Sitter fragmentation, JHEP 02 (1999) 011 [hep-
th/9812073].
[33]N. Seiberg and E. Witten, The D1 / D5 system and singular CFT, JHEP 04 (1999) 017 [hep-th/9903224].
[34]E. Witten, Anti-de Sitter space and holography, Adv. Theor. Math. Phys. 2 (1998) 253 [hep-th/9802150].
[35]J.M. Maldacena and C. Nunez, Towards the large N limit of pure N=1 superYang-Mills, Phys. Rev. Lett. 86
(2001) 588 [hep-th/0008001].
[36]I.R. Klebanov and M.J. Strassler, Supergravity and a confining gauge theory: Duality cascades and chi SB
resolution of naked singularities, JHEP 08 (2000) 052 [hep-th/0007191].
[37]D.Z. Freedman and J.A. Minahan, Finite temperature effects in the supergravity dual of the N=1* gauge
theory, JHEP 01 (2001) 036 [hep-th/0007250].
[38]S.S. Gubser, C.P. Herzog, I.R. Klebanov and A.A. Tseytlin, Restoration of chiral symmetry: A Supergravity
perspective, JHEP 05 (2001) 028 [hep-th/0102172].
[39]A. Buchel, C.P. Herzog, I.R. Klebanov, L.A. Pando Zayas and A.A. Tseytlin, Nonextremal gravity duals for
fractional D-3 branes on the conifold, JHEP 04 (2001) 033 [hep-th/0102105].
[40]A. Buchel and A.R. Frey, Comments on supergravity dual of pure N=1 superYang-Mills theory with unbroken
chiral symmetry, Phys. Rev. D 64 (2001) 064007 [hep-th/0103022].
[41]S.S. Gubser, A.A. Tseytlin and M.S. Volkov, NonAbelian 4-d black holes, wrapped five-branes, and their
dual descriptions, JHEP 09 (2001) 017 [hep-th/0108205].
[42]A. Buchel, On the thermodynamic instability of LST, hep-th/0107102.
[43]A. Buchel and J.T. Liu, Thermodynamics of the N=2* flow, JHEP 11 (2003) 031 [hep-th/0305064].
[44]O. Aharony, J. Sonnenschein and S. Yankielowicz, A Holographic model of deconfinement and chiral symmetry
restoration, Annals Phys. 322 (2007) 1420 [hep-th/0604161].
[45]O. Aharony, A. Buchel and P. Kerner, The Black hole in the throat: Thermodynamics of strongly coupled
cascading gauge theories, Phys. Rev. D 76 (2007) 086005 [0706.1768].
[46]A. Buchel, S. Deakin, P. Kerner and J.T. Liu, Thermodynamics of the N=2* strongly coupled plasma, Nucl.
Phys. B 784 (2007) 72 [hep-th/0701142].
[47]A. Buchel, Klebanov-Strassler black hole, JHEP 01 (2019) 207 [1809.08484].
[48]J.M. Maldacena and H. Ooguri, Strings in AdS(3) and SL(2,R) WZW model 1.: The Spectrum, J. Math. Phys. 42
(2001) 2929 [hep-th/0001053].
[49]N. Agia, I. Halder and D.L. Jafferis. upcoming work.
[50]J. Polchinski, String theory. Vol. 2: Superstring theory and beyond, Cambridge Monographs on Mathematical
Physics, Cambridge University Press (12, 2007), 10.1017/CBO9780511618123.
[51]A. Cavaglià, N. Gromov, B. Stefański, Jr. and A. Torrielli, Quantum Spectral Curve for
AdS$_{3}$/CFT$_{2}$: a proposal, JHEP 12 (2021) 048 [2109.05500].
[52]S. Ekhammar and D. Volin, Monodromy bootstrap for SU(2|2) quantum spectral curves: from Hubbard model to
AdS$_{3}$/CFT$_{2}$, JHEP 03 (2022) 192 [2109.06164].
[53]A. Cavaglià, S. Ekhammar, N. Gromov and P. Ryan, Exploring the Quantum Spectral Curve for
AdS${}_3$/CFT${}_2$, 2211.07810.
[54]S. Frolov and A. Sfondrini, Mirror thermodynamic Bethe ansatz for AdS3/CFT2, JHEP 03 (2022) 138
[2112.08898].
[55]E. Witten, Anti-de Sitter space, thermal phase transition, and confinement in gauge theories, Adv. Theor.
Math. Phys. 2 (1998) 505 [hep-th/9803131].
[56]F. Bigazzi, T. Canneti and A.L. Cotrone, On the Hagedorn temperature in holographic confining gauge
theories, JHEP 01 (2023) 034 [2210.09893].
[57]O. Aharony, J. Marsano, S. Minwalla, K. Papadodimas, M. Van Raamsdonk and T. Wiseman, The Phase structure
of low dimensional large N gauge theories on Tori, JHEP 01 (2006) 140 [hep-th/0508077].
[58]O. Aharony, S.S. Gubser, J.M. Maldacena, H. Ooguri and Y. Oz, Large N field theories, string theory and
gravity, Phys. Rept. 323 (2000) 183 [hep-th/9905111].
[59]C. Csaki, H. Ooguri, Y. Oz and J. Terning, Glueball mass spectrum from supergravity, JHEP 01 (1999) 017
[hep-th/9806021].
[60]A.H. Chamseddine and M.S. Volkov, NonAbelian BPS monopoles in N=4 gauged supergravity, Phys. Rev. Lett. 79
(1997) 3343 [hep-th/9707176].
[61]D. Kutasov and D.A. Sahakyan, Comments on the thermodynamics of little string theory, JHEP 02 (2001) 021
[hep-th/0012258].
[62]L.A. Pando Zayas, J. Sonnenschein and D. Vaman, Regge trajectories revisited in the gauge / string
correspondence, Nucl. Phys. B 682 (2004) 3 [hep-th/0311190].
[63]T.G. Mertens, H. Verschelde and V.I. Zakharov, The thermal scalar and random walks in $AdS_3$ and $BTZ$,
JHEP 06 (2014) 156 [1402.2808].
[64]S. Hemming, E. Keski-Vakkuri and P. Kraus, Strings in the extended BTZ space-time, JHEP 10 (2002) 006
[hep-th/0208003].
