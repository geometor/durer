:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive 4-Track Book Codex & Symbolic Environment

Welcome to the GEOMETOR critical digital edition of Albrecht Dürer's *Underweysung der Messung* (*Instruction in Measurement*, Nuremberg, 1525 / Camerarius Latin, 1532). This edition combines an authentic early modern diplomatic transcription with a fresh English translation, interactive geometric visualization, and 100% exact symbolic algebra.

----

1. Synchronized Reading Tracks
------------------------------

Every unit in the Book Codex (:doc:`/underweysung/index`) is organized across four synchronized reading tracks accessible from the chapter header bar:

* **English**: A freshly authored, independent GEOMETOR translation rendered directly from Dürer's 1525 Nuremberg Early New High German, collated with Joachim Camerarius's 1532 Latin terminology.
* **German (1525)**: The diplomatic German copy-text faithfully transcribed from the 1525 Nuremberg first edition held by SLUB Dresden (`PPN 27778509X`), preserving original orthography and Dürer's 1525 Errata.
* **Summary**: Structural digests highlighting Dürer's geometric sequence, definitions, workshop constructions, and practical applications.
* **Notes**: Scholarly commentary detailing the exact mathematical theory (*demonstrative* vs. *mechanice*), philological variants, and historical reception across classical and modern mathematics.

Switch between tracks at any time using the track navigation bar at the top of each chapter. The reader maintains your reading position across companion tracks.

----

2. Primary-Source Folio Milestones
----------------------------------

Every paragraph and woodcut in the text is tied to the historical printing:

* Marginal folio badges (such as ``[N1525 p. 005–006]`` or ``[N1525 p. 053–056]``) anchor the section to the physical folios of the 1525 Nuremberg printing.
* Clicking a milestone badge opens the exact high-resolution digital facsimile page in the SLUB Dresden archive.
* The header **Folio** indicator confirms the exact page span of the current unit within the 182-page Nuremberg witness.

----

3. Interactive Diagrams & Deductive Links
-----------------------------------------

The edition features custom interactive ``.euclid-graphic`` SVG diagrams rendered directly from exact symbolic geometry:

* **Element Hovering**: Hovering over or clicking diagram labels (*a*, *b*, *c*, *d*, conic section curves, polyhedral net vertices) highlights the corresponding elements on the plate and cross-references them with the text.
* **Demonstrative vs. Mechanice Overlays**: Special comparison plates (such as Dürer's single-aperture "rusty compass" pentagon vs. Euclid's exact golden-section pentagon) show exact geometric divergence and workshop tolerances.
* **Responsive Rendering**: Vector diagrams scale smoothly on all devices and seamlessly adapt to light and dark theme modes.

----

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

A fast client-side search index indexes both the English and German tracks:

* Enter search terms into the sidebar search bar.
* Results link directly to matching chapters, sections, and paragraphs.
* Matched keywords are automatically highlighted in-page using URL ``?highlight=`` parameters for quick discovery.

----

5. Categories, Tags, Document Types & Collection Views
------------------------------------------------------

Explore the four books through interconnected facets:

* **Taxonomy Facets**: Filter by topic (e.g. *spirals*, *conic sections*, *polygons*, *polyhedral nets*, *perspective*, *typography*), historical geometers, or document types.
* **Collection Views**: Collection index pages (such as the :doc:`/log/index`) support instant layout toggling between **Cards**, **Banners**, and **List** views.

----

6. People, Bibliography & Glossary Tooltips
-------------------------------------------

Scholarly context is available throughout the reading pane:

* **People Tooltips**: Hovering over any linked name (such as :person:`Albrecht Dürer <durer>`, :person:`Joachim Camerarius <camerarius>`, :person:`Euclid <euclid>`, or :person:`Johannes Kepler <kepler>`) displays a biographical summary with a link to the :doc:`/underweysung/persons` registry.
* **Citations**: Citations (such as :cite:`durer:1525` or :cite:`durer:1532:camerarius`) display complete bibliographical data on hover and link to the :doc:`/underweysung/bibliography`.
* **Technical Terms**: Specialized Early New High German workshop terms and Latin equivalents (such as :term:`Schlangenlini <schlangenlini>`, :term:`Eierlini <eierlini>`, or :term:`Aufgezogner Grund <aufgezogner-grund>`) link to definition cards in the :doc:`/underweysung/glossary`.
* **Theme Switcher**: Toggle between light parchment and dark modes using the theme switcher in the top navigation bar.

----

7. Command-Line & Python API
----------------------------

For computational geometers and researchers, ``geometor.durer`` provides symbolic models and command-line tools:

Verifying Parity & Folio Alignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Verify paragraph parity and audit all 28 primary-source folio links against SLUB Dresden facsimile anchors:

.. code-block:: bash

   publish folio-links

Interactive Symbolic Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Construct Dürer's geometric algorithms with 100% exact SymPy coordinates:

.. code-block:: python

   from geometor.durer import construct_durer_pentagon, construct_archimedean_spiral

   # Construct Dürer's single-aperture rusty-compass pentagon
   model, metrics = construct_durer_pentagon()
   print(f"Base angle: {metrics['base_angle_deg']:.4f}° (error: {metrics['error_arcmin']:+.2f}')")
