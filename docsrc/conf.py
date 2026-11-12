"""Sphinx configuration for GEOMETOR • durer."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _p in (_REPO_ROOT / "src", _REPO_ROOT.parent / "model" / "src"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.durer as module  # noqa: E402
from geometor.durer.sphinx_ext import (  # noqa: E402
    configure_local_intersphinx,
    register_german_1525_book_track,
)

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "durer"
repo_name = "durer"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

if "geometor.durer.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.durer.sphinx_ext")  # noqa: F405

register_german_1525_book_track()
configure_local_intersphinx(intersphinx_mapping, _REPO_ROOT)  # noqa: F405

project = "GEOMETOR • durer"
author = "Albrecht Dürer"
copyright = "1525 Nuremberg (Editio Princeps) • 1532 Camerarius • Digital Edition GEOMETOR"

html_static_path = ["_static"]

autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
if "modules/api/geometor/durer/index.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("modules/api/geometor/durer/index.rst")  # noqa: F405

suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]
