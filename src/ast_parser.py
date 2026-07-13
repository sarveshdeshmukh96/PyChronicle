import ast
import json
from pathlib import Path
from collections import Counter

from loguru import logger


class ASTParser:
    """PyChronicle AST Parser"""

    def __init__(self, file_path: str):

        self.file_path = Path(file_path)

        self.tree = None

    def read_source(self):

        if not self.file_path.exists():
            raise FileNotFoundError(self.file_path)

        return self.file_path.read_text(encoding="utf-8")

    def parse(self):

        source = self.read_source()

        self.tree = ast.parse(source)

        logger.success("AST Parsed Successfully")

        return self.tree

    def print_ast(self):

        if self.tree is None:
            self.parse()

        print(ast.dump(self.tree, indent=4))

    def get_statistics(self):

        if self.tree is None:
            self.parse()

        stats = Counter()

        assignments = []

        functions = []

        classes = []

        imports = []

        for node in ast.walk(self.tree):

            stats[type(node).__name__] += 1

            if isinstance(node, ast.Assign):

                for target in node.targets:

                    if isinstance(target, ast.Name):

                        assignments.append(target.id)

            elif isinstance(node, ast.FunctionDef):

                functions.append(node.name)

            elif isinstance(node, ast.ClassDef):

                classes.append(node.name)

            elif isinstance(node, ast.Import):

                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                imports.append(node.module)

        report = {

            "file": str(self.file_path),

            "total_nodes": sum(stats.values()),

            "functions": functions,

            "classes": classes,

            "imports": imports,

            "assignments": assignments,

            "node_statistics": dict(stats)

        }

        return report

    def print_report(self):

        report = self.get_statistics()

        print("\n" + "=" * 60)
        print("PyChronicle AST Report")
        print("=" * 60)

        print(f"File : {report['file']}")
        print(f"Total Nodes : {report['total_nodes']}")
        print(f"Functions : {len(report['functions'])}")
        print(f"Classes : {len(report['classes'])}")
        print(f"Imports : {len(report['imports'])}")
        print(f"Assignments : {len(report['assignments'])}")

        print("\nFunction Names")

        for function in report["functions"]:
            print("-", function)

        print("\nClass Names")

        for cls in report["classes"]:
            print("-", cls)

        print("\nImports")

        for module in report["imports"]:
            print("-", module)

        print("\nVariables")

        for variable in report["assignments"]:
            print("-", variable)

    def export_json(self, filename="analysis_report.json"):

        report = self.get_statistics()

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(report, file, indent=4)

        logger.success(f"Report exported -> {filename}")


if __name__ == "__main__":

    parser = ASTParser("sample_programs/sample.py")

    parser.parse()

    parser.print_report()

    parser.export_json()