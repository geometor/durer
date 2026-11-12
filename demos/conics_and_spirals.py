"""Runnable demonstration of Book I Archimedean spirals & two-view orthographic conic sections."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / "src", ROOT.parent / "model" / "src"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from rich.console import Console
from rich.table import Table

from geometor.durer import construct_durer_conic_sections, construct_durer_spiral_volute


def main() -> None:
    console = Console()
    spiral = construct_durer_spiral_volute(turns=2)
    conics = construct_durer_conic_sections()

    console.print("[bold cyan]Book I — 12-Sector Archimedean Spiral & Two-View Conic Projection[/bold cyan]")
    console.print(
        f"Spiral sectors: {spiral.sector_count}, outer radius: {spiral.outer_radius}, "
        f"constructed exact points in Q(sqrt(3)): {len(spiral.spiral_points)}"
    )

    tbl = Table(title="Book I, Fig. 34 — Orthographic Cone-Section Stations (Elipsis / Eierlini)")
    tbl.add_column("Station k", justify="right")
    tbl.add_column("Elevation x_k")
    tbl.add_column("Height z_k")
    tbl.add_column("Plan Radius r_k")
    tbl.add_column("Exact Half-Width w_k", style="green")

    for k, xk, zk, rk, wk in conics.ellipse_stations:
        tbl.add_row(str(k), str(xk), str(zk), str(rk), str(wk))

    console.print(tbl)
    console.print(
        f"Bilateral symmetry w_k == w_{{12-k}} verified: [bold green]{conics.ellipse_bilateral_symmetry_verified}[/bold green]  |  "
        f"a = {conics.ellipse_semi_major}, b = {conics.ellipse_semi_minor}, "
        f"c = {conics.ellipse_focal_distance}, e = {conics.ellipse_eccentricity}"
    )
    console.print(
        f"Parabola focal length f = {conics.parabola_focal_length}  |  "
        f"Hyperbola (a_h, b_h) = ({conics.hyperbola_semi_transverse}, {conics.hyperbola_semi_conjugate})"
    )


if __name__ == "__main__":
    main()
