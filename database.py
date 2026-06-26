import sqlite3

conn = sqlite3.connect("interview.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    role TEXT,
    score INTEGER
)
""")

conn.commit()

def save_result(name, role, score):
    print("Saving:", name, role, score)

    cursor.execute(
        "INSERT INTO results(name, role, score) VALUES (?, ?, ?)",
        (name, role, score)
    )

    conn.commit()
    print("Saved successfully!")