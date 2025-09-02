import sqlite3
import csv

# Paths
csv_path = 'browns.csv'
db_path = 'browns.db'
table_name = 'browns'

# Read CSV header
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

# Create table schema
columns = ', '.join([f'"{col}" TEXT' for col in header])
create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns});'

# Connect to SQLite and create table
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute(create_table_sql)

# Insert CSV rows
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    rows = [row for row in reader]
    placeholders = ', '.join(['?' for _ in header])
    insert_sql = f'INSERT INTO {table_name} VALUES ({placeholders})'
    c.executemany(insert_sql, rows)

conn.commit()
conn.close()
