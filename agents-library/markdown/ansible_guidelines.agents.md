# :material-ansible: Ansible Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying Ansible playbooks, roles, and inventories. The goal is to produce Ansible code that is modular, reusable, and easy to maintain, following best practices from the Ansible community and conventions observed in the [nicholaswilde/homelab-playbooks](https://github.com/nicholaswilde/homelab-playbooks) repository.

## :material-folder-open: File Structure

-   **Playbooks:** Organize playbooks logically, often by application or purpose.
-   **Roles:** Use Ansible roles for reusability and modularity. A typical role structure includes:
    -   `defaults/main.yml`: Default variables for the role.
    -   `vars/main.yml`: Other variables for the role.
    -   `tasks/main.yml`: Main tasks for the role.
    -   `handlers/main.yml`: Handlers for the role.
    -   `templates/`: Jinja2 templates used by the role.
    -   `files/`: Static files copied by the role.
    -   `meta/main.yml`: Metadata for the role.
-   **Inventory:** Separate inventory files for different environments (e.g., `inventory/production`, `inventory/development`).

## :material-format-text: Naming Conventions

-   **Playbooks:** Use descriptive, lowercase names with underscores (e.g., `deploy_web_app.yml`).
-   **Roles:** Use lowercase, descriptive names (e.g., `nginx`, `docker`).
-   **Variables:** Use `snake_case` for variable names.
-   **Tasks:** Provide clear, concise names for tasks using `name:`.

## :material-code-tags: Code Style and Formatting

-   **YAML Syntax:** Adhere to YAML best practices (2-space indentation, consistent quoting).
-   **Playbook Structure:**
    -   Always start with `---`.
    -   Use `name:` for play and task descriptions.
    -   Keep plays focused on a single objective.
-   **Idempotency:** Ensure playbooks are idempotent, meaning they can be run multiple times without causing unintended side effects.
-   **Error Handling:** Implement robust error handling using `failed_when`, `changed_when`, `ignore_errors`, and `block/rescue/always`.
-   **Tags:** Use tags to allow for selective execution of parts of a playbook.

## :material-security: Security Considerations

-   **Vault:** Use Ansible Vault to encrypt sensitive data (e.g., passwords, API keys) in variable files.
-   **Least Privilege:** Run playbooks with the minimum necessary privileges.
-   **SSH Keys:** Securely manage SSH keys used for connecting to target hosts.

## :material-repeat: Reusability

-   **Roles:** Maximize the use of roles for common functionalities.
-   **Variables:** Use variables effectively to make playbooks flexible and reusable across environments.
-   **Templates:** Leverage Jinja2 templates for configuration files that require dynamic content.

## :material-source-repository: Referencing homelab-playbooks

The [nicholaswilde/homelab-playbooks](https://github.com/nicholaswilde/homelab-playbooks) repository serves as a good example for structuring Ansible projects, particularly for homelab environments. Observe its conventions for:
-   Role organization.
-   Inventory management.
-   Playbook design patterns.
