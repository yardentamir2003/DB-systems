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
    
    # Create shoe table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shoe (
        shoe_id INT PRIMARY KEY,
        shoe_name VARCHAR(31) NOT NULL,
        price SMALLINT NOT NULL)
    """)

    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
