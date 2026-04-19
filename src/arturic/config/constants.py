from pathlib import Path


def _find_project_root() -> Path:
    """Walk up from this file until we find the project root (where pyproject.toml lives)."""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    raise FileNotFoundError("Could not find project root (no pyproject.toml found)")

# Path to project root
PROJECT_ROOT = _find_project_root()

# Path to the data directory
DATA_DIR = PROJECT_ROOT / "data"

# Path to the log directory
LOG_DIR = PROJECT_ROOT / "logs"
