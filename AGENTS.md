# Log Pipeline Developer & Agent Guide

## Core Commands
- Run strict pipeline: `./run_pipeline.sh` or `runlog`
- Run unit tests: `python3 test_main.py`
- Run type & linter check: `pre-commit run --all-files`

## Code Style & Standards
- Python Version: >= 3.10 (strict type hints required for all function signatures)
- Formatting & Linting: Managed via Ruff and Mypy.
- Error Handling: Use defensive assertions and explicit `ValueError`.
