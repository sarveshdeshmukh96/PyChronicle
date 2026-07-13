import os
import sys
from pathlib import Path

from ast_parser import ASTParser
from database import Database
from utils import validate_python_file


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def print_menu():
    print("\n" + "=" * 60)
    print("         PyChronicle - AST Powered Time-Travel Debugger")
    print("=" * 60)
    print("1. Print AST")
    print("2. Show AST Nodes")
    print("3. Detect Variable Assignments")
    print("4. Count AST Nodes")
    print("5. Export JSON Report")
    print("6. Run Complete Analysis")
    print("7. Run with Execution Tracing")
    print("8. Show Execution History")
    print("0. Exit")
    print("=" * 60)


def get_python_file():
    while True:
        file_path = input("\nEnter Python file path (or 'q' to quit): ").strip()

        if file_path.lower() == "q":
            print("\nExiting PyChronicle...")
            exit()

        if Path(file_path).exists():
            return file_path

        print("File not found. Please enter a valid Python file.")


def run_complete_analysis(parser):
    print("\nRunning Complete Analysis...\n")

    parser.print_ast()
    parser.walk_ast()
    parser.detect_assignments()
    parser.count_nodes()
    parser.export_report()

    print("\nAnalysis completed successfully.")


def run_with_tracing(file_path: str):
    """Run a Python file, trace it, and save execution to the database."""

    if not validate_python_file(file_path):
        return

    db = Database()

    session_id = db.start_session(file_path)

    print(f"\nSession Started: {session_id}")

    def tracer(frame, event, arg):
        db.save_event(
            session_id,
            frame.f_lineno,
            event,
            dict(frame.f_locals),
        )
        return tracer

    sys.settrace(tracer)

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    exec(compile(code, file_path, "exec"))

    sys.settrace(None)

    db.close()

    print("Execution trace saved successfully.")


def show_history():
    """Display execution history."""

    db = Database()

    sessions = db.get_all_sessions()

    if not sessions:
        print("\nNo execution history found.")
    else:
        print("\nExecution History")
        print("=" * 60)

        for session in sessions:
            print(
                f"Session: {session[0]} | "
                f"File: {session[1]} | "
                f"Time: {session[2]}"
            )

    db.close()


def main():
    clear_screen()

    print("=" * 60)
    print("        Welcome to PyChronicle")
    print("   AST Powered Time-Travel Debugger")
    print("=" * 60)

    file_path = get_python_file()
    parser = ASTParser(file_path)

    while True:
        clear_screen()
        print_menu()

        choice = input("Select an option: ").strip()

        try:

            if choice == "1":
                parser.print_ast()
                pause()

            elif choice == "2":
                parser.walk_ast()
                pause()

            elif choice == "3":
                parser.detect_assignments()
                pause()

            elif choice == "4":
                parser.count_nodes()
                pause()

            elif choice == "5":
                parser.export_report()
                pause()

            elif choice == "6":
                run_complete_analysis(parser)
                pause()

            elif choice == "7":
                run_with_tracing(file_path)
                pause()

            elif choice == "8":
                show_history()
                pause()

            elif choice == "0":
                print("\nThank you for using PyChronicle.")
                break

            else:
                print("\nInvalid option.")
                pause()

        except Exception as e:
            print(f"\nError: {e}")
            pause()


if __name__ == "__main__":
    main()