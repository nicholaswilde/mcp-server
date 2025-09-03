# Terraform Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying Terraform configurations. The goal is to produce Terraform code that is modular, reusable, and easy to maintain.

## 1. File Structure

-   **`main.tf`**: Contains the primary set of resources for the configuration.
-   **`variables.tf`**: Defines all input variables for the configuration.
-   **`outputs.tf`**: Declares all outputs from the configuration.
-   **`versions.tf`**: Specifies version constraints for Terraform and providers.
-   **`README.md`**: Provides documentation for the Terraform module or configuration.

## 2. Naming Conventions

-   **Resources:** Use `snake_case` and be descriptive (e.g., `aws_s3_bucket.app_storage`).
-   **Variables:** Use `snake_case`. Provide clear descriptions and default values where appropriate.
-   **Outputs:** Use `snake_case` and provide descriptions.

## 3. Code Style and Formatting

-   **Formatting:** Always run `terraform fmt` before committing changes to ensure consistent formatting.
-   **Arguments:** Align arguments within resource blocks for readability.
-   **Comments:** Use comments (`#`) to explain complex configurations or non-obvious logic.

## 4. State Management

-   **Remote Backend:** Always use a remote backend (e.g., AWS S3 with DynamoDB for locking, Azure Storage Account, or Terraform Cloud) to store the state file securely and to manage state locking. Avoid committing the `.tfstate` file to version control.

## 5. Modularity

-   **Modules:** Group related resources into modules to promote reusability and maintain a clean root configuration.
-   **Module Sources:** Use versioned module sources from a reliable registry (e.g., Terraform Registry, a private registry, or a version-controlled repository).

## 6. Variables and Outputs

-   **Input Variables:** Avoid hardcoding values. Use variables for all configurable parameters.
-   **Outputs:** Expose useful information from resources as outputs for other configurations to consume.

### Example Structure

```
.
├── main.tf
├── variables.tf
├── outputs.tf
├── versions.tf
└── README.md
```

### Example `versions.tf`

```terraform
terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "global/s3/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```
