import os
import secrets
from pathlib import Path

import yaml
from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader


# Configuration
def load_config() -> dict:
    """Loads configuration from config.yaml and overrides with environment variables."""
    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)

    # Override config with environment variables
    def _override_config_with_env(current_config: dict, prefix: str = "") -> dict:
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
                        current_config[key] = os.environ[env_var_name].lower() in (
                            "true",
                            "1",
                            "t",
                            "y",
                            "yes",
                        )
                    else:
                        current_config[key] = os.environ[env_var_name]
                except ValueError:
                    print(
                        f"Warning: Could not convert environment variable "
                        f"{env_var_name} to type of {key}. Using default."
                    )
        return current_config

    return _override_config_with_env(cfg)


config = load_config()
API_KEY_FILE = Path(config["api_key"]["file_path"])
API_KEY_NAME = config["api_key"]["header_name"]
API_KEY_HEADER = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


def get_api_key() -> str:
    """Retrieves the API key from the configured file path."""
    if not API_KEY_FILE.is_file():
        raise HTTPException(status_code=500, detail="API key not found. Please generate one.")
    return API_KEY_FILE.read_text().strip()


def generate_api_key() -> str:
    """Generates a new API key and saves it to the configured file path."""
    api_key = secrets.token_urlsafe(32)
    API_KEY_FILE.write_text(api_key)
    return api_key


async def verify_api_key(api_key: str = Security(API_KEY_HEADER)) -> str:
    """Verifies the provided API key against the one stored on the server."""
    server_api_key = get_api_key()
    if not secrets.compare_digest(api_key, server_api_key):
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key
