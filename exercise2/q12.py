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
    
    # Find all shoes that have not been ordered without duplicates
    cursor.execute("""
    SELECT s.shoe_name
    FROM shoe s
    LEFT JOIN order_shoe os ON s.shoe_id = os.shoe_id
    GROUP BY s.shoe_id
    HAVING COUNT(os.order_id) = 0;
    """)

    # Fetch and print results as required by Listing 2
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
