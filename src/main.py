import os
from pathlib import Path

from ast_parser import ASTParser


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
    print("0. Exit")
    print("=" * 60)


def get_python_file():
    while True:
        file_path = input("\nEnter Python file path (or 'q' to quit): ").strip()

        if file_path.lower() == "q":
            print("\nExiting PyChronicle...")
            exit()

        if not file_path:
            print("Error: File path cannot be empty.")
            continue

        if not file_path.endswith(".py"):
            print("Error: Please enter a valid Python (.py) file.")
            continue

        if Path(file_path).is_file():
            return file_path

        print("Error: File not found. Please try again.")


def run_complete_analysis(parser):
    print("\nRunning Complete Analysis...\n")

    parser.print_ast()
    parser.walk_ast()
    parser.detect_assignments()
    parser.count_nodes()
    parser.export_report()

    print("\nAnalysis completed successfully.")


def main():
    clear_screen()

    print("=" * 60)
    print("           Welcome to PyChronicle")
    print("      AST Powered Time-Travel Debugger")
    print("=" * 60)

    file_path = get_python_file()
    parser = ASTParser(file_path)

    valid_choices = {"0", "1", "2", "3", "4", "5", "6"}

    while True:
        clear_screen()
        print_menu()

        choice = input("Select an option: ").strip()

        if choice not in valid_choices:
            print("\nInvalid choice! Please select a number between 0 and 6.")
            pause()
            continue

        try:
            if choice == "1":
                parser.print_ast()
                print("\nAST printed successfully.")
                pause()

            elif choice == "2":
                parser.walk_ast()
                print("\nAST nodes displayed successfully.")
                pause()

            elif choice == "3":
                parser.detect_assignments()
                print("\nVariable assignments detected successfully.")
                pause()

            elif choice == "4":
                parser.count_nodes()
                print("\nAST node count completed successfully.")
                pause()

            elif choice == "5":
                parser.export_report()
                print("\nJSON report exported successfully.")
                pause()

            elif choice == "6":
                run_complete_analysis(parser)
                pause()

            elif choice == "0":
                print("\nThank you for using PyChronicle.")
                print("Goodbye!")
                break

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            pause()


if __name__ == "__main__":
    main()