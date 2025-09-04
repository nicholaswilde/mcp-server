#!/usr/bin/env bash
################################################################################
#
# Script Name: scale_resource.sh
# ----------------
# Scales cloud resources up or down.
#
# @author Nicholas Wilde, 0xb299a622
# @date 04 Sep 2025
# @version 0.1.0
#
################################################################################

set -o errexit
set -o nounset
set -o pipefail

# --- Global Variables ---
CLOUD_PROVIDER=""
RESOURCE_TYPE=""
RESOURCE_NAME=""
ACTION=""
AMOUNT=""
REGION=""

# --- Functions ---

# Function to display script usage
usage() {
  echo "Usage: $0 --cloud-provider <provider> --resource-type <type> --resource-name <name> --action <scale-up|scale-down> --amount <number> [--region <region>]"
  echo "  --cloud-provider  Cloud provider (e.g., aws, azure, gcp)."
  echo "  --resource-type   Type of resource to scale (e.g., ec2-instance, container-replicas, rds-instance)."
  echo "  --resource-name   Name or identifier of the resource."
  echo "  --action          Scaling action (scale-up or scale-down)."
  echo "  --amount          The amount to scale by (e.g., number of instances, new capacity)."
  echo "  --region          (Optional) Cloud region of the resource."
  exit 1
}

# Function to parse command-line arguments
parse_args() {
  while [[ "$#" -gt 0 ]]; do
    case "$1" in
      --cloud-provider) CLOUD_PROVIDER="$2"; shift ;;
      --resource-type) RESOURCE_TYPE="$2"; shift ;;
      --resource-name) RESOURCE_NAME="$2"; shift ;;
      --action) ACTION="$2"; shift ;;
      --amount) AMOUNT="$2"; shift ;;
      --region) REGION="$2"; shift ;;
      -h|--help) usage ;;
      *) echo "Unknown parameter passed: $1"; usage ;;
    esac
    shift
  done

  # Validate required arguments
  if [[ -z "$CLOUD_PROVIDER" || -z "$RESOURCE_TYPE" || -z "$RESOURCE_NAME" || -z "$ACTION" || -z "$AMOUNT" ]]; then
    echo "Error: Missing required arguments."
    usage
  fi

  # Validate action
  case "$ACTION" in
    scale-up|scale-down) ;;
    *) echo "Error: Invalid action: $ACTION. Must be scale-up or scale-down."; usage ;;
  esac

  # Validate amount is a number
  if ! [[ "$AMOUNT" =~ ^[0-9]+$ ]]; then
    echo "Error: Amount must be a number."
    usage
  fi
}

# Function to scale AWS resources
scale_aws() {
  echo "Scaling AWS $RESOURCE_TYPE '$RESOURCE_NAME' $ACTION by $AMOUNT..."
  # Add AWS-specific scaling logic here (e.g., aws autoscaling update-auto-scaling-group, aws ecs update-service)
  echo "AWS resource scaling complete."
}

# Function to scale Azure resources
scale_azure() {
  echo "Scaling Azure $RESOURCE_TYPE '$RESOURCE_NAME' $ACTION by $AMOUNT..."
  # Add Azure-specific scaling logic here
  echo "Azure resource scaling complete."
}

# Function to scale GCP resources
scale_gcp() {
  echo "Scaling GCP $RESOURCE_TYPE '$RESOURCE_NAME' $ACTION by $AMOUNT..."
  # Add GCP-specific scaling logic here
  echo "GCP resource scaling complete."
}

# --- Main Logic ---
main() {
  parse_args "$@"

  echo "Starting resource scaling for '$RESOURCE_NAME' ($RESOURCE_TYPE) on $CLOUD_PROVIDER."

  case "$CLOUD_PROVIDER" in
    aws)
      scale_aws
      ;;
    azure)
      scale_azure
      ;;
    gcp)
      scale_gcp
      ;;
    *)
      echo "Error: Unsupported cloud provider: $CLOUD_PROVIDER"
      usage
      ;;
  esac

  echo "Resource scaling script finished."
}

main "$@"
