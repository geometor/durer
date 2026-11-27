====================================================================
26.112 — Initial Bilingual Codex & Exact Symbolic Engine (`v0.1.0`)
====================================================================

Established the complete ``geometor-durer`` repository for Albrecht Dürer's *Underweysung der
Messung, mit dem Zirckel un[d] Richtscheyt, in Linien Ebnen unnd gantzen Corporen* (Nuremberg,
1525; 2nd ed. 1538; Camerarius Latin ed. 1532):

- **4-Track Bilingual Digital Scriptorium Codex** (``docsrc/underweysung/``) pairing an original
  GEOMETOR English translation directly from the 1525 Nuremberg Early New High German (`English`)
  with the diplomatic SLUB Dresden `PPN 27778509X` copy-text (`German (1525)`), structural
  digests (`Summary`), and mathematical commentary (`Notes`) across all Four Books.
- **Exact Symbolic Engine** (``src/geometor/durer/``) built on ``SymPy`` and ``geometor.model``
  with zero floating-point coordinates:

  1. Book I 12-sector Archimedean spiral over :math:`\mathbb{Q}(\sqrt{3})` and two-view descriptive
     geometry of conic sections proving :math:`w_k = \frac{\sqrt{2k(12-k)}}{3}` (:math:`w_{12-k} = w_k`).
  2. Book II direct comparison of Dürer's single-aperture ("rusty compass") pentagon (:math:`Q = 1`,
     base angle :math:`108.3661^\circ`, :math:`+21.97'` error) against Euclid's :math:`\mathbb{Q}(\phi)` pentagon,
     plus Eisenstein cubic residual :math:`P_7(\frac{3}{4}) = -\frac{1}{64}` for the workshop heptagon
     and :math:`\pi_{\text{Dürer}} = \frac{25}{8} = 3.125`.
  3. Book III Roman *Antiqua* capitals ``A``, ``O``, ``Q`` inside the :math:`10 \times 10` square and
     modular Gothic *Textura* minuscules ``i, n, m``.
  4. Book IV planar fold-out nets for the Tetrahedron, Cube, Octahedron, Dodecahedron (double
     pentagonal rosette over :math:`\mathbb{Q}(\sqrt{5}, \sin 36^\circ)`), Icosahedron, and
     Cuboctahedron, plus central perspective cube projection (:math:`\operatorname{CR} = -1`) and
     Delian cube duplication (:math:`c^3 = 2 g^3`).

- **11 Theme-Adaptive ``.euclid-graphic`` SVGs** and 4 runnable scripts in ``demos/``.
