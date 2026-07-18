from src.database import Database


def test_database_creation():
    db = Database(":memory:")
    assert db.connection is not None
    db.close()


def test_start_session():
    db = Database(":memory:")
    session_id = db.start_session("sample.py")

    assert session_id > 0
    assert len(db.get_sessions()) == 1

    db.close()


def test_save_event():
    db = Database(":memory:")
    session_id = db.start_session("sample.py")

    db.save_event(
        session_id,
        "main",
        10,
        "line",
        {"x": 100},
    )

    events = db.get_events(session_id)

    assert len(events) == 1
    assert events[0]["function_name"] == "main"

    db.close()


def test_delete_session():
    db = Database(":memory:")
    session_id = db.start_session("sample.py")

    db.delete_session(session_id)

    assert len(db.get_sessions()) == 0

    db.close()