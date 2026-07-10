import sqlite3
import json
from datetime import datetime

class Database:
    def __init__(self, db_path: str = "pychronicle.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()
    
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT,
                run_at TEXT
            )
        """)
        self.cursor.execuute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                line_no INTEGER,
                event_type TEXT,
                variables TEXT,
                FOREIGN KEY (session_id) REFERENCES session(id)
                )
            """)
        self.connection.commit()

    def start_session(self, file_name: str) -> int:
        run_at = datetime.now().isoformat()
        self.cursor.execute(
            "INSERT INTO sessions (file_name, run_at) VALUES (?, ?)",
            (file_name, run_at)
        )
        self.connection.commit()
        return self.cursor.lastrowid