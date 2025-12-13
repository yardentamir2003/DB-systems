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
    
    # Add pre_order_avaliable column to upcoming table, set default value to 0
    cursor.execute("""
    ALTER TABLE upcoming 
    ADD pre_order_avaliable BIT(1) DEFAULT 0;
    """)

    # !!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
