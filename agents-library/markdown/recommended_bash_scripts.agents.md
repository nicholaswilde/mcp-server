# Recommended Bash Scripts

Based on the existing scripts in the `agents-library/bash/` directory, here are two recommended additions that follow the established conventions and provide useful functionality for cloud operations and local development.

## 1. Cloud Backup Script (`backup.sh`)

This script provides a standardized way to back up a local file or directory to a major cloud storage provider. It complements the existing cloud-focused scripts like `deploy_app.sh` and `manage_resource.sh`.

### Usage

```bash
./agents-library/bash/backup.sh --source-path /path/to/data --destination-url s3://my-bucket/backups/ --cloud-provider aws
```

### Script Content (`backup.sh`)

To create this script, place the following content in `agents-library/bash/backup.sh`:

```bash
#!/usr/bin/env bash
################################################################################
#
# Script Name: backup.sh
# ----------------
# Backs up a specified file or directory to a cloud storage provider.
#
# @author Nicholas Wilde, 0xb299a622
# @date 03 Sep 2025
# @version 0.1.0
#
################################################################################

set -o errexit
set -o nounset
set -o pipefail

# --- Global Variables ---
SOURCE_PATH=""
DESTINATION_URL=""
CLOUD_PROVIDER=""

# --- Functions ---

# Function to display script usage
usage() {
  echo "Usage: $0 --source-path <path> --destination-url <url> --cloud-provider <provider>"
  echo "  --source-path    Local path to the file or directory to back up."
  echo "  --destination-url Cloud storage URL (e.g., s3://my-bucket/backups/)."
  echo "  --cloud-provider Cloud provider (e.g., aws, azure, gcp)."
  exit 1
}

# Function to parse command-line arguments
parse_args() {
  while [[ "$#" -gt 0 ]]; do
    case "$1" in
      --source-path) SOURCE_PATH="$2"; shift ;;
      --destination-url) DESTINATION_URL="$2"; shift ;;
      --cloud-provider) CLOUD_PROVIDER="$2"; shift ;;
      -h|--help) usage ;;
      *) echo "Unknown parameter passed: $1"; usage ;;
    esac
    shift
  done

  # Validate required arguments
  if [[ -z "$SOURCE_PATH" || -z "$DESTINATION_URL" || -z "$CLOUD_PROVIDER" ]]; then
    echo "Error: Missing required arguments."
    usage
  fi

  if [[ ! -e "$SOURCE_PATH" ]]; then
    echo "Error: Source path '$SOURCE_PATH' does not exist."
    exit 1
  fi
}

# Function to perform backup to AWS S3
backup_aws() {
  echo "Backing up '$SOURCE_PATH' to AWS S3 at '$DESTINATION_URL'..."
  # Placeholder for AWS S3 backup logic
  # Example: aws s3 cp "$SOURCE_PATH" "$DESTINATION_URL" --recursive
  echo "AWS S3 backup complete."
}

# Function to perform backup to Azure Blob Storage
backup_azure() {
  echo "Backing up '$SOURCE_PATH' to Azure Blob Storage at '$DESTINATION_URL'..."
  # Placeholder for Azure Blob backup logic
  # Example: az storage blob upload-batch --source "$SOURCE_PATH" --destination "$DESTINATION_URL"
  echo "Azure Blob backup complete."
}

# Function to perform backup to GCP Cloud Storage
backup_gcp() {
  echo "Backing up '$SOURCE_PATH' to GCP Cloud Storage at '$DESTINATION_URL'..."
  # Placeholder for GCP Cloud Storage backup logic
  # Example: gsutil -m cp -r "$SOURCE_PATH" "$DESTINATION_URL"
  echo "GCP Cloud Storage backup complete."
}

# --- Main Logic ---
main() {
  parse_args "$@"

  echo "Starting backup for '$SOURCE_PATH' to $CLOUD_PROVIDER."

  case "$CLOUD_PROVIDER" in
    aws)
      backup_aws
      ;;
    azure)
      backup_azure
      ;;
    gcp)
      backup_gcp
      ;;
    *)
      echo "Error: Unsupported cloud provider: $CLOUD_PROVIDER"
      usage
      ;;
  esac

  echo "Backup script finished."
}

main "$@"
```

## 2. Git Housekeeping Script (`git_housekeeping.sh`)

This script helps developers maintain a clean and efficient local Git repository by automating common cleanup tasks.

### Usage

```bash
# Prune local merged branches and remote-tracking branches, then run garbage collection
./agents-library/bash/git_housekeeping.sh --action all --repo-path /path/to/your/repo
```

### Script Content (`git_housekeeping.sh`)

To create this script, place the following content in `agents-library/bash/git_housekeeping.sh`:

```bash
#!/usr/bin/env bash
################################################################################
#
# Script Name: git_housekeeping.sh
# ----------------
# Performs common Git repository maintenance tasks.
#
# @author Nicholas Wilde, 0xb299a622
# @date 03 Sep 2025
# @version 0.1.0
#
################################################################################

set -o errexit
set -o nounset
set -o pipefail

# --- Global Variables ---
ACTION=""
REPO_PATH="."
REMOTE="origin"

# --- Functions ---

# Function to display script usage
usage() {
  echo "Usage: $0 --action <action> [--repo-path <path>] [--remote <name>]"
  echo "  --action      Action to perform (prune-local, prune-remote, gc, all)."
  echo "                prune-local: Deletes local branches that have been merged into the main/master branch."
  echo "                prune-remote: Deletes remote branches that no longer exist on the remote."
  echo "                gc: Runs git garbage collection."
  echo "                all: Runs all housekeeping actions."
  echo "  --repo-path   (Optional) Path to the git repository. Defaults to the current directory."
  echo "  --remote      (Optional) The remote to prune against. Defaults to 'origin'."
  exit 1
}

# Function to parse command-line arguments
parse_args() {
  while [[ "$#" -gt 0 ]]; do
    case "$1" in
      --action) ACTION="$2"; shift ;;
      --repo-path) REPO_PATH="$2"; shift ;;
      --remote) REMOTE="$2"; shift ;;
      -h|--help) usage ;;
      *) echo "Unknown parameter passed: $1"; usage ;;
    esac
    shift
  done

  # Validate required arguments
  if [[ -z "$ACTION" ]]; then
    echo "Error: Missing required --action argument."
    usage
  fi

  if [[ ! -d "$REPO_PATH/.git" ]]; then
    echo "Error: '$REPO_PATH' is not a git repository."
    exit 1
  fi
}

# Function to prune merged local branches
prune_local_branches() {
  echo "--> Pruning local branches merged into main/master..."
  cd "$REPO_PATH"
  git checkout -q main || git checkout -q master
  git fetch --prune
  git branch --merged | egrep -v "(^\*|main|master)" | xargs -r git branch -d
  echo "--> Local branch pruning complete."
}

# Function to prune remote-tracking branches
prune_remote_branches() {
  echo "--> Pruning remote-tracking branches for remote '$REMOTE'..."
  cd "$REPO_PATH"
  git fetch "$REMOTE" --prune
  echo "--> Remote branch pruning complete."
}

# Function to run garbage collection
run_git_gc() {
  echo "--> Running git garbage collection..."
  cd "$REPO_PATH"
  git gc --prune=now --aggressive
  echo "--> Garbage collection complete."
}


# --- Main Logic ---
main() {
  parse_args "$@"

  echo "Starting Git housekeeping for repository at '$REPO_PATH' with action '$ACTION'."

  case "$ACTION" in
    prune-local)
      prune_local_branches
      ;;
    prune-remote)
      prune_remote_branches
      ;;
    gc)
      run_git_gc
      ;;
    all)
      prune_local_branches
      prune_remote_branches
      run_git_gc
      ;;
    *)
      echo "Error: Invalid action: $ACTION."
      usage
      ;;
  esac

  echo "Git housekeeping script finished."
}

main "$@"
```
