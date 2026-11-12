"""Exact symbolic planar polyhedral nets from Book IV of Dürer's *Underweysung der Messung* (1525).

In Book IV (pp. 142–158, Figs. 29–43), Albrecht Dürer published the **first printed fold-out
planar polyhedral nets in the history of mathematics** (*aufgeschnittene und nidergelegte Corpora*),
covering all 5 Platonic solids, 7 Archimedean semi-regular solids, and 2 invented composite solids.

Every net constructed in this module uses **100% exact symbolic SymPy coordinates** with unit edge
quadrance ``Q = 1``:

- **Tetrahedron** (Fig. 29), **Octahedron** (Fig. 30), **Icosahedron** (Fig. 31), and
  **Cuboctahedron** (Fig. 37): coordinates in ``Q(sqrt(3))``.
- **Cube** (Fig. 32): coordinates in ``Q``.
- **Dodecahedron** (Fig. 33 — two 6-pentagon rosettes hinged across a shared outer petal edge):
  coordinates in the degree-4 cyclotomic subfield ``Q(sqrt(5), sin(36°))`` where
  ``sin(36°) = sqrt(10 - 2*sqrt(5)) / 4`` and ``phi = (1 + sqrt(5)) / 2``.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, zero_test

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)
SIN_36: sp.Expr = sp.sqrt(sp.Integer(10) - sp.Integer(2) * sp.sqrt(5)) / sp.Integer(4)
COS_72: sp.Expr = (sp.sqrt(5) - sp.Integer(1)) / sp.Integer(4)
SIN_72: sp.Expr = sp.expand(PHI * SIN_36)
SQRT3_HALF: sp.Expr = sp.sqrt(3) / sp.Integer(2)

__all__ = [
    "DURER_BOOK4_SOLIDS_CATALOG",
    "Book4SolidCatalogEntry",
    "PolyhedralFace",
    "PolyhedralNet",
    "construct_durer_polyhedral_nets",
    "polyhedral_net_to_model",
]


@dataclass(frozen=True)
class PolyhedralFace:
    """Single regular polygon face in an unfolded 2D planar polyhedral net."""

    face_id: str
    n_gon: int
    vertices: tuple[tuple[sp.Expr, sp.Expr], ...]


@dataclass(frozen=True)
class PolyhedralNet:
    """Exact 2D planar fold-out net for a Platonic or Archimedean polyhedron."""

    key: str
    title: str
    durer_figure: str
    family: str
    algebraic_field: str
    vertices_3d: int
    edges_3d: int
    faces_3d: int
    faces: tuple[PolyhedralFace, ...]
    fold_edges: tuple[tuple[tuple[sp.Expr, sp.Expr], tuple[sp.Expr, sp.Expr]], ...]
    cut_edges: tuple[tuple[tuple[sp.Expr, sp.Expr], tuple[sp.Expr, sp.Expr]], ...]
    unit_edge_verified: bool
    euler_characteristic: int
    seam_count_verified: bool
    non_overlapping_verified: bool


@dataclass(frozen=True)
class Book4SolidCatalogEntry:
    """Historical & combinatorial catalog entry for Dürer's Book IV solids (Figs. 29–43)."""

    figure_num: int
    slub_page: int
    german_name_1525: str
    english_name: str
    family: str
    vertex_config: str
    vertices: int
    edges: int
    faces: int
    face_summary: str


DURER_BOOK4_SOLIDS_CATALOG: tuple[Book4SolidCatalogEntry, ...] = (
    Book4SolidCatalogEntry(
        29, 143, "Dreyanglicht Corpus (Tetraedron)", "Regular Tetrahedron", "Platonic",
        "3.3.3", 4, 6, 4, "4 triangles",
    ),
    Book4SolidCatalogEntry(
        30, 144, "Achtseitigs Corpus wie ein Diamant Punct", "Regular Octahedron", "Platonic",
        "3.3.3.3", 6, 12, 8, "8 triangles",
    ),
    Book4SolidCatalogEntry(
        31, 145, "Zweintzigseitigs Corpus (Icosaedron)", "Regular Icosahedron", "Platonic",
        "3.3.3.3.3", 12, 30, 20, "20 triangles",
    ),
    Book4SolidCatalogEntry(
        32, 146, "Sechsseitigs Corpus / Würffel (Cubus)", "Regular Cube (Hexahedron)", "Platonic",
        "4.4.4", 8, 12, 6, "6 squares",
    ),
    Book4SolidCatalogEntry(
        33, 147, "Zwölffünffeckigs Corpus (Dodecaedron)", "Regular Dodecahedron", "Platonic",
        "5.5.5", 20, 30, 12, "12 pentagons",
    ),
    Book4SolidCatalogEntry(
        35, 149, "Abgeschnittnes Dreyanglichts Corpus", "Truncated Tetrahedron", "Archimedean",
        "3.6.6", 12, 18, 8, "4 triangles + 4 hexagons",
    ),
    Book4SolidCatalogEntry(
        36, 150, "Abgeschnittner Würffel", "Truncated Cube", "Archimedean",
        "3.8.8", 24, 36, 14, "8 triangles + 6 octagons",
    ),
    Book4SolidCatalogEntry(
        37, 151, "Sechs Fierung und Acht Dryangel", "Cuboctahedron", "Archimedean",
        "3.4.3.4", 12, 24, 14, "8 triangles + 6 squares",
    ),
    Book4SolidCatalogEntry(
        38, 152, "Sechs Fierung und Acht Sechseck", "Truncated Octahedron", "Archimedean",
        "4.6.6", 24, 36, 14, "6 squares + 8 hexagons",
    ),
    Book4SolidCatalogEntry(
        39, 153, "Achtzehen Fierung und Acht Dryangel", "Rhombicuboctahedron", "Archimedean",
        "3.4.4.4", 24, 48, 26, "8 triangles + 18 squares",
    ),
    Book4SolidCatalogEntry(
        40, 154, "Sechs Fierung und Zweyunddreissig Dryangel", "Snub Cube", "Archimedean",
        "3.3.3.3.4", 24, 60, 38, "32 triangles + 6 squares",
    ),
    Book4SolidCatalogEntry(
        41, 155, "Zwölf Fierung, Acht Sechseck, Sechs Achteck", "Truncated Cuboctahedron",
        "Archimedean", "4.6.8", 48, 72, 26, "12 squares + 8 hexagons + 6 octagons",
    ),
)


def _norm_coord(expr: sp.Expr) -> sp.Expr:
    return sp.expand(expr)


def _regular_polygon_on_edge(
    a0: tuple[sp.Expr, sp.Expr],
    a1: tuple[sp.Expr, sp.Expr],
    n_gon: int,
) -> tuple[tuple[sp.Expr, sp.Expr], ...]:
    """Construct a CCW unit regular ``n_gon`` (``n_gon in {3, 4, 5}``) on directed base ``a0 -> a1``."""
    tx = _norm_coord(a1[0] - a0[0])
    ty = _norm_coord(a1[1] - a0[1])
    nx = _norm_coord(-ty)
    ny = _norm_coord(tx)

    if n_gon == 3:
        a2 = (
            _norm_coord(a0[0] + sp.Rational(1, 2) * tx + SQRT3_HALF * nx),
            _norm_coord(a0[1] + sp.Rational(1, 2) * ty + SQRT3_HALF * ny),
        )
        return (a0, a1, a2)

    if n_gon == 4:
        a2 = (_norm_coord(a1[0] + nx), _norm_coord(a1[1] + ny))
        a3 = (_norm_coord(a0[0] + nx), _norm_coord(a0[1] + ny))
        return (a0, a1, a2, a3)

    if n_gon == 5:
        h_top = _norm_coord(SIN_72 + SIN_36)
        a2 = (
            _norm_coord(a1[0] + COS_72 * tx + SIN_72 * nx),
            _norm_coord(a1[1] + COS_72 * ty + SIN_72 * ny),
        )
        a3 = (
            _norm_coord(a0[0] + sp.Rational(1, 2) * tx + h_top * nx),
            _norm_coord(a0[1] + sp.Rational(1, 2) * ty + h_top * ny),
        )
        a4 = (
            _norm_coord(a0[0] - COS_72 * tx + SIN_72 * nx),
            _norm_coord(a0[1] - COS_72 * ty + SIN_72 * ny),
        )
        return (a0, a1, a2, a3, a4)

    raise ValueError(f"Unsupported n_gon={n_gon}")


def _unfold_across_edge(
    parent_face: PolyhedralFace,
    edge_index: int,
    child_id: str,
    child_n_gon: int,
) -> PolyhedralFace:
    """Unfold a CCW regular ``child_n_gon`` outward across ``edge_index`` of ``parent_face``."""
    verts = parent_face.vertices
    m = len(verts)
    p_start = verts[edge_index % m]
    p_end = verts[(edge_index + 1) % m]
    # Reversing orientation (p_end -> p_start) places the child CCW face strictly outside parent_face
    child_verts = _regular_polygon_on_edge(p_end, p_start, child_n_gon)
    return PolyhedralFace(face_id=child_id, n_gon=child_n_gon, vertices=child_verts)


def _point_key(pt: tuple[sp.Expr, sp.Expr]) -> tuple[int, int]:
    """Quantized geometric hash key (1e-9 tolerance) used strictly to pair coincident seam vertices."""
    return (round(float(pt[0].evalf(20)) * 1_000_000_000), round(float(pt[1].evalf(20)) * 1_000_000_000))


def _polygons_strictly_disjoint(
    f1: PolyhedralFace,
    f2: PolyhedralFace,
    eps: float = 1e-7,
) -> bool:
    """Separating-axis check confirming two convex faces have disjoint interiors."""
    pts1 = [(float(x.evalf(20)), float(y.evalf(20))) for x, y in f1.vertices]
    pts2 = [(float(x.evalf(20)), float(y.evalf(20))) for x, y in f2.vertices]

    for poly in (pts1, pts2):
        n = len(poly)
        for idx in range(n):
            x0, y0 = poly[idx]
            x1, y1 = poly[(idx + 1) % n]
            ax, ay = -(y1 - y0), (x1 - x0)
            proj1 = [px * ax + py * ay for px, py in pts1]
            proj2 = [px * ax + py * ay for px, py in pts2]
            if max(proj1) <= min(proj2) + eps or max(proj2) <= min(proj1) + eps:
                return True
    return False


def _assemble_net(
    *,
    key: str,
    title: str,
    durer_figure: str,
    family: str,
    algebraic_field: str,
    vertices_3d: int,
    edges_3d: int,
    faces: list[PolyhedralFace],
) -> PolyhedralNet:
    # 1. Verify exact unit edge quadrance on every edge of every face
    unit_ok = True
    edge_Buckets: dict[
        tuple[tuple[int, int], tuple[int, int]],
        list[tuple[tuple[sp.Expr, sp.Expr], tuple[sp.Expr, sp.Expr]]],
    ] = {}

    for face in faces:
        fv = face.vertices
        m = len(fv)
        for idx in range(m):
            u = fv[idx]
            v = fv[(idx + 1) % m]
            dx = u[0] - v[0]
            dy = u[1] - v[1]
            q_val = sp.expand(dx * dx + dy * dy)
            if not zero_test(q_val - 1):
                unit_ok = False
            ku, kv = _point_key(u), _point_key(v)
            ekey = (ku, kv) if ku <= kv else (kv, ku)
            edge_Buckets.setdefault(ekey, []).append((u, v))

    fold_edges: list[tuple[tuple[sp.Expr, sp.Expr], tuple[sp.Expr, sp.Expr]]] = []
    cut_edges: list[tuple[tuple[sp.Expr, sp.Expr], tuple[sp.Expr, sp.Expr]]] = []
    for seg_list in edge_Buckets.values():
        if len(seg_list) == 2:
            # Verify exact symbolic coincidence of shared fold endpoints
            (u1, v1), (u2, v2) = seg_list
            coincide = (
                zero_test(u1[0] - v2[0])
                and zero_test(u1[1] - v2[1])
                and zero_test(v1[0] - u2[0])
                and zero_test(v1[1] - u2[1])
            )
            if not coincide:
                unit_ok = False
            fold_edges.append(seg_list[0])
        elif len(seg_list) == 1:
            cut_edges.append(seg_list[0])
        else:
            unit_ok = False

    # 2. Verify Euler characteristic and seam pairing:
    # A valid tree-unfolded planar net of F faces has (F - 1) interior fold edges
    # and 2*(E_3d - (F - 1)) open boundary cut edges.
    faces_3d = len(faces)
    euler_chi = vertices_3d - edges_3d + faces_3d
    seam_ok = (len(fold_edges) == faces_3d - 1) and (
        len(cut_edges) == 2 * (edges_3d - (faces_3d - 1))
    )

    # 3. Verify pairwise non-overlapping convex interiors
    non_overlap = True
    for i in range(len(faces)):
        for j in range(i + 1, len(faces)):
            if not _polygons_strictly_disjoint(faces[i], faces[j]):
                non_overlap = False
                break

    return PolyhedralNet(
        key=key,
        title=title,
        durer_figure=durer_figure,
        family=family,
        algebraic_field=algebraic_field,
        vertices_3d=vertices_3d,
        edges_3d=edges_3d,
        faces_3d=faces_3d,
        faces=tuple(faces),
        fold_edges=tuple(fold_edges),
        cut_edges=tuple(cut_edges),
        unit_edge_verified=unit_ok,
        euler_characteristic=euler_chi,
        seam_count_verified=seam_ok,
        non_overlapping_verified=non_overlap,
    )


def _build_tetrahedron_net() -> PolyhedralNet:
    base = PolyhedralFace(
        "T0", 3, _regular_polygon_on_edge((sp.Integer(0), sp.Integer(0)), (sp.Integer(1), sp.Integer(0)), 3)
    )
    faces = [
        base,
        _unfold_across_edge(base, 0, "T1", 3),
        _unfold_across_edge(base, 1, "T2", 3),
        _unfold_across_edge(base, 2, "T3", 3),
    ]
    return _assemble_net(
        key="tetrahedron",
        title="Regular Tetrahedron (Book IV, Fig. 29)",
        durer_figure="Book IV, Fig. 29 (p. 143)",
        family="Platonic",
        algebraic_field="Q(sqrt(3))",
        vertices_3d=4,
        edges_3d=6,
        faces=faces,
    )


def _build_cube_net() -> PolyhedralNet:
    s0 = PolyhedralFace(
        "S0", 4, _regular_polygon_on_edge((sp.Integer(0), sp.Integer(0)), (sp.Integer(1), sp.Integer(0)), 4)
    )
    s_south = _unfold_across_edge(s0, 0, "S1", 4)
    s_east = _unfold_across_edge(s0, 1, "S2", 4)
    s_north = _unfold_across_edge(s0, 2, "S3", 4)
    s_west = _unfold_across_edge(s0, 3, "S4", 4)
    # Opposite top square attached north of s_north (edge 2 of s_north is its far north edge)
    s_far = _unfold_across_edge(s_north, 2, "S5", 4)
    return _assemble_net(
        key="cube",
        title="Regular Cube / Hexahedron (Book IV, Fig. 32)",
        durer_figure="Book IV, Fig. 32 (p. 146)",
        family="Platonic",
        algebraic_field="Q",
        vertices_3d=8,
        edges_3d=12,
        faces=[s0, s_south, s_east, s_north, s_west, s_far],
    )


def _build_octahedron_net() -> PolyhedralNet:
    # Dürer Fig. 30: Two 4-triangle "diamond-point" fans hinged along the base edge (0,0)-(1,0)
    a1 = PolyhedralFace(
        "A1", 3, _regular_polygon_on_edge((sp.Integer(0), sp.Integer(0)), (sp.Integer(1), sp.Integer(0)), 3)
    )
    a2 = _unfold_across_edge(a1, 1, "A2", 3)
    a3 = _unfold_across_edge(a2, 1, "A3", 3)
    a0 = _unfold_across_edge(a1, 2, "A0", 3)

    b1 = _unfold_across_edge(a1, 0, "B1", 3)
    b2 = _unfold_across_edge(b1, 1, "B2", 3)
    b3 = _unfold_across_edge(b2, 1, "B3", 3)
    b0 = _unfold_across_edge(b1, 2, "B0", 3)

    return _assemble_net(
        key="octahedron",
        title="Regular Octahedron — Diamond Point (Book IV, Fig. 30)",
        durer_figure="Book IV, Fig. 30 (p. 144)",
        family="Platonic",
        algebraic_field="Q(sqrt(3))",
        vertices_3d=6,
        edges_3d=12,
        faces=[a0, a1, a2, a3, b0, b1, b2, b3],
    )


def _build_dodecahedron_net() -> PolyhedralNet:
    # Dürer Fig. 33: Two 6-pentagon rosettes (central pentagon + 5 petals) joined along one outer petal edge
    p0 = PolyhedralFace(
        "A_center",
        5,
        _regular_polygon_on_edge((sp.Integer(0), sp.Integer(0)), (sp.Integer(1), sp.Integer(0)), 5),
    )
    petals_a = [_unfold_across_edge(p0, idx, f"A_petal_{idx}", 5) for idx in range(5)]
    # Hinge second rosette across outer edge 2 of petal 1 (upper-right petal) so Rosette B sits cleanly to the right
    bridge_petal = _unfold_across_edge(petals_a[1], 2, "B_petal_0", 5)
    # In bridge_petal, edge 0 is the hinge back to A_petal_1; opposite outer edge 2 (or 3) reaches B_center!
    b_center = _unfold_across_edge(bridge_petal, 3, "B_center", 5)
    # B_center has edge 0 shared with bridge_petal; unfold the remaining 4 petals of Rosette B on edges 1, 2, 3, 4!
    petals_b = [_unfold_across_edge(b_center, idx, f"B_petal_{idx}", 5) for idx in range(1, 5)]

    return _assemble_net(
        key="dodecahedron",
        title="Regular Dodecahedron — Double Pentagonal Rosette (Book IV, Fig. 33)",
        durer_figure="Book IV, Fig. 33 (p. 147)",
        family="Platonic",
        algebraic_field="Q(sqrt(5), sin(36°))",
        vertices_3d=20,
        edges_3d=30,
        faces=[p0, *petals_a, bridge_petal, b_center, *petals_b],
    )


def _build_icosahedron_net() -> PolyhedralNet:
    # Dürer Fig. 31: Equatorial alternating band of 10 triangles + 5 lower cap + 5 upper cap triangles
    t0 = PolyhedralFace(
        "Eq_0",
        3,
        _regular_polygon_on_edge((sp.Integer(0), sp.Integer(0)), (sp.Integer(1), sp.Integer(0)), 3),
    )
    band: list[PolyhedralFace] = [t0]
    for step in range(1, 10):
        prev = band[-1]
        # Alternate unfolding across right edge (1) for up-pointing and left/lower-right edge (2) for down-pointing
        # Let's check: t0=(0,0),(1,0),(1/2,h). Edge 1 is (1,0)->(1/2,h).
        # t1 = _unfold_across_edge(t0, 1): vertices are ((1/2,h), (1,0), (3/2,h)).
        # In t1, edge 0 is (1/2,h)->(1,0) (back to t0); edge 1 is (1,0)->(3/2,h) (eastward!); edge 2 is (3/2,h)->(1/2,h) (north horizontal!).
        # Unfolding t2 across edge 1 of t1 gives ((3/2,h), (1,0), (2,0)):
        # In t2, edge 0 is back to t1; edge 1 is (1,0)->(2,0) (south horizontal!); edge 2 is (2,0)->(3/2,h) (eastward!).
        hinge_idx = 1 if (step % 2 == 1) else 1
        if step > 1 and step % 2 == 1:
            hinge_idx = 2
        band.append(_unfold_across_edge(prev, hinge_idx, f"Eq_{step}", 3))

    caps: list[PolyhedralFace] = []
    # t0 has south horizontal edge 0; even-indexed Eq_2, Eq_4, Eq_6, Eq_8 have south horizontal edge 1
    caps.append(_unfold_across_edge(band[0], 0, "CapS_0", 3))
    for k_even in (2, 4, 6, 8):
        caps.append(_unfold_across_edge(band[k_even], 1, f"CapS_{k_even // 2}", 3))
    # Odd-indexed Eq_1, Eq_3, Eq_5, Eq_7, Eq_9 have north horizontal edge 2
    for k_odd in (1, 3, 5, 7, 9):
        caps.append(_unfold_across_edge(band[k_odd], 2, f"CapN_{k_odd // 2}", 3))

    return _assemble_net(
        key="icosahedron",
        title="Regular Icosahedron — Equatorial Band & Polar Caps (Book IV, Fig. 31)",
        durer_figure="Book IV, Fig. 31 (p. 145)",
        family="Platonic",
        algebraic_field="Q(sqrt(3))",
        vertices_3d=12,
        edges_3d=30,
        faces=[*band, *caps],
    )


def _build_cuboctahedron_net() -> PolyhedralNet:
    # Dürer Fig. 37: 6 squares + 8 triangles unfolded via the exact 4-arm bipartite spanning tree
    s_top = PolyhedralFace(
        "Sq_top",
        4,
        _regular_polygon_on_edge((sp.Integer(0), sp.Integer(0)), (sp.Integer(1), sp.Integer(0)), 4),
    )
    faces: list[PolyhedralFace] = [s_top]
    arm_names = ("S", "E", "N", "W")
    east_bot_tri: PolyhedralFace | None = None

    for idx, arm in enumerate(arm_names):
        # 1. Top corner triangle attached to side idx of s_top
        t_upper = _unfold_across_edge(s_top, idx, f"Tri_top_{arm}", 3)
        # 2. Lateral square attached to edge 1 of t_upper
        s_side = _unfold_across_edge(t_upper, 1, f"Sq_{arm}", 4)
        # 3. Bottom corner triangle attached to opposite edge 2 of s_side
        t_lower = _unfold_across_edge(s_side, 2, f"Tri_bot_{arm}", 3)
        faces.extend([t_upper, s_side, t_lower])
        if arm == "E":
            east_bot_tri = t_lower

    assert east_bot_tri is not None
    # 4. Bottom square attached to edge 2 of east_bot_tri
    s_bot = _unfold_across_edge(east_bot_tri, 2, "Sq_bot", 4)
    faces.append(s_bot)

    return _assemble_net(
        key="cuboctahedron",
        title="Cuboctahedron — Six Squares & Eight Triangles (Book IV, Fig. 37)",
        durer_figure="Book IV, Fig. 37 (p. 151)",
        family="Archimedean",
        algebraic_field="Q(sqrt(3))",
        vertices_3d=12,
        edges_3d=24,
        faces=faces,
    )


def construct_durer_polyhedral_nets() -> dict[str, PolyhedralNet]:
    """Construct all 6 exact symbolic planar polyhedral nets from Dürer's Book IV.

    Returns
    -------
    dict[str, PolyhedralNet]
        Mapping from ``'tetrahedron'``, ``'cube'``, ``'octahedron'``, ``'dodecahedron'``,
        ``'icosahedron'``, and ``'cuboctahedron'`` to verified exact planar nets.
    """
    return {
        "tetrahedron": _build_tetrahedron_net(),
        "cube": _build_cube_net(),
        "octahedron": _build_octahedron_net(),
        "dodecahedron": _build_dodecahedron_net(),
        "icosahedron": _build_icosahedron_net(),
        "cuboctahedron": _build_cuboctahedron_net(),
    }


def polyhedral_net_to_model(net: PolyhedralNet, model: Model | None = None) -> Model:
    """Populate a ``geometor.model.Model`` with exact vertices, face polygons, and fold/cut seams."""
    if model is None:
        model = Model(f"durer_net_{net.key}", logger=False, auto_intersect=False)

    pt_cache: dict[tuple[int, int], spg.Point] = {}

    def _get_model_pt(coord: tuple[sp.Expr, sp.Expr]) -> spg.Point:
        pk = _point_key(coord)
        if pk not in pt_cache:
            pt_cache[pk] = model.set_point(
                coord[0], coord[1], classes=["net_vertex"], ID=f"V{len(pt_cache)}"
            )
        return pt_cache[pk]

    for face in net.faces:
        m_pts = [_get_model_pt(c) for c in face.vertices]
        face_cls = f"face_{face.n_gon}gon"
        model.set_polygon(m_pts, classes=["net_face", face_cls])

    for u, v in net.fold_edges:
        pu, pv = _get_model_pt(u), _get_model_pt(v)
        if not zero_test(quadrance(pu, pv) - 1):
            raise ValueError(f"Non-unit fold edge in {net.key}")
        model.set_segment(pu, pv, classes=["fold_edge"])

    for u, v in net.cut_edges:
        pu, pv = _get_model_pt(u), _get_model_pt(v)
        if not zero_test(quadrance(pu, pv) - 1):
            raise ValueError(f"Non-unit cut edge in {net.key}")
        model.set_segment(pu, pv, classes=["cut_edge"])

    return model
