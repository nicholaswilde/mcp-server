# Security Checks Guidelines

As an AI assistant, I will adhere to the following guidelines when performing security checks or generating security-related content.

## General Principles

- Prioritize security by design in all generated code and recommendations.
- Avoid introducing known vulnerabilities.
- Follow secure coding best practices.
- Be cautious with sensitive information and avoid hardcoding credentials.

## Specific Checks (Examples - to be expanded)

- **Input Validation:** Always validate and sanitize user inputs to prevent injection attacks (e.g., SQL injection, XSS).
- **Authentication and Authorization:** Ensure proper authentication and authorization mechanisms are in place where applicable.
- **Error Handling:** Implement secure error handling to avoid leaking sensitive information.
- **Dependency Security:** Be aware of known vulnerabilities in third-party libraries and recommend secure versions.
- **Least Privilege:** Recommend running processes with the minimum necessary privileges.

## Automated Security Checks

- Utilize automated tools and scripts for continuous security monitoring and scanning.
- Refer to the `security_scan.sh` script for initiating various types of security scans on cloud resources or applications.
