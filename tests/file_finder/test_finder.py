import pytest
from pathlib import Path
from arturic.file_finder.finder import get_valid_file_paths


def test_get_file_paths_finds_supported_extensions(tmp_path):
    # Create supported files in root
    (tmp_path / "data1.csv").touch()
    (tmp_path / "data2.mdr").touch()
    (tmp_path / "data3.txt").touch()

    # Nested directory with supported file
    nested_dir = tmp_path / "nested"
    nested_dir.mkdir()
    (nested_dir / "data6.csv").touch()

    paths = get_valid_file_paths(tmp_path)
    assert len(paths) == 4


def test_get_file_paths_empty_directory(tmp_path):
    paths = get_valid_file_paths(tmp_path)
    assert len(paths) == 0


def test_get_file_paths_no_supported_extensions(tmp_path):
    (tmp_path / "data.log").touch()
    (tmp_path / "data.json").touch()
    paths = get_valid_file_paths(tmp_path)
    assert len(paths) == 0


def test_get_file_paths_with_string_path(tmp_path):
    (tmp_path / "data1.csv").touch()
    paths = get_valid_file_paths(str(tmp_path))
    assert len(paths) == 1
    assert paths[0].name == "data1.csv"
