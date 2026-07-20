import sys
import time
from pathlib import Path

from src.database import Database
from loguru import logger
from tqdm import tqdm


class Tracer:
    """PyChronicle Execution Tracer"""

    def __init__(self):

        self.database = Database()

        self.session_id = None

        self.target_file = None

        self.events = 0

        self.start_time = 0

        self.end_time = 0

    def trace_callback(self, frame, event, arg):

        filename = Path(frame.f_code.co_filename).resolve()

        if filename != self.target_file:
            return self.trace_callback

        self.events += 1

        self.database.save_event(

            self.session_id,

            frame.f_code.co_name,

            frame.f_lineno,

            event,

            dict(frame.f_locals)

        )

        return self.trace_callback

    def run(self, file_path: str):

        file = Path(file_path).resolve()

        if not file.exists():

            logger.error("Python file not found.")

            return

        self.target_file = file

        self.session_id = self.database.start_session(file.name)

        source = file.read_text(encoding="utf-8")

        logger.info(f"Tracing {file.name}")

        self.start_time = time.perf_counter()

        sys.settrace(self.trace_callback)

        try:

            for _ in tqdm(range(1), desc="Tracing"):

                exec(

                    compile(

                        source,

                        str(file),

                        "exec"

                    )

                )

        finally:

            sys.settrace(None)

        self.end_time = time.perf_counter()

        logger.success("Tracing Completed")

        self.database.close()

    def summary(self):

        print("\n" + "=" * 60)

        print("PyChronicle Trace Summary")

        print("=" * 60)

        print(f"Events Captured : {self.events}")

        print(f"Execution Time  : {round(self.end_time-self.start_time,5)} sec")

        print("=" * 60)


if __name__ == "__main__":

    tracer = Tracer()

    tracer.run("sample_programs/sample.py")

    tracer.summary()