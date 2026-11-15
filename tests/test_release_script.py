"""Tests for the release script output."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "release.py"


def test_release_script_prints_expected_message() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == (
        "Release steps: bump version, update changelog, tag, publish"
    )