---
inclusion: always
---

# Code Simplification Guidelines

## Recent Refactoring

This project was recently refactored to eliminate code duplication and improve maintainability.

### Before: Duplicated Code

Previously, each CLI script (~150 lines) contained:
- Duplicate argument parsing logic
- Duplicate input loading logic
- Duplicate output saving logic
- Duplicate streaming logic
- Duplicate error handling

### After: Centralized Framework

Now uses `base_cli.py` as a shared framework:
- Each CLI script is now ~15 lines
- All common logic is centralized
- Easier to maintain and test
- Consistent behavior across all tools

### Key Components

#### base_cli.py

Provides:
- `stream_response()` - Handles API streaming
- `load_input()` - Loads from file or argument
- `save_output()` - Saves results to file
- `run_cli()` - Main CLI orchestration

#### Individual CLI Scripts

Each script only needs:
```python
from base_cli import run_cli

def main():
    run_cli(
        description="Tool description",
        prompt_builder=lambda text: f"Prompt template: {text}",
        success_msg="Success message"
    )
```

## Refactoring Principles Applied

1. **DRY (Don't Repeat Yourself)**: Common code extracted to base_cli.py
2. **Single Responsibility**: Each module has one clear purpose
3. **Composition over Inheritance**: Using functions instead of class hierarchies
4. **Minimal Code**: Each script contains only what's unique to it

## When Adding New Features

- Add shared functionality to `base_cli.py`
- Add configuration to `config_manager.py`
- Add constants to `constants.py`
- Keep individual scripts minimal

## Testing Strategy

- Test shared components in `test_cli.py`
- Mock external API calls
- Test file I/O with temporary files
- Verify all modules can be imported
