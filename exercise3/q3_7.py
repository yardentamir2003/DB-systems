import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hosppdd", 
        port='3307'
    )

    # Create Rate table
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rate (
    rating_id INT PRIMARY KEY,
    rating INT CHECK (rating >= 1 AND rating <= 10),
    patient_id INT,
    doctor_id INT,
    hospital_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id, hospital_id) REFERENCES doctor(doctor_id, hospital_id))
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
