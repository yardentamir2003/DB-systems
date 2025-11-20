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
# Return driver's name and minimum time for lap
SELECT 
    w.Winner AS driver,
    MIN(f.time) AS min_time
    
# Left join by winner=driver
FROM winners w
LEFT JOIN fastest_laps_updated f
ON w.Winner = f.Driver

# Inner query
WHERE w.Winner = (
    SELECT w1.Winner
    FROM winners w1
    WHERE YEAR(STR_TO_DATE(w1.Date, '%Y-%m-%d')) = 2000
    GROUP BY w1.Winner
    
    # Order by total laps and return first element(=max)
    ORDER BY SUM(w1.Laps) DESC
    LIMIT 1
)
GROUP BY w.Winner;
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))
 