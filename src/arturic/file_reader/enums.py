from enum import Enum


class FileType(str, Enum):
    """Supported file extensions for parsing."""

    MDR = ".mdr"
    CSV = ".csv"
    TXT = ".txt"


class MDRField(str, Enum):
    SESSION_ID = "session_id"
    PROCESSOR = "processor"
    DEPARTMENT = "department"
    TIMESTAMP = "timestamp"
    ENTRIES = "entries"
    REF = "ref"
    BIN = "bin"
    VALUE = "value"
    CATEGORY = "category"


class CSVField(str, Enum):
    SESSION_ID = "session_id"
    PROCESSOR = "processor"
    DEPARTMENT = "department"
    TIMESTAMP = "timestamp"
    REF = "ref"
    BIN = "bin"
    OUTPUT_METRIC = "output_metric"
    CLASSIFICATION = "classification"


class TXTField(str, Enum):
    SESSION = "SESSION"
    PROCESSOR = "PROCESSOR"
    DEPARTMENT = "DEPARTMENT"
    TIMESTAMP = "TIMESTAMP"
    REF = "REF"
    BIN = "BIN"
    READING = "READING"
    TYPE = "TYPE"
