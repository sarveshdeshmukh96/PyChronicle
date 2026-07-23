from src.controller import PyChronicleController

def test_end_to_end_workflow():
    controller = PyChronicleController()
    assert controller is not None