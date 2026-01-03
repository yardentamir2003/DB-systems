Question 1:
didn't finish ER diagram.
1 - patient has 0/1 previous disease and exactly 1 new disease
2 - consult doctor
3 - unique doctors id in each hospial

Question 2:
Patient(patient_id, name, height, weight, gender, previous_disease, new_disease, doctor)
PK: patient_id
FK:

Disease(disease_id, name, severity, medicine)
PK: disease_id
FK: 

Hospital(hospital_id, doctors)
PK: hospital_id
FK:

Doctor(doctor_id, name, consult_doctor, hospital)
PK: doctor_id
FK:

Rate(rating_id, rating, patient, doctor)
PK: rating_id
FK:

Opinion(comment)