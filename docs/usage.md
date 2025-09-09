# :person_running: Usage

You can run the server using Task, which simplifies the process, or with Docker Compose for a containerized environment.

## :desktop_computer: Running the Server Locally

To run the FastAPI server on your local machine:

=== "Task"

    ```bash
    task run
    ```

=== "Manual"

    ```bash
    AGENTS_LIBRARY_PATH="./agents-library" && ./venv/bin/python -m uvicorn app.server:app --host 0.0.0.0 --port 8080 --reload
    ```

The server will be available at `http://0.0.0.0:8080`. It will automatically reload when code changes are detected.

## :whale: Running with Docker

To build the server in a Docker container:

=== "Task"

    ```bash
    task build
    ```
=== "Manual"

    ```bash
    docker build -t nicholaswilde/mcp-server .
    ```

To run the server in a Docker container:

=== "Task"

    ```bash
    task docker-run
    ```

=== "Manual"

    ```bash
    docker run -p 8080:8080 nicholaswilde/mcp-server
    ```

The server will be available at `http://localhost:8080`.

??? abstract "compose.yaml"

    ```yaml
    --8<-- "compose.yaml"
    ```

## :clipboard: Available Tasks

!!! abstract ""

    ```yaml
    --8<-- "task-list.txt"
    ```
