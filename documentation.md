Environment Setup:

Ensure you have Python installed on your system. If not, download and install it from Python's official website.

Install required Python packages using the following command in your terminal or command prompt:

bash
Copy code
pip install tabula-py pandas
Script and PDF Preparation:

Save the provided script into a file (e.g., process_bank_statement.py).
Replace "your_bank_statement.pdf" in the script with the actual path to your bank statement PDF.
Ensure you have the necessary permissions to read the PDF file and write to the directory for the SQLite database.
Run the Script:

Open a terminal or command prompt.

Navigate to the directory where the script is saved.

Run the script using the following command:

bash
Copy code
python process_bank_statement.py
This will execute the script, read the specified PDF, and attempt to insert data into the SQLite database.

Check Logs:

After running the script, check the app_log.log file in the same directory for any error messages or warnings. This log file captures issues encountered during script execution.
Verify Database:

Check if the SQLite database file (bank_transactions.db) has been created or updated.

You can use a SQLite database viewer or command-line tool to inspect the contents of the database. For example:

bash
Copy code
sqlite3 bank_transactions.db
Then, you can run SQL queries to inspect the data:

sql
Copy code
SELECT * FROM transactions;
Ensure that the expected data has been inserted into the database.

Adjust and Iterate:

If there are issues or the script doesn't work as expected, review the logs, update the script accordingly, and iterate the testing process.