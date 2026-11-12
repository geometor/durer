"""Runnable demonstration of Book III Roman Antiqua capitals (A, O, Q) & Gothic Textura minuscules."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / "src", ROOT.parent / "model" / "src"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from rich.console import Console
from rich.table import Table

from geometor.durer import (
    construct_durer_roman_letter_A,
    construct_durer_roman_letter_O,
    construct_durer_roman_letter_Q,
    construct_durer_textura_minuscules,
)


def main() -> None:
    console = Console()
    let_a = construct_durer_roman_letter_A()
    let_o = construct_durer_roman_letter_O()
    let_q = construct_durer_roman_letter_Q()
    tex = construct_durer_textura_minuscules()

    tbl = Table(title="Book III — Geometric Typography (Antiqua & Textura)")
    tbl.add_column("Glyph", style="cyan")
    tbl.add_column("Framing Grid")
    tbl.add_column("Exact Algebraic Parameters", style="green")

    tbl.add_row(
        "Roman A",
        "10 x 10 Square",
        f"thick={let_a.thick_stroke}, thin={let_a.thin_stroke}, "
        f"outer serif r={let_a.outer_serif_radius}, inner serif r={let_a.inner_serif_radius}, "
        f"counter apex=({let_a.counter_triangle[2].x}, {let_a.counter_triangle[2].y})",
    )
    tbl.add_row(
        "Roman O",
        "10 x 10 Square (cb diagonal)",
        f"centers f=({let_o.shifted_center_f.x}, {let_o.shifted_center_f.y}), "
        f"g=({let_o.shifted_center_g.x}, {let_o.shifted_center_g.y}), r={let_o.bowl_radius}",
    )
    tbl.add_row(
        "Roman Q",
        "10 x 10 Square + ad tail",
        f"bowl r={let_q.bowl_radius}, tail tip=({let_q.tail_points[-1].x}, {let_q.tail_points[-1].y})",
    )
    tbl.add_row(
        "Textura i, n, m",
        "3 Unit Squares + 45° Diamonds",
        f"stem width={tex.stem_width}, modules: i={len(tex.glyph_polygons['i'])}, "
        f"n={len(tex.glyph_polygons['n'])}, m={len(tex.glyph_polygons['m'])}",
    )
    console.print(tbl)


if __name__ == "__main__":
    main()
