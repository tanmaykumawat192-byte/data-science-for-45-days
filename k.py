class StudentManagement:

    def __init__(self):
        self.students = {}

    def add_student(self):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        cgpa = float(input("Enter CGPA: "))
        sem = int(input("Enter Semester: "))

        self.students[roll_no] = {
            "name": name,
            "age": age,
            "course": course,
            "cgpa": cgpa,
            "sem": sem
        }

        print("Student Added Successfully!")

    def show_student(self):
        roll_no = input("Enter Roll No: ")

        if roll_no in self.students:
            print(self.students[roll_no])
        else:
            print("Student Not Found!")

    def update_student(self):
        roll_no = input("Enter Roll No to Update: ")

        if roll_no in self.students:
            self.students[roll_no]["name"] = input("Enter New Name: ")
            self.students[roll_no]["cgpa"] = float(input("Enter New CGPA: "))
            print("Record Updated!")
        else:
            print("Student Not Found!")

    def delete_student(self):
        roll_no = input("Enter Roll No to Delete: ")

        if roll_no in self.students:
            del self.students[roll_no]
            print("Student Deleted!")
        else:
            print("Student Not Found!")

    def show_all(self):
        for roll, data in self.students.items():
            print("\nRoll No:", roll)
            print("Name:", data["name"])
            print("Age:", data["age"])
            print("Course:", data["course"])
            print("CGPA:", data["cgpa"])
            print("Semester:", data["sem"])


obj = StudentManagement()

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        obj.add_student()

    elif choice == "2":
        obj.show_student()

    elif choice == "3":
        obj.update_student()

    elif choice == "4":
        obj.delete_student()

    elif choice == "5":
        obj.show_all()

    elif choice == "6":
        break

    else:
        print("Invalid Choice")