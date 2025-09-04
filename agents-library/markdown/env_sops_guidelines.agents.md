# :material-lock: .env and SOPS Guidelines

As an AI assistant, I will adhere to the following guidelines when working with `.env` files and secrets management using SOPS.

## :material-key: .env Files

-   `.env` files are used to store environment-specific variables, especially sensitive information like API keys, database credentials, and other secrets.
-   They should **NEVER** be committed directly to version control (Git).

## :material-shield: SOPS Encryption

-   All `.env` files containing sensitive information **MUST** be encrypted using [SOPS](https://github.com/getsops/sops).
-   SOPS allows for encryption of files using various key management systems (KMS), such as AWS KMS, GCP KMS, Azure Key Vault, or PGP/Age keys.
-   The encrypted `.env` file should be named `.<environment>.env.enc` (e.g., `.env.prod.enc`, `.env.dev.enc`).

## :material-git: .gitignore Configuration

-   Ensure that all `.env` files (both plain and encrypted) are properly ignored by Git.
-   Add entries like `*.env` and `*.env.enc` to your project's `.gitignore` file.

## :material-security: Best Practices

-   **Local Development:** For local development, use a `.env` file (unencrypted) that is explicitly ignored by Git. This file should contain non-sensitive defaults or placeholders.
-   **Production/Staging:** Encrypted `.env.enc` files should be used in production and staging environments. These files should be decrypted at deployment time using SOPS.
-   **Key Management:** Ensure that the keys used for SOPS encryption are securely managed and accessible only to authorized personnel or systems.
-   **Environment Variables:** When deploying applications, prefer injecting secrets as environment variables directly into the runtime environment rather than relying on decrypted files on disk, if the platform supports it.
