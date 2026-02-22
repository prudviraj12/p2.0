students = {}

while True:
    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print("Student already exists.")
        else:
            students[name] = "Not Marked"
            print("Student added.")

    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            status = input("Enter P for Present or A for Absent: ")
            if status == "P":
                students[name] = "Present"
            elif status == "A":
                students[name] = "Absent"
            else:
                print("Invalid input.")
        else:
            print("Student not found.")

    elif choice == "3":
        if len(students) == 0:
            print("No students available.")
        else:
            for name in students:
                print(name, ":", students[name])

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")