import sqlite3 #imports SQLite to handle to database
import os #imports os for folder pathing

os.makedirs('../db', exist_ok=True) #checks to see if the db folder exists

conn = sqlite3.connect('../db/hospital.db')
cursor = conn.cursor() #allows to execute SQL commands

#table creation for patients in dbeaver
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    password TEXT
)
''')

#table creation for doctors in dbeaver
cursor.execute('''
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT,
    available_slots TEXT
)
''')

#table creation for appointments in dbeaver
cursor.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    doctor_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    FOREIGN KEY(doctor_id) REFERENCES doctors(id)
)
''')

conn.commit() #saves all changes database changes
conn.close() # closes connection
print("Database and tables created successfully") #confirms if databse and tables were created