import duckdb
import os

# Define paths
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Move one level up to jaffle-shop-classic
csv_file = os.path.join(base_path, 'data/issues.csv')  # Path to your CSV file
db_file = os.path.join(base_path, 'data/issues.duckdb')  # Path to your DuckDB file

# Ensure the database folder exists
os.makedirs(os.path.dirname(db_file), exist_ok=True)

# Connect to DuckDB (creates the database if it doesn't exist)
conn = duckdb.connect(db_file)

# Load the CSV into a DuckDB table
conn.execute(f"""
    CREATE TABLE IF NOT EXISTS issues AS
    SELECT * FROM read_csv_auto('{csv_file}');
""")

# Verify the data
print("Loaded data:")
print(conn.execute("SELECT * FROM issues LIMIT 5").fetchdf())

# Close the connection
conn.close()