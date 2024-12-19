import sqlite3

conn = sqlite3.connect('user_db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_expenses (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER UNIQUE,
    user_name TEXT,
    cat1 TEXT,
    cat2 TEXT,
    cat3 TEXT,
    expenses1 INTEGER,
    expenses2 INTEGER,
    expenses3 INTEGER)
''')
conn.commit()
conn.close()
