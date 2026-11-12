"""Runnable demonstration of Book IV planar polyhedral nets, perspective glass frame & cube doubling."""

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
    construct_durer_perspective_apparatus,
    construct_durer_polyhedral_nets,
    generate_all_codex_figures,
)


def main() -> None:
    console = Console()
    nets = construct_durer_polyhedral_nets()
    persp = construct_durer_perspective_apparatus()

    tbl = Table(title="Book IV — Exact Planar Polyhedral Fold-Out Nets")
    tbl.add_column("Net", style="cyan")
    tbl.add_column("Field", style="magenta")
    tbl.add_column("V, E, F (chi)")
    tbl.add_column("Folds / Cuts")
    tbl.add_column("Unit Q=1", style="green")
    tbl.add_column("Disjoint", style="green")

    for net in nets.values():
        tbl.add_row(
            net.title,
            net.algebraic_field,
            f"({net.vertices_3d}, {net.edges_3d}, {net.faces_3d}) -> {net.euler_characteristic}",
            f"{len(net.fold_edges)} / {len(net.cut_edges)}",
            str(net.unit_edge_verified),
            str(net.non_overlapping_verified),
        )
    console.print(tbl)

    console.print(
        f"Perspective Apparatus: Eye={persp.eye_3d} -> Vanishing Point V_x="
        f"({persp.vanishing_point.x}, {persp.vanishing_point.y}), "
        f"Harmonic Cross-Ratio CR={persp.harmonic_cross_ratio_2d} "
        f"(verified={persp.cross_ratio_invariant_verified})"
    )
    console.print(
        f"Delian Doubling of the Cube (Fig. 50): g={persp.delian_cube.given_g}, "
        f"c={persp.delian_cube.first_mean_c}, d={persp.delian_cube.second_mean_d}, "
        f"e={persp.delian_cube.given_e} => c^3/g^3 = {persp.delian_cube.volume_ratio}"
    )

    figs_dir = ROOT / "docsrc" / "_static" / "figures"
    paths = generate_all_codex_figures(figs_dir)
    console.print(f"[bold green]Generated {len(paths)} .euclid-graphic SVG figures in {figs_dir}[/bold green]")


if __name__ == "__main__":
    main()
