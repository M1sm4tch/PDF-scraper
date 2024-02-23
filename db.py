import sqlite3
import pdf_scraper

# Create SQLite database connection and cursor
conn = sqlite3.connect('bank_transactions.db')
cursor = conn.cursor()

# Create a table named 'bank_transactions'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bank_transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        payment_type TEXT,
        detail TEXT,
        credit REAL,
        debit REAL,
        balance REAL
    )
''')

pdf_path = 'statement.pdf'
result = pdf_scraper.extract_information(pdf_path)

for transaction in result:
    print(transaction)

# Insert data into the 'bank_transactions' table
for entry in result:
    cursor.execute('''
        INSERT INTO bank_transactions (date, payment_type, detail, credit, debit, balance)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (entry['date'], entry['payment_type'], entry['detail'], entry['credit'], entry['debit'], entry['balance']))

# Commit the changes and close the connection
conn.commit()
conn.close()
