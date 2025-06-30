import sqlite3


def init_db():
    conn = sqlite3.connect("data_output/jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            date_posted TEXT,
            salary TEXT,
            source TEXT
        )
    """)
    conn.commit()
    conn.close()