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
    d.Nationality,
    AVG(d.pts) AS avg_pts,
    MIN(STR_TO_DATE(f.time, '%i:%s.%f')) AS min_time,
    MAX(w.date) AS latest
FROM drivers d
LEFT JOIN fastest_laps f 
       ON d.driver = f.driver
LEFT JOIN winners w
       ON d.driver = w.winner
GROUP BY d.Nationality
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))
