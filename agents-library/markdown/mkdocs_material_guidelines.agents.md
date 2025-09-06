# MkDocs-Material Documentation Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying documentation for a MkDocs site using the Material theme.

## General Guidelines

- All documentation is written in Markdown and generated using MkDocs with the Material theme.
- Adhere strictly to the MkDocs-Material syntax extensions.
- Ensure all new pages are added to the `nav` section of the `mkdocs.yml` file.
- All internal links must be relative and point to other `.md` files.
- All proposed git commits must be reviewed and approved by a maintainer before being committed.
- Before implementing any significant changes or features, a detailed plan of action must be outlined and approved by a maintainer.

## Style Guide

- **Headings:** Use ATX-style headings (`#`, `##`, etc.). The main page title is always H1. All headings should start with an emoji using mkdocs-material compatible shortcodes.
- **Admonitions:** Use admonitions to highlight information (e.g., `!!! note`, `!!! warning`).
- **Icons & Emojis:** Use Material Design icons and emojis where appropriate, using shortcodes.
- **Links:** List items that are links should be enclosed with `<` and `>` if they do no use square brackets (e.g. [link][1]).
- **Hyperlinks:** All hyperlinks should reference a number at the bottom of the document.

## Sections

- All sections should have an emoji in front of the section name.
- **References:** Always end a page with a References section, a horizontal line, and the `:link:` emoji.
- **Config:** Create a config section.
- **Installation:** Create an installation section, with instructions for both amd64 and arm64 architectures.
- **Usage:** Create a usage section.
- **Upgrade:** Create an upgrade section.

## File Naming Conventions

- **Applications:** `docs/apps/app-name.md`
- **Tools:** `docs/tools/tool-name.md`
- **Hardware:** `docs/hardware/hardware-name.md`

## Content Structure

- **Front Matter:** (Optional) Includes `tags`.
- **Title:** H1 heading with an emoji and the name of the item.
- **Description:** A brief overview with a hyperlink to the official source.
- **Installation:** Instructions for installation.
- **Config:** Configuration details.
- **Usage:** Instructions and examples.
- **Upgrade:** Instructions for upgrading.
- **Troubleshooting:** (Optional) Common issues and solutions.
- **References:** A list of relevant external links.

## Integration with README.md

When a MkDocs site is used for documentation, the `README.md` file in the repository should serve as a high-level overview and a pointer to the comprehensive documentation.

- **Primary Documentation Link:** The `README.md` should prominently feature a link to the main MkDocs site URL.
- **Essential Sections:** Despite the presence of a full documentation site, the `README.md` must still include:
    - The repository title and a concise description.
    - A "TL;DR" (Too Long; Didn't Read) section providing a quick summary or quick start guide.
    - A "License" section.
    - An "About" or "Author" section.
