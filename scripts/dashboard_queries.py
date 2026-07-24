import pandas as pd 

from scripts.database_connection import create_connection

def get_locations():
    connection, cursor = create_connection()

    query = """
    SELECT DISTINCT location
    FROM restaurants
    ORDER BY location;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    connection.close()

    return [row[0] for row in rows]

def get_cuisines():
    connection, cursor = create_connection()

    query = """
    SELECT DISTINCT cuisines
    FROM restaurants
    ORDER BY cuisines;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    connection.close()

    return [row[0] for row in rows]


def get_price_categories():
    connection, cursor = create_connection()

    query = """
    SELECT DISTINCT price_category
    FROM restaurants
    ORDER BY price_category;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    connection.close()

    return [row[0] for row in rows]


def get_online_order_options():
    connection, cursor = create_connection()

    query = """
    SELECT DISTINCT online_order
    FROM restaurants
    ORDER BY online_order;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    connection.close()

    return [row[0] for row in rows]


def get_book_table_options():
    connection, cursor = create_connection()

    query = """
    SELECT DISTINCT book_table
    FROM restaurants
    ORDER BY book_table;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    connection.close()

    return [row[0] for row in rows]

def filter_restaurants(locations, cuisines, price_categories,
                       online_orders, book_tables, min_rating):

    connection, cursor = create_connection()

    query = """
    SELECT
        name,
        location,
        cuisines,
        price_category,
        online_order,
        book_table,
        rate,
        "approx_cost(for two people)" AS approx_cost
    FROM restaurants
    WHERE rate >= ?
    """

    parameters = [min_rating]

    if locations:
        placeholders = ",".join(["?"] * len(locations))
        query += f" AND location IN ({placeholders})"
        parameters.extend(locations)

    if cuisines:
        placeholders = ",".join(["?"] * len(cuisines))
        query += f" AND cuisines IN ({placeholders})"
        parameters.extend(cuisines)

    if price_categories:
        placeholders = ",".join(["?"] * len(price_categories))
        query += f" AND price_category IN ({placeholders})"
        parameters.extend(price_categories)

    if online_orders:
        placeholders = ",".join(["?"] * len(online_orders))
        query += f" AND online_order IN ({placeholders})"
        parameters.extend(online_orders)

    if book_tables:
        placeholders = ",".join(["?"] * len(book_tables))
        query += f" AND book_table IN ({placeholders})"
        parameters.extend(book_tables)

    query += " ORDER BY rate DESC"

    cursor.execute(query, parameters)

    rows = cursor.fetchall()

    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)

    connection.close()

    return df
