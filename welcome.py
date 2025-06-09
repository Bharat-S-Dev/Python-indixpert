# Take User input and print result  
# Write a program to input student name and marks of 3 subjects. Print name and percentage in output.  

# Prompting the user for their name and 3 subject marks  
name = input("Enter your name: ") 
hindi_marks = input("Enter Hindi Marks: ") 
maths_marks = input("Enter Maths Marks: ") 
science_marks = input("Enter Science Marks: ")

# Calculating total marks percentage for 3 subjects 
total_marks = hindi_marks + maths_marks +science_marks
percentage = int(total_marks) / 3
# percentage = ((int(hindi_marks) + int(maths_marks) + int(science_marks))/300)*100 

# Printing the results 
print(f"{name}, have {percentage}%. Well done & keep working hard!!")