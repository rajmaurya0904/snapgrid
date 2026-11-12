# Snapgrid

**An interactive visual grid overlay for web pages that lets designers snap elements to a configurable baseline, filling the gap where no easy-to-use browser extension exists.**

Every time you build a web layout from scratch, vertical rhythm drifts. Designing without live baseline guides means manual pixel nudging, inconsistent typography spacing, and endless inspection in developer tools.

## Example

Generate CSS for a 20px baseline grid overlay:

```python
from snapgrid.grid import GridOverlay
print(GridOverlay(20).generate_css())
```

```css
background-size: 100% 20px;
```

## Install

```bash
pip install -e .
```

## Usage

- Python API: initialize `GridOverlay(baseline)` and call `generate_css()`.
- Command-line interface: run `snapgrid` to print generated overlay CSS.

## How it works

- Stores a configurable baseline pixel integer.
- Computes baseline grid overlay CSS rules.
- Emits standard properties including `background-size`.

## Limitations

- Does not currently render an interactive browser UI.
- Generates horizontal baseline grid CSS rules only.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
