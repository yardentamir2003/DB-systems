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
    
    # Create city table, define foreign key
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS city (
        city_id INT PRIMARY KEY,
        city_name VARCHAR(63) NOT NULL,
        country_id INT NOT NULL,
        FOREIGN KEY (country_id) REFERENCES country(country_id))
    """)

    print(", ".join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
