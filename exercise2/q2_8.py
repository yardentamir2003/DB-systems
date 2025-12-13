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
    
    # Create company_order table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS company_order (
        order_id INT PRIMARY KEY,
        order_date DATETIME NOT NULL)
    """)

    # !!! Commit the transaction to save the changes to the database!!!
    mydb.commit()  
    cursor.close()
    mydb.close()
