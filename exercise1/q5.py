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
# Return car and average points 
SELECT t.Car, AVG(t.PTS) AS avg_pts
FROM teams_updated t

# Only for cars with fastest lap below 2 minutes
WHERE t.Car IN (
	SELECT DISTINCT Car
	FROM fastest_laps_updated f
	WHERE MINUTE(STR_TO_DATE(f.Time, '%i:%s.%f')) < 2
)
GROUP BY t.Car
ORDER BY avg_pts DESC;
 

 """)
 print(', '.join(str(row) for row in cursor.fetchall()))
 