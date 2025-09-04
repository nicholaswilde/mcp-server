# :material-book: MkDocs-Material Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying documentation for MkDocs-Material.

## :material-format-text: General Guidelines

- All documentation is written in Markdown and generated using MkDocs with the Material theme.
- Include badges for build status and CI/test workflows (if they exist), using the 'for-the-badge' style from shields.io.
- Adhere strictly to the MkDocs-Material syntax extensions.
- Ensure all new pages are added to the `nav` section of the `mkdocs.yml` file.
- All internal links must be relative and point to other `.md` files.
- Do not use first-person or third-person perspective.

## :material-palette: Style Guide

- **Headings:** Use ATX-style headings (`#`, `##`, etc.). The main page title is always H1. All headings should start with an emoji using mkdocs-material compatible shortcodes (e.g., `:material-lightbulb:`).
- **Admonitions:** Use admonitions to highlight information (e.g., `!!! note`, `!!! warning`).
- **Code Blocks:** Always specify the language for syntax highlighting.
- **Lists:** Use hyphens for unordered lists and numbers for ordered lists.
- **Icons & Emojis:** Use Material Design icons and emojis where appropriate, using shortcodes (e.g., `:material-check:`).
- **Indentation:** Use 2 spaces for indentation.
- **Links:** List items that are links should be enclosed with `<` and `>` if they do no use square brackets (e.g. [link][1]).
- **Linting:** Formatting shall be compatible with markdownlint.
- **Hyperlinks:** All hyperlinks should reference a number at the bottom of the document.

## :material-graph: Sections

- All sections should have an emoji in front of the section name.
- **References:** Always end a page with a References section, starting with the `:material-link:` emoji.
- **Config:** Create a config section.
- **Installation:** Create an installation section, with instructions for both amd64 and arm64 architectures.
- **Usage:** Create a usage section.
- **Upgrade:** Create an upgrade section.

## :material-file-document: File Naming Conventions

- **Applications:** `docs/apps/app-name.md`
- **Tools:** `docs/tools/tool-name.md`
- **Hardware:** `docs/hardware/hardware-name.md`

## :material-format-list-bulleted: Content Structure

- **Front Matter:** (Optional) Includes `tags`.
- **Title:** H1 heading with an emoji and the name of the item.
- **Description:** A brief overview with a hyperlink to the official source.
- **Installation:** Instructions for installation.
- **Config:** Configuration details.
- **Usage:** Instructions and examples.
- **Upgrade:** Instructions for upgrading.
- **Troubleshooting:** (Optional) Common issues and solutions.
- **References:** A list of relevant external links.
