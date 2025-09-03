# YAML File Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying YAML files. My goal is to produce YAML that is clear, consistent, and easily parsable.

## General Guidelines

-   **Start of Document:** Every YAML file must begin with `---` on the first line to denote the start of a new document.
-   **Indentation:** Use 2 spaces for indentation. Do not use tabs.
-   **Keys:** Keys should be in `snake_case` or `camelCase` depending on the existing convention of the project. Be consistent.
-   **Values:**
    -   Strings with special characters (e.g., `:`, `{`, `}`, `[`, `]`, `,`, `&`, `*`, `#`, `?`, `|`, `-`, `<`, `>`, `=`, `!`, `%`, `@`, `` ` ``) should be enclosed in quotes.
    -   Use single quotes `'` by default, unless the string contains a single quote, in which case use double quotes `"`.
    -   Boolean values should be written as `true` or `false`.
-   **Lists (Sequences):** Use a hyphen followed by a space (`- `) for list items.
-   **Comments:** Use comments (`#`) to explain non-obvious configurations or important details.
-   **Structure:** Maintain a clear and logical structure. Group related items together.

### Example

```yaml
---
# Example YAML configuration
version: '3.8'

services:
  web:
    image: "nginx:latest"
    ports:
      - "8080:80" # Expose port 8080 on the host
    restart: always
    environment:
      - "NODE_ENV=production"
      - "SECRET_KEY='my_super_secret_key'"

  database:
    image: "postgres:13"
    volumes:
      - "db_data:/var/lib/postgresql/data"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  db_data: # Define the volume
```
