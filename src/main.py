from pathlib import Path

from controller import PyChronicleController
from utils import (
    banner,
    clear_screen,
    pause,
    show_info,
    show_error,
    validate_python_file,
)

controller = PyChronicleController()


def print_menu():
    print("\n" + "=" * 60)
    print("                    PyChronicle")
    print("=" * 60)
    print("1. Load Python File")
    print("2. Parse AST")
    print("3. Export JSON Report")
    print("4. Run Execution Tracer")
    print("5. Show Execution History")
    print("0. Exit")
    print("=" * 60)


def load_python_file():
    while True:
        file_path = input("\nEnter Python file path (or 'q' to quit): ").strip()

        if file_path.lower() == "q":
            return False

        if not file_path:
            show_error("File path cannot be empty.")
            continue

        if not file_path.endswith(".py"):
            show_error("Please select a Python (.py) file.")
            continue

        if not validate_python_file(file_path):
            continue

        controller.load_file(file_path)

        show_info(f"Loaded file: {Path(file_path).name}")
        return True


def show_execution_history():
    sessions = controller.get_history()

    print("\n" + "=" * 60)
    print("                 Execution History")
    print("=" * 60)

    if not sessions:
        print("No execution history found.")
    else:
        for session in sessions:
            print(f"Session ID : {session['id']}")
            print(f"File       : {session['file_name']}")
            print(f"Executed   : {session['run_at']}")
            print("-" * 60)

    pause()


def main():
    clear_screen()
    banner()

    valid_choices = {"0", "1", "2", "3", "4", "5"}

    while True:
        print_menu()

        choice = input("\nSelect Option : ").strip()

        if choice not in valid_choices:
            show_error("Invalid choice! Please select a number between 0 and 5.")
            pause()
            clear_screen()
            banner()
            continue

        try:
            if choice == "1":
                load_python_file()
                pause()

            elif choice == "2":
                controller.parse_ast()
                show_info("AST parsed successfully.")
                pause()

            elif choice == "3":
                controller.export_report()
                show_info("JSON report exported successfully.")
                pause()

            elif choice == "4":
                controller.run_tracer()
                show_info("Execution tracer completed successfully.")
                pause()

            elif choice == "5":
                show_execution_history()

            elif choice == "0":
                print("\nThank you for using PyChronicle.")
                print("Goodbye!")
                break

            clear_screen()
            banner()

        except Exception as e:
            show_error(str(e))
            pause()
            clear_screen()
            banner()


if __name__ == "__main__":
    main()