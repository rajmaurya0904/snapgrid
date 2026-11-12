"""Grid overlay module."""


class GridOverlay:
    """An interactive visual grid overlay with a configurable baseline."""

    def __init__(self, baseline: int) -> None:
        self.baseline = baseline

    def snap_position(self, y: int) -> int:
        """Return the nearest multiple of baseline to y (rounding down)."""
        return (y // self.baseline) * self.baseline

