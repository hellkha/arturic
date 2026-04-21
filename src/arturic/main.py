from arturic.config.constants import DATA_DIR
from arturic.pipeline.pipeline import run_pipeline
from arturic.utils.logger import log_statistics
from datetime import datetime


def main():
    data_dir = DATA_DIR
    print(f"Scanning target directory: {data_dir.name}/ ...")

    # Define target processing window (Q4 2025)
    start_period = datetime(2025, 10, 1)
    end_period = datetime(2025, 12, 31, 23, 59, 59)
    print(f"Processing entries between {start_period} and {end_period} ...")

    # Handoff to the processing pipeline
    results = run_pipeline(data_dir, start_period, end_period)

    # Log statistics, including the sum result
    log_statistics(results.invalid_entries, results.valid_entries, results.total_value)

    # Terminal UI
    print(f"\n- Successfully scanned {results.total_loaded} Total Entry objects! -")
    print(f"- Valid Entries: {results.valid_entries} -")
    print(f"- Invalid Entries: {results.invalid_entries} -")
    print(f"- Total Value of Valid Entries: {results.total_value} -")


if __name__ == "__main__":
    main()
