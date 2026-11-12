"""Tests for GridOverlay initialization."""

from snapgrid.grid import GridOverlay


def test_grid_overlay_initialization() -> None:
    """Test that GridOverlay initializes with the correct baseline attribute."""
    grid = GridOverlay(16)
    assert grid.baseline == 16

    grid_default = GridOverlay(8)
    assert grid_default.baseline == 8
