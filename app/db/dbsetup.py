import sqlite3
from dbconnection import DatabaseConnection

def create_tables():
    with DatabaseConnection("project.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                team_number INTEGER, 
                division TEXT
            )
        """)

        conn.commit()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                school_id INTEGER,
                FOREIGN KEY (school_id) REFERENCES users(id)        
        )
        """)

        conn.commit()
