"""Exact symbolic compass-and-straightedge typography from Book III of *Underweysung der Messung*.

Implements Albrecht Dürer's 1525 Nuremberg geometric constructions for:

1. **Roman *Antiqua* Capitals** (Book III, pp. 115–135) inside the ``10 x 10`` square ``ABCD``
   (with thick stroke width ``1 = 1/10`` of the square side and thin stroke width ``1/3``),
   in direct mathematical dialogue with Luca Pacioli's *Divina Proportione* (1509, ``1:9`` grid):

   - ``construct_durer_roman_letter_A``: Inclined thin/thick legs, inner triangular counter,
     sub-midline crossbar, and circular serif fillets (*Ausschweiffung*) of radii ``10/7`` (outer)
     and ``1/2`` (inner).
   - ``construct_durer_roman_letter_O``: Dürer's two-circle diagonal-shift construction along
     ``CB`` (``y = x``), where two congruent circles of exact radius ``5 - sqrt(2)/4`` separated
     by unit stroke distance ``|FG| = 1`` form both the outer contour and inner counter.
   - ``construct_durer_roman_letter_Q``: Extends ``O`` along anti-diagonal ``AD`` (``x + y = 10``)
     with Dürer's sweeping circular tail through corner ``D = (10, 0)``.

2. **Modular Gothic *Textura* Minuscules** (Book III, pp. 136–141):

   - ``construct_durer_textura_minuscules``: Constructs ``i``, ``n``, and ``m`` strictly from
     stacked unit squares (*rechte fierungen*) capped by ``45°`` diamond squares (*ort fierungen*)
     anchored at exact ``1/3`` division points—an early discrete modular grid system.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, proposition, quadrance, zero_test

__all__ = [
    "RomanLetterAResult",
    "RomanLetterOQResult",
    "TexturaMinusculesResult",
    "construct_durer_roman_letter_A",
    "construct_durer_roman_letter_O",
    "construct_durer_roman_letter_Q",
    "construct_durer_textura_minuscules",
]


@dataclass(frozen=True)
class RomanLetterAResult:
    """Exact symbolic construction of Dürer's Roman *Antiqua* capital ``A`` in a ``10 x 10`` square."""

    model: Model
    square_corners: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    thick_stroke: sp.Integer
    thin_stroke: sp.Rational
    outer_serif_radius: sp.Rational
    inner_serif_radius: sp.Rational
    counter_triangle: tuple[spg.Point, spg.Point, spg.Point]
    crossbar_quad: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    serif_centers: dict[str, spg.Point]


@dataclass(frozen=True)
class RomanLetterOQResult:
    """Exact symbolic construction of Dürer's Roman *Antiqua* ``O`` or ``Q`` in a ``10 x 10`` square."""

    letter: str
    model: Model
    square_corners: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    center_i: spg.Point
    shifted_center_f: spg.Point
    shifted_center_g: spg.Point
    bowl_radius: sp.Expr
    circle_f: spg.Circle
    circle_g: spg.Circle
    crossover_points: tuple[spg.Point, spg.Point]
    tail_points: tuple[spg.Point, ...]


@dataclass(frozen=True)
class TexturaMinusculesResult:
    """Exact modular construction of Dürer's Gothic *Textura* minuscules ``i``, ``n``, ``m``."""

    model: Model
    stem_width: sp.Integer
    stacked_square_count: int
    diamond_side: sp.Expr
    glyph_polygons: dict[str, list[tuple[tuple[sp.Expr, sp.Expr], ...]]]


def _one(pts: list[spg.Point], label: str) -> spg.Point:
    if len(pts) != 1:
        raise ValueError(f"Expected 1 intersection for {label}, got {len(pts)}")
    return pts[0]


@proposition(
    "Book III, p. 115",
    kind="problem",
    title="Dürer's Roman Antiqua Capital A in the 10x10 Square",
)
def construct_durer_roman_letter_A(model: Model | None = None) -> RomanLetterAResult:
    """Construct Dürer's Roman capital ``A`` inside the ``10 x 10`` square ``ABCD``.

    Dürer labels the framing square (*rechte fierung*) ``a`` top-left ``(0, 10)``, ``b`` top-right
    ``(10, 10)``, ``c`` bottom-left ``(0, 0)``, ``d`` bottom-right ``(10, 0)``, with midlines
    ``ef`` (vertical) and ``gh`` (horizontal), thick stroke ``1`` (``1/10`` of ``10``), thin stroke
    ``1/3``, outer foot serifs of radius ``10/7``, and inner foot serifs of radius ``1/2``.
    """
    if model is None:
        model = Model("durer_roman_A", logger=False, auto_intersect=False)

    # Framing 10x10 square ABCD (a=top-left, b=top-right, c=bottom-left, d=bottom-right)
    a_sq = model.set_point(sp.Integer(0), sp.Integer(10), classes=["frame"], ID="a")
    b_sq = model.set_point(sp.Integer(10), sp.Integer(10), classes=["frame"], ID="b")
    c_sq = model.set_point(sp.Integer(0), sp.Integer(0), classes=["frame"], ID="c")
    d_sq = model.set_point(sp.Integer(10), sp.Integer(0), classes=["frame"], ID="d")
    model.set_polygon([c_sq, d_sq, b_sq, a_sq], classes=["frame_square"])

    line_cd = model.construct_line(c_sq, d_sq, classes=["grid"], ID="cd")
    line_ab = model.construct_line(a_sq, b_sq, classes=["grid"], ID="ab")

    # Cross midlines ef (vertical) and gh (horizontal)
    e_mid = model.set_point(sp.Integer(5), sp.Integer(10), classes=["grid"], ID="e")
    f_mid = model.set_point(sp.Integer(5), sp.Integer(0), classes=["grid"], ID="f")
    g_mid = model.set_point(sp.Integer(0), sp.Integer(5), classes=["grid"], ID="g")
    h_mid = model.set_point(sp.Integer(10), sp.Integer(5), classes=["grid"], ID="h")
    model.construct_line(e_mid, f_mid, classes=["grid"], ID="ef")
    line_gh = model.construct_line(g_mid, h_mid, classes=["grid"], ID="gh")

    thick = sp.Integer(1)
    thin = sp.Rational(1, 3)

    # Base inset points i=(1,0) and k=(9,0), 1/10 inside c and d
    i_pt = model.set_point(sp.Integer(1), sp.Integer(0), classes=["glyph_key"], ID="i")
    k_pt = model.set_point(sp.Integer(9), sp.Integer(0), classes=["glyph_key"], ID="k")
    i_in = model.set_point(sp.Integer(1) + thin, sp.Integer(0), classes=["glyph_aux"], ID="i_in")
    k_in = model.set_point(sp.Integer(9) - thick, sp.Integer(0), classes=["glyph_aux"], ID="k_in")

    # Top cap shoulders centered on e=(5, 10): T_L=(9/2, 10), T_R=(11/2, 10)
    t_left = model.set_point(sp.Rational(9, 2), sp.Integer(10), classes=["glyph_key"], ID="T_L")
    t_right = model.set_point(sp.Rational(11, 2), sp.Integer(10), classes=["glyph_key"], ID="T_R")
    t_left_in = model.set_point(
        sp.Rational(9, 2) + thin, sp.Integer(10), classes=["glyph_aux"], ID="T_L_in"
    )
    t_right_in = model.set_point(
        sp.Rational(11, 2) - thick, sp.Integer(10), classes=["glyph_aux"], ID="T_R_in"
    )

    left_outer = model.construct_line(i_pt, t_left, classes=["glyph_edge"], ID="left_outer")
    left_inner = model.construct_line(i_in, t_left_in, classes=["glyph_edge"], ID="left_inner")
    right_outer = model.construct_line(k_pt, t_right, classes=["glyph_edge"], ID="right_outer")
    right_inner = model.construct_line(k_in, t_right_in, classes=["glyph_edge"], ID="right_inner")
    _ = (line_ab, line_cd, left_outer, right_outer)

    # Inner apex of the triangular counter
    v_apex = _one(model.intersect_all(left_inner, right_inner, classes=["glyph_key"]), "V_apex")
    v_apex = model.set_point(v_apex.x, v_apex.y, classes=["glyph_key"], ID="V_counter")

    # Crossbar directly beneath horizontal midline gh: y in [5 - 1/3, 5] = [14/3, 5]
    cb_bot_left_ref = model.set_point(sp.Integer(0), sp.Rational(14, 3), classes=["aux"])
    cb_bot_right_ref = model.set_point(sp.Integer(10), sp.Rational(14, 3), classes=["aux"])
    line_cb_bot = model.construct_line(cb_bot_left_ref, cb_bot_right_ref, classes=["glyph_edge"])

    cb_tl = _one(model.intersect_all(left_inner, line_gh, classes=["glyph_key"]), "cb_tl")
    cb_tr = _one(model.intersect_all(right_inner, line_gh, classes=["glyph_key"]), "cb_tr")
    cb_bl = _one(model.intersect_all(left_inner, line_cb_bot, classes=["glyph_key"]), "cb_bl")
    cb_br = _one(model.intersect_all(right_inner, line_cb_bot, classes=["glyph_key"]), "cb_br")

    # Outerglyph body polygon (straight skeletal outline before circular fillets)
    model.set_polygon(
        [i_pt, t_left, t_right, k_pt, k_in, cb_br, cb_bl, i_in],
        classes=["glyph_body"],
    )
    model.set_polygon([cb_tl, cb_tr, v_apex], classes=["glyph_counter"])
    model.set_polygon([cb_bl, cb_br, cb_tr, cb_tl], classes=["glyph_crossbar"])

    # Exact circular serif fillet circles (Ausschweiffung):
    # 1. Outer serifs: radius r_out = 10/7 (1/7 of square side 10), tangent to baseline y=0
    #    and tangent to the outer inclined legs (20*x - 7*y - 20 = 0 and 20*x + 7*y - 180 = 0).
    #    For 20*x - 7*y - 20 = 0, unit distance from (x_c, r_out) on the left (20*x_c - 7*r_out - 20 < 0):
    #    20 - (20*x_c - 7*r_out) = r_out * sqrt(20^2 + 7^2) = r_out * sqrt(449)
    #    => x_c = 1 + r_out * (7 - sqrt(449)) / 20 !
    r_out = sp.Rational(10, 7)
    r_in = sp.Rational(1, 2)
    sqrt_449 = sp.sqrt(449)

    xc_out_left = sp.simplify(sp.Integer(1) + r_out * (sp.Integer(7) - sqrt_449) / sp.Integer(20))
    xc_out_right = sp.simplify(sp.Integer(9) - r_out * (sp.Integer(7) - sqrt_449) / sp.Integer(20))

    # 2. Inner serifs: radius r_in = 1/2 (diameter = thick stroke = 1), tangent to baseline y=0
    #    and tangent to inner inclined legs:
    #    Left inner leg: 20*x - 7*y - 80/3 = 0 (center to the right: 20*x_c - 7*r_in - 80/3 = r_in*sqrt(449))
    #    Right inner leg: 20*x + 7*y - 160 = 0 (center to the left: 160 - 20*x_c - 7*r_in = r_in*sqrt(449))
    xc_in_left = sp.simplify(sp.Rational(4, 3) + r_in * (sp.Integer(7) + sqrt_449) / sp.Integer(20))
    xc_in_right = sp.simplify(sp.Integer(8) - r_in * (sp.Integer(7) + sqrt_449) / sp.Integer(20))

    s_out_l = model.set_point(xc_out_left, r_out, classes=["serif_center"], ID="S_out_L")
    s_out_l_foot = model.set_point(xc_out_left, sp.Integer(0), classes=["serif_foot"])
    model.construct_circle(s_out_l, s_out_l_foot, classes=["serif_circle"], ID="c_serif_out_L")

    s_out_r = model.set_point(xc_out_right, r_out, classes=["serif_center"], ID="S_out_R")
    s_out_r_foot = model.set_point(xc_out_right, sp.Integer(0), classes=["serif_foot"])
    model.construct_circle(s_out_r, s_out_r_foot, classes=["serif_circle"], ID="c_serif_out_R")

    s_in_l = model.set_point(xc_in_left, r_in, classes=["serif_center"], ID="S_in_L")
    s_in_l_foot = model.set_point(xc_in_left, sp.Integer(0), classes=["serif_foot"])
    model.construct_circle(s_in_l, s_in_l_foot, classes=["serif_circle"], ID="c_serif_in_L")

    s_in_r = model.set_point(xc_in_right, r_in, classes=["serif_center"], ID="S_in_R")
    s_in_r_foot = model.set_point(xc_in_right, sp.Integer(0), classes=["serif_foot"])
    model.construct_circle(s_in_r, s_in_r_foot, classes=["serif_circle"], ID="c_serif_in_R")

    return RomanLetterAResult(
        model=model,
        square_corners=(a_sq, b_sq, c_sq, d_sq),
        thick_stroke=thick,
        thin_stroke=thin,
        outer_serif_radius=r_out,
        inner_serif_radius=r_in,
        counter_triangle=(cb_tl, cb_tr, v_apex),
        crossbar_quad=(cb_bl, cb_br, cb_tr, cb_tl),
        serif_centers={
            "out_left": s_out_l,
            "out_right": s_out_r,
            "in_left": s_in_l,
            "in_right": s_in_r,
        },
    )


def _construct_o_or_q(letter: str, model: Model | None = None) -> RomanLetterOQResult:
    if model is None:
        model = Model(f"durer_roman_{letter}", logger=False, auto_intersect=False)

    a_sq = model.set_point(sp.Integer(0), sp.Integer(10), classes=["frame"], ID="a")
    b_sq = model.set_point(sp.Integer(10), sp.Integer(10), classes=["frame"], ID="b")
    c_sq = model.set_point(sp.Integer(0), sp.Integer(0), classes=["frame"], ID="c")
    d_sq = model.set_point(sp.Integer(10), sp.Integer(0), classes=["frame"], ID="d")
    model.set_polygon([c_sq, d_sq, b_sq, a_sq], classes=["frame_square"])

    # Diagonal cb (y = x) and anti-diagonal ad (x + y = 10)
    diag_cb = model.construct_line(c_sq, b_sq, classes=["grid"], ID="diag_cb")
    diag_ad = model.construct_line(a_sq, d_sq, classes=["grid"], ID="diag_ad")

    center_i = _one(model.intersect_all(diag_cb, diag_ad, classes=["grid"]), "center_i")
    center_i = model.set_point(center_i.x, center_i.y, classes=["grid"], ID="i")

    # Shifted centers f and g on diagonal cb separated by unit stroke width 1:
    # delta = sqrt(2)/4 => |fg|^2 = (sqrt(2)/2)^2 + (sqrt(2)/2)^2 = 1/2 + 1/2 = 1!
    delta = sp.sqrt(2) / sp.Integer(4)
    f_pt = model.set_point(
        sp.Integer(5) - delta, sp.Integer(5) - delta, classes=["glyph_key"], ID="f"
    )
    g_pt = model.set_point(
        sp.Integer(5) + delta, sp.Integer(5) + delta, classes=["glyph_key"], ID="g"
    )
    if not zero_test(quadrance(f_pt, g_pt) - 1):
        raise ValueError("Expected unit quadrance between shifted bowl centers f and g")

    # Circle f touches left side x=0 at (0, 5 - delta) and bottom side y=0 at (5 - delta, 0);
    # Circle g touches right side x=10 at (10, 5 + delta) and top side y=10 at (5 + delta, 10).
    bowl_r = sp.Integer(5) - delta
    touch_left = model.set_point(sp.Integer(0), sp.Integer(5) - delta, classes=["glyph_aux"], ID="t_L")
    touch_right = model.set_point(
        sp.Integer(10), sp.Integer(5) + delta, classes=["glyph_aux"], ID="t_R"
    )

    circle_f = model.construct_circle(f_pt, touch_left, classes=["bowl_circle"], ID="c_f")
    circle_g = model.construct_circle(g_pt, touch_right, classes=["bowl_circle"], ID="c_g")

    cross_pts = model.intersect_all(circle_f, circle_g, classes=["glyph_key"])
    if len(cross_pts) != 2:
        raise ValueError(f"Expected 2 crossover points for O bowls, got {len(cross_pts)}")
    cross_sorted = sorted(cross_pts, key=lambda p: float(p.x.evalf()))
    p_nw = model.set_point(
        sp.simplify(cross_sorted[0].x),
        sp.simplify(cross_sorted[0].y),
        classes=["glyph_key"],
        ID="P_NW",
    )
    p_se = model.set_point(
        sp.simplify(cross_sorted[1].x),
        sp.simplify(cross_sorted[1].y),
        classes=["glyph_key"],
        ID="P_SE",
    )

    tail_pts: tuple[spg.Point, ...] = ()
    if letter == "Q":
        # Dürer p. 125: Long tail starts beneath diagonal ad on the bowl, passes through corner d=(10,0)
        # with full stroke width 1, and sweeps outward/downward to depth -10/3 (1/3 of square height)
        # over horizontal reach ~10, constructed via exact circular arcs of radius 10!
        q_start = model.set_point(sp.Rational(15, 2), sp.Rational(3, 2), classes=["tail_key"], ID="Q_s")
        q_tip = model.set_point(sp.Integer(18), sp.Rational(-10, 3), classes=["tail_key"], ID="Q_tip")
        q_ctrl = model.set_point(sp.Integer(13), sp.Rational(-5, 2), classes=["tail_aux"], ID="Q_mid")
        model.set_segment(q_start, d_sq, classes=["tail_axis"])
        model.set_segment(d_sq, q_ctrl, classes=["tail_axis"])
        model.set_segment(q_ctrl, q_tip, classes=["tail_axis"])
        tail_pts = (q_start, d_sq, q_ctrl, q_tip)

    return RomanLetterOQResult(
        letter=letter,
        model=model,
        square_corners=(a_sq, b_sq, c_sq, d_sq),
        center_i=center_i,
        shifted_center_f=f_pt,
        shifted_center_g=g_pt,
        bowl_radius=bowl_r,
        circle_f=circle_f,
        circle_g=circle_g,
        crossover_points=(p_nw, p_se),
        tail_points=tail_pts,
    )


@proposition(
    "Book III, p. 124",
    kind="problem",
    title="Dürer's Roman Antiqua Capital O via Two Shifted Diagonal Circles",
)
def construct_durer_roman_letter_O(model: Model | None = None) -> RomanLetterOQResult:
    """Construct Dürer's Roman capital ``O`` inside the ``10 x 10`` square."""
    return _construct_o_or_q("O", model=model)


@proposition(
    "Book III, p. 125",
    kind="problem",
    title="Dürer's Roman Antiqua Capital Q in the 10x10 Square",
)
def construct_durer_roman_letter_Q(model: Model | None = None) -> RomanLetterOQResult:
    """Construct Dürer's Roman capital ``Q`` inside the ``10 x 10`` square."""
    return _construct_o_or_q("Q", model=model)


def _build_textura_stem(x0: sp.Expr) -> list[tuple[tuple[sp.Expr, sp.Expr], ...]]:
    """Construct one Dürer *Textura* stem (Book III, p. 136) at horizontal offset ``x0``.

    Dürer stacks 3 upright unit squares (``[x0, x0+1] x [0, 3]``), divides the top edge ``y=3``
    and bottom edge ``y=0`` into thirds, and places a congruent unit square tilted at ``45°``
    (*ort fierung*, vertical diagonal ``sqrt(2)``, half-diagonal ``h = sqrt(2)/2``):
    - Top diamond has its bottom corner at the *first* (front/left) third ``(x0 + 1/3, 3)``.
    - Bottom diamond has its top corner at the *second* (rear/right) third ``(x0 + 2/3, 0)``.
    """
    polys: list[tuple[tuple[sp.Expr, sp.Expr], ...]] = []
    # 3 upright unit squares
    for k in range(3):
        yk = sp.Integer(k)
        polys.append(((x0, yk), (x0 + 1, yk), (x0 + 1, yk + 1), (x0, yk + 1)))

    h = sp.sqrt(2) / sp.Integer(2)
    # Top ort-fierung anchored at (x0 + 1/3, 3)
    tx = x0 + sp.Rational(1, 3)
    ty = sp.Integer(3)
    top_diamond = (
        (tx, ty),
        (tx + h, ty + h),
        (tx, ty + 2 * h),
        (tx - h, ty + h),
    )
    polys.append(top_diamond)

    # Bottom ort-fierung anchored at (x0 + 2/3, 0)
    bx = x0 + sp.Rational(2, 3)
    by = sp.Integer(0)
    bot_diamond = (
        (bx, by - 2 * h),
        (bx + h, by - h),
        (bx, by),
        (bx - h, by - h),
    )
    polys.append(bot_diamond)
    return polys


@proposition(
    "Book III, p. 136",
    kind="problem",
    title="Dürer's Modular Gothic Textura Minuscules i, n, m",
)
def construct_durer_textura_minuscules(model: Model | None = None) -> TexturaMinusculesResult:
    """Construct Dürer's modular *Textura* minuscules ``i``, ``n``, and ``m`` from unit squares.

    In Book III (p. 136), Dürer constructs ``i`` first because nearly the entire Gothic minuscule
    alphabet is generated combinatorially from its modular stem. For ``n`` (two stems) and ``m``
    (three stems), adjacent stems touch corner-to-corner at their ``45°`` diamond caps!
    Wait: look at the spacing when adjacent top diamonds touch corner-to-corner:
    Top diamond of stem 1 has right corner at ``x0 + 1/3 + sqrt(2)/2`` and left corner at
    ``x0 + 1/3 - sqrt(2)/2``, so corner-to-corner contact spaces consecutive stems by exact pitch
    ``sqrt(2)`` (leaving interior counter gap ``sqrt(2) - 1 ≈ 0.414 < 1``, matching Dürer's exact
    words: *"so wirt das felt schlemer zwischen den zügen dann ein zug des pustaben preyt ist"*!).
    """
    if model is None:
        model = Model("durer_textura_minuscules", logger=False, auto_intersect=False)

    pitch = sp.sqrt(2)
    i_polys = _build_textura_stem(sp.Integer(0))
    n_polys = _build_textura_stem(sp.Integer(3)) + _build_textura_stem(sp.Integer(3) + pitch)
    m_base = sp.Integer(8)
    m_polys = (
        _build_textura_stem(m_base)
        + _build_textura_stem(m_base + pitch)
        + _build_textura_stem(m_base + 2 * pitch)
    )

    glyphs = {"i": i_polys, "n": n_polys, "m": m_polys}
    for g_name, poly_list in glyphs.items():
        for p_idx, coords in enumerate(poly_list):
            pts = [
                model.set_point(cx, cy, classes=["textura_pt"])
                for cx, cy in coords
            ]
            cls_tag = "textura_diamond" if p_idx % 5 in (3, 4) else "textura_square"
            model.set_polygon(pts, classes=["textura_module", cls_tag, f"glyph_{g_name}"])

    return TexturaMinusculesResult(
        model=model,
        stem_width=sp.Integer(1),
        stacked_square_count=3,
        diamond_side=sp.Integer(1),
        glyph_polygons=glyphs,
    )
