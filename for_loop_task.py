students = []  

for i in range(2):
    print(f"\nEnter details for Student {i + 1}: ")

    student = {}

    student["id"] = int(input("Enter ID: "))
    student["name"] = input("Enter Name: ")
    student["address"] = input("Enter Address: ")

   
    qualification = {}
    qualification["course_name"] = input("Enter Qualification Name: ")
    qualification["passing_year"] = int(input("Enter Passing Year: "))
    student["qualification"] = qualification

    student["contact_no"] = int(input("Enter Contact Number: "))
    student["email"] = input("Enter Email ID: ")

   
    students.append(student)
    print(students)


print("\n------ All Student Registrations ------")
for i in range(2):
    print(f"\nStudent {i+1}: ")
    print("ID:", students[i]["id"])
    print("Name:", students[i]["name"].title())
    print("Address:", students[i]["address"].title())
    print("Qualification:", students[i]["qualification"]["course_name"].upper())
    print("Passing Year:", students[i]["qualification"]["passing_year"])
    print("Contact:", students[i]["contact_no"])
    print("Email:", students[i]["email"])
