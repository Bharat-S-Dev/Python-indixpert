Student_list = []

choice_of_students = int(input("How many students you want to Register(0-10): "))
# condition: number must be > 0 and <= 10

if 0 <choice_of_students <=10:
    for i in range(choice_of_students):
        print(f"\nEnter details of Student{i+1}:")

        student = {}

        student["id"] = int(input("please Enter Student Id: "))
        student["name"] = input("please Enter Student Name: ")
        student["address"] = input("please Enter Address: ")

        qualification = []
        total_qual = int(input("How many qualifications to enter: "))

        for q in range(total_qual):
            print(f" Qualifications {q+1}:")

            qual = {}
            qual["course_name"] = input("Enter Course Name: ")
            qual["passing_Year"] = int(input("Enter Passing Year: "))

            qualification.append(qual)

        student["qualification"] = qualification

        student["contact_No"] = input("Enter Student contact number: ")
        student["email_id"] = input("Enter student Email_Id: ")

        Student_list.append(student)
        print("*"*20)
        print(Student_list)

else:
    print("Please enter a number between 1 to 10")



# ------------------------------------------------------------
# method 2 - using while loop

Student_list = []

choice_of_students = int(input("How many students you want to Register(0-10): "))
# condition: number must be > 0 and <= 10

if 0 <choice_of_students <=10:
    for i in range(choice_of_students):
        print(f"\nEnter detais of Student{i+1}:")

        student = {}

        student["id"] = int(input("please Enter Student Id: "))
        student["name"] = input("please Enter Student Name: ")
        student["address"] = input("please Enter Address: ")

        qualification = []

        while True:
            sub_qual = {}
            decision = input("Do you want add qualifications(yes/ no):")
            if decision.lower() == "yes":
                sub_qual["course_name"] = input("Enter Course Name: ")
                sub_qual["passing_year"] = input("Enter passing year: ")
                qualification.append(sub_qual)
            else:
                break

            student["qualification"] = qualification

        student["contact_No"] = input("Enter Student contact number: ")
        student["email_id"] = input("Enter student Email_Id: ")

        Student_list.append(student)
        print("*"*20)
        print(Student_list)

else:
    print("Please enter a number between 1 to 10")