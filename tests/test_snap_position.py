"""Tests for snap_position logic in GridOverlay."""

import pytest

from snapgrid.grid import GridOverlay


@pytest.mark.parametrize(
    "baseline, y, expected",
    [
        # Exact multiples
        (10, 0, 0),
        (10, 10, 10),
        (10, 20, 20),
        (10, -10, -10),
        (10, -20, -20),
        # Between multiples (rounds down towards negative infinity per integer division)
        (10, 5, 0),
        (10, 15, 10),
        (10, -5, -10),
        (10, -15, -20),
        # Zero baseline edge case (though baseline is typically positive, python // behavior)
        # Custom baseline
        (8, 0, 0),
        (8, 12, 8),
        (8, 16, 16),
        (8, -12, -16),
    ],
)
def test_snap_position(baseline: int, y: int, expected: int) -> None:
    grid = GridOverlay(baseline)
    assert grid.snap_position(y) == expected
