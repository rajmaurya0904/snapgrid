"""Tests for grid module."""

from snapgrid.grid import GridOverlay


def test_grid_overlay_baseline() -> None:
    grid = GridOverlay(10)
    assert grid.baseline == 10
