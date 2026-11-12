==========================================================================
Notes — Book I: Descriptive Geometry & the *Eierlini* Symmetry Proof
==========================================================================

1. Birth of Two-View Descriptive Geometry (270 Years Before Monge)
==================================================================

Before :person:`Gaspard Monge's <monge>` *Géométrie descriptive* (:cite:`monge:1799`), stonecutters
and architects knew empirical plan-and-elevation templates, and :person:`Piero della Francesca <piero>`
applied coupled projections to human heads in *De prospectiva pingendi*. Yet Book I, Figures
34–37 of Dürer's 1525 *Underweysung* represent the **first printed mathematical application of
coupled orthographic elevation and ground-plan views to determine the true metric locus of
curved three-dimensional sections**.

2. Exact Algebraic Resolution of Dürer's *Eierlini* Paradox
===========================================================

Why did Dürer translate Apollonius's *ellipsis* as :term:`Eierlini <eierlini>` ("egg-line", *"darumb
das sie schyer einem ey gleich ist"*) and draw his 1525 woodcut Fig. 34 slightly narrower at the
upper end near the cone's apex?

Let us evaluate **Dürer's own 12-station algorithm** symbolically in ``geometor.durer``
(:func:`~geometor.durer.conics_perspective.construct_durer_conic_sections`). Take a right circular
cone of base radius $R = 6$ and height $H = 12$, so at height $z \in [0, 12]$ the horizontal
circular cross-section has radius

$$r(z) = \frac{12 - z}{2}.$$

Slice the cone obliquely along segment $fg$ from $F = (-4, 4)$ on the left generator to
$G = (2, 8)$ on the right generator, divided into 12 equal parts $k = 0, 1, \dots, 12$:

$$x_k = -4 + \frac{k}{2}, \qquad z_k = 4 + \frac{k}{3}, \qquad r_k = 4 - \frac{k}{6}.$$

In the circular ground plan (*Grundriss*), the vertical projector at $x_k$ cuts the horizontal
section circle $x^2 + y^2 = r_k^2$ in a chord of exact half-width $w_k$:

$$w_k^2 = r_k^2 - x_k^2 = \left(4 - \frac{k}{6}\right)^2 - \left(-4 + \frac{k}{2}\right)^2
= \left(16 - \frac{4}{3}k + \frac{k^2}{36}\right) - \left(16 - 4k + \frac{k^2}{4}\right)
= \frac{2}{9}\,k\,(12 - k).$$

Hence for every station $k \in \{0, 1, \dots, 12\}$:

$$w_k = \frac{\sqrt{2\,k\,(12 - k)}}{3} = w_{12 - k}!$$

**Dürer's geometric construction rule is 100% exact and strictly symmetric** under $k \mapsto 12 - k$!
Because $|FG| = \sqrt{6^2 + 4^2} = 2\sqrt{13}$, the curve is a true Apollonian ellipse with
semi-major axis $a = \sqrt{13}$, semi-minor axis $b = w_6 = 2\sqrt{2}$, focal distance
$c = \sqrt{a^2 - b^2} = \sqrt{5}$, and eccentricity $e = \frac{\sqrt{65}}{13}$.

Why then did Dürer suspect asymmetry? In the **ground plan** (*der grund zum kegell*), the
upper half of the cutting plane ($k = 7, \dots, 12$) crosses directly over the cone's apex
projection $O_{\text{plan}} = (0, 0)$ at $k = 8$ ($x_8 = 0$), crowding the upper concentric
circles tightly around the center, whereas near $k = 1, 2, 3$ the arcs sweep broadly near the rim!
A slight compass transfer error on the crowded upper circles immediately pinches the top of the
plotted curve into an egg shape—an optical and draftsmanship trap definitively resolved by
:person:`Johannes Kepler <kepler>` in Chapter IV of *Ad Vitellionem Paralipomena*
(:cite:`kepler:1604`).

3. Exact Polar Stations of the 12-Sector Spiral over $\mathbb{Q}(\sqrt{3})$
===========================================================================

Because $\cos(k \cdot 30^\circ), \sin(k \cdot 30^\circ) \in \left\{0, \pm\frac{1}{2}, \pm\frac{\sqrt{3}}{2}, \pm 1\right\}$
for every integer $k$, all 25 stations of Dürer's two-turn 12-sector Archimedean spiral
$P_k = \left(\frac{k}{2}\cos\frac{k\pi}{6},\, \frac{k}{2}\sin\frac{k\pi}{6}\right)$ belong
entirely to the quadratic field $\mathbb{Q}(\sqrt{3})$, requiring zero floating-point evaluation
in ``geometor.model``.
