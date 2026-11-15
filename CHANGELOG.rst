=========
Changelog
=========

0.1.5
-----
*2026-11-15*

- Rebuilt codex documentation with ``photon-platform/publish`` ``v0.4.6`` so every inline ``.euclid-graphic`` SVG carries explicit ``viewBox`` pixel dimensions, per-diagram scoped ``<style>`` rules, and Nocturnal Codex dark/light theme parity.

0.1.4
-----
*2026-11-15*

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.3
-----
*2026-11-14*

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2
-----
*2026-11-14*

- Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.1 (2026-11-13)
==================

- Resolve 100% of marginal ``.. folio::`` source links (28 directives) to SLUB Dresden digital facsimile page anchors via ``publish folio-links``.

0.1.0 (2026-11-12)
==================

- Initial release of ``geometor-durer`` (`GEOMETOR • durer`).
- **4-Track Bilingual Digital Scriptorium Book Codex** (`docsrc/underweysung/`): `English`,
  `German (1525)`, `Summary`, and `Notes` across Dedication and Books I–IV of Albrecht Dürer's
  *Underweysung der Messung* (Nuremberg, 1525), collated with Joachim Camerarius's 1532 Latin
  edition and Dürer's 1538 posthumous second edition.
- **Exact Symbolic Library** (`src/geometor/durer/`):

  - `polygons.py`: `construct_durer_vs_euclid_pentagon` and `construct_durer_heptagon_workshop`.
  - `polyhedra.py`: `construct_durer_polyhedral_nets` and `polyhedral_net_to_model` across 6
    Platonic and Archimedean solids.
  - `typography.py`: `construct_durer_roman_letter_A`, `construct_durer_roman_letter_O`,
    `construct_durer_roman_letter_Q`, and `construct_durer_textura_minuscules`.
  - `conics_perspective.py`: `construct_durer_spiral_volute`, `construct_durer_conic_sections`,
    and `construct_durer_perspective_apparatus`.
  - `render.py`, `concordance.py`, `sphinx_ext.py`, and `cli.py`.
- **11 `.euclid-graphic` SVG Plates**, 5 JSON apparatus registries in `resources/underweysung/`,
  4 runnable `demos/`, and full `pytest` + `ruff` + `publish build` verification.
