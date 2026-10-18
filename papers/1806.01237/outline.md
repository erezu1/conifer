# Outline of: The metric description of viscoelasticity and instabilities in viscoelastic solids

Abstract:

Many manmade and naturally occurring materials form viscoelastic solids. The increasing use of biologically inspired elastomeric material and the extreme mechanical response these elastomers offer drive the need for a better, more intuitive and quantitative understanding of the mechanical response of such continua. This is in particular important in determining the stability of viscoelastic structure over time where in lieu of robust rules we often must resort to simulations.
In this work we put forward a metric description of viscoelasticity in which the continua is characterized by temporally evolving reference lengths quantified by a rest reference metric. This rest reference metric serves as a state variable describing the result of the viscoelastic flow in the system, and allows us to provide robust claims regarding stability of incompressible isotropic viscoelastic media. We demonstrate these claims for a simple bistable systems of three standard-linear-solid spring dashpot assemblies where the predicted rules can be verified by explicit calculations, and also show quantitative agreement with recent experiments in viscoelastic silicone rubber shells that display delayed stability loss.

# [root] paper
## [introduction] section: ?? Introduction
### [introduction-p1] paragraph

Elastomeric solids are ubiquitous materials composed of cross-linked long molecular chains and display extreme
mechanical response properties. Examples include latex rubber, silicone rubbers [1] as well as the crosslinked
proteins resilin and elastin responsible for the mechanical properties of tissues such as ligaments and
arteries [2, 3, 4]. Elastomeric solids are characterized by low elastic moduli, and reversible deformations
even at strains exceeding one hundred percent. However, they also show stress relaxation when held at constant
displacement and creep under a constant load [5]. These creep and stress relaxation phenomena are dissipative
yet are reversible. Unlike viscoelastic fluids, elastomeric solids retain the topology of material elements in
the body indefinitely. Moreover, they display only fractional stress relaxation, supporting a finite fraction
of the stress even after arbitrarily long relaxation times.

### [introduction-p2] paragraph

One of the most fascinating phenomena displayed by elastomeric materials is delayed stability loss, in which a
fast instability releasing the elastically stored energy in a system is preceded by a slow creep. Such
phenomena have been observed in the rapid snapping of the Venus fly-trap leaf  [6] activated by the plant to
capture prey, in the passive snap through of thin elastomeric shells known as jumping poppers  [7, 8], and for
non-elastomeric materials in the slow crustal dynamics leading to some earthquakes [9, 10].

### [introduction-p3] paragraph

The equations of state for viscoelastic materials commonly relate the stress to the full history of the strain
in the body through a material dependent memory kernel [5]. Such equations of state accurately capture the
material response, and may be used to numerically study the response of viscoelastic structures given their
geometry and loading conditions [11, 12]. However, they rarely allow explicit solutions and provide very
little insight to the state of the viscoelastic material and its general response properties. The lack of
intuition for viscoelastic dynamics is exceptionally evident when considering viscoelastic instabilities; as
linear stress relaxation acts to reduce local stresses it is expected to have a stabilizing effect and in
particular never cause a meta-stable state to lose stability. More elaborated variations of this hand waving
argument, as we show in section ??, only prove it stronger rather than refute it, thus elucidating the subtle
nature of viscoelastic instabilities.

### [introduction-p4] paragraph

In this works we describe a metric approach to viscoelasticity and viscoelastic stability. We begin by
describing one dimensional viscoelastic systems through temporally evolving rest lengths and specifically
formulate the dynamics of the standard linear solid (SLS) model as a spring with temporally evolving rest
length. We then consider an assembly of three SLS springs in the form of a Von-Misses truss as a first example
of transient elastic stability in viscoelastic systems. We conclude the section describing this one
dimensional motion by using the temporally evolving rest lengths to prove general claims regarding the elastic
stability and stationarity of a general 1D, SLS systems.

### [introduction-p5] paragraph

The intuitive results we obtain for one dimensional SLS systems can be generalized to full three dimensional
systems. We next do so by constructing a covariant metric description of viscoelastic solids. The theory
describes the material response as elastic with respect to a time dependent three dimensional reference
metric. We elucidate the notions of quasi static approximation, transient elastic stability and isotropicity
in light of this new description. We then discuss results regarding the quasi-static dynamics when considering
isotropic and incompressible materials. Several claims regarding the elastic stability and stationary states
of such bodies are shown.

## [sec-1d_viscoelasticity] section: ?? Viscoelasticity and delayed stability loss in 1D
### [fig-sls_diagram] figure: Figure ??

.SLS_diagram.tex
Figure ??. Standard linear solid with total stiffness $k$, $\b$ and viscosity $\eta$.

### [standard-linear-solid] section: ?? Standard linear solid
#### [standard-linear-solid-p1] paragraph

The simplest intuitive model capable of displaying both finite stress relaxation and a finite response at high
rates is called the standard linear solid model (SLS) [13]. The SLS is a generalization of two spring-dashpot-
models - the Kelvin-Voigt model, accounting for the creep response, and the Maxwell model capturing the stress
relaxation and high loading rate response [14]. The SLS consist of spring of stiffness $\beta k$ and dashpot
of viscosity $\eta$ connected in series, both connected in parallel to another spring of stiffness
$(1-\beta)k$ (see FIG. ??). The dimensionless constant, $0\le \b \le 1$, accounts for difference between the
spring stiffness. The total length of the system is denoted $L$, the length on the dashpot is $L_d$, and the
rest length of the long and short springs read $\bar{L}^0$ and $\tilde{L}^0$, respectively. The total force is
then

\[ F = -(1-\b)k (L- \bar L ^0) - \b k (L-L_d- \tilde L ^0), \]

(??)

while force balance between the spring and dashpot in series yields the closure relation

\[ \eta \dot L_d = \b k (L-L_d- \tilde L ^0). \]

(??)

Rapid variation of the total length $L\to L+\Delta L$ will elongate the springs while leaving the dashpot
length, $L_{d}$ unchanged. The force under such conditions will increase by $\Delta F = k \Delta L$, similar
to a simple spring of stiffness $k$. Motivated by the temporal scale separation between the elastic response
of viscoelastic solids and their typical creep rate we seek to rephrase the force equations as a simple
elastic spring. By setting the reference length

\[ \bar L = (1-\beta)\bar{L}^0 +\beta\tilde L ^{0}+ \beta L_d, \]

and substituting in eq.?? we obtain

\[ F = -k (L-\bar L). \]

(??)

This is supplemented by the closure relation describing the temporal evolution of the reference length

\[ \dot {\bar L} = - \frac{1}{\tau}\left( \b (\bar L - L) + (1-\b)(\bar L - \bar L ^0) \right), \]

(??)

where $\tau = \frac{\eta}{\b k}$. The reference length evolves simultaneously towards $L$, the present state
of the system, and towards $\bar L^{0}$, the rest length to which it will asymptotically approach if left
unconstrained. The two simultaneous evolution terms are weighted by the dimensionless factor $0\le\beta\le 1$.
$\b =0$ corresponds to the elastic case in which $\bar L$ starts and stays at $\bar L ^0$. $\b = 1$
corresponds to a Maxwell material where the material reference length $\bar L$ has no preferred rest value and
approaches $L$, relaxing the force it supports to zero. One can easily generalize the SLS model to account for
multiple relaxation time scales by adding more spring dashpot pairs to the system in parallel, and even
account for a distribution of time scales that could give rise to non-exponential relaxation; e.g. power-law
or logarithmic. Such generalizations will not change the notion of the reference length or its interpretation
through eq.??, but only change the closure relation describing its temporal evolution:

\[ \bar{L} (t) = (1-\b)\bar L ^0 - \b \int_{-\infty}^{t} \dot \phi(t-s)L (s) ds. \]

(??)

Note that $\b$ retains its meaning as the fraction of force that is relaxed asymptotically in a constant
displacement setting. As we will see later this quantity dominates most of the questions of stability in
viscoelasitc systems, while the actual functional form of the memory kernel, $\phi$, only influences the
temporal approach to instability. For this reason it suffices to examine the question of stability loss in 1D
considering only the behavior of a simple SLS model. While ??, ?? are a mere reformulation of the familiar
viscoelastic dynamics, stating the problem in these new variables allows an intuitive interpretation of the
dynamics and deeper insight to the behavior such systems exhibit.

#### [fig-sls_von_mises_truss_diagram] figure: Figure ??

.SLS_model_diagram.tex
Figure ??. The SLS von-Mises truss model. Point mass connected to two diagonal SLS with $k_1$ each, and a
vertical SLS with total $k_2$. Both with dashpot $\eta$ and compliance $\b$.

### [sec-sls_von_Mises_truss] section: ?? SLS von-Mises truss
#### [sec-sls_von_Mises_truss-p1] paragraph

One of the most striking and subtle viscoelastic phenomena is delayed instability. To capture the essence of
the phenomena we consider three SLS’s of similar material parameters $\b$ and $\tau$, arranged to form a von-
Mises truss [15] as illustrated in figure ??. The truss is composed of a point mass that moves along the $z$
axis. It is connected to two diagonal SLS’s of stiffness $k_1$ that create a bi-stable elastic potential. The
symmetry of this potential is broken by a vertical SLS of stiffness $k_2$. The rest lengths are chosen such
that the system is relaxed and stationary at position $z = 1$ at rest lengths $\bar L^0_1 = \sqrt{2}$ and
$\bar L^0_2 = 0$. The lengths of each spring as function of $z$ are $L_1(z) = \sqrt{1+z^2}$ and $L_2(z) =
|z-1|$ respectively. As displayed on the previous section, each SLS is associated with a reference length
$\bar L_i$ that slowly evolves according to Eq. ??. The force on the mass is minus the derivative with respect
to $z$ of the instanteneous elastic energy

\[ E(z) =2 \frac{k_1}{2}(L_1(z)-\bar L_1)^2 + \frac{k_2}{2}(L_2(z)-\bar L_2)^2 \]

(??)

We set $\a = \sqrt{\tfrac{k_2}{2 k_1}}$ and note that for the purely elastic truss bi-stability is obtained
for small values of $\a$ whereas mono-stability is displayed at higher $\a$, where only the $z>0$ position is
stable. We wish to investigate the dynamics of the system in the quasi-static approximation, in which the the
mass position is causes vanishing of the total force $\frac{dE}{dz}=0$. For these purposes it is instructive
to employ a normalized energy function

\[ e(z) = \frac{E(z)}{k_1}  = (L_1(z)-\bar L_1)^2 + (\a L_2(z)-\a \bar L_2)^2 \]

(??)

This energy function may be interpreted as the Euclidean “distance” between the normalized reference lengths
$\mathbf{\bar L} = (\bar L_1, \a \bar L_2)$ and the normalized configuration lengths $\mathbf{L}(z) =
(L_1(z),\a L_2(z))$. We can thus use this 2D ’phase space’ of normalized lengths to understand the behavior of
the system. The admissible (normalized) lengths of the springs $\mathbf{L}(z)$ form a one dimensional curve
parameterized by $z$, whereas the reference lengths $\mathbf{\bar L}$ could be anywhere in the two dimensional
space. The Euclidean distance between the configuration $\mathbf{L}$ and the reference lengths $\mathbf{\bar
L}$ is exactly the elastic energy of the configuration. Specifically, as $\mathbf{L}(z) = (\sqrt{1+z^2}, \a
|z-1|)$, $z<1$ parametrize a hyperbola with its vertex at $(1,\a)$ (corresponding to $z=0$) and asymptotic
line $(L_1, \a L_1)$ as $z\rightarrow -\infty$. The rest lengths $\mathbf{\bar L^0}=(\sqrt{2},0)$ is a point
on the admissible lengths with $z=1$, or $\mathbf{\bar L^0} = \mathbf{L}(z=1)$ (see FIG. ??).

#### [sec-sls_von_Mises_truss-p2] paragraph

To understand the dynamics of the system, we choose the following protocol; the mass is taken from rest, where
$L_i=\bar L_i = \bar L_i^0$, abruptly to $z=-1$ and held there for a finite time. That is, at $t=0$ the
reference lengths $\mathbf{\bar L}$ are at the rest length values $\mathbf{\bar L^0}=(\sqrt{2},0)$ whereas the
springs are held at the configuration $\mathbf{L}_\text{hold} = (\sqrt{2},2 \a)$. By Eq. ?? during the holding
the reference lengths $\mathbf{\bar L}$ evolve along the line connecting $\mathbf{\bar L^0}$ and
$\mathbf{L}_\text{hold}$ up to a stationary position between them (See FIG. ??). We note that due to the
relaxation the reference lengths assume values not on the curve of admissible lengths, $\mathbf{L}(z)$, and
therefore do not correspond to any realizable configuration of the system. Nevertheless $\mathbf{\bar L}$
might have stable realizable configurations. An elastic equilibrium corresponds to a point of minimal
“distance” according to ?? between $L(z)$ and $\mathbf{\bar L}(t)$. Geometrically, this minimization condition
is satisfied if the line between the reference lengths $\mathbf{\bar L}$ and the configuration $\mathbf{L}$ is
normal to the admissible lengths curve $\mathbf{\bar L(z)}$ (see FIG. ??). After the release of the mass from
$\mathbf{L}_\text{hold}$ it will elastically snap to the closest stable point. Using this geometrical
interpretation of the viscoelastic quasi-static evolution, we can explain how different values of $\a$ create
different dynamical phases.

#### [fig-sls_von_mises_truss_lengths_space] figure: Figure ??

Figure ??. The normalized lengths 2D space for (a) $\a = 1$, (b) $\a = 0.3$ and (c) $\a = 0.1$. The curve of
admissible lengths $\mathbf{L}(z)$ is drawn in thick (black) line. The initial lengths $\mathbf{\bar
L}^0=(\sqrt{2},0)$ is drawn in (red) filled circle. During the relaxation the reference lengths $\mathbf{\bar
L}$ - drawn in gray filled circle - evolve in the direction of the holding lengths
$\mathbf{L}_\text{hold}=\mathbf{L}(z=-1)=(\sqrt{2},2\a)$. The stable positions of a specific reference lengths
is geometrically the normals from its point to the curve. (a) Unstable - even along the relaxation the system
remain mono-stable. (b) Finitely stable - bistability emerge because of the relaxation, and dissolve finite
time after releasing the system. (c) Stable - the system remains bistable during the holding.

#### [sec-sls_von_Mises_truss-p3] paragraph

We first consider cases with large $\a \rightarrow \infty$, illustrated in FIG. ??a. At rest, $\mathbf{\bar
L}=\mathbf{\bar L^0}$, only the rest lengths’s point $\mathbf{\bar L^0}$ is stable. That is, no other line
connecting the point $\mathbf{\bar L^0}$ with the curve $\mathbf{L}(z)$ meets the curve $\mathbf{L}(z)$
perpendicularly. During the holding, the reference lengths $\mathbf{\bar L}$ approache
$\mathbf{L}_\text{hold}$. However, still there is only one stable distance minimizing solution, which in turn
is obtained by slightly perturbing the rest solution $\mathbf{\bar L}=\mathbf{\bar L^0}$. In other words, the
elastic potential remain mono-stable along the entire relaxation. Upon release from $\mathbf{L}_\text{hold}$,
the configuration will snap to $\mathbf{L}_\text{s}$ and evolve back with $\mathbf{\bar L}$ to $\mathbf{\bar
L^0}$. Put in more conventional terms the relaxation of the forces during the holding was not enough to
stabilize the mass near the position of relaxation and when released it snaps back to a position near its
original rest position.

#### [sec-sls_von_Mises_truss-p4] paragraph

The second limit to consider is that of small $\a \rightarrow 0$, FIG. ??c. Low values of $\a$ diminish the
value of the eccentricity towards unity, shrink the hyperbola vertically and transform the two asymptotic
lines to become closer to parallel. Thus, as expected, the rest lengths $\mathbf{\bar L^0}$ is now associated
with two stable points; the original rest position and another stable point, $\mathbf{L}_\text{i}$, situated
closer to the inverted configuration $\mathbf{L}_\text{hold}$, and associated with $z<0$. During relaxation
the position of the two stable configurations also evolve slightly, $\mathbf{L}_\text{s}$ for some another
$z>0$ and $\mathbf{L}_\text{i}$ for different $z<0$. The system remains bi-stable, and the relaxation only
further lowers the instantaneous elastic energy of the inverted states (as their distance decreases).

#### [sec-sls_von_Mises_truss-p5] paragraph

If for this case we follow a different protocol in which the systems starts at rest and then brought abruptly
to the state $\mathbf{L}=\mathbf{L_{i}^0}$ which is a locally stable equilibrium with respect to $\mathbf{\bar
L}=\mathbf{\bar L^0}$, then while $\mathbf{\bar L}$ will evolve towards $\mathbf{L_{i}^0}$, the actual
configuration will remain unchanged at $\mathbf{L}=\mathbf{L_{i}^0}$. We term such states stationary states.
This stationarity property can be easily understood geometrically. In the protocol described $\mathbf{\bar L}$
evolves along the line connecting $\mathbf{L_{i}^0}$ and $\mathbf{\bar{L}^0}$ for every point on this line the
assumed configuration $\mathbf{L_{i}^0}$ is locally the closest to it, and thus the position of the elastic
equilibrium does not change.

#### [sec-sls_von_Mises_truss-p6] paragraph

Last we consider the case of intermediate values of $\a$ that display delayed instability. One could find
values of $\a$ large enough such that for $\mathbf{\bar L}=\mathbf{\bar L^0}$ only the state
$\mathbf{L}=\mathbf{\bar L}$ is stable, yet small enough such that after relaxation at
$\mathbf{L}_\text{hold}$ for time $t$ there will be two distinct locally stable equilibria with respect to
$\mathbf{\bar L}(t)$, as depicted in FIG. ??b. When released from relaxation the system will assume the state
$\mathbf{L}=\mathbf{L}_\text{i}$, where $z<0$. However, the reference length $\mathbf{\bar L}$ continuously
evolves towards collinearity with $\mathbf{L}$ and $\mathbf{\bar L^{0}}$. However, as no state other than the
trivial one is stable with respect to $\mathbf{\bar L}=\mathbf{\bar L^0}$ such a process cannot converge to a
stable state and thus must at some time loose stability.

#### [sec-sls_von_Mises_truss-p7] paragraph

The Von-Mises truss SLS models displays non-trivial phenomenology of instabilities of viscoelastic systems,
all of which are intuitively explained through the graphical representation. If the system at rest can be
brought to another locally stable equilibrium, then the equilibrium point will remain unchanged despite the
visco-elastic evolution. In particular it will never become unstable. Conversely, state that lose stability at
a finite time must have not been stable with respect to their rest state and their stability must have been
acquired through relaxation. Last, every acquired stable point cannot remain stable indefinitely and must
become unstable. The results obtained here were obtained for the specific geometry and constitutive relations
of the Von-Mises SLS system. However, they remain valid for rather general linear visco-elastic systems. In
appendix ?? we show that they hold for an arbitrary collection of SLS’s provided the mass they are connected
to is constrained to move along a line and they all share the same $\b$ and $\tau$. We next come to generalize
these result for the general isotropic and incompressible three dimensional linearly viscoelastic continua.

## [sec-metric_linear_viscoelasticity] section: ?? Metric linear viscoelasticity
### [sec-metric_linear_viscoelasticity-p1] paragraph

We now turn to discuss linear viscoelasticity of continuous bodies. Such systems are amenable to a geometric
reformulation similar to what we did for the SLS model. Here we need to exploit an infinitesimal analog of the
evolving reference lengths, which we achive by resorting to an elastic description using metric tensors.

### [sec-viscoelastic_continuum] section: ?? Linear viscoelastic continuum
#### [sec-viscoelastic_continuum-p1] paragraph

We start by equipping the body with a material (or Lagrangian) coordinate system $x^1,x^2,x^3$.
$\textbf{r}(x^i,t)$ is the configuration of the body at time $t$ in $\mathbb{R}^3$. The configuration manifest
itself on the coordinate system (up to time dependent rigid motions) by the induced Euclidean metric
$g_{ij}=\partial_i \textbf{r}\cdot \partial_j \textbf{r}$, which measure the infinitesimal lengths in the
solid [16]. In analogy with $\bar L^0$ we define the rest reference metric $\gbaro_{ij}$ as the metric on
which the body is locally stress-free and stationary. That is, if the body was to be cut to infinitesimal
pieces and each of the pieces allowed to freely relax indefinitely, then the lengths of each piece will
approach those represented by the rest reference metric $\gbaro_{ij}$. The strain tensor of the body is

\[ \e_{ij}(t) = \tfrac 1 2 \left(g_{ij}(t)-\gbaro_{ij} \right). \]

(??)

Different measures of stress correspond to different measures of volume. The second Piola-Kirchoff stress
tensor $S^{ij}$ is the virtual work conjugate of the metric, per unit volume $\sqrt{\gbaro}$  [17, 16]

\[ \begin{align*}
                        \d W & = -\int S^{ij} \d \e_{ij} \sqrt{\gbaro} d^3x
                        &  = -\frac{1}{2} \int S^{ij} \d g_{ij} \sqrt{\gbaro} d^3x
                \end{align*} \]

Intuitively, the energy difference obtained by varying only the distance between two points is exactly the
force between them. The general viscoelastic model assumes the stress at time $t$ is a functional of the
entire history of the strain $S^{ij}(t) = S^{ij}[\e_{ij}(s)]$ of times $s \le t$. $\gbaro_{ij}$ was described
above as the only stationary stress-free configuration. By Eq. ??, $S^{ij}(t)=0$ for all $t$ if and only if
the strain $\e_{ij}(t)=0$ for all $t$. Following [18] we can approximate the functional $S^{ij}[\e_{ij}]$
around the zero function, and obtain a linear functional

\[ S^{ij}(t) = C^{ijkl}\e_{kl} + \int_{-\infty}^t \Phi^{ijkl}(t-s) \e_{kl}(s)\ ds. \]

(??)

$C^{ijkl}$ is the stiffness tensor, $\Phi^{ijkl}(s)$ is the memory kernel accounting for the viscoelastic
dissipation. $\Phi(s)$ should fade over time, thus we take $\dot \Phi(s)<0$ and
$\Phi(s\rightarrow\infty)=0$ [18].

#### [sec-viscoelastic_continuum-p2] paragraph

Similar to the SLS, Eq. ?? predicts that instantaneous incremental deformations $\Delta g_{ij}$ lead to linear
stress increments $\Delta S^{ij} = \tfrac{1}{2}C^{ijkl}\Delta g_{kl}$. Following the above notion of temporal
reference length $\bar L$, we define the time-dependent reference metric $\gbar_{ij}$ of the body to satisfy

\[ S^{ij}(t) = C^{ijkl}\tfrac{1}{2} \left(g_{kl}(t)- \gbar_{kl}(t) \right). \]

(??)

The temporal evolution of the reference metric can be deduced from ??, ??, ??, ??, and reads

\[ \begin{align*}
                        \gbar_{ij}(t) & = \gbaro_{ij} - C^{-1}_{ijkl} \int_{-\infty}^{t} \dot
\Phi^{klmn}(t-s)\left(g_{mn}(s) -\gbaro_{mn}\right)ds  \tag{??}\\
                        & = \gbaro_{ij} - \int_{-\infty}^{t} \dot {\hat \Phi}^{kl}_{ij}(t-s)\left(g_{kl}(s)
-\gbaro_{kl}\right)\ ds.  \tag{??}\end{align*} \]

$\hat \Phi^{kl}_{ij}(s) = C^{-1}_{ijkl} \Phi^{klmn}(s)$ is the metric memory kernel. As we can see, $\bar
g_{ij}$ is defined only on cases where the stiffness tensor is invertible, a reasonable assumptions for most
solids. As expected, $\gbar_{ij}(t)$ remains unchanged by instantaneous variations of $g_{ij}$. We may thus
consider it as the slow state variable describing the viscoelastic evolution of the material. At each moment
in time we may consider the system as an elastic system with respect to the reference metric $\gbar_{ij}$ [16,
19].

### [sec-quasi_static_approximation] section: ?? The quasi static approximation
#### [sec-quasi_static_approximation-p1] paragraph

Viscoelastic systems are dissipative, thus the notion of an elastic free energy is ill defined. Nonetheless,
the virtual work of spatial variations performed by the body over a short period $\Delta t \rightarrow 0$,
coincides with the instantaneous elastic energy functional [16]

\[ E\left[\e^\text{el}_{ij}\right]=\int \frac{1}{2}C^{ijkl} \e^\text{el}_{ij} \e^\text{el}_{kl}\ \sqrt{|\gbaro|}\ d^3x, \]

(??)

where the elastic strain is again $\e^\text{el}_{ij} = \tfrac{1}{2}\left(g_{ij}-\gbar_{ij}\right)$. Typically
the elastic response time scale in elastomers is much smaller than the viscoelastic relaxation time. In such
cases we can eliminate inertia from the system and approximate the motion of material as quasi static
evolution between elastic equilibrium states. That is, the configuration at every moment in time, given by the
metric $g_{ij}(t)$, minimizes the instantaneous elastic energy functional ??. If we can characterize the
possible Euclidean metrics by finite set of variables $\l_\a$, i.e. $g_{ij}(x) = g_{ij} [ \l_\a ] (x)$ then
the minimization condition is for all $\a$, reads $\frac{\delta E}{\delta \l_\a}=0$ or

\[ F_\a\left[g_{ij}\right]=-\frac{1}{2}\int \frac{\delta g_{ij}}{\delta \l_\a} S^{ij} \ \sqrt{|\gbaro|}\ d^3x =0, \]

(??)

which is the vanishing of the generalized forces. For this extremal point to be a minima, the Hessian,
$\frac{\d^2E}{\d \l_\a \d \l_\b}$, needs to be positive definite.

#### [sec-quasi_static_approximation-p2] paragraph

Condition ?? gives $g_{ij}(t)$ as function of $\gbar_{ij}(t)$, which in turn evolve according to Eq. ??. The
quasi static evolution gives an intuitive interpretation of the slow evolution of viscoelastic bodies. Over
time, the material’s configuration quickly minimizes its ’distance’ to the reference metric. The idea that in
viscoelasticity bodies adapts to their configuration is implemented by the slow dynamics of the reference
metric from the rest reference metric toward the recent configurations. This coupled evolution of $g_{ij}$ and
$\gbar_{ij}$ is also simpler to analyze both numerically and theoretically compared with the full dynamics.

### [sec-delayed_stability_and_loss] section: ?? Acquired stability and stability loss
#### [sec-delayed_stability_and_loss-p1] paragraph

In section ?? we describe how the evolution of the reference lengths in discrete, 1D systems can result in non
trivial evolution of the configuration (characterized by $z$). When the parameter $\a$ is appropriately set
the von-Mises truss could acquire new type of stable states; namely states that are unstable initially, but
acquire stability through stress relaxation at a strained state. Such states also exist for continuous
viscoelastic systems, and similarly to the discrete case described above can be shown in some cases to not be
able to remain stable indefinitely.

#### [sec-delayed_stability_and_loss-p2] paragraph

A given reference metric $\gbar_{ij}$ can yield multiple elastically stable configurations of the
instantaneous elastic energy functional ??. Under external loading, as the reference metric slowly evolves
viscoelastically according to Eq. ?? it could acquire new stable configurations, merge existing stable points
or cause stable elastic configurations to lose their stability. Acquiring stability is most easily understood
by examining loading at constant displacements. Consider a body taken from rest to an initially unstable
configuration $g_{ij}^\text{hold}$. The body is held fixed at this position and the reference metric
$\gbar_{ij}$ starts from $\gbaro_{ij}$ and slowly advances toward the metric $g_{ij}^\text{hold}$, and the
forces pushing the body away from its present state gradually relax. When releasing the body an initially
unstable metrics near $g_{ij}^\text{hold}$ might display transient stability. This phenomenon is called
acquired stability.

#### [sec-delayed_stability_and_loss-p3] paragraph

State with acquired stability lose their stability through delayed stability loss. Seemingly stable state
gradually creep until at some point elastic stability is lost, and the body rapidly snaps to a near stable
configuration. Both acquired stability and delayed stability loss are expected for linear viscoelastic bodies,
close to multi-stability. Described quantitatively in section ?? below, as the memory kernel become comparable
to the stiffness, more configurations are able to acquire stability.

### [isotropicity] section: ?? Isotropicity and homogeneity
#### [isotropicity-p1] paragraph

Considering isotropic materials the stiffness and memory kernel tensors $C^{ijkl}$ and $\Phi^{ijkl}(s)$
further simplify. Isotropicity is the infinitesimal invariance to rotation in some configuration of the body.
More generally, it is the infinitesimal invariance to orthogonal transformations induced by some metric on the
body. This metric describes how each piece of the body should be deformed in order to have the same value
under rotations.

#### [isotropicity-p2] paragraph

By Eq. ??, the metric associated with the stiffness is the metric used to raise the indices of the elastic
strain to create the scalar energy density. In linear elasticity, in which $\gbar_{ij} = \gbaro_{ij}$, the
stiffness is usually taken as isotropic with respect to the reference metric $\gbar_{ij}$ [16]. This amounts
to assuming the body is isotropic in the undeformed configuration. The natural generalization of this
assumption to viscoelasticity is to take the stiffness as isotropic with respect to the instantaneous
reference metric $\gbar_{ij}$. This will yield isotropic response properties about the instantaneous stress
free state. However, an isotropic elastic response is often intimately related to isotropic material
composition and internal structure which in our case is set by the rest reference metric $\gbaro_{ij}$.
Therefore, we assume here the stiffness tensor to be isotropic with respect to the rest reference metric

\[ C^{ijkl} = \l \  \gbar_0^{ij} \gbar_0^{kl} + 2\mu \  \gbar_0^{ik} \gbar_0^{jl}. \]

(??)

We note that in principle, some materials may display a different constitutive behaviors, and in particular be
isotropic with respect the instantaneous reference metric $\gbar_{ij}$ in which case the elasticity tensor
should be adapted accordingly. Moreover, while it is reasonable to assume that the memory kernel
$\Phi^{ijkl}(s)$ accounting for the viscoelastic response will also be isotropic with respect to
$\gbaro_{ij}$, there is no restriction preventing it from being isotropic with respect to any linear
combination of $\gbaro_{ij}$ and $\gbaro_{ij}$.

#### [isotropicity-p3] paragraph

The assumption of homogeneity is usually obtained by taking the tensor at hand as constant in space. However,
because both $C^{ijkl}$ and $\Phi^{ijkl}(s)$ are densities of properties, homogeneity is a matter of measure.
Directly from Eq. ??, constant stiffness gives equal energy density per ’initial’ volume element
$\sqrt{\gbaro}d^3x$ (with the same deformation). Here too, in principle, one can account for other measures
induced by other metrics, and thus for different types of homogeneity. Thus even when a material is considered
isotropic and homogeneous, there are some choices as to how to express these symmetries in the constitutive
relations.

#### [isotropicity-p4] paragraph

We now focus on the reasonable and simplest option, where the stiffness and the memory kernel are both
isotropic and homogeneous with respect to $\gbaro_{ij}$. The general form of the metric memory kernel ${\hat
\Phi}^{kl}_{ij}(s)$ is

\[ \hat \Phi^{kl}_{ij}(s) = \b \phi(s) \d_i^k \d_j^l + \psi(s) \ \gbaro_{ij} \gbar^{kl}_0 \]

(??)

where $0<\b<1$ is defined by taking $\phi(0)=1$, and both $\phi(s),\psi(s)$ decrease monotonically to zero as
$s\rightarrow\infty$. Substitution in Eq. ?? gives the isotropic evolution of the reference metric

\[ \gbar(t) = (1-\b -\a(x,t))\ \gbaro_{ij} - \b \int_{-\infty}^{t} \dot \phi(t-s)\ g_{ij}(s)\ ds, \]

(??)

where

\[ \a(x,t) = \int_{-\infty}^t \dot \psi(t-s) \left(\gbar^{kl}_0 g_{kl}(x,s)-3\right) ds. \]

(??)

Note that $\a(x,t)$ is the only term in Eq. ?? that mixes the indices of the metrics.

## [sec-scalar_viscoelasticity] section: ?? Viscoelasticity of incompressible materials
### [constitutive-relations] section: ?? Constitutive relations
#### [constitutive-relations-p1] paragraph

Incompressible isotropic materials are described by Poisson ratio $\nu=\tfrac{1}{2}$. The incompressible
Poissonian contraction is expected to hold also during the viscoelastic relaxation. Thus, we expect
$\psi(s)=0$. Put in Eq. ?? and Eq ??, we obtain the following constitutive relation between stress and strain

\[ S^{ij}(t) = C^{ijkl} \left( \e_{kl}(t) + \b \int_{-\infty}^{t} \dot \phi(t-s) \e_{kl}(s)ds \right) . \]

(??)

The incompressible evolution of the reference metric (by ??, ??) also gives

\[ \gbar_{ij}(t) = (1-\b)\ \gbaro_{ij} - \b \int_{-\infty}^{t} \dot \phi(t-s)\ g_{ij}(s)\ ds. \]

(??)

The dimensionless factor $\beta$ quantifies the degree of viscoelasticity in the system. It corresponds to the
asymptotic value of the fraction of stress relaxed in a constant displacement experiment starting from rest.
Imposing a stationary solution for $\gbar_{ij}$ and $g_{ij}$ in Eq. ??, we obtain

\[ \gbar^\text{stat}_{ij} = \b g_{ij} + (1-\b)\gbaro_{ij}. \]

(??)

Here $\beta$ is shown to control the degree to which the reference metric of a viscoelastic body will approach
the current configuration metric; $\b=0$ describes a purely elastic material with a constant reference metric,
and $\b=1$ describes a viscoelastic fluid in which no information is conserved indefinitely, asymptotically
all stresses are relaxed, and the notion of the rest reference metric $\gbaro_{ij}$ has no meaning.

#### [constitutive-relations-p2] paragraph

As seen from Eq. ??, the long time stability of a body depends only on $\b$, and not on the specific memory
kernel. It is thus instructive to discuss the SLS model. The memory kernel for the SLS model is given by
$\phi(s)=e^{-\nicefrac{s}{\tau}}$. In analogy to Eq. ??, the differential equation for the reference metric
reads

\[ \begin{align*}
                        \dot \gbar_{ij}(t) =& -\frac{1}{\tau}\left(\b \left(\gbar_{ij}(t) - g_{ij}(t) \right)
+(1-\b) \left(\gbar_{ij}(t) - \gbaro_{ij} \right)\right)
                        =&-\frac{1}{\tau}\left( \gbar_{ij}(t)-\gbar^\text{stat}_{ij} (t)\right).

                \end{align*} \]

#### [fig-metric_space] figure: Figure ??

.metric_space.tex
Figure ??. A schematic representation of the metrics collinearity. The minimization of the metric $g$ is
constrained and performed with respect to a subset of metrics that correspond to realizable configurations.
Such metrics are in particular orientation preserving and Euclidean. This set is represented by the dashed
line above. Given a reference metric $\gbar$ the realized metric will correspond to the closest point from the
set of admissible metrics to $\gbar$ according to the distance function given by the instantaneous elastic
energy ??. Starting from rest, $\gbar$ evolves from $\gbaro$ towards $g$. Conversely, if $g$ is the closest
admissible metric to $\gbar^{\text stat}$ it is also such for $\gbaro$ which is collinear with the two.

### [sec-stationary_states] section: ?? Stationary states and the rest system
#### [sec-stationary_states-p1] paragraph

We now turn to examine the stationary solutions of the incompressible evolution rules Eq. ?? and??. As
described on section ?? and in appendix ??, the stationary states of one dimensional SLS structures are
extremal solutions of the rest elastic system $\bar L_i = \bar L_i^0$. Similar claim can be made for general
linear viscoelastic and incompressible bodies. By Eq ?? at stationarity $\gbar^\text{stat}_{ij} = \b g_{ij} +
(1-\b)\gbaro_{ij}$. Configuration $g_{ij}$ is stationary if it is in elastic equilibrium with respect to its
stationary reference metric $\gbar_{ij}^\text{stat}$. Thus, the generalized forces with respect to
$\gbar_{ij}^\text{stat}$ must vanish

\[ \begin{align*}
                        0 & = F^\text{stat}_\a\left[g_{ij}\right] \\
                        & = -\int C^{ijkl} \frac{\d g_{ij}}{\d \l_\a} (g_{kl}-\gbar^\text{stat}_{kl})
\sqrt{|\gbaro|}\ d^3x \\
                        & = -(1-\b) \ \int C^{ijkl} \frac{\d g_{ij}}{\d \l_\a} (g_{kl}-\gbaro_{kl})
\sqrt{|\gbaro|}\ d^3x\\
                        & = (1-\b) F_\a^0\left[g_{ij}\right].
                \end{align*} \]

$F_\a^0\left[g_{ij}\right]$ is the generalized force calculated in the rest elastic system $\gbar_{ij} =
\gbaro_{ij}$. Therefore the configuration is an extremal of the elastic energy functional with respect to the
rest reference metric $F^0_\a\left[g_{ij}\right]=0$. We thus obtained that all the stationary configurations
of viscoelastic body are extremals of its the rest elastic system.

#### [sec-stationary_states-p2] paragraph

Following Eqs. ?? and ??, we arrive to the following relation between the energy Hessians of the stationary
and rest systems

\[ \frac{\d^{2}E_\text{stat}}{\d\l_{\a}\d\l_{\b}} = (1-\b) \frac{\d^{2}E_0}{\d\l_{\a}\d\l_{\b}} 
                        + \frac{\b}{4} \int C^{ijkl}\frac{\d g_{ij}\left(x\right)}{\d\l_{\a}}\frac{\d
g_{kl}\left(x\right)}{\d\l_{\b}} \]

(??)

Drucker stability criterion states that $C^{ijkl}$ is positive definite, thus also $\int C^{ijkl}\frac{\d
g_{ij}\left(x\right)}{\d\l_{\a}}\frac{\d g_{kl}\left(x\right)}{\d\l_{\b}}$ is a positive definite matrix [14].
If the configuration was initially stable and $\frac{\d^{2}E_0}{\d\l_{\a}\d\l_{\b}}$ is positive definite,
then the stationary Hessian is also positive definite (sum of two positive definite matrices). Thus initially
stable (not only extremal) configuration is also stationary. But Eq. ?? also open the possibility for non-
stable but extremal configuration of the rest system, for example a saddle point, to stabilize indefinitely.
Eq. ?? also elucidate the basic intuition that when a system is held at constant displacement, stress
relaxation stabilizes the configuration; as we can see from the equation, originally non positive Hessian
become ’more positive’ along the relaxation. Both features depend on the value of $\b$. As $\b\rightarrow 0$
the system almost doesn’t change at all under relaxation and only initially stable configurations are also
stationary. Conversely, as $\b\rightarrow 1$ the system is able to stabilize more and more configurations, and
all the rest system extremals will become also stationary configurations.

#### [sec-stationary_states-p3] paragraph

The second phenomenon described in section ?? and in appendix ?? deals with bringing a system to a metastable
state abruptly from rest. Here we take body at rest and deform it fast into some other local elastically
stable configuration. We claim that the dynamics of the system’s configuration is trivial, i.e. a
configuration itself will display no temporal variation despite the continuous evolution of the reference
metric and the relaxation of the corresponding stress 1. First, we assume that the system starts at rest, i.e.
for all $t<0$ we have $g_{ij}(t)=\gbar_{ij}(t)=\gbaro_{ij}$. At $t=0$ the system is brought abruptly to an
elastically stable conifguration $g_{ij}(0)\ne \gbaro_{ij}$, such that $g_{ij}(0)$ satisfies ??. We wish to
show that $\dot g_{ij}(t) =0$ satisfies the evolution rules for all $t>0$. First, substitution in Eq. ?? gives

\[ \gbar_{ij}(t) = \gbaro+\b\left(1-\phi\left(t\right)\right)\left(g_{ij}-\gbaro_{ij}\right), \]

(??)

where $g_{ij}=g_{ij}(t)$ is constant in time. More importantly, we have the evolution of the elastic strain
$\e^\text{el}_{ij}(t) = \tfrac{1}{2}\left(g_{ij}-\gbar_{ij}(t)\right)$

\[ \begin{align*}
                        \e^\text{el}_{ij}(t) & = \left(1-\b\left(1-\phi\left(t\right)\right)\right)
\tfrac{1}{2}\left(g_{ij}-\gbaro_{ij}\right)
                        & = \left(1-\b + \b \phi(t)\right) \e^\text{el}_{ij}(t=0)
                \end{align*} \]

It is left to prove that the constant $g_{ij}$ remains at local minimum of the instantaneous energy functional
with respect to Eq. ??. First, the generalized force

\[ \begin{align*}
                        F_\a(t) & = -\frac{1}{2}\int C^{ijkl} \frac{\d g_{ij}}{\d \l_\a} \e^\text{el}_{kl}(t)
\sqrt{|\gbaro|}\ d^3x
                        & = \left(1-\b + \b \phi(t)\right) \ F_\a(t=0)
                        & = 0
                \end{align*} \]

The last step uses the stability of $g_{ij}$ at $t=0$ (with respect to $\gbaro_{ij}$). Second, the Hessian

\[ \begin{align*}
                        \frac{\d^{2}E(t) }{\d\l_{\a}\d\l_{\b}}& = \left(1-\b + \b \phi(t)\right)
\frac{\d^{2}E(t=0)}{\d\l_{\a}\d\l_{\b}} \\
                        & + \frac{\b}{4} \left(1-\phi(t)\right) \int C^{ijkl}\frac{\d
g_{ij}\left(x\right)}{\d\l_{\a}}\frac{\d g_{kl}\left(x\right)}{\d\l_{\b}}
                \end{align*} \]

By assumption, $\frac{\d^{2}E(t=0)}{\d\l_{\a}\d\l_{\b}}$ is a positive definite matrix. As we note above, the
right matrix is also positive definite. $\frac{\d^{2}E(t)}{\d\l_{\a}\d\l_{\b}}$ is thus a sum of two positive
definite matrices, and therefore also positive definite for all $t>0$. Thus, we have shown that $\dot
g_{ij}(t) =0$ for any $t>0$ is the solution to the quasi static evolution equations.

#### [sec-stationary_states-p4] paragraph

We note that the claims can not be derived under the general memory kernel $\Phi^{ijkl}(s)$ but only under the
assumption that the metric kernel is scalar $\hat \Phi_{ij}^{kl} = \b \phi(s) \d_i^k \d_j^l$. Still, the
result are valid to any incompressible solid in a continuous manner. That is, the actual variation from these
result diminish as the material at hand is closer to incompressibility.

#### [sec-stationary_states-p5] paragraph

Intuitively, both claims are due to collinearity of $g_{ij}$, $\gbaro_{ij}$ and $\gbar_{ij}$ under the
appropriate initial condition (see FIG. ??). If the evolution of the reference metric starts at rest
$\gbar_{ij}=\gbaro_{ij}$ then evolving toward $g^\text{stat}_{ij}$ also evolve in the direction of $g_{ij}$.
If the metric was originally stable - with ’minimal length’ to $\gbar_{ij}=\gbaro_{ij}$ , than it will also be
minimal to any reference metric $\gbar_{ij}(t)$ on the line between the rest reference metric to $g_{ij}$.

### [sec-transient_stability_loss] section: ?? Transient elastic stability and snap-through
#### [sec-transient_stability_loss-p1] paragraph

We have so far discussed the behavior of viscoelastic systems in states that are stable when arrived to from
rest. We next come to discuss the complementary states that are unstable. In particular we would like to
address how could they acquire stability and also in turn how this stability is lost. Jumping poppers are thin
rubber shells. Very thin poppers display almost isometric bi-stability, while thick poppers have only one
elastically stable shape. However, when an appropriately cut popper is flipped inside out and laid on the
table [Fig. ??] it creeps for a few seconds and snaps back to its original shape, much in the same manner
systems with intermediate values of $\a$ in the Von-Mises truss model of section ?? acquired and lost
stability.

#### [sec-transient_stability_loss-p2] paragraph

One general corollary of the previous section is that stability loss can occur only from configurations that
were “originally” unstable - not a stable configuration of the rest elastic system $\gbar_{ij}=\gbaro_{ij}$.
If the configuration was originally stable, than by the above claim it is also stationary, and its stability
can never be lost. Thus a system exhibiting temporary stability followed by a snap though, was necessarily
away of its rest system $\gbar_{ij}\ne\gbaro_{ij}$ before the free evolution. Therefore if a popper snap a
finite time after being inverted, its stability (prior to the snap) was necessarily acquired, presumably by
holding it inverted for a long enough duration.

#### [sec-transient_stability_loss-p3] paragraph

Second, acquired stability from configurations that were not extremal initially (e.g. saddle points) cannot
persist indefinitely and must be eventually lost. If a configuration is stationary after a relaxation that
started from rest then it must also be extremal with respect to the rest reference metric. In the case of the
popper it means that if it was originally unstable, there is no way (by holdings the popper inverted or by any
other deformations) to stabilize the popper indefinitely after the external loads are removed. For such cases
the inverted shapes cannot be stationary states of the system, and the popper will always eventually snap back
to an rest state.

#### [sec-transient_stability_loss-p4] paragraph



#### [fig-hopper_popper] figure: Figure ??

./protocol.pgf
  flip_time_vs_thickness.pgf
Figure ??.  (a) Straight and inverted poppers. (b) The experiment protocol: The cone is held in the inverted
shape for a time $t_\text{hold}$ and then released; it flips after a time $t_\text{flip}$. (c) The flipping
time as function of the cone thickness for the two limiting cases of immediate release and long holding time.
The elastic cone was simulated with geometrical properties $r_\text{min}=10[\text{mm}],r_{max}=25[\text{mm}]$.
The material properties taken were $\b = 0.3$, Young’s modulus $E=2.5[\text{MPa}]$ and Poisson ratio
$\nu=0.47$. A similar phase plot presented in [12] and in [8].

## [summary] section: ?? Summary and discussion
### [summary-p1] paragraph

Naively one expects stress relaxation to only diminish internal forces and thus act to stabilize a system
rendering the notion of viscoelastic instabilities elusive. We have shown this intuition to indeed be correct;
if a system is brought abruptly from its rest state into an elastically meta-stable state then stress
relaxation will never cause it to lose stability. We moreover proved that in such a setting the configuration
of the system will show no evolution despite the continuous vicoelastic attenuation of internal stresses.

### [summary-p2] paragraph

Having formulated the viscoelastic evolution in terms of metric tensors we observed that the instantaneous
reference metric evolves not only toward $g$, the assumed configuration, but also toward $\gbaro$, its rest
metric. When starting from rest only the former is observed. In this case the reference metric evolves along a
straight line and as a result the elastic energy minimizer at time $t$ with respect to $\gbar(t)$ remains the
minimizer for subsequent times, as explained graphically in FIG. ??. For every other case, in which $\gbar$
does not evolve solely toward $g$, we expect a visible creep and in particular such systems may display
viscoelastic instabilities. We have shown that the only states that can display viscoelastic instabilities are
states that are elastically unstable with respect to $\gbaro$ but have acquired stability through stress
relaxation. We have also shown that every instance of such an acquired stability cannot persist indefinitely
and must be lost in time.

### [summary-p3] paragraph

These results are expected to hold for every isotropic and incompressible linearly viscoelastic material
regardless of the form of history dependence of the stress relaxation kernel. However, considering a single
SLS system or any other purely one dimensional viscoelastic system we do not observe this rich phenomenology
of instabilities due to the trivial structure of the set of admissible states. The ability of a viscoelastic
system to display delayed instabilities relies on the non-trivial shape of the set of admissible states. As
observed in FIG. ?? for the SLS Von-Misses truss, only when the set of admissible states is sufficiently
curved can it support multi-stability. For continuous media the structure of admissible (Euclidean) states is
non-convex. As a result we may bring a systems that is initially at rest in an Euclidean configuration, to
another Euclidean state by the application of external forces, and the viscoelastic evolution will result in a
non-Euclidean instantaneous reference metric, giving rise to a geometrically frustrated state. In such cases
residual stress is like to appear even in lieu of multistability.

### [summary-p4] paragraph

While in the theory presented here the rest metric, $\gbaro_{ij}$, is assumed constant one could consider
growing tissue or plastically deforming material by allowing the rest metric to vary in time. The variation
could be provided by external conditions or obey some additional constitutive relations. This will result in a
covariant elaso-visco-plastic theory. Such a description may provide crucial insight into growing and
deforming biological polymers where a rapid growth or shrinkage events may be masked by the slow evolution of
the instantaneous reference metric. The applicability of such a theory, reminiscent of the additive
decomposition of strains [21, 19], to growing and deforming tissue remains to shown.

## [acknowledgments] section: Acknowledgments
### [acknowledgments-p1] paragraph

The authors would like to thank D. Biron, G. Cohen, A. Grosberg, S.M. Rubinstein, E. Sharon, Y. Bar-Sinai and
D. Vella for helpful discussions, as well as acknowledge the Aspen Center for Physics, which is supported by
National Science Foundation grant PHY-1607761, for hosting many of these discussions.

### [footnotes] footnotes: Footnotes

Notes1For the case of elasto-plasticity, a similar idea was first proved but never published by H. Aharony.
This type of behavior was also conjecture [22].

2Technically, another possibility is that the point will continuously progress to one of the rest elastic
system extremum points.

### [refs] references: References

References[1] L. R. G. Treloar,  The physics of rubber elasticity ( Oxford University Press, USA, 1975)
[2] S. O. Andersen, Biochimica et biophysica acta  69, 249 ( 1963)
[3] R. E. Neuman and M. A. Logan, Journal of Biological Chemistry  186, 549 ( 1950)
[4] J.  Gosline, M.  Lillie, E.  Carrington, P.  Guerette, C.  Ortlepp, and K.  Savage, Philosophical
Transactions of the Royal Society of London B: Biological Sciences  357, 121 ( 2002)
[5] R.  Christensen,  Theory of viscoelasticity: an introduction ( Elsevier, 2012)
[6] Y.  Forterre, J. M. Skotheim, J.  Dumais, and L.  Mahadevan, Nature  433, 421 ( 2005)
[7] A.  Pandey, D. E. Moulton, D.  Vella, and D. P. Holmes, EPL (Europhysics Letters)  105, 24001 ( 2014)
[8] E. Y. Urbach and E.  Efrati, “ Delayed instabilities in viscoelastic solids through a metric description,”
( 2018)
[9] A. M. Freed and J.  Lin, Nature  411, 180 ( 2001)
[10] Z.  Reches, G.  Schubert, and C.  Anderson, Journal of Geophysical Research: Solid Earth  99, 21983 (
1994)
[11] M.  Santer, International Journal of Solids and Structures  47, 3263 ( 2010)
[12] A.  Brinkmeyer, M.  Santer, A.  Pirrera, and P.  Weaver, International Journal of Solids and Structures
49, 1077 ( 2012)
[13] C.  Zener,  Elasticity and Anelasticity of Metals ( University of Chicago Press, 1948) google-Books-ID:
FKcZAAAAIAAJ
[14] A. F. Bower,  Applied mechanics of solids ( CRC press, 2009)
[15] Z.  Bažant and L.  Cedolin,  Stability of Structures: Elastic, Inelastic, Fracture, and Damage Theories,
Dover books on engineering ( Dover Publications, 1991)
[16] E.  Efrati, E.  Sharon, and R.  Kupferman, Journal of the Mechanics and Physics of Solids  57, 762 (
2009)
[17] L. D. Landau and E.  Lifshitz, Course of Theoretical Physics  3, 109 ( 1986)
[18] B. D. Coleman and W.  Noll, Reviews of Modern Physics  33, 239 ( 1961)
[19] E.  Efrati, E.  Sharon, and R.  Kupferman, Soft Matter  9, 8187 ( 2013)
[20]For the case of elasto-plasticity, a similar idea was first proved but never published by H. Aharony. This
type of behavior was also conjecture [22].
[21] E. H. Lee ( ASME, 1969)
[22] B.  Hayman, Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences
364, 393 ( 1978)
[23] N. J. Hoff, The Aeronautical Quarterly  7, 1 ( 1956)
[24]Technically, another possibility is that the point will continuously progress to one of the rest elastic
system extremum points.

## [app-1d_sls_systems] section: ?? 1D SLS truss and rest state stationarity
### [app-1d_sls_systems-p1] paragraph

Here we examine an explicitly solvable discrete system that is more complex than the three spring truss. This
system is composed of a point mass $m$, free to move along the $\hat z$ axis whose position we denote $z(t)$.
The mass is connected through SLS’s to $N$ pinned positions in the 2D space $(x_i,z_i)$. All the SLS’s share
the same $\b,\tau$ but may differ in their stiffnesses $k_i$. This choice is well justified when considering
large structures, or composite materials, made of many identical SLS’s. The compositions of identical SLS’s
(in parallel or in series) leave $\b$ and $\tau$ unchanged. Thus the effective description of an SLS structure
can assign different stiffnesses to distinct modes of deformations, but take $\b$ and $\tau$ as intrinsic
material properties. The length on each of the SLS’s is denoted $L_i = \sqrt{x_i^2 + (z_i-z)^2}$, and the
reference length and rest length of each SLS is denoted $\bar L_i$ and $\bar L^0_i$ respectively.

### [app-1d_sls_systems-p2] paragraph

We assume a temporal scale separation between the fast elastic time-scale and the slow viscoelastic time
shared by all the springs, and that no external time scale enters the problem. We may thus reduce the problem
to studying the quasi static evolution of the system in which every configuration the system assumes minimizes
the instantaneous elastic energy that in turn depends on the slowly evolving reference lengths $\bar L_i$,

\[ E(z) = \sum_{i=1}^N \frac{1}{2} k_i \left(L_i-\bar L_i\right)^2. \]

(??)

In this quasi-static limit the force on the point mass vanishes

\[ \begin{align*}
                        0 = F(z) & = -\frac{d E}{d z} = -\sum_{i=1}^N k_i \frac{dL_i}{dz} \left(L_i-\bar
L_i\right).  \tag{??}\end{align*} \]

The rest length $\bar L_i$ change in time and, as in the case of the Von-Mises truss, could change the shape
of the instantaneous elastic energy. For example they could cause an unstable state to become stable through
viscoelastic relaxation. Such states with acquired stability in viscoelastic systems were first identified in
the context of creep buckling [23, 22], and revisited recently where this phenomenon was termed temporary
bistability [11] or pseudo bistability [12], as these states were observed numerically to always lose their
stability.

### [app-1d_sls_systems-p3] paragraph

In order to analyze the dynamic of the system, we differentiate the force Eq. ?? in time, and use Eq. ??:

\[ \begin{align*}
                        \frac{d^2 E}{dz^2} \dot z & = \sum_{i=1}^N k_i \frac{dL_i}{dz} \dot {\bar L}_i
                        & = \frac{1}{\tau} \sum_{i=1}^N k_i \frac{dL_i}{dz}
                        \left( L_i - \bar L_i - (1-\b)\left(L_i-\bar L_i ^0\right)\right)
                \end{align*} \]

Substitution of Eq. ?? gives

\[ \frac{d^2 E}{dz^2} \dot z = \frac{1-\b}{\tau} F^0(z), \]

(??)

where $F^0(z)=-\sum_{i=1}^N k_i \frac{dL_i}{dz} \left(L_i-\bar L_i^0\right)$ is the force on the mass at $z$,
with respect to reference lengths that equal the rest lengths, $\bar L_i = \bar L_i^0$. We thus obtained that
when the point mass is in a convex region of the potential ($\frac{d^2 E}{dz^2}>0$), $z$ changes continuously
and the sign of $\dot z$ remains the same as the sign of the force in the rest elastic system $F^0(z)$. When
the second derivative vanishes $\frac{d^2 E}{dz^2}=0$ the system loses its transient elastic stability, and
snaps to another stable point.

### [app-1d_sls_systems-p4] paragraph

Immediate result of Eq. ?? is that stationary states of Eqs. ?? and ?? are all extremal points of the rest
elastic system’s potential. That is assuming both $\dot z =0$ and $\dot{\bar L}_i=0$ implies $F^0(z)=0$. This
result agrees with the phenomenology of the von-Mises truss described above. Both the unstable and the
finitely stable cases eventually result in the original position - stable point of the rest elastic system.
The stable phase satisfy the claim trivially, by staying stable from the very rest. We have thus also shown
that in general, any acquired stability (initially non extremal point that has become stable), will eventually
result in a snap 2.

### [app-1d_sls_systems-p5] paragraph

The sign of $\dot z$ in Eq. ?? is independent of the reference lengths. Thus, mass left on a stable point of
the rest elastic system $F^0(z)=0$ will remain static, although all the reference length $\bar L_i$ will
continue to change. Intuitively, this phenomenon occurs because the relaxation takes the same force fraction
of each SLS over time, preserving the vanishing total force on the point mass. One only need to check whether
$\frac{d^2 E(t)}{dz^2}>0$ during the relaxation. The second derivative reads

\[ \frac{d^2 E(t)}{dz^2} = \sum_{i=1}^N k_i \frac{d^2L_i}{dz^2} \left(L_i-\bar L_i(t)\right) + \sum_{i=1}^N k_i \left(\frac{dL_i}{dz}\right)^2 \]

(??)

Assuming the point to be at rest $\bar L_i = \bar L_i^0$ at $t=0$, and taking constant $z$ and $L_i$’s, Eq. ??
gives

\[ \bar L_i(t) = \left( 1- B(t)\right) \bar L_i^0 + B(t) L_i, \]

where $B(t)= \b \left(1-e^{-\nicefrac t \tau}\right)$. Thus

\[ \frac{d^2 E(t)}{dz^2} = \left( 1- B(t)\right) \frac{d^2 E(t=0)}{dz^2} + B(t) \sum_{i=1}^N k_i \left(\frac{dL_i}{dz}\right)^2 \]

(??)

Because $0<B(t)<1$ for all $t>0$ we get that if the position was stable at rest $\frac{d^2 E(t=0)}{dz^2}>0$ it
would indeed remain stable for any $t>0$. We have therefore obtained that stable points of the rest elastic
system are also static, when arrived to directly from rest.

### [app-1d_sls_systems-p6] paragraph

By considering the SLS as a spring with dynamic reference length we were able to show explicitly that the
results obtained for the Von-Mises truss SLS system are in fact rather general and in particular apply even
when the system display multiple metastable states and is comprised of many springs of different stiffnesses
provided their $\b$ and $\tau$ values coincide.
