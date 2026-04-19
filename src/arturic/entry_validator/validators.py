import math
from datetime import datetime
from arturic.models.entry import Entry
from .enums import Department, Processor, Bin, Category

_VALID_DEPARTMENTS = {e.value for e in Department}
_VALID_PROCESSORS = {e.value for e in Processor}
_VALID_BINS = {e.value for e in Bin}
_VALID_CATEGORIES = {e.value for e in Category}


def validate_department(entry: Entry) -> bool:
    """Validates if the entry's department exists in the Department Enum."""
    return entry.department in _VALID_DEPARTMENTS


def validate_processor(entry: Entry) -> bool:
    """Validates if the entry's processor exists in the Processor Enum."""
    return entry.processor in _VALID_PROCESSORS


def validate_bin(entry: Entry) -> bool:
    """Validates if the entry's bin exists in the Bin Enum."""
    return entry.bin in _VALID_BINS


def validate_category(entry: Entry) -> bool:
    """Validates if the entry's category exists in the Category Enum."""
    return entry.category in _VALID_CATEGORIES


def validate_value(entry: Entry) -> bool:
    """Validates if the entry's value is higher than 0, not NaN, not None, not infinity"""
    if entry.value is None:
        return False
    return entry.value > 0 and math.isfinite(entry.value)


def validate_timestamp(entry: Entry, start_date: datetime, end_date: datetime) -> bool:
    """Validates if the entry's timestamp is within the given date range."""
    return start_date <= entry.timestamp <= end_date


def is_valid_in_timeframe(
    entry: Entry, start_date: datetime, end_date: datetime
) -> bool:
    """Returns True if the entry has valid enum properties, positive value, and falls within the period."""
    return (
        validate_department(entry)
        and validate_processor(entry)
        and validate_bin(entry)
        and validate_category(entry)
        and validate_value(entry)
        and validate_timestamp(entry, start_date, end_date)
    )
