import sqlite3
from faker import Faker
import random

DB_PATH = "data/game_inventory.db"
fake = Faker()

# Function to connect to the database
def create_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

# Function to initialize the database
def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Games (
        game_id INTEGER PRIMARY KEY,
        name TEXT,
        developer TEXT,
        category TEXT,
        platform TEXT,
        price REAL,
        release_date TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY,
        game_id INTEGER,
        customer_id INTEGER,
        order_date TEXT,
        amount REAL,
        FOREIGN KEY (game_id) REFERENCES Games(game_id),
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    ''')

    conn.commit()
    conn.close()

# Function to populate the database with sample data using Faker
def populate_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Sample data for games
    categories = ['Action', 'Adventure', 'Puzzle', 'Strategy', 'Sports', 'RPG']
    platforms = ['PC', 'PlayStation', 'Xbox', 'Nintendo', 'Mobile']

    for _ in range(50):  # Generate 50 sample games
        name = fake.word().capitalize() + " Game"
        developer = fake.company()
        category = random.choice(categories)
        platform = random.choice(platforms)
        price = round(random.uniform(10.0, 100.0), 2)
        release_date = fake.date()

        cursor.execute("INSERT INTO Games (name, developer, category, platform, price, release_date) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, developer, category, platform, price, release_date))

    # Sample data for customers
    for _ in range(20):  # Generate 20 sample customers
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()

        cursor.execute("INSERT INTO Customers (name, email, phone) VALUES (?, ?, ?)",
                       (name, email, phone))

    # Sample data for orders
    cursor.execute("SELECT game_id FROM Games")
    game_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT customer_id FROM Customers")
    customer_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(30):  # Generate 30 sample orders
        game_id = random.choice(game_ids)
        customer_id = random.choice(customer_ids)
        order_date = fake.date()
        amount = round(random.uniform(20.0, 150.0), 2)

        cursor.execute("INSERT INTO Orders (game_id, customer_id, order_date, amount) VALUES (?, ?, ?, ?)",
                       (game_id, customer_id, order_date, amount))

    conn.commit()
    conn.close()

# Initialize and populate the database
initialize_database()
populate_database()
print("Database setup and data population complete.")


