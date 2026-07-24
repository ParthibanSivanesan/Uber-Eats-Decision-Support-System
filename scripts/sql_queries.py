#Connect to SQLite
from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "database" / "uber_eats.db"

def get_connection():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    return connection, cursor

#Key Business Questions:
#Q1 Which Bangalore locations have the highest average restaurant ratings?

def highest_rated_locations():
    connection, cursor = get_connection()
    query = """
    SELECT 
        location, COUNT(*) AS restaurant_count, ROUND(AVG(rate), 2) AS avg_ratings 
    FROM restaurants 
    GROUP BY location 
    ORDER BY avg_ratings DESC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df

#Q2 Which locations are over-saturated with restaurants?

def oversaturated_locations():
    connection, cursor = get_connection()
    query="""
    SELECT 
        location, COUNT(*) AS restaurant_count 
    FROM restaurants 
    GROUP BY location 
    ORDER BY restaurant_count DESC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q3 Does online ordering improve restaurant ratings?

def onlin_ordering_correlation():
    connection, cursor = get_connection()
    query="""
    SELECT 
        online_order, COUNT(*) AS total_restaurants, ROUND(AVG(rate), 2) AS avg_ratings 
    FROM restaurants 
    GROUP BY online_order 
    ORDER BY avg_ratings DESC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q4 Does table booking correlate with higher customer ratings?

def table_booking_correlation():
    connection, cursor = get_connection()
    query="""
    SELECT
        book_table, COUNT(*) AS restaurant_count, ROUND(AVG(rate), 2) AS avg_ratings 
    FROM restaurants 
    GROUP BY book_table 
    ORDER BY avg_ratings DESC;
    """
    cursor.execute(query)
    rows=cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q5 What price range delivers the best customer satisfaction?

def price_range_performance():
    connection, cursor = get_connection()
    query="""
    SELECT
        price_category,
        COUNT(*) AS restaurant_count,
        ROUND(AVG(rate),2) AS avg_ratings
    FROM restaurants
    GROUP BY price_category
    ORDER BY avg_ratings DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df

#Q6 How do low, mid, and premium-priced restaurants perform?

def pricing_segment_performance():
    connection, cursor = get_connection()
    query="""
    SELECT
        price_category,
        COUNT(*) AS restaurant_count,
        ROUND(AVG(rate),2) AS avg_ratings
    FROM restaurants
    GROUP BY price_category
    ORDER BY avg_ratings DESC;
    """
    cursor.execute(query)
    rows=cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q7 Which cuisines are most common?

def common_cuisines():
    connection, cursor = get_connection()
    query="""
    SELECT
        cuisines,
        COUNT(*) AS restaurant_count
    FROM restaurants
    GROUP BY cuisines
    ORDER BY restaurant_count DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q8 Which cuisines receive the highest ratings?

def highest_rated_cuisines():
    connection, cursor = get_connection()
    query="""
    SELECT
        cuisines,
        COUNT(*) AS restaurant_count,
        ROUND(AVG(rate),2) AS avg_ratings
    FROM restaurants
    GROUP BY cuisines
    ORDER BY avg_ratings DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q9 Which cuisines perform well despite fewer restaurants?

def best_performing_cuisines():
    connection, cursor = get_connection()
    query="""
    SELECT cuisines,
        COUNT(*) AS restaurants_count,
        ROUND(AVG(rate), 2) AS avg_ratings
    FROM restaurants
    GROUP BY cuisines
    ORDER BY restaurants_count ASC, avg_ratings DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df= pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q10 Relationship between cost and rating

def cost_rating_relationship():
    connection, cursor = get_connection()
    query="""
    SELECT
        "approx_cost(for two people)" AS approx_cost,
        COUNT(*) AS restaurant_count,
        ROUND(AVG(rate), 2) AS avg_rating
    FROM restaurants
    GROUP BY "approx_cost(for two people)"
    ORDER BY approx_cost;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q11 Ideal locations for premium restaurant onboarding

def ideal_locations_for_premium():
    connection, cursor = get_connection()
    query="""
    SELECT
        location,
        COUNT(*) AS restaurant_count,
        ROUND(AVG(rate),2) AS avg_ratings
    FROM restaurants
    WHERE price_category = 'Premium'
    GROUP BY location
    ORDER BY avg_ratings DESC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q12 High demand but lower ratings

def high_demand_low_rating():
    connection, cursor = get_connection()
    query="""
    SELECT location,
       COUNT(*) AS restaurants_count,
       ROUND(AVG(rate),2) AS avg_ratings
    FROM restaurants
    GROUP BY location
    ORDER BY
    restaurants_count DESC, avg_ratings ASC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Q13 Both Online Order + Table Booking

def online_order_table_booking():
    connection, cursor = get_connection()
    query="""
    SELECT
        COUNT(*) AS restaurant_count,
        ROUND(AVG(rate), 2) AS avg_ratings
    FROM restaurants
    WHERE online_order = 'Yes'
    AND book_table = 'Yes';
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df

#Q14 Success factors

def success_factors():
    connection, cursor = get_connection()
    query="""
    SELECT
        location,
        cuisines,
        price_category,
        online_order,
        book_table,
        COUNT(*) AS restaurant_count,
        ROUND(AVG(rate), 2) AS avg_ratings
    FROM restaurants
    GROUP BY
        location,
        cuisines,
        price_category,
        online_order,
        book_table
    ORDER BY avg_ratings DESC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df

#Q15 Top restaurants in each pricing segment

def top_restaurants_by_pricing_segment():
    connection, cursor = get_connection()
    query="""
    SELECT
        DISTINCT name AS restaurant_name,
        price_category,
        rate
    FROM restaurants
    WHERE rate IS NOT NULL
    ORDER BY price_category, rate DESC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


#Additional Business Questions:

# A1: What is the total revenue generated from all orders?
def total_revenue():
    connection, cursor = get_connection()
    query="""
    SELECT
        ROUND(SUM(order_value), 2) AS total_revenue
    FROM orders;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


# A2: Which restaurants generated the highest revenue?
def restaurants_by_revenue():
    connection, cursor = get_connection()
    query="""
    SELECT
        restaurant_name,
        COUNT(*) AS total_orders,
        ROUND(SUM(order_value), 2) AS total_revenue
    FROM orders
    GROUP BY restaurant_name
    ORDER BY total_revenue DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


# A3: Which payment method is used the most?
def most_used_payment_method():
    connection, cursor = get_connection()
    query="""
    SELECT
        payment_method,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY payment_method
    ORDER BY total_orders DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


# A4: Does using discounts increase average order value?
def discount_vs_average_order_value():
    connection, cursor = get_connection()
    query="""
    SELECT
        discount_used,
        COUNT(*) AS total_orders,
        ROUND(AVG(order_value), 2) AS avg_order_value
    FROM orders
    GROUP BY discount_used;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df
    
    

# A5: Which month generated the highest revenue?
def highest_revenue_month():
    connection, cursor = get_connection()
    query="""
    SELECT
        strftime('%Y-%m', order_date) AS order_month,
        ROUND(SUM(order_value),2) AS total_revenue
    FROM orders
    GROUP BY order_month
    ORDER BY total_revenue DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df
    
    

# A6: Which restaurant locations generate the highest revenue?
def revenue_by_location():
    connection, cursor = get_connection()
    query="""
    SELECT
        r.location,
        COUNT(o.order_id) AS total_orders,
        ROUND(SUM(o.order_value),2) AS total_revenue
    FROM restaurants r
    INNER JOIN orders o
    ON r.name = o.restaurant_name
    GROUP BY r.location
    ORDER BY total_revenue DESC;            
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df
    
    

# A7: Which cuisines generate the highest revenue?
def revenue_by_cuisine():
    connection, cursor = get_connection()
    query="""
    SELECT
        r.cuisines,
        COUNT(o.order_id) AS total_orders,
        ROUND(SUM(o.order_value),2) AS total_revenue
    FROM restaurants r
    INNER JOIN orders o
    ON r.name = o.restaurant_name
    GROUP BY r.cuisines
    ORDER BY total_revenue DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df
    
    

# A8: Which price category generates the highest revenue?
def revenue_by_price_category():
    connection, cursor = get_connection()
    query="""
    SELECT
        r.price_category,
        COUNT(o.order_id) AS total_orders,
        ROUND(SUM(o.order_value),2) AS total_revenue
    FROM restaurants r
    INNER JOIN orders o
    ON r.name = o.restaurant_name
    GROUP BY r.price_category
    ORDER BY total_revenue DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df
    
    

# A9: Do highly rated restaurants receive more orders?
def rating_vs_order_count():
    connection, cursor = get_connection()
    query="""
    SELECT
        r.rating_category,
        COUNT(o.order_id) AS total_orders,
        ROUND(AVG(o.order_value),2) AS avg_order_value
    FROM restaurants r
    INNER JOIN orders o
    ON r.name = o.restaurant_name
    GROUP BY r.rating_category
    ORDER BY total_orders DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df
    
    

# A10: Which locations have the highest average order value?
def average_order_value_by_location():
    connection, cursor = get_connection()
    query="""
    SELECT
        r.location,
        COUNT(o.order_id) AS total_orders,
        ROUND(AVG(o.order_value),2) AS avg_order_value
    FROM restaurants r
    INNER JOIN orders o
    ON r.name = o.restaurant_name
    GROUP BY r.location
    ORDER BY avg_order_value DESC;
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df    
    
    

# A11: Top 5 restaurants by revenue
def top_5_restaurants_by_revenue():
    connection, cursor = get_connection()
    query="""
    SELECT
        restaurant_name,
        ROUND(SUM(order_value),2) AS total_revenue
    FROM orders
    GROUP BY restaurant_name
    ORDER BY total_revenue DESC
    LIMIT 5;   
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df
    
    

# A12: Highest revenue premium restaurants
def highest_revenue_premium_restaurants():
    connection, cursor = get_connection()
    query="""
    SELECT
        r.name,
        r.price_category,
        ROUND(SUM(o.order_value),2) AS total_revenue
    FROM restaurants r
    INNER JOIN orders o
    ON r.name = o.restaurant_name
    WHERE r.price_category = 'Premium'
    GROUP BY r.name, r.price_category
    ORDER BY total_revenue DESC;  
    """
    cursor.execute(query)
    rows= cursor.fetchall()
    columns= [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    connection.close()
    return df


def close_connection():
    cursor.close()
    connection.close()