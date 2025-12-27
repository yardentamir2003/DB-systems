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
    
    # Create country table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS country (
        country_id INT PRIMARY KEY,
        country_name VARCHAR(63) NOT NULL)
    """)

    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
