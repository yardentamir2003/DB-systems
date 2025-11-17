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
    driver_avg.nationality,
    driver_avg.avg_pts,
    flaps.min_time,
    wins.latest
FROM (
    SELECT 
        d.Nationality AS nationality,
        AVG(d.pts) AS avg_pts
    FROM 
        drivers d
    GROUP BY 
        d.Nationality
) driver_avg
LEFT JOIN (
    SELECT 
        d.Nationality AS nationality,
        MIN(f.time) AS min_time
    FROM 
        drivers d
        LEFT JOIN fastest_laps f ON d.driver = f.driver
    GROUP BY 
        d.Nationality
) flaps ON driver_avg.nationality = flaps.nationality
LEFT JOIN (
    SELECT 
        d.Nationality AS nationality,
        MAX(w.date) AS latest
    FROM 
        drivers d
        LEFT JOIN winners w ON d.driver = w.winner
    GROUP BY 
        d.Nationality
) wins ON driver_avg.nationality = wins.nationality;


 """)
 print(', '.join(str(row) for row in cursor.fetchall()))

# CHECK WHY NOT WORKING????????????????????????????????????????????????

# SELECT 
#     d.Nationality,
#     AVG(d.pts) AS avg_pts,
# 	MIN(f.time) AS min_time,    
#     MAX(w.date) AS latest  

# FROM drivers d
# LEFT JOIN fastest_laps f 
#        ON d.driver = f.driver
# LEFT JOIN winners w
#        ON d.driver = w.winner
# GROUP BY d.Nationality