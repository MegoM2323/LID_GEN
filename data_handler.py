import sqlite3

db_name = 'users.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()


def create_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            telegram_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()


def add_user(telegram_id, name):
    try:
        cursor.execute('''
            INSERT INTO users (telegram_id, name) VALUES (?, ?)
        ''', (telegram_id, name))
        conn.commit()
        return 1
    except sqlite3.IntegrityError:
        return -1
