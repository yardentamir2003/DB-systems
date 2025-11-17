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
    w.Winner AS driver,
    TIME_FORMAT(MIN(STR_TO_DATE(f.Time, '%i:%s.%f')), '%i:%s.%f') AS min_time
FROM winners w
LEFT JOIN fastest_laps f
ON w.Winner = f.Driver
WHERE w.Winner = (
    SELECT w1.Winner
    FROM winners w1
    WHERE YEAR(STR_TO_DATE(w1.Date, '%Y-%m-%d')) = 2000
    GROUP BY w1.Winner
    ORDER BY SUM(w1.Laps) DESC
    LIMIT 1
)
GROUP BY w.Winner;
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))
 
 
 # Is it llowed to use TIME_FORMAT