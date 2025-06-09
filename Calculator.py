first_no = int(input("Please Enter First Number: "))
Second_no = int(input("Please Enter Second Number: "))

Mini_Calculator = {
    "Sum": first_no + Second_no,
    "Subtraction": first_no - Second_no,
    "Multiplication": first_no * Second_no,
    "Division": first_no / Second_no
}

print("*" *30 )
print(Mini_Calculator)
print("*" *30 )



# method 2
# mini_cal = {}

# first_no = int(input("Please Enter First Number: "))
# Second_no = int(input("Please Enter Second Number: "))

# mini_cal["Sum"] = first_no + Second_no
# mini_cal["Subtraction"] = first_no - Second_no
# mini_cal["Multiplication"] = first_no * Second_no
# mini_cal["Division"] = first_no / Second_no

# print(mini_cal)

# cal_keys =Mini_Calculator.keys()
# print(cal_keys)
# cal_values = Mini_Calculator.values()
# print(cal_values)

# print(f"{cal_keys} : {cal_values}")
