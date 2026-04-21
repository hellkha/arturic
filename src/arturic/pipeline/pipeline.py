from datetime import datetime
from pathlib import Path

from arturic.file_finder.finder import get_valid_file_paths
from arturic.entry_validator.validators import is_valid_in_timeframe
from arturic.file_reader.reader import read_file
from arturic.utils.logger import log_invalid_entry
from arturic.models.result import PipelineResult


def run_pipeline(
    data_dir: Path, start_period: datetime, end_period: datetime
) -> PipelineResult:
    """
    Executes the main data pipeline, handling file discovery,
    validation, logging of invalid entries, and metric aggregation.
    """
    filepaths = get_valid_file_paths(data_dir)

    total_loaded = 0
    invalid_entries_count = 0
    valid_entries = []
    total_value = 0

    for filepath in filepaths:
        try:
            entries = read_file(filepath)
        except Exception as e:
            raise Exception(f"Failed to read file: {filepath}, Error: {e}")

        for entry in entries:
            total_loaded += 1

            if is_valid_in_timeframe(entry, start_period, end_period):
                valid_entries.append(entry)
                total_value += entry.value
            else:
                invalid_entries_count += 1
                log_invalid_entry(entry)

    valid_entries_count = len(valid_entries)

    return PipelineResult(
        total_loaded=total_loaded,
        valid_entries=valid_entries_count,
        invalid_entries=invalid_entries_count,
        total_value=total_value,
    )
