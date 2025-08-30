# Markdown Documentation Guidelines

As an AI assistant, I will adhere to the following guidelines when creating or modifying markdown documentation.

## General Guidelines

- Use clear and descriptive headings.
- Employ bullet points and numbered lists for readability.
- Use backticks for inline code and triple backticks for code blocks, specifying the language.
- Keep paragraphs concise.
- Link to relevant files or sections using relative paths.
- Ensure a consistent and instructional tone.
- Favor simple Markdown over complex HTML.
- All documentation is written in Markdown and generated using MkDocs with the Material theme.
- Adhere strictly to the MkDocs-Material syntax extensions.
- Ensure all new pages are added to the `nav` section of the `mkdocs.yml` file.
- All internal links must be relative and point to other `.md` files.
- Do not use first-person or third-person perspective.

## Style Guide

- **Headings:** Use ATX-style headings (`#`, `##`, etc.). The main page title is always H1. All headings should start with an emoji using mkdocs-material compatible shortcodes.
- **Admonitions:** Use admonitions to highlight information (e.g., `!!! note`, `!!! warning`).
- **Code Blocks:** Always specify the language for syntax highlighting.
- **Lists:** Use hyphens for unordered lists and numbers for ordered lists.
- **Icons & Emojis:** Use Material Design icons and emojis where appropriate, using shortcodes.
- **Indentation:** Use 2 spaces for indentation.
- **Links:** List items that are links should be enclosed with `<` and `>`.
- **Linting:** Formatting shall be compatible with markdownlint.
- **Hyperlinks:** All hyperlinks should reference a number at the bottom of the document.

## Sections

- All sections should have an emoji in front of the section name.
- **References:** Always end a page with a References section, starting with the `:link:` emoji.
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
