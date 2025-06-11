# Validate the user OTP

while True:
    otp = input("Please enter a 6-digit OTP: ")

    if len(otp) == 6 and otp.isdigit() and int(otp)>0:      #isdigit()	-Checks if all characters are numbers (0-9).
        print("OTP entered:", otp)                          #int(otp)>0	-Checks if all numbers shoud not be 0.
        break
    else:
        print("Invalid OTP. Please enter 6 digits OTP in numbers only.")
