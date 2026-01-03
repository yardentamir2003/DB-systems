import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="", 
        port='3307'
    )

    # Create database hosppdd
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE DATABASE hosppdd;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
