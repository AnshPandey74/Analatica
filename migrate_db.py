# migrate_db.py
import sqlite3

conn = sqlite3.connect('events.db')
cur = conn.cursor()

# Add columns only if they don't exist
cols = [r[1] for r in cur.execute("PRAGMA table_info(events)")]
def add_col(name, coltype):
    if name not in cols:
        cur.execute(f"ALTER TABLE events ADD COLUMN {name} {coltype}")
        print(f"Added column {name}")

add_col('url', 'TEXT')
add_col('referrer', 'TEXT')

conn.commit()
conn.close()
print("Migration complete")
