# Lab0 - Fundamentals of Continuous Integration

**GitHub repository:** [https://github.com/InakiGarin/Lab0](https://github.com/InakiGarin/Lab0)

## Overview

This project implements a collection of data preprocessing functions and a command-line interface (CLI) using Python and Click.

The main objective is to practice software development fundamentals, including project organization, dependency management, code quality, unit testing, integration testing, and test coverage.

## Features

The preprocessing functions are organized into four categories:

### 1. Clean
- Remove missing values.
- Fill missing values with a specified value.
- Remove duplicate values.

### 2. Numeric
- Normalize values using Min-Max scaling.
- Standardize values using Z-score.
- Clip values within a specified range.
- Convert strings to integers.
- Apply logarithmic transformation to positive values.

### 3. Text
- Tokenize text into lowercase alphanumeric words.
- Remove punctuation.
- Remove stop words.

### 4. Struct
- Flatten lists of lists.
- Shuffle elements using an optional random seed.
- Extract unique values.

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for Python environment and dependency management.

Clone the repository:

```bash
git clone https://github.com/InakiGarin/Lab0.git
cd Lab0
```

Install the dependencies and synchronize the environment:

```bash
uv sync
```

## Usage

The application provides a command-line interface organized into four command groups: `clean`, `numeric`, `text`, and `struct`.

To display the available commands:

```bash
uv run python -m src.cli --help
```

To display the commands available within a group:

```bash
uv run python -m src.cli numeric --help
```

### Examples

**Clean:**

```bash
uv run python -m src.cli clean remove-missing-values "[1, None, 2]"
uv run python -m src.cli clean fill-missing-values "[1, None, 2]" --fill-value 0
```

**Numeric:**

```bash
uv run python -m src.cli numeric normalize "[1, 2, 3]"
uv run python -m src.cli numeric standardize "[1, 2, 3]"
uv run python -m src.cli numeric clip "[1, 5, 10]" --min-value 2 --max-value 8
uv run python -m src.cli numeric convert-to-integers "['1', '2', 'hello']"
uv run python -m src.cli numeric log-transform "[1, 2, 3]"
```

**Text:**

```bash
uv run python -m src.cli text tokenize "Hello World!"
uv run python -m src.cli text remove-punctuation "Hello, World!"
uv run python -m src.cli text remove-stop-words "This is a test" --stop-words "is a"
```

**Struct:**

```bash
uv run python -m src.cli struct shuffle "[1, 2, 3, 4]" --seed 42
uv run python -m src.cli struct flatten "[[1, 2], [3, 4]]"
uv run python -m src.cli struct unique-values "[1, 2, 2, 3]"
```

## Testing

The project includes unit tests for the preprocessing functions and integration tests for the CLI.

Run all tests:

```bash
uv run python -m pytest -v
```

Run tests with coverage:

```bash
uv run python -m pytest -v --cov=src
```

To display the lines not covered by tests:

```bash
uv run python -m pytest --cov=src --cov-report=term-missing
```

## Code Quality

The project uses Black for code formatting and Pylint for static code analysis.

Format the source files:

```bash
uv run black src/*.py
```

Format the test files:

```bash
uv run black tests/*.py
```

Run Pylint:

```bash
uv run python -m pylint src/*.py
```

## Project Structure

```text
Lab0/
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   └── cli.py
├── tests/
│   ├── __init__.py
│   ├── test_logic.py
│   └── test_cli.py
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Technologies

- Python 3.13
- uv
- Click
- Pytest
- pytest-cov
- Black
- Pylint