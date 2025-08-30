# MCP Server

This is a Python project designed to serve as an MCP (Multi-Cloud Platform) server. It utilizes FastAPI for the web framework and Uvicorn as the ASGI server. The project also includes an `agents-library` for managing agent-related rules and prompts.

## :rocket: Technologies Used

*   **Python**
*   **FastAPI**: Web framework for building APIs.
*   **Uvicorn**: ASGI server.
*   **mcp**: Multi-Cloud Platform SDK.

## :open_file_folder: Project Structure

*   `Dockerfile`: Used for containerizing the application.
*   `compose.yaml`: Used for running the application with Docker Compose.
*   `requirements.txt`: Lists Python dependencies.
*   `app/`:
    *   `server.py`: The main application server.
*   `agents-library/`:
    *   `dev_rules.agents.md`: Development-related agent rules.
    *   `security_checks.agents.md`: Security-related agent checks.
    *   `common_prompts.agents.md`: Common prompts for agents.

## :checkered_flag: Getting Started

To get started with this project, you need to have Python 3.10+ and Docker installed on your system.

### Prerequisites

*   Python 3.10+
*   Docker
*   pip

### Installation

1.  **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## :hammer_and_wrench: Building and Running

You can run the server using Docker Compose or directly with Uvicorn.

### Using Docker Compose

To run the server with Docker Compose, use the following command:

```bash
docker compose up
```

### Using Uvicorn

To run the server with Uvicorn, use the following command:

```bash
uvicorn app.server:app --host 0.0.0.0 --port 8080
```

## :scroll: Development Conventions

*   **Virtual Environments**: Always use a virtual environment for dependency management.
*   **Dependencies**: All Python dependencies should be listed in `requirements.txt`.

## :electric_plug: API Endpoints

The following API endpoints are available:

*   `POST /test/call_tool`: Test endpoint for direct tool invocation.
*   `POST /test/read_resource`: Test endpoint for direct resource invocation.

The MCP server also exposes the following tools:

*   `get_agents_instructions`: Retrieves a specific AGENTS.md file for providing AI with instructions and context.
*   `list_agents_instructions`: Lists all available AGENTS.md files.

## :gemini: Adding to gemini-cli

To add this server to `gemini-cli`, you need to edit your `settings.json` file. You can find this file in `~/.gemini/settings.json` (user settings) or in `.gemini/settings.json` (project settings).

Add the following to your `settings.json` file:

```json
{
  "mcpServers": {
    "httpServer": {
      "httpUrl": "http://<ip-address>:8080"
    }
  }
}
```

### Using the `mcp` tool

Once the `mcp-server` is configured in `gemini-cli`, you can use the `mcp` tool to interact with the server. For example, to list all available agent instructions:

```bash
gemini mcp list_agents_instructions
```

To retrieve a specific agent instruction file:

```bash
gemini mcp get_agents_instructions --file_name dev_rules.agents.md
```

See [reference][1].

## :balance_scale: License

This project is licensed under the [Apache License 2.0](./LICENSE).

## :pencil: Author

This project was started in 2025 by [Nicholas Wilde](https://github.com/nicholaswilde/).

[1]: <https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md>
