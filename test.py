import unittest
import sqlite3
from models.bank import *

class TestingBank(unittest.TestCase):    
    def setUp(self):
        self.conn=sqlite3.connect(":memory:")
        cursor=self.conn.cursor()

        cursor.execute("""
        CREATE TABLE accounts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            balance REAL
            )               
        """)
        
        self.conn.commit()

    def test_creating_account(self):
        create_account(self.conn,"Greenman",100)
        cursor=self.conn.cursor()
        cursor.execute("SELECT * FROM accounts")
        result=cursor.fetchone()
        self.assertEqual(result[1],"Greenman")
        self.assertEqual(result[2],100)

    def test_deposits(self):
        create_account(self.conn,"JeanMaster",100)
        deposit(self.conn,1,50)
        cursor=self.conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE id = 1")
        balance=cursor.fetchone()[0]
        self.assertEqual(balance,150)

    def test_withdrawls(self):
        create_account(self.conn,"Coops",400)
        withdraw(self.conn,1,100)
        cursor=self.conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE id = 1")
        balance= cursor.fetchone()[0]
        self.assertEqual(balance,300)
    def test_overdrafts(self):
        create_account(self.conn,"Craig",100)
        withdraw(self.conn,1,200)
        cursor=self.conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE id = 1")
        balance=cursor.fetchone()[0]
        self.assertEqual(balance,100)
    def test_checking_balance(self):
        create_account(self.conn,"Maryanne",300)
        cursor=self.conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE id = 1")
        balance=cursor.fetchone()[0]
        self.assertEqual(balance,300)
    
if __name__ == "__main__":
    unittest.main()