import sqlite3

def create_connection():
    connection = sqlite3.connect("database/uber_eats.db")
    cursor = connection.cursor()

    return connection, cursor