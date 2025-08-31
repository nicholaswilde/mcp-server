# Project Overview

This is a Python project designed to serve as an MCP (Multi-Cloud Platform) server. It utilizes FastAPI for the web framework and Uvicorn as the ASGI server. The project also includes an `agents-library` for managing agent-related rules and prompts.

## Technologies Used

*   **Python**
*   **FastAPI**: Web framework for building APIs.
*   **Uvicorn**: ASGI server.
*   **mcp**: Multi-Cloud Platform SDK.

## Project Structure

*   `Dockerfile`: Used for containerizing the application.
*   `requirements.txt`: Lists Python dependencies.
*   `app/`:
    *   `server.py`: The main application server.
*   `agents-library/`:
    *   `bash/`: Contains bash scripts.
    *   `markdown/`: Contains markdown agent instruction files.
        *   `common_prompts.agents.md`: Common prompts for agents.
        *   `dev_rules.agents.md`: Development-related agent rules.
        *   `fantasy_football_ai.agents.md`: Git commit and tagging conventions.
        *   `frame_fi.agents.md`: Bash and Python scripting guidelines.
        *   `homelab_docs.agents.md`: Markdown documentation guidelines.
        *   `security_checks.agents.md`: Security-related agent checks.

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

## Development Conventions

*   **Virtual Environments**: Always use a virtual environment for dependency management.
*   **Dependencies**: All Python dependencies should be listed in `requirements.txt`.
*   **Git Commit Messages**: When creating commit messages using `git commit -m`, avoid using command substitution (e.g., `$(...)`, `<(...)`, `>(...)`) as it is not allowed for security reasons. Provide the commit message directly as a string.
*   **Git Tags**: When creating git tags, always use an annotated tag with a message using the `-a` and `-m` flags (e.g., `git tag -a v1.0.0 -m "Release v1.0.0"`). This prevents the command from attempting to open an editor in non-interactive environments.