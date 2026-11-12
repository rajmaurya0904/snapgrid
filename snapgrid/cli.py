"""Command line interface for snapgrid."""

import argparse
import sys

from snapgrid.grid import GridOverlay


def main() -> None:
    """Parse arguments and print generated CSS to stdout."""
    parser = argparse.ArgumentParser(
        description="Generate baseline grid CSS overlay."
    )
    parser.add_argument(
        "--baseline",
        type=int,
        default=10,
        help="Baseline grid size in pixels (default: 10)",
    )
    args = parser.parse_args()

    grid = GridOverlay(baseline=args.baseline)
    sys.stdout.write(grid.generate_css() + "\n")


if __name__ == "__main__":
    main()
