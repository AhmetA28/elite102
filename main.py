import sqlite3

def connect_db():
    return sqlite3.connect("example.db")

def check_balance():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = 1")
    result = cursor.fetchone()

    if result:
        print("Balance:", result[0])
    else:
        print("Account not found.")

    conn.close()

def deposit():
    conn = connect_db()
    cursor = conn.cursor()

    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Deposit must be greater than 0.")
    else:
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = 1", (amount,))
        conn.commit()
        print("Deposit successful.")

    conn.close()

def withdraw():
    conn = connect_db()
    cursor = conn.cursor()

    amount = float(input("Enter amount to withdraw: "))

    cursor.execute("SELECT balance FROM accounts WHERE id = 1")
    result = cursor.fetchone()

    if not result:
        print("Account not found.")
    else:
        balance = result[0]

        if amount > balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Amount must be greater than 0.")
        else:
            cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = 1", (amount,))
            conn.commit()
            print("Withdrawal successful.")

    conn.close()

def create_account():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter account name: ")
    balance = float(input("Enter starting balance: "))

    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        (name, balance)
    )
    conn.commit()

    print("Account created successfully.")
    conn.close()

def menu():
    while True:
        print("\n--- Banking System ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Create Account")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            create_account()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()