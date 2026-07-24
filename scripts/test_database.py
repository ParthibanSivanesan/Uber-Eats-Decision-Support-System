#To Verify Table Created 
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "database" / "uber_eats.db"

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM restaurants")
print("Restaurants:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM orders")
print("Orders:", cursor.fetchone()[0])


connection.close()