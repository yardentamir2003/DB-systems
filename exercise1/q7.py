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
SELECT DISTINCT Driver
FROM drivers_updated d 

# Left join drivers, winners. avoid data loss (not every driver is a winner)
LEFT JOIN winners w
ON d.Driver = w.Winner
WHERE w.Car='Ferrari' OR d.Nationality='ARG'

# Order matching drivers alphabetically
ORDER BY Driver ASC
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))