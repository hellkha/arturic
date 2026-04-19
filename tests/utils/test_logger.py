from arturic.utils.logger import log_statistics

def test_log_statistics(tmp_path):
    log_path = (tmp_path / "logs")

    # Log dummy data
    log_statistics(
        invalid_count=0,
        valid_count=100,
        total_sum=500.5,
        log_dir=log_path
    )
    
    # Assert that the engine generated the log file on disk
    file_path = (log_path / "statistics.log")
    assert file_path.exists()
