from pathlib import Path
from arturic.file_reader.enums import FileType


def get_valid_file_paths(directory: list[Path, str]) -> list[Path]:
    """
    Scans a directory recursively and returns a list of valid file paths.
    """
    directory = Path(directory)
    paths = []
    supported_extensions = {ext.value for ext in FileType}

    for filepath in directory.rglob("*"):
        if filepath.is_file() and filepath.suffix in supported_extensions:
            paths.append(filepath)

    return paths
