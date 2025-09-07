# MCP Server

[![Test Workflow](https://img.shields.io/github/actions/workflow/status/nicholaswilde/mcp-server/test.yml?label=test&style=for-the-badge&branch=main)](https://github.com/nicholaswilde/mcp-server/actions/workflows/test.yml)
[![Task Enabled](https://img.shields.io/badge/Task-Enabled-brightgreen?style=for-the-badge&logo=task&logoColor=white)](https://taskfile.dev/#/)

An MCP (Multi-Cloud Platform) server that provides a library of reusable agent instructions and scripts to a generative AI model.

> [!WARNING]
> This project is in a development stage. Features and configurations are subject to change.

## :mag: Overview

This server uses FastAPI to expose a set of tools that can be consumed by a compatible AI model (like Google's Gemini). The primary purpose is to provide the AI with a library of standardized instructions (`AGENTS.md` files) and utility scripts (`.sh` files). This allows the AI to perform complex, context-aware tasks consistently by drawing from a central, version-controlled library.

The core components are:
-   **`app/server.py`**: The FastAPI application that serves the tools.
-   **`agents-library/`**: The central repository for agent instructions and scripts.

## :rocket: Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### :gear: Prerequisites

-   Python 3.11+
-   [Task](https://taskfile.dev/installation/)
-   [Docker](https://www.docker.com/get-started) (for containerized deployment)
-   [pre-commit](https://pre-commit.com/#installation) (for development)

### :computer: Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nicholaswilde/mcp-server.git
    cd mcp-server
    ```

2.  **Set up the Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    This project uses `pip-tools` to manage dependencies.
    ```bash
    pip install pip-tools
    task install
    ```

4.  **Set up pre-commit hooks:**
    Install the pre-commit hooks to ensure your commits adhere to the project's code style and quality standards.
    ```bash
    pre-commit install
    ```

## :running: Usage

You can run the server using Task, which simplifies the process, or with Docker Compose for a containerized environment.

### :desktop_computer: Running the Server Locally

To run the FastAPI server on your local machine:
```bash
task run
```
The server will be available at `http://0.0.0.0:8080`. It will automatically reload when code changes are detected.

To generate a new API key:
```bash
python app/server.py --generate-api-key
```

### :whale: Running with Docker

To build and run the server in a Docker container:
```bash
# Build the multi-platform image and push it
task build

# Run the container locally
task docker-run
```
The server will be available at `http://localhost:8080`.

### :clipboard: Available Tasks

This project uses `Task` as a command runner. Here are the most common commands:

-   `task install`: Install/sync Python dependencies.
-   `task run`: Run the FastAPI server locally with auto-reload.
-   `task lint`: Run linting and formatting checks.
-   `task test`: Run the unit tests.
-   `task build`: Build and push the multi-platform Docker image.
-   `task docker-run`: Run the application in a Docker container.

To see all available tasks, run `task -l`.

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

### :tools: Using the `mcp` tool

Once the `mcp-server` is configured in `gemini-cli`, you can use the `mcp` tool to interact with the server. For example, to list all available agent instructions:

**Prompt**

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

**Prompt**

```bash
list_agents_instructions
```

**Output**

```
✔ list_agents_instructions (sharedAgents MCP Server) list_agents_instructions (sharedAgents MCP Server)

   {
     "files": [
       "frame_fi",
       "git",
       "security_checks",
       "dev_rules",
       "common_prompts",
       "homelab_docs"
     ]
   }
```

**Prompt**

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

Instead of explictly stating to use the mcp agent in every prompt, instruct `gemini-cli` to use the MCP server's prompts by adding the following to the project's `AGENTS.md` file.

```markdown
# Agent Instructions

## Agent Rules

## Ansible Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `ansible_guidelines` agent when creating or modifying Ansible playbooks, roles, and inventories.

## Cloud Best Practices Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `cloud_best_practices` agent when discussing cloud best practices.

## Common Prompts Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `common_prompts` agent for general prompting guidelines.

## Dev Rules Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `dev_rules` agent when discussing development rules.

## Dockerfile Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `dockerfile_guidelines` agent when creating or modifying Dockerfiles.

## Docs Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `docs_guidelines` agent when creating or modifying documentation.

## Git Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `git` agent for git-related queries.

## Frame.fi Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `frame_fi` agent for Frame.fi related queries.

## GitHub Repo Config Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `github_repo_config` agent when configuring GitHub repositories.

## Homelab Docs Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `homelab_docs` agent for homelab documentation.

## .env and SOPS Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `env_sops_guidelines` agent when working with `.env` files and SOPS encryption.

## MkDocs-Material Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `mkdocs_material_guidelines` agent when creating or modifying MkDocs-Material documentation.

## README.md Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `readme_guidelines` agent when creating or modifying `README.md` files.

## MkDocs Site Creation Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `mkdocs_site_creation` agent when creating MkDocs sites.

## Platform.io Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `platformio_guidelines` agent when creating or modifying Platform.io projects.

## Recommended Bash Scripts Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `recommended_bash_scripts` agent when recommending bash scripts.

## Bash Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `bash_guidelines` agent when discussing bash scripting guidelines.

## Python Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `python_guidelines` agent when discussing python scripting guidelines.

## Security Checks Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `security_checks` agent when performing security checks.

## SOPS Config Creation Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `sops_config_creation` agent when configuring SOPS.

## Taskfile Creation Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `taskfile_creation` agent when creating Taskfiles.

## Terraform Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `terraform_guidelines` agent when discussing Terraform guidelines.

## YAML Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `yaml_guidelines` agent when creating or modifying YAML files.
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](./docs/contributing.md) to get started.

See [reference][1].

## :balance_scale: License

This project is licensed under the [Apache License 2.0](./LICENSE).

## :pencil: Author

This project was started in 2025 by [Nicholas Wilde](https://github.com/nicholaswilde/).
