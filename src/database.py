import sqlite3
import json
from datetime import datetime
from pathlib import Path

from loguru import logger


class Database:
    """
    Database Manager for PyChronicle.
    Handles SQLite operations.
    """

    def __init__(self, db_path="pychronicle.db"):

        self.db_path = Path(db_path)

        self.connection = sqlite3.connect(self.db_path)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

        logger.success("Database Connected")

    def create_tables(self):
        """
        Create required tables.
        """

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            file_name TEXT NOT NULL,

            run_at TEXT NOT NULL

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS events(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            function_name TEXT,

            line_no INTEGER,

            event_type TEXT,

            variables TEXT,

            FOREIGN KEY(session_id)

            REFERENCES sessions(id)

        )
        """)

        self.connection.commit()

        logger.info("Tables Ready")

    def start_session(self, file_name):

        run_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        self.cursor.execute(

            """
            INSERT INTO sessions(file_name,run_at)

            VALUES(?,?)
            """,

            (file_name, run_time)

        )

        self.connection.commit()

        session_id = self.cursor.lastrowid

        logger.success(f"Session Created : {session_id}")

        return session_id

    def save_event(

        self,

        session_id,

        function_name,

        line_no,

        event_type,

        variables,

    ):

        self.cursor.execute(

            """
            INSERT INTO events

            (

                session_id,

                function_name,

                line_no,

                event_type,

                variables

            )

            VALUES(?,?,?,?,?)

            """,

            (

                session_id,

                function_name,

                line_no,

                event_type,

                json.dumps(

                    variables,

                    indent=4,

                    default=str

                )

            )

        )

        self.connection.commit()

    def get_sessions(self):

        self.cursor.execute(

            """
            SELECT *

            FROM sessions

            ORDER BY id DESC

            """
        )

        return self.cursor.fetchall()

    def get_events(self, session_id):

        self.cursor.execute(

            """
            SELECT *

            FROM events

            WHERE session_id=?

            ORDER BY id ASC

            """,

            (session_id,)

        )

        return self.cursor.fetchall()

    def delete_session(self, session_id):

        self.cursor.execute(

            "DELETE FROM events WHERE session_id=?",

            (session_id,)

        )

        self.cursor.execute(

            "DELETE FROM sessions WHERE id=?",

            (session_id,)

        )

        self.connection.commit()

        logger.warning(

            f"Session {session_id} deleted."

        )

    def close(self):

        self.connection.close()

        logger.info("Database Closed")


if __name__ == "__main__":

    db = Database()

    session = db.start_session("sample_programs/sample.py")

    db.save_event(

        session,

        "<module>",

        1,

        "line",

        {

            "x": 10,

            "y": 20

        }

    )

    print()

    print("Sessions")

    print(db.get_sessions())

    print()

    print("Events")

    print(db.get_events(session))

    db.close()