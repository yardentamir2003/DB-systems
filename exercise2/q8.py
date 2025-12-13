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
    
    # Executing the SQL Query
    cursor.execute("""
    ## PUT YOUR QUERY HERE ##
    """)

    # Fetch and print results as required by Listing 2
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
