import asyncio
import os
import subprocess
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
import yaml
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from mcp.server import FastMCP
from mcp.server.fastmcp.exceptions import ResourceError, ToolError
from mcp.server.fastmcp.resources import FunctionResource
from pydantic import BaseModel


# Configuration
def load_config():
    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)

    # Override config with environment variables
    def _override_config_with_env(current_config, prefix=""):
        for key, value in current_config.items():
            env_var_name = f"{prefix}{key}".upper()
            if isinstance(value, dict):
                _override_config_with_env(value, f"{env_var_name}_")
            elif env_var_name in os.environ:
                # Attempt to convert environment variable to the same type as the config value
                try:
                    if isinstance(value, int):
                        current_config[key] = int(os.environ[env_var_name])
                    elif isinstance(value, bool):
                        current_config[key] = os.environ[env_var_name].lower() in ('true', '1', 't', 'y', 'yes')
                    else:
                        current_config[key] = os.environ[env_var_name]
                except ValueError:
                    print(f"Warning: Could not convert environment variable {env_var_name} to type of {key}. Using default.")
        return current_config

    return _override_config_with_env(cfg)

config = load_config()
SERVER_PORT = int(config["server"]["port"])
AGENTS_LIBRARY_PATH = Path(config["server"]["agents_library_path"])

# Initialize the FastAPI app and the MCP server
mcp_server = FastMCP(
    name=config["mcp_server"]["name"],
    streamable_http_path=config["mcp_server"]["streamable_http_path"],
    json_response=config["mcp_server"]["json_response"],
)

# A dictionary to store the contents of our AGENTS.md files
agents_data: dict[str, str] = {}

async def load_agents_data(agents_library_path: Path):
    """Loads all AGENTS.md files into memory."""
    if not agents_library_path.is_dir():
        print(f"Directory not found: {agents_library_path}")
        return

    for file_path in agents_library_path.glob("markdown/*.agents.md"):
        try:
            content = file_path.read_text(encoding="utf-8")
            # Use the filename (without extension) as the tool name
            tool_name = file_path.stem.replace(".agents", "")
            agents_data[tool_name] = content
            print(f"Loaded AGENTS.md file: {file_path.name} as tool '{tool_name}'")
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

async def load_bash_scripts(agents_library_path: Path):
    """Loads all .sh files as resources."""
    if not agents_library_path.is_dir():
        print(f"Directory not found: {agents_library_path}")
        return

    def create_run_script_callable(script_path: Path):
        async def _run_script(script_timeout: int = 60, **kwargs):
            try:
                command_args = ["bash", str(script_path)]
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
                    print(f"Error running script {script_path.name}: {stderr.decode().strip()}")
                    raise HTTPException(status_code=500, detail=f"Script execution failed: {stderr.decode().strip()}")
                return stdout.decode().strip()
            except TimeoutError:
                process.kill()
                await process.wait()
                print(f"Error running script {script_path.name}: Timeout after {script_timeout} seconds.")
                raise HTTPException(status_code=500, detail=f"Script execution timed out after {script_timeout} seconds.")
        return _run_script

    for file_path in agents_library_path.glob("bash/*.sh"):
        try:
            script_name = file_path.stem
            resource_uri = f"resource://scripts/{script_name}"

            mcp_server.add_resource(
                FunctionResource(
                    fn=create_run_script_callable(file_path),
                    uri=resource_uri,
                    name=script_name,
                    description=f"Executes the {script_name}.sh script and returns its output.",
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
            print(f"Loaded bash script: {file_path.name} as resource '{resource_uri}'")
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Context manager for managing the lifespan of the FastAPI application.
    Handles startup and shutdown events.
    """
    # Get AGENTS_LIBRARY_PATH from environment variable during lifespan startup
    agents_library_path = Path(os.environ.get("AGENTS_LIBRARY_PATH", "/app/agents-library"))
    await load_agents_data(agents_library_path)
    await load_bash_scripts(agents_library_path)
    mcp_app = mcp_server.streamable_http_app()
    async with mcp_server.session_manager.run():
        app.mount("/", mcp_app)
        print("MCP server started and ready to serve.")
        yield
    # Clean up / shutdown events can go here if needed

app = FastAPI(lifespan=lifespan)

@app.exception_handler(ToolError)
async def tool_error_handler(request: Request, exc: ToolError):
    return JSONResponse(
        status_code=500,
        content={
            "detail": f"Tool execution failed: {exc}"
        },
    )

class ToolCallRequest(BaseModel):
    tool_name: str
    args: dict

class ResourceReadRequest(BaseModel):
    uri: str

# Temporary test endpoints for direct tool/resource invocation
@app.post("/test/call_tool")
async def test_call_tool(request: ToolCallRequest):
    return await mcp_server.call_tool(request.tool_name, request.args)

@app.get("/health")
async def health_check():
    """Health check endpoint.
    """
    return {"status": "ok"}


@app.post("/test/read_resource")
async def test_read_resource(request: ResourceReadRequest):
    try:
        # The read_resource returns an Iterable[ReadResourceContents]
        # For testing, we'll just get the first item's content
        contents = await mcp_server.read_resource(request.uri)
        if contents:
            # Assuming content is text for simplicity in testing
            return {"content": contents[0].content, "mime_type": contents[0].mime_type}
        raise HTTPException(status_code=404, detail="Resource content not found.")
    except ResourceError as e:
        raise HTTPException(status_code=500, detail=f"Resource error: {e}")

@mcp_server.tool(
    name="get_agents_instructions",
    description="Retrieves a specific AGENTS.md file for providing AI with instructions and context."
)
async def get_agents_instructions(name: str) -> dict[str, str]:
    """Handler to return the content of a requested AGENTS.md file.
    """
    if name in agents_data:
        return {
            "content": agents_data[name],
            "content_type": "text/markdown"
        }
    raise HTTPException(status_code=404, detail=f"AGENTS.md file '{name}' not found.")

@mcp_server.tool(
    name="list_agents_instructions",
    description="Lists all available AGENTS.md files."
)
async def list_agents_instructions() -> dict[str, list]:
    """Handler to list all available AGENTS.md files.
    """
    return {"files": sorted(list(agents_data.keys()))}

@mcp_server.tool(
    name="update_agents_file",
    description="Updates the content of a specific AGENTS.md file in the agents-library."
)
async def update_agents_file(file_name: str, new_content: str) -> str:
    """Handler to update a markdown file in the agents-library.

    Args:
        file_name: The name of the file to update (e.g., 'common_prompts').
        new_content: The new content to write to the file.
    """
    # Security check: Ensure the file has the correct extension
    if not file_name.endswith(".agents.md"):
        raise HTTPException(
            status_code=403,
            detail="File must end with '.agents.md'."
        )

    # Define the base directory for agents and ensure the file is in the markdown subdirectory
    target_dir = AGENTS_LIBRARY_PATH / "markdown"

    # Resolve the absolute path of the target directory to prevent path traversal attacks
    safe_target_dir = target_dir.resolve()

    # Construct the full file path and resolve it to its absolute path
    file_path = (target_dir / file_name).resolve()

    # Security check: Ensure the resolved file path is within the safe target directory
    if not str(file_path).startswith(str(safe_target_dir)):
        raise HTTPException(
            status_code=403,
            detail=f"Access denied: '{file_name}' is not in the allowed directory."
        )

    try:
        # Write the new content to the file
        file_path.write_text(new_content, encoding="utf-8")

        # Reload agents data to reflect the changes in memory
        await load_agents_data(AGENTS_LIBRARY_PATH)

        return f"Successfully updated '{file_name}'."
    except Exception as e:
        raise ToolError(f"Error updating file '{file_name}': {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=SERVER_PORT)
