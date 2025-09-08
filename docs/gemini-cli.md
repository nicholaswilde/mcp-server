# :gemini: Adding to gemini-cli

To add this server to `gemini-cli`, you need to edit your `settings.json` file. You can find this file in `~/.gemini/settings.json` (user settings) or in `.gemini/settings.json` (project settings).

Add the following to your `settings.json` file:

```json
{
  "mcpServers": {
    "sharedAgents": {
      "httpUrl": "http://<ip-address>:8080"
    }
  }
}
```

## :tools: Using the `mcp` tool

Once the `mcp-server` is configured in `gemini-cli`, you can use the `mcp` tool to interact with the server. For example, to list all available agent instructions:

**Prompt**

```bash
/mcp list
```

**Output**

```bash
  🟢 sharedAgents - Ready (2 tools)
    Tools:
    - get_agents_instructions
    - list_agents_instructions
```

**Prompt**

```bash
list_agents_instructions
```

**Output**

```
✔ list_agents_instructions (sharedAgents MCP Server) list_agents_instructions (sharedAgents MCP Server)

   {
     "files": [
       "frame_fi",
       "git",
       "security_checks",
       "dev_rules",
       "common_prompts",
       "homelab_docs"
     ]
   }
```

**Prompt**

```bash
get_agents_instructions common_prompts
```

**Output**

```
✦ I have retrieved the "common_prompts" instructions. It contains guidelines for creating Markdown
  documentation and for scripting in Bash and Python.
```

Example `gemini-cli` prompt to use the `common_prompts` agent to create a bash script.

```bash
using the get_agents_instructions common_prompts agent, write me a bash script that checks
downloads the latest release of sops from GitHub with architecture amd64 and linux.
```

!!! tip

    It's important to add the `get_agents_instructions` to the prompt so that `gemini-cli` knows which tool to use to retrieve the remote agent.

Instead of explictly stating to use the mcp agent in every prompt, instruct `gemini-cli` to use the MCP server's prompts by adding the following to the project's `AGENTS.md` file.

```markdown
# Agent Instructions

## Agent Rules

## Ansible Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `ansible_guidelines` agent when creating or modifying Ansible playbooks, roles, and inventories.

## Cloud Best Practices Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `cloud_best_practices` agent when discussing cloud best practices.

## Common Prompts Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `common_prompts` agent for general prompting guidelines.

## Dev Rules Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `dev_rules` agent when discussing development rules.

## Dockerfile Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `dockerfile_guidelines` agent when creating or modifying Dockerfiles.



## Git Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `git` agent for git-related queries.

## Frame.fi Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `frame_fi` agent for Frame.fi related queries.

## GitHub Repo Config Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `github_repo_config` agent when configuring GitHub repositories.

## Homelab Docs Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `homelab_docs` agent for homelab documentation.

## .env and SOPS Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `env_sops_guidelines` agent when working with `.env` files and SOPS encryption.

## MkDocs-Material Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `mkdocs_material_guidelines` agent when creating or modifying MkDocs-Material documentation.

## README.md Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `readme_guidelines` agent when creating or modifying `README.md` files.

## MkDocs Site Creation Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `mkdocs_site_creation` agent when creating MkDocs sites.

## Platform.io Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `platformio_guidelines` agent when creating or modifying Platform.io projects.

## Recommended Bash Scripts Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `recommended_bash_scripts` agent when recommending bash scripts.

## Bash Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `bash_guidelines` agent when discussing bash scripting guidelines.

## Python Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `python_guidelines` agent when discussing python scripting guidelines.

## Security Checks Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `security_checks` agent when performing security checks.

## SOPS Config Creation Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `sops_config_creation` agent when configuring SOPS.

## Taskfile Creation Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `taskfile_creation` agent when creating Taskfiles.

## Terraform Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `terraform_guidelines` agent when discussing Terraform guidelines.

## YAML Guidelines Agent Rules

- **ALWAYS** use the `sharedAgents` MCP server's `get_agents_instructions` `yaml_guidelines` agent when creating or modifying YAML files.