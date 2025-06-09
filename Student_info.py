students = []

student1 = {
    "id": int(input("Enter ID for Student 1: ")),
    "name": input("Enter Name for Student 1: "),
    "qualification": [
        {"Qual_name": input("Qualification Name 1: "), "passingYear": input("Year: ")},
        {"Qual_name": input("Qualification Name 2: "), "passingYear": input("Year: ")}
    ]
}
students.append(student1)

print("*"*40)

student2 = {
    "id": int(input("Enter ID for Student 2: ")),
    "name": input("Enter Name for Student 2: "),
    "qualification": [
        {"Qual_name": input("Qualification Name 1: "), "passingYear": input("Year: ")},
        {"Qual_name": input("Qualification Name 2: "), "passingYear": input("Year: ")}
    ]
}
students.append(student2)
print("*"*40)

print("All Students Data:")
print(students)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

students = [] 
student1 = {}

student1["id"] = int(input("Enter ID for Student 1: "))
student1["name"] = input("Enter Name for Student 1: ")

qual1 = [] #  list

q1 = {"Qual_name": input("Enter Qualification 1 Name: "), 
      "passingYear": input("Enter Passing Year: ")
      }

q2 = {"Qual_name": input("Enter Qualification 2 Name: "), 
      "passingYear": input("Enter Passing Year: ")
      }

qual1.append(q1)
qual1.append(q2)


student1["qualification"] = qual1
students.append(student1)

print("*"*40)
student2 = {}

student2["id"] = int(input("Enter ID for Student 2: "))
student2["name"] = input("Enter Name for Student 2: ")

qual2 = []

q4 = {"Qual_name": input("Enter Qualification 1 Name: "), 
      "passingYear": input("Enter Passing Year: ")
      }

q5 = {"Qual_name": input("Enter Qualification 2 Name: "), 
      "passingYear": input("Enter Passing Year: ")
      }


qual2.append(q4)
qual2.append(q5)


student2["qualification"] = qual2
students.append(student2)

print("*"*40)

print(" All Students Data:")
print(students)
