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
SELECT
    (
        (SELECT SUM(pts) FROM teams WHERE Car = 'Ferrari') -
        (SELECT SUM(pts) FROM teams WHERE Car = 'Maserati')
    ) AS diff;
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))