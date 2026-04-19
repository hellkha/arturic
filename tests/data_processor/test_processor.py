from datetime import datetime
from arturic.pipeline.pipeline import run_pipeline

def test_run_pipeline_simple(tmp_path):
    """
    Simulates the orchestrator mapping end-to-end natively by dropping a tiny synthetic.mdr
    file inside the ephemeral temporary directory and explicitly verifying the PipelineResult numbers.
    """
    
    # Create mock MDR file
    test_file = tmp_path / "mock_data.mdr"
    
    # Mock MDR file
    test_file.write_text("""
    {
        "session_id": "MDR-0001",
        "processor": "Nora.K",
        "department": "MDR",
        "timestamp": "2025-11-15T12:00:00",
        "entries": [
            {
                "ref": "AX-A002",
                "bin": "AX",
                "value": 250.75,
                "category": "alpha"
            }
        ]
    }
    """)
    
    # Set Q4 2025 windows
    start_period = datetime(2025, 10, 1)
    end_period = datetime(2025, 12, 31, 23, 59, 59)
    
    # Run pipeline
    results = run_pipeline(tmp_path, start_period, end_period)
    
    # Assert the returned PipelineResult exactly mapped the integration values 
    assert results.total_loaded == 1
    assert results.valid_entries == 1
    assert results.invalid_entries == 0
    assert results.total_value == 250.75
