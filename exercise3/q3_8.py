import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hosppdd", 
        port='3307'
    )

    # Create Opinion table
    cursor = mydb.cursor()
    cursor.execute("""
    ## PUT YOUR CREATE QUERY ##
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
