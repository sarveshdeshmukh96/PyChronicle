from database import connect_database

def insert_data():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO execution_trace
    (filename, function_name, line_number, event)
    VALUES (?, ?, ?, ?)
    """, ("demo.py", "hello", 10, "call"))

    conn.commit()
    conn.close()


def read_data():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM execution_trace")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


insert_data()
read_data()