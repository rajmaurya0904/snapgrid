"""Tests for CLI module."""

import subprocess
import sys


def test_cli_baseline() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "snapgrid.cli", "--baseline", "10"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "background-size" in result.stdout
    assert "10px" in result.stdout
