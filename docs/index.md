# :robot: MCP Server :computer:

[![Test Workflow](https://img.shields.io/github/actions/workflow/status/nicholaswilde/mcp-server/test.yml?label=test&style=for-the-badge&branch=main)](https://github.com/nicholaswilde/mcp-server/actions/workflows/test.yml)
[![Task Enabled](https://img.shields.io/badge/Task-Enabled-brightgreen?style=for-the-badge&logo=task&logoColor=white)](https://taskfile.dev/#/)

An MCP (Multi-Cloud Platform) server that provides a library of reusable agent instructions and scripts to a generative AI model.

!!! warning

    This project is in a development stage. Features and configurations are subject to change.

This documentation provides a comprehensive guide to the MCP Server. Use the navigation on the left to explore different sections.

## :rocket: TL;DR

To bootstrap the project
```bash
task bootstrap
```

To run the server locally:
```bash
task run
```

Add to `gemini-cli` settings:
```json
{
  "mcpServers": {
    "sharedAgents": {
      "httpUrl": "http://<ip-address>:8080"
    }
  }
}
```

To generate a new API key:
```bash
python app/server.py --generate-api-key
```

## :mag: Overview

This server uses FastAPI to expose a set of tools that can be consumed by a compatible AI model (like Google's Gemini). The primary purpose is to provide the AI with a library of standardized instructions (`AGENTS.md` files) and utility scripts (`.sh` files). This allows the AI to perform complex, context-aware tasks consistently by drawing from a central, version-controlled library.

The core components are:
-   **`app/server.py`**: The FastAPI application that serves the tools.
-   **`agents-library/`**: The central repository for agent instructions and scripts.

## :scales: License

​[​Apache License 2.0](https://raw.githubusercontent.com/nicholaswilde/mcp-server/refs/heads/main/docs/LICENSE)

## :pencil: Author

This project was started in 2025 by [Nicholas Wilde](https://github.com/nicholaswilde/).
