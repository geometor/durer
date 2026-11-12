"""Exact symbolic constructions for Book I spirals & conic projections and Book IV perspective.

Covers two landmark innovations in Albrecht Dürer's *Underweysung der Messung* (1525):

1. **Book I — Spirals & Two-View Descriptive Geometry of Conic Sections** (pp. 011, 018, 034–039):

   - ``construct_durer_spiral_volute``: Exact 12-sector Archimedean spiral (*Schneckenlini*,
     Book I, Figs. 7 & 17) over ``Q(sqrt(3))``.
   - ``construct_durer_conic_sections``: Dürer's orthographic elevation (*Aufriss*) + circular
     ground plan (*Grundriss*) + rotated true-shape section plane for the right circular cone
     (radius ``R = 6``, height ``H = 12``), proving algebraically that his 12-station transfer
     algorithm yields ``w_k^2 = (2/9)*k*(12 - k)``—identically symmetric (``w_{12-k} = w_k``),
     confirming a true Apollonian ellipse rather than an asymmetric *Eierlini* (egg-curve)—alongside
     exact focal and asymptotic laws for the *Parabola / Brennspiegellini* and *Hiperbole / Gabellini*.

2. **Book IV — Central Perspective Apparatus & Delian Cube Duplication** (pp. 159–181):

   - ``construct_durer_perspective_apparatus``: Exact homogeneous ray-plane intersection over ``Q``
     from eye point ``E = (-12, 3, 5)`` onto picture plane ``x = 0`` for cube
     ``[4, 8] x [-2, 2] x [0, 4]``, verifying convergence at principal vanishing point
     ``V_x = (3, 5)``, harmonic cross-ratio invariance ``CR(P4', P8'; P6', V_x) = -1``, and
     Plato's two-mean-proportionals identity ``c^3 = g^2 * e`` for doubling the cube.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, cross_ratio, proposition, zero_test

__all__ = [
    "ConicSectionsResult",
    "DelianCubeCertificate",
    "PerspectiveApparatusResult",
    "SpiralVoluteResult",
    "construct_durer_conic_sections",
    "construct_durer_perspective_apparatus",
    "construct_durer_spiral_volute",
]


@dataclass(frozen=True)
class SpiralVoluteResult:
    """Exact 12-sector Archimedean spiral (*Schneckenlini*, Book I, Figs. 7 & 17) over ``Q(sqrt(3))``."""

    model: Model
    center: spg.Point
    outer_radius: sp.Integer
    sector_count: int
    spiral_points: tuple[spg.Point, ...]
    radii: tuple[sp.Expr, ...]


@dataclass(frozen=True)
class ConicSectionsResult:
    """Exact symbolic audit of Dürer's Book I two-view orthographic conic sections (Figs. 34–37)."""

    model: Model
    cone_radius: sp.Integer
    cone_height: sp.Integer
    ellipse_stations: tuple[tuple[int, sp.Expr, sp.Expr, sp.Expr, sp.Expr], ...]
    ellipse_semi_major: sp.Expr
    ellipse_semi_minor: sp.Expr
    ellipse_focal_distance: sp.Expr
    ellipse_eccentricity: sp.Expr
    ellipse_bilateral_symmetry_verified: bool
    parabola_focal_length: sp.Expr
    hyperbola_semi_transverse: sp.Integer
    hyperbola_semi_conjugate: sp.Integer


@dataclass(frozen=True)
class DelianCubeCertificate:
    """Symbolic verification of Plato's / Sporus's two-mean-proportionals cube duplication."""

    given_g: sp.Expr
    given_e: sp.Expr
    first_mean_c: sp.Expr
    second_mean_d: sp.Expr
    volume_ratio: sp.Expr
    proportion_verified: bool


@dataclass(frozen=True)
class PerspectiveApparatusResult:
    """Exact rational perspective projection of a 3D cube onto Dürer's Book IV glass frame."""

    model: Model
    eye_3d: tuple[sp.Integer, sp.Integer, sp.Integer]
    picture_plane_x: sp.Integer
    vanishing_point: spg.Point
    cube_vertices_3d: dict[str, tuple[sp.Integer, sp.Integer, sp.Integer]]
    projected_vertices_2d: dict[str, spg.Point]
    harmonic_cross_ratio_3d: sp.Rational
    harmonic_cross_ratio_2d: sp.Expr
    cross_ratio_invariant_verified: bool
    delian_cube: DelianCubeCertificate


# Exact cos(k * pi / 6), sin(k * pi / 6) table over Q(sqrt(3)) for k = 0..12
_EXACT_UNIT_CIRCLE_12: tuple[tuple[sp.Expr, sp.Expr], ...] = (
    (sp.Integer(1), sp.Integer(0)),
    (sp.sqrt(3) / 2, sp.Rational(1, 2)),
    (sp.Rational(1, 2), sp.sqrt(3) / 2),
    (sp.Integer(0), sp.Integer(1)),
    (-sp.Rational(1, 2), sp.sqrt(3) / 2),
    (-sp.sqrt(3) / 2, sp.Rational(1, 2)),
    (sp.Integer(-1), sp.Integer(0)),
    (-sp.sqrt(3) / 2, -sp.Rational(1, 2)),
    (-sp.Rational(1, 2), -sp.sqrt(3) / 2),
    (sp.Integer(0), sp.Integer(-1)),
    (sp.Rational(1, 2), -sp.sqrt(3) / 2),
    (sp.sqrt(3) / 2, -sp.Rational(1, 2)),
)


@proposition(
    "Book I, Figs. 7 & 17",
    kind="problem",
    title="Dürer's 12-Sector Archimedean Spiral (Schneckenlini)",
)
def construct_durer_spiral_volute(
    turns: int = 2,
    model: Model | None = None,
) -> SpiralVoluteResult:
    """Construct Dürer's Book I Archimedean spiral over ``Q(sqrt(3))`` using 12 angular sectors.

    Dürer divides the outer circle into 12 radial rays (``1..12``, every ``30°``) and divides the
    outer radius ``R = 12`` into ``12 * turns`` equal radial steps ``r_k = k / turns``, plotting
    ``P_k = (r_k * cos(k * 30°), r_k * sin(k * 30°))`` with 100% exact coordinates in ``Q(sqrt(3))``.
    """
    if turns < 1:
        raise ValueError("turns must be >= 1")
    if model is None:
        model = Model("durer_spiral_volute", logger=False, auto_intersect=False)

    outer_r = sp.Integer(12)
    center = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="O")
    rim_east = model.set_point(outer_r, sp.Integer(0), classes=["frame"], ID="R0")
    model.construct_circle(center, rim_east, classes=["outer_circle"], ID="c_outer")

    # 12 radial spokes
    for s_idx in range(6):
        cx, sy = _EXACT_UNIT_CIRCLE_12[s_idx]
        p_pos = model.set_point(outer_r * cx, outer_r * sy, classes=["sector_rim"])
        p_neg = model.set_point(-outer_r * cx, -outer_r * sy, classes=["sector_rim"])
        model.set_segment(p_neg, p_pos, classes=["sector_ray"])

    total_steps = 12 * turns
    pts: list[spg.Point] = [center]
    radii: list[sp.Expr] = [sp.Integer(0)]

    for k in range(1, total_steps + 1):
        rk = sp.Rational(k, turns)
        cx, sy = _EXACT_UNIT_CIRCLE_12[k % 12]
        px = sp.simplify(rk * cx)
        py = sp.simplify(rk * sy)
        pt = model.set_point(px, py, classes=["spiral_pt"], ID=f"S{k}")
        model.set_segment(pts[-1], pt, classes=["spiral_chord"])
        pts.append(pt)
        radii.append(rk)

    return SpiralVoluteResult(
        model=model,
        center=center,
        outer_radius=outer_r,
        sector_count=12,
        spiral_points=tuple(pts),
        radii=tuple(radii),
    )


@proposition(
    "Book I, Figs. 34–37",
    kind="theorem",
    title="Dürer's Two-View Orthographic Projection of Conic Sections",
)
def construct_durer_conic_sections(model: Model | None = None) -> ConicSectionsResult:
    """Construct Dürer's Book I elevation + ground-plan + true-section diagram for the ellipse.

    Also computes exact focal and asymptotic invariants for Dürer's *Parabola* (*Brennspiegellini*)
    and *Hiperbole* (*Gabellini*).
    """
    if model is None:
        model = Model("durer_conic_sections", logger=False, auto_intersect=False)

    R = sp.Integer(6)
    H = sp.Integer(12)

    # -------------------------------------------------------------------------
    # View 1: Elevation Cone (Aufriss) centered on x=0, z in [0, 12]
    # -------------------------------------------------------------------------
    apex_a = model.set_point(sp.Integer(0), H, classes=["cone_frame"], ID="Apex")
    base_l = model.set_point(-R, sp.Integer(0), classes=["cone_frame"], ID="Base_L")
    base_r = model.set_point(R, sp.Integer(0), classes=["cone_frame"], ID="Base_R")
    model.set_polygon([base_l, base_r, apex_a], classes=["cone_elevation"])

    # Oblique cutting plane FG from F=(-4, 4) on left generator to G=(2, 8) on right generator
    f_cut = model.set_point(sp.Integer(-4), sp.Integer(4), classes=["cut_key"], ID="f")
    g_cut = model.set_point(sp.Integer(2), sp.Integer(8), classes=["cut_key"], ID="g")
    model.set_segment(f_cut, g_cut, classes=["cut_plane"])

    # -------------------------------------------------------------------------
    # View 2: Circular Ground Plan (Grundriss) centered at (0, -9) below the cone
    # -------------------------------------------------------------------------
    plan_cy = sp.Integer(-9)
    plan_o = model.set_point(sp.Integer(0), plan_cy, classes=["plan_center"], ID="O_plan")
    plan_rim = model.set_point(R, plan_cy, classes=["plan_frame"])
    model.construct_circle(plan_o, plan_rim, classes=["plan_base_circle"])

    # -------------------------------------------------------------------------
    # View 3: True-Shape Section (Elipsis) plotted vertically to the right at x_sec = 12
    # -------------------------------------------------------------------------
    sec_cx = sp.Integer(12)
    sec_y0 = sp.Integer(0)

    # Unit step along FG has length sqrt(52)/12 = sqrt(13)/6
    step_s = sp.sqrt(13) / sp.Integer(6)

    stations: list[tuple[int, sp.Expr, sp.Expr, sp.Expr, sp.Expr]] = []
    upper_curve_pts: list[spg.Point] = []
    lower_curve_pts: list[spg.Point] = []

    for k in range(13):
        xk = sp.Integer(-4) + sp.Rational(k, 2)
        zk = sp.Integer(4) + sp.Rational(k, 3)
        rk = sp.Integer(4) - sp.Rational(k, 6)
        # Exact chord half-width w_k = sqrt(r_k^2 - x_k^2) = sqrt(2*k*(12 - k)) / 3
        wk = sp.simplify(sp.sqrt(rk**2 - xk**2))
        stations.append((k, xk, zk, rk, wk))

        # Elevation station & horizontal cone slice
        p_elev = model.set_point(xk, zk, classes=["station_pt"])
        slice_l = model.set_point(-rk, zk, classes=["cone_slice_pt"])
        slice_r = model.set_point(rk, zk, classes=["cone_slice_pt"])
        if k in (2, 4, 6, 8, 10):
            model.set_segment(slice_l, slice_r, classes=["cone_slice"])
            # Vertical projector down to plan chord (xk, plan_cy +/- wk)
            p_plan_top = model.set_point(xk, plan_cy + wk, classes=["plan_chord_pt"])
            p_plan_bot = model.set_point(xk, plan_cy - wk, classes=["plan_chord_pt"])
            model.set_segment(p_elev, p_plan_top, classes=["projector_line"])
            model.set_segment(p_plan_bot, p_plan_top, classes=["plan_chord"])
            # Concentric horizontal-section circle in ground plan
            p_ring = model.set_point(rk, plan_cy, classes=["aux"])
            model.construct_circle(plan_o, p_ring, classes=["plan_section_circle"])

        # True-shape ellipse coordinates (s_k = k * step_s, +/- w_k)
        sk_y = sec_y0 + k * step_s
        pt_r = model.set_point(sec_cx + wk, sk_y, classes=["ellipse_pt"])
        pt_l = model.set_point(sec_cx - wk, sk_y, classes=["ellipse_pt"])
        upper_curve_pts.append(pt_r)
        lower_curve_pts.append(pt_l)
        if 0 < k < 12:
            model.set_segment(pt_l, pt_r, classes=["ellipse_ordinate"])

    # Axis of true ellipse & polygonal chord chain
    model.set_segment(upper_curve_pts[0], upper_curve_pts[-1], classes=["ellipse_axis"])
    for idx in range(12):
        model.set_segment(upper_curve_pts[idx], upper_curve_pts[idx + 1], classes=["ellipse_arc"])
        model.set_segment(lower_curve_pts[idx], lower_curve_pts[idx + 1], classes=["ellipse_arc"])

    # Verify exact bilateral symmetry w_k == w_{12 - k} for all k = 0..12
    sym_ok = all(zero_test(stations[k][4] - stations[12 - k][4]) for k in range(13))

    semi_a = sp.sqrt(13)
    semi_b = sp.Integer(2) * sp.sqrt(2)
    focal_c = sp.simplify(sp.sqrt(semi_a**2 - semi_b**2))  # sqrt(5)
    ecc = sp.simplify(focal_c / semi_a)

    # Parabola cut x = z/2 on the same cone: w(z)^2 = 6*(6 - z) = (12/sqrt(5))*s => f = 3*sqrt(5)/5
    parabola_f = sp.Rational(3, 5) * sp.sqrt(5)

    # Hyperbola cut x = 2 parallel to axis: (12 - z)^2 / 16 - w^2 / 4 = 1 => a_h = 4, b_h = 2
    hyp_a = sp.Integer(4)
    hyp_b = sp.Integer(2)

    return ConicSectionsResult(
        model=model,
        cone_radius=R,
        cone_height=H,
        ellipse_stations=tuple(stations),
        ellipse_semi_major=semi_a,
        ellipse_semi_minor=semi_b,
        ellipse_focal_distance=focal_c,
        ellipse_eccentricity=ecc,
        ellipse_bilateral_symmetry_verified=sym_ok,
        parabola_focal_length=parabola_f,
        hyperbola_semi_transverse=hyp_a,
        hyperbola_semi_conjugate=hyp_b,
    )


@proposition(
    "Book IV, Figs. 50 & 56–63",
    kind="theorem",
    title="Dürer's Perspective Glass Apparatus & Delian Cube Duplication",
)
def construct_durer_perspective_apparatus(
    model: Model | None = None,
) -> PerspectiveApparatusResult:
    """Project a 3D cube in ``Q^3`` onto Dürer's picture plane ``x = 0`` from eye ``E(-12, 3, 5)``.

    Verifies:

    1. Exact rational screen coordinates ``(y', z') in Q^2`` for all 8 cube vertices.
    2. Exact convergence of all 4 depth edges at principal vanishing point ``V_x = (3, 5)``.
    3. Exact projective cross-ratio invariance ``CR(P4', P8'; P6', V_x) = -1`` (harmonic range!).
    4. Exact algebraic verification of Plato's / Sporus's two mean proportionals (Book IV, Fig. 50)
       for doubling the cube (``g = 1, e = 2 => c = 2^(1/3), d = 2^(2/3), c^3 = 2``).
    """
    if model is None:
        model = Model("durer_perspective_apparatus", logger=False, auto_intersect=False)

    ex, ey, ez = sp.Integer(-12), sp.Integer(3), sp.Integer(5)
    plane_x = sp.Integer(0)

    def _project(px: sp.Expr, py: sp.Expr, pz: sp.Expr) -> tuple[sp.Rational, sp.Rational]:
        # Ray E + t*(P - E) meets x = 0 at t = (0 - ex) / (px - ex)
        t_param = sp.Rational(plane_x - ex, px - ex)
        yp = sp.Rational(ey + t_param * (py - ey))
        zp = sp.Rational(ez + t_param * (pz - ez))
        return yp, zp

    # Glass picture frame outline on x = 0: y in [-3, 4], z in [-1, 6]
    fr_bl = model.set_point(sp.Integer(-3), sp.Integer(-1), classes=["glass_frame"])
    fr_br = model.set_point(sp.Rational(9, 2), sp.Integer(-1), classes=["glass_frame"])
    fr_tr = model.set_point(sp.Rational(9, 2), sp.Integer(6), classes=["glass_frame"])
    fr_tl = model.set_point(sp.Integer(-3), sp.Integer(6), classes=["glass_frame"])
    model.set_polygon([fr_bl, fr_br, fr_tr, fr_tl], classes=["glass_frame_rect"])

    cube_3d: dict[str, tuple[sp.Integer, sp.Integer, sp.Integer]] = {
        "F_BL": (sp.Integer(4), sp.Integer(-2), sp.Integer(0)),
        "F_BR": (sp.Integer(4), sp.Integer(2), sp.Integer(0)),
        "F_TR": (sp.Integer(4), sp.Integer(2), sp.Integer(4)),
        "F_TL": (sp.Integer(4), sp.Integer(-2), sp.Integer(4)),
        "B_BL": (sp.Integer(8), sp.Integer(-2), sp.Integer(0)),
        "B_BR": (sp.Integer(8), sp.Integer(2), sp.Integer(0)),
        "B_TR": (sp.Integer(8), sp.Integer(2), sp.Integer(4)),
        "B_TL": (sp.Integer(8), sp.Integer(-2), sp.Integer(4)),
    }

    proj_2d: dict[str, spg.Point] = {}
    for name, (px, py, pz) in cube_3d.items():
        yp, zp = _project(px, py, pz)
        proj_2d[name] = model.set_point(yp, zp, classes=["cube_vertex"], ID=name)

    # Front and back face polygons + 4 receding edges
    model.set_polygon(
        [proj_2d["F_BL"], proj_2d["F_BR"], proj_2d["F_TR"], proj_2d["F_TL"]],
        classes=["cube_front_face"],
    )
    model.set_polygon(
        [proj_2d["B_BL"], proj_2d["B_BR"], proj_2d["B_TR"], proj_2d["B_TL"]],
        classes=["cube_back_face"],
    )

    receding_lines: list[spg.Line] = []
    for corner in ("BL", "BR", "TR", "TL"):
        pf = proj_2d[f"F_{corner}"]
        pb = proj_2d[f"B_{corner}"]
        model.set_segment(pf, pb, classes=["cube_depth_edge"])
        receding_lines.append(model.construct_line(pf, pb, classes=["vanishing_ray"]))

    # Intersect receding lines in Model to verify exact convergence at V_x = (3, 5)
    vp_pts = model.intersect_all(receding_lines[0], receding_lines[1], classes=["vanishing_point"])
    if len(vp_pts) != 1:
        raise ValueError("Expected unique vanishing point V_x")
    v_x = model.set_point(vp_pts[0].x, vp_pts[0].y, classes=["vanishing_point"], ID="V_x")
    for r_line in receding_lines[2:]:
        if not r_line.contains(v_x):
            raise ValueError("Receding cube edge failed to pass through V_x")

    #Sighting ray segments from Cube vertices to V_x
    for corner in ("BL", "BR", "TR", "TL"):
        model.set_segment(proj_2d[f"B_{corner}"], v_x, classes=["sight_ray"])

    # Projective cross-ratio check along lower-left depth edge (x = 4, 6, 8, infinity):
    # In 3D along x-line, (4, 8; 6, infinity) has exact harmonic cross-ratio -1!
    mid_yp, mid_zp = _project(sp.Integer(6), sp.Integer(-2), sp.Integer(0))
    p6_2d = model.set_point(mid_yp, mid_zp, classes=["harmonic_mid"], ID="M_depth")

    cr_3d = sp.Rational(-1)
    cr_2d = sp.simplify(cross_ratio(proj_2d["F_BL"], proj_2d["B_BL"], p6_2d, v_x))
    cr_ok = zero_test(cr_2d - cr_3d)

    # Delian Doubling of the Cube certificate (Book IV, Fig. 50):
    # g = 1, e = 2 => c = 2^(1/3), d = 2^(2/3) satisfy c^2 = g*d and d^2 = c*e => c^3 = 2*g^3
    g_val = sp.Integer(1)
    e_val = sp.Integer(2)
    c_val = sp.cbrt(2)
    d_val = sp.cbrt(4)
    prop_ok = zero_test(c_val**2 - g_val * d_val) and zero_test(d_val**2 - c_val * e_val)
    vol_ratio = sp.simplify(c_val**3 / g_val**3)

    delian = DelianCubeCertificate(
        given_g=g_val,
        given_e=e_val,
        first_mean_c=c_val,
        second_mean_d=d_val,
        volume_ratio=vol_ratio,
        proportion_verified=prop_ok and zero_test(vol_ratio - 2),
    )

    return PerspectiveApparatusResult(
        model=model,
        eye_3d=(ex, ey, ez),
        picture_plane_x=plane_x,
        vanishing_point=v_x,
        cube_vertices_3d=cube_3d,
        projected_vertices_2d=proj_2d,
        harmonic_cross_ratio_3d=cr_3d,
        harmonic_cross_ratio_2d=cr_2d,
        cross_ratio_invariant_verified=cr_ok,
        delian_cube=delian,
    )
