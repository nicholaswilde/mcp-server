# :material-folder-open: Agents Library Files

The `agents-library` directory contains a collection of markdown files that serve as guidelines and instructions for AI agents. These files define best practices, coding standards, and operational procedures for various aspects of software development and cloud management.

## :material-file-document-outline: Purpose of Markdown Files

Each markdown file within the `agents-library/markdown/` directory focuses on a specific domain or technology, providing detailed guidance. For example:

*   `python_guidelines.agents.md`: Outlines Python scripting best practices.
*   `bash_guidelines.agents.md`: Details standards for writing bash scripts.
*   `dockerfile_guidelines.agents.md`: Provides best practices for creating Dockerfiles.
*   `api_design_guidelines.agents.md`: Sets standards for API design.
*   `git.agents.md`: Defines conventions for Git commit messages and tagging.
*   `cloud_best_practices.agents.md`: Lists general cloud best practices for agents.
*   `mkdocs_material_guidelines.agents.md`: Specifies guidelines for documenting with MkDocs-Material.
*   `terraform_guidelines.agents.md`: Outlines best practices for Terraform configurations.
*   `env_sops_guidelines.agents.md`: Details guidelines for managing environment variables and secrets with SOPS.
*   `taskfile_creation.agents.md`: Provides guidance on creating and using `Taskfile.yml`.

These files are crucial for ensuring consistency and quality across different development tasks performed by the AI.

## :material-bash: Bash Scripts

The `agents-library/bash/` directory contains various bash scripts designed to automate common tasks related to cloud operations and system management. These scripts are intended to be used by AI agents or directly by developers.

*   `cost_optimizer.sh`: Analyzes and optimizes cloud resource costs.
*   `deploy_app.sh`: Automates the deployment of applications.
*   `health_check.sh`: Performs health checks on services or applications.
*   `list_markdown_files.sh`: Lists markdown files within the agents library.
*   `manage_resource.sh`: Provides functionality for managing cloud resources.
*   `monitor_logs.sh`: Monitors application or system logs.
*   `uptime.sh`: Checks and reports the uptime of services.

## :material-pencil-ruler: Updating and Creating Agent Guidelines

To update an existing guideline or create a new one:

1.  **Identify the Need:** Determine if a new guideline is needed or if an existing one requires updates based on project requirements or observed best practices.
2.  **Create/Edit Markdown File:**
    *   **New File:** Create a new markdown file in the `agents-library/markdown/` directory. The filename should be descriptive and follow the convention `*.agents.md` (e.g., `new_guideline.agents.md`).
    *   **Existing File:** Locate the relevant markdown file in `agents-library/markdown/` and edit its content.
3.  **Content Structure:** Follow the established structure within existing files. Typically, this includes:
    *   A clear title with an emoji.
    *   Sections detailing principles, best practices, naming conventions, code style, security considerations, and examples.
    *   Use of Markdown for formatting, including headings, lists, code blocks, and links.
4.  **LLM Assistance:** An AI model (like myself) can assist in drafting, refining, and formatting these markdown files. You can prompt the AI to generate content for a specific guideline or to improve existing content. For example, you could ask: "Draft guidelines for writing secure Go code, following the pattern of `python_guidelines.agents.md`."
5.  **Review and Commit:** Once the markdown file is updated or created, review the changes and commit them to the repository following the project's Git conventions.

By maintaining these guidelines, we ensure that AI agents operate effectively and consistently within the project's established standards.
