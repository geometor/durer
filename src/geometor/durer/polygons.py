"""Exact symbolic constructions & workshop audits for Book II regular polygons and quadrature.

Covers Albrecht Dürer's *Underweysung der Messung* (1525), Book II:

- **Figs. 15 & 16 (pp. 058–059)**: Direct symbolic comparison between:

  1. **Euclid / Ptolemy's exact regular pentagon** over ``Q(phi)`` (``phi = (1 + sqrt(5))/2``),
     marked *demonstrative* by Dürer, with exact interior angle ``108°`` and diagonal-to-side
     ratio ``phi``.
  2. **Dürer's Single-Aperture ("Rusty Compass") Pentagon** (*mit unverrucktem Zirckel*, inherited
     from Abū al-Wafāʾ and *Geometria Deutsch*), which constructs all five sides with exact unit
     quadrance ``Q = 1`` and exact bilateral symmetry using a single fixed compass opening, but
     yields nested quadratic-radical vertices whose base interior angle is ``~108.3660°``
     (``+0.3660°``, or ``~21.96'`` arcminutes too wide).
- **Figs. 11 & 15 (pp. 057–059)**: Dürer's workshop regular heptagon (*7-gon*), taking half the
  side of the inscribed equilateral triangle ``s_7 = (sqrt(3)/2) * R`` (``Q = 3/4 * R^2``),
  audited against the irreducible cubic minimal polynomial ``P_7(q) = q^3 - 7*q^2 + 14*q - 7``
  (Eisenstein at ``p = 7``), with exact rational residual ``P_7(3/4) = -1/64``.
- **Fig. 19 (pp. 060–061)**: Workshop *mechanice* rules for the ``11``-gon (``s_11 = 9/16 * R``)
  and ``13``-gon (``s_13 = 1/2 * R``).
- **Fig. 34 (p. 075)**: Workshop quadrature of the circle (square diagonal ``10`` parts, circle
  diameter ``8`` parts, implying ``pi_Durer = 25/8 = 3.125``).
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, clean_expr, line_spread, proposition, quadrance, zero_test

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)

__all__ = [
    "PHI",
    "HeptagonWorkshopReport",
    "PentagonComparisonResult",
    "WorkshopPolygonEntry",
    "construct_durer_heptagon_workshop",
    "construct_durer_vs_euclid_pentagon",
]


@dataclass(frozen=True)
class PentagonComparisonResult:
    """Exact symbolic result comparing Dürer's single-aperture pentagon with Euclid's pentagon."""

    model: Model
    base_a: spg.Point
    base_b: spg.Point
    durer_vertices: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    euclid_vertices: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    durer_aux_points: dict[str, spg.Point]
    durer_side_quadrances: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    euclid_side_quadrances: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    euclid_diagonal_quadrance: sp.Expr
    durer_base_diagonal_quadrance: sp.Expr
    durer_shoulder_diagonal_quadrance: sp.Expr
    durer_base_spread: sp.Expr
    euclid_base_spread: sp.Expr
    durer_equilateral: bool
    durer_equiangular: bool
    euclid_regular: bool

    @property
    def durer_base_interior_deg(self) -> float:
        """Numerical evaluation (degrees) of Dürer's interior angle at A and B."""
        a, b, h, _, _ = self.durer_vertices
        dx = float((h.x - b.x).evalf(30))
        dy = float((h.y - b.y).evalf(30))
        # Vector BA is (-1, 0); interior angle between BA and BH is 180° - atan2(dy, dx)
        import math

        return 180.0 - math.degrees(math.atan2(dy, dx))

    @property
    def base_angle_error_deg(self) -> float:
        """Signed error (degrees) of Dürer's base interior angle relative to exact 108°."""
        return self.durer_base_interior_deg - 108.0

    @property
    def base_angle_error_arcmin(self) -> float:
        """Signed error (arcminutes) of Dürer's base interior angle relative to exact 108°."""
        return self.base_angle_error_deg * 60.0


@dataclass(frozen=True)
class WorkshopPolygonEntry:
    """Exact algebraic vs. trigonometric audit for one of Dürer's Book II workshop rules."""

    n_sides: int
    durer_label: str
    classification: str
    exact_chord_over_r: sp.Expr
    exact_quadrance_over_r2: sp.Expr
    true_chord_over_r_float: float
    relative_chord_error: float
    central_angle_durer_deg: float
    central_angle_true_deg: float


@dataclass(frozen=True)
class HeptagonWorkshopReport:
    """Exact symbolic construction & cubic-impossibility audit for Dürer's Book II heptagon."""

    model: Model
    center: spg.Point
    circumcircle: spg.Circle
    equilateral_chord_top: spg.Point
    equilateral_chord_bottom: spg.Point
    radius_midpoint: spg.Point
    workshop_vertices: tuple[spg.Point, ...]
    durer_chord_quadrance: sp.Rational
    minimal_polynomial_expr: sp.Expr
    minimal_polynomial_at_durer: sp.Rational
    eisenstein_prime: int
    quadrature_circle_diameter_over_side: sp.Expr
    quadrature_implied_pi: sp.Rational
    workshop_catalog: tuple[WorkshopPolygonEntry, ...]


def _select_point(
    pts: list[spg.Point],
    predicate,
    label: str,
) -> spg.Point:
    matches = [pt for pt in pts if predicate(pt)]
    if len(matches) != 1:
        raise ValueError(f"Expected 1 intersection for {label}, got {len(matches)}: {pts}")
    return matches[0]


@proposition(
    "Book II, Figs. 15–16",
    kind="problem",
    title="Dürer's Single-Aperture Pentagon vs. Euclid's Golden-Section Pentagon",
)
def construct_durer_vs_euclid_pentagon(model: Model | None = None) -> PentagonComparisonResult:
    """Construct Dürer's single-aperture pentagon and Euclid's exact pentagon on base ``AB``.

    Parameters
    ----------
    model : Model | None
        Optional existing ``geometor.model.Model`` (created with ``auto_intersect=False`` if omitted).

    Returns
    -------
    PentagonComparisonResult
        Exact symbolic coordinates, quadrances, spreads, and regularity audit.
    """
    if model is None:
        model = Model("durer_vs_euclid_pentagon", logger=False, auto_intersect=False)

    # Given: unit base segment AB from A=(0,0) to B=(1,0)
    A = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="A")
    B = model.set_point(sp.Integer(1), sp.Integer(0), classes=["given"], ID="B")
    line_ab = model.construct_line(A, B, classes=["given"], ID="AB")

    # -------------------------------------------------------------------------
    # Part 1: Dürer's Single-Aperture ("Rusty Compass") Pentagon (Book II, Fig. 16)
    # Fixed compass opening r = |AB| = 1 throughout.
    # -------------------------------------------------------------------------
    c_a = model.construct_circle(A, B, classes=["durer_aux"], ID="c_A")
    c_b = model.construct_circle(B, A, classes=["durer_aux"], ID="c_B")

    vesica_pts = model.intersect_all(c_a, c_b, classes=["durer_aux"])
    C_ves = _select_point(vesica_pts, lambda p: bool(p.y.evalf() > 0), "C_ves")
    D = _select_point(vesica_pts, lambda p: bool(p.y.evalf() < 0), "D")
    model.set_point(C_ves.x, C_ves.y, classes=["durer_aux"], ID="C_ves")
    model.set_point(D.x, D.y, classes=["durer_aux"], ID="D")

    sym_axis = model.construct_line(C_ves, D, classes=["symmetry_axis"], ID="CD")

    # Third unit circle centered at D through A (and B)
    c_d = model.construct_circle(D, A, classes=["durer_aux"], ID="c_D")

    pts_da = model.intersect_all(c_d, c_a, classes=["durer_aux"])
    E = _select_point(pts_da, lambda p: bool(p.x.evalf() < 0), "E")
    model.set_point(E.x, E.y, classes=["durer_aux"], ID="E")

    pts_db = model.intersect_all(c_d, c_b, classes=["durer_aux"])
    F = _select_point(pts_db, lambda p: bool(p.x.evalf() > 1), "F")
    model.set_point(F.x, F.y, classes=["durer_aux"], ID="F")

    pts_dsym = model.intersect_all(c_d, sym_axis, classes=["durer_aux"])
    G = _select_point(pts_dsym, lambda p: bool(p.y.evalf() > float(D.y.evalf())), "G")
    model.set_point(G.x, G.y, classes=["durer_aux"], ID="G")

    # Sighting lines EG and FG (exact slope +1 and -1)
    line_eg = model.construct_line(E, G, classes=["durer_ray"], ID="EG")
    line_fg = model.construct_line(F, G, classes=["durer_ray"], ID="FG")

    pts_h = model.intersect_all(line_eg, c_b, classes=["durer_vertex"])
    H_durer = _select_point(pts_h, lambda p: bool(p.x.evalf() > 1 and p.y.evalf() > 0), "H_durer")
    H_durer = model.set_point(
        clean_expr(H_durer.x),
        clean_expr(H_durer.y),
        classes=["durer_vertex"],
        ID="H_durer",
    )

    pts_i = model.intersect_all(line_fg, c_a, classes=["durer_vertex"])
    I_durer = _select_point(pts_i, lambda p: bool(p.x.evalf() < 0 and p.y.evalf() > 0), "I_durer")
    I_durer = model.set_point(
        clean_expr(I_durer.x),
        clean_expr(I_durer.y),
        classes=["durer_vertex"],
        ID="I_durer",
    )

    # Pure single-aperture top arcs: H_durer lies on c_B so |H_durer B| = 1,
    # and I_durer lies on c_A so |I_durer A| = 1!
    c_h = model.construct_circle(H_durer, B, classes=["durer_aux"], ID="c_H")
    c_i = model.construct_circle(I_durer, A, classes=["durer_aux"], ID="c_I")

    pts_k = model.intersect_all(c_h, c_i, classes=["durer_vertex"])
    K_durer = _select_point(pts_k, lambda p: bool(p.y.evalf() > 1), "K_durer")
    K_durer = model.set_point(
        clean_expr(K_durer.x),
        clean_expr(K_durer.y),
        classes=["durer_vertex"],
        ID="K_durer",
    )

    durer_vertices = (A, B, H_durer, K_durer, I_durer)
    model.set_polygon(list(durer_vertices), classes=["durer_pentagon"])

    # -------------------------------------------------------------------------
    # Part 2: Exact Euclidean Regular Pentagon on Base AB over Q(phi)
    # -------------------------------------------------------------------------
    pts_mid = model.intersect_all(sym_axis, line_ab, classes=["euclid_aux"])
    M_ab = _select_point(pts_mid, lambda _: True, "M_ab")
    M_ab = model.set_point(M_ab.x, M_ab.y, classes=["euclid_aux"], ID="M_AB")

    # Erect perpendicular at B of unit height: P_perp = (1, 1) via circle around B
    # Using exact point (1, 1) constructed from perpendicular at B meeting c_B:
    # Line through B perpendicular to AB: construct via circle(M_AB, C_ves)? Let's use pure compass:
    # Extend AB to B2=(2,0) by intersecting c_B with line_ab:
    pts_b_line = model.intersect_all(c_b, line_ab, classes=["euclid_aux"])
    B_ext = _select_point(pts_b_line, lambda p: bool(p.x.evalf() > 1), "B_ext")
    c_a_bext = model.construct_circle(A, B_ext, classes=["euclid_aux"])
    c_bext_a = model.construct_circle(B_ext, A, classes=["euclid_aux"])
    perp_b_pts = model.intersect_all(c_a_bext, c_bext_a, classes=["euclid_aux"])
    P_b_top = _select_point(perp_b_pts, lambda p: bool(p.y.evalf() > 0), "P_b_top")
    perp_b = model.construct_line(B, P_b_top, classes=["euclid_aux"])

    pts_b_unit = model.intersect_all(perp_b, c_b, classes=["euclid_aux"])
    N_unit = _select_point(pts_b_unit, lambda p: bool(p.y.evalf() > 0), "N_unit")

    # Golden-section arc centered at M_AB=(1/2, 0) through N_unit=(1, 1) of radius sqrt(5)/2
    c_golden = model.construct_circle(M_ab, N_unit, classes=["euclid_aux"], ID="c_golden")
    golden_pts = model.intersect_all(c_golden, line_ab, classes=["euclid_aux"])
    X_phi = _select_point(golden_pts, lambda p: bool(p.x.evalf() > 1), "X_phi")
    X_phi_left = _select_point(golden_pts, lambda p: bool(p.x.evalf() < 0), "X_phi_left")
    X_phi = model.set_point(
        sp.simplify(X_phi.x), sp.Integer(0), classes=["euclid_aux"], ID="X_phi"
    )
    X_phi_left = model.set_point(
        sp.simplify(X_phi_left.x), sp.Integer(0), classes=["euclid_aux"], ID="X_phi_left"
    )

    # Diagonal circles of radius phi centered at A and B
    c_diag_a = model.construct_circle(A, X_phi, classes=["euclid_aux"], ID="c_diag_A")
    c_diag_b = model.construct_circle(B, X_phi_left, classes=["euclid_aux"], ID="c_diag_B")

    pts_he = model.intersect_all(c_diag_a, c_b, classes=["euclid_vertex"])
    H_euclid = _select_point(pts_he, lambda p: bool(p.y.evalf() > 0), "H_euclid")
    H_euclid = model.set_point(
        sp.simplify(H_euclid.x),
        sp.simplify(H_euclid.y),
        classes=["euclid_vertex"],
        ID="H_euclid",
    )

    pts_ie = model.intersect_all(c_diag_b, c_a, classes=["euclid_vertex"])
    I_euclid = _select_point(pts_ie, lambda p: bool(p.y.evalf() > 0), "I_euclid")
    I_euclid = model.set_point(
        sp.simplify(I_euclid.x),
        sp.simplify(I_euclid.y),
        classes=["euclid_vertex"],
        ID="I_euclid",
    )

    pts_ke = model.intersect_all(c_diag_a, c_diag_b, classes=["euclid_vertex"])
    K_euclid = _select_point(pts_ke, lambda p: bool(p.y.evalf() > 0), "K_euclid")
    K_euclid = model.set_point(
        sp.simplify(K_euclid.x),
        sp.simplify(K_euclid.y),
        classes=["euclid_vertex"],
        ID="K_euclid",
    )

    euclid_vertices = (A, B, H_euclid, K_euclid, I_euclid)
    model.set_polygon(list(euclid_vertices), classes=["euclid_pentagon"])

    # -------------------------------------------------------------------------
    # Exact Rational Trigonometry Invariants (Quadrances & Spreads)
    # -------------------------------------------------------------------------
    durer_side_q = tuple(
        sp.simplify(quadrance(durer_vertices[idx], durer_vertices[(idx + 1) % 5]))
        for idx in range(5)
    )
    euclid_side_q = tuple(
        sp.simplify(quadrance(euclid_vertices[idx], euclid_vertices[(idx + 1) % 5]))
        for idx in range(5)
    )

    euclid_diag_q = sp.simplify(quadrance(A, H_euclid))
    durer_base_diag_q = sp.simplify(quadrance(A, H_durer))
    durer_shoulder_diag_q = sp.simplify(quadrance(I_durer, H_durer))

    line_bh_durer = spg.Line(B, H_durer)
    line_bh_euclid = spg.Line(B, H_euclid)
    durer_base_s = sp.simplify(line_spread(line_ab, line_bh_durer))
    euclid_base_s = sp.simplify(line_spread(line_ab, line_bh_euclid))

    durer_equilateral = all(zero_test(q - 1) for q in durer_side_q)
    # A convex equilateral pentagon is equiangular (regular) iff all 5 diagonals are equal
    durer_equiangular = zero_test(durer_base_diag_q - durer_shoulder_diag_q)

    euclid_diags = [
        quadrance(euclid_vertices[idx], euclid_vertices[(idx + 2) % 5]) for idx in range(5)
    ]
    euclid_regular = all(zero_test(q - 1) for q in euclid_side_q) and all(
        zero_test(dq - PHI**2) for dq in euclid_diags
    )

    return PentagonComparisonResult(
        model=model,
        base_a=A,
        base_b=B,
        durer_vertices=durer_vertices,
        euclid_vertices=euclid_vertices,
        durer_aux_points={"C_ves": C_ves, "D": D, "E": E, "F": F, "G": G, "M_AB": M_ab},
        durer_side_quadrances=durer_side_q,
        euclid_side_quadrances=euclid_side_q,
        euclid_diagonal_quadrance=euclid_diag_q,
        durer_base_diagonal_quadrance=durer_base_diag_q,
        durer_shoulder_diagonal_quadrance=durer_shoulder_diag_q,
        durer_base_spread=durer_base_s,
        euclid_base_spread=euclid_base_s,
        durer_equilateral=durer_equilateral,
        durer_equiangular=durer_equiangular,
        euclid_regular=euclid_regular,
    )


@proposition(
    "Book II, Figs. 11, 15, 19 & 34",
    kind="problem",
    title="Dürer's Workshop Regular Heptagon, 11/13-gons, and Circle Quadrature Audit",
)
def construct_durer_heptagon_workshop(model: Model | None = None) -> HeptagonWorkshopReport:
    """Construct Dürer's workshop regular heptagon in the unit circle and audit its cubic residual.

    In Book II, Figs. 11 & 15, Dürer sets the heptagon chord equal to the half-side of the
    inscribed equilateral triangle: ``s_7 = sqrt(3)/2 * R`` (``Q_Durer = 3/4`` for ``R = 1``).
    The true regular heptagon chord quadrance ``Q_7 = 2*(1 - cos(2*pi/7))`` is a root of the
    Eisenstein-irreducible cubic ``P_7(q) = q^3 - 7*q^2 + 14*q - 7 = 0``, yielding the exact
    non-zero rational residual ``P_7(3/4) = -1/64``.
    """
    import math

    if model is None:
        model = Model("durer_heptagon_workshop", logger=False, auto_intersect=False)

    O_pt = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="O")
    B_right = model.set_point(sp.Integer(1), sp.Integer(0), classes=["given"], ID="B")
    C_left = model.set_point(sp.Integer(-1), sp.Integer(0), classes=["given"], ID="C")

    diam_bc = model.construct_line(C_left, B_right, classes=["given"], ID="BC")
    circum = model.construct_circle(O_pt, B_right, classes=["given"], ID="circumcircle")

    # Dürer Fig. 15: Circle centered at B=(1,0) through O=(0,0) bisects OB at E=(1/2,0)
    # and cuts circumcircle at T1=(1/2, sqrt(3)/2), T2=(1/2, -sqrt(3)/2)
    c_bisect = model.construct_circle(B_right, O_pt, classes=["aux"], ID="c_bisect")
    eq_pts = model.intersect_all(circum, c_bisect, classes=["aux"])
    T_top = _select_point(eq_pts, lambda p: bool(p.y.evalf() > 0), "T_top")
    T_bot = _select_point(eq_pts, lambda p: bool(p.y.evalf() < 0), "T_bot")
    T_top = model.set_point(T_top.x, T_top.y, classes=["heptagon_gauge"], ID="T_top")
    T_bot = model.set_point(T_bot.x, T_bot.y, classes=["heptagon_gauge"], ID="T_bot")

    chord_t = model.construct_line(T_top, T_bot, classes=["heptagon_gauge"], ID="T_chord")
    mid_pts = model.intersect_all(chord_t, diam_bc, classes=["heptagon_gauge"])
    E_mid = _select_point(mid_pts, lambda _: True, "E_mid")
    E_mid = model.set_point(E_mid.x, E_mid.y, classes=["heptagon_gauge"], ID="E")

    # Segment E -> T_top has exact length sqrt(3)/2 (quadrance 3/4)
    durer_q = sp.Rational(3, 4)
    if not zero_test(quadrance(E_mid, T_top) - durer_q):
        raise ValueError("Expected quadrance(E, T_top) == 3/4")

    # Step off chord length sqrt(3)/2 counterclockwise around the unit circle starting at W0 = (0, 1)
    W0 = model.set_point(sp.Integer(0), sp.Integer(1), classes=["heptagon_vertex"], ID="W0")
    vertices: list[spg.Point] = [W0]

    # Exact rotation step on unit circle corresponding to chord s = sqrt(3)/2:
    # 2*(1 - cos(alpha)) = 3/4  =>  cos(alpha) = 5/8,  sin(alpha) = sqrt(39)/8!
    # Look at that: cos(alpha) = 5/8 and sin(alpha) = sqrt(39)/8 are in Q(sqrt(39)),
    # AND each step on the circle is intersected via compass circle of radius sqrt(3)/2!
    cos_a = sp.Rational(5, 8)
    sin_a = sp.sqrt(39) / sp.Integer(8)

    curr = W0
    for step_idx in range(1, 8):
        # Counterclockwise rotation of curr=(x, y) by alpha where chord quadrance is 3/4:
        nx = sp.simplify(curr.x * cos_a - curr.y * sin_a)
        ny = sp.simplify(curr.x * sin_a + curr.y * cos_a)
        # Verify it lies on unit circle and at exact compass quadrance 3/4 from curr
        cand = spg.Point(nx, ny)
        if not (zero_test(quadrance(O_pt, cand) - 1) and zero_test(quadrance(curr, cand) - durer_q)):
            raise ValueError(f"Step {step_idx} failed exact unit-circle / compass-quadrance check")
        cls = ["heptagon_vertex"] if step_idx < 7 else ["heptagon_overshoot"]
        pt = model.set_point(nx, ny, classes=cls, ID=f"W{step_idx}")
        model.set_segment(curr, pt, classes=["heptagon_side"])
        vertices.append(pt)
        curr = pt

    # Minimal cubic polynomial for exact regular heptagon chord quadrance Q_7 = 2*(1 - cos(2*pi/7)):
    # Since 8*c^3 + 4*c^2 - 4*c - 1 = 0 for c = cos(2*pi/7) = 1 - q/2,
    # substituting c = 1 - q/2 gives -(q^3 - 7*q^2 + 14*q - 7) = 0!
    q_sym = sp.Symbol("q")
    min_poly = q_sym**3 - 7 * q_sym**2 + 14 * q_sym - 7
    residual = sp.Rational(min_poly.subs(q_sym, durer_q))

    # Quadrature of the circle (Book II, Fig. 34, p. 075):
    # Square side a = 1, diagonal sqrt(2) divided into 10 parts, circle diameter = 8 parts
    d_over_a = sp.Rational(4, 5) * sp.sqrt(2)
    # pi * (d/2)^2 = 1  =>  pi_Durer = 4 / d^2 = 4 / (32/25) = 25/8 = 3.125
    pi_durer = sp.Rational(25, 8)

    # Build complete Book II workshop vs. demonstrative catalog
    entries: list[WorkshopPolygonEntry] = []
    specs = [
        (
            5,
            "Euclid / Ptolemy Inscribed Pentagon (Fig. 15)",
            "demonstrative",
            sp.sqrt(sp.Integer(10) - sp.Integer(2) * sp.sqrt(5)) / sp.Integer(2),
        ),
        (
            7,
            "Equilateral Half-Side Heptagon (Figs. 11 & 15)",
            "mechanice",
            sp.sqrt(3) / sp.Integer(2),
        ),
        (
            11,
            "Quarter-Diameter Nine-Eighths Hendecagon (Fig. 19)",
            "mechanice",
            sp.Rational(9, 16),
        ),
        (
            13,
            "Quarter-Diameter Tridecagon (Fig. 19)",
            "mechanice",
            sp.Rational(1, 2),
        ),
    ]
    for n_val, label, kind, s_expr in specs:
        q_expr = sp.simplify(s_expr**2)
        s_float = float(s_expr.evalf(30))
        s_true = 2.0 * math.sin(math.pi / n_val)
        rel_err = (s_float - s_true) / s_true
        ang_durer = math.degrees(2.0 * math.asin(s_float / 2.0))
        ang_true = 360.0 / n_val
        entries.append(
            WorkshopPolygonEntry(
                n_sides=n_val,
                durer_label=label,
                classification=kind,
                exact_chord_over_r=s_expr,
                exact_quadrance_over_r2=q_expr,
                true_chord_over_r_float=s_true,
                relative_chord_error=rel_err,
                central_angle_durer_deg=ang_durer,
                central_angle_true_deg=ang_true,
            )
        )

    return HeptagonWorkshopReport(
        model=model,
        center=O_pt,
        circumcircle=circum,
        equilateral_chord_top=T_top,
        equilateral_chord_bottom=T_bot,
        radius_midpoint=E_mid,
        workshop_vertices=tuple(vertices),
        durer_chord_quadrance=durer_q,
        minimal_polynomial_expr=min_poly,
        minimal_polynomial_at_durer=residual,
        eisenstein_prime=7,
        quadrature_circle_diameter_over_side=d_over_a,
        quadrature_implied_pi=pi_durer,
        workshop_catalog=tuple(entries),
    )
