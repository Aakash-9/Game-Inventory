import sqlite3
import os
import pandas as pd

def get_db_connection():
    db_path = os.path.join(os.getcwd(), 'data', 'game_inventory.db')
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))
    conn = sqlite3.connect(db_path)
    return conn

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            developer TEXT NOT NULL,
            category TEXT NOT NULL,
            platform TEXT NOT NULL,
            price REAL NOT NULL,
            release_date DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_games():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM Games", conn)
    conn.close()
    return df

def add_game(name, developer, category, platform, price, release_date):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO Games (name, developer, category, platform, price, release_date) VALUES (?, ?, ?, ?, ?, ?)",
        (name, developer, category, platform, price, release_date)
    )
    conn.commit()
    conn.close()

def update_game(game_id, name, developer, category, platform, price, release_date):
    conn = get_db_connection()
    conn.execute(
        """UPDATE Games
           SET name = ?, developer = ?, category = ?, platform = ?, price = ?, release_date = ?
           WHERE id = ?""",
        (name, developer, category, platform, price, release_date, game_id)
    )
    conn.commit()
    conn.close()

def delete_game(game_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM Games WHERE id = ?", (game_id,))
    conn.commit()
    conn.close()

# Initialize the database when the module is imported
initialize_db()
