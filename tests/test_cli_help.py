"""Tests for CLI help output."""

import subprocess
import sys


def test_cli_help() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "snapgrid.cli", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "usage:" in result.stdout or "Usage:" in result.stdout
