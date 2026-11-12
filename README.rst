==============
geometor-durer
==============

**Albrecht Dürer's *Underweysung der Messung* (Nuremberg, 1525 / Camerarius, 1532) — Bilingual Digital Scriptorium Book Codex & 100% Exact Symbolic Geometry Demonstrations**

``geometor-durer`` pairs a four-track bilingual scholarly Book Codex (``:layout: book``) of
**Albrecht Dürer's** *Underweysung der Messung, mit dem Zirckel un[d] Richtscheyt, in Linien Ebnen
unnd gantzen Corporen* (Nuremberg, 1525; 2nd enlarged ed. 1538; collated with Joachim Camerarius's
1532 Paris Latin *Institutionum Geometricarum Libri Quatuor*) with 100% exact symbolic ``SymPy`` +
``geometor.model`` constructions across all four books.

Highlights
==========

1. **Four-Track Bilingual Digital Scriptorium Codex (``docsrc/underweysung/``)**:

   - **English**: Fresh GEOMETOR translation directly from the 1525 Nuremberg Early New High German
     *editio princeps* (``SLUB Dresden PPN 27778509X``).
   - **German (1525)**: Diplomatic 1525 Early New High German copy-text collated with Camerarius's
     1532 Latin terminology and Dürer's 1525 *Errata* (p. 182).
   - **Summary**: Structural folio-by-folio digest across Dedication and Books I–IV.
   - **Notes**: Exact algebraic audits, Rational Trigonometry quadrance/spread proofs, and
     historical concordances linking ``euclid``, ``elements``, ``pacioli``, ``pappus``, ``divine``,
     ``klein``, ``lemoine``, and ``thompson``.

2. **100% Exact Symbolic Constructions (``src/geometor/durer/`` — Zero ``float`` in ``Model``)**:

   - **Book I (`conics_perspective.py`)**: 12-sector Archimedean *Schneckenlini* over
     $\mathbb{Q}(\sqrt{3})$ and two-view Mongean descriptive geometry of the conic *Elipsis*
     (*Eierlini*), proving algebraically that Dürer's 12-station transfer rule gives strictly
     symmetric ordinates $w_k = \frac{\sqrt{2k(12-k)}}{3} = w_{12-k}$ ($a = \sqrt{13}$,
     $b = 2\sqrt{2}$, $c = \sqrt{5}$).
   - **Book II (`polygons.py`)**: Exact comparison of Euclid/Ptolemy's $\mathbb{Q}(\phi)$ regular
     pentagon ($108^\circ$) against Dürer's fixed-aperture ("rusty compass") equilateral pentagon
     ($Q = 1$ on all five sides, base angle $108.36612^\circ$, error $+21.97'$), workshop heptagon
     $Q = \frac{3}{4}$ audited against Eisenstein-irreducible $P_7(q) = q^3 - 7q^2 + 14q - 7$
     (exact residual $P_7(\frac{3}{4}) = -\frac{1}{64}$, $-0.2008\%$ chord error), and circle
     quadrature $\pi_{\text{Dürer}} = \frac{25}{8} = 3.125$.
   - **Book III (`typography.py`)**: Compass-and-straightedge Roman *Antiqua* capitals **A**, **O**,
     and **Q** inside the $10 \times 10$ *rechte Fierung* ($1 : \frac{1}{3}$ stroke contrast,
     shifted-diagonal bowl radius $5 - \frac{\sqrt{2}}{4}$), plus modular Gothic *Textura*
     minuscules **i**, **n**, **m** with $\sqrt{2}$ stem pitch and $\sqrt{2} - 1$ counter width.
   - **Book IV (`polyhedra.py`, `conics_perspective.py`)**: Exact unit-quadrance ($Q = 1$) planar
     fold-out nets for all 5 Platonic solids (including the double 6-pentagon rosette Dodecahedron
     over $\mathbb{Q}(\sqrt{5}, \sin 36^\circ)$) and the Archimedean Cuboctahedron, Delian cube
     douplication over $\mathbb{Q}(\sqrt[3]{2})$, and homogeneous central projection onto Dürer's
     glass picture frame preserving harmonic cross-ratio $\operatorname{CR}(A', E'; M', V_x) = -1$.

Usage & Verification
====================

.. code-block:: bash

   # Run exact symbolic test suite (offline sandbox)
   pytest

   # Run executable mathematical demonstrations
   PYTHONPATH=src /home/phi/PROJECTS/geometor/.venv/bin/python demos/conics_and_spirals.py
   PYTHONPATH=src /home/phi/PROJECTS/geometor/.venv/bin/python demos/pentagon_and_heptagon_audit.py
   PYTHONPATH=src /home/phi/PROJECTS/geometor/.venv/bin/python demos/roman_capitals_antiqua.py
   PYTHONPATH=src /home/phi/PROJECTS/geometor/.venv/bin/python demos/polyhedral_nets_and_perspective.py

   # Compile the 4-track Book Codex and site into docs/
   publish build

License
=======

MIT License — GEOMETOR Initiative.
