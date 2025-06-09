print("----Choose a number 1-4")
print("\nPress 1 for Sum")
print("Press 2 for Subtraction")
print("Press 3 for Division")
print("Press 4 for Multiply")

print("*"*20)
num = int(input("Please select option: "))

num1 = int(input("Please select first number : "))
num2 = int(input("Please select second number: "))

if num ==1:
    print("You have selected Sum")
    print("Your Sum is:", num1 + num2)

elif num ==2:
    print("You have selected Subtraction")
    print("Your subtraction is:", num1 - num2)

elif num ==3:
    print("You have selected Multiply")
    print("Your Sum is:", num1 / num2)

elif num ==2:
    print("You have selected Division")
    print("Your subtraction is:", num1 * num2)


# ---------------------------------------------------
# calculator using character that is either smallcase or uppercase
print("Press A for Sum")
print("Press B for Subtraction")
print("Press C for Division")
print("Press D for Multiply")

num = input("Please select option: ").upper()

num1 = int(input("Please select first number : "))
num2 = int(input("Please select second number: "))

if num == "A":
    print("You have selected Sum")
    print("Your Sum is:", num1 + num2)

elif num =="B":
    print("You have selected Subtraction")
    print("Your subtraction is:", num1 - num2)

elif num =="C":
    print("You have selected Multiply")
    print("Your Sum is:", num1 / num2)

elif num =="D":
    print("You have selected Division")
    print("Your subtraction is:", num1 * num2)
else:
    print("you press a wrong character")