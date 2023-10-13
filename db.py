import sqlite3

# Create a new SQLite database (or connect to an existing one)
conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS sample_table (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                )''')

# Insert 100 rows of sample data into the table
for i in range(1, 101):
    name = f"User{i}"
    age = 18 + i  # Age varies from 18 to 117
    cursor.execute("INSERT INTO sample_table (name, age) VALUES (?, ?)", (name, age))

# Commit the changes and close the database connection
conn.commit()
conn.close()

print("Database 'sample.db' created with 100 rows.")
