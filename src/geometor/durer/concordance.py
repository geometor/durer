"""Scholarly apparatus & cross-corpus concordance loader for *Underweysung der Messung* (1525)."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

__all__ = [
    "ConcordanceEntry",
    "UnderweysungApparatus",
    "default_resources_dir",
    "load_apparatus",
]


@dataclass(frozen=True)
class ConcordanceEntry:
    """Single cross-corpus concordance link from Dürer's *Underweysung* to GEOMETOR."""

    id: str
    book: int
    unit: str
    durer_locus: str
    german_term: str
    latin_1532_term: str
    english_title: str
    classification: str
    sister_repos: tuple[str, ...]
    algebraic_field: str
    summary: str


@dataclass(frozen=True)
class UnderweysungApparatus:
    """Loaded JSON apparatus registries for ``resources/underweysung/``."""

    sources_manifest: dict[str, Any]
    concordance: tuple[ConcordanceEntry, ...]
    persons: dict[str, dict[str, Any]]
    citations: dict[str, dict[str, Any]]
    glossary: dict[str, dict[str, Any]]


def default_resources_dir() -> Path:
    """Locate ``resources/underweysung/`` relative to the repository root."""
    return Path(__file__).resolve().parents[3] / "resources" / "underweysung"


def load_apparatus(resources_dir: str | Path | None = None) -> UnderweysungApparatus:
    """Load all five JSON apparatus files from ``resources/underweysung/``."""
    base = Path(resources_dir) if resources_dir is not None else default_resources_dir()
    sources = json.loads((base / "sources_manifest.json").read_text(encoding="utf-8"))
    conc_raw = json.loads((base / "concordance.json").read_text(encoding="utf-8"))
    persons = json.loads((base / "persons.json").read_text(encoding="utf-8"))
    citations = json.loads((base / "citations.json").read_text(encoding="utf-8"))
    glossary = json.loads((base / "glossary.json").read_text(encoding="utf-8"))

    entries = tuple(
        ConcordanceEntry(
            id=item["id"],
            book=int(item["book"]),
            unit=item["unit"],
            durer_locus=item["durer_locus"],
            german_term=item["german_term"],
            latin_1532_term=item["latin_1532_term"],
            english_title=item["english_title"],
            classification=item["classification"],
            sister_repos=tuple(item["sister_repos"]),
            algebraic_field=item["algebraic_field"],
            summary=item["summary"],
        )
        for item in conc_raw["entries"]
    )

    return UnderweysungApparatus(
        sources_manifest=sources,
        concordance=entries,
        persons=persons,
        citations=citations,
        glossary=glossary,
    )
