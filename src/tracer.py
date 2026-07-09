import sys

def trace_function(frame, event, arg):
    print(f"Event: {event}, Function: {frame.f_code.co_name}, Line: {frame.f_lineno}")
    return trace_function

def greet():
    print("Hello")
    print("Welcome to PyChronicle!")

sys.settrace(trace_function)

greet()

sys.settrace(None)