==========================================================================
Notes — Book IV: Combinatorics of Dürer's Nets, $\sqrt[3]{2}$ & Projectivity
==========================================================================

1. Exact Algebraic & Topological Audit of Dürer's Polyhedral Nets
=================================================================

Book IV (pp. 142–157) marks a watershed between :person:`Luca Pacioli's <pacioli>` *Divina
Proportione* (:cite:`pacioli:1509`)—where :person:`Leonardo da Vinci <leonardo>` rendered polyhedra
as perspective wooden frames—and :person:`Johannes Kepler's <kepler>` *Harmonices Mundi* Book II
(:cite:`kepler:1619`), which completed the enumeration of all thirteen Archimedean solids.

In ``geometor.durer`` (:func:`~geometor.durer.polyhedra.construct_durer_polyhedral_nets`), every
unfolded planar net is modeled as a connected spanning tree of exact regular polygons with **unit
edge quadrance $Q = 1$** across three nested number fields:

- **Cube** ($F = 6, E = 12, V = 8$): pure rational lattice $\mathbb{Q}$, $5$ interior fold hinges +
  $14$ open cut boundary edges ($5 + \frac{14}{2} = 12$ edges in 3D).
- **Tetrahedron** ($4, 6, 4$), **Octahedron** ($8, 12, 6$), **Icosahedron** ($20, 30, 12$), and
  **Archimedean Cuboctahedron** ($14, 24, 12$): quadratic field $\mathbb{Q}(\sqrt{3})$, verified to
  have pairwise disjoint face interiors (``non_overlapping_verified = True``, zero self-overlap—an
  early constructive witness to **Dürer's Conjecture** on edge-unfolding convex polyhedra!).
- **Regular Dodecahedron** ($12, 30, 20$, Fig. 33): cyclotomic golden-ratio field
  $\mathbb{Q}(\sqrt{5}, \sin 36^\circ) = \mathbb{Q}\!\left(\sqrt{5},\, \frac{\sqrt{10 - 2\sqrt{5}}}{4}\right)$,
  unfolded into two six-pentagon rosettes joined across a shared hinge ($11$ interior fold hinges +
  $38$ open cut edges $\implies 11 + \frac{38}{2} = 30$ edges, Euler characteristic
  $\chi = V - E + F = 20 - 30 + 12 = 2$).

Philological Note on Figure 35 (Truncated Tetrahedron, SLUB N1525 p. 149)
-------------------------------------------------------------------------
On page 149, introducing the first semi-regular solid (Truncated Tetrahedron, `[3.6.6]`), Dürer's
1525 prose inadvertently reads *"vier sechs ecketter vnd **drey** dryangletter ebner felder"* ("four
hexagonal and *three* triangular plane faces"), even though he immediately states the true 3D counts
(*zwelf eck vnnd achtzehen scharpfer seyten*: $V = 12, E = 18 \implies F = 2 - 12 + 18 = 8$) and his
own woodcut Figure 35 accurately draws **four hexagons and four triangles**! :person:`Joachim
Camerarius <camerarius>` silently restored *quatuor triangulis* in the 1532 Latin edition
(:cite:`durer:1532:camerarius`), and Dürer's posthumous 1538 edition (:cite:`durer:1538`) added two
further Archimedean truncations (bringing Dürer's total to nine of Archimedes's thirteen solids).

2. Two Mean Proportionals & Wantzel's Cubic Impossibility
=========================================================

In **Plato's mechanical carpenter's square** (Fig. 50, p. 163), setting right-angled legs $gb = g$
and $be = e$ along orthogonal axes with right angles at $c = (0, c)$ and $d = (-d, 0)$ forces
altitude-on-hypotenuse similarity (Euclid VI.8) in $\triangle gcd$ and $\triangle cde$:

$$\frac{g}{c} = \frac{c}{d} = \frac{d}{e} \implies c^2 = gd, \quad d^2 = ce \implies c^3 = g^2 e.$$

Taking $g = 1$ and $e = 2$ yields $c = \sqrt[3]{2}$ and $d = \sqrt[3]{4}$, so $\operatorname{Vol}(c)
/ \operatorname{Vol}(g) = c^3 / g^3 = 2$ identically! Because $x^3 - 2$ is irreducible over
$\mathbb{Q}$ of degree $3 \neq 2^k$, :person:`Pierre Laurent Wantzel <wantzel>` (:cite:`wantzel:1837`)
and :person:`Felix Klein <klein>` (:cite:`klein:1895`) proved why all three of Dürer's Book IV
constructions (**Sporus's** graduated ruler, **Plato's** sliding square, and **Hero's** pivoting
straightedge) necessarily employ **neusis or mechanical linkage** beyond unmarked straightedge and
compass.

3. Homogeneous Central Projection & Cross-Ratio Invariance
==========================================================

In :func:`~geometor.durer.conics_perspective.construct_durer_perspective_apparatus`, let the artist's
fixed :term:`eye point <augpunct>` be $E = (-12, 3, 5)$ looking orthogonally toward the vertical
glass picture frame $x = 0$ (principal vanishing point $V_x = (3, 5)$ on the glass, focal distance
$f = 12$). Every vertex $P = (X, Y, Z) \in \mathbb{Q}^3$ projects along rectilinear sight-ray $EP$
to exact rational picture-plane coordinates:

$$u(P) = 3 + \frac{12\,(Y - 3)}{X + 12}, \qquad v(P) = 5 + \frac{12\,(Z - 5)}{X + 12}.$$

For the cube $[4, 8] \times [-2, 2] \times [0, 4]$:

1. **Exact Convergence at the Principal Vanishing Point**: All four receding depth edges
   $A'E', B'F', C'G', D'H'$ intersect on the picture plane at the single point $V_x = (3, 5)$—corresponding
   to the ideal point at infinity $(1 : 0 : 0 : 0) \in \mathbb{P}^3(\mathbb{Q})$.
2. **Foreshortening & Harmonic Cross-Ratio ($\operatorname{CR} = -1$)**: Along the lower-left depth
   edge from $A = (4, -2, 0)$ to $E_{\text{back}} = (8, -2, 0)$, the true 3D midpoint
   $M = (6, -2, 0)$ projects to $M' = \left(-\frac{1}{3},\, \frac{5}{3}\right)$, which is strictly
   closer to the back corner $E' = (0, 2)$ than to the front corner $A' = \left(-\frac{3}{4},\,
   \frac{5}{4}\right)$—yet its **projective cross-ratio** with vanishing point $V_x = (3, 5)$ (the
   harmonic fourth of the midpoint and ideal point at infinity, cf. ``geometor/pappus``
   :cite:`pappus:synagoge`) is preserved with 100% symbolic exactness:

   $$\operatorname{CR}(A', E';\, M', V_x)
   = \frac{(u_{A'} - u_{M'})\,(u_{E'} - u_{V_x})}{(u_{A'} - u_{V_x})\,(u_{E'} - u_{M'})}
   = \frac{\left(-\frac{3}{4} + \frac{1}{3}\right)(0 - 3)}{\left(-\frac{3}{4} - 3\right)\left(0 + \frac{1}{3}\right)}
   = \frac{\left(-\frac{5}{12}\right)(-3)}{\left(-\frac{15}{4}\right)\left(\frac{1}{3}\right)}
   = -1.$$
