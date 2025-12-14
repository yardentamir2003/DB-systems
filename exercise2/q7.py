import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes", 
        port='3307'
    )

    cursor = mydb.cursor()
    
    # Return firat name, last name and total revenue of each customer
    cursor.execute("""
    # Use COALESCE if customer does'nt have any orders. return amout=0 instead of NULL
    SELECT c.first_name, c.last_name, COALESCE(SUM(s.price), 0)
    FROM customer c
    LEFT JOIN order_customer oc ON c.customer_id = oc.customer_id
    LEFT JOIN order_shoe os ON oc.order_id = os.order_id
    LEFT JOIN shoe s ON os.shoe_id = s.shoe_id
    GROUP BY c.customer_id 
    """)

    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
