BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password = input("Enter new password: ")
    confirmed = input("Confirm new password: ") 

    if password == confirmed and 8 < len(password) < 12 and password.lower() not in BAD_PASSWORDS:
        print("Password set successfull")
        break
    else:
        print("Error in validating Enter again please ")
        continue