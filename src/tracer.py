import sys


def trace_function(frame, event, arg):
    """
    Trace function that prints execution details.
    """
    print(
        f"Event: {event}, "
        f"Function: {frame.f_code.co_name}, "
        f"Line: {frame.f_lineno}"
    )
    return trace_function


def sample_function():
    """
    Simple function to demonstrate tracing.
    """
    a = 10
    b = 20
    c = a + b
    print(f"Sum = {c}")


if __name__ == "__main__":
    print("=" * 50)
    print("PyChronicle - Execution Tracer Demo")
    print("=" * 50)

    # Start tracing
    sys.settrace(trace_function)

    # Execute sample function
    sample_function()

    # Stop tracing
    sys.settrace(None)
