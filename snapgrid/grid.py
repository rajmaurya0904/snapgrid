"""Grid overlay module."""


class GridOverlay:
    """An interactive visual grid overlay with a configurable baseline."""

    def __init__(self, baseline: int) -> None:
        self.baseline = baseline
