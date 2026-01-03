import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hosppdd", 
        port='3307'
    )

    # Create Hospital table
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hospital (
    hospital_id INT PRIMARY KEY,
    name VARCHAR(31) NOT NULL)
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
