from src.tracer import Tracer


def test_tracer_creation():
    tracer = Tracer()
    assert tracer is not None