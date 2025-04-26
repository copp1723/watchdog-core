# Contributing to Watchdog Core

Thank you for your interest in contributing to Watchdog Core! This document outlines some key guidelines that all contributors should follow to maintain code quality and consistency.

## Project Rules

### 1. Type Annotations and Strict Type Checking

All new packages imported in the `api/` directory must:
- Be fully type-annotated
- Pass `mypy --strict` validation

This ensures type safety and improves code readability and maintainability. Type annotations serve as both documentation and runtime validation support.

Example:
```python
# Good - with proper type annotations
from typing import List, Dict, Optional

def process_data(input_data: List[Dict[str, str]]) -> Optional[str]:
    # Implementation
    pass
```

### 2. External Service References

Every external service (S3, Supabase, LLM APIs, databases, etc.) must be referenced **only** through an interface in the `/interfaces` directory—never directly in feature code.

This pattern:
- Decouples business logic from external dependencies
- Makes testing easier through mocking
- Allows for swapping implementations without changing feature code

### 3. Conventional Commits

Use [Conventional Commits](https://www.conventionalcommits.org/) format (`feat:`, `fix:`, `chore:`, etc.) for all commit messages.

Examples:
- `feat: add user authentication endpoint`
- `fix: correct validation in sales data parser`
- `chore: update CI dependencies`
- `docs: clarify API usage in README`
- `refactor: simplify data transformation logic`
- `test: add coverage for edge cases in parsing module`

This format ensures auto-changelog tools work correctly and makes the commit history more useful and navigable.

## Development Workflow

1. Create a branch for your feature or fix
2. Make changes following the rules above
3. Run all tests and linting locally before submitting
4. Submit a pull request with a clear description of changes
5. Address any feedback from code reviews

Thank you for helping make Watchdog Core better!

