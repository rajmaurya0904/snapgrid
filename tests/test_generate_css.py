"""Tests for GridOverlay.generate_css."""

from snapgrid.grid import GridOverlay


def test_generate_css_contains_background_size_for_baseline():
    overlay = GridOverlay(baseline=8)
    css = overlay.generate_css()
    assert "background-size" in css
    assert "8px" in css


def test_generate_css_background_size_matches_baseline():
    overlay = GridOverlay(baseline=16)
    css = overlay.generate_css()
    assert "background-size: 100% 16px" in css


def test_generate_css_background_size_changes_with_baseline():
    css_8 = GridOverlay(baseline=8).generate_css()
    css_24 = GridOverlay(baseline=24).generate_css()
    assert "100% 8px" in css_8
    assert "100% 24px" in css_24
    assert css_8 != css_24