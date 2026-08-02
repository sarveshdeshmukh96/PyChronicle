from src.controller import PyChronicleController


def test_controller_has_methods():
    controller = PyChronicleController()

    assert hasattr(controller, "parse_ast")
    assert hasattr(controller, "export_report")
    assert hasattr(controller, "run_tracer")


def test_controller_has_file_path_attribute():
    controller = PyChronicleController()

    assert hasattr(controller, "file_path")
    assert controller.file_path is None


def test_controller_updates_file_path():
    controller = PyChronicleController()

    result = controller.load_file("sample_programs/sample.py")

    assert result is True
    assert controller.file_path == "sample_programs/sample.py"