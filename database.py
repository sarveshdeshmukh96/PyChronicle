import sqlite3

DATABASE_NAME = "pychronicle.db"

def connect_database():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS execution_trace (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        function_name TEXT,
        line_number INTEGER,
        event TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and table created successfully!")