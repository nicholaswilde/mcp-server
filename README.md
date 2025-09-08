# :robot: MCP Server :computer:

[![Test Workflow](https://img.shields.io/github/actions/workflow/status/nicholaswilde/mcp-server/test.yml?label=test&style=for-the-badge&branch=main)](https://github.com/nicholaswilde/mcp-server/actions/workflows/test.yml)
[![Task Enabled](https://img.shields.io/badge/Task-Enabled-brightgreen?style=for-the-badge&logo=task&logoColor=white)](https://taskfile.dev/#/)

An MCP (Multi-Cloud Platform) server that provides a library of reusable agent instructions and scripts to a generative AI model.

>[!WARNING]
>This project is in a development stage. Features and configurations are subject to change.

## :book: Documentation

For comprehensive documentation, please visit the [MkDocs site](https://nicholaswilde.io/mcp-server/).

## :mag: TL;DR

The MCP Server uses FastAPI to expose a set of tools that can be consumed by a compatible AI model (like Google's Gemini). It provides a library of standardized instructions (`AGENTS.md` files) and utility scripts (`.sh` files) to enable the AI to perform complex, context-aware tasks.

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

## :balance_scale: License

This project is licensed under the [Apache License 2.0](./LICENSE).

## :pencil: Author

This project was started in 2025 by [Nicholas Wilde](https://github.com/nicholaswilde/).
