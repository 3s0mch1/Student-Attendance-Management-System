students = {}
attendance = {}

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    students[student_id] = name
    print("Student added successfully.\n")

def mark_attendance():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        status = input("Enter Attendance (Present/Absent): ")
        attendance[student_id] = status
        print("Attendance marked.\n")
    else:
        print("Student not found.\n")

def view_attendance():
    print("\nAttendance Report")
    for sid, status in attendance.items():
        print(students[sid], "-", status)
    print()

while True:
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")
