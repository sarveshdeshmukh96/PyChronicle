import ast
from src.ast_parser import ASTParser


def test_ast_parser_creation():
    parser = ASTParser("sample_programs/sample.py")

    assert parser is not None


def test_ast_parse_python_code():
    parser = ASTParser("sample_programs/sample.py")

    result = parser.parse()

    assert result is not None


def test_invalid_python_code():
    code = """
def hello(
"""

    try:
        ast.parse(code)
        assert False
    except SyntaxError:
        assert True