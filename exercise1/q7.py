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
SELECT DISTINCT drivers.Driver AS driver
From winners

# Join drivers and winners tables by 'name code' field
JOIN drivers ON winners.`Name Code` = drivers.`Name Code`
WHERE winners.Car = 'Ferrari' OR drivers.Nationality = 'FRA'

# Sort alphabetically
ORDER BY drivers.Driver ASC
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))