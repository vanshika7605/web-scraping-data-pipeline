import pandas as pd
import sqlite3

# Read the scraped CSV file
df = pd.read_csv("books_data.csv")

# Create connection to SQLite database
conn = sqlite3.connect("books.db")

# Store the data in SQL table
df.to_sql("books", conn, if_exists="replace", index=False)

print("Data successfully stored in SQL database!")