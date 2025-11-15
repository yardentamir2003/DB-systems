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
SELECT f.driver, MIN(f.time) AS min_time
FROM fastest_laps f
JOIN (
    SELECT winner AS driver
    FROM winners
    WHERE YEAR(date) = 2000
    GROUP BY winner
    HAVING SUM(laps) = (
        SELECT MAX(total_laps)
        FROM (
            SELECT winner, SUM(laps) AS total_laps
            FROM winners
            WHERE YEAR(date) = 2000
            GROUP BY winner
        ) AS t
    )
) AS max_driver
ON f.driver = max_driver.driver
GROUP BY f.driver;
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))
 
 
 # total number of laps in the year 2000. not sure if that was the instruction - SOULD ASK IN THE MOODLE!