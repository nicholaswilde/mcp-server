# :material-docker: Dockerfile Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying Dockerfiles. The goal is to produce Docker images that are efficient, secure, and easy to maintain, following best practices inspired by the `linuxserver.io` Docker image philosophy.

## :material-folder-open: Structure and Best Practices

-   **Minimal Base Image:** Start with a minimal and appropriate base image (e.g., Alpine Linux variants) to reduce image size and attack surface.
-   **Multi-Stage Builds:** Utilize multi-stage builds to separate build-time dependencies from runtime dependencies, resulting in smaller final images.
-   **Layer Caching:** Order instructions to leverage Docker's layer caching effectively. Place frequently changing instructions (e.g., `COPY` application code) later in the Dockerfile.
-   **Consolidate `RUN` Instructions:** Combine multiple `RUN` commands using `&&` and `\` to reduce the number of layers. Clean up temporary files in the same `RUN` instruction.
-   **Specific Versions:** Always pin specific versions for base images and dependencies to ensure reproducible builds. Avoid `latest`.

## :material-format-text: Instructions and Usage

-   **`FROM`:** Specify the base image and tag.
-   **`LABEL`:** Add metadata to the image (e.g., maintainer, version, description).
-   **`ENV`:** Define environment variables for configuration. Use clear and descriptive names.
-   **`ARG`:** Define build-time variables.
-   **`WORKDIR`:** Set the working directory for subsequent `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` instructions.
-   **`COPY` vs. `ADD`:** Prefer `COPY` for copying local files and directories. Avoid `ADD` unless you need its tar extraction or URL fetching capabilities.
-   **`RUN`:** Execute commands in a new layer.
-   **`USER`:** Run processes as a non-root user. Create a dedicated user and group with minimal privileges.
-   **`EXPOSE`:** Document the ports the application listens on.
-   **`VOLUME`:** Define mount points for external volumes.
-   **`HEALTHCHECK`:** Implement health checks to verify the container's health.
-   **`CMD` / `ENTRYPOINT`:** Define the default command or entry point for the container. Use the exec form (`["executable", "param1", "param2"]`).

## :material-security: Security Considerations

-   **Non-Root User:** Always run your application as a non-root user.
-   **Minimize Privileges:** Grant only the necessary permissions to files and directories.
-   **Remove Sensitive Data:** Ensure no sensitive data (e.g., API keys, passwords) is left in the image layers.
-   **Regular Updates:** Keep base images and dependencies updated to patch security vulnerabilities.

## :material-speedometer: Optimization

-   **`.dockerignore`:** Use a `.dockerignore` file to exclude unnecessary files and directories from the build context.
-   **Smallest Possible Image:** Strive for the smallest possible final image size.
-   **Build Caching:** Optimize Dockerfile instructions to maximize build cache utilization.

## :material-source-repository: Referencing linuxserver.io Style

The `linuxserver.io` Docker images are renowned for their efficiency, security, and ease of use. Key aspects to emulate include:
-   Consistent use of Alpine Linux as a base.
-   Standardized environment variables for configuration.
-   Proper user/group ID (PUID/PGID) handling.
-   Clear documentation and examples.
-   Focus on single-process containers.
