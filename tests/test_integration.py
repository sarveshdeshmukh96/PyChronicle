from src.controller import PyChronicleController


def test_end_to_end_workflow():
    controller = PyChronicleController()
    assert controller is not None


def test_load_file_sets_file_path():
    controller = PyChronicleController()

    result = controller.load_file("sample_programs/sample.py")

    assert result is True
    assert controller.file_path == "sample_programs/sample.py"


def test_load_file_overwrites_previous_path():
    controller = PyChronicleController()

    controller.load_file("first.py")
    controller.load_file("second.py")

    assert controller.file_path == "second.py"