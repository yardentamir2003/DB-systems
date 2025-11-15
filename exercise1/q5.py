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
SELECT team, AVG(pts) AS avg_pts
FROM teams
WHERE team IN (
    SELECT DISTINCT Car
    FROM fastest_laps
    WHERE 
        (MINUTE(STR_TO_DATE(Time, '%i:%s.%f')) * 60 +
         SECOND(STR_TO_DATE(Time, '%i:%s.%f'))) < 120
)
GROUP BY team
ORDER BY avg_pts DESC;

 """)
 print(', '.join(str(row) for row in cursor.fetchall()))
 