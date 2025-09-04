# :material-lock: SOPS and .env Guidelines

As an AI assistant, I will adhere to the following guidelines when working with `.env` files and secrets management using SOPS.

## :material-key: .env Files

-   `.env` files are used to store environment-specific variables, especially sensitive information like API keys, database credentials, and other secrets.
-   They should **NEVER** be committed directly to version control (Git).

## :material-shield: SOPS Encryption

-   All `.env` files containing sensitive information **MUST** be encrypted using [SOPS](https://github.com/getsops/sops).
-   Encrypted files should consistently end with the `.enc` extension (e.g., `.env.enc`, `secrets.yaml.enc`).
-   - SOPS allows for encryption of files using various key management systems (KMS). **Prefer `age` keys for encryption due to their simplicity and strong cryptographic properties**, but other options such as AWS KMS, GCP KMS, Azure Key Vault, or PGP keys are also supported.
-   The encrypted `.env` file should be named `.<environment>.env.enc` (e.g., `.env.prod.enc`, `.env.dev.enc`).

## :material-git: .gitignore Configuration

-   Ensure that all `.env` files (both plain and encrypted) are properly ignored by Git.
-   Add entries like `*.env` and `*.env.enc` to your project's `.gitignore` file.

## :material-security: Best Practices

-   **Local Development:** For local development, use a `.env` file (unencrypted) that is explicitly ignored by Git. This file should contain non-sensitive defaults or placeholders.
-   **Production/Staging:** Encrypted `.env.enc` files should be used in production and staging environments. These files should be decrypted at deployment time using SOPS.
-   **Key Management:** Ensure that the keys used for SOPS encryption are securely managed and accessible only to authorized personnel or systems.
-   **Environment Variables:** When deploying applications, prefer injecting secrets as environment variables directly into the runtime environment rather than relying on decrypted files on disk, if the platform supports it.
-   **Avoid In-Place Encryption:** Do not encrypt files in-place using the `-i` flag with SOPS. Instead, pipe the output to a new file to prevent accidental data loss or corruption. For example: `sops <file> > <file>.enc`.

## :material-file-document: SOPS Configuration File Creation

This section provides instructions for creating a `.sops.yaml` configuration file for use with SOPS (Secrets OPerationS).

### .sops.yaml

The `.sops.yaml` file is used to configure SOPS for a repository. It defines rules for encrypting files based on their filenames.

### Example `.sops.yaml`

Here is an example of a `.sops.yaml` file that encrypts all `.yaml` and `.db` files using an `age` key.

```yaml
creation_rules:
  - filename_regex: \.yaml$
    age: 'age1x2at6wwq2gks47fsep9a25emdeqd93e3k0gfsswtmhruqrteu5jqjvy7kd'
  - filename_regex: \.db$
    age: 'age1x2at6wwq2gks47fsep9a25emdeqd93e3k0gfsswtmhruqrteu5jqjvy7kd'
```

### Instructions

1.  Create a file named `.sops.yaml` in the root of your repository.
2.  Copy the content from the example above into your `.sops.yaml` file.
3.  Replace the `age` key with your own public `age` key.
