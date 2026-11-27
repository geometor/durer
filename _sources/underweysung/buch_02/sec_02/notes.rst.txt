:layout: book
:canonical_id: II.9–20
:breadcrumb_title: II.9–20
:order: 2
:type: section
:folio: N1525 p. 057–061
:tracks: English: index | German: de | Summary: summary | Notes: notes
:featured_image: /_static/figures/book2_durer_vs_euclid_pentagon.svg

.. _buch_02-sec_02-notes:

Notes — Algebraic Audit of Dürer's Pentagon, Heptagon & 1525 Errata
===================================================================

1. Exact Radical Audit of Dürer's Rusty-Compass Pentagon (Fig. 16)
==================================================================

Why did :person:`Dürer <durer>` present *two* pentagon constructions back-to-back on pages 058–059
(Figs. 15 and 16)? While Figure 15 gives :person:`Ptolemy's <ptolemy>` exact golden-ratio chord
over :math:`\mathbb{Q}(\phi)`, Figure 16 requires **never changing the compass opening** (*auß
vnuerruckten zirckel*)—a classic medieval stonemasons' and Islamic workshop protocol going back to
:person:`Abū al-Wafāʾ <abu-l-wafa>` (:cite:`abulwafa:craftsmen`) and :person:`Matthäus Roriczer
<roritzer>` (:cite:`roritzer:1487`), which :person:`Hermann Staigmüller <durer>` (:cite:`staigmuller:1891`)
and :person:`Émile Lemoine <lemoine>` (:cite:`lemoine:1902`) celebrated as a milestone of
constructive simplicity.

In :func:`~geometor.durer.polygons.construct_durer_vs_euclid_pentagon`, let the given base be
:math:`A = (0, 0)` and :math:`B = (1, 0)` with fixed unit aperture :math:`R = 1`:

- The vesica intersections are :math:`C = \left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)` and
  :math:`D = \left(\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)`.
- The third unit circle centered at :math:`D` meets :math:`\bigcirc(A, 1)` at
  :math:`E = \left(\frac{1}{2} - \frac{\sqrt{3}}{2},\, -\frac{\sqrt{3}}{2} + \frac{1}{2}\right)` and
  meets the vertical axis :math:`CD` at :math:`G = \left(\frac{1}{2},\, 1 - \frac{\sqrt{3}}{2}\right)`.
- Ray :math:`EG` has slope :math:`m = \frac{1}{\sqrt{3}}(2 - \sqrt{3})`? Let us read off :math:`\Delta x = \frac{\sqrt{3}}{2}` and :math:`\Delta y = \frac{1}{2}`, so ray :math:`EG` makes an exact :math:`30^\circ` **angle**
  with the horizontal! Intersecting ray :math:`EG` with :math:`\bigcirc(B, 1)` yields the closed-form nested
  quadratic coordinates of vertex :math:`H_{\text{Dürer}}`:

.. math::

   H_{\text{Dürer}} = \left(\frac{5}{8} + \frac{\sqrt{3}\,\sqrt{6\sqrt{3} - 4}}{8},\;
   -\frac{\sqrt{3}}{2} + \frac{7}{8} + \frac{\sqrt{6\sqrt{3} - 4}}{8}\right),

and by bilateral reflection :math:`I_{\text{Dürer}} = (1 - x_H, y_H)`. Stepping unit circles from
:math:`I_{\text{Dürer}}` and :math:`H_{\text{Dürer}}` closes at apex :math:`K_{\text{Dürer}} = \left(\frac{1}{2}, y_K\right)`.

Symbolic verification in ``geometor.durer`` proves:

1. **100% Exact Equilateral Side Quadrances**: Every edge :math:`AB, BH_{\text{Dürer}}, H_{\text{Dürer}}K_{\text{Dürer}}, K_{\text{Dürer}}I_{\text{Dürer}}, I_{\text{Dürer}}A` has exact quadrance :math:`Q = 1`.
2. **Non-Equiangularity (+21.97 Arcminutes)**: Whereas Euclid's :math:`\mathbb{Q}(\phi)` pentagon has all
   five interior angles equal to :math:`108^\circ` (interior line spread :math:`s = \frac{5 + \sqrt{5}}{8}`),
   Dürer's pentagon has interior angles:

   - At base vertices :math:`A, B`: :math:`108.36612^\circ` (:math:`+0.36612^\circ = +21.97'` too wide),
   - At shoulder vertices :math:`I_{\text{Dürer}}, H_{\text{Dürer}}`: :math:`107.03899^\circ` (:math:`-57.66'`),
   - At apex :math:`K_{\text{Dürer}}`: :math:`109.18978^\circ` (:math:`+1^\circ 11.39'`).

Within twenty-five years of Dürer's book, :person:`Lodovico Ferrari <ferrari>` and
:person:`Gerolamo Cardano <cardano>` proved that **even the exact** :math:`\mathbb{Q}(\phi)` **pentagon can
be constructed with straightedge and a single fixed compass opening**, albeit requiring many more
circles than Dürer's ultra-fast five-circle workshop layout.

2. Eisenstein Irreducibility & Residual of the Workshop Heptagon (Figs. 11 & 15)
================================================================================

For a regular heptagon inscribed in the unit circle :math:`R = 1`, setting :math:`\theta = \frac{2\pi}{7}` gives
chord quadrance :math:`q = 4\sin^2\frac{\pi}{7} = 2 - 2\cos\frac{2\pi}{7}`. Since :math:`2\cos\theta` satisfies
:math:`t^3 + t^2 - 2t - 1 = 0`, substituting :math:`t = 2 - q` yields the minimal polynomial of the regular
heptagon's side quadrance (:func:`~geometor.durer.polygons.construct_durer_heptagon_workshop`):

.. math::

   P_7(q) = q^3 - 7q^2 + 14q - 7 = 0.

By **Eisenstein's criterion** at the prime :math:`p = 7` (:math:`7 \mid -7, 14, -7` and :math:`7^2 \nmid -7`),
:math:`P_7(q)` is **irreducible over** :math:`\mathbb{Q}` of degree :math:`3 \neq 2^k`. By the **Gauss–Wantzel
theorem** (:person:`Gauss <gauss>` :cite:`gauss:1801`; :person:`Wantzel <wantzel>`
:cite:`wantzel:1837`), no unmarked ruler-and-compass construction can ever construct :math:`q_{\text{exact}} \approx 0.753020396`, vindicating Dürer's explicit *Mechanice* label! Evaluating :math:`P_7` at Dürer's
half-equilateral quadrance :math:`Q_{\text{Dürer}} = \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{3}{4}`
gives the extraordinarily tiny exact rational residual:

.. math::

   P_7\!\left(\frac{3}{4}\right) = \frac{27}{64} - \frac{63}{16} + \frac{21}{2} - 7 = -\frac{1}{64},

corresponding to a relative chord error of :math:`-0.2008\%` (less than :math:`0.2\text{ mm}` on a
:math:`100\text{ mm}` radius circle!). Similarly, Dürer's hendecagon rule :math:`s_{11} = \frac{9}{16}R = 0.5625\,R` misses :math:`2\sin\frac{\pi}{11} \approx 0.563465\,R` by just :math:`-0.1713\%`.

Philological Note on the 1525 Errata (SLUB N1525 p. 182)
---------------------------------------------------------
In the 1525 first printing of p. 058 (Fig. 15), the typesetter omitted the clause bisecting ``a.c.``
at ``e`` before drawing segment ``e.d.``, and the woodblock cutter omitted line ``d.e.`` inside the
first circle. Dürer caught this himself on the final Errata leaf (p. 182): *"Im .E. am vierten plat
in der fünftzeheten figur im ersten cirkel soll .d.e. mit einer lini zusamen gezogen werden."*
