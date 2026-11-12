"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import snapgrid


def test_version_is_set() -> None:
    assert snapgrid.__version__
