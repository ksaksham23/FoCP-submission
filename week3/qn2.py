password = input("Enter new password: ")
confirmed = input("Confirm new password")

if password == confirmed:
    print("Password set successfull")
else: 
    print("Error occured during validation")
    
