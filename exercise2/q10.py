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
    
    # Combine the list of shoe names from the inventory with the list of special upcoming collection names
    cursor.execute("""
    # Use aliasing for hard code a value = Inventory
    SELECT s.shoe_name AS name, 'Inventory' AS source
    FROM shoe s
    UNION
    # Use aliasing for hard code a value = Inventory
    SELECT u.collection_name AS name, 'Upcoming Release' AS source
    FROM upcoming u;
    """)

    # Fetch and print results as required by Listing 2
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
