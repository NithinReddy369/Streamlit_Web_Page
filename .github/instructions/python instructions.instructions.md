---
applyTo: '**/*.py'
---

# Python Project Guidelines

## Code Structure and Organization
1. Use modular programming approach:
    - Separate code into logical modules/packages
    - Each module should have a single responsibility
    - Create separate files for different functionalities

## Coding Standards
1. Follow PEP 8 style guide:
    - Use 4 spaces for indentation
    - Maximum line length of 79 characters
    - Use descriptive variable and function names
    - Use snake_case for functions and variables
    - Use PascalCase for class names

2. Documentation:
    - Include docstrings for modules, classes, and functions
    - Use type hints for function parameters and return values
    - Add meaningful comments for complex logic

3. Best Practices:
    - Write DRY (Don't Repeat Yourself) code
    - Use list comprehensions when appropriate
    - Implement proper error handling with try/except
    - Use context managers (with statements) for file operations
    - Write unit tests for critical functions

4. Project Structure:
    - Use requirements.txt or setup.py for dependencies
    - Include README.md with project documentation
    - Organize imports in order: standard library, third-party, local

5. Performance:
    - Use appropriate data structures
    - Optimize resource-intensive operations
    - Consider memory usage in large data operations