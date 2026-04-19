# Arturic Pipeline - Project Documentation

## TL;DR

**Arturic** is a modular Python data-processing pipeline. It scans directories for multi-format datasets (`.csv`, `.txt`, `.mdr`), parses and normalizes them into strict Python DataClasses (`Entry`), validates them against domain constraints and temporal windows, aggregates the valid financial metrics, and dumps logs and invalidation errors to the `logs` directory.

---

**For running the project check [README.md](../README.md)**

---

## Detailed Overview

### Pipeline Flow

The core logic runs in **`src/arturic/data_processor/processor.py`**. When `run_pipeline(data_dir, start, end)` is triggered:

1. **Discovery**: `get_valid_file_paths()` finds all supported `.mdr, (holds JSON format text)`, `.csv`, and `.txt` files in the target directory.
2. **Reading**: The `file_reader` parses each file based on its format (JSON, CSV, or TXT) into a standard `Entry` dataclass.
3. **Validation**: Each `Entry` is checked against temporal constraints (e.g., in Q4 2025) and domain bounds to prevent malformed data leaks (e.g., missing values and invalid values). 
4. **Aggregation**: Valid entries are accumulated in a list and summed up in the pipeline loop. Invalid entries are logged to `logs/invalid_entries.log`.
5. **Output**: A `PipelineResult` payload is returned containing the total scanned, valid, invalid, and summed metric values.

### Module Breakdown (Docstrings)

- **`arturic.file_finder`**
  - *Returns paths to valid data files within a directory.*
- **`arturic.file_reader`**
  - *Provides parsing functions (`_read_mdr`, `_read_csv`, `_read_txt`) to convert files into `Entry` objects.*
- **`arturic.entry_validator`**
  - *Contains `is_valid_in_timeframe(entry, start, end)` to check both temporal and IEEE float domain bounds.*
- **`arturic.pipeline`**
  - *Executes the main pipeline handling file loading, validation streams, and metric aggregation.*
- **`arturic.models`**
  - *Defines the strictly-typed `Entry` and `PipelineResult` dataclasses.
- **`arturic.utils`**
  - *Contains logger, an utility function for the pipeline.*
- **`arturic.config`**
  - *Contains the configuration for the pipeline (e.g. directories to find data and save logs.)*

## How to Run

Check [README.md](../README.md)

### Logging Outputs

- `logs/statistics.log` - Metrics for the run.
- `logs/invalid_entries.log` - Rejection reasons and data for all invalid entries.

### Test Suite

To run the integration and unit tests:

```bash
pytest          # For pip + venv
uv run pytest   # For uv
```
