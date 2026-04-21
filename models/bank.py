def create_account(conn,name,deposit):
    cursor=conn.cursor()
    cursor.execute(
        "INSERT INTO accounts (name,balance) VALUES (?,?)",
        (name,deposit)
    )
    conn.commit()

def deposit(conn,account_id,amount):
    cursor=conn.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance+ ? WHERE id = ?",
        (amount,account_id)
    )
    conn.commit()

def withdraw(conn,account_id,amount):
    cursor=conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE id= ?",(account_id,))
    balance=cursor.fetchone()[0]
    if balance<amount:
        print("Insufficient Funds")
        return
    cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?",(amount,account_id)
    )
    conn.commit()

def check_balance(conn,account_id):
    cursor=conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE id= ?",(account_id,))
    result= cursor.fetchone()
    print(result[0])

def list_accounts(conn):
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    for row in cursor.fetchall():
        print(row)
