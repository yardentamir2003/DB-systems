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
SELECT w1.`Grand Prix` AS grandPrix1, w2.`Grand Prix` AS grandPrix2

# Self join on winners table
FROM winners w1
JOIN winners w2

# Pair grand prix from w1 and w2 if they have the same number of laps 
ON w1.Laps = w2.Laps 

# Avoid pairing grand prix with itself
AND w1.`Grand Prix` < w2.`Grand Prix`
WHERE w1.Laps > 120
ORDER BY grandPrix1 ASC, grandPrix2 ASC;
 """)
 print(', '.join(str(row) for row in cursor.fetchall()))
 