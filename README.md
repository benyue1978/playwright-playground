# Cursor Python Template

## Environment Setup

```shell
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install uv (fast Python package manager)
pip install uv

# Install dependencies from pyproject.toml
uv pip install -r <(uv pip compile pyproject.toml)

# Install Playwright browsers
python -m playwright install
```

## Code Style Check

```shell
ruff check .
```

## Run Tests

```shell
pytest
```

## Dependency Management

- All dependencies are managed in `pyproject.toml`.
- Use `uv` for fast and reproducible installs.
- Update dependencies by editing `pyproject.toml` and re-running the install steps above.
