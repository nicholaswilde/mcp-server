# :material-handshake: Contributing to MCP Server

We welcome contributions to the MCP Server project! By contributing, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

Please take a moment to review this document to ensure a smooth and effective contribution process.

## :material-lightbulb-on: How to Contribute

### :material-bug: Reporting Bugs

If you find a bug, please help us by reporting it. A good bug report makes it easier for us to track and fix the issue. Please include:

*   A clear and concise title.
*   A detailed description of the bug.
*   Steps to reproduce the behavior.
*   Expected versus actual behavior.
*   Any relevant logs or error messages.

### :material-star-four-points: Suggesting Enhancements

We love new ideas! If you have a suggestion for an enhancement or a new feature, please open an issue and describe it in detail. Include:

*   A clear and concise title.
*   A detailed description of the proposed enhancement.
*   Any mockups or examples that help illustrate your idea.

### :material-source-pull: Pull Requests

1.  **Fork the Repository:** Start by forking the `mcp-server` repository to your GitHub account.
2.  **Clone Your Fork:** Clone your forked repository to your local machine.
    ```bash
    git clone https://github.com/YOUR_USERNAME/mcp-server.git
    cd mcp-server
    ```
3.  **Create a New Branch:** Create a new branch for your feature or bug fix. Use a descriptive name.
    ```bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/your-bug-fix-name
    ```
4.  **Set up Your Development Environment:**
    Ensure you have Python 3.11+ and Docker installed.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install pip-tools
    pip-compile requirements.in
    pip-sync
    ```
5.  **Set up Pre-Commit Hooks:**
    This repository uses `pre-commit` to automatically run linters and formatters before each commit.
    ```bash
    pre-commit install
    ```
6.  **Make Your Changes:**
    Implement your feature or bug fix. Remember to:
    *   Adhere to existing code style and conventions.
    *   Write clear, concise, and well-documented code.
    *   Add or update tests for your changes.
    *   Ensure all existing tests pass.

7.  **Run Tests:**
    Before committing, ensure all tests pass.
    ```bash
    task test
    ```
8.  **Commit Your Changes:**
    When you commit, the pre-commit hooks will automatically run and may fix formatting issues. If they fail, you'll need to stage the changes and commit again.
    ```bash
    git add .
    git commit -m "feat: Your descriptive commit message"
    ```
9.  **Push to Your Fork:**
    ```bash
    git push origin feature/your-feature-name
    ```
10. **Create a Pull Request:**
    Go to the original `mcp-server` repository on GitHub and create a new pull request from your forked branch.
    *   Provide a clear title and description for your pull request.
    *   Reference any related issues.

## :material-format-paint: Code Style and Conventions

*   **Python:** Follow PEP 8 guidelines. We use `ruff` for linting and `black` for formatting.
*   **Docstrings:** Use Google-style docstrings for all functions, classes, and modules.
*   **Type Hinting:** Use type hints for all function arguments and return values where appropriate.

## :material-book-open-variant: Documentation Style

All documentation is written in Markdown and generated using MkDocs with the Material theme. Please ensure:

*   Clear and descriptive headings.
*   Use admonitions for important information (e.g., `!!! note`, `!!! warning`).
*   Specify the language for code blocks (e.g., ````python`, ````bash`).
*   Add new pages to the `nav` section of `mkdocs.yml` if you create new documentation files.

## :material-git: Git Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for commit messages. This helps with automated changelog generation and understanding the nature of changes.

**Examples:**
*   `feat: Add user authentication module`
*   `fix: Correct off-by-one error in pagination`
*   `docs: Update README with installation instructions`
*   `chore: Update dependencies`

## :material-tag: Versioning

The project version is managed through Git tags. When creating a release, an annotated tag (e.g., `v1.0.0`) should be used.

## :material-license: License

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

## :material-help-circle: Need Help?

If you have any questions or need assistance, feel free to open an issue or reach out to the maintainers.

Thank you for contributing!
