import sqlite3
import json
from datetime import datetime


class Database:
    """Handles SQLite database operations for PyChronicle."""

    def __init__(self, db_path: str = "pychronicle.db"):
        """Initialize database connection and create tables."""
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create required database tables if they don't exist."""

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL,
                run_at TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER NOT NULL,
                line_no INTEGER,
                event_type TEXT,
                variables TEXT,
                FOREIGN KEY (session_id) REFERENCES sessions(id)
            )
        """)

        self.connection.commit()

    def start_session(self, file_name: str) -> int:
        """
        Create a new execution session.

        Returns:
            int: ID of the newly created session.
        """
        run_at = datetime.now().isoformat()

        self.cursor.execute(
            "INSERT INTO sessions (file_name, run_at) VALUES (?, ?)",
            (file_name, run_at)
        )

        self.connection.commit()
        return self.cursor.lastrowid

    def save_event(
        self,
        session_id: int,
        line_no: int,
        event_type: str,
        variables: dict
    ):
        """
        Save an execution event to the database.
        """

        self.cursor.execute(
            """
            INSERT INTO events
            (session_id, line_no, event_type, variables)
            VALUES (?, ?, ?, ?)
            """,
            (
                session_id,
                line_no,
                event_type,
                json.dumps(variables)
            )
        )

        self.connection.commit()

    def get_all_sessions(self):
        """Return all execution sessions."""

        self.cursor.execute(
            "SELECT * FROM sessions ORDER BY run_at DESC"
        )

        return self.cursor.fetchall()

    def get_events(self, session_id: int):
        """Return all events for a given session."""

        self.cursor.execute(
            """
            SELECT *
            FROM events
            WHERE session_id = ?
            ORDER BY id ASC
            """,
            (session_id,)
        )

        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()


if __name__ == "__main__":
    db = Database()

    session_id = db.start_session("sample_programs/sample.py")

    db.save_event(
        session_id,
        1,
        "line",
        {"x": 10, "y": 20}
    )

    print("Sessions:")
    print(db.get_all_sessions())

    print("\nEvents:")
    print(db.get_events(session_id))

    db.close()
