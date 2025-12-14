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
    
    # Create a view summarizing total sales per shoe
    cursor.execute("""
    CREATE VIEW total_sales_per_shoe AS
    SELECT s.shoe_id, s.shoe_name, COALESCE(SUM(s.price), 0) AS total_revenue
    FROM shoe s
    LEFT JOIN order_shoe os ON s.shoe_id = os.shoe_id
    GROUP BY s.shoe_id, s.shoe_name;
    """)

    # !!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
