# Docker Compose Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying `docker-compose.yaml` files.

## General Principles

- **Readability:** Organize services logically and use comments where necessary.
- **Modularity:** Break down complex applications into smaller, manageable services.
- **Reproducibility:** Ensure the `docker-compose.yaml` file can consistently recreate the environment.

## Services

Each service in `docker-compose.yaml` should represent a single container.

- **`image`:** Use specific image versions (e.g., `nginx:1.21.3`) instead of `latest` to ensure reproducibility.
- **`build`:** If building a custom image, specify the `context` and `dockerfile`.
- **`ports`:** Map host ports to container ports (e.g., `80:80`).
- **`volumes`:** Mount host paths or named volumes to container paths for persistent data or configuration.
- **`environment`:** Define environment variables for the service. Use a `.env` file for sensitive information.
- **`depends_on`:** Define service dependencies to control the startup order. Note that `depends_on` only waits for the container to start, not for the service inside the container to be ready.
- **`networks`:** Assign services to custom networks for isolation and communication.
- **`restart`:** Define the restart policy for the service (e.g., `always`, `on-failure`).

## Networks

Define custom networks for better isolation and organization of services.

- **`name`:** Use descriptive names for networks.
- **`driver`:** Specify the network driver (e.g., `bridge`).

## Volumes

Define named volumes for persistent data storage.

- **`name`:** Use descriptive names for volumes.
- **`driver`:** (Optional) Specify the volume driver.

## Best Practices

- **Specific Image Versions:** Always use explicit image tags (e.g., `image: postgres:14.1-alpine`) instead of `latest`.
- **Environment Variables:** Externalize configuration using environment variables and a `.env` file.
- **Health Checks:** Implement `healthcheck` directives for services to ensure they are truly ready before dependent services start.
- **Resource Limits:** (Optional) Define `deploy.resources.limits` and `deploy.resources.reservations` for production environments.
- **Profiles:** Use `profiles` to define different service configurations for various environments (e.g., `docker-compose.dev.yaml`, `docker-compose.prod.yaml`).
- **Comments:** Add comments to explain complex configurations or decisions.
- **Avoid Root:** Run containers as non-root users whenever possible for security.
