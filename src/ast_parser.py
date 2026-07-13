import ast
import json
from pathlib import Path


class ASTParser:
    """Simple AST Explorer"""

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def read_source(self) -> str:
        """Read source code from a Python file."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()

    def parse(self):
        """Parse source code into an AST."""
        source_code = self.read_source()
        return ast.parse(source_code)

    def print_ast(self):
        """Print formatted AST."""
        tree = self.parse()
        print("=" * 60)
        print("Abstract Syntax Tree")
        print("=" * 60)
        print(ast.dump(tree, indent=4))

    def walk_ast(self):
        """Walk through every AST node."""
        tree = self.parse()

        print("\n" + "=" * 60)
        print("AST Nodes")
        print("=" * 60)

        for node in ast.walk(tree):
            print(type(node).__name__)

    def detect_assignments(self):
        """Detect variable assignments."""
        tree = self.parse()

        print("\n" + "=" * 60)
        print("Variable Assignments")
        print("=" * 60)

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        print(f"Variable: {target.id}")

                        if isinstance(node.value, ast.Constant):
                            print(f"Value: {node.value.value}")

                        elif isinstance(node.value, ast.BinOp):
                            print("Value: Binary Operation")

                        else:
                            print(f"Value Type: {type(node.value).__name__}")

                        print("-" * 30)

    def count_nodes(self):
        """Count total AST nodes."""
        tree = self.parse()

        total_nodes = sum(1 for _ in ast.walk(tree))

        print("\n" + "=" * 60)
        print("AST Statistics")
        print("=" * 60)
        print(f"Total AST Nodes: {total_nodes}")
    
    def export_report(self, filename="analysis_report.json"):
        """Export AST analysis report to JSON."""

        tree = self.parse()

        assignments = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):

                        if isinstance(node.value, ast.Constant):
                            value = node.value.value

                        elif isinstance(node.value, ast.BinOp):
                            value = "Binary Operation"

                        else:
                            value = type(node.value).__name__

                        assignments.append({
                            "variable": target.id,
                            "value": value
                        })

        report = {
            "file": str(self.file_path),
            "total_nodes": sum(1 for _ in ast.walk(tree)),
            "assignments": assignments
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        print(f"\nReport exported successfully -> {filename}")
        
if __name__ == "__main__":
    parser = ASTParser("sample_programs/sample.py")

    parser.print_ast()
    parser.walk_ast()
    parser.detect_assignments()
    parser.count_nodes()
    parser.export_report()