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
    app.server.AGENTS_LIBRARY_PATH = test_agents_library_path

    # Create a TestClient directly for the main FastAPI app
    with TestClient(app.server.app) as c:
        # Create a dummy uptime.sh script in the temporary agents-library path
        uptime_script_path = test_agents_library_path / "bash" / "uptime.sh"
        uptime_script_path.write_text("""#!/bin/bash
while [[ "$#" -gt 0 ]]; do
    case "$1" in
        --project_name) PROJECT_NAME="$2"; shift ;;
        --mcp_server_url) MCP_SERVER_URL="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done
echo "System is up! Project: ${PROJECT_NAME}, MCP Server: ${MCP_SERVER_URL}"""
)

        # Define the _run_script callable for the uptime resource
        async def _run_uptime_script(script_timeout: int = 60, **kwargs):
            try:
                command_args = ["bash", str(uptime_script_path)]
                for key, value in kwargs.items():
                    command_args.append(f"--{key}")
                    command_args.append(str(value))

                process = await asyncio.create_subprocess_exec(
                    *command_args,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=script_timeout)
                if process.returncode != 0:
                    raise Exception(f"Script execution failed: {stderr.decode().strip()}")
                return stdout.decode().strip()
            except asyncio.TimeoutError:
                process.kill()
                await process.wait()
                raise Exception(f"Script execution timed out after {script_timeout} seconds.")

        # Add the uptime resource to the mcp_server instance
        app.server.mcp_server.add_resource(
            FunctionResource(
                fn=_run_uptime_script,
                uri="resource://scripts/uptime",
                name="uptime",
                description="Executes the uptime.sh script and returns its output.",
                mime_type="text/plain",
                schema={
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "The name of the new project."},
                        "mcp_server_url": {"type": "string", "description": "The URL of the MCP server (e.g., http://localhost:8080)."},
                        "script_timeout": {"type": "integer", "description": "Timeout for script execution in seconds (default: 60).", "default": 60}
                    },
                    "required": [],
                    "additionalProperties": True
                }
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
    assert content_json == {"files": ["common_prompts", "dev_rules", "security_checks"]}

@pytest.mark.asyncio
async def test_get_uptime_script_resource(client, test_agents_library_path):
    """Test retrieving the dynamically loaded uptime script resource."""
    # Create a dummy uptime.sh script in the temporary agents-library path
    (test_agents_library_path / "bash" / "uptime.sh").write_text("#!/bin/bash\necho \"System is up!\"")

    response = client.post(
        "/test/read_resource",
        json={
            "uri": "resource://scripts/uptime",
            "args": {"project_name": "test_project", "mcp_server_url": "http://localhost:8080"}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200
    assert "System is up!" in response.json()["content"]

@pytest.mark.asyncio
async def test_get_uptime_script_resource_timeout(client, test_agents_library_path):
    """Test if the uptime script resource times out correctly."""
    # Create a dummy uptime.sh script that sleeps for a long time
    long_running_script_path = test_agents_library_path / "bash" / "long_running_uptime.sh"
    long_running_script_path.write_text('''#!/bin/bash
sleep 5
echo "Done sleeping"''')

    # Add this long-running script as a resource
    async def _run_long_running_uptime_script(script_timeout: int = 60, **kwargs):
        try:
            command_args = ["bash", str(long_running_script_path)]
            for key, value in kwargs.items():
                command_args.append(f"--{key}")
                command_args.append(str(value))

            print(f"Executing command: {' '.join(command_args)}")
            process = await asyncio.create_subprocess_exec(
                *command_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=script_timeout)
            print(f"Script stdout: {stdout.decode().strip()}")
            print(f"Script stderr: {stderr.decode().strip()}")
            if process.returncode != 0:
                raise Exception(f"Script execution failed: {stderr.decode().strip()}")
            return stdout.decode().strip()
        except asyncio.TimeoutError:
            process.kill()
            await process.wait()
            raise Exception(f"Script execution timed out after {script_timeout} seconds.")

    app.server.mcp_server.add_resource(
        FunctionResource(
            fn=_run_long_running_uptime_script,
            uri="resource://scripts/long_running_uptime",
            name="long_running_uptime",
            description="Executes a long-running uptime.sh script and returns its output.",
            mime_type="text/plain",
            schema={
                "type": "object",
                "properties": {
                    "project_name": {"type": "string", "description": "The name of the new project."},
                    "mcp_server_url": {"type": "string", "description": "The URL of the MCP server (e.g., http://localhost:8080)."},
                    "script_timeout": {"type": "integer", "description": "Timeout for script execution in seconds (default: 60).", "default": 60}
                },
                "required": [],
                "additionalProperties": True
            }
        )
    )

    response = client.post(
        "/test/read_resource",
        json={
            "uri": "resource://scripts/long_running_uptime",
            "args": {"project_name": "test_project", "mcp_server_url": "http://localhost:8080", "script_timeout": 1}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 500
    content_json = response.json()
    expected_detail_substring = "Script execution timed out after 1 seconds."
    assert expected_detail_substring in content_json["detail"]

@pytest.mark.asyncio
async def test_update_agents_file_success(client, test_agents_library_path):
    """Test updating an existing AGENTS.md file."""
    file_name = "dev_rules.agents.md"
    new_content = "## Updated Development Rules"
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "update_agents_file",
            "args": {"file_name": file_name, "new_content": new_content}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200
    assert response.json()[0][0]["text"] == f"Successfully updated '{file_name}'."

    # Verify content was actually updated in the file system
    updated_file_path = test_agents_library_path / "markdown" / file_name
    assert updated_file_path.read_text() == new_content

    # Verify content was reloaded into agents_data
    assert app.server.agents_data["dev_rules"] == new_content

@pytest.mark.asyncio
async def test_update_agents_file_create_new(client, test_agents_library_path):
    """Test creating a new AGENTS.md file."""
    file_name = "new_agent.agents.md"
    new_content = "## New Agent Instructions"
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "update_agents_file",
            "args": {"file_name": file_name, "new_content": new_content}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200
    assert response.json()[0][0]["text"] == f"Successfully updated '{file_name}'."

    # Verify new file was created in the file system
    new_file_path = test_agents_library_path / "markdown" / file_name
    assert new_file_path.read_text() == new_content

    # Verify content was loaded into agents_data
    assert app.server.agents_data["new_agent"] == new_content

@pytest.mark.asyncio
async def test_update_agents_file_invalid_extension(client):
    """Test updating a file with an invalid extension."""
    file_name = "bad_file.txt"
    new_content = "Some content"
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "update_agents_file",
            "args": {"file_name": file_name, "new_content": new_content}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 500
    content_json = response.json()
    expected_detail_substring = "Tool execution failed: Error executing tool update_agents_file: 403: File must end with '.agents.md'."
    assert expected_detail_substring in content_json["detail"]

@pytest.mark.asyncio
async def test_update_agents_file_path_traversal(client):
    """Test path traversal attempt."""
    file_name = "../../bad_location.agents.md"
    new_content = "Malicious content"
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "update_agents_file",
            "args": {"file_name": file_name, "new_content": new_content}
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 500
    content_json = response.json()
    expected_detail_substring = "Tool execution failed: Error executing tool update_agents_file: 403: Access denied: '../../bad_location.agents.md' is not in the allowed directory."
    assert expected_detail_substring in content_json["detail"]
