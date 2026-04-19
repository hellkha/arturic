from datetime import datetime
from arturic.models.entry import Entry
import pytest
from arturic.file_reader.reader import read_file

def test_read_file_mdr(tmp_path):
    # Create file
    file_path = tmp_path / "data.mdr"
    file_path.touch()
    
    # Write content to file
    with open(file_path, "w") as f:
        f.write("""
        {
            "session_id": "MDR-0001",
            "processor": "Nora.K",
            "department": "MDR",
            "timestamp": "2025-11-05T11:14:00",
            "entries": 
            [
                {
                    "ref": "AX-A002",
                    "bin": "AX",
                    "value": 372.93,
                    "category": "alpha"
                },
                {
                    "ref": "AX-A003",
                    "bin": "AX",
                    "value": 216.74,
                    "category": "alpha"
                }
            ]
        }
        """)

    contents = read_file(file_path)

    # Create entry objects that should be result of the mocked file
    entry_1 = Entry(
            session_id="MDR-0001",
            processor="Nora.K",
            department="MDR",
            timestamp=datetime.fromisoformat("2025-11-05T11:14:00"),
            ref="AX-A002",
            bin="AX",
            value=372.93,
            category="alpha",
        )
    
    entry_2 = Entry(
            session_id="MDR-0001",
            processor="Nora.K",
            department="MDR",
            timestamp=datetime.fromisoformat("2025-11-05T11:14:00"),
            ref="AX-A003",
            bin="AX",
            value=216.74,
            category="alpha",
        )
    
    entries = [entry_1, entry_2]

    # Compare generated objects with expected objects
    assert contents == entries