password = input("Enter new password: ")
confirmed = input("Confirm new password: ")

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


if password == confirmed and 8 < len(password) < 12 and password.lower() not in BAD_PASSWORDS:
    print("Password set successfull")
else: 
    print("Error occured during validation")
    
