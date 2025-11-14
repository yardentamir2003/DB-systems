import mysql.connector
if __name__ == '__main__':
 mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="f1_data",
 port='3307',
 )
 cursor = mydb.cursor()
 cursor.execute("""
SELECT DISTINCT driver 
FROM drivers
WHERE drivers.nationality = 'BRA'
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))