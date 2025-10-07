import sqlite3
import json

# Your JSON data
data = {
    "contacts": [
        {
            "name": "John Doe",
            "contact_no": "000000000000",
            "email": "john.doe@example.com"
        },
        {
            "name": "Jane Smith",
            "contact_no": "000000000000",
            "email": "jane.smith@example.com"
        }
    ]
}

# Connect (or create) SQLite database
conn = sqlite3.connect('address_book.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact_no TEXT,
        email TEXT
    )
''')

# Insert data into table
# for contact in data['contacts']:
#     cursor.execute('''
#         INSERT INTO contacts (name, contact_no, email)
#         VALUES (?, ?, ?)
#     ''', (contact['name'], contact['contact_no'], contact['email']))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created and contacts inserted successfully.")
