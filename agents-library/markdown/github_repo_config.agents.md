# GitHub Repository Configuration

This document provides instructions and content for creating essential GitHub repository configuration files: `CODEOWNERS`, `FUNDING.yml`, `dependabot.yml`, and `renovate.json`. These files should be placed in the `.github/` directory of the repository.

## 1. CODEOWNERS

The `CODEOWNERS` file defines individuals or teams that are responsible for code in a repository.

**Instructions:** Create a file named `CODEOWNERS` inside the `.github/` directory with the following content.

```
*       @nicholaswilde
```

## 2. FUNDING.yml

The `FUNDING.yml` file displays a sponsor button in your repository to increase visibility of funding options.

**Instructions:** Create a file named `FUNDING.yml` inside the `.github/` directory with the following content.

```yaml
---
github: nicholaswilde
```

## 3. dependabot.yml

The `dependabot.yml` file configures Dependabot to automatically update dependencies for your project.

**Instructions:** Create a file named `dependabot.yml` inside the `.github/` directory with the following content.

```yaml
---
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "daily"
      time: "08:00"
      timezone: "America/Los_Angeles"
    labels:
      - ":game_die: dependencies"
      - ":robot: bot"
```

## 4. renovate.json

The `renovate.json` file configures Renovate Bot to automate dependency updates in your repository.

**Instructions:** Create a file named `renovate.json` inside the `.github/` directory with the following content.

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended"
  ],
  "ignoreDeps": [
    "ghcr.io/browserless/chromium"
  ],
  "docker-compose": {
    "fileMatch": [
    // Default patterns for docker-compose files
    "(^|/)(?:docker-)?compose[^/]*\.ya?ml$",
    // Add your custom pattern for .j2 files
    "^compose\.ya?ml(?:\.j2)?$"
    ]
  }
}
```

