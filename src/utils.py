"""
utils.py

Common utility functions used throughout the PyChronicle project.
"""

import os
import logging
from pathlib import Path
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# =====================================================
# Logging Configuration
# =====================================================

logging.basicConfig(
    filename="pychronicle.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("PyChronicle")


def log_info(message: str):
    """Log informational messages."""
    logger.info(message)


def log_warning(message: str):
    """Log warning messages."""
    logger.warning(message)


def log_error(message: str):
    """Log error messages."""
    logger.error(message)


# =====================================================
# Terminal Utilities
# =====================================================

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pause execution."""
    input("\nPress Enter to continue...")


def separator():
    console.rule("[bold cyan]PyChronicle")


def banner():
    """Display application banner."""
    console.print(
        Panel.fit(
            "[bold cyan]🚀 PyChronicle[/bold cyan]\n"
            "AST Powered Time-Travel Debugger",
            border_style="bright_blue",
        )
    )


# =====================================================
# File Utilities
# =====================================================

def validate_python_file(file_path: str) -> bool:
    """Validate a Python source file."""

    file = Path(file_path)

    if not file.exists():
        show_error("File not found.")
        log_error(f"File not found: {file_path}")
        return False

    if file.suffix != ".py":
        show_error("Please select a Python (.py) file.")
        log_warning(f"Invalid file type selected: {file_path}")
        return False

    log_info(f"Validated Python file: {file_path}")
    return True


def read_python_file(file_path: str) -> str:
    """Read Python file."""

    log_info(f"Reading file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# =====================================================
# Message Utilities
# =====================================================

def show_success(message: str):
    console.print(f"[bold green]✔ {message}[/bold green]")
    log_info(message)


def show_error(message: str):
    console.print(f"[bold red]✘ {message}[/bold red]")
    log_error(message)


def show_info(message: str):
    console.print(f"[bold cyan]ℹ {message}[/bold cyan]")
    log_info(message)


# =====================================================
# Database Display
# =====================================================

def print_sessions(sessions):
    table = Table(title="Execution Sessions")

    table.add_column("ID", style="cyan")
    table.add_column("File")
    table.add_column("Run Time", style="green")

    for row in sessions:
        table.add_row(
            str(row["id"]),
            row["file_name"],
            row["run_at"]
        )

    console.print(table)


def print_events(events):
    table = Table(title="Execution Events")

    table.add_column("ID")
    table.add_column("Function")
    table.add_column("Line")
    table.add_column("Event")

    for row in events:
        table.add_row(
            str(row["id"]),
            row["function_name"],
            str(row["line_no"]),
            row["event_type"]
        )

    console.print(table)


# =====================================================
# Miscellaneous
# =====================================================

def current_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


if __name__ == "__main__":
    banner()
    show_success("Utilities Loaded Successfully")
    show_info(current_time())