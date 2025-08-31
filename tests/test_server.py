import os
import pytest
from fastapi.testclient import TestClient
from pathlib import Path
import importlib
import json
import asyncio
import subprocess
from mcp.server.fastmcp.resources import FunctionResource

# Import the app.server module directly
import app.server

@pytest.fixture(scope="module")
def test_agents_library_path(tmp_path_factory):
    """Creates a temporary directory for AGENTS_LIBRARY_PATH and populates it with dummy files."""
    temp_dir = tmp_path_factory.mktemp("agents_library")
    markdown_dir = temp_dir / "markdown"
    markdown_dir.mkdir()
    bash_dir = temp_dir / "bash"
    bash_dir.mkdir()

    # Create dummy AGENTS.md files
    (markdown_dir / "dev_rules.agents.md").write_text("## Development Rules")
    (markdown_dir / "security_checks.agents.md").write_text("## Security Checks")
    (markdown_dir / "common_prompts.agents.md").write_text("## Common Prompts")

    # Set the environment variable for the test session
    os.environ["AGENTS_LIBRARY_PATH"] = str(temp_dir)
    yield temp_dir
    # Clean up the environment variable after tests
    del os.environ["AGENTS_LIBRARY_PATH"]

@pytest.fixture(scope="module")
def client(test_agents_library_path):
    """Provides a TestClient for the FastAPI app."""
    # Clear agents_data before each test run to ensure a clean state
    app.server.agents_data.clear()

    # Reload app.server to ensure the environment variable is picked up
    # test_agents_library_path already sets os.environ["AGENTS_LIBRARY_PATH"]
    importlib.reload(app.server)

    # Create a TestClient directly for the main FastAPI app
    with TestClient(app.server.app) as c:
        # Create a dummy uptime.sh script in the temporary agents-library path
        uptime_script_path = test_agents_library_path / "bash" / "uptime.sh"
        uptime_script_path.write_text("#!/bin/bash\necho \"System is up!\"")

        # Define the _run_script callable for the uptime resource
        async def _run_uptime_script():
            process = await asyncio.create_subprocess_exec(
                "bash", str(uptime_script_path),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            if process.returncode != 0:
                raise Exception(f"Script execution failed: {stderr.decode().strip()}")
            return stdout.decode().strip()

        # Add the uptime resource to the mcp_server instance
        app.server.mcp_server.add_resource(
            FunctionResource(
                fn=_run_uptime_script,
                uri="resource://scripts/uptime",
                name="uptime",
                description="Executes the uptime.sh script and returns its output.",
                mime_type="text/plain"
            )
        )
        yield c

@pytest.mark.asyncio
async def test_load_agents_data(test_agents_library_path):
    """Test if AGENTS.md files are loaded correctly."""
    app.server.agents_data.clear() # Clear any previous data
    # Pass the path directly to load_agents_data for direct testing
    await app.server.load_agents_data(test_agents_library_path)
    assert "dev_rules" in app.server.agents_data
    assert "security_checks" in app.server.agents_data
    assert "common_prompts" in app.server.agents_data
    assert app.server.agents_data["dev_rules"] == "## Development Rules"

@pytest.mark.asyncio
async def test_get_agents_instructions_success(client):
    """Test retrieving an existing AGENTS.md file via MCP tool invocation."""
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "get_agents_instructions",
            "args": {"name": "dev_rules"}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200
    content_json = json.loads(response.json()[0][0]["text"])
    assert content_json == {"content": "## Development Rules", "content_type": "text/markdown"}

@pytest.mark.asyncio
async def test_get_agents_instructions_not_found(client):
    """Test retrieving a non-existent AGENTS.md file via MCP tool invocation."""
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "get_agents_instructions",
            "args": {"name": "non_existent"}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 500
    content_json = response.json()
    expected_detail_substring = "Tool execution failed: Error executing tool get_agents_instructions: 404: AGENTS.md file 'non_existent' not found."
    assert expected_detail_substring in content_json["detail"]

@pytest.mark.asyncio
async def test_list_agents_instructions(client):
    """Test listing all available AGENTS.md files via MCP tool invocation."""
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "list_agents_instructions",
            "args": {}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200
    content_json = json.loads(response.json()[0][0]["text"])
    assert content_json == {"files": ["common_prompts", "security_checks", "dev_rules"]}

@pytest.mark.asyncio
async def test_get_uptime_script_resource(client, test_agents_library_path):
    """Test retrieving the dynamically loaded uptime script resource."""
    # Create a dummy uptime.sh script in the temporary agents-library path
    (test_agents_library_path / "bash" / "uptime.sh").write_text("#!/bin/bash\necho \"System is up!\"")

    response = client.post(
        "/test/read_resource",
        json={
            "uri": "resource://scripts/uptime"
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200
    assert "System is up!" in response.json()["content"]
