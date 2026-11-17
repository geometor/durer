:layout: book
:canonical_id: IV.52–63
:breadcrumb_title: IV.52–63
:order: 3
:type: section
:folio: N1525 p. 166–182
:tracks: English: index | German: de | Summary: summary | Notes: notes
:featured_image: /_static/figures/book4_perspective_cube_apparatus.svg

.. _buch_04-sec_03-notes:

Notes — Homogeneous Central Projection & Cross-Ratio Invariance
===============================================================

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
