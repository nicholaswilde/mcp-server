# MkDocs-Material Site Creation Guidelines

This document provides instructions for creating a new documentation site within this repository using MkDocs-Material. It leverages configurations from an existing `mkdocs.yml` to ensure consistency.

## 1. Prerequisites

Ensure you have `mkdocs` and `mkdocs-material` installed. If not, you can install them using pip:

```bash
pip install mkdocs mkdocs-material
```

## 2. Basic Site Setup

To create a new MkDocs project, navigate to the desired location within the repository (e.g., `docs/new-site/`) and run:

```bash
mkdocs new .
```

This will create an `mkdocs.yml` configuration file and a `docs` directory with an `index.md` file.

## 3. Configuration Details

Update the `mkdocs.yml` file with the following configurations, adapting `site_name`, `site_description`, `site_url`, etc., to your new site's specifics. The following sections are derived from `https://github.com/nicholaswilde/homelab/raw/refs/heads/main/mkdocs.yml`:

```yaml
site_name: Your New Site Name
site_description: A brief description of your new site
site_author: Your Name
site_url: https://your-new-site-url.com
copyright: Copyright © 2025 Your Name

# Repository (Update these to reflect this repository)
repo_name: nicholaswilde/mcp-server
repo_url: https://github.com/nicholaswilde/mcp-server
edit_uri: "edit/main/docs/your-new-site/"

extra_css:
  - stylesheets/extra.css

extra:
  social:
    - icon: fontawesome/solid/house
      link: https://nicholaswilde.io/
    - icon: fontawesome/brands/github
      link: https://github.com/nicholaswilde
    - icon: fontawesome/brands/twitter
      link: https://twitter.com/nicholascwilde
    - icon: fontawesome/brands/instagram
      link: https://www.instagram.com/wildewoodworking/
    - icon: fontawesome/brands/linkedin-in
      link: https://www.linkedin.com/in/nicholaswilde
    - icon: fontawesome/brands/facebook
      link: https://www.facebook.com/nicholas.wilde/
    - icon: fontawesome/brands/keybase
      link: https://keybase.io/nicholaswilde
    - icon: fontawesome/solid/key
      link: https://github.com/nicholaswilde.gpg

theme:
  name: material
  language: en
  icon:
    repo: fontawesome/brands/github
    logo: fontawesome/solid/house-chimney
  features:
    - navigation.top
    - navigation.tracking
    - navigation.footer
    - content.code.copy
    - content.action.edit
    - content.action.view
  palette:
    - media: "(prefers-color-scheme)"
      toggle:
        icon: material/brightness-auto
        name: Switch to light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle:
        icon: material/toggle-switch-off-outline
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/toggle-switch
        name: Switch to light mode

plugins:
  - search
  - tags
  - minify:
      minify_html: true

markdown_extensions:
  - admonition
  - abbr
  - attr_list
  - def_list
  - footnotes
  - meta
  - tables
  - md_in_html
  - toc:
      permalink: true
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.critic
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.magiclink:
      repo_url_shorthand: true
      user: nicholaswilde
      repo: homepage
  - pymdownx.mark
  - pymdownx.snippets:
      base_path:
        - ./pve
        - ./docker
        - ./vm
        - ./docs
  - pymdownx.smartsymbols
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde
```

## 4. Content Creation

Create your markdown files within the `docs` directory of your new site. Update the `nav` section in your `mkdocs.yml` to define the navigation structure of your site.

## 5. Building and Serving

To build your site, navigate to your new site's root directory (where `mkdocs.yml` is located) and run:

```bash
mkdocs build
```

To serve your site locally for development, use:

```bash
mkdocs serve
```

This will typically serve the site at `http://127.0.0.1:8000`.
