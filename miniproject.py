class studentsmanagement:
    def __init__(self, roll_no, cource, name, age, cgpa, sem):
        self.roll_no = roll_no
        self.cource = cource
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.sem = sem

    def display(self):
        print(f"Student Name -> {self.name}")
        print(f"Roll No      -> {self.roll_no}")
        print(f"Age          -> {self.age}")
        print(f"CGPA         -> {self.cgpa}")
        print(f"Course       -> {self.cource}")
        print(f"Semester     -> {self.sem}")


class office:
    def __init__(self):
        self.studentsmanagement = []

    def add_students(self):
        roll_no = int(input("Enter Roll No : "))
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        cource = input("Enter Course : ")
        cgpa = float(input("Enter CGPA : "))
        sem = int(input("Enter Semester : "))

        std = studentsmanagement(
            roll_no,
            cource,
            name,
            age,
            cgpa,
            sem
        )

        self.studentsmanagement.append(std)

        print("Student Added Successfully")

    def show_student(self):
        roll_no = int(input("Enter Roll No : "))

        for student in self.studentsmanagement:
            if student.roll_no == roll_no:
                student.display()
                return

        print("Student Not Found")

    def search_student(self):
        roll_no = int(input("Enter Roll No : "))

        for student in self.studentsmanagement:
            if student.roll_no == roll_no:
                print("Student Present")
                return

        print("Student Not Present")

    def update_student(self):
        roll_no = int(input("Enter Roll No To Update : "))

        for student in self.studentsmanagement:
            if student.roll_no == roll_no:

                student.name = input("Enter New Name : ")
                student.age = int(input("Enter New Age : "))
                student.cource = input("Enter New Course : ")
                student.cgpa = float(input("Enter New CGPA : "))
                student.sem = int(input("Enter New Semester : "))

                print("Student Updated Successfully")
                return

        print("Student Not Found")


obj = office()

while True:
    print("1. Add Student")
    print("2. Show Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        obj.add_students()

    elif choice == 2:
        obj.show_student()

    elif choice == 3:
        obj.search_student()

    elif choice == 4:
        obj.update_student()

    elif choice == 5:
        print("Exitt!!")
        break

    else:
        print("Invalid Choice")
            
