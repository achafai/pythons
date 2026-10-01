
import os
import site
import sys


def is_in_venv() -> bool:
    """Check if running inside a virtual environment."""
    return (
        sys.prefix != sys.base_prefix
    )


def get_site_packages_path() -> str:
    """Retrieve the primary site-packages directory path."""
    try:
        packages: list[str] = site.getsitepackages()
        if packages:
            return packages[0]
    except AttributeError:
        pass
    return "Unknown"


def display_outside_status() -> None:
    """Display environment info when outside a virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("Then run this program again.")


def display_inside_status() -> None:
    """Display environment info when inside a virtual environment."""
    env_path: str = sys.prefix
    env_name: str = os.path.basename(env_path)
    pkg_path: str = get_site_packages_path()

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print(pkg_path)
    print("run: 'deactivate' to exit from venv")


def main() -> None:
    """Execute the construct environment check."""
    try:
        if is_in_venv():
            display_inside_status()
        else:
            display_outside_status()
    except (IOError, OSError) as error:
        sys.stderr.write(f"Stream error encountered: {error}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
