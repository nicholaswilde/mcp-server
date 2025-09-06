# Taskfile.yml Creation Guidelines

This document provides instructions for creating a new `Taskfile.yml` within this repository. Task is a task runner / build tool that aims to be simpler and easier to use than `Makefile`.

## 1. Prerequisites

Ensure you have Task installed. If not, you can find installation instructions on the [Task website](https://taskfile.dev/#/installation).

## 2. Basic Taskfile Structure

A `Taskfile.yml` typically consists of three main sections:

*   `version`: Specifies the Taskfile schema version (e.g., `'3'`).
*   `vars`: Defines variables that can be reused across tasks.
*   `tasks`: Contains the definitions of individual tasks.

## 3. Common Tasks

Here are some common tasks you might include in your `Taskfile.yml`, inspired by the project's existing `Taskfile.yml`:

*   **`install`**: Installs project dependencies.
*   **`run`**: Runs the main application server.

*   **`lint`**: Executes linting and formatting checks.
*   **`build`**: Builds project artifacts, such as Docker images.
*   **`docker-run`**: Runs the application within a Docker container.
*   **`test`**: Executes unit or integration tests.

## 4. Example `Taskfile.yml`

Below is an example `Taskfile.yml` based on the project's existing configuration. You can adapt this to your specific needs.

```yaml
version: '3'

vars:
  VER: '2.5'
  SOURCE: 'source venv/bin/activate'
  DOCKER_REPO: 'nicholaswilde/mcp-server'

tasks:
  gflash:
    desc: Run Gemini with the gemini-2.5-flash model.
    cmds:
      - gemini -m gemini-{{ .VER }}-flash
  glite:
    desc: Run Gemini with the gemini-2.5-flash-lite model.
    cmds:
      - gemini -m gemini-{{ .VER }}-flash-lite

  gpro:
    desc: 'Run Gemini with the gemini-{{ .VER }}-pro model.'
    cmds:
      - gemini -m gemini-{{ .VER }}-pro

  install:
    desc: "Install Python dependencies"
    cmds:
      - ./venv/bin/pip-sync

  run:
    desc: "Run the FastAPI server"
    env:
      AGENTS_LIBRARY_PATH: "{{ .TASKFILE_DIR }}/agents-library"
    cmds:
      - |
        {{ .TASKFILE_DIR }}/venv/bin/python -m uvicorn app.server:app --host 0.0.0.0 --port 8080 --reload
    ignore_error: true

  lint:
    desc: "Run linting and formatting checks"
    cmds:
      - ./venv/bin/ruff check .
      - ./venv/bin/ruff format . --check # Use --check in CI to only verify formatting

  build:
    desc: "Build and push the Docker image for multiple architectures (amd64, arm64)"
    cmds:
      - docker buildx build --platform linux/amd64,linux/arm64 -t {{ .DOCKER_REPO }}:latest --push .

  docker-run:
    desc: "Run the Docker container"
    cmds:
      - docker run -p 8080:8080 {{ .DOCKER_REPO }}

  test:
    desc: "Run Python unit tests"
    cmds:
      - |
        PYTHONPATH=. ./venv/bin/pytest tests/test_server.py
  default:
    cmds:
      - task -l
    silent: true
```

## MkDocs Integration

If an MkDocs site is available in the repository, a `serve` task should be created in `Taskfile.yml` to serve the documentation locally using the `nicholaswilde/mkdocs-material` Docker image.

- **Task Name:** `serve`
- **Description:** "Serve the documentation locally using Docker."
- **Command:**
  ```yaml
  cmds:
    - >-
      docker run --rm -it -p {{ .PORT }}:{{ .PORT}} -v ${PWD}:/docs --platform linux/amd64 {{ .IMAGE }} serve --dev-addr 0.0.0.0:{{ .PORT }} -f ./mkdocs.yml
  ```
- **Variables:**
    - `IMAGE`: Should be set to `nicholaswilde/mkdocs-material`.
    - `PORT`: The port on which the documentation will be served (e.g., `8000`).

## Gemini CLI Integration

Tasks should be created to facilitate the launching of the `gemini-cli` with different models.

- **Task Names:**
    - `gpro`: For running Gemini with the `gemini-2.5-pro` model.
    - `gflash`: For running Gemini with the `gemini-2.5-flash` model.
- **Description:** Clear descriptions indicating the model used.
- **Commands:**
  ```yaml
  cmds:
    - gemini -m gemini-2.5-pro
  ```
  ```yaml
  cmds:
    - gemini -m gemini-2.5-flash
  ```

## Docker Integration

Tasks should be created to facilitate building and testing Docker images.

- **Task Name:** `build`
- **Description:** "Build and push the Docker image for multiple architectures (amd64, arm64)."
- **Command:**
  ```yaml
  cmds:
    - docker buildx build --platform linux/amd64,linux/arm64 -t {{ .DOCKER_REPO }}:latest --push .
  ```
- **Variables:**
    - `DOCKER_REPO`: The name of the Docker repository (e.g., `nicholaswilde/mcp-server`).

## Language-Specific Tasks

`Taskfile.yml` should include tasks tailored to the primary programming language(s) used in the project, facilitating common development workflows.

### Python

- **`install`**: Install Python dependencies (e.g., `pip install -r requirements.txt` or `pip-sync`).
- **`run`**: Run the main Python application (e.g., `python main.py` or `uvicorn app.server:app`).
- **`test`**: Run Python unit and integration tests (e.g., `pytest`).
- **`lint`**: Run linting and formatting checks (e.g., `ruff check .`, `ruff format .`).
- **`compile`**: Compile `requirements.in` to `requirements.txt` (e.g., `pip-compile requirements.in`).

### JavaScript/TypeScript

- **`install`**: Install Node.js dependencies (e.g., `npm install` or `yarn install`).
- **`start`**: Start the development server (e.g., `npm start` or `npm run dev`).
- **`build`**: Build the project for production (e.g., `npm run build`).
- **`test`**: Run JavaScript/TypeScript tests (e.g., `npm test` or `jest`).
- **`lint`**: Run linting and formatting checks (e.g., `npm run lint` or `eslint .`).

### Go

- **`build`**: Compile the Go application (e.g., `go build -o bin/app .`).
- **`run`**: Run the Go application (e.g., `go run main.go`).
- **`test`**: Run Go tests (e.g., `go test ./...`).
- **`lint`**: Run Go linting checks (e.g., `golangci-lint run`).
- **`clean`**: Clean build artifacts (e.g., `go clean`).

## Default Task

A `default` task should be created to list all available tasks and their descriptions. This provides a quick overview of the project's commands.

- **Task Name:** `default`
- **Description:** "List all available tasks."
- **Command:**
  ```yaml
  cmds:
    - task -l
  ```
- **Options:**
    - `silent: true`: To prevent Task from printing the command itself before execution.
