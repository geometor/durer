:order: 25
:nav_title: Demos

=====
Demos
=====

.. rubric:: Exact Symbolic Demonstrations in Python & SymPy

All executable Python constructions for Albrecht Dürer's *Underweysung der Messung* live
cleanly outside the historical codex in ``demos/`` and ``src/geometor/durer/``. Every
:class:`~geometor.model.Model` instance runs with ``auto_intersect=False`` and 100% exact
``SymPy`` coordinates over :math:`\mathbb{Q}`, :math:`\mathbb{Q}(\sqrt{2})`, :math:`\mathbb{Q}(\sqrt{3})`,
:math:`\mathbb{Q}(\phi)`, and :math:`\mathbb{Q}(\sqrt{5}, \sin 36^\circ)`.

1. Book I — Spirals & Two-View Conic Sections
=============================================

Constructs Dürer's 12-sector Archimedean spiral (*Schneckenlini*) over :math:`\mathbb{Q}(\sqrt{3})`
and verifies his 12-station descriptive-geometry transfer law
:math:`w_k = \frac{\sqrt{2k(12 - k)}}{3}` for the right circular cone, proving exact bilateral
symmetry :math:`w_{12-k} = w_k` (*Elipsis* vs. *Eierlini*).

.. literalinclude:: ../../demos/conics_and_spirals.py
   :language: python
   :linenos:

2. Book II — Pentagon, Heptagon & Quadrature Audit
==================================================

Constructs both Dürer's single-aperture ("rusty compass") pentagon and Euclid's :math:`\mathbb{Q}(\phi)`
regular pentagon on shared base :math:`AB`, proving exact unit side quadrances :math:`Q = 1` and quantifying
the :math:`+21.97'` base-angle discrepancy, alongside the Eisenstein cubic residual
:math:`P_7\left(\frac{3}{4}\right) = -\frac{1}{64}` for the workshop heptagon and :math:`\pi_{\text{Dürer}} = \frac{25}{8}`.

.. literalinclude:: ../../demos/pentagon_and_heptagon_audit.py
   :language: python
   :linenos:

3. Book III — Roman *Antiqua* Capitals & Modular *Textura*
==========================================================

Constructs Roman capitals ``A``, ``O``, and ``Q`` inside the :math:`10 \times 10` square (*rechte
Fierung*) with :math:`1 : \frac{1}{3}` stroke contrast, circular serif fillets (:math:`r = \frac{10}{7}, \frac{1}{2}`),
and shifted-diagonal bowls (:math:`r = 5 - \frac{\sqrt{2}}{4}`), paired with modular Gothic *Textura*
minuscules ``i, n, m``.

.. literalinclude:: ../../demos/roman_capitals_antiqua.py
   :language: python
   :linenos:

4. Book IV — Planar Polyhedral Nets & Perspective Apparatus
===========================================================

Unfolds exact non-overlapping planar nets for the Tetrahedron, Cube, Octahedron, Dodecahedron
(double 6-pentagon rosette), Icosahedron, and Archimedean Cuboctahedron, projects a 3D cube in
:math:`\mathbb{Q}^3` onto Dürer's glass picture plane verifying harmonic cross-ratio invariance
:math:`\operatorname{CR}(A', E'; M', V_x) = -1`, and generates all 11 ``.euclid-graphic`` SVG plates.

.. literalinclude:: ../../demos/polyhedral_nets_and_perspective.py
   :language: python
   :linenos:
