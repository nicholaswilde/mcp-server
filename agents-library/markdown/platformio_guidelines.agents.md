# :material-chip: Platform.io Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying Platform.io projects. The goal is to produce Platform.io code that is modular, reusable, and easy to maintain, following best practices and conventions observed in the [nicholaswilde/frame-fi](https://github.com/nicholaswilde/frame-fi) repository.

## :material-folder-open: Project Structure

-   **`platformio.ini`**: The main configuration file for the Platform.io project.
-   **`src/`**: Contains the source code for your project (e.g., `.c`, `.cpp`, `.h` files).
-   **`lib/`**: Contains private libraries specific to your project.
-   **`include/`**: Contains header files.
-   **`test/`**: Contains unit tests for your project.
-   **`.pio/`**: Platform.io's internal project data (should be ignored by Git).

## :material-format-text: Naming Conventions

-   **Project Name:** Use descriptive, lowercase names with hyphens (e.g., `my-sensor-project`).
-   **Source Files:** Use descriptive names (e.g., `main.cpp`, `sensor_readings.cpp`).
-   **Variables/Functions:** Follow standard C/C++ naming conventions (e.g., `snake_case` for variables, `camelCase` for functions).

## :material-code-tags: Code Style and Formatting

-   **C/C++ Standards:** Adhere to C++11 or later standards.
-   **Indentation:** Use consistent indentation (e.g., 2 or 4 spaces).
-   **Comments:** Use comments to explain complex logic, hardware interactions, or non-obvious parts of the code.
-   **Includes:** Organize include directives logically (e.g., standard library, third-party, project-specific).

## :material-settings: `platformio.ini` Configuration

-   **`[env]` Sections:** Use `[env]` sections to define different build environments (e.g., for different boards, upload protocols, or build flags).
-   **`board`:** Specify the target development board.
-   **`framework`:** Define the development framework (e.g., `arduino`, `esp-idf`).
-   **`lib_deps`:** Declare project dependencies from Platform.io's library registry.
-   **`build_flags`:** Use build flags for compiler options, defines, or warnings.

## :material-test-tube: Testing

-   Utilize Platform.io's built-in testing framework for unit testing.
-   Organize tests in the `test/` directory.

## :material-source-repository: Referencing frame-fi

The [nicholaswilde/frame-fi](https://github.com/nicholaswilde/frame-fi) repository serves as a good example for structuring Platform.io projects, particularly for embedded systems. Observe its conventions for:
-   `platformio.ini` configuration.
-   Source code organization.
-   Library management.
