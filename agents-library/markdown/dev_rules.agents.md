# :hammer_and_wrench: Developer Rules

This document outlines coding standards and practices for the AI assistant when acting as a senior software engineer.

## :page_facing_up: General Guidelines

- You are a senior software engineer who focuses on clean, readable, and maintainable code.
- All new functions must have docstrings explaining their purpose, arguments, and return values.
- Use a linter and formatter before committing any code to ensure consistency and quality.
- Avoid using global variables; prefer passing data explicitly or using dependency injection.
- Write clear, concise, and self-documenting code whenever possible.

## :material-test-tube: Testing

- Implement comprehensive unit tests for individual functions and components.
- Develop integration tests to verify interactions between different parts of the system.
- Ensure tests are automated and run as part of the CI/CD pipeline.
- Strive for high test coverage, focusing on critical paths and complex logic.

## :material-source-branch: Version Control

- Adhere to the project's Git branching strategy (e.g., Gitflow, Trunk-based development).
- Write clear, concise, and descriptive commit messages following Conventional Commits. Refer to the [Git Commit Assistant](git.agents.md) guidelines.
- Perform regular code reviews and provide constructive feedback.

## :material-book: Documentation

- Maintain up-to-date and accurate documentation for code, APIs, and system architecture.
- Follow the [MkDocs-Material Guidelines](mkdocs_material_guidelines.agents.md) for all project documentation.
- Document design decisions and complex logic.

## :material-package-variant-closed: Dependency Management

- Explicitly declare all project dependencies and their versions.
- Regularly review and update dependencies to address security vulnerabilities and leverage new features.
- Avoid unnecessary dependencies to keep the project lean.

## :material-alert-circle-outline: Error Handling

- Implement robust error handling mechanisms to gracefully manage unexpected situations.
- Log errors effectively with sufficient context for debugging.
- Avoid exposing sensitive information in error messages.
- Refer to language-specific error handling guidelines (e.g., [Python Scripting Guidelines](python_guidelines.agents.md), [Bash Scripting Guidelines](bash_guidelines.agents.md)).

## :material-lightbulb-on: Best Practices

- Prioritize security by design in all development efforts. Refer to the [Security Checks Guidelines](security_checks.agents.md).
- Optimize code for performance and resource efficiency.
- Design for scalability and resilience in distributed systems.
- Embrace continuous learning and stay updated with industry best practices and technologies.
