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
    
    # Find the average price of shoes available in each size, ordered from highest to lowest
    cursor.execute("""
    SELECT size.european_number, size.us_number, AVG(shoe.price) AS average_price
    FROM shoe
    JOIN shoe_size ss ON shoe.shoe_id = ss.shoe_id
    JOIN size ON ss.size_id = size.size_id
    GROUP BY size.size_id
    ORDER BY average_price DESC;
    """)

    # Fetch and print results as required by Listing 2
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
