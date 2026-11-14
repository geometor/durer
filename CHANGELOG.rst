=========
Changelog
=========

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
