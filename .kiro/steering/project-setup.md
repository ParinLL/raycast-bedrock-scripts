---
inclusion: always
---

# Project Setup and Development Guidelines

## Package Manager: PDM

This project uses **PDM (Python Development Master)** for dependency management and virtual environment handling.

### Why PDM?

- Modern Python package manager following PEP 582 and PEP 621
- Faster dependency resolution than pip
- Automatic virtual environment management
- Lock file for reproducible builds
- Better dependency isolation

### Common PDM Commands

```bash
# Install all dependencies
pdm install

# Add a new dependency
pdm add package-name

# Add a development dependency
pdm add -d package-name

# Update dependencies
pdm update

# Run a script in the PDM environment
pdm run python source/script.py

# Run tests
pdm run python source/test_cli.py

# Show installed packages
pdm list

# Activate virtual environment
eval $(pdm venv activate)
```

## Project Structure

```
.
├── source/                 # All Python source code
│   ├── base_cli.py        # Shared CLI framework (DRY principle)
│   ├── config_manager.py  # Configuration management
│   ├── constants.py       # Shared constants
│   ├── test_cli.py        # Test suite
│   └── *.py               # Individual CLI tools
├── pyproject.toml         # PDM project configuration
├── pdm.lock              # Dependency lock file
└── *.sh                  # Shell script wrappers
```

## Development Workflow

### Running Scripts

Always use `pdm run` to ensure scripts run in the correct environment:

```bash
pdm run python source/ask-me-anything.py "Your question"
```

### Testing

Run tests before committing changes:

```bash
pdm run python source/test_cli.py
```

### Adding New CLI Tools

When creating a new CLI tool:

1. Import `run_cli` from `base_cli.py`
2. Define a `prompt_builder` function (lambda or regular function)
3. Call `run_cli()` with description, prompt_builder, and success_msg
4. Keep it minimal - all common logic is in `base_cli.py`

Example:
```python
from base_cli import run_cli

def main():
    run_cli(
        description="Your tool description",
        prompt_builder=lambda text: f"Your prompt: {text}",
        success_msg="Output saved to {}"
    )

if __name__ == "__main__":
    main()
```

## Code Style

- Follow DRY (Don't Repeat Yourself) principle
- Use type hints where appropriate
- Keep functions focused and single-purpose
- Document complex logic with comments
- Use descriptive variable names

## AWS Configuration

Scripts require AWS credentials with Bedrock access:

```bash
# Configure AWS CLI
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=ap-northeast-1
```

## Important Notes

- Python 3.12 is required (specified in pyproject.toml)
- All scripts use streaming output for real-time responses
- Input files must be UTF-8 encoded
- Model ID defaults to Claude Sonnet 4.6 in ap-northeast-1 region
- Using Bedrock services incurs AWS costs
