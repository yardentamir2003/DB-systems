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
    
    # Add uk_number column, UK sizes initialized to NULL 
    cursor.execute("""
    ALTER TABLE size 
    ADD uk_number TINYINT;
    """)

    # !!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()
