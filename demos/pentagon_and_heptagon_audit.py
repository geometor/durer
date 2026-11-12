"""Runnable demonstration auditing Book II regular polygons (Dürer vs. Euclid) & circle quadrature."""

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
    construct_durer_heptagon_workshop,
    construct_durer_vs_euclid_pentagon,
)


def main() -> None:
    console = Console()
    pent = construct_durer_vs_euclid_pentagon()
    hep = construct_durer_heptagon_workshop()

    console.print("[bold cyan]Book II — Demonstrative vs. Mechanice Regular Polygons[/bold cyan]")
    console.print(f"Euclid regular pentagon over Q(phi) verified: [green]{pent.euclid_regular}[/green]")
    console.print(
        f"Dürer single-aperture pentagon: equilateral=[green]{pent.durer_equilateral}[/green], "
        f"equiangular=[yellow]{pent.durer_equiangular}[/yellow]"
    )
    console.print(
        f"Dürer base interior angle = {pent.durer_base_interior_deg:.5f}° vs. 108.00000° "
        f"(error = {pent.base_angle_error_deg:+.5f}° = {pent.base_angle_error_arcmin:+.2f}')"
    )
    console.print(
        f"Heptagon minimal polynomial P_7(q) = {hep.minimal_polynomial_expr}; "
        f"P_7(3/4) = [bold yellow]{hep.minimal_polynomial_at_durer}[/bold yellow] (Eisenstein p={hep.eisenstein_prime})"
    )

    tbl = Table(title="Book II Polygon & Quadrature Accuracy Audit")
    tbl.add_column("n", justify="right")
    tbl.add_column("Construction")
    tbl.add_column("Type", style="magenta")
    tbl.add_column("Exact s/R")
    tbl.add_column("Rel. Chord Error", justify="right")
    tbl.add_column("Step Angle", justify="right")

    for row in hep.workshop_catalog:
        tbl.add_row(
            str(row.n_sides),
            row.durer_label,
            row.classification,
            str(row.exact_chord_over_r),
            f"{row.relative_chord_error * 100:+.4f}%",
            f"{row.central_angle_durer_deg:.4f}° (true {row.central_angle_true_deg:.4f}°)",
        )
    console.print(tbl)
    console.print(
        f"Circle Quadrature (Fig. 34): d/a = {hep.quadrature_circle_diameter_over_side} "
        f"=> pi_Durer = {hep.quadrature_implied_pi} = {float(hep.quadrature_implied_pi):.4f}"
    )


if __name__ == "__main__":
    main()
