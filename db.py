import sqlite3


def save_incident(message: str):
    conn = sqlite3.connect("incidents.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY,
            message TEXT NOT NULL,
            status TEXT NOT NULL,
            analysis TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO incidents (message, status, analysis)
        VALUES (?, ?, ?)
    """, (message, "received", None))

    conn.commit()
    conn.close()