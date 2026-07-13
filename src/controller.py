from ast_parser import ASTParser
from tracer import Tracer
from database import Database


class PyChronicleController:
    """
    Central controller for PyChronicle.
    Coordinates AST parsing, tracing and database operations.
    """

    def __init__(self):
        self.file_path = None

    def load_file(self, file_path: str):

        self.file_path = file_path

        return True

    def parse_ast(self):

        parser = ASTParser(self.file_path)

        parser.parse()

        parser.print_report()

    def export_report(self):

        parser = ASTParser(self.file_path)

        parser.export_json()

    def run_tracer(self):

        tracer = Tracer()

        tracer.run(self.file_path)

        tracer.summary()

    def get_history(self):

        db = Database()

        sessions = db.get_sessions()

        db.close()

        return sessions