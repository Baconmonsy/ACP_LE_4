import os # to find the Documents folder

# Get the path to the Documents folder
documents_path = os.path.expanduser("~/Documents")

# Create the Documents folder if it doesn't exist
if not os.path.exists(documents_path):
    os.makedirs(documents_path)

# Start the menu loop
while True:
    print("\n=== Student Records Menu ===")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Option 1: Register a new student   
    
    if choice == "1":
        print("\n--- Register Student ---")
        student_no = input("Student No.: ")
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        middle_initial = input("Middle Initial: ")
        program = input("Program: ")
        age = input("Age: ")
        gender = input("Gender: ")
        birthday = input("Birthday: ")
        contact_no = input("Contact No.: ")

        # Save the details in a list
        data = [
            f"Student No.: {student_no}",
            f"Full Name: {last_name}, {first_name} {middle_initial}.",
            f"Program: {program}",
            f"Age: {age}",
            f"Gender: {gender}",
            f"Birthday: {birthday}",
            f"Contact No.: {contact_no}"
        ]

        # Create file path (like Documents/123456.txt)
        file_path = os.path.join(documents_path, f"{student_no}.txt")

        # Write the data to the file
        try:
            with open(file_path, "w") as f:
                for line in data:
                    f.write(line + "\n")
            print("✅ Student registered successfully!")
        except Exception as e:
            print(f"❌ Error: {e}")

    # Option 2: Open a student record
    elif choice == "2":
        print("\n--- Open Student Record ---")
        student_no = input("Enter Student No.: ")
        file_path = os.path.join(documents_path, f"{student_no}.txt")

        try:
            with open(file_path, "r") as f:
                print("\n📄 Student Record:")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("❌ Student record not found.")

    # Option 3: Exit the program
    elif choice == "3":
        print("\n👋 Goodbye!")
        break

    # Wrong input
    else:
        print("❌ Invalid choice. Try again.")
