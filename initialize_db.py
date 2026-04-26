import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
""")

cursor.execute("""
INSERT INTO accounts (name, balance)
SELECT 'Test Account', 1000.00
WHERE NOT EXISTS (SELECT 1 FROM accounts)
""")

connection.commit()
connection.close()

print("Accounts table created and sample account added.")