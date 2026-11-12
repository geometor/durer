"""Theme-adaptive ``.euclid-graphic`` SVG renderer & figure generator for ``geometor.durer``.

Serializes exact :class:`~geometor.model.Model` constructions from Books I–IV of Albrecht Dürer's
*Underweysung der Messung* (1525) into interactive, publication-grade ``.euclid-graphic`` SVGs
compatible with ``photon-platform/publish``'s ``.. picture::`` directive and ``:g:`` hover roles.
"""

from __future__ import annotations

import html
import math
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.durer.conics_perspective import (
    construct_durer_conic_sections,
    construct_durer_perspective_apparatus,
    construct_durer_spiral_volute,
)
from geometor.durer.polygons import (
    construct_durer_heptagon_workshop,
    construct_durer_vs_euclid_pentagon,
)
from geometor.durer.polyhedra import (
    construct_durer_polyhedral_nets,
    polyhedral_net_to_model,
)
from geometor.durer.typography import (
    construct_durer_roman_letter_A,
    construct_durer_roman_letter_Q,
    construct_durer_textura_minuscules,
)

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "export_svg",
    "generate_all_codex_figures",
    "render_model_svg",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    --svg-bg: #fafaf9;
    --ink: #1c1917;
    --label-halo: rgba(250, 250, 249, 0.92);
    --grid-stroke: #94a3b8;
    --aux-stroke: #64748b;
    --durer-stroke: #b45309;
    --durer-fill: #f59e0b;
    --euclid-stroke: #0369a1;
    --euclid-fill: #0ea5e9;
    --accent-stroke: #0f766e;
    --accent-fill: #14b8a6;
    --violet-stroke: #7c3aed;
    --crimson-stroke: #be123c;
    font-family: "Inter", "Fira Sans", "Segoe UI", system-ui, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic {
      --svg-bg: #141417;
      --ink: #f4f4f5;
      --label-halo: rgba(20, 20, 23, 0.92);
      --grid-stroke: #64748b;
      --aux-stroke: #94a3b8;
      --durer-stroke: #fbbf24;
      --durer-fill: #fbbf24;
      --euclid-stroke: #38bdf8;
      --euclid-fill: #38bdf8;
      --accent-stroke: #2dd4bf;
      --accent-fill: #2dd4bf;
      --violet-stroke: #c084fc;
      --crimson-stroke: #fb7185;
    }
  }
  [data-theme="dark"] .euclid-graphic {
    --svg-bg: #141417;
    --ink: #f4f4f5;
    --label-halo: rgba(20, 20, 23, 0.92);
    --grid-stroke: #64748b;
    --aux-stroke: #94a3b8;
    --durer-stroke: #fbbf24;
    --durer-fill: #fbbf24;
    --euclid-stroke: #38bdf8;
    --euclid-fill: #38bdf8;
    --accent-stroke: #2dd4bf;
    --accent-fill: #2dd4bf;
    --violet-stroke: #c084fc;
    --crimson-stroke: #fb7185;
  }
  .euclid-graphic .canvas-bg { fill: #fafaf9; fill: var(--svg-bg); }
  .euclid-graphic .geom-circle { fill: none; stroke: var(--aux-stroke); stroke-width: 1.35; stroke-dasharray: 5 3.5; opacity: 0.72; }
  .euclid-graphic .geom-circle.primary-circle { stroke: var(--euclid-stroke); stroke-width: 2.15; stroke-dasharray: none; opacity: 0.95; }
  .euclid-graphic .geom-circle.bowl-circle { stroke: var(--durer-stroke); stroke-width: 2.35; stroke-dasharray: none; opacity: 0.95; }
  .euclid-graphic .geom-circle.serif-circle { stroke: var(--violet-stroke); stroke-width: 1.55; stroke-dasharray: 4 2.5; opacity: 0.85; }
  .euclid-graphic .geom-line { fill: none; stroke: var(--grid-stroke); stroke-width: 1.25; stroke-dasharray: 4 3; opacity: 0.65; }
  .euclid-graphic .geom-line.ray-line { stroke: var(--durer-stroke); stroke-width: 1.5; stroke-dasharray: 5 3; opacity: 0.82; }
  .euclid-graphic .geom-segment { fill: none; stroke: var(--ink); stroke-width: 1.9; stroke-linecap: round; }
  .euclid-graphic .geom-segment.fold-seam { stroke: var(--euclid-stroke); stroke-width: 1.85; stroke-dasharray: 6 3.5; }
  .euclid-graphic .geom-segment.cut-seam { stroke: var(--ink); stroke-width: 2.15; }
  .euclid-graphic .geom-segment.spiral-seg { stroke: var(--durer-stroke); stroke-width: 2.55; }
  .euclid-graphic .geom-segment.sector-seg { stroke: var(--grid-stroke); stroke-width: 1.05; stroke-dasharray: 3 3; opacity: 0.58; }
  .euclid-graphic .geom-segment.accent-seg { stroke: var(--accent-stroke); stroke-width: 2.35; }
  .euclid-graphic .geom-segment.projector-seg { stroke: var(--grid-stroke); stroke-width: 1.1; stroke-dasharray: 3 3; opacity: 0.7; }
  .euclid-graphic .geom-polygon { fill: var(--euclid-fill); fill-opacity: 0.08; stroke: var(--euclid-stroke); stroke-width: 2.15; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.durer-poly { fill: var(--durer-fill); fill-opacity: 0.11; stroke: var(--durer-stroke); stroke-width: 2.4; }
  .euclid-graphic .geom-polygon.euclid-poly { fill: var(--euclid-fill); fill-opacity: 0.08; stroke: var(--euclid-stroke); stroke-width: 2.2; stroke-dasharray: 7 3.5; }
  .euclid-graphic .geom-polygon.frame-poly { fill: none; stroke: var(--grid-stroke); stroke-width: 1.5; stroke-dasharray: 5 3; }
  .euclid-graphic .geom-polygon.glyph-poly { fill: var(--durer-fill); fill-opacity: 0.16; stroke: var(--durer-stroke); stroke-width: 2.35; }
  .euclid-graphic .geom-polygon.counter-poly { fill: var(--svg-bg); fill-opacity: 0.92; stroke: var(--euclid-stroke); stroke-width: 1.85; }
  .euclid-graphic .geom-polygon.net-3gon { fill: var(--euclid-fill); fill-opacity: 0.11; stroke: none; }
  .euclid-graphic .geom-polygon.net-4gon { fill: var(--durer-fill); fill-opacity: 0.13; stroke: none; }
  .euclid-graphic .geom-polygon.net-5gon { fill: var(--accent-fill); fill-opacity: 0.13; stroke: none; }
  .euclid-graphic .geom-point { fill: var(--ink); stroke: var(--svg-bg); stroke-width: 1.4; }
  .euclid-graphic .geom-point.durer-pt { fill: var(--durer-stroke); }
  .euclid-graphic .geom-point.euclid-pt { fill: var(--euclid-stroke); }
  .euclid-graphic .geom-point.accent-pt { fill: var(--crimson-stroke); }
  .euclid-graphic .euclid-label {
    fill: var(--ink);
    font-size: 13px;
    font-weight: 650;
    paint-order: stroke fill;
    stroke: var(--label-halo);
    stroke-width: 3.5px;
    stroke-linejoin: round;
    user-select: none;
  }
  .euclid-graphic .euclid-sub { font-size: 9.6px; font-weight: 650; }
  .euclid-graphic .caption-note {
    fill: var(--aux-stroke);
    font-size: 12px;
    font-weight: 550;
  }
""".strip()


def _fmt(val: float) -> str:
    if abs(val - round(val)) < 1e-5:
        return str(int(round(val)))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _seg_path_d(x1: float, y1: float, x2: float, y2: float) -> str:
    xm = 0.5 * (x1 + x2)
    ym = 0.5 * (y1 + y2)
    return f"M {_fmt(x1)} {_fmt(y1)} L {_fmt(xm)} {_fmt(ym)} L {_fmt(x2)} {_fmt(y2)}"


def _clip_line(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []
    if abs(b_f) > eps:
        for x_e in (xmin, xmax):
            yv = -(a_f * x_e + c_f) / b_f
            if ymin - 1e-7 <= yv <= ymax + 1e-7:
                hits.append((x_e, min(max(yv, ymin), ymax)))
    if abs(a_f) > eps:
        for y_e in (ymin, ymax):
            xv = -(b_f * y_e + c_f) / a_f
            if xmin - 1e-7 <= xv <= xmax + 1e-7:
                pt = (min(max(xv, xmin), xmax), y_e)
                if all(math.hypot(pt[0] - h[0], pt[1] - h[1]) > 1e-5 for h in hits):
                    hits.append(pt)
    if len(hits) < 2:
        return None
    return hits[0], hits[1]


def _format_label_xml(raw: str) -> str:
    if "_" in raw:
        base, sub = raw.split("_", 1)
        return (
            f'{html.escape(base)}<tspan class="euclid-sub" dy="3">{html.escape(sub)}</tspan>'
        )
    return html.escape(raw)


def render_model_svg(
    model: Model,
    *,
    width: int = 760,
    height: int = 560,
    padding: float = 48.0,
    math_bounds: tuple[float, float, float, float] | None = None,
    labeled_keys: dict[str, str] | None = None,
    extra_annotations: list[tuple[float, float, str]] | None = None,
    show_lines: bool = True,
    show_unlabeled_points: bool = False,
) -> str:
    """Serialize a :class:`~geometor.model.Model` into a crisp ``.euclid-graphic`` SVG string."""
    pts: list[tuple[spg.Point, object]] = []
    circles: list[tuple[spg.Circle, object]] = []
    lines: list[tuple[spg.Line, object]] = []
    segments: list[tuple[spg.Segment, object]] = []
    polygons: list[tuple[object, object]] = []

    for el, info in model.items():
        if isinstance(el, spg.Point2D):
            pts.append((el, info))
        elif isinstance(el, spg.Circle):
            circles.append((el, info))
        elif isinstance(el, spg.Line2D):
            lines.append((el, info))
        elif isinstance(el, spg.Segment2D):
            segments.append((el, info))
        elif isinstance(el, (spg.Polygon, spg.Triangle, spg.RegularPolygon)):
            polygons.append((el, info))

    if math_bounds is None:
        xs: list[float] = []
        ys: list[float] = []
        for pt, _ in pts:
            xs.append(float(pt.x.evalf()))
            ys.append(float(pt.y.evalf()))
        for circ, _ in circles:
            cx = float(circ.center.x.evalf())
            cy = float(circ.center.y.evalf())
            cr = abs(float(circ.radius.evalf()))
            xs.extend([cx - cr, cx + cr])
            ys.extend([cy - cr, cy + cr])
        xmin = min(xs) if xs else -1.0
        xmax = max(xs) if xs else 1.0
        ymin = min(ys) if ys else -1.0
        ymax = max(ys) if ys else 1.0
        span_x = max(xmax - xmin, 1e-3)
        span_y = max(ymax - ymin, 1e-3)
        xmin -= 0.08 * span_x
        xmax += 0.08 * span_x
        ymin -= 0.08 * span_y
        ymax += 0.08 * span_y
    else:
        xmin, xmax, ymin, ymax = math_bounds

    avail_w = width - 2.0 * padding
    avail_h = height - 2.0 * padding
    scale = min(avail_w / max(xmax - xmin, 1e-6), avail_h / max(ymax - ymin, 1e-6))
    cx_math = 0.5 * (xmin + xmax)
    cy_math = 0.5 * (ymin + ymax)

    def to_px(mx: float, my: float) -> tuple[float, float]:
        px = 0.5 * width + (mx - cx_math) * scale
        py = 0.5 * height - (my - cy_math) * scale
        return px, py

    out: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'viewBox="0 0 {width} {height}" role="img">',
        f"  <style>\n{EMBEDDED_SVG_STYLE}\n  </style>",
        f'  <rect class="canvas-bg" x="0" y="0" width="{width}" height="{height}" rx="8"/>',
    ]

    # 1. Polygons
    out.append('  <g class="layer-polygons">')
    for poly, info in polygons:
        classes = set(getattr(info, "classes", {}).keys())
        p_cls = "geom-polygon"
        if "durer_pentagon" in classes:
            p_cls += " durer-poly"
        elif "euclid_pentagon" in classes:
            p_cls += " euclid-poly"
        elif "frame_square" in classes or "glass_frame_rect" in classes:
            p_cls += " frame-poly"
        elif "glyph_body" in classes or "glyph_crossbar" in classes or "textura_module" in classes:
            p_cls += " glyph-poly"
        elif "glyph_counter" in classes:
            p_cls += " counter-poly"
        elif "face_3gon" in classes:
            p_cls += " net-3gon"
        elif "face_4gon" in classes:
            p_cls += " net-4gon"
        elif "face_5gon" in classes:
            p_cls += " net-5gon"
        elif "cube_front_face" in classes:
            p_cls += " durer-poly"

        coords_str = " ".join(
            f"{_fmt(px)},{_fmt(py)}"
            for px, py in (
                to_px(float(v.x.evalf()), float(v.y.evalf())) for v in poly.vertices
            )
        )
        pid = html.escape(str(getattr(info, "ID", "")))
        out.append(f'    <polygon class="{p_cls}" data-ref="{pid}" points="{coords_str}"/>')
    out.append("  </g>")

    # 2. Circles
    out.append('  <g class="layer-circles">')
    for circ, info in circles:
        classes = set(getattr(info, "classes", {}).keys())
        c_cls = "geom-circle"
        if "given" in classes or "outer_circle" in classes or "plan_base_circle" in classes:
            c_cls += " primary-circle"
        elif "bowl_circle" in classes:
            c_cls += " bowl-circle"
        elif "serif_circle" in classes:
            c_cls += " serif-circle"

        cx_p, cy_p = to_px(float(circ.center.x.evalf()), float(circ.center.y.evalf()))
        r_p = abs(float(circ.radius.evalf())) * scale
        cid = html.escape(str(getattr(info, "ID", "")))
        out.append(
            f'    <circle class="{c_cls}" data-ref="{cid}" '
            f'cx="{_fmt(cx_p)}" cy="{_fmt(cy_p)}" r="{_fmt(r_p)}"/>'
        )
    out.append("  </g>")

    # 3. Clipped Lines
    if show_lines and lines:
        out.append('  <g class="layer-lines">')
        for ln, info in lines:
            clipped = _clip_line(ln, xmin, xmax, ymin, ymax)
            if clipped is None:
                continue
            (mx1, my1), (mx2, my2) = clipped
            px1, py1 = to_px(mx1, my1)
            px2, py2 = to_px(mx2, my2)
            classes = set(getattr(info, "classes", {}).keys())
            l_cls = "geom-line"
            if "durer_ray" in classes or "vanishing_ray" in classes:
                l_cls += " ray-line"
            lid = html.escape(str(getattr(info, "ID", "")))
            out.append(
                f'    <path class="{l_cls}" data-ref="{lid}" d="{_seg_path_d(px1, py1, px2, py2)}"/>'
            )
        out.append("  </g>")

    # 4. Segments
    out.append('  <g class="layer-segments">')
    for seg, info in segments:
        px1, py1 = to_px(float(seg.p1.x.evalf()), float(seg.p1.y.evalf()))
        px2, py2 = to_px(float(seg.p2.x.evalf()), float(seg.p2.y.evalf()))
        classes = set(getattr(info, "classes", {}).keys())
        s_cls = "geom-segment"
        if "fold_edge" in classes:
            s_cls += " fold-seam"
        elif "cut_edge" in classes:
            s_cls += " cut-seam"
        elif "spiral_chord" in classes or "ellipse_arc" in classes or "cut_plane" in classes:
            s_cls += " spiral-seg"
        elif "sector_ray" in classes or "sight_ray" in classes:
            s_cls += " sector-seg"
        elif "projector_line" in classes or "cone_slice" in classes or "ellipse_ordinate" in classes:
            s_cls += " projector-seg"
        elif "heptagon_side" in classes or "plan_chord" in classes or "tail_axis" in classes:
            s_cls += " accent-seg"
        sid = html.escape(str(getattr(info, "ID", "")))
        out.append(
            f'    <path class="{s_cls}" data-ref="{sid}" d="{_seg_path_d(px1, py1, px2, py2)}"/>'
        )
    out.append("  </g>")

    # 5. Points & Collision-Free Labels
    labels_map = labeled_keys or {}
    placed_boxes: list[tuple[float, float]] = []
    out.append('  <g class="layer-points">')
    label_elems: list[str] = []

    # Centroid of all points to push labels radially outward
    all_px = [to_px(float(p.x.evalf()), float(p.y.evalf())) for p, _ in pts]
    cen_x = sum(p[0] for p in all_px) / max(len(all_px), 1)
    cen_y = sum(p[1] for p in all_px) / max(len(all_px), 1)

    for pt, info in pts:
        key_id = str(getattr(info, "ID", ""))
        has_label = key_id in labels_map
        if not has_label and not show_unlabeled_points:
            continue
        px, py = to_px(float(pt.x.evalf()), float(pt.y.evalf()))
        classes = set(getattr(info, "classes", {}).keys())
        pt_cls = "geom-point"
        if "durer_vertex" in classes or "spiral_pt" in classes:
            pt_cls += " durer-pt"
        elif "euclid_vertex" in classes:
            pt_cls += " euclid-pt"
        elif "vanishing_point" in classes or "heptagon_overshoot" in classes:
            pt_cls += " accent-pt"

        r_dot = "3.7" if has_label else "2.4"
        lx = html.escape(sp.latex(pt.x))
        ly = html.escape(sp.latex(pt.y))
        disp = labels_map.get(key_id, key_id)
        esc_id = html.escape(key_id)
        esc_disp = html.escape(disp)
        out.append(
            f'    <circle class="{pt_cls}" data-ref="{esc_id}" data-aliases="{esc_id},{esc_disp}" '
            f'data-latex-x="{lx}" data-latex-y="{ly}" cx="{_fmt(px)}" cy="{_fmt(py)}" r="{r_dot}">'
            f"<title>{esc_disp}: ({lx}, {ly})</title></circle>"
        )

        if has_label:
            vx = px - cen_x
            vy = py - cen_y
            norm = math.hypot(vx, vy)
            if norm < 1e-3:
                vx, vy = 0.7, -0.7
            else:
                vx, vy = vx / norm, vy / norm

            best_tx, best_ty = px + 14.0 * vx, py + 14.0 * vy
            for ang_off in (0.0, 0.45, -0.45, 0.9, -0.9, 1.4, -1.4, math.pi):
                ca, sa = math.cos(ang_off), math.sin(ang_off)
                rx = vx * ca - vy * sa
                ry = vx * sa + vy * ca
                cand_x = px + 15.5 * rx
                cand_y = py + 15.5 * ry + 4.0
                if all(math.hypot(cand_x - bx, cand_y - by) > 16.0 for bx, by in placed_boxes):
                    best_tx, best_ty = cand_x, cand_y
                    break
            placed_boxes.append((best_tx, best_ty))
            label_elems.append(
                f'    <text class="euclid-label" data-ref="{esc_id}" '
                f'x="{_fmt(best_tx)}" y="{_fmt(best_ty)}" text-anchor="middle">'
                f"{_format_label_xml(disp)}</text>"
            )

    out.append("  </g>")
    if label_elems or extra_annotations:
        out.append('  <g class="layer-labels">')
        out.extend(label_elems)
        for ax, ay, text in extra_annotations or []:
            px, py = to_px(ax, ay)
            out.append(
                f'    <text class="caption-note" x="{_fmt(px)}" y="{_fmt(py)}" '
                f'text-anchor="middle">{html.escape(text)}</text>'
            )
        out.append("  </g>")

    out.append("</svg>\n")
    return "\n".join(out)


def export_svg(svg_text: str, output_path: str | Path) -> Path:
    """Write ``svg_text`` to ``output_path`` creating parent directories if needed."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg_text, encoding="utf-8")
    return path


def _translate_net_into_model(
    model: Model,
    net_key: str,
    dx: sp.Expr,
    dy: sp.Expr,
) -> None:
    nets = construct_durer_polyhedral_nets()
    net = nets[net_key]
    sub_model = polyhedral_net_to_model(net)
    pt_remap: dict[spg.Point, spg.Point] = {}
    for el, info in sub_model.items():
        if isinstance(el, spg.Point2D):
            pt_remap[el] = model.set_point(
                el.x + dx, el.y + dy, classes=list(info.classes.keys())
            )
    for el, info in sub_model.items():
        if isinstance(el, (spg.Polygon, spg.Triangle, spg.RegularPolygon)):
            model.set_polygon([pt_remap[v] for v in el.vertices], classes=list(info.classes.keys()))
        elif isinstance(el, spg.Segment2D):
            model.set_segment(
                pt_remap[el.p1], pt_remap[el.p2], classes=list(info.classes.keys())
            )


def generate_all_codex_figures(output_dir: str | Path) -> list[Path]:
    """Generate all 10 interactive ``.euclid-graphic`` SVG figures for ``docsrc/_static/figures/``."""
    out_dir = Path(output_dir)
    written: list[Path] = []

    # 1. Book I: 12-Sector Archimedean Spiral (Schneckenlini)
    sp_res = construct_durer_spiral_volute(turns=2)
    svg1 = render_model_svg(
        sp_res.model,
        width=700,
        height=620,
        math_bounds=(-13.5, 13.5, -13.5, 13.5),
        labeled_keys={"O": "O", "S6": "P_6", "S12": "P_12", "S18": "P_18", "S24": "P_24"},
        extra_annotations=[(0.0, -13.0, "Book I, Figs. 7 & 17 — 12-Sector Archimedean Schneckenlini")],
        show_unlabeled_points=True,
    )
    written.append(export_svg(svg1, out_dir / "book1_spiral_volute.svg"))

    # 2. Book I: Two-View Conic Projection (Elipsis / Eierlini)
    con_res = construct_durer_conic_sections()
    svg2 = render_model_svg(
        con_res.model,
        width=800,
        height=660,
        math_bounds=(-7.5, 16.8, -16.2, 13.2),
        labeled_keys={
            "Apex": "a",
            "Base_L": "b",
            "Base_R": "c",
            "f": "f",
            "g": "g",
            "O_plan": "O_plan",
        },
        extra_annotations=[
            (0.0, 12.7, "Aufriss (Elevation Cone)"),
            (0.0, -15.7, "Grundriss (Circular Plan)"),
            (12.0, 8.3, "Elipsis / Eierlini (w_k = w_{12-k})"),
        ],
        show_unlabeled_points=True,
    )
    written.append(export_svg(svg2, out_dir / "book1_cone_ellipse_projection.svg"))

    # 3. Book II: Dürer Single-Aperture Pentagon vs. Euclid Q(phi) Pentagon
    pent_res = construct_durer_vs_euclid_pentagon()
    svg3 = render_model_svg(
        pent_res.model,
        width=780,
        height=620,
        math_bounds=(-1.65, 2.65, -1.95, 1.85),
        labeled_keys={
            "A": "a",
            "B": "b",
            "C_ves": "c",
            "D": "d",
            "E": "e",
            "F": "f",
            "G": "g",
            "H_durer": "h",
            "I_durer": "i",
            "K_durer": "k",
            "H_euclid": "H_phi",
            "I_euclid": "I_phi",
            "K_euclid": "K_phi",
            "X_phi": "phi",
        },
        extra_annotations=[
            (0.5, 1.74, "Solid Gold: Dürer Rusty Compass (108.37°)  |  Dashed Blue: Euclid Q(phi) (108°)"),
        ],
    )
    written.append(export_svg(svg3, out_dir / "book2_durer_vs_euclid_pentagon.svg"))

    # 4. Book II: Workshop Heptagon & Circle Quadrature
    hep_res = construct_durer_heptagon_workshop()
    # Add quadrature square & circle to the right at x_offset = 3
    q_mod = hep_res.model
    sq_c = q_mod.set_point(sp.Integer(2), sp.Rational(-4, 5), classes=["frame"], ID="Sq_c")
    sq_d = q_mod.set_point(sp.Rational(18, 5), sp.Rational(-4, 5), classes=["frame"], ID="Sq_d")
    sq_b = q_mod.set_point(sp.Rational(18, 5), sp.Rational(4, 5), classes=["frame"], ID="Sq_b")
    sq_a = q_mod.set_point(sp.Integer(2), sp.Rational(4, 5), classes=["frame"], ID="Sq_a")
    q_mod.set_polygon([sq_c, sq_d, sq_b, sq_a], classes=["frame_square"])
    q_mod.set_segment(sq_c, sq_b, classes=["spiral_chord"])
    q_cen = q_mod.set_point(sp.Rational(14, 5), sp.Integer(0), classes=["given"], ID="O_quad")
    r_quad = sp.Rational(16, 25) * sp.sqrt(2)
    q_rim = q_mod.set_point(sp.Rational(14, 5) + r_quad, sp.Integer(0), classes=["aux"])
    q_mod.construct_circle(q_cen, q_rim, classes=["bowl_circle"])

    svg4 = render_model_svg(
        q_mod,
        width=820,
        height=520,
        math_bounds=(-1.35, 4.05, -1.35, 1.35),
        labeled_keys={
            "O": "a",
            "B": "b",
            "C": "c",
            "E": "e",
            "T_top": "d",
            "W0": "W_0",
            "W1": "W_1",
            "W2": "W_2",
            "W6": "W_6",
            "O_quad": "O_q",
        },
        extra_annotations=[
            (0.0, -1.24, "Heptagon: s_7 = sqrt(3)/2 R (P_7(3/4) = -1/64)"),
            (2.8, -1.24, "Quadrature: d = (8/10) diag => pi = 25/8 = 3.125"),
        ],
    )
    written.append(export_svg(svg4, out_dir / "book2_heptagon_and_quadrature.svg"))

    # 5. Book III: Roman Antiqua Capital A in 10x10 Square
    a_res = construct_durer_roman_letter_A()
    svg5 = render_model_svg(
        a_res.model,
        width=680,
        height=640,
        math_bounds=(-1.2, 11.2, -1.2, 11.2),
        labeled_keys={
            "a": "a",
            "b": "b",
            "c": "c",
            "d": "d",
            "e": "e",
            "f": "f",
            "g": "g",
            "h": "h",
            "i": "i",
            "k": "k",
            "V_counter": "V",
            "S_out_L": "S_L",
            "S_out_R": "S_R",
        },
        extra_annotations=[(5.0, -0.9, "Book III, p. 115 — Roman Antiqua A (10x10 Square, 1 : 1/3 Contrast)")],
    )
    written.append(export_svg(svg5, out_dir / "book3_roman_letter_a.svg"))

    # 6. Book III: Shifted-Diagonal Roman O/Q & Textura Minuscules
    q_res = construct_durer_roman_letter_Q()
    svg6_oq = render_model_svg(
        q_res.model,
        width=780,
        height=580,
        math_bounds=(-1.2, 19.2, -4.3, 11.2),
        labeled_keys={
            "a": "a",
            "b": "b",
            "c": "c",
            "d": "d",
            "i": "i",
            "f": "f",
            "g": "g",
            "P_NW": "P_1",
            "P_SE": "P_2",
            "Q_tip": "h",
        },
        extra_annotations=[
            (8.5, -3.9, "Book III, pp. 124–125 — Two-Circle Shifted Diagonal O & Q (|fg| = 1, r = 5 - sqrt(2)/4)"),
        ],
    )
    written.append(export_svg(svg6_oq, out_dir / "book3_roman_letters_oq.svg"))

    # 7. Book III: Modular Gothic Textura Minuscules i, n, m
    tex_res = construct_durer_textura_minuscules()
    svg7_tex = render_model_svg(
        tex_res.model,
        width=800,
        height=460,
        math_bounds=(-1.2, 13.0, -2.2, 5.2),
        extra_annotations=[
            (0.5, -1.85, "i (3 squares + 2 ort-fierungen)"),
            (4.2, -1.85, "n (pitch = sqrt(2))"),
            (9.9, -1.85, "m (3 modular stems)"),
        ],
        show_lines=False,
    )
    written.append(export_svg(svg7_tex, out_dir / "book3_textura_minuscules.svg"))

    # 8. Book IV: Platonic Nets — Tetrahedron, Octahedron, Cube
    plat_mod = Model("durer_platonic_trio", logger=False, auto_intersect=False)
    _translate_net_into_model(plat_mod, "tetrahedron", sp.Integer(0), sp.Rational(1, 2))
    _translate_net_into_model(plat_mod, "octahedron", sp.Rational(7, 2), sp.Rational(1, 2))
    _translate_net_into_model(plat_mod, "cube", sp.Integer(8), sp.Rational(-1, 2))
    svg8 = render_model_svg(
        plat_mod,
        width=840,
        height=480,
        math_bounds=(-1.2, 10.6, -2.1, 3.1),
        extra_annotations=[
            (0.5, -1.85, "Tetrahedron (Fig. 29)"),
            (4.2, -1.85, "Octahedron (Fig. 30)"),
            (8.5, -1.85, "Cube (Fig. 32)"),
        ],
        show_lines=False,
        show_unlabeled_points=True,
    )
    written.append(export_svg(svg8, out_dir / "book4_platonic_nets.svg"))

    # 9. Book IV: Dodecahedron Double-Rosette Net over Q(sqrt(5), sin 36°)
    nets = construct_durer_polyhedral_nets()
    dod_mod = polyhedral_net_to_model(nets["dodecahedron"])
    svg9 = render_model_svg(
        dod_mod,
        width=840,
        height=560,
        extra_annotations=[
            (2.8, -2.55, "Book IV, Fig. 33 — Regular Dodecahedron Net (Two 6-Pentagon Rosettes over Q(phi))"),
        ],
        show_lines=False,
        show_unlabeled_points=True,
    )
    written.append(export_svg(svg9, out_dir / "book4_dodecahedron_net.svg"))

    # 10. Book IV: Cuboctahedron Net & Central Perspective Cube Apparatus
    persp_res = construct_durer_perspective_apparatus()
    # Place Cuboctahedron net to the left of the glass frame so Book IV's two twin glories shine side by side,
    # OR export two separate clean SVGs? Let's export BOTH:
    # 10a: Icosahedron + Cuboctahedron planar nets
    ico_cub_mod = Model("durer_ico_cuboctahedron", logger=False, auto_intersect=False)
    _translate_net_into_model(ico_cub_mod, "icosahedron", sp.Integer(0), sp.Rational(1, 2))
    _translate_net_into_model(ico_cub_mod, "cuboctahedron", sp.Rational(19, 2), sp.Rational(1, 2))
    svg10 = render_model_svg(
        ico_cub_mod,
        width=860,
        height=480,
        math_bounds=(-0.8, 15.2, -3.5, 4.8),
        extra_annotations=[
            (2.8, -3.1, "Icosahedron (Fig. 31 — 20 Triangles)"),
            (10.8, -3.1, "Archimedean Cuboctahedron (Fig. 37 — 6 Squares + 8 Triangles)"),
        ],
        show_lines=False,
        show_unlabeled_points=True,
    )
    written.append(export_svg(svg10, out_dir / "book4_cuboctahedron_icosahedron_nets.svg"))

    # 10b: Central Perspective Cube Apparatus (Book IV, Figs. 56–63)
    svg11 = render_model_svg(
        persp_res.model,
        width=740,
        height=560,
        math_bounds=(-3.4, 5.0, -1.5, 6.5),
        labeled_keys={
            "F_BL": "A'",
            "F_BR": "B'",
            "F_TR": "C'",
            "F_TL": "D'",
            "B_BL": "E'",
            "B_BR": "F'",
            "B_TR": "G'",
            "B_TL": "H'",
            "M_depth": "M'",
            "V_x": "V_x",
        },
        extra_annotations=[
            (0.8, -1.25, "Book IV, Figs. 56–63 — Glass Picture Plane Projection (CR(A', E'; M', V_x) = -1)"),
        ],
    )
    written.append(export_svg(svg11, out_dir / "book4_perspective_cube_apparatus.svg"))

    return written
