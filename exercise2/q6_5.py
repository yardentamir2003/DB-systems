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
    
    # Update UK number to 9 where US number is 11
    cursor.execute("""
    UPDATE size
    SET uk_number = 9
    WHERE us_number = 11
    """)

    # !!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
