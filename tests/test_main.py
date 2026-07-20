import importlib

def test_main_module_import():
    module = importlib.import_module("src.main")
    assert module is not None