import sqlite3
import os

# Database file location
DB_FILE = os.path.join(os.path.dirname(__file__), "idea_engine.db")

def create_connection():
    """Creates and returns a database connection."""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
    return conn

def create_tables():
    """Creates necessary tables for storing ideas."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ideas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT NOT NULL,
                idea TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

def insert_idea(prompt, idea):
    """Inserts a new idea into the database."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ideas (prompt, idea) VALUES (?, ?)", (prompt, idea))
        conn.commit()
        conn.close()

def get_all_ideas():
    """Retrieves all stored ideas."""
    conn = create_connection()
    ideas = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ideas ORDER BY created_at DESC")
        ideas = cursor.fetchall()
        conn.close()
    return ideas

if __name__ == "__main__":
    create_tables()
    print("Database setup completed.")
