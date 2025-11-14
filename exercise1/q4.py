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
SELECT COUNT(*) AS 'wins'
FROM winners
WHERE YEAR(date) = 2001

# Find team's car who had most wins in 1999
AND car = (
	SELECT car
	FROM winners
	WHERE YEAR(date) = 1999
	GROUP BY car
      
	# Sort in descending order and return the first element(=max element) 
	ORDER BY COUNT(*) DESC
	LIMIT 1
  );
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))