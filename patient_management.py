import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # Change to your MySQL username
    password="root",  # Change to your MySQL password
    database="hospital_db"
)
cursor = conn.cursor()

def add_patient():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    diagnosis = input("Enter diagnosis: ")
    sql = "INSERT INTO patients (name, age, gender, diagnosis) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, age, gender, diagnosis))
    conn.commit()
    print("✅ Patient added successfully.\n")

def view_patients():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_patient():
    pid = int(input("Enter patient ID: "))
    cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (pid,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("❌ Patient not found.")

def update_patient():
    pid = int(input("Enter patient ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    gender = input("Enter new gender: ")
    diagnosis = input("Enter new diagnosis: ")
    sql = "UPDATE patients SET name=%s, age=%s, gender=%s, diagnosis=%s WHERE patient_id=%s"
    cursor.execute(sql, (name, age, gender, diagnosis, pid))
    conn.commit()
    print("🔄 Patient updated successfully.\n")

def delete_patient():
    pid = int(input("Enter patient ID to delete: "))
    cursor.execute("DELETE FROM patients WHERE patient_id = %s", (pid,))
    conn.commit()
    print("🗑️ Patient deleted successfully.\n")

def main():
    while True:
        print("\nPatient Management System")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient Info")
        print("5. Delete Patient")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            update_patient()
        elif choice == '5':
            delete_patient()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

