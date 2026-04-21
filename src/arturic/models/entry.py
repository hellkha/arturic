from dataclasses import dataclass
from datetime import datetime


@dataclass
class Entry:
    """
    Represents a flattened data entry, combining both the common file
    metadata (like session_id) and the individual record data.
    """

    session_id: str
    processor: str
    department: str
    timestamp: datetime
    ref: str
    bin: str
    value: float | None
    category: str
