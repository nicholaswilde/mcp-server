# Project Overview

This is a Python project designed to serve as an MCP (Multi-Cloud Platform) server. It utilizes FastAPI for the web framework and Uvicorn as the ASGI server. The project also includes an `agents-library` for managing agent-related rules and prompts.

## Technologies Used

*   **Python**
*   **FastAPI**: Web framework for building APIs.
*   **Uvicorn**: ASGI server.
*   **mcp**: Multi-Cloud Platform SDK.

## Project Structure

*   `Dockerfile`: Used for containerizing the application.
*   `requirements.txt`: Lists Python dependencies, generated from `requirements.in` by `pip-compile`.
*   `requirements.in`: Defines direct Python dependencies for the project.
*   `app/`: Contains the core application logic.
    *   `server.py`: The main FastAPI application server.
*   `agents-library/`: Stores agent-related rules and prompts, categorized by type.
    *   `bash/`: Contains bash scripts used by agents.
    *   `markdown/`: Contains markdown files with agent instructions and prompts.
*   `.github/`: Contains GitHub Actions workflow definitions and other repository configurations.
*   `tests/`: Contains unit and integration tests for the application.
    *   `test_server.py`: Tests for the main FastAPI server.
*   `docs/`: Contains project documentation.
    *   `contributing.md`: Guidelines for contributing to the project.
*   `Taskfile.yml`: Defines various development tasks using Task (e.g., linting, testing, running the server).

## Building and Running

To set up and run this project, follow these steps:

1.  **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Server:**
    ```bash
    uvicorn app.server:app --host 0.0.0.0 --port 8080
    ```

4.  **Run Linting and Formatting Checks:**
    ```bash
    task lint
    ```

5.  **Run Tests:**
    ```bash
    task test
    ```

## Development Conventions

*   **Virtual Environments**: Always use a virtual environment for dependency management.
*   **Dependencies**: All Python dependencies should be listed in `requirements.txt`.
*   **Git Commit Messages**: When creating commit messages using `git commit -m`, avoid using command substitution (e.g., `$(...)`, `<(...)`, `>(...)`) as it is not allowed for security reasons in some environments. Provide the commit message directly as a string.
*   **Git Tags**: When creating git tags, always use an annotated tag with a message using the `-a` and `-m` flags (e.g., `git tag -a v1.0.0 -m "Release v1.0.0"`). This prevents the command from attempting to open an editor in non-interactive environments, which can cause issues in automated scripts.
*   **Commit Approval**: All proposed git commits must be reviewed and approved by a maintainer before being committed.
*   **Plan Approval**: Before implementing any significant changes or features, a detailed plan of action must be outlined and approved by a maintainer.