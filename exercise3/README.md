Question 1:
didn't finish ER diagram.
1 - patient has 0/1 previous disease and exactly 1 new disease
2 - consult doctor
3 - unique doctors id in each hospial
4 - rating is between 1-10 (my addition)

Question 2:
Patient(patient_id, name, height, weight, gender, previous_disease_id, new_disease_id, patient_doctor_id, patient_hospital_id)
PK: patient_id
FK:
Patient(previous_disease_id)=Disease(disease_id)
Patient(new_disease_id)=Disease(disease_id)
Patient(patient_doctor_id, patient_hospital_id)=Doctor(doctor_id, hospital_id)


Disease(disease_id, name, severity, medicine)
PK: disease_id
FK: 
Disease(medicine)=Medicine(medicine_id)


Medicine(medicine_id, name)
PK: medicine_id


Hospital(hospital_id, name)
PK: hospital_id


Doctor(doctor_id, hospital_id, name, consult_doctor_id, consult_doctor_hospital)
PK: doctor_id, hospital_id
FK:
Doctor(consult_doctor_id, consult_doctor_hospital)=Doctor(doctor_id, hospital_id)
Doctor(hospital_id)=Hospital(hospital_id)


Rate(rating_id, rating, patient, doctor_id, hospital_id)
PK: rating_id
FK:
Rate(patient)=Patient(patient_id)
Rate(doctor_id, hospital_id)=Doctor(doctor_id, hospital_id)

Opinion(rating_id, comment)
PK: rating_id
FK:
Opinion(rating_id) = Rate(rating_id)