:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:
.. _about-durer:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

**GEOMETOR • durer** is the scholarly Digital Scriptorium edition and exact symbolic engine for **Albrecht Dürer's** landmark treatise, *Underweysung der Messung, mit dem Zirckel un[d] Richtscheyt, in Linien Ebnen unnd gantzen Corporen* (*Instruction in Measurement, with Compass and Straightedge, in Lines, Planes, and Whole Solid Bodies*, Nuremberg, 1525; 2nd enlarged ed., 1538), collated with **Joachim Camerarius's** 1532 Paris Latin translation, *Institutionum Geometricarum Libri Quatuor*. Dedicated to his humanist patron **Willibald Pirckheimer**, Dürer's *Underweysung* stands as the first printed mathematics book in the German language and the decisive intellectual bridge connecting classical Greek demonstrative geometry with Northern and Italian Renaissance workshop practice.

The edition reconstructs all four books (*Vier Bücher*) through a synchronized four-track codex structure (diplomatic 1525 Nuremberg German, modern English translation, structural digest, and mathematical notes). Implicit geometric concepts across Dürer's curriculum are extracted into machine-addressable semantic elements: two-view descriptive geometry of conic sections (*Eierlini*, *Brennspiegellini*, *Gabellini*), 12-sector Archimedean spirals and spatial helices, regular polygon constructions and modular parquetries, architectural sundials ($49^\circ$ Nuremberg gnomonics) and Roman *Antiqua* capitals, planar fold-out polyhedral nets (the first in print history), the Delian doubling of the cube, and the four perspective projection devices.

Crucially, the edition honors Dürer's profound epistemic distinction between exact Euclidean demonstration (*demonstrative*) and rapid workshop approximation (*mechanice*). Using :mod:`geometor.model` and `SymPy <https://www.sympy.org>`_, every construction is certified algebraically without floating-point injection—proving the exact cubic residual :math:`P_7(\frac{3}{4}) = -\frac{1}{64}` of his heptagon, the nested quadratic radicals of his single-aperture pentagon, and the bilateral symmetry of his two-view conic sections. This work connects Dürer's Nuremberg workshop directly to sister GEOMETOR treatises: the foundational canons of ``geometor.elements`` and ``geometor.euclid``, Luca Pacioli's ``geometor.pacioli`` (*De Divina Proportione*), and the golden ratio discovery canon ``geometor.divine``.

The GEOMETOR Mission
--------------------

Founded by **phi ARCHITECT**, the GEOMETOR project is dedicated to three foundational pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. GEOMETOR elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Anchoring geometric constructions in 100% exact symbolic algebra (`SymPy <https://www.sympy.org>`_) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic number fields rather than floating-point approximations. Every geometric theorem and construction is mathematically verified and permanently reproducible.

Repurposing Knowledge Across Mediums
    Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

The Digital Scriptorium edition of *Underweysung der Messung* is established on primary archival witnesses and rigorous symbolic methods:

- **German (1525) Copy-Text**: Diplomatic Early New High German transcription of the 1525 Nuremberg first edition held by the Sächsische Landesbibliothek – Staats- und Universitätsbibliothek Dresden (SLUB Dresden, `PPN 27778509X <https://kxp.k10plus.de/DB=1.65/PPNSET?PPN=27778509X>`_), preserving original folio pagination, orthographic superscripts (:math:`u^\circ`), and Dürer's own 1525 Errata list.
- **Latin Translation (1532)**: Joachim Camerarius, *Institutionum Geometricarum Libri Quatuor* (Paris: Christian Wechel, 1532), establishing humanistic Latin nomenclature for Dürer's vernacular terminology.
- **Second German Edition (1538)**: *Underweysung der Messung* (Nuremberg: Hieronymus Andreae, 1538), incorporating Dürer's posthumous expansions and additional figures.
- **English Translation**: Modern, independent scholarly translation prepared directly from the 1525 copy-text, collated with Camerarius (1532) and Walter L. Strauss's commentary (Abaris Books, 1977).
- **Exact Symbolic Engine**: Every geometric construction in ``geometor.durer`` preserves 100% exact algebraic coordinates in SymPy and :mod:`geometor.model` without floating-point error, compiled through the Photon Publisher framework.
