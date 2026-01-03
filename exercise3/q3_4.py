import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hosppdd", 
        port='3307'
    )

    # Create Disease table
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS disease (
    disease_id INT PRIMARY KEY,
    name VARCHAR(31) NOT NULL,
    severity INT,
    medicine INT,
    FOREIGN KEY (medicine) REFERENCES medicine(medicine_id))
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
