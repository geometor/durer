"""Command-line interface for ``geometor.durer``."""

from __future__ import annotations

import argparse
from pathlib import Path

from rich.console import Console
from rich.table import Table

from geometor.durer.conics_perspective import (
    construct_durer_conic_sections,
    construct_durer_perspective_apparatus,
)
from geometor.durer.polygons import (
    construct_durer_heptagon_workshop,
    construct_durer_vs_euclid_pentagon,
)
from geometor.durer.polyhedra import construct_durer_polyhedral_nets
from geometor.durer.render import generate_all_codex_figures
from geometor.durer.typography import (
    construct_durer_roman_letter_A,
    construct_durer_roman_letter_O,
)


def _cmd_audit(console: Console) -> int:
    pent = construct_durer_vs_euclid_pentagon()
    hep = construct_durer_heptagon_workshop()
    con = construct_durer_conic_sections()
    persp = construct_durer_perspective_apparatus()
    let_a = construct_durer_roman_letter_A()
    let_o = construct_durer_roman_letter_O()

    tbl = Table(title="GEOMETOR Dürer — Exact Symbolic Audit (Nuremberg 1525)")
    tbl.add_column("Book & Locus", style="cyan")
    tbl.add_column("Construction", style="bold")
    tbl.add_column("Exact Invariant / Certificate", style="green")

    tbl.add_row(
        "Book I, Fig. 34",
        "Two-View Cone Ellipse (Eierlini)",
        f"w_k = sqrt(2k(12-k))/3; symmetric={con.ellipse_bilateral_symmetry_verified}; "
        f"a={con.ellipse_semi_major}, b={con.ellipse_semi_minor}",
    )
    tbl.add_row(
        "Book II, Fig. 16",
        "Single-Aperture Pentagon vs. Euclid",
        f"Equilateral={pent.durer_equilateral}; Equiangular={pent.durer_equiangular}; "
        f"angle={pent.durer_base_interior_deg:.4f}° ({pent.base_angle_error_arcmin:+.2f}')",
    )
    tbl.add_row(
        "Book II, Figs. 11 & 15",
        "Workshop Regular Heptagon",
        f"Q_Durer = {hep.durer_chord_quadrance}; P_7(3/4) = {hep.minimal_polynomial_at_durer} "
        f"(Eisenstein p={hep.eisenstein_prime})",
    )
    tbl.add_row(
        "Book II, Fig. 34",
        "Quadrature of the Circle",
        f"d/a = {hep.quadrature_circle_diameter_over_side}; pi_Durer = {hep.quadrature_implied_pi} "
        f"= {float(hep.quadrature_implied_pi):.3f}",
    )
    tbl.add_row(
        "Book III, pp. 115, 124",
        "Roman Antiqua Capitals A & O",
        f"A contrast {let_a.thick_stroke}:{let_a.thin_stroke}, serifs {let_a.outer_serif_radius}; "
        f"O bowl radius {let_o.bowl_radius}",
    )
    tbl.add_row(
        "Book IV, Figs. 50, 56–63",
        "Perspective Frame & Cube Duplication",
        f"V_x = ({persp.vanishing_point.x}, {persp.vanishing_point.y}); "
        f"CR = {persp.harmonic_cross_ratio_2d}; c^3/g^3 = {persp.delian_cube.volume_ratio}",
    )
    console.print(tbl)
    return 0


def _cmd_nets(console: Console) -> int:
    nets = construct_durer_polyhedral_nets()
    tbl = Table(title="Book IV Planar Polyhedral Nets — Exact Symbolic Seam Verification")
    tbl.add_column("Net", style="cyan")
    tbl.add_column("Locus")
    tbl.add_column("Field", style="magenta")
    tbl.add_column("V - E + F", justify="right")
    tbl.add_column("Folds / Cuts", justify="right")
    tbl.add_column("Verified", style="green")

    for net in nets.values():
        ok = (
            net.unit_edge_verified
            and net.seam_count_verified
            and net.non_overlapping_verified
            and net.euler_characteristic == 2
        )
        tbl.add_row(
            net.key,
            net.durer_figure,
            net.algebraic_field,
            f"{net.vertices_3d} - {net.edges_3d} + {net.faces_3d} = {net.euler_characteristic}",
            f"{len(net.fold_edges)} / {len(net.cut_edges)}",
            "PASS" if ok else "FAIL",
        )
    console.print(tbl)
    return 0


def _cmd_render(console: Console, out_dir: str) -> int:
    paths = generate_all_codex_figures(Path(out_dir))
    console.print(f"[green]Rendered {len(paths)} .euclid-graphic SVGs into {out_dir}:[/green]")
    for p in paths:
        console.print(f"  - {p.name}")
    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the ``geometor-durer`` CLI."""
    parser = argparse.ArgumentParser(
        prog="durer",
        description="GEOMETOR Dürer — Exact symbolic constructions for Underweysung der Messung (1525).",
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("audit", help="Run exact symbolic audit across Books I–IV")
    sub.add_parser("nets", help="Verify Book IV planar polyhedral fold-out nets")
    p_render = sub.add_parser("render", help="Generate all .euclid-graphic SVG figures")
    p_render.add_argument(
        "--out",
        default="docsrc/_static/figures",
        help="Target directory for generated SVG figures",
    )

    args = parser.parse_args(argv)
    console = Console()

    if args.command == "nets":
        return _cmd_nets(console)
    if args.command == "render":
        return _cmd_render(console, args.out)
    if args.command == "audit":
        return _cmd_audit(console)

    _cmd_audit(console)
    _cmd_nets(console)
    return 0
