import sqlite3
from tabulate import tabulate
from cryptography.fernet import Fernet
import os

# Decipher
with open('encrypted.bin', 'rb') as file:
    ciphertext = file.read()
    cipher = Fernet(os.environ.get('db_pw').encode('ascii'))

with open('database.db', 'wb') as file:
    file.write(cipher.decrypt(ciphertext))

# Establish a connection to the SQLite database
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the SQL query to get the table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

# Fetch all table names
table_names = cursor.fetchall()

# Process the retrieved table names
for table in table_names:
    table_name = table[0]

    # Execute the SQL query to fetch all rows from the table
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows
    rows = cursor.fetchall()

    # Fetch column names from the cursor description
    column_names = [description[0] for description in cursor.description]

    # Print the table using the tabulate library
    print(tabulate(rows, headers=column_names, tablefmt="grid"))




# Close the connection
conn.close()


os.remove('database.db')