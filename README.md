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
        *   `bash/`: Contains bash scripts.
            *   `uptime.sh`: Example uptime script.
        *   `markdown/`: Contains markdown agent instruction files.
            *   `common_prompts.agents.md`: Common prompts for agents.
            *   `dev_rules.agents.md`: Development-related agent rules.
            *   `fantasy_football_ai.agents.md`: Git commit and tagging conventions.
            *   `frame_fi.agents.md`: Bash and Python scripting guidelines.
            *   `homelab_docs.agents.md`: Markdown documentation guidelines.
            *   `security_checks.agents.md`: Security-related agent checks.

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

For custom user and group IDs, you can set `PUID` and `PGID` environment variables in your `compose.yaml` or directly in your shell:

```bash
PUID=1000 PGID=1000 docker compose up
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
    "sharedAgents": {
      "httpUrl": "http://<ip-address>:8080"
    }
  }
}
```

### Using the `mcp` tool

Once the `mcp-server` is configured in `gemini-cli`, you can use the `mcp` tool to interact with the server. For example, to list all available agent instructions:

```bash
/mcp list
```

**Output**

```bash
  🟢 sharedAgents - Ready (2 tools)
    Tools:
    - get_agents_instructions
    - list_agents_instructions
```

```bash
list_agents_instructions
```

**Output**

```json
 ╭───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ✔ list_agents_instructions (sharedAgents MCP Server) list_agents_instructions (sharedAgents MCP Server)  │
 │                                                                                                           │
 │    {                                                                                                      │
 │      "files": [                                                                                           │
 │        "frame_fi",                                                                                        │
 │        "fantasy_football_ai",                                                                             │
 │        "security_checks",                                                                                 │
 │        "dev_rules",                                                                                       │
 │        "common_prompts",                                                                                  │
 │        "homelab_docs"                                                                                     │
 │      ]                                                                                                    │
 │    }                                                                                                      │
 ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

```bash
get_agents_instructions common_prompts
```

**Output**

```
✦ I have retrieved the "common_prompts" instructions. It contains guidelines for creating Markdown
  documentation and for scripting in Bash and Python.
```

Example `gemini-cli` prompt to use the `common_prompts` agent to create a bash script.

```bash
using the get_agents_instructions common_prompts agent, write me a bash script that checks
downloads the latest release of sops from GitHub with architecture amd64 and linux. 
```

>[!TIP]
>It's important to add the `get_agents_instructions` to the prompt so that `gemini-cli` knows which tool to use to retrieve the remote agent.

Instead of explictly stating to use the mcp agent in every prompt, instruct `gemini-cli` to use the MCP server's `common_prompts` by adding the following to the project's `AGENTS.md` file.

```markdown
# Agent Instructions

## Bash Scripting Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `common_prompts` agent whenever a user asks to create or modify a bash script.
```
See [reference][1].

## :balance_scale: License

This project is licensed under the [Apache License 2.0](./LICENSE).

## :pencil: Author

This project was started in 2025 by [Nicholas Wilde](https://github.com/nicholaswilde/).

[1]: <https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md>
