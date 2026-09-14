import os
import statistics
from datetime import datetime
patients = {}
def register_patient(patient_id, name, age, gender):
    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender
    }
    print("Patient registered:", name)


def show_patients():
    print("\n--- Patient List ---")
    for pid in patients:
        info = patients[pid]
        print("ID:", pid, "| Name:", info["name"],
              "| Age:", info["age"], "| Gender:", info["gender"])
appointments = []
def schedule_appointment(patient_name, doctor_name, date):
    # add one appointment to the list
    appointment = patient_name + " with " + doctor_name + " on " + date
    appointments.append(appointment)
    print("Appointment added:", appointment)


def show_appointments():
    print("\n--- Appointments ---")
    for item in appointments:
        print(item)

def save_medical_record(patient_name, diagnosis):
    file = open("medical_records.txt", "a")   # "a" = append mode
    file.write(patient_name + " - " + diagnosis + "\n")
    file.close()
    print("Medical record saved for", patient_name)


def show_medical_records():
    print("\n--- Medical Records ---")
    file = open("medical_records.txt", "r")   # "r" = read mode
    for line in file:
        print(line.strip())
    file.close()
doctor1 = ("Dr. Ayesha Khan", "Cardiology")
doctor2 = ("Dr. Rohan Mehta", "Orthopedics")

doctors = [doctor1, doctor2] 
def show_doctors():
    print("\n--- Doctors ---")
    for doc in doctors:
        print("Name:", doc[0], "| Specialization:", doc[1])
class Bill:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.total_amount = 0

    def add_charge(self, amount):
        self.total_amount = self.total_amount + amount

    def show_bill(self):
        print("Bill for", self.patient_name, "-> Total: Rs.", self.total_amount)
def generate_report():
    print("\n--- Hospital Report ---")
    print("Report generated on:", datetime.now())
    print("Total patients:", len(patients))
    print("Total appointments:", len(appointments))
    print("Total doctors:", len(doctors))

# Step 1: Register patients
register_patient("P1", "Amit Sharma", 34, "Male")
register_patient("P2", "Priya Nair", 28, "Female")
show_patients()

# Step 2: Show doctor list
show_doctors()

# Step 3: Schedule appointments
schedule_appointment("Amit Sharma", "Dr. Ayesha Khan", "10-Sep-2026")
schedule_appointment("Priya Nair", "Dr. Rohan Mehta", "11-Sep-2026")
show_appointments()

# Step 4: Save and show medical records
save_medical_record("Amit Sharma", "Hypertension")
save_medical_record("Priya Nair", "Seasonal Flu")
show_medical_records()

# Step 5: Create bills using the Bill class
bill1 = Bill("Amit Sharma")
bill1.add_charge(500)
bill1.add_charge(800)
bill1.show_bill()

bill2 = Bill("Priya Nair")
bill2.add_charge(400)
bill2.show_bill()

# Step 6: Generate final report
generate_report()