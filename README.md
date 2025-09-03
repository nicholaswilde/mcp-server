# MCP Server

[![Test Workflow](https://img.shields.io/github/actions/workflow/status/nicholaswilde/mcp-server/test.yml?label=test&style=for-the-badge&branch=main)](https://github.com/nicholaswilde/mcp-server/actions/workflows/test.yml)
[![Task Enabled](https://img.shields.io/badge/Task-Enabled-brightgreen?style=for-the-badge&logo=task&logoColor=white)](https://taskfile.dev/#/)

An MCP (Multi-Cloud Platform) server that provides a library of reusable agent instructions and scripts to a generative AI model.

> [!WARNING]
> This project is in a development stage. Features and configurations are subject to change.

## Overview

This server uses FastAPI to expose a set of tools that can be consumed by a compatible AI model (like Google's Gemini). The primary purpose is to provide the AI with a library of standardized instructions (`AGENTS.md` files) and utility scripts (`.sh` files). This allows the AI to perform complex, context-aware tasks consistently by drawing from a central, version-controlled library.

The core components are:
-   **`app/server.py`**: The FastAPI application that serves the tools.
-   **`agents-library/`**: The central repository for agent instructions and scripts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.11+
-   [Task](https://taskfile.dev/installation/)
-   [Docker](https://www.docker.com/get-started) (for containerized deployment)
-   [pre-commit](https://pre-commit.com/#installation) (for development)

### Installation

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

## Usage

You can run the server using Task, which simplifies the process, or with Docker Compose for a containerized environment.

### Running the Server Locally

To run the FastAPI server on your local machine:
```bash
task run
```
The server will be available at `http://0.0.0.0:8080`. It will automatically reload when code changes are detected.

### Running with Docker

To build and run the server in a Docker container:
```bash
# Build the multi-platform image and push it
task build

# Run the container locally
task docker-run
```
The server will be available at `http://localhost:8080`.

### Available Tasks

This project uses `Task` as a command runner. Here are the most common commands:

-   `task install`: Install/sync Python dependencies.
-   `task run`: Run the FastAPI server locally with auto-reload.
-   `task lint`: Run linting and formatting checks.
-   `task test`: Run the unit tests.
-   `task build`: Build and push the multi-platform Docker image.
-   `task docker-run`: Run the application in a Docker container.

To see all available tasks, run `task -l`.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](./docs/contributing.md) to get started.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](./LICENSE) file for details.