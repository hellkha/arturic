# Arturic - Sum of valid Entries

This is a tool for managing data entries. It sums the values of valid entries within the Q4 2025 timeframe (October 1st, 2025 to December 31st, 2025) across all departments.

## Requirements

- Python 3.10+

## Installation and Usage

### Option 1: pip + venv

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/hellkha/arturic.git
    cd arturic
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install .
    ```

4. **Run the project**:
    ```bash
    python src/arturic/main.py
    ```

### Option 2: uv

1. **Install uv** (if you don't have it):
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd arturic
    ```

3. **Run the project**:
    ```bash
    uv run arturic
    # or
    uv run python src/arturic/main.py
    ```

### Files location

- Source data directory: `"arturic(root)/data/"`
- Logs directory: `"arturic(root)/logs/"`
- Results are printed to console and logged under `"arturic(root)/logs/statistics.log"`


## Project Structure

```
arturic/
├── data/                       # Source data directory
├── logs/                       # Logs directory
├── src/
│   ├── arturic/
│   │   ├── config/             # Configuration files
│   │   ├── pipeline/           # Data processing logic, orquestrates the pipeline
│   │   ├── entry_validator/    # Validation rules and models
│   │   ├── file_finder/        # Searches data files in data directory
│   │   ├── file_reader/        # Transform content of data files to Entry objects
│   │   ├── models/             # Data models
│   │   ├── utils/              # Logging and helpers
│   |   └── main.py             # Main entry point
├── tests/                      # Unit tests
├── README.md                   # Project documentation
└── pyproject.toml              # Project dependencies
```

## Development

### Running Tests

To run the test suite:

```bash
pytest
```

---

## For more information (root/docs/)

### Details in [documentation.md](docs/documentation.md) 

### Explanation of methodology and anomalies in [explanation.md](docs/explanation.md)