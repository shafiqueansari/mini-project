import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hotel_db"
)
cursor = conn.cursor()

# ---------------- GUEST CRUD ------------------

def create_guest(name, phone, email):
    cursor.execute("INSERT INTO guests (name, phone, email) VALUES (%s, %s,%s)", (name, phone, email))
    conn.commit()
    print("✅ Guest created!")

def read_guests():
    cursor.execute("SELECT * FROM guests")
    for row in cursor.fetchall():
        print(row)

def update_guest(guest_id, name=None, phone=None, email=None):
    updates = []
    params = []
    if name:
        updates.append("name = %s")
        params.append(name)
    if phone:
        updates.append("phone = %s")
        params.append(phone)
    if email:
        updates.append("email = %s")
        params.append(email)
    params.append(guest_id)
    query = f"UPDATE guests SET {', '.join(updates)} WHERE guest_id = %s"
    cursor.execute(query, tuple(params))
    conn.commit()
    print("✅ Guest updated!")

def delete_guest(guest_id):
    cursor.execute("DELETE FROM guests WHERE guest_id = %s", (guest_id,))
    conn.commit()
    print("🗑️ Guest deleted!")

# ---------------- ROOM CRUD ------------------

def create_room(number, r_type, price):
    cursor.execute("INSERT INTO rooms (room_number, room_type, price_per_night) VALUES (%s, %s, %s)", (number, r_type, price))
    conn.commit()
    print("✅ Room created!")

def read_rooms():
    cursor.execute("SELECT * FROM rooms")
    for room in cursor.fetchall():
        print(room)

def update_room(room_id, number=None, r_type=None, price=None):
    updates = []
    params = []
    if number:
        updates.append("room_number = %s")
        params.append(number)
    if r_type:
        updates.append("room_type = %s")
        params.append(r_type)
    if price:
        updates.append("price_per_night = %s")
        params.append(price)
    params.append(room_id)
    query = f"UPDATE rooms SET {', '.join(updates)} WHERE room_id = %s"
    cursor.execute(query, tuple(params))
    conn.commit()
    print("✅ Room updated!")

def delete_room(room_id):
    cursor.execute("DELETE FROM rooms WHERE room_id = %s", (room_id,))
    conn.commit()
    print("🗑️ Room deleted!")

# ---------------- BOOKINGS ------------------

def create_booking(guest_id, room_id, check_in, check_out):
    cursor.execute("SELECT is_available FROM rooms WHERE room_id = %s", (room_id,))
    if cursor.fetchone()[0]:
        cursor.execute("INSERT INTO bookings (guest_id, room_id, check_in_date, check_out_date) VALUES (%s, %s, %s, %s)", 
                       (guest_id, room_id, check_in, check_out))
        cursor.execute("UPDATE rooms SET is_available = FALSE WHERE room_id = %s", (room_id,))
        conn.commit()
        print("✅ Booking created!")
    else:
        print("❌ Room not available!")

def read_bookings():
    cursor.execute("SELECT * FROM bookings")
    for booking in cursor.fetchall():
        print(booking)

def delete_booking(booking_id):
    cursor.execute("SELECT room_id FROM bookings WHERE booking_id = %s", (booking_id,))
    room_id = cursor.fetchone()[0]
    cursor.execute("DELETE FROM bookings WHERE booking_id = %s", (booking_id,))
    cursor.execute("UPDATE rooms SET is_available = TRUE WHERE room_id = %s", (room_id,))
    conn.commit()
    print("🗑️ Booking cancelled!")

# ---------------- CLI MENU ------------------

def main_menu():
    while True:
        print("\n--- Hotel Management ---")
        print("1. Create Guest")
        print("2. View Guests")
        print("3. Update Guest")
        print("4. Delete Guest")
        print("5. Create Room")
        print("6. View Rooms")
        print("7. Update Room")
        print("8. Delete Room")
        print("9. Book Room")
        print("10. View Bookings")
        print("11. Cancel Booking")
        print("12. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            create_guest(name, phone, email)
        elif choice == '2':
            read_guests()
        elif choice == '3':
            guest_id = int(input("Guest ID: "))
            name = input("New name (blank to skip): ") or None
            phone = input("New phone (blank to skip): ") or None
            email = input("New email (blank to skip): ") or None
            update_guest(guest_id, name, phone, email)
        elif choice == '4':
            delete_guest(int(input("Guest ID: ")))
        elif choice == '5':
            number = input("Room Number: ")
            r_type = input("Room Type: ")
            price = float(input("Price per Night: "))
            create_room(number, r_type, price)
        elif choice == '6':
            read_rooms()
        elif choice == '7':
            room_id = int(input("Room ID: "))
            number = input("New Number (blank to skip): ") or None
            r_type = input("New Type (blank to skip): ") or None
            price = input("New Price (blank to skip): ")
            price = float(price) if price else None
            update_room(room_id, number, r_type, price)
        elif choice == '8':
            delete_room(int(input("Room ID: ")))
        elif choice == '9':
            guest_id = int(input("Guest ID: "))
            room_id = int(input("Room ID: "))
            check_in = input("Check-in date (YYYY-MM-DD): ")
            check_out = input("Check-out date (YYYY-MM-DD): ")
            create_booking(guest_id, room_id, check_in, check_out)
        elif choice == '10':
            read_bookings()
        elif choice == '11':
            booking_id = int(input("Booking ID: "))
            delete_booking(booking_id)
        elif choice == '12':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main_menu()
