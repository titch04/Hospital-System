import sqlite3 #imports sqlite for access to database

print("Appointment Booking") #Header

name = input("Enter your name: ")
doctor_id = input("Enter doctor ID: ")#allows user to input doctor id
date = input("Enter dateJord (YYYY-MM-DD): ") #allows user to input the date
time = input("Enter time (HH:MM): ") #allows user to input a specific time

conn = sqlite3.connect('../db/hospital.db') #connects to database
cursor = conn.cursor()


cursor.execute(
    "INSERT INTO appointments (patient_name, doctor_id, date, time) VALUES (?, ?, ?, ?)",
    (name, doctor_id, date, time)
) #creates new appointment into database

conn.commit() #saves any changes
conn.close() #close connection

print (f"Appointment has been booked successfully for {name} with Doctor ID {doctor_id} on {date} at {time}. Thank you for making a booking.")
#confirms the booking has been made for user