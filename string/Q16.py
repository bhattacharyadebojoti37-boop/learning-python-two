# Student Management System
students = []

# Function to add a student
def add_student():
    try:
        roll = int(input("Enter Roll Number: "))

        # Check if roll number already exists
        for student in students:
            if student["roll"] == roll:
                print("Roll number already exists!")
                return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        student = {
            "roll": roll,
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    except ValueError:
        print("Please enter valid data.")


# Function to display students
def display_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n----- Student Details -----")

    for student in students:
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("---------------------------")


# Function to search student
def search_student():
    try:
        roll = int(input("Enter Roll Number to search: "))

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Marks:", student["marks"])
                return

        print("Student not found.")

    except ValueError:
        print("Invalid roll number.")


# Function to find topper
def find_topper():
    if len(students) == 0:
        print("No students available.")
        return

    topper = max(students, key=lambda student: student["marks"])

    print("\n----- Topper -----")
    print("Roll Number:", topper["roll"])
    print("Name:", topper["name"])
    print("Marks:", topper["marks"])


# Function to sort students according to marks
def sort_students():
    if len(students) == 0:
        print("No students available.")
        return

    sorted_students = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    print("\n----- Students by Marks -----")

    for student in sorted_students:
        print(
            student["roll"],
            student["name"],
            student["marks"]
        )


# Function to save data into a file
def save_data():
    with open("students.txt", "w") as file:

        for student in students:
            file.write(
                str(student["roll"]) + "," +
                student["name"] + "," +
                str(student["age"]) + "," +
                str(student["marks"]) + "\n"
            )

    print("Data saved successfully!")


# Main menu
while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Sort Students by Marks")
    print("6. Save Data")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        find_topper()

    elif choice == "5":
        sort_students()

    elif choice == "6":
        save_data()

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")