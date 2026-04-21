import sqlite3
from models.bank import *

def menu():
    conn=sqlite3.connect("bank.db")
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4.Check Balance")
        print("5.List Accounts")
        print("6.Exit")
        choice=input("Please choose your selection: ")

        if choice=="1":
            name=input("Acct Name: ")
            deposit_amount=float(input("initial deposit: "))
            create_account(conn,name,deposit_amount)
        elif choice=="2":
            acc_id=int(input("Account ID: "))
            amount=float(input("Deposit Amount: "))
            deposit(conn,acc_id,amount)
        elif choice=="3":
            acc_id=int(input("Account ID: "))
            amount=float(input("Withdrawl Amount: "))
            withdraw(conn,acc_id,amount)

        elif choice=="4":
            acc_id=int(input("Account ID: "))
            check_balance(conn,acc_id)
        elif choice=="5":
            list_accounts(conn)
        elif choice=="6":
            break
menu()