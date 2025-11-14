import sqlite3

conn = sqlite3.connect('events.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    user_id TEXT,
    session_id TEXT,
    url TEXT,
    referrer TEXT,
    device_os TEXT,
    device_browser TEXT,
    device_type TEXT,
    metadata TEXT
)
''')

conn.commit()
conn.close()
print('Initialized events.db with table events')
