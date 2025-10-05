import os

def get_documents_folder():
    try:
        doc_path = os.path.expanduser('~/Documents')
        return doc_path
    except Exception as e:
        print(f"Error accessing Documents folder: {e}")
        return None

def menu():
    while True:
        print("\n--- Student Records ---")
        print("1. Register Student")
        print("2. Open Student Record")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            open_student_record()
        elif choice == "3":
            exit_program()
            break
        else:
            print("Invalid choice, please try again.")

def register_student():
    print("\n--- Register Student ---")
    student_no = input("Enter Student No.: ")
    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    middle_initial = input("Enter Middle Initial: ")
    program = input("Enter Program: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender (Male/Female/Other): ")
    birthday = input("Enter Birthday (DD/MM/YYYY): ")
    contact_no = input("Enter Contact No.: ")

    data = [
        f"Student No.: {student_no}",
        f"Full Name: {last_name}, {first_name} {middle_initial}.",
        f"Program: {program}",
        f"Age: {age}",
        f"Gender: {gender}",
        f"Birthday: {birthday}",
        f"Contact No.: {contact_no}"
    ]

    doc_path = get_documents_folder()
    if doc_path:
        file_path = os.path.join(doc_path, f"{student_no}.txt")
        try:
            with open(file_path, "w") as file:
                for line in data:
                    file.write(line + "\n")
            print(f"Student {first_name} {last_name} registered successfully!")
        except Exception as e:
            print(f"Error saving record: {e}")
    else:
        print("Failed to access the Documents folder.")

def open_student_record():
    print("\n--- Open Student Record ---")
    student_no = input("Enter the Student No. to open their record: ")
    doc_path = get_documents_folder()
    if doc_path:
        file_path = os.path.join(doc_path, f"{student_no}.txt")
        try:
            with open(file_path, "r") as file:
                print(f"\n--- Student Record for {student_no} ---")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("❌ Student record not found.")
        except Exception as e:
            print(f"Error reading record: {e}")
    else:
        print("Failed to access the Documents folder.")

def exit_program():
    print("\nGoodbye! Thank you for using the Student Records Management System.")

if _name_ == "_main_":
    menu()
