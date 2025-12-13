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
    
    # Update UK number to 7 where US number is 9
    cursor.execute("""
    UPDATE size
    SET uk_number = 7
    WHERE us_number = 9
    """)

    # !!! Commit the transaction to save the changes to the database!!!
    mydb.commit() 
    cursor.close()
    mydb.close()
