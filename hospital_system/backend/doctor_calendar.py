import sqlite3 #imports sqlite libray into code

print("Doctor Availability") #Terminal header

doctor_id = input("Enter doctor ID to check their availability: ") #asks user for the doctors ID

conn = sqlite3.connect('../db/hospital.db') #connects to the database
cursor = conn.cursor()

cursor.execute("SELECT name, available_slots FROM doctors WHERE id=?", (doctor_id)) #gets informaiton from the database
doctor = cursor.fetchone()
conn.close() #closes the connection

if doctor:
    print(f"Doctor: {doctor[0]}")
    print(f"Available Slots: {doctor[1]}")
else:
    print("Doctor not found")

#the above if and else displays the availability, if not it displays an error command