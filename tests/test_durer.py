"""Comprehensive exact symbolic & codex verification suite for ``geometor.durer``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, zero_test

import geometor.durer as gd
from geometor.durer.cli import main as cli_main

REPO_ROOT = Path(__file__).resolve().parents[1]


def _assert_zero_floats_in_model(model: Model) -> None:
    """Assert that every geometric primitive in ``model`` is 100% free of ``sp.Float``."""
    for el in model:
        if isinstance(el, spg.Point2D):
            assert not el.x.atoms(sp.Float), f"Float found in Point.x: {el}"
            assert not el.y.atoms(sp.Float), f"Float found in Point.y: {el}"
        elif isinstance(el, (spg.Line2D, spg.Segment2D)):
            for pt in (el.p1, el.p2):
                assert not pt.x.atoms(sp.Float), f"Float found in {el}"
                assert not pt.y.atoms(sp.Float), f"Float found in {el}"
        elif isinstance(el, spg.Circle):
            assert not el.center.x.atoms(sp.Float), f"Float found in Circle center: {el}"
            assert not el.center.y.atoms(sp.Float), f"Float found in Circle center: {el}"
            assert not el.radius.atoms(sp.Float), f"Float found in Circle radius: {el}"
        elif isinstance(el, (spg.Polygon, spg.Triangle, spg.RegularPolygon)):
            for v in el.vertices:
                assert not v.x.atoms(sp.Float), f"Float found in Polygon vertex: {v}"
                assert not v.y.atoms(sp.Float), f"Float found in Polygon vertex: {v}"


def test_version_and_public_api() -> None:
    assert gd.__version__ == "0.1.1"
    assert zero_test(gd.PHI**2 - gd.PHI - 1)


def test_book1_spiral_and_conic_sections_exact() -> None:
    spiral = gd.construct_durer_spiral_volute(turns=2)
    _assert_zero_floats_in_model(spiral.model)
    assert spiral.outer_radius == sp.Integer(12)
    assert spiral.sector_count == 12
    assert len(spiral.spiral_points) == 25
    assert spiral.radii[0] == sp.Integer(0)
    assert spiral.radii[12] == sp.Integer(6)
    assert spiral.radii[24] == sp.Integer(12)

    conics = gd.construct_durer_conic_sections()
    _assert_zero_floats_in_model(conics.model)
    assert conics.ellipse_bilateral_symmetry_verified is True
    assert zero_test(conics.ellipse_semi_major - sp.sqrt(13))
    assert zero_test(conics.ellipse_semi_minor - 2 * sp.sqrt(2))
    assert zero_test(conics.ellipse_focal_distance - sp.sqrt(5))
    assert zero_test(conics.parabola_focal_length - sp.Rational(3, 5) * sp.sqrt(5))
    for k, _, _, _, wk in conics.ellipse_stations:
        expected_w_sq = sp.Rational(2, 9) * k * (12 - k)
        assert zero_test(wk**2 - expected_w_sq)


def test_book2_durer_vs_euclid_pentagon_and_heptagon() -> None:
    pent = gd.construct_durer_vs_euclid_pentagon()
    _assert_zero_floats_in_model(pent.model)
    assert pent.durer_equilateral is True
    assert pent.durer_equiangular is False
    assert pent.euclid_regular is True
    for q_side in pent.durer_side_quadrances:
        assert zero_test(q_side - 1)
    for q_side in pent.euclid_side_quadrances:
        assert zero_test(q_side - 1)
    assert zero_test(pent.euclid_diagonal_quadrance - gd.PHI**2)
    assert abs(pent.durer_base_interior_deg - 108.36612) < 1e-3
    assert abs(pent.base_angle_error_arcmin - 21.97) < 0.05

    hep = gd.construct_durer_heptagon_workshop()
    _assert_zero_floats_in_model(hep.model)
    assert hep.durer_chord_quadrance == sp.Rational(3, 4)
    assert hep.minimal_polynomial_at_durer == sp.Rational(-1, 64)
    assert hep.eisenstein_prime == 7
    assert hep.quadrature_implied_pi == sp.Rational(25, 8)
    assert len(hep.workshop_catalog) >= 3


def test_book3_roman_antiqua_and_textura_exact() -> None:
    let_a = gd.construct_durer_roman_letter_A()
    _assert_zero_floats_in_model(let_a.model)
    assert let_a.thick_stroke == sp.Integer(1)
    assert let_a.thin_stroke == sp.Rational(1, 3)
    assert let_a.outer_serif_radius == sp.Rational(10, 7)
    assert let_a.inner_serif_radius == sp.Rational(1, 2)
    v_apex = max(let_a.counter_triangle, key=lambda p: float(p.y.evalf()))
    assert v_apex.x == sp.Rational(14, 3)
    assert v_apex.y == sp.Rational(200, 21)

    let_o = gd.construct_durer_roman_letter_O()
    _assert_zero_floats_in_model(let_o.model)
    assert zero_test(let_o.bowl_radius - (sp.Integer(5) - sp.sqrt(2) / 4))
    assert zero_test(quadrance(let_o.shifted_center_f, let_o.shifted_center_g) - 1)
    assert len(let_o.crossover_points) == 2

    let_q = gd.construct_durer_roman_letter_Q()
    _assert_zero_floats_in_model(let_q.model)
    assert let_q.letter == "Q"
    assert len(let_q.tail_points) >= 3

    tex = gd.construct_durer_textura_minuscules()
    _assert_zero_floats_in_model(tex.model)
    assert tex.stem_width == sp.Integer(1)
    assert tex.stacked_square_count == 3
    assert set(tex.glyph_polygons.keys()) == {"i", "n", "m"}


def test_book4_polyhedral_nets_and_perspective() -> None:
    nets = gd.construct_durer_polyhedral_nets()
    expected_keys = {
        "tetrahedron",
        "cube",
        "octahedron",
        "dodecahedron",
        "icosahedron",
        "cuboctahedron",
    }
    assert set(nets.keys()) == expected_keys
    for key, net in nets.items():
        assert net.unit_edge_verified is True, f"Non-unit edge in {key}"
        assert net.seam_count_verified is True, f"Seam count mismatch in {key}"
        assert net.non_overlapping_verified is True, f"Self-overlap in {key}"
        assert net.euler_characteristic == 2, f"Euler characteristic != 2 in {key}"

    for key in ("tetrahedron", "cube", "cuboctahedron"):
        net_model = gd.polyhedral_net_to_model(nets[key])
        _assert_zero_floats_in_model(net_model)

    assert len(gd.DURER_BOOK4_SOLIDS_CATALOG) >= 12

    persp = gd.construct_durer_perspective_apparatus()
    _assert_zero_floats_in_model(persp.model)
    assert persp.vanishing_point == spg.Point(3, 5)
    assert persp.harmonic_cross_ratio_2d == sp.Integer(-1)
    assert persp.cross_ratio_invariant_verified is True
    assert persp.delian_cube.volume_ratio == sp.Integer(2)
    assert persp.delian_cube.proportion_verified is True


def test_codex_apparatus_tracks_svgs_and_cli(tmp_path: Path) -> None:
    app = gd.load_apparatus()
    assert len(app.concordance) >= 12
    assert "durer" in app.persons
    assert "pirckheimer" in app.persons
    assert "camerarius" in app.persons
    assert "durer:1525" in app.citations
    assert "eierlini" in app.glossary

    codex_dir = REPO_ROOT / "docsrc" / "underweysung"
    units = (
        "unit-1-lines-spirals-conics",
        "unit-2-planes-polygons-tilings",
        "unit-3-architecture-sundials-typography",
        "unit-4-solids-nets-perspective",
    )
    for unit in units:
        for suffix in ("en", "de", "summary", "notes"):
            rst_file = codex_dir / unit / f"{unit}-{suffix}.rst"
            assert rst_file.is_file(), f"Missing track file: {rst_file}"
            content = rst_file.read_text(encoding="utf-8")
            assert len(content) > 400
            assert ".. py_file::" not in content, f"Forbidden py_file in {rst_file}"

    for entry in app.concordance:
        assert entry.unit in units

    fig_dir = REPO_ROOT / "docsrc" / "_static" / "figures"
    svg_files = sorted(fig_dir.glob("*.svg"))
    assert len(svg_files) == 11
    for svg_path in svg_files:
        svg_txt = svg_path.read_text(encoding="utf-8")
        assert 'class="euclid-graphic"' in svg_txt

    svg_sample = gd.render_model_svg(gd.construct_durer_spiral_volute(turns=1).model)
    out_svg = gd.export_svg(svg_sample, tmp_path / "sample.svg")
    assert out_svg.is_file()
    assert 'class="euclid-graphic"' in out_svg.read_text(encoding="utf-8")

    assert cli_main(["audit"]) == 0
    assert cli_main(["nets"]) == 0
