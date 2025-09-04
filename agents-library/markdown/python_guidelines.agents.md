# :material-language-python: Python Scripting Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying python scripts. My goal is to produce scripts that are not only effective but also clear, robust, and maintainable.

## :material-code-tags: General Coding Practices

- Avoid using "magic numbers" or hardcoded literal values directly in the code. Instead, define them as named constants with clear, descriptive names. This improves readability and maintainability.

### 1. Shebang

- Every script must begin with a shebang to ensure it's executed with the correct interpreter.
- I will use `#!/usr/bin/env python3` for portability.

### 2. Error Handling

- I will use `try`/`except` blocks to handle potential errors gracefully.
- I will log errors to stderr.
- When re-raising exceptions within an `except` clause, I will use `raise ... from err` or `raise ... from None` to preserve the original traceback and clarify the cause of the error.

### 3. Variable Handling

- I will use snake_case for variable names.
- I will use type hints to improve readability and allow for static analysis.

### 4. Command Usage

- I will use the `subprocess` module to run external commands.
- I will use f-strings for string formatting.

### 5. Functions

- I will use functions to group related code.
- I will use docstrings to explain what a function does.

### 6. Script Structure

- I will use a `main` function to encapsulate the main logic of the script.
- I will use comments to explain complex parts of the script.
- I will use a consistent and readable style that is PEP 8 compliant.
- All lines of code will adhere to a maximum length of 120 characters, as configured in `pyproject.toml`.

### 7. Linting and Testing

- **Linting:** I will use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting. The configuration is defined in `pyproject.toml`. I will run `task lint` or `task ruff` to perform checks and apply fixes.
- **Testing:** I will use [Pytest](https://docs.pytest.org/en/stable/) for unit and integration testing. Tests are located in the `tests/` directory. I will run `task test` to execute tests.
- **Automated Checks:** I will use `pre-commit` hooks to automatically run linting and formatting checks before committing code.

### 8. Security

- I will be cautious about using `eval`.
- I will not store sensitive information in scripts.
- I will use `bandit` to lint my scripts and identify potential security issues.

### 9. Commented Header

- Every Python script must start with a commented header in the following format. The values should be automatically populated based on the script's purpose.

```
#!/usr/bin/env python3
################################################################################
#
# Script Name: <script_name>.py
# ----------------
# <A description of the script's purpose>
#
# @author Nicholas Wilde, 0xb299a622
# @date <Current Date in DD MM YYYY format>
# @version <Version in semver format>
#
################################################################################
```

By following these guidelines, I will create python scripts that are reliable, easy to understand, and secure.
