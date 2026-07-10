"""
utils.py

Common utility functions used across the PyChronicle project.
"""

from pathlib import Path
import os


def print_separator():
    """Print a separator line."""
    print("=" * 60)


def print_header(title: str):
    """Print a formatted header."""
    print_separator()
    print(title.center(60))
    print_separator()


def validate_python_file(file_path: str) -> bool:
    """
    Validate whether the given file exists
    and has a .py extension.
    """
    path = Path(file_path)

    if not path.exists():
        print("Error: File does not exist.")
        return False

    if path.suffix != ".py":
        print("Error: Please select a Python (.py) file.")
        return False

    return True


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pause program execution."""
    input("\nPress Enter to continue...")


def format_status(message: str, status: str = "INFO"):
    """
    Display a formatted status message.

    Example:
    [INFO] File Loaded Successfully
    """
    print(f"[{status}] {message}")