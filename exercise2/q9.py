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
    
    # List all shoe names with the count of sizes available for each
    # Use left join to include shoes that don’t have any size
    cursor.execute("""
    SELECT s.shoe_name, COUNT(ss.shoe_id)
    FROM shoe s
    LEFT JOIN shoe_size ss ON s.shoe_id = ss.shoe_id
    GROUP BY s.shoe_id;
    """)

    # Fetch and print results as required by Listing 2
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
