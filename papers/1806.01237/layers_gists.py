# One line per node (sections, figures, paragraphs), at most 20 words, stating the node's claim or its role.
# Drafted from the text; status ai-draft for all. No gist for the acknowledgements, the footnotes, the references and
# the empty paragraph sec-transient_stability_loss-p4 (the source has a commented-out experimental section there).
GIST = {
    # ---- Introduction
    "section-I": r"Rewriting viscoelasticity as elasticity about evolving reference lengths turns the stability of creeping solids into simple rules.",
    "section-I-p1": r"Elastomers creep and relax stress reversibly, yet keep their topology and a finite fraction of stress indefinitely.",
    "section-I-p2": r"In delayed stability loss a slow creep precedes a fast snap: Venus fly-traps, jumping poppers, some earthquakes.",
    "section-I-p3": r"Memory-kernel laws simulate well but explain little; relaxation seems bound to stabilize, which makes viscoelastic instabilities puzzling.",
    "section-I-p4": r"Plan of the one-dimensional part: the standard linear solid as an evolving spring, a truss, general 1D claims.",
    "section-I-p5": r"Plan of the continuum part: a covariant metric description, then claims for isotropic incompressible bodies.",

    # ---- 1D
    "sec-1d_viscoelasticity": r"In one dimension, evolving rest lengths explain when a truss of viscoelastic springs acquires and then loses stability.",
    "fig-sls_diagram": r"The standard linear solid: a spring in parallel with a spring and dashpot in series.",
    "section-II-A": r"A standard linear solid is a spring of fixed stiffness whose reference length relaxes towards its current and rest lengths.",
    "section-II-A-p1": r"The SLS force is $-k(L-\bar L)$; $\bar L$ relaxes towards $L$ and $\bar L^0$, weighted by $\beta$, the asymptotically relaxed force fraction.",
    "fig-sls_von_mises_truss_diagram": r"The truss: a mass on a line, two diagonal SLS elements making it bistable, a vertical one breaking symmetry.",
    "sec-sls_von_Mises_truss": r"Holding a viscoelastic truss inverted gives three phases: never bistable, always bistable, or bistable for a while.",
    "sec-sls_von_Mises_truss-p1": r"The truss's energy is the squared distance between the reference point and the curve of admissible lengths.",
    "sec-sls_von_Mises_truss-p2": r"While the truss is held, the reference point moves straight towards the held lengths; equilibria are feet of normals.",
    "fig-sls_von_mises_truss_lengths_space": r"The plane of lengths for three values of $\alpha$: unstable, finitely stable and stable phases.",
    "sec-sls_von_Mises_truss-p3": r"With a stiff vertical spring the truss stays monostable throughout and snaps back on release.",
    "sec-sls_von_Mises_truss-p4": r"With a soft vertical spring the truss is bistable from the start, and relaxation only deepens the inverted state.",
    "sec-sls_von_Mises_truss-p5": r"A stable state reached abruptly from rest never moves, because the reference point slides along a line towards it.",
    "sec-sls_von_Mises_truss-p6": r"At intermediate stiffness the stability acquired while held must be lost: no inverted state is stable at rest.",
    "sec-sls_von_Mises_truss-p7": r"Rest-stable states never destabilize; states that lose stability had acquired it, and acquired stability is eventually lost.",

    # ---- Metric linear viscoelasticity
    "sec-metric_linear_viscoelasticity": r"A continuum is elastic at each instant about a slowly evolving reference metric, the analogue of the reference length.",
    "sec-metric_linear_viscoelasticity-p1": r"Continuous bodies need an infinitesimal reference length: a metric tensor.",
    "sec-viscoelastic_continuum": r"Linear viscoelasticity defines a reference metric that fast deformations leave unchanged: the material's slow state variable.",
    "sec-viscoelastic_continuum-p1": r"Sets up configuration metric, rest reference metric, strain and stress; linear viscoelasticity adds a fading memory kernel.",
    "sec-viscoelastic_continuum-p2": r"The reference metric, defined by elastic stress in $g-\bar g$, is unchanged by fast deformations: the slow state variable.",
    "sec-quasi_static_approximation": r"Because relaxation is slow, the body always minimizes its instantaneous elastic energy about the drifting reference metric.",
    "sec-quasi_static_approximation-p1": r"With fast elasticity, the configuration minimizes the instantaneous elastic energy; generalized forces vanish and the Hessian is positive.",
    "sec-quasi_static_approximation-p2": r"The shape tracks the closest admissible metric while the reference metric drifts from rest towards recent configurations.",
    "sec-delayed_stability_and_loss": r"Holding a continuum in an unstable shape can make it transiently stable; that acquired stability is later lost.",
    "sec-delayed_stability_and_loss-p1": r"Continua, like the truss, can acquire stable states through relaxation that cannot always last.",
    "sec-delayed_stability_and_loss-p2": r"A body held in an unstable shape may be stable when released: acquired stability.",
    "sec-delayed_stability_and_loss-p3": r"Acquired stability ends in delayed stability loss, a creep then a snap; both are expected near multistability.",
    "section-III-D": r"Isotropy and homogeneity must refer to a metric; taking the rest metric gives a two-function memory kernel.",
    "section-III-D-p1": r"Isotropy is invariance under the rotations of some metric on the body, which must be specified.",
    "section-III-D-p2": r"The stiffness is taken isotropic about the rest metric, set by the material's composition, not the instantaneous one.",
    "section-III-D-p3": r"Homogeneity is a matter of measure: constant stiffness means equal energy per initial volume.",
    "section-III-D-p4": r"Isotropic homogeneous kernels reduce to a scalar part $\beta\phi$ and a part $\psi$ mixing the metric's components.",

    # ---- Incompressible materials
    "sec-scalar_viscoelasticity": r"For incompressible solids, stable shapes reached from rest never evolve, and only acquired stability can be lost.",
    "section-IV-A": r"Incompressibility makes the kernel scalar, so the reference metric relaxes towards a fixed mix of current and rest metrics.",
    "section-IV-A-p1": r"Incompressibility removes $\psi$; at stationarity $\bar g^{\rm stat}_{ij}=\beta g_{ij}+(1-\beta)\bar g^0_{ij}$, with $\beta$ the relaxed stress fraction.",
    "section-IV-A-p2": r"Long-time stability depends only on $\beta$; the exponential SLS kernel suffices to discuss it.",
    "fig-metric_space": r"Realized metrics are the admissible ones closest to the reference metric, which moves along a line from rest.",
    "sec-stationary_states": r"Stationary configurations are rest-system extremals, and rest-stable configurations reached abruptly from rest stay exactly still.",
    "sec-stationary_states-p1": r"Stationary forces are $(1-\beta)$ times the rest system's, so every stationary configuration is an extremal of the rest system.",
    "sec-stationary_states-p2": r"Relaxation adds a positive term to the Hessian: rest-stable configurations are stationary, and rest saddles may stabilize indefinitely.",
    "sec-stationary_states-p3": r"Deformed abruptly from rest into a stable shape, a body never moves: its elastic strain shrinks uniformly.",
    "sec-stationary_states-p4": r"The proof needs a scalar metric kernel, so it holds for incompressible solids and approximately near incompressibility.",
    "sec-stationary_states-p5": r"Both claims reflect collinearity: from rest, the reference metric moves on the line towards the configuration metric.",
    "sec-transient_stability_loss": r"Only shapes unstable at rest can lose stability, and acquired stability away from rest extremals must end.",
    "sec-transient_stability_loss-p1": r"An inverted, suitably cut jumping popper creeps for seconds then snaps back, like the intermediate-stiffness truss.",
    "sec-transient_stability_loss-p2": r"Stability can be lost only if it was acquired, so a popper that snaps late had been relaxed while inverted.",
    "sec-transient_stability_loss-p3": r"Acquired stability of a configuration that is not a rest extremal must end: such a popper always snaps back.",
    "fig-hopper_popper": r"Poppers and the hold-release protocol; simulated flip times mark stable, acquired-stability and unstable ranges of cone thickness.",

    # ---- Summary and discussion
    "section-V": r"Relaxation does stabilize states reached from rest; instabilities need acquired stability and a curved set of admissible shapes.",
    "section-V-p1": r"The naive intuition holds: a metastable state reached abruptly from rest never loses stability or moves.",
    "section-V-p2": r"Only states unstable about the rest metric that acquired stability can snap, and that acquired stability cannot last.",
    "section-V-p3": r"Delayed instabilities need a curved set of admissible states; in continua relaxation can also leave residual stress.",
    "section-V-p4": r"Letting the rest metric evolve could give a covariant theory of growth and plasticity, not yet tested.",

    # ---- Appendix
    "app-1d_sls_systems": r"For any SLS assembly on a line sharing $\beta$ and $\tau$, rest-stable states stay still and acquired stability ends.",
    "app-1d_sls_systems-p1": r"Sets up a mass on a line tied by SLS elements, sharing $\beta$ and $\tau$, to fixed points.",
    "app-1d_sls_systems-p2": r"Quasi-statically the force vanishes; acquired stability, known from creep buckling, was always lost in simulations.",
    "app-1d_sls_systems-p3": r"While stable, the mass creeps in the direction of the rest system's force; it snaps when stiffness vanishes.",
    "app-1d_sls_systems-p4": r"Stationary states are rest-system extremals, so acquired stability at a non-extremal point ends in a snap.",
    "app-1d_sls_systems-p5": r"A rest-stable point reached from rest stays static: relaxation removes the same force fraction from every element.",
    "app-1d_sls_systems-p6": r"The truss results hold for many springs of different stiffness and multiple metastable states, given common $\beta,\tau$.",
}
