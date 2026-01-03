import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hosppdd", 
        port='3307'
    )

    # Create Doctor table
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctor (
    doctor_id INT,
    hospital_id INT,
    name VARCHAR(31) NOT NULL,
    consult_doctor_id INT,
    consult_doctor_hospital INT,
    PRIMARY KEY (doctor_id, hospital_id),
    FOREIGN KEY (hospital_id) REFERENCES hospital(hospital_id),
    FOREIGN KEY (consult_doctor_id, consult_doctor_hospital) REFERENCES doctor(doctor_id, hospital_id))
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
