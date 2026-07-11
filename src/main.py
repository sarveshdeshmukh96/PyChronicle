import sys
from database import Database
from ast_parser import ASTParser
from tracer import trace_function
from ui import PyChronicleUI
from utils import validate_python_file

def run_with_tracing(file_path: str):
    """Run a Python file, trace it, and save everything to the DB."""
    
    if not validate_python_file(file_path):
        return

    db = Database()                              
    session_id = db.start_session(file_path)     
    print(f"[INFO] Session started: ID = {session_id}")

    def tracer(frame, event, arg):
        line_no = frame.f_lineno
        variables = dict(frame.f_locals)         
        db.save_event(session_id, line_no, event, variables)
        return tracer

    sys.settrace(tracer)                         

    with open(file_path, "r") as f:
        code = f.read()
    exec(compile(code, file_path, "exec"))

    sys.settrace(None)  
    db.close()
    print(f"[INFO] Execution recorded. Session ID = {session_id}")

def show_history():
    """Print all saved sessions from the DB."""
    db = Database()
    sessions = db.get_all_sessions()
    if not sessions:
        print("No execution history found.")
    else:
        print("=" * 50)
        print("Execution History")
        print("=" * 50)
        for s in sessions:
            print(f"Session {s[0]} | File: {s[1]} | Ran at: {s[2]}")
    db.close()


if __name__ == "__main__":
    PyChronicleUI().run() 