# :rocket: Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## :gear: Prerequisites

-   Python 3.11+
-   [Task](https://taskfile.dev/installation/)
-   [Docker](https://www.docker.com/get-started) (for containerized deployment)
-   [pre-commit](https://pre-commit.com/#installation) (for development)

## :computer: Installation

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
