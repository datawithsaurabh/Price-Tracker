import pandas as pd
import sqlite3

# Read merged CSV
df = pd.read_csv("merged_prices.csv")

# Create Database
conn = sqlite3.connect("price_tracker.db")

# Save Table
df.to_sql(
    "product_prices",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()

print("Database Created Successfully!")

conn.close()