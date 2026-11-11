import sqlite3

DB_NAME = 'vendo.db'

def get_db_connection():
    """Tworzy połączenie z bazą SQLite z włączoną kontrolą kluczy obcych i mapowaniem kolumn."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
