import sqlite3

# Read the SQL schema and insert data
with open('data/sample_sales_db.sql', 'r') as f:
    sql_script = f.read()

# Create the database
conn = sqlite3.connect('data/sales.db')
cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()
conn.close()

print("✅ sales.db created successfully.")
