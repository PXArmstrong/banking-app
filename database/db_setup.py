import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to SQLite DB successful: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_tables(conn):
    try:
        cursor= conn.cursor()
        sql_create_accounts= """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        );
        """
        sql_create_transactions="""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            type TEXT,
            amount REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP    
        );
        """
        cursor.execute(sql_create_accounts)
        cursor.execute(sql_create_transactions)
        conn.commit()
        print("Tables Created sucessfully")
    except Exception as e:
        print(f"Error: {e}")
def initialize_database(db_file):
    """Initialize the database by creating a connection and setting up tables."""
    conn = create_connection(db_file)
    if conn:
        create_tables(conn)
        conn.close()