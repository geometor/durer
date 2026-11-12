"""Runtime Sphinx & photon-platform/publish integration for GEOMETOR Dürer.

Labels the ``de`` companion track as ``"German (1525)"`` in ``photon_platform.publish.book``
at Sphinx build time (without modifying ``photon-platform/publish``) and binds offline-safe
local ``objects.inv`` inventories across GEOMETOR sister repositories.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def register_german_1525_book_track() -> None:
    """Relabel ``<stem>-de`` companion tracks in ``photon_platform.publish.book`` as ``German (1525)``."""
    try:
        from photon_platform.publish import book
    except ImportError:
        return

    book._TRACK_SUFFIX_PATTERNS = [
        (pat, key, "German (1525)" if key == "de" else lbl)
        for pat, key, lbl in book._TRACK_SUFFIX_PATTERNS
    ]

    if getattr(book.detect_companion_tracks, "_durer_de_patched", False):
        return

    orig_detect = book.detect_companion_tracks

    def _detect_with_german_1525(env: Any, pagename: str) -> list[dict[str, Any]]:
        tracks = orig_detect(env, pagename)
        updated: list[dict[str, Any]] = []
        for tr in tracks:
            item = dict(tr)
            if item.get("key") == "de":
                item["label"] = "German (1525)"
            updated.append(item)
        return updated

    _detect_with_german_1525._durer_de_patched = True  # type: ignore[attr-defined]
    book.detect_companion_tracks = _detect_with_german_1525


def configure_local_intersphinx(
    intersphinx_mapping: dict[str, Any], project_root: Path
) -> None:
    """Bind local ``objects.inv`` files across GEOMETOR sister repos for zero-warning offline builds."""
    geometor_dir = project_root.parent
    sister_repos = (
        "euclid",
        "elements",
        "pacioli",
        "pappus",
        "lemoine",
        "hilbert",
        "casey",
        "plato",
        "thompson",
        "divine",
        "model",
        "explorer",
        "etc",
        "proclus",
    )
    for repo in sister_repos:
        inv_path = geometor_dir / repo / "docs" / "objects.inv"
        if inv_path.exists():
            key = repo.replace("-", "_")
            intersphinx_mapping[key] = (
                f"https://geometor.github.io/{repo}",
                str(inv_path),
            )

    for key in list(intersphinx_mapping.keys()):
        _url, inv = intersphinx_mapping[key]
        if inv is None or (isinstance(inv, str) and not Path(inv).exists()):
            del intersphinx_mapping[key]


def setup(app: Any) -> dict[str, Any]:
    """Sphinx extension entrypoint registering the ``German (1525)`` track label."""
    register_german_1525_book_track()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
