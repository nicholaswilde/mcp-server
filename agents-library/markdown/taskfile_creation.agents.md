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
