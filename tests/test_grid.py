"""Tests for grid module."""

from snapgrid.grid import GridOverlay


def test_grid_overlay_baseline() -> None:
    grid = GridOverlay(10)
    assert grid.baseline == 10


def test_generate_css_acceptance() -> None:
    assert GridOverlay(20).generate_css() == "background-size: 100% 20px;"


def test_generate_css_various_baselines() -> None:
    assert GridOverlay(8).generate_css() == "background-size: 100% 8px;"
    assert GridOverlay(24).generate_css() == "background-size: 100% 24px;"


def test_snap_position_acceptance() -> None:
    assert GridOverlay(10).snap_position(27) == 20
    assert GridOverlay(15).snap_position(44) == 30


def test_snap_position_edge_cases() -> None:
    grid = GridOverlay(10)
    assert grid.snap_position(0) == 0
    assert grid.snap_position(10) == 10
    assert grid.snap_position(19) == 10
    assert grid.snap_position(-5) == -10
    assert grid.snap_position(-15) == -20
