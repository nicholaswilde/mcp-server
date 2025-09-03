#!/usr/bin/env bash
################################################################################
#
# Script Name: list_markdown_files.sh
# ----------------
# Lists all markdown files in the agents-library/markdown/ directory.
#
# @author Nicholas Wilde, 0xb299a622
# @date 03 Sep 2025
# @version 0.1.0
#
################################################################################

set -o errexit
set -o nounset
set -o pipefail

MARKDOWN_DIR="$(dirname "$0")"/../markdown

echo "Markdown files in $MARKDOWN_DIR:"
find "$MARKDOWN_DIR" -maxdepth 1 -type f -name "*.md" -printf "%f\n" | sort
