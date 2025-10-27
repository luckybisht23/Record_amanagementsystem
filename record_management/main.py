
import database

def menu():
    print("""
    === Record Management System ===
    1. Add Record
    2. View Records
    3. Update Record
    4. Delete Record
    5. Exit
    """)

def main():
    database.create_table()
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            database.add_record(name, email, phone)
        elif choice == "2":
            database.view_records()
        elif choice == "3":
            record_id = input("Enter record ID: ")
            name = input("New name: ")
            email = input("New email: ")
            phone = input("New phone: ")
            database.update_record(record_id, name, email, phone)
        elif choice == "4":
            record_id = input("Enter record ID to delete: ")
            database.delete_record(record_id)
        elif choice == "5":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
