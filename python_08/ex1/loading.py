import importlib.metadata
import importlib.util
import sys
from typing import Any


DEPENDENCIES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}


def check_dependency(name: str) -> tuple[bool, str]:
    """Check if a module is installed and return its status or version."""
    spec = importlib.util.find_spec(name)
    if spec is None:
        return False, "Missing package"
    try:
        version: str = importlib.metadata.version(name)
        return True, version
    except importlib.metadata.PackageNotFoundError:
        return False, "Version unknown"


def check_all_dependencies() -> bool:
    """Verify presence and versions of all required dependencies."""
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    all_ok: bool = True
    for pkg, desc in DEPENDENCIES.items():
        is_installed, ver_info = check_dependency(pkg)
        if is_installed:
            print(f"[OK] {pkg} ({ver_info}) - {desc}")
        else:
            print(f"[FAIL] {pkg} - {ver_info}")
            all_ok = False
    return all_ok


def print_missing_instructions() -> None:
    """Display installation instructions for missing dependencies."""
    print("\nMissing dependencies detected!")
    print("Please install required dependencies using one of these:")
    print("\n  1. Using pip:")
    print("     pip install -r requirements.txt")
    print("\n  2. Using Poetry:")
    print("     poetry install\n")


def run_analysis() -> None:
    """Perform Matrix data analysis and generate visual plot."""
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("Analyzing Matrix data...")
    num_points: int = 1000
    print(f"Processing {num_points} data points...")

    np.random.seed(42)
    raw_data: np.ndarray[Any, Any] = np.random.normal(
        loc=0.0, scale=1.0, size=num_points
    )
    noise: np.ndarray[Any, Any] = np.random.uniform(
        low=-0.5, high=0.5, size=num_points
    )
    matrix_signal: np.ndarray[Any, Any] = raw_data + noise

    data_frame: pd.DataFrame = pd.DataFrame(
        {
            "Time": np.arange(num_points),
            "Signal": matrix_signal,
            "Rolling_Mean": pd.Series(matrix_signal).rolling(50).mean(),
        }
    )

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(
        data_frame["Time"],
        data_frame["Signal"],
        alpha=0.3,
        label="Raw Signal",
    )
    ax.plot(
        data_frame["Time"],
        data_frame["Rolling_Mean"],
        color="green",
        linewidth=2,
        label="Matrix Stream (50-pt Mean)",
    )
    ax.set_title("Matrix Data Analysis")
    ax.set_xlabel("Time Step")
    ax.set_ylabel("Signal Amplitude")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)

    output_file: str = "matrix_analysis.png"
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    """Execute loading script flow."""
    try:
        if check_all_dependencies():
            run_analysis()
        else:
            print_missing_instructions()
    except (IOError, OSError) as err:
        sys.stderr.write(f"Stream error encountered: {err}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
