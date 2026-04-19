from datetime import datetime
from arturic.models.entry import Entry
from arturic.entry_validator.validators import validate_department, is_valid_in_timeframe
from arturic.entry_validator.enums import Department


def test_validate_department():
    # Test a valid department ("MDR")
    valid_entry = Entry(
        session_id="MDR-0001",
        processor="Nora.K",
        department="MDR",
        timestamp=datetime(2025, 11, 5, 11, 14, 0),
        ref="AX-A002",
        bin="AX",
        value=372.93,
        category="alpha",
    )
    
    assert validate_department(valid_entry) is True

    # Test an invalid department ("XYZ")
    invalid_entry = Entry(
        session_id="MDR-0001",
        processor="Nora.K",
        department="XYZ", # Intentionally invalid
        timestamp=datetime(2025, 11, 5, 11, 14, 0),
        ref="AX-A002",
        bin="AX",
        value=372.93,
        category="alpha",
    )
    
    assert validate_department(invalid_entry) is False


def test_is_valid_in_timeframe():
    start_period = datetime(2025, 10, 1)
    end_period = datetime(2025, 12, 31, 23, 59, 59)

    # Test an entirely valid entry within timeframe constraints
    perfect_entry = Entry(
        session_id="MDR-0001",
        processor="Nora.K",
        department="MDR",
        timestamp=datetime(2025, 11, 5, 11, 14, 0),
        ref="AX-A002",
        bin="AX",
        value=372.93,
        category="alpha",
    )
    assert is_valid_in_timeframe(perfect_entry, start_period, end_period) is True

    # Test an entry valid in enums, but timestamp is strictly outside the boundaries
    out_of_bounds_entry = Entry(
        session_id="MDR-0001",
        processor="Nora.K",
        department="MDR",
        timestamp=datetime(2026, 1, 5, 11, 14, 0), # 2026
        ref="AX-A002",
        bin="AX",
        value=372.93,
        category="alpha",
    )
    assert is_valid_in_timeframe(out_of_bounds_entry, start_period, end_period) is False
    
    # Test an entry within bounds, but containing a broken enum (invalid category)
    invalid_category_entry = Entry(
        session_id="MDR-0001",
        processor="Nora.K",
        department="MDR",
        timestamp=datetime(2025, 11, 5, 11, 14, 0),
        ref="AX-A002",
        bin="AX",
        value=372.93,
        category="XYZ", # Invalid Enum
    )
    assert is_valid_in_timeframe(invalid_category_entry, start_period, end_period) is False
