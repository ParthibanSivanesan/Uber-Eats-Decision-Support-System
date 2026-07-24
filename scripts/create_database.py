from pathlib import Path
import sqlite3
import pandas as pd


#Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

#Paths
db_path = BASE_DIR / "database" / "uber_eats.db"
restaurants_csv = BASE_DIR / "data" / "restaurants_cleaned.csv"
orders_csv = BASE_DIR / "data" / "orders_cleaned.csv"

#print("Database Path:", db_path)

#Connect to the SQLite database
connection = sqlite3.connect(db_path)

#Read Cleaned CSV
restaurants_df = pd.read_csv(restaurants_csv)
orders_df = pd.read_csv(orders_csv)

#Insert into SQlite
restaurants_df.to_sql(
    "restaurants",
    connection,
    if_exists='replace',
    index=False
)

orders_df.to_sql(
    "orders",
    connection,
    if_exists='replace',
    index=False
)

#print("Database created and Successfully Connected to SQLite")
print("Restaurants table created successfully")
print("Orders table created successfully")

connection.close()