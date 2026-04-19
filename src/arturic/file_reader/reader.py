"""
Module for functions that read files of different extensions.
"""

from arturic.utils.logger import log_unsupported_file_extension
import json
import csv
from pathlib import Path
from datetime import datetime
from arturic.models.entry import Entry
from .enums import FileType, MDRField, CSVField, TXTField


def read_file(filepath: Path | str) -> list[Entry]:
    """Reads a file and returns a list of flattened Entry objects."""
    filepath = Path(filepath)

    if filepath.suffix == FileType.MDR:
        return _read_mdr(filepath)
    elif filepath.suffix == FileType.CSV:
        return _read_csv(filepath)
    elif filepath.suffix == FileType.TXT:
        return _read_txt(filepath)
    else:
        log_unsupported_file_extension(filepath)


def _read_mdr(filepath: Path | str) -> list[Entry]:
    """Reads a .mdr file and returns a list of flattened Entry objects."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    session_id = data.get(MDRField.SESSION_ID, "")
    processor = data.get(MDRField.PROCESSOR, "")
    department = data.get(MDRField.DEPARTMENT, "")
    timestamp_raw = data.get(MDRField.TIMESTAMP, "")
    timestamp = datetime.fromisoformat(timestamp_raw) if timestamp_raw else None

    entries_list = []
    for item in data.get(MDRField.ENTRIES, []):
        entries_list.append(
            Entry(
                session_id=session_id,
                processor=processor,
                department=department,
                timestamp=timestamp,
                ref=item.get(MDRField.REF, ""),
                bin=item.get(MDRField.BIN, ""),
                value=float(item.get(MDRField.VALUE, 0.0)),
                category=item.get(MDRField.CATEGORY, ""),
            )
        )

    return entries_list


def _read_csv(filepath: Path | str) -> list[Entry]:
    """Reads a CSV file and maps it to a list of Entry objects."""
    entries_list = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entries_list.append(
                Entry(
                    session_id=row.get(CSVField.SESSION_ID, ""),
                    processor=row.get(CSVField.PROCESSOR, ""),
                    department=row.get(CSVField.DEPARTMENT, ""),
                    timestamp=datetime.fromisoformat(row.get(CSVField.TIMESTAMP, "")),
                    ref=row.get(CSVField.REF, ""),
                    bin=row.get(CSVField.BIN, ""),
                    value=float(row.get(CSVField.OUTPUT_METRIC, 0.0)),
                    category=row.get(CSVField.CLASSIFICATION, ""),
                )
            )

    return entries_list


def _read_txt(filepath: Path | str) -> list[Entry]:
    """Reads a custom formatted TXT file and maps it to a list of Entry objects."""
    entries_list = []
    metadata = {}

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    parsing_metadata = True
    for line in lines:
        if line.strip() == "---":
            parsing_metadata = False
            continue

        if parsing_metadata:
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip()
        else:
            if not line.strip():
                continue

            # Parse record: REF: AX-F069 | BIN: AX | READING: 64.39 | TYPE: beta
            record = {}
            parts = line.split("|")
            for part in parts:
                if ":" in part:
                    k, v = part.split(":", 1)
                    record[k.strip()] = v.strip()

            if record:
                entries_list.append(
                    Entry(
                        session_id=metadata.get(TXTField.SESSION, ""),
                        processor=metadata.get(TXTField.PROCESSOR, ""),
                        department=metadata.get(TXTField.DEPARTMENT, ""),
                        timestamp=datetime.fromisoformat(
                            metadata.get(TXTField.TIMESTAMP, "")
                        ),
                        ref=record.get(TXTField.REF, ""),
                        bin=record.get(TXTField.BIN, ""),
                        value=float(record.get(TXTField.READING, 0.0)),
                        category=record.get(TXTField.TYPE, ""),
                    )
                )

    return entries_list
