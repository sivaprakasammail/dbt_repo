import sqlite3
import pandas as pd

# Load CSV data
csv_file = 'data/issues.csv'
df = pd.read_csv(csv_file)

# Debugging: Print column names
print("Columns in CSV:", df.columns)

# Connect to SQLite database (creates database if it doesn't exist)
conn = sqlite3.connect('data/issues.db')
cursor = conn.cursor()

# Drop the table if it exists
cursor.execute("DROP TABLE IF EXISTS issues")

# Dynamically create a table with columns matching the CSV
columns = ", ".join([f'"{col}" TEXT' for col in df.columns])  # Define all columns as TEXT
create_table_query = f"CREATE TABLE issues ({columns});"
cursor.execute(create_table_query)

# Insert data into the table
for _, row in df.iterrows():
    placeholders = ", ".join(["?"] * len(row))  # Generate placeholders for all columns
    insert_query = f"INSERT INTO issues VALUES ({placeholders})"
    cursor.execute(insert_query, tuple(row))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data successfully loaded into SQLite database (data/issues.db).")