from pathlib import Path

from ast_parser import ASTParser


def print_menu():
    print("\n" + "=" * 60)
    print("PyChronicle - AST Powered Time-Travel Debugger")
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
        file_path = input("\nEnter Python file path: ").strip()

        if Path(file_path).exists():
            return file_path

        print("File not found. Please enter a valid Python file.")


def main():
    print("\nWelcome to PyChronicle")

    file_path = get_python_file()
    parser = ASTParser(file_path)

    while True:
        print_menu()

        choice = input("Select an option: ").strip()

        try:
            if choice == "1":
                parser.print_ast()

            elif choice == "2":
                parser.walk_ast()

            elif choice == "3":
                parser.detect_assignments()

            elif choice == "4":
                parser.count_nodes()

            elif choice == "5":
                parser.export_report()

            elif choice == "6":
                parser.print_ast()
                parser.walk_ast()
                parser.detect_assignments()
                parser.count_nodes()
                parser.export_report()

            elif choice == "0":
                print("\nThank you for using PyChronicle.")
                break

            else:
                print("Invalid option. Please try again.")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()