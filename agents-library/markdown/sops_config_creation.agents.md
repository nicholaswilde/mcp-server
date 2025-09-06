# SOPS Configuration File Creation

This document provides instructions for creating a `.sops.yaml` configuration file for use with SOPS (Secrets OPerationS).

## .sops.yaml

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
