import sqlite3

from database.db_setup import initialize_database

if __name__=="__main__":
    initialize_database("bank.db")
