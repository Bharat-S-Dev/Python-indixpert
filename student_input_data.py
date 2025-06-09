# Student_input_Info 
student_input = []

student ={
"id" : int(input("Enter Student ID: ")),
"name" : input("Enter Student Name: "),
"address" : input("Please Enter the Address: "),

"marks" : [
    {"Hindi": int(input("Enter your Hindi Marks: "))},
    {"English": int(input("Enter your English Marks: "))},
    {"Math": int(input("Enter your Math Marks: "))},
    {"Science": int(input("Enter your Science Marks: "))}
    ]
}

student_input.append(student)

print("*"*40)
print(student_input)
print("*"*40)

#  Calculate Total_marks and Percentage:
hindi = student["marks"][0]["Hindi"]
english = student["marks"][1]["English"]
math = student["marks"][2]["Math"]
science = student["marks"][3]["Science"]

total_marks = hindi + english + math + science
percentage = total_marks / 4
CGPA = percentage / 9.5

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")
print("*"*30)

print("----Output-----")
print("your ID is: ", student["id"])
print("your name is: ", student["name"].title())
print("your Address is: ", student["address"].title())
print("your Percentage is: ", percentage)
print(f"CGPA of Student is: {CGPA}")


#----------------------------------------
marks = {}

hindi = int(input("plz enter Hindi marks: "))
english = int(input("plz enter English marks: "))
math = int(input("plz enter Math marks: "))

Marks = [{"hindi": hindi},{"english": english},{"math": math}]
print(Marks)

total_marks = (hindi + english + math)
percentage =total_marks / 3 
print("Total Marks: ",total_marks)
print("Percentage: ",percentage)