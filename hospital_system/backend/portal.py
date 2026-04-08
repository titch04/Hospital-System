import sqlite3 #imports sqlite library

print ("Portal for Patients")

patient_name = input("Please enter your full name to view appointments: ")
#allows users to input their name to view their bookings

conn = sqlite3.connect('../db/hospital.db')
cursor = conn.cursor()
#connects to the database

cursor.execute(
    "SELECT doctor_id, date, time FROM appointments WHERE patient_name=?",
    (patient_name,) #pulls information from the databse
)
appointments = cursor.fetchall() #stores the results in the table
conn.close()  #closes the connection

if appointments:
    print(f"\nAppointments for {patient_name}:")
    for appt in appointments:
        print(f"Doctor ID: {appt[0]}, Date: {appt[1]}, Time: {appt[2]}") #this whole section prints the patients appointment date and time along with their name
else:
    print("No appointments found") #prints if no appointment has been found