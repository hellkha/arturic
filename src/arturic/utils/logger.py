from dataclasses import asdict
from pathlib import Path
import logging
import json
from arturic.config.constants import LOG_DIR
from arturic.models.entry import Entry


def _setup_logger(name: str, log_file: str, log_dir: Path) -> logging.Logger:
    """Helper to set up a logger with a specific file backend dynamically."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Clear handlers completely so tests can fluidly redirect logs back and forth
    logger.handlers.clear()

    log_dir.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(log_dir / log_file, mode="a")
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def log_invalid_entry(entry: Entry, log_dir: Path = LOG_DIR):
    """Logs an invalid entry as a JSON string with the reading timestamp handled automatically by the logger."""
    invalid_logger = _setup_logger("invalid_entries", "invalid_entries.log", log_dir)
    entry_dict = asdict(entry)

    # Safely convert datetime object to a string format so JSON can serialize it
    if entry_dict.get("timestamp"):
        entry_dict["timestamp"] = entry_dict["timestamp"].isoformat()

    invalid_logger.info(json.dumps(entry_dict))


def log_statistics(
    invalid_count: int, valid_count: int, total_sum: float, log_dir: Path = LOG_DIR
):
    """Logs the final execution statistics summarizing the pipeline run."""
    stats_logger = _setup_logger("statistics", "statistics.log", log_dir)

    stats = {
        "invalid_entries": invalid_count,
        "valid_entries": valid_count,
        "total_sum_of_valid_entries": round(total_sum, 2),
    }
    stats_logger.info(f"Pipeline Execution Stats: {json.dumps(stats)}")


def log_unsupported_file_extension(filepath: Path, log_dir: Path = LOG_DIR):
    """Logs files ignored by the parser during directory discovery."""
    invalid_logger = _setup_logger("invalid_entries", "invalid_entries.log", log_dir)
    invalid_logger.info(f"Unsupported file extension: {filepath.suffix}")
