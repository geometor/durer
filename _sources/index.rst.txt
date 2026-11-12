:navigation: header

==========================================================================
GEOMETOR • Dürer — *Underweysung der Messung* (Nuremberg, 1525 / 1538)
==========================================================================

.. epigraph::

   *Sann warhafftig steckt die kunst inn der natur / wer sie herauß kan reyssen / der hat sie.
   Überkumbstu sie / so wirdet sie dir vil fels nemen in deinem werck. Vnd durch die Geometria
   magstu deines wercks vil beweyssen.*

   — **Albrecht Dürer**, *Vier Bücher von menschlicher Proportion* (1528), Book III

**GEOMETOR • durer** presents a four-track bilingual Digital Scriptorium Book Codex of
**Albrecht Dürer's** landmark **Underweysung der Messung, mit dem Zirckel un[d] Richtscheyt,
in Linien Ebnen unnd gantzen Corporen** (*Instruction in Measurement, with Compass and
Straightedge, in Lines, Planes, and Whole Solid Bodies*, Nuremberg, 1525; 2nd enlarged ed.,
1538; Latin ed. by Joachim Camerarius, Paris, 1532), paired with **100% exact symbolic SymPy
and ``geometor.model`` constructions** verifying every Euclidean proof, workshop approximation,
typographic canon, planar polyhedral net, and perspective projection.

.. picture:: _static/figures/book2_durer_vs_euclid_pentagon.svg
   :caption: Dürer's Single-Aperture ("Rusty Compass") Pentagon (solid gold, exact unit sides $Q = 1$, base angle $108.3661^\circ$) overlaid on Euclid's Golden-Section Pentagon over $\mathbb{Q}(\phi)$ (dashed blue, exact interior angle $108^\circ$) on shared base $ab$.

----

Codex & Symbolic Architecture
=============================

1. :doc:`underweysung/index` — **4-Track Bilingual Digital Scriptorium Codex** (`English`,
   `German (1525)`, `Summary`, `Notes`) spanning Dürer's Dedication to Willibald Pirckheimer
   and all Four Books (*Vier Bücher*):

   - **Book I** (`unit-1-lines-spirals-conics`): Point, serpentine curve (*Schlangenlini*),
     12-sector Archimedean spirals (*Schneckenlinien*), spatial helices, Nicomedes's conchoid
     (*Muschellini*), and the invention of **two-view orthographic descriptive geometry** for
     the *Elipsis / Eierlini*, *Parabola / Brennspiegellini*, and *Hiperbole / Gabellini*.
   - **Book II** (`unit-2-planes-polygons-tilings`): Planar tilings and pentagonal parquetries,
     *demonstrative* vs. *mechanice* regular polygons (`3` through `16` sides), the
     single-aperture pentagon, the $\frac{\sqrt{3}}{2}R$ heptagon, Euclidean area quadrature,
     and the $\pi \approx \frac{25}{8} = 3.125$ circle quadrature.
   - **Book III** (`unit-3-architecture-sundials-typography`): Architectural columns,
     Nuremberg sundial gnomonics ($49^\circ$ pole), optical scaling of tower inscriptions,
     Roman *Antiqua* capitals (`A`–`Z`) inside the $10 \times 10$ square, and modular Gothic
     *Textura* minuscules.
   - **Book IV** (`unit-4-solids-nets-perspective`): The **first printed planar fold-out
     polyhedral nets in mathematical history** (all 5 Platonic + 7 Archimedean solids), the
     Delian **Doubling of the Cube** (Sporus, Plato's mechanical square, Hero, and cannonball
     scaling), cube shadow sciagraphy, and the **four perspective instruments**.

2. :doc:`demos/index` — **Executable Exact Symbolic Demonstrations** auditing every construction
   in ``SymPy`` and ``geometor.model`` with zero floating-point coordinates.

3. :doc:`modules/index` — **Python Package Reference** for ``geometor.durer``.

.. toctree::
   :maxdepth: 2
   :hidden:

   about/index
   mission/index
   underweysung/index
   demos/index
   modules/index
   log/index
   changelog
