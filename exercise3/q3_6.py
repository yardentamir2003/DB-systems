import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hosppdd", 
        port='3307'
    )

    # Create Patient table
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient (
    patient_id INT PRIMARY KEY,
    name VARCHAR(31) NOT NULL,
    height FLOAT,
    weight FLOAT,
    gender VARCHAR(31),
    previous_disease_id INT,
    new_disease_id INT NOT NULL,
    patient_doctor_id INT,
    patient_hospital_id INT,
    FOREIGN KEY (previous_disease_id) REFERENCES disease(disease_id),
    FOREIGN KEY (new_disease_id) REFERENCES disease(disease_id),
    FOREIGN KEY (patient_doctor_id, patient_hospital_id) REFERENCES doctor(doctor_id, hospital_id))
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
