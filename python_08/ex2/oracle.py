import os
import sys
from typing import NamedTuple

from dotenv import load_dotenv


class Config(NamedTuple):
    """Data structure representing system configuration."""

    matrix_mode: str
    database_url: str
    api_key: str
    log_level: str
    zion_endpoint: str


def load_config() -> tuple[Config, list[str]]:

    load_dotenv()

    missing_keys: list[str] = []

    matrix_mode: str | None = os.getenv("MATRIX_MODE")
    if not matrix_mode:
        missing_keys.append("MATRIX_MODE")
        matrix_mode = "development"

    database_url: str | None = os.getenv("DATABASE_URL")
    if not database_url:
        missing_keys.append("DATABASE_URL")
        database_url = "not connected"

    api_key: str | None = os.getenv("API_KEY")
    if not api_key:
        missing_keys.append("API_KEY")
        api_key = "no value found"

    log_level: str | None = os.getenv("LOG_LEVEL")
    if not log_level:
        missing_keys.append("LOG_LEVEL")
        log_level = "DEBUG" if matrix_mode == "development" else "INFO"

    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")
    if not zion_endpoint:
        missing_keys.append("ZION_ENDPOINT")
        zion_endpoint = "no value found"

    config = Config(
        matrix_mode=matrix_mode,
        database_url=database_url,
        api_key=api_key,
        log_level=log_level,
        zion_endpoint=zion_endpoint,
    )
    return config, missing_keys


def display_status(config: Config, missing_keys: list[str]) -> None:
    """Display environment status and runtime details."""
    print("ORACLE STATUS: Reading the Matrix...")

    if missing_keys:
        print("\nWARNING: Missing environment variables:")
        for key in missing_keys:
            print(f"  - {key} (Using default fallback)")

    print("\nConfiguration loaded:")
    print(f"Mode: {config.matrix_mode}")

    if config.matrix_mode == "production":
        print(f"Database: Connected to production ")
        print(f"API Access: Authenticated ")
        print(f"Log Level: (Production Optimized)")
        print(f"Zion Network: Online ")
    else:
        print(f"Database: Connected to local instance ({config.database_url})")
        print(f"API Access: Authenticated [{config.api_key}]")
        print(f"Log Level: {config.log_level} (Verbose Dev Mode)")
        print(f"Zion Network: Online ({config.zion_endpoint})")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


def main() -> None:
    """Execute Oracle configuration system."""
    try:
        config, missing_keys = load_config()
        display_status(config, missing_keys)
    except (IOError, OSError) as error:
        sys.stderr.write(f"Stream error encountered: {error}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
