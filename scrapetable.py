import tabula
import sqlite3
import logging
import pandas as pd

# Configure the logging settings
logging.basicConfig(filename='app_log.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def read_pdf(file_path):
    """Read PDF and extract tables using tabula."""
    try:
        tables = tabula.read_pdf(file_path, pages='all')
        return [table.dropna(how='all') for table in tables if table is not None]
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        return []

def validate_date_format(date_str):
    """Validate the date format."""
    try:
        pd.to_datetime(date_str, format='%d/%m/%Y', errors='raise')
        return True
    except ValueError as e:
        logging.error(f"Invalid date format: {date_str}, Error: {e}")
        return False

def validate_data(row):
    """Validate the data before insertion."""
    if not validate_date_format(str(row[0])):
        return False

    return True

def create_table(cursor):
    """Create the SQLite table if it doesn't exist."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            reference_no INTEGER PRIMARY KEY,
            date TEXT,
            type TEXT,
            details TEXT,
            credit REAL,
            debit REAL,
            balance REAL
        )
    ''')

def insert_data(cursor, row):
    """Insert validated data into the SQLite database."""
    try:
        cursor.execute('''
            INSERT INTO transactions (date, type, details, credit, debit, balance)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (str(row[0]), str(row[1]), str(row[2]), row[3], row[4], row[5]))
    except Exception as e:
        logging.error(f"Error inserting validated row: {row}, Error: {e}")

def process_pdf(file_path, db_file):
    """Process the bank statement PDF and insert data into SQLite database."""
    try:
        # Read PDF and extract tables
        tables = read_pdf(file_path)

        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        create_table(cursor)

        # Insert data into the table after validation
        for df in tables:
            for row in df.itertuples(index=False, name=None):
                if validate_data(row):
                    insert_data(cursor, row)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_file_path = "statement.pdf"
    database_file = "bank_transactions.db"
    process_pdf(pdf_file_path, database_file)
