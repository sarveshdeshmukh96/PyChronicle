from src.controller import PyChronicleController

def test_controller_has_methods():
    controller = PyChronicleController()

    assert hasattr(controller, "parse_ast")
    assert hasattr(controller, "export_report")
    assert hasattr(controller, "run_tracer")