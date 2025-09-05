import asyncio
import importlib
import json
import os
from http import HTTPStatus
from pathlib import Path
from typing import Any, Generator

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from mcp.server.fastmcp.resources import FunctionResource

# Import the app.server module directly
import app.server


@pytest.fixture(scope="module")
def test_agents_library_path(tmp_path_factory: Any) -> Path:
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

    # Create dummy bash scripts
    (bash_dir / "uptime.sh").write_text('#!/bin/bash\necho "System is up!"')
    (bash_dir / "long_running_uptime.sh").write_text(
        '#!/bin/bash\nsleep 5\necho "Done sleeping"'
    )

    # Set the environment variable for the test session
    os.environ["AGENTS_LIBRARY_PATH"] = str(temp_dir)
    yield temp_dir
    # Clean up the environment variable after tests
    del os.environ["AGENTS_LIBRARY_PATH"]




@pytest.fixture
def client(test_agents_library_path: Path, monkeypatch: Any) -> Generator[TestClient, None, None]:
    """Provides a TestClient for the FastAPI app with security disabled."""
    monkeypatch.setattr(app.server, "AGENTS_LIBRARY_PATH", test_agents_library_path)
    monkeypatch.setattr(app.server, "SECURITY_ENABLED", False)
    monkeypatch.setattr(app.server, "API_KEYS", [])
    
    app.server.agents_data.clear()
    
    with TestClient(app.server.create_app()) as c:
        yield c


@pytest.fixture
def secure_client(test_agents_library_path: Path, monkeypatch: Any) -> Generator[TestClient, None, None]:
    """Provides a TestClient for the FastAPI app with security enabled."""
    monkeypatch.setattr(app.server, "AGENTS_LIBRARY_PATH", test_agents_library_path)
    monkeypatch.setattr(app.server, "SECURITY_ENABLED", True)
    monkeypatch.setattr(app.server, "API_KEYS", ["test-key"])

    app.server.agents_data.clear()

    with TestClient(app.server.create_app()) as c:
        yield c






# Security disabled tests
def test_health_check_security_disabled(client: TestClient) -> None:
    """Test health check endpoint with security disabled."""
    response = client.get("/health")
    assert response.status_code == HTTPStatus.OK.value
    assert response.json() == {"status": "ok"}

def test_call_tool_security_disabled(client: TestClient) -> None:
    """Test calling a tool with security disabled."""
    response = client.post(
        "/test/call_tool",
        json={"tool_name": "list_agents_instructions", "args": {}},
    )
    assert response.status_code == HTTPStatus.OK.value

def test_call_tool_security_disabled_no_api_key(client: TestClient) -> None:
    """Test calling a tool with security disabled and no API key provided."""
    response = client.post(
        "/test/call_tool",
        json={"tool_name": "list_agents_instructions", "args": {}},
    )
    assert response.status_code == HTTPStatus.OK.value


# Security enabled tests
def test_health_check_security_enabled(secure_client: TestClient) -> None:
    """Test health check endpoint with security enabled (should not require a key)."""
    response = secure_client.get("/health")
    assert response.status_code == HTTPStatus.OK.value
    assert response.json() == {"status": "ok"}

def test_call_tool_with_valid_key(secure_client: TestClient) -> None:
    """Test calling a tool with a valid API key."""
    response = secure_client.post(
        "/test/call_tool",
        json={"tool_name": "list_agents_instructions", "args": {}},
        headers={"X-API-Key": "test-key"},
    )
    assert response.status_code == HTTPStatus.OK.value

def test_call_tool_with_invalid_key(secure_client: TestClient) -> None:
    """Test calling a tool with an invalid API key."""
    response = secure_client.post(
        "/test/call_tool",
        json={"tool_name": "list_agents_instructions", "args": {}},
        headers={"X-API-Key": "invalid-key"},
    )
    assert response.status_code == HTTPStatus.FORBIDDEN.value
    assert response.json() == {"detail": "Invalid or missing API key"}

def test_call_tool_with_missing_key(secure_client: TestClient) -> None:
    """Test calling a tool with a missing API key."""
    response = secure_client.post(
        "/test/call_tool",
        json={"tool_name": "list_agents_instructions", "args": {}},
    )
    assert response.status_code == HTTPStatus.FORBIDDEN.value
    assert response.json() == {"detail": "Invalid or missing API key"}


@pytest.mark.asyncio
async def test_get_agents_instructions_success(client: TestClient) -> None:
    """Test retrieving an existing AGENTS.md file via MCP tool invocation."""
    response = client.post(
        "/test/call_tool",
        json={"tool_name": "get_agents_instructions", "args": {"name": "dev_rules"}},
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert response.status_code == HTTPStatus.OK.value


@pytest.mark.asyncio
async def test_get_agents_instructions_not_found(client: TestClient) -> None:
    """Test retrieving a non-existent AGENTS.md file via MCP tool invocation."""
    response = client.post(
        "/test/call_tool",
        json={"tool_name": "get_agents_instructions", "args": {"name": "non_existent"}},
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR.value
    content_json = response.json()
    expected_detail_substring = (
        "Tool execution failed: Error executing tool get_agents_instructions: "
        "404: AGENTS.md file 'non_existent' not found."
    )
    assert expected_detail_substring in content_json["detail"]


@pytest.mark.asyncio
async def test_list_agents_instructions(client: TestClient) -> None:
    """Test listing all available AGENTS.md files via MCP tool invocation."""
    response = client.post(
        "/test/call_tool",
        json={"tool_name": "list_agents_instructions", "args": {}},
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert response.status_code == HTTPStatus.OK.value
    content_json = json.loads(response.json()[0][0]["text"])
    assert content_json == {"files": ["common_prompts", "dev_rules", "security_checks"]}





@pytest.mark.asyncio
@pytest.mark.usefixtures("test_agents_library_path")
async def test_update_agents_file_success(client: TestClient) -> None:
    """Test updating an existing AGENTS.md file."""
    file_name = "dev_rules.agents.md"
    new_content = "## Updated Development Rules"
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "update_agents_file",
            "args": {"file_name": file_name, "new_content": new_content},
        },
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert response.status_code == HTTPStatus.OK.value


@pytest.mark.asyncio
async def test_update_agents_file_create_new(client: TestClient, test_agents_library_path: Path) -> None:
    """Test creating a new AGENTS.md file."""
    file_name = "new_agent.agents.md"
    new_content = "## New Agent Instructions"
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "update_agents_file",
            "args": {"file_name": file_name, "new_content": new_content},
        },
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert response.status_code == HTTPStatus.OK.value
    assert response.json()[0][0]["text"] == f"Successfully updated '{file_name}'."

    # Verify new file was created in the file system
    new_file_path = test_agents_library_path / "markdown" / file_name
    assert new_file_path.read_text() == new_content

    # Verify content was loaded into agents_data
    assert app.server.agents_data["new_agent"] == new_content


@pytest.mark.asyncio
async def test_update_agents_file_invalid_extension(client: TestClient) -> None:
    """Test updating a file with an invalid extension."""
    file_name = "bad_file.txt"
    new_content = "Some content"
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "update_agents_file",
            "args": {"file_name": file_name, "new_content": new_content},
        },
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR.value
    content_json = response.json()
    expected_detail_substring = (
        "Tool execution failed: Error executing tool update_agents_file: "
        "403: File must end with '.agents.md'."
    )
    assert expected_detail_substring in content_json["detail"]


@pytest.mark.asyncio
async def test_update_agents_file_path_traversal(client: TestClient) -> None:
    """Test path traversal attempt."""
    file_name = "../../bad_location.agents.md"
    new_content = "Malicious content"
    response = client.post(
        "/test/call_tool",
        json={
            "tool_name": "update_agents_file",
            "args": {"file_name": file_name, "new_content": new_content},
        },
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR.value
    content_json = response.json()
    expected_detail_substring = (
        "Tool execution failed: Error executing tool update_agents_file: "
        "403: Access denied: '../../bad_location.agents.md' is not in the allowed "
        "directory."
    )
    assert expected_detail_substring in content_json["detail"]
