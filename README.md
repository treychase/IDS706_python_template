# IDS706_python_template

[![CI](https://github.com/treychase/IDS706_python_template/actions/workflows/main.yml/badge.svg)](https://github.com/treychase/IDS706_python_template/actions/workflows/main.yml)

## Description

A Python template project for IDS 706 with automated testing, linting, and continuous integration.

## hello.py

This template includes two utility functions:

- **`introduce_me(name: str)`** - A friendly introduction function for new classmates
- **`abs_diff(a: int, b: int)`** - Calculate the absolute difference between two integers

## Project Structure

```
.
├── hello.py           # Main module with utility functions
├── test_hello.py      # Test cases for hello.py functions
├── requirements.txt   # Project dependencies
├── README.md         # This file
└── .github/
    └── workflows/
        └── main.yml  # GitHub Actions CI workflow
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/treychase/IDS706_python_template.git
   cd IDS706_python_template
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Introduction Function
```python
from hello import introduce_me

# Introduce yourself to a classmate
message = introduce_me("Katie")
print(message)  # "Hello, Katie, my name is Trey, your new classmate!"
```

### Absolute Difference Function
```python
from hello import abs_diff

# Calculate absolute difference
result = abs_diff(10, 3)
print(result)  # 7

# Works with negative numbers too
result = abs_diff(-5, 4)
print(result)  # 9
```

## Development

### Running Tests
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=hello
```

### Code Quality
```bash
# Lint with flake8
flake8 hello.py

# Format with black
black hello.py

# Lint with pylint
pylint hello.py
```

## CI/CD

This project uses GitHub Actions for continuous integration. The workflow automatically:
- Sets up Python 3.11
- Installs dependencies
- Runs linting with flake8
- Executes tests with pytest and generates coverage reports

## Dependencies

- **pytest** - Testing framework
- **pytest-cov** - Coverage reporting
- **flake8** - Code linting
- **black** - Code formatting
- **pylint** - Code analysis
- **click** - Command line interface creation



