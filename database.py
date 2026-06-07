import sqlite3

def connect_db():
    return sqlite3.connect('parking.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS parking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_type TEXT,
        category TEXT,
        name TEXT,
        vehicle_number TEXT,
        class TEXT,
        division TEXT,
        entry_time TEXT,
        exit_time TEXT,
        date TEXT,
        paid INTEGER
    )
    ''')
    conn.commit()
    conn.close()
