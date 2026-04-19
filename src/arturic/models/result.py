from dataclasses import dataclass


@dataclass
class PipelineResult:
    total_loaded: int
    valid_entries: int
    invalid_entries: int
    total_value: float
