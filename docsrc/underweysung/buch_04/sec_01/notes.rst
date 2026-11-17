:layout: book
:canonical_id: IV.29–43
:breadcrumb_title: IV.29–43
:order: 1
:type: section
:folio: N1525 p. 142–157
:tracks: English: index | German: de | Summary: summary | Notes: notes
:featured_image: /_static/figures/book4_platonic_nets.svg

.. _buch_04-sec_01-notes:

Notes — Combinatorics & Topology of Dürer's Polyhedral Nets
===========================================================

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
