"""GEOMETOR Dürer: Exact symbolic constructions & bilingual codex for *Underweysung der Messung* (1525).

Provides 100% exact SymPy + ``geometor.model`` constructions across all Four Books (*Vier Bücher*)
of Albrecht Dürer's *Underweysung der Messung, mit dem Zirckel un[d] Richtscheyt, in Linien Ebnen
unnd gantzen Corporen* (Nuremberg, 1525; 2nd ed. 1538; Camerarius Latin ed. 1532):

- **Book I** (:mod:`geometor.durer.conics_perspective`): 12-sector Archimedean spirals
  (*Schneckenlinien*) and two-view descriptive geometry of conic sections (*Elipsis / Eierlini*,
  *Parabola / Brennspiegellini*, *Hiperbole / Gabellini*).
- **Book II** (:mod:`geometor.durer.polygons`): Exact comparison of Dürer's Single-Aperture
  ("Rusty Compass") Pentagon with Euclid's ``Q(phi)`` regular pentagon, plus cubic-impossibility
  and quadrature audits for workshop ``7``-, ``11``-, and ``13``-gons and ``pi = 25/8``.
- **Book III** (:mod:`geometor.durer.typography`): Compass-and-straightedge Roman *Antiqua*
  capitals (``A``, ``O``, ``Q``) in the ``10 x 10`` square and modular Gothic *Textura* minuscules.
- **Book IV** (:mod:`geometor.durer.polyhedra`, :mod:`geometor.durer.conics_perspective`): Planar
  fold-out polyhedral nets for Platonic & Archimedean solids, Delian cube duplication, and central
  perspective projection onto the glass picture plane.
"""

from __future__ import annotations

from geometor.durer.concordance import (
    ConcordanceEntry,
    UnderweysungApparatus,
    default_resources_dir,
    load_apparatus,
)
from geometor.durer.conics_perspective import (
    ConicSectionsResult,
    DelianCubeCertificate,
    PerspectiveApparatusResult,
    SpiralVoluteResult,
    construct_durer_conic_sections,
    construct_durer_perspective_apparatus,
    construct_durer_spiral_volute,
)
from geometor.durer.polygons import (
    PHI,
    HeptagonWorkshopReport,
    PentagonComparisonResult,
    WorkshopPolygonEntry,
    construct_durer_heptagon_workshop,
    construct_durer_vs_euclid_pentagon,
)
from geometor.durer.polyhedra import (
    DURER_BOOK4_SOLIDS_CATALOG,
    Book4SolidCatalogEntry,
    PolyhedralFace,
    PolyhedralNet,
    construct_durer_polyhedral_nets,
    polyhedral_net_to_model,
)
from geometor.durer.render import (
    EMBEDDED_SVG_STYLE,
    export_svg,
    generate_all_codex_figures,
    render_model_svg,
)
from geometor.durer.typography import (
    RomanLetterAResult,
    RomanLetterOQResult,
    TexturaMinusculesResult,
    construct_durer_roman_letter_A,
    construct_durer_roman_letter_O,
    construct_durer_roman_letter_Q,
    construct_durer_textura_minuscules,
)

__version__ = "0.1.1"

__all__ = [
    "DURER_BOOK4_SOLIDS_CATALOG",
    "EMBEDDED_SVG_STYLE",
    "PHI",
    "Book4SolidCatalogEntry",
    "ConcordanceEntry",
    "ConicSectionsResult",
    "DelianCubeCertificate",
    "HeptagonWorkshopReport",
    "PentagonComparisonResult",
    "PerspectiveApparatusResult",
    "PolyhedralFace",
    "PolyhedralNet",
    "RomanLetterAResult",
    "RomanLetterOQResult",
    "SpiralVoluteResult",
    "TexturaMinusculesResult",
    "UnderweysungApparatus",
    "WorkshopPolygonEntry",
    "__version__",
    "construct_durer_conic_sections",
    "construct_durer_heptagon_workshop",
    "construct_durer_perspective_apparatus",
    "construct_durer_polyhedral_nets",
    "construct_durer_roman_letter_A",
    "construct_durer_roman_letter_O",
    "construct_durer_roman_letter_Q",
    "construct_durer_spiral_volute",
    "construct_durer_textura_minuscules",
    "construct_durer_vs_euclid_pentagon",
    "default_resources_dir",
    "export_svg",
    "generate_all_codex_figures",
    "load_apparatus",
    "polyhedral_net_to_model",
    "render_model_svg",
]
