"""Module entrypoint for ``python -m geometor.durer``."""

from __future__ import annotations

import sys

from geometor.durer.cli import main

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
