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
# Use distinct to avoid duplicates
SELECT DISTINCT driver 
FROM drivers_updated

# Return all drivers from Brazil
WHERE nationality = 'BRA'
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))