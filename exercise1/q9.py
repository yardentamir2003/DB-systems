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
WITH

# Average points for nationality
avg_points AS (
    SELECT d.Nationality, AVG(d.pts) AS avg_pts
    FROM drivers_updated d
    GROUP BY d.Nationality
),

# Minimum time of a fastest lap for nationality
min_fastest AS (
	SELECT d.Nationality, MIN(f.Time) AS min_time
    FROM drivers_updated d
    JOIN fastest_laps_updated f 
    ON d.Driver = f.Driver
    GROUP BY d.Nationality
),

# Most recent win for each nationality
latest_win AS (
    SELECT d.Nationality, MAX(w.Date) AS latest
    FROM drivers_updated d
    JOIN winners w ON d.Driver = w.Winner
    GROUP BY d.Nationality
)

# Return requiered fields
SELECT a.Nationality, a.avg_pts, m.min_time, l.latest
FROM avg_points a
LEFT JOIN min_fastest m 
ON a.Nationality = m.Nationality
LEFT JOIN latest_win l 
ON a.Nationality = l.Nationality
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))


