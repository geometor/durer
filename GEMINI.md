# `geometor-durer` — Agent Context & Architectural Guide

## Purpose

`geometor-durer` (`/home/phi/PROJECTS/geometor/durer`) is the GEOMETOR Digital Scriptorium Book Codex and exact symbolic Python laboratory for **Albrecht Dürer's *Underweysung der Messung, mit dem Zirckel un[d] Richtscheyt, in Linien Ebnen unnd gantzen Corporen*** (Nuremberg, 1525 1st ed.; 1538 2nd ed.), collated with **Joachim Camerarius's** 1532 Paris Latin edition (*Institutionum Geometricarum Libri Quatuor*).

## Strict Architectural Mandates

1. **100% Exact Symbolic Precision (`src/geometor/durer/`)**:
   - **Zero `float` or `sp.Float` in `geometor.model.Model`**: Every point, line, circle, segment, and polygon registered in a `Model` uses exact `SymPy` rationals, quadratic radicals, cyclotomic golden-ratio expressions ($\mathbb{Q}(\phi), \mathbb{Q}(\sqrt{5}, \sin 36^\circ)$), or nested radical intersections via `Model(..., logger=False, auto_intersect=False)` and `model.intersect_all(...)`.
   - Floating-point numbers (`evalf`) are permitted strictly at SVG serialization time in `render.py` or human-readable arcminute error reporting.
2. **Strict Content / Code Separation (`docsrc/underweysung/`)**:
   - **Zero `py_file` directives** inside `docsrc/underweysung/`.
   - All executable code lives in `src/geometor/durer/` and `demos/`.
   - All 11 interactive `.euclid-graphic` SVGs live in `docsrc/_static/figures/` and are regenerable deterministically via `generate_all_codex_figures("docsrc/_static/figures")`.
3. **Copyright & Translation Integrity**:
   - Primary German source: Public-domain 1525 Nuremberg *editio princeps* (`SLUB Dresden PPN 27778509X`).
   - English track (`-en.rst`): Freshly translated directly from Dürer's 1525 Early New High German—never copy or paraphrase Walter L. Strauss's 1977 English translation (*The Painter's Manual*).

## Repository Map

- `src/geometor/durer/`:
  - `polygons.py`: `construct_durer_vs_euclid_pentagon`, `construct_durer_heptagon_workshop`.
  - `polyhedra.py`: `construct_durer_polyhedral_nets` (Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron, Cuboctahedron), `polyhedral_net_to_model`, `DURER_BOOK4_SOLIDS_CATALOG`.
  - `typography.py`: `construct_durer_roman_letter_A`, `construct_durer_roman_letter_O`, `construct_durer_roman_letter_Q`, `construct_durer_textura_minuscules`.
  - `conics_perspective.py`: `construct_durer_spiral_volute`, `construct_durer_conic_sections`, `construct_durer_perspective_apparatus`.
  - `render.py`: Theme-adaptive `.euclid-graphic` SVG renderer (`render_model_svg`, `generate_all_codex_figures`).
  - `concordance.py`: Typed JSON loaders for `resources/underweysung/*.json`.
  - `sphinx_ext.py`: Relabels the `de` track tab to `"German (1525)"` and wires offline local sibling `intersphinx` inventories.
  - `cli.py` & `__main__.py`: CLI entrypoints (`audit`, `nets`, `render`).
- `demos/`: Four standalone runnable scripts auditing Books I–IV.
- `docsrc/underweysung/`: 4-track Book Codex (`-en`, `-de`, `-summary`, `-notes`) across Units 1–4 plus `concordance.rst`, `bibliography.rst`, `persons.rst`, and `glossary.rst`.
- `resources/underweysung/`: `sources_manifest.json`, `concordance.json`, `persons.json`, `citations.json`, `glossary.json`.
- `tests/test_durer.py`: Offline symbolic test suite.

## Verification Commands (Offline Sandbox)

```bash
pytest
ruff check src demos tests
publish build
```
