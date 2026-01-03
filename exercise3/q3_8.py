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
    CREATE TABLE IF NOT EXISTS opinion (
    rating_id INT PRIMARY KEY,
    comment TEXT,
    FOREIGN KEY (rating_id) REFERENCES rate(rating_id))
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
